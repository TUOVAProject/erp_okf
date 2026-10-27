"""
Browsable HTML rendering of okf/. Reads the bundle emit_okf.py just wrote --
not the model -- so the site is the bundle, page for page, and cannot say
anything the markdown does not. No new traversal, no new counting: every
sentence, table and link on a page comes from the corresponding .md file.

Links are rewritten from .md to .html and stay file-relative, so the site
works opened straight from disk (file://) as well as served.
"""

import json
import re
import shutil
from html import escape
from pathlib import Path

import markdown
import yaml
from bs4 import BeautifulSoup, NavigableString

from .paths import OKF_DIR, OKF_HTML_DIR, OKF_HTML_TMP_DIR

SITE_ASSETS = Path(__file__).resolve().parent / "site_assets"

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

H1 = re.compile(r"^# (.+)$", re.MULTILINE)

# Relative hrefs to bundle files; absolute URLs and pure "#fragment" links are
# left alone.
MD_HREF = re.compile(r'href="(?![a-z]+:|#)([^"#]*?)\.md(#[^"]*)?"')

ENDPOINT = re.compile(r"^(GET|POST|PUT|PATCH|DELETE) (\S+)$")

MARKDOWN_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "toc"]

# Table columns whose cells are lists of entity links, shown as chips.
CHIP_COLUMNS = {"References", "Entities"}

# Index-entry descriptions that carry numbers worth drawing (root index module
# list and entities/index.md).
MODULE_COUNTS = re.compile(r"(\d+) queryable, (\d+) commands, (\d+) types")
PAGE_COUNT = re.compile(r"(\d+) pages")

# Numeric column drawn with a proportional bar (guides/core-entities.md).
BAR_COLUMN = "Referenced by"

# `npx serve okf-html` reads this. Its default cleanUrls redirects
# .../Sales/index.html to .../Sales (no trailing slash), which shifts the base
# directory and breaks every relative link on index pages.
SERVE_JSON = '{\n  "cleanUrls": false\n}\n'


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Frontmatter and body. Reserved files (index.md, log.md) have no
    frontmatter, so their title is derived from the first heading, as OKF
    allows a consumer to do when `title` is absent."""
    match = FRONTMATTER.match(text)
    fields, body = (yaml.safe_load(match.group(1)) or {}, text[match.end():]) if match else ({}, text)

    if "title" not in fields:
        heading = H1.search(body)
        if heading:
            fields["title"] = heading.group(1).strip()

    return fields, body


def html_path(md_relative: str) -> str:
    return md_relative[: -len(".md")] + ".html"


def new_tag(soup, name: str, text: str = "", **attrs):
    tag = soup.new_tag(name, attrs={k.rstrip("_"): v for k, v in attrs.items()})

    if text:
        tag.string = text

    return tag


def align_cells(soup) -> None:
    """The tables extension aligns with inline styles; the stylesheet uses .num."""
    for cell in soup.find_all(["th", "td"], style=True):
        if "right" in cell["style"]:
            cell["class"] = cell.get("class", []) + ["num"]

        del cell["style"]


def column_names(table) -> list[str]:
    return [th.get_text(strip=True) for th in table.find("thead").find_all("th")]


def stats_cards(soup) -> None:
    """A two-column table with a blank header (the root index's numbers) as cards."""
    for table in soup.find_all("table"):
        if any(column_names(table)) or len(column_names(table)) != 2:
            continue

        cards = new_tag(soup, "div", class_="stats")

        for row in table.find("tbody").find_all("tr"):
            label, value = row.find_all("td")
            card = new_tag(soup, "div", class_="stat")
            card.append(new_tag(soup, "span", value.get_text(strip=True), class_="stat-n"))
            card.append(new_tag(soup, "span", label.get_text(strip=True), class_="stat-l"))
            cards.append(card)

        table.replace_with(cards)


def endpoint_badge(soup, dd) -> None:
    code = dd.find("code")
    match = code and ENDPOINT.match(code.get_text())

    if not match:
        return

    method, path = match.groups()
    code.string = path
    code.insert_before(new_tag(soup, "span", method, class_=f"method {method.lower()}"))
    code.insert_before(" ")


def meta_list(soup) -> None:
    """The entity fact list ("- **Endpoint:** ...") as a <dl class="meta">."""
    for ul in soup.find_all("ul", recursive=False):
        if ul.find_previous_sibling("h2"):
            return

        items = ul.find_all("li", recursive=False)
        labels = [li.find("strong") for li in items]

        if not items or not all(
            label and label is li.contents[0] and label.get_text().endswith(":")
            for li, label in zip(items, labels)
        ):
            continue

        dl = new_tag(soup, "dl", class_="meta")

        for li, label in zip(items, labels):
            label.extract()
            dl.append(new_tag(soup, "dt", label.get_text()[:-1]))
            dd = new_tag(soup, "dd")

            for child in list(li.contents):
                dd.append(child.extract())

            if dd.contents and isinstance(dd.contents[0], NavigableString):
                dd.contents[0].replace_with(dd.contents[0].lstrip())

            endpoint_badge(soup, dd)
            dl.append(dd)

        ul.replace_with(dl)
        return


def to_chips(cell) -> None:
    links = cell.find_all("a")

    for link in links:
        link["class"] = ["chip"]

    cell.clear()

    for link in links:
        cell.append(link)


def bar_cells(soup, table, column: int) -> None:
    cells = [row.find_all("td")[column] for row in table.find("tbody").find_all("tr")]
    values = [int(cell.get_text(strip=True)) for cell in cells]
    widest = max(values) or 1

    for cell, value in zip(cells, values):
        cell.clear()
        bar_cell = new_tag(soup, "div", class_="barcell")
        bar = new_tag(soup, "div", class_="bar")
        bar.append(new_tag(soup, "span", style=f"width: {100 * value / widest:.1f}%"))
        bar_cell.append(bar)
        bar_cell.append(new_tag(soup, "span", str(value), class_="n"))
        cell.append(bar_cell)


def style_tables(soup) -> None:
    """Per-column classes, null badges, chips and deprecation marks."""
    for table in soup.find_all("table"):
        names = column_names(table)

        if names[:2] == ["Property", "Type"]:
            table["class"] = ["props"]

        if BAR_COLUMN in names:
            bar_cells(soup, table, names.index(BAR_COLUMN))

        for row in table.find("tbody").find_all("tr"):
            for name, cell in zip(names, row.find_all("td")):
                if name == "Property" and "props" in table.get("class", []):
                    cell["class"] = ["prop"]
                elif name == "Type" and "props" in table.get("class", []):
                    cell["class"] = ["type"]
                elif name == "Null":
                    nullable = cell.get_text(strip=True) == "yes"
                    cell.clear()
                    cell["class"] = ["nullable"]

                    if nullable:
                        cell.append(new_tag(soup, "span", "null", class_="badge"))
                elif name in CHIP_COLUMNS:
                    to_chips(cell)
                elif name == "Constraints":
                    strong = cell.find("strong")

                    if strong and strong.get_text().startswith("deprecated"):
                        strong.replace_with(new_tag(soup, "span", strong.get_text(), class_="badge dep"))
                        row["class"] = ["deprecated"]


def enum_chips(soup) -> None:
    """Under "Enumerations", each "### Name" + Name|Value table as one chip row."""
    heading = soup.find("h2", id="enumerations")

    if not heading:
        return

    enums = new_tag(soup, "ul", class_="enums")

    for h3 in heading.find_next_siblings():
        if h3.name == "h2":
            break

        if h3.name != "h3":
            continue

        table = h3.find_next_sibling("table")
        name, _, note = h3.get_text().partition(" (")
        item = new_tag(soup, "li")
        item.append(new_tag(soup, "code", name))

        if note:
            item.append(new_tag(soup, "span", note.rstrip(")"), class_="badge"))

        values = new_tag(soup, "div", class_="evs")

        for row in table.find("tbody").find_all("tr"):
            member, value = (cell.get_text(strip=True) for cell in row.find_all("td"))
            chip = new_tag(soup, "span", member, class_="ev")
            chip.append(new_tag(soup, "span", f"={value}"))
            values.append(chip)

        item.append(values)
        enums.append(item)
        table.extract()
        h3.extract()

    heading.insert_after(enums)


def composition(soup, counts: list[tuple[str, str]]):
    """Queryable/commands/types as a segmented bar plus a legend.

    Segment widths are the raw counts as flex-grow, so the browser does the
    proportions and this module never adds the numbers up."""
    wrap = new_tag(soup, "div", class_="comp")
    bar = new_tag(soup, "div", class_="comp-bar")
    legend = new_tag(soup, "div", class_="comp-legend")

    for kind, value in counts:
        if value != "0":
            bar.append(new_tag(soup, "span", class_=f"seg {kind}", style=f"flex-grow: {value}"))

        item = new_tag(soup, "span", class_=f"key {kind}" + (" zero" if value == "0" else ""))
        item.append(new_tag(soup, "b", value))
        item.append(f" {kind}")
        legend.append(item)

    wrap.append(bar)
    wrap.append(legend)

    return wrap


def card(soup, link, description: str):
    """One index entry as a card; the whole card is the link."""
    tile = new_tag(soup, "a", class_="card", href=link["href"])
    tile.append(new_tag(soup, "span", link.get_text(), class_="card-t"))
    counts = MODULE_COUNTS.fullmatch(description)
    pages = PAGE_COUNT.fullmatch(description)

    if counts:
        tile.append(composition(soup, list(zip(("queryable", "commands", "types"), counts.groups()))))
    elif pages:
        figure = new_tag(soup, "span", class_="card-n")
        figure.append(new_tag(soup, "b", pages.group(1)))
        figure.append(" pages")
        tile.append(figure)
    elif description:
        tile.append(new_tag(soup, "span", description, class_="card-d"))

    return tile


def index_cards(soup) -> None:
    """On index pages, link lists ("- [X](x.md) — note") and the modules table
    become card grids. Every value is the text of the item it replaces."""
    for ul in soup.find_all("ul", recursive=False):
        items = ul.find_all("li", recursive=False)
        entries = []

        for li in items:
            link = li.find("a")
            rest = "".join(str(node) for node in li.contents[1:]) if link is li.contents[0] else None

            if rest is None or not rest.startswith(" — "):
                break

            entries.append((link, rest[len(" — "):].strip()))

        if not items or len(entries) != len(items):
            continue

        grid = new_tag(soup, "div", class_="cards")

        for link, description in entries:
            grid.append(card(soup, link, description))

        ul.replace_with(grid)

    for table in soup.find_all("table"):
        if column_names(table) != ["Module", "Queryable", "Commands", "Types"]:
            continue

        grid = new_tag(soup, "div", class_="cards")

        for row in table.find("tbody").find_all("tr"):
            cells = row.find_all("td")
            numbers = ", ".join(
                f"{cell.get_text(strip=True)} {kind}"
                for cell, kind in zip(cells[1:], ("queryable", "commands", "types"))
            )
            grid.append(card(soup, cells[0].find("a"), numbers))

        table.replace_with(grid)


def wrap_tables(soup) -> None:
    for table in soup.find_all("table"):
        table.wrap(new_tag(soup, "div", class_="table-wrap"))


def render_content(body: str, is_index: bool = False) -> BeautifulSoup:
    html = markdown.markdown(body, extensions=MARKDOWN_EXTENSIONS, output_format="html")
    html = MD_HREF.sub(lambda m: f'href="{m.group(1)}.html{m.group(2) or ""}"', html)
    soup = BeautifulSoup(html, "html.parser")

    if is_index:
        index_cards(soup)

    align_cells(soup)
    stats_cards(soup)
    meta_list(soup)
    style_tables(soup)
    enum_chips(soup)
    wrap_tables(soup)

    return soup


def nav_link(label: str, target: str, page: str, root: str, count=None, current="page") -> str:
    attrs = f' aria-current="{current}"' if target == page or current == "location" else ""
    badge = f'<span class="count">{count}</span>' if count is not None else ""

    return f'<a href="{escape(root + target)}"{attrs}>{escape(label)}{badge}</a>'


def sidebar(nav: dict, page: str, module: str, root: str, soup) -> str:
    groups = [
        '<div class="nav-group">\n'
        + "\n".join(nav_link(label, target, page, root) for label, target in nav["start"])
        + "\n</div>",
        '<div class="nav-group"><h4>Guides</h4>\n'
        + "\n".join(nav_link(label, target, page, root) for label, target in nav["guides"])
        + "\n</div>",
        '<div class="nav-group"><h4>Modules</h4>\n'
        + "\n".join(
            nav_link(
                name,
                target,
                page,
                root,
                count,
                "location" if name == module and target != page else "page",
            )
            for name, target, count in nav["modules"]
        )
        + "\n</div>",
    ]

    toc = [
        f'<a class="toc-{"h" if h.name == "h2" else "i"}" href="#{h["id"]}">'
        f"{escape(h.get_text())}</a>"
        for h in soup.find_all(["h2", "h3"])
        if h.get("id")
    ]

    if toc:
        groups.append('<div class="nav-group toc"><h4>On this page</h4>\n' + "\n".join(toc) + "\n</div>")

    return (
        '<nav class="side" id="side">\n'
        '  <input type="search" id="search" placeholder="Search all entities  ( / )" '
        'aria-label="Search all entities" autocomplete="off">\n'
        '  <div id="results" hidden></div>\n'
        '  <div id="nav">\n' + "\n".join(groups) + "\n  </div>\n</nav>"
    )


def crumb(fields: dict, module: str, root: str, site_title: str) -> str:
    title = escape(fields.get("title", ""))

    if title == escape(site_title):
        return "Overview"

    if not module:
        return title

    return (
        f'<a href="{root}modules/{escape(module)}.html">{escape(module)}</a>'
        f'<span class="sep">/</span>{title}'
    )


def page_meta(fields: dict) -> str:
    parts = []

    if fields.get("resource"):
        url = escape(fields["resource"])
        parts.append(f'Source: <a href="{url}">{url}</a>')

    if fields.get("tags"):
        parts.append("".join(f'<span class="badge">{escape(str(tag))}</span>' for tag in fields["tags"]))

    if not parts:
        return ""

    return '<div class="page-meta">' + "<br>".join(parts) + "</div>"


def render_page(relative: str, fields: dict, body: str, nav: dict) -> str:
    page = html_path(relative)
    root = "../" * page.count("/")
    module = fields.get("module", "") if relative.startswith("entities/") else ""
    title = fields.get("title", "")
    full_title = title if title == nav["title"] else f"{title} · {nav['title']}"
    description = fields.get("description", "")
    soup = render_content(body, is_index=relative.endswith("index.md"))

    return (
        "<!doctype html>\n"
        '<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{escape(full_title)}</title>\n"
        + (f'<meta name="description" content="{escape(description)}">\n' if description else "")
        + f'<link rel="stylesheet" href="{root}assets/okf.css">\n'
        "</head>\n<body>\n"
        '<header class="top">\n'
        '  <button class="menu" id="menu" aria-label="Toggle navigation">☰</button>\n'
        f'  <a class="brand" href="{root}index.html">{escape(nav["title"])}</a>\n'
        f'  <span class="crumb">{crumb(fields, module, root, nav["title"])}</span>\n'
        "</header>\n"
        '<div class="layout">\n'
        f"{sidebar(nav, page, module, root, soup)}\n"
        f'<main class="content">\n{soup}\n{page_meta(fields)}\n</main>\n'
        "</div>\n"
        f'<script>window.OKF_ROOT = "{root}";</script>\n'
        f'<script src="{root}assets/okf-index.js"></script>\n'
        f'<script src="{root}assets/okf.js"></script>\n'
        "</body>\n</html>\n"
    )


def load_bundle() -> dict:
    """Every okf/ markdown file as {relative posix path: (frontmatter, body)}."""
    pages = {}

    for path in sorted(OKF_DIR.rglob("*.md")):
        relative = path.relative_to(OKF_DIR).as_posix()
        pages[relative] = split_frontmatter(path.read_text(encoding="utf-8"))

    return pages


def build_nav(pages: dict) -> dict:
    """Sidebar sections from the bundle's own files, in a stable order.

    Guides keep the order guides/index.md lists them in, since that ordering
    is an editorial choice made by emit_okf.py. Module counts are the
    entity_count each module file already declares in its frontmatter.
    """
    guide_index = pages["guides/index.md"][1]
    guide_files = re.findall(r"\]\(([^)#]+\.md)\)", guide_index)

    return {
        "title": pages["index.md"][0]["title"],
        "start": [
            ("Overview", "index.html"),
            ("About this bundle", "about.html"),
            ("All modules", "modules/index.html"),
            ("All entities", "entities/index.html"),
            ("Generation log", "log.html"),
        ],
        "guides": [
            (pages[f"guides/{name}"][0]["title"], html_path(f"guides/{name}"))
            for name in guide_files
            if f"guides/{name}" in pages
        ],
        "modules": [
            (fields["title"], html_path(relative), fields.get("entity_count"))
            for relative, (fields, _) in pages.items()
            if relative.startswith("modules/") and relative != "modules/index.md"
        ],
    }


def search_index(pages: dict) -> str:
    entries = [
        {
            "t": fields.get("title", ""),
            "id": f"{fields.get('module', '')}.{fields.get('api_class', '')}",
            "k": fields.get("type", "").removeprefix("API "),
            "d": fields.get("description", ""),
            "m": fields.get("module", ""),
            "p": html_path(relative),
        }
        for relative, (fields, _) in pages.items()
        if relative.startswith("entities/") and not relative.endswith("/index.md")
    ]

    return f"window.OKF_INDEX = {json.dumps(entries, ensure_ascii=False)};\n"


def write(relative: str, content: str) -> None:
    path = OKF_HTML_TMP_DIR / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_all() -> None:
    """Write the whole site into OKF_HTML_TMP_DIR."""
    pages = load_bundle()
    nav = build_nav(pages)

    for relative, (fields, body) in pages.items():
        write(html_path(relative), render_page(relative, fields, body, nav))

    for asset in sorted(SITE_ASSETS.iterdir()):
        write(f"assets/{asset.name}", asset.read_text(encoding="utf-8"))

    write("assets/okf-index.js", search_index(pages))
    write("serve.json", SERVE_JSON)


def emit(model: dict) -> None:
    """Render okf/ to okf-html/ via a staging directory, then swap it in.

    model is accepted for symmetry with the other emitters but not read: the
    input is the bundle on disk, so emit_okf.emit() must run first.
    """
    if OKF_HTML_TMP_DIR.exists():
        shutil.rmtree(OKF_HTML_TMP_DIR)

    OKF_HTML_TMP_DIR.mkdir(parents=True)

    render_all()

    if OKF_HTML_DIR.exists():
        shutil.rmtree(OKF_HTML_DIR)

    OKF_HTML_TMP_DIR.rename(OKF_HTML_DIR)
