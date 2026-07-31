# Monitor ERP API — knowledge bundle

## Lyhyesti

Monitor ERP:n julkinen API-dokumentaatio muunnettuna luettavaksi tietomalliksi:
jokainen kyseltävä resurssi, sen kentät, enumeraatiot, oikeusvaatimus ja suhteet
muihin resursseihin. Tarkoitettu sekä ihmisen selattavaksi että AI-agentin
luettavaksi.

**Haluatko vain lukea?** Avaa [`okf/index.md`](okf/index.md). Mitään ei tarvitse asentaa.

---

## What this is

A scrape-and-transform pipeline that turns the public Monitor ERP API
documentation at <https://api.monitor.se/api/> into a **knowledge bundle**: a
directory of markdown files describing the API's data model, where every
relationship between entities is a real link you can follow.

It is not an application and not an API client. It answers *which resource holds
this data, what are its fields, and what does it connect to* — the questions you
have to answer before you can write an integration.

## I just want to read the docs

Open **[`okf/index.md`](okf/index.md)**. Nothing to install, no build step. It is
plain markdown, so GitHub renders it and any editor opens it.

From there: [`okf/guides/`](okf/guides/) explains how the API is shaped,
[`okf/modules/`](okf/modules/) lists the eight modules, and
`okf/entities/<Module>/<Class>.md` is one page per resource.

Pointing an AI agent at this repo works the same way — the bundle is designed so
an agent can answer a question by opening two or three files rather than loading
everything.

## I want to query it in code

Run the build (below) to produce **`build/model.json`** — the whole model as one
JSON file:

```jsonc
{
  "entities": {                  // keyed by "<Module>.<ApiClass>"
    "Sales.CustomerOrder": {
      "title": "CustomerOrders",
      "endpoint": { "method": "GET", "path": "/api/v1/Sales/CustomerOrders" },
      "properties": [ ... ],
      "references_out": [ ... ],
      "referenced_by": [ ... ]
    }
  },
  "relationships": [ ... ],      // flat edge list
  "modules":       { ... },
  "stats":         { ... }
}
```

`build/` is not committed — it is fully derived and regenerates in seconds.

## Quickstart

```bash
git clone <this repo>
cd "MonitorApi Documentation"

python3.11 -m venv .venv
.venv/bin/pip install -r requirements.txt

.venv/bin/python build.py     # offline, a few seconds
.venv/bin/python check.py     # verify the build
```

The default build is **offline and deterministic**: it reads the committed
`html/` cache and never touches the network. Running it twice produces
byte-identical output.

## What's in the repo

| Path | |
|---|---|
| `okf/` | **The deliverable.** The knowledge bundle — 405 markdown files. Committed. |
| `build/model.json` | The same model as one JSON file, for code. Generated, not committed. |
| `html/` | Cache of the scraped documentation pages. Committed, so builds are reproducible offline. |
| `endpoint_index.json` | Crawl manifest: what was found and what was deliberately skipped. |
| `baseline.json` | Recorded stats floor. The build fails if extraction drops below it. |
| `build.py` | The only entry point. |
| `check.py` | Verification suite — run after any change. |
| `monitor_api/` | The pipeline: `scrape` → `parse` → `model` → `emit_json` / `emit_okf`. |

## How it works

```
api.monitor.se ──scrape.py──▶ html/ ──parse.py──▶ raw page dicts
                                                        │
                                                     model.py          normalise, resolve
                                                        │              references, build the
                                                        ▼              graph, validate
                                        ┌───────────────┴───────────────┐
                                  emit_json.py                     emit_okf.py
                                        │                               │
                                  build/model.json                    okf/
```

1. **`scrape.py`** crawls from `toc.html`, writes `html/<Module>/<Class>.html`.
2. **`parse.py`** turns docfx HTML into raw dicts. It reads structure, not prose:
   a relative `Monitor.API.<Module>.<Class>.html` href is an exact entity
   pointer, and per-property facts come from `<li>` elements.
3. **`model.py`** normalises, resolves every reference, builds the graph both
   ways, and **validates**. A failure here means the source markup changed.
4. **`emit_json.py`** and **`emit_okf.py`** are pure projections of that model.

## Refreshing from upstream

```bash
.venv/bin/python build.py --scrape    # fetch pages missing from the cache
.venv/bin/python build.py --refresh   # re-fetch every page, replacing the cache
```

`html/` is a cache and a cached page is never silently updated, so `--scrape`
only adds what is new. Use `--refresh` to pick up documentation changes; treat
the result as a deliberate commit and read the diff before keeping it.

## Scope — read this before relying on the bundle

This bundle covers the **queryable data model**. Two things are deliberately or
unavoidably absent:

- **Write operations.** The 913 `Monitor.API.<Module>.Commands.*` pages are
  excluded by design. This is the read model.
- **Authentication and request syntax.** The source documentation contains no
  authentication reference, no `$filter`/`$expand`/paging syntax and no status
  codes — so neither does this bundle, and nothing here is invented to fill the
  gap. `okf/guides/querying.md` states exactly what the source does and does not
  say.

Use this to determine *which resource and which field*. You will need Monitor's
own operational documentation to actually make a call.

## Numbers

Deliberately not repeated here — they would go stale. The current counts are
generated into [`okf/index.md`](okf/index.md) and
[`okf/log.md`](okf/log.md) on every build.

## Licence and attribution

The **code** (`build.py`, `check.py`, `monitor_api/`) is MIT licensed — see
[`LICENSE`](LICENSE).

The contents of `html/` and `okf/` are a cache of, and a derivative work of, the
Monitor ERP API documentation published by **Monitor ERP System AB** at
<https://api.monitor.se/api/>. All rights in that documentation remain with its
owner. See the NOTICE section in [`LICENSE`](LICENSE).