"""Verify the pipeline and the bundle it produced.

    .venv/bin/python check.py

No test framework: plain assertions, one function per check, non-zero exit if
any of them fails. That matches the rest of the repo -- flat procedural modules
with a main() guard -- and means verification needs no dependency that building
does not already need.

Run this after any change to monitor_api/. The build's own validate() checks
that the *model* is sound; these checks cover the things it cannot see: that the
parser still reads real pages the same way, that output is reproducible, that
extraction has not quietly shrunk, and that the bundle's links actually resolve.
"""

import json
import re
import shutil
import sys

import yaml

from monitor_api import emit_compact, emit_html, emit_okf
from monitor_api.model import build
from monitor_api.paths import (
    BASELINE_JSON,
    HTML_DIR,
    OKF_COMPACT_DIR,
    OKF_DIR,
    OKF_HTML_DIR,
    REPO_ROOT,
)
from monitor_api.parse import parse_page

# Pages chosen to pin down a specific parser behaviour each. If one of these
# assertions fails, the named rule in CLAUDE.md has been broken.
FIXTURES = [
    {
        "path": "Sales/CustomerOrder.html",
        "why": "unrendered <see cref> must still yield a foreign key",
        "kind": "entity",
        "endpoint_path": "/api/v1/Sales/CustomerOrders",
        "min_properties": 100,
    },
    {
        "path": "Common/Money.html",
        "why": "a Type page has no endpoint; its first <pre> is the JSON example",
        "kind": "type",
        "endpoint_path": None,
        "min_properties": 2,
    },
    {
        "path": "Sales/CreateSalesPickingList.html",
        "why": "a command page is POST and its table is a request body",
        "kind": "command",
        "endpoint_path": "/api/v1/Sales/SalesPickingLists/Create",
        "min_properties": 1,
    },
    {
        "path": "Common/PaymentTerm.html",
        "why": "enum members come from <li>, never from prose",
        "kind": "entity",
        "endpoint_path": "/api/v1/Common/PaymentTerms",
        "min_properties": 10,
    },
]

LINK_PATTERN = re.compile(r"\]\(([^)\s]+)\)")
HTML_LINK_PATTERN = re.compile(r'(?:href|src)="([^"]+)"')


def check_fixtures():
    """The parser still reads known pages the way it is documented to."""
    for fixture in FIXTURES:
        path = HTML_DIR / fixture["path"]
        assert path.exists(), f"fixture page missing: {path}"

        page = parse_page(path)
        label = f"{fixture['path']} ({fixture['why']})"

        assert page["kind"] == fixture["kind"], (
            f"{label}: kind is {page['kind']!r}, expected {fixture['kind']!r}"
        )

        if fixture["endpoint_path"] is None:
            assert page["endpoint"] is None, f"{label}: expected no endpoint"
        else:
            assert page["endpoint"], f"{label}: endpoint was not parsed"
            assert page["endpoint"]["url"].endswith(fixture["endpoint_path"]), (
                f"{label}: endpoint {page['endpoint']['url']!r} does not end with "
                f"{fixture['endpoint_path']!r}"
            )

        assert len(page["properties"]) >= fixture["min_properties"], (
            f"{label}: {len(page['properties'])} properties, expected at least "
            f"{fixture['min_properties']}"
        )

    # The specific edge that unrendered docfx crefs used to lose entirely.
    model = build()
    order = model["entities"]["Sales.CustomerOrder"]
    payment_method = next(p for p in order["properties"] if p["name"] == "PaymentMethodId")

    assert any(ref["target"] == "Common.PaymentMethod" for ref in payment_method["references"]), (
        "Sales.CustomerOrder.PaymentMethodId lost its reference to Common.PaymentMethod "
        "-- the <see cref> resolver has regressed"
    )


def check_determinism():
    """Same input, same bytes out. Without this the bundle's diff is noise."""
    first, second = build(), build()

    assert first == second, "two builds of the same input produced different models"
    assert first["source_digest"] == second["source_digest"], "source digest is unstable"

    staging = REPO_ROOT / "okf.check.tmp"

    if staging.exists():
        shutil.rmtree(staging)

    try:
        original_dir = emit_okf.OKF_TMP_DIR
        emit_okf.OKF_TMP_DIR = staging
        emit_okf.emit_root(first)
        emit_okf.emit_guides(first)
        rendered = {
            path.relative_to(staging): path.read_bytes() for path in staging.rglob("*.md")
        }
    finally:
        emit_okf.OKF_TMP_DIR = original_dir
        shutil.rmtree(staging, ignore_errors=True)

    assert rendered, "emitting produced no files"

    for relative, content in rendered.items():
        committed = OKF_DIR / relative
        assert committed.exists(), f"{relative} was emitted but is not in okf/"
        assert committed.read_bytes() == content, (
            f"okf/{relative} differs from a fresh emit -- okf/ is stale, re-run build.py"
        )

    # okf-compact/ is only ~14 files, cheap enough to re-emit and diff in full
    # (unlike okf/'s check above, which only covers emit_root + emit_guides).
    compact_staging = REPO_ROOT / "okf-compact.check.tmp"

    if compact_staging.exists():
        shutil.rmtree(compact_staging)

    try:
        original_compact_dir = emit_compact.OKF_COMPACT_TMP_DIR
        emit_compact.OKF_COMPACT_TMP_DIR = compact_staging
        emit_compact.emit_root(first)
        emit_compact.emit_guides(first)
        emit_compact.emit_modules(first)
        rendered_compact = {
            path.relative_to(compact_staging): path.read_bytes()
            for path in compact_staging.rglob("*.md")
        }
    finally:
        emit_compact.OKF_COMPACT_TMP_DIR = original_compact_dir
        shutil.rmtree(compact_staging, ignore_errors=True)

    assert rendered_compact, "emitting the compact bundle produced no files"

    for relative, content in rendered_compact.items():
        committed = OKF_COMPACT_DIR / relative
        assert committed.exists(), f"okf-compact/{relative} was emitted but is not committed"
        assert committed.read_bytes() == content, (
            f"okf-compact/{relative} differs from a fresh emit -- "
            "okf-compact/ is stale, re-run build.py"
        )


def check_html_fresh():
    """okf-html/ is exactly what rendering the committed okf/ produces now."""
    staging = REPO_ROOT / "okf-html.check.tmp"

    if staging.exists():
        shutil.rmtree(staging)

    try:
        original_dir = emit_html.OKF_HTML_TMP_DIR
        emit_html.OKF_HTML_TMP_DIR = staging
        emit_html.render_all()
        rendered = {
            path.relative_to(staging): path.read_bytes()
            for path in staging.rglob("*")
            if path.is_file()
        }
    finally:
        emit_html.OKF_HTML_TMP_DIR = original_dir
        shutil.rmtree(staging, ignore_errors=True)

    committed = {
        path.relative_to(OKF_HTML_DIR) for path in OKF_HTML_DIR.rglob("*") if path.is_file()
    }

    assert rendered, "rendering produced no files"
    assert committed == set(rendered), (
        f"okf-html/ has {len(committed ^ set(rendered))} files that a fresh render "
        "does not (or vice versa) -- re-run build.py"
    )

    for relative, content in rendered.items():
        assert (OKF_HTML_DIR / relative).read_bytes() == content, (
            f"okf-html/{relative} differs from a fresh render -- okf-html/ is stale, "
            "re-run build.py"
        )


def check_html_links():
    """Every relative href/src in okf-html/ resolves, including its anchor."""
    broken = []
    texts = {}

    def text(path):
        if path not in texts:
            texts[path] = path.read_text(encoding="utf-8")
        return texts[path]

    for path in sorted(OKF_HTML_DIR.rglob("*.html")):
        for target in HTML_LINK_PATTERN.findall(text(path)):
            if re.match(r"[a-z]+:", target):
                continue

            file_part, _, fragment = target.partition("#")
            resolved = (path.parent / file_part).resolve() if file_part else path

            if not resolved.exists():
                broken.append(f"{path.relative_to(OKF_HTML_DIR)} -> {target} (missing file)")
            elif fragment and f'id="{fragment}"' not in text(resolved):
                broken.append(f"{path.relative_to(OKF_HTML_DIR)} -> {target} (missing anchor)")

    assert not broken, f"{len(broken)} broken HTML links, e.g. " + "; ".join(broken[:5])


def check_baseline():
    """Extraction has not shrunk since the recorded floor."""
    assert BASELINE_JSON.exists(), "baseline.json is missing"

    baseline = json.loads(BASELINE_JSON.read_text(encoding="utf-8"))["stats"]
    stats = build()["stats"]

    for name, recorded in sorted(baseline.items()):
        assert name in stats, f"stat {name!r} is no longer produced"
        assert stats[name] >= recorded * 0.95, (
            f"{name} fell to {stats[name]}, below 95% of the recorded {recorded}"
        )


def check_links():
    """Every link resolves to a file that exists, relative to the file it's in.

    Relationships in this bundle *are* the links, so a broken one is a broken
    fact, not a cosmetic problem. Links are file-relative (e.g. "../Common/X.md")
    so they work when the bundle is browsed as a plain directory -- GitHub, an
    editor, a file manager -- not only when something serves okf/ as a web root.
    """
    broken = []

    for path in sorted(OKF_DIR.rglob("*.md")):
        for target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue

            file_part, _, _ = target.partition("#")

            if file_part and not (path.parent / file_part).resolve().exists():
                broken.append(f"{path.relative_to(OKF_DIR)} -> {target}")

    assert not broken, f"{len(broken)} broken links, e.g. " + "; ".join(broken[:5])


def check_compact_links():
    """Every okf-compact/ link resolves, including its in-file anchor.

    Compact links carry a '#entity-key' fragment instead of pointing at a
    separate per-entity file, so the file part and the anchor must both be
    verified -- a broken in-module reference would otherwise pass silently.
    Links are file-relative, same as check_links().
    """
    broken = []
    anchors_by_file = {}

    for path in sorted(OKF_COMPACT_DIR.rglob("*.md")):
        for target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue

            file_part, _, fragment = target.partition("#")
            resolved = (path.parent / file_part).resolve() if file_part else path

            if not resolved.exists():
                broken.append(f"{path.relative_to(OKF_COMPACT_DIR)} -> {target} (missing file)")
                continue

            if not fragment:
                continue

            if resolved not in anchors_by_file:
                anchors_by_file[resolved] = resolved.read_text(encoding="utf-8")

            if f'id="{fragment}"' not in anchors_by_file[resolved]:
                broken.append(f"{path.relative_to(OKF_COMPACT_DIR)} -> {target} (missing anchor)")

    assert not broken, f"{len(broken)} broken compact links, e.g. " + "; ".join(broken[:5])


def check_compact_structure():
    """okf-compact/ stays inside the ~50-file agent context budget, and every
    entity the model knows about actually made it into its module file."""
    files = sorted(OKF_COMPACT_DIR.rglob("*.md"))
    assert len(files) <= 50, f"{len(files)} files in okf-compact/, exceeds the 50-file agent budget"

    model = build()

    for name, module in model["modules"].items():
        text = (OKF_COMPACT_DIR / "modules" / f"{name}.md").read_text(encoding="utf-8")
        for key in module["entities"]:
            assert f'id="{key}"' in text, f"{key} is missing from okf-compact/modules/{name}.md"


def _mojibake_files(root):
    """UTF-8-decoded-as-latin-1 corruption never occurs in real prose, so any
    C1 control character in a markdown file is proof of a decoding error."""
    return [
        str(path.relative_to(root))
        for path in sorted(root.rglob("*.md"))
        if re.search(r"[\x80-\x9f]", path.read_text(encoding="utf-8"))
    ]


def check_encoding():
    """No UTF-8-decoded-as-latin-1 corruption anywhere in the bundle."""
    mangled = _mojibake_files(OKF_DIR)

    assert not mangled, f"{len(mangled)} files contain mojibake, e.g. {mangled[:3]}"


def check_compact_encoding():
    """Same mojibake scan as check_encoding, applied to okf-compact/."""
    mangled = _mojibake_files(OKF_COMPACT_DIR)

    assert not mangled, f"{len(mangled)} compact files contain mojibake, e.g. {mangled[:3]}"


def check_okf_conformance():
    """The three OKF v0.2 conformance rules, plus the reserved-file structure.

    Every non-reserved file has parseable frontmatter with a non-empty `type`;
    index.md and log.md have none, except okf_version on the root index.md;
    log.md headings are YYYY-MM-DD, newest first.
    """
    frontmatter = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
    problems = []

    for path in sorted(OKF_DIR.rglob("*.md")):
        relative = path.relative_to(OKF_DIR).as_posix()
        text = path.read_text(encoding="utf-8")
        match = frontmatter.match(text)

        if path.name in ("index.md", "log.md"):
            allowed = {"okf_version"} if relative == "index.md" else set()
            fields = set(yaml.safe_load(match.group(1)) or {}) if match else set()
            if fields - allowed:
                problems.append(f"{relative}: reserved file carries frontmatter {sorted(fields - allowed)}")
            continue

        fields = yaml.safe_load(match.group(1)) if match else None
        if not isinstance(fields, dict) or not fields.get("type"):
            problems.append(f"{relative}: no frontmatter with a non-empty type")

    root = frontmatter.match((OKF_DIR / "index.md").read_text(encoding="utf-8"))
    assert root and yaml.safe_load(root.group(1)).get("okf_version") == emit_okf.OKF_VERSION, (
        "root index.md does not declare okf_version"
    )

    dates = re.findall(r"^## (.+)$", (OKF_DIR / "log.md").read_text(encoding="utf-8"), re.MULTILINE)
    if not dates or not all(re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) for d in dates):
        problems.append(f"log.md: headings are not YYYY-MM-DD dates: {dates}")
    elif dates != sorted(dates, reverse=True):
        problems.append("log.md: dates are not newest first")

    assert not problems, f"{len(problems)} problems, e.g. {problems[:3]}"


CHECKS = [
    ("parser fixtures", check_fixtures),
    ("deterministic output", check_determinism),
    ("baseline floor", check_baseline),
    ("okf conformance", check_okf_conformance),
    ("link integrity", check_links),
    ("character encoding", check_encoding),
    ("compact bundle structure", check_compact_structure),
    ("compact bundle links", check_compact_links),
    ("compact bundle encoding", check_compact_encoding),
    ("html site freshness", check_html_fresh),
    ("html site links", check_html_links),
]


def main():
    if not all(d.exists() for d in (OKF_DIR, OKF_COMPACT_DIR, OKF_HTML_DIR)):
        sys.exit("No bundle to check. Run: python build.py")

    failures = 0

    for name, check in CHECKS:
        try:
            check()
        except AssertionError as error:
            failures += 1
            print(f"FAIL  {name}\n        {error}")
        except Exception as error:
            failures += 1
            print(f"ERROR {name}\n        {type(error).__name__}: {error}")
        else:
            print(f"PASS  {name}")

    if failures:
        sys.exit(f"\n{failures} of {len(CHECKS)} checks failed.")

    print(f"\nAll {len(CHECKS)} checks passed.")


if __name__ == "__main__":
    main()
