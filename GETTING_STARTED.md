# Getting started

This guide takes you from a fresh download to a working setup, in order. Steps 1–2
are all most people need. The rest is only for writing code against the model or
rebuilding the bundle yourself.

| I want to… | Do steps | Install anything? |
| --- | --- | --- |
| Read the docs, or point an AI agent at them | 1, 2 | No |
| Query the model from my own code | 1, 3, 4 | Python |
| Refresh from upstream or change the pipeline | 1, 3, 5, 6 | Python |

## What this gives you, and what it does not

The repo turns the public Monitor ERP API documentation (<https://api.monitor.se/api/>)
into a description of the API's **data model**: every queryable resource, its
fields, enumerations, required permission, and how resources link to each other.

It tells you *which resource and which field* holds the data you need. Two
things are left out on purpose: the 913 write-operation (command) pages, and
Monitor's [Developer Guide](https://api.monitor.se/articles/v1/index.html), which
covers authentication, URL format, query options and examples. Use the Developer
Guide alongside this bundle when you make actual API calls.

## 1. Get the repo

```bash
git clone https://github.com/TUOVAProject/erp_okf.git
cd erp_okf
```

Or download the ZIP from GitHub (**Code → Download ZIP**) and extract it. The
download is about 10–20 MB. Everything needed for reading is already built and
committed.

## 2. Use the bundle

There are three ready-made outputs, all generated from the same model. Pick the
one that fits how you work.

### Read it as markdown: `okf/`

Open [`okf/index.md`](okf/index.md). It is plain markdown with working relative
links, so GitHub, VS Code, or any editor renders it.

Suggested reading order:

1. [`okf/about.md`](okf/about.md): scope and headline numbers.
2. [`okf/guides/core-entities.md`](okf/guides/core-entities.md): the 20 entities
   most of the model hangs off. Start here.
3. [`okf/guides/relationships.md`](okf/guides/relationships.md): foreign keys vs.
   navigation properties, the one concept you need to follow links.
4. `okf/entities/<Module>/<Class>.md`: one page per resource, for example
   [`okf/entities/Sales/CustomerOrder.md`](okf/entities/Sales/CustomerOrder.md).

Each entity page lists its endpoint, permission, full property table,
enumerations, a JSON example, and a **Referenced by** section. Every reference is
a link, so you can walk the graph in both directions.

`okf/` is an [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)
bundle. Any OKF-aware tool can consume it directly.

### Browse it in a browser: `okf-html/`

Open `okf-html/index.html` directly from disk. No server is needed. It is the
same content page for page, with a sidebar, entity search (press `/`), and a row
filter on long property tables.

To serve it over HTTP instead:

```bash
npx serve okf-html
```

`okf-html/serve.json` turns off `serve`'s clean-URL redirects, which would
otherwise break relative links on index pages. Keep it.

### Give it to an AI agent

Use the variant that matches what your agent can load.

**`okf/`: agents that can open files on demand.** This includes coding agents
working inside the repo, such as Claude Code, GitHub Copilot in VS Code, and
Cursor. The bundle is built so that answering a question takes opening two or
three files, not loading everything. Point the agent at the bundle and its entry
point. For example, put this in your agent instructions (`CLAUDE.md`,
`.github/copilot-instructions.md`, or similar):

```markdown
The Monitor ERP API data model is documented in `okf/`.
Start at `okf/index.md`, then `okf/guides/core-entities.md`.
Each entity is `okf/entities/<Module>/<Class>.md`; follow its links for related entities.
Only state what these files say. If they do not cover something, say so instead
of guessing.
```

**`okf-compact/`: agents with a cap on attached files.** This includes custom or
hosted agents where you upload a fixed set of knowledge files. It holds the same
model in 14 files: one per module, each containing every entity in that module,
plus guides and an index. Upload the whole `okf-compact/` directory. To fit,
it drops the JSON examples, the per-member enum tables, and the per-property
constraint flags.

Example questions either variant answers:

- *Which entity holds customer orders, and how does it link to payment terms?*
- *What references `Common.Currency`?*
- *Which permission does the `Parts` endpoint require?*

## 3. Install Python (for steps 4–6 only)

You need **Python 3.10 or newer**. The pipeline is tested with 3.11.

**Linux, macOS and WSL:**

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

**Windows (PowerShell):**

```powershell
py -3 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

The commands in the rest of this guide use the Linux form `.venv/bin/python`. On
Windows, write `.venv\Scripts\python` instead.

The build is verified on Linux and WSL only. Native Windows may write different
line endings, which makes `check.py` report the output as stale. Use WSL if you
plan to rebuild.

Dependencies are pinned in `requirements.txt`: `requests`, `beautifulsoup4`,
`PyYAML`, `Markdown`.

## 4. Query the model from code

`build/model.json` holds the whole model as one JSON file. It is not committed,
so build it once:

```bash
.venv/bin/python build.py
```

This takes a few seconds and runs offline. It reads the committed `html/` cache
and never touches the network. It also regenerates `okf/`, `okf-html/`, and
`okf-compact/`, which come out byte-identical to what you downloaded.

The shape of the file:

- `entities` is keyed by `"<Module>.<ApiClass>"`, for example `"Sales.CustomerOrder"`.
- Each entity has `title`, `endpoint`, `required_permission`, `properties`,
  `references_out`, and `referenced_by`.
- `relationships` is the flat edge list. Each edge has `source`, `target`,
  `property`, and `kind` (`foreign_key` or `navigation`).

```python
import json

with open("build/model.json", encoding="utf-8") as f:
    model = json.load(f)

order = model["entities"]["Sales.CustomerOrder"]
print(order["endpoint"]["method"], order["endpoint"]["path"])  # GET /api/v1/Sales/CustomerOrders

for ref in order["references_out"][:5]:
    print(ref["property"], "->", ref["target"], f"({ref['kind']})")

# Everything that points at Currency
for edge in model["relationships"]:
    if edge["target"] == "Common.Currency":
        print(edge["source"], edge["property"])
```

## 5. Verify a build

```bash
.venv/bin/python check.py
```

All checks should print `PASS`. The checks cover the following:

- Parser fixtures still read real pages correctly.
- Two builds produce identical output, and that output matches the committed files.
- Extraction has not shrunk below the recorded baseline.
- Every link resolves.
- There is no broken character encoding.
- The HTML site is up to date.

Run it after any change.

## 6. Refresh from upstream

The `html/` folder is a cache of the scraped documentation pages, and a normal
build never updates it. To pick up changes Monitor has made to its
documentation:

```bash
.venv/bin/python build.py --scrape    # fetch only pages missing from the cache
.venv/bin/python build.py --refresh   # re-fetch every page
.venv/bin/python check.py
git diff --stat
```

A full refresh downloads roughly 380 pages and takes a few minutes, because it
pauses between requests. Read the diff before you commit it. It is the record of
what changed upstream. `okf/log.md` is dated from the last time a cached page
actually changed, so a refresh that finds nothing new changes nothing.

### When the build fails

The build stops with a non-zero exit instead of producing incomplete output.
Common causes:

| Message | Meaning | What to do |
| --- | --- | --- |
| `unclassified property bullets` | Upstream added a new kind of property annotation | Add the pattern to `classify_bullets` in `monitor_api/parse.py` |
| `baseline: … fell to …` | Extraction got smaller | If upstream really removed pages, regenerate `baseline.json` as a reviewed commit. Otherwise a parser rule broke. |
| `references unknown page` | A link points at a page not in the cache | Run `build.py --scrape` |
| `mojibake` | A cached page was decoded with the wrong encoding | Run `build.py --refresh`. Do not hand-edit the cache. |
| no `fetched_on` date | `endpoint_index.json` predates date tracking | Run `build.py --scrape` |

Do not loosen these checks to make a build pass. They exist so that a change in
the source documentation is noticed instead of silently dropping data. The
developer reference for the pipeline is in [`README.md`](README.md).

## Licence

The code is MIT licensed. The contents of `html/`, `okf/`, `okf-html/`, and
`okf-compact/` are derived from documentation owned by Monitor ERP System AB. See
[`LICENSE`](LICENSE) before redistributing them.
