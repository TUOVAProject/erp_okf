"""
OKF (Open Knowledge Format, https://github.com/GoogleCloudPlatform/knowledge-catalog)
represents knowledge as a directory of markdown files with YAML frontmatter.
Only ``type`` is required; ``index.md`` and ``log.md`` are the reserved
filenames; relationships are expressed as ordinary markdown links, which is what
turns the directory into a graph.

Every cross-entity reference in a properties table is emitted as a markdown
link, so an agent can answer "what does CustomerOrders reference, and what
references Currencies?" by following links instead of loading the whole model.

Link targets are built as bundle-root-absolute paths (``/entities/Common/X.md``)
throughout this module -- that is the simplest thing for entity_path/module_path
to produce, since a page never needs to know who is linking to it. ``write()``
rewrites them to paths relative to the file being written just before it hits
disk, via ``relativize_links``. That happens in exactly one place because a
leading ``/`` only resolves against ``okf/`` if something serves ``okf/`` as the
web root; GitHub, a plain file manager and most editors resolve it against the
repo root instead, one directory too high.
"""

import json
import posixpath
import re
import shutil
from collections import defaultdict

import yaml

from .paths import OKF_DIR, OKF_TMP_DIR

ABSOLUTE_LINK = re.compile(r"\]\((/[^)\s]+)\)")


def relativize_links(body: str, from_path: str) -> str:
    """Rewrite every ``](/...)`` link target in body to be relative to from_path.

    from_path and the recorded targets are both bundle-root-absolute strings
    like "/entities/Sales/CustomerOrder.md" -- posixpath math on them, no
    filesystem access needed. A "#fragment" (used by emit_compact.py's
    per-entity anchors) is carried through untouched.
    """
    from_dir = posixpath.dirname(from_path)

    def replace(match: re.Match) -> str:
        file_part, _, fragment = match.group(1).partition("#")
        relative = posixpath.relpath(file_part, from_dir)

        return f"]({relative}#{fragment})" if fragment else f"]({relative})"

    return ABSOLUTE_LINK.sub(replace, body)

OKF_VERSION = "0.2"
GENERATOR = "process:monitor-okf-build"

# How many entities the "start here" guide lists. Long enough to cover the shared
# basic data every module joins to, short enough to read in one sitting.
CORE_ENTITY_COUNT = 20

KIND_TO_TYPE = {
    "entity": "API Entity",
    "command": "API Command",
    "type": "API Type",
}

KIND_TO_TAG = {
    "entity": "queryable",
    "command": "command",
    "type": "type",
}


def md_cell(text) -> str:
    """Make a value safe to place inside a markdown table cell."""
    return str(text or "").replace("|", "\\|").replace("\n", " ").strip()


def entity_path(entity: dict) -> str:
    return f"/entities/{entity['module']}/{entity['api_class']}.md"


def module_path(module: str) -> str:
    return f"/modules/{module}.md"


def scope_note(model: dict) -> str:
    """One sentence about the command pages the crawl leaves out.

    The count comes from the crawl manifest rather than being written by hand,
    so it cannot drift from what the scraper actually did. Older manifests do not
    record it, in which case the claim is made without a number rather than with
    a guessed one.
    """
    excluded = model.get("scope", {}).get("excluded_pages")

    if not excluded:
        return (
            "The API's command pages (`POST` operations that create, update or "
            "remove data) are excluded by the crawler."
        )

    return (
        f"The API's {excluded} command pages (`POST` operations that create, "
        "update or remove data) are excluded by the crawler."
    )


def endpoint_cell(entity: dict, with_method: bool = False) -> str:
    """Endpoint as a table cell, or an em dash when the page declares none.

    Payload types never have one, and validate() only guarantees an endpoint for
    queryable and command pages, so this must not assume the dict is there.
    """
    endpoint = entity["endpoint"]

    if not endpoint:
        return "—"

    if with_method:
        return f"`{endpoint['method']} {endpoint['path']}`"

    return f"`{endpoint['path']}`"


def link(label: str, target: str) -> str:
    return f"[{md_cell(label)}]({target})"


def frontmatter(fields: dict) -> str:
    clean = {k: v for k, v in fields.items() if v not in (None, "", [], {})}
    body = yaml.safe_dump(clean, sort_keys=False, allow_unicode=True, default_flow_style=False)

    return f"---\n{body}---\n"


def write(relative_path: str, fields: dict, body: str) -> None:
    path = OKF_TMP_DIR / relative_path.lstrip("/")
    path.parent.mkdir(parents=True, exist_ok=True)
    body = relativize_links(body, relative_path)
    path.write_text(frontmatter(fields) + "\n" + body.rstrip() + "\n", encoding="utf-8")


def constraint_tokens(prop: dict) -> list[str]:
    tokens = []

    if prop["expandable"]:
        tokens.append("expandable")
    if prop["is_collection"]:
        tokens.append("collection")
    if prop["unique"]:
        tokens.append(f"unique (per {prop['unique_scope']})" if prop["unique_scope"] else "unique")
    if prop["mandatory"]:
        tokens.append(
            f"mandatory ({prop['mandatory_when']})" if prop["mandatory_when"] else "mandatory"
        )
    if prop["max_length"] is not None:
        tokens.append(f"max length {prop['max_length']}")
    if prop["min_length"] is not None:
        tokens.append(f"min length {prop['min_length']}")
    if prop["default"] is not None:
        tokens.append(f"default: {prop['default']}")
    if prop["bitmask"]:
        tokens.append("bitmask")
    if prop["enum_values"]:
        tokens.append("enum")
    if prop["obsolete"]:
        tokens.append(f"**deprecated since {prop['obsolete_since']}**")
    if prop["introduced_in"]:
        tokens.append(f"since {prop['introduced_in']}")

    return tokens


def property_rows(entity: dict, entities: dict) -> list[str]:
    rows = []

    for prop in entity["properties"]:
        references = ", ".join(
            link(ref["label"], entity_path(entities[ref["target"]])) for ref in prop["references"]
        )
        description = md_cell(prop["summary"])

        if prop["obsolete_note"]:
            description = f"{description} _({md_cell(prop['obsolete_note'])})_".strip()

        rows.append(
            "| `{name}` | `{type}` | {null} | {refs} | {constraints} | {desc} |".format(
                name=md_cell(prop["name"]),
                type=md_cell(prop["type"]),
                null="yes" if prop["nullable"] else "no",
                refs=references,
                constraints=md_cell(", ".join(constraint_tokens(prop))),
                desc=description,
            )
        )

    return rows


def enum_sections(entity: dict) -> list[str]:
    sections = []

    for prop in entity["properties"]:
        if not prop["enum_values"]:
            continue

        heading = f"### {prop['name']}"

        if prop["bitmask"]:
            heading += " (bitmask — values combine)"

        lines = [heading, "", "| Name | Value |", "| --- | ---: |"]
        lines += [
            f"| `{md_cell(member['name'])}` | {member['value']} |" for member in prop["enum_values"]
        ]
        sections.append("\n".join(lines))

    return sections


def entity_body(entity: dict, entities: dict) -> str:
    parts = [f"# {entity['title']}", ""]

    if entity["title"] != entity["doc_name"]:
        parts.append(f"Operation `{entity['doc_name']}` on the Monitor API.")
        parts.append("")

    parts.append(entity["description"])
    parts.append("")

    facts = [f"- **Module:** {link(entity['module'], module_path(entity['module']))}"]
    facts.append(f"- **API class:** `{entity['api_class']}`")

    if entity["endpoint"]:
        facts.append(
            f"- **Endpoint:** `{entity['endpoint']['method']} {entity['endpoint']['path']}`"
        )
    else:
        facts.append("- **Endpoint:** none — this is a payload type, not a queryable resource.")

    if entity["required_permission"]:
        facts.append(f"- **Required permission:** {entity['required_permission']}")
    if entity["guid"]:
        facts.append(f"- **GUID:** `{entity['guid']}`")
    if entity["introduced_in"]:
        facts.append(f"- **Introduced in:** {entity['introduced_in']}")

    parts.append("\n".join(facts))

    if entity["notes"]:
        parts += ["", "## Notes", ""] + [f"- {note}" for note in entity["notes"]]

    if entity["properties"]:
        heading = "Request body" if entity["kind"] == "command" else "Properties"
        parts += [
            "",
            f"## {heading}",
            "",
            "| Property | Type | Null | References | Constraints | Description |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        parts += property_rows(entity, entities)

    enums = enum_sections(entity)

    if enums:
        parts += ["", "## Enumerations", ""] + ["\n".join([section, ""]) for section in enums]

    if entity["referenced_by"]:
        parts += ["", "## Referenced by", ""]
        by_module = defaultdict(list)

        for ref in sorted(entity["referenced_by"], key=lambda r: (r["source_title"], r["property"])):
            by_module[ref["source_module"]].append(ref)

        for module in sorted(by_module):
            parts.append(f"**{module}**")
            parts.append("")
            for ref in by_module[module]:
                target = entity_path(entities[ref["source"]])
                kind = "expand" if ref["kind"] == "navigation" else "FK"
                parts.append(f"- {link(ref['source_title'], target)} — `{ref['property']}` ({kind})")
            parts.append("")

    if entity["example"] is not None:
        parts += [
            "",
            "## Example",
            "",
            "```json",
            json.dumps(entity["example"], ensure_ascii=False, indent=2),
            "```",
        ]

    return "\n".join(parts)


def emit_entities(model: dict) -> None:
    entities = model["entities"]

    for entity in entities.values():
        fields = {
            "type": KIND_TO_TYPE[entity["kind"]],
            "title": entity["title"],
            "description": entity["description"],
            "resource": entity["doc_url"],
            "tags": [entity["module"], KIND_TO_TAG[entity["kind"]]],
            "status": entity["status"],
            "generated": {"by": GENERATOR, "from": model["source_digest"]},
            "sources": [{"resource": entity["doc_url"], "title": f"Monitor API — {entity['api_class']}"}],
            "module": entity["module"],
            "api_class": entity["api_class"],
            "doc_name": entity["doc_name"],
            "endpoint": (
                f"{entity['endpoint']['method']} {entity['endpoint']['path']}"
                if entity["endpoint"]
                else None
            ),
            "guid": entity["guid"],
            "permission": entity["required_permission"],
            "introduced_in": entity["introduced_in"],
            "property_count": len(entity["properties"]),
            "references_out": sorted(
                {entity_path(entities[ref["target"]]) for ref in entity["references_out"]}
            ),
            "referenced_by": sorted(
                {entity_path(entities[ref["source"]]) for ref in entity["referenced_by"]}
            ),
        }

        write(entity_path(entity), fields, entity_body(entity, entities))


def emit_entity_indexes(model: dict) -> None:
    entities = model["entities"]
    by_module = defaultdict(list)

    for entity in entities.values():
        by_module[entity["module"]].append(entity)

    for module, members in sorted(by_module.items()):
        members.sort(key=lambda e: e["title"].lower())
        lines = [
            f"# {module} entities",
            "",
            f"{len(members)} documented pages in the {module} module.",
            "",
            "| Entity | Kind | Endpoint | Description |",
            "| --- | --- | --- | --- |",
        ]

        for entity in members:
            lines.append(
                f"| {link(entity['title'], entity_path(entity))} "
                f"| {KIND_TO_TAG[entity['kind']]} | {endpoint_cell(entity)} "
                f"| {md_cell(entity['description'])} |"
            )

        write(
            f"/entities/{module}/index.md",
            {"type": "Index", "title": f"{module} entities", "tags": [module]},
            "\n".join(lines),
        )

    lines = ["# Entities", "", "Documented pages grouped by module.", ""]

    for module, members in sorted(by_module.items()):
        lines.append(f"- [{module}](/entities/{module}/index.md) — {len(members)} pages")

    write(
        "/entities/index.md",
        {"type": "Index", "title": "Entities"},
        "\n".join(lines),
    )


def emit_modules(model: dict) -> None:
    entities = model["entities"]

    for name, module in model["modules"].items():
        members = [entities[key] for key in module["entities"]]
        lines = [
            f"# {name}",
            "",
            f"Monitor API module `{name}`: {module['queryable']} queryable entities, "
            f"{module['commands']} commands, {module['types']} payload types.",
            "",
            f"Full listing: [{name} entities](/entities/{name}/index.md)",
            "",
            "## Queryable entities",
            "",
            "| Entity | Endpoint | Description |",
            "| --- | --- | --- |",
        ]

        for entity in members:
            if entity["kind"] != "entity":
                continue
            lines.append(
                f"| {link(entity['title'], entity_path(entity))} "
                f"| {endpoint_cell(entity)} | {md_cell(entity['description'])} |"
            )

        commands = [e for e in members if e["kind"] == "command"]

        if commands:
            lines += ["", "## Commands", "", "| Command | Endpoint | Description |", "| --- | --- | --- |"]
            for entity in commands:
                lines.append(
                    f"| {link(entity['title'], entity_path(entity))} "
                    f"| {endpoint_cell(entity, with_method=True)} "
                    f"| {md_cell(entity['description'])} |"
                )

        types = [e for e in members if e["kind"] == "type"]

        if types:
            lines += ["", "## Payload types", "", "| Type | Description |", "| --- | --- |"]
            for entity in types:
                lines.append(
                    f"| {link(entity['title'], entity_path(entity))} "
                    f"| {md_cell(entity['description'])} |"
                )

        # Cross-module dependencies are the most useful thing to know about a
        # module up front: which other modules its data actually depends on.
        dependencies = module["dependencies"]

        if dependencies:
            lines += ["", "## Depends on other modules", ""]
            for other in sorted(dependencies):
                targets = ", ".join(
                    link(entities[key]["title"], entity_path(entities[key]))
                    for key in sorted(dependencies[other], key=lambda k: entities[k]["title"].lower())
                )
                lines.append(f"- {link(other, module_path(other))}: {targets}")

        write(
            module_path(name),
            {
                "type": "API Module",
                "title": name,
                "description": f"Monitor ERP API module {name}.",
                "tags": [name, "module"],
                "generated": {"by": GENERATOR, "from": model["source_digest"]},
                "entity_count": len(members),
                "queryable_count": module["queryable"],
            },
            "\n".join(lines),
        )

    lines = ["# Modules", "", "| Module | Queryable | Commands | Types |", "| --- | ---: | ---: | ---: |"]

    for name, module in model["modules"].items():
        lines.append(
            f"| {link(name, module_path(name))} | {module['queryable']} "
            f"| {module['commands']} | {module['types']} |"
        )

    write("/modules/index.md", {"type": "Index", "title": "Modules"}, "\n".join(lines))


def querying_body(model: dict, entities: dict, entity_link, modules_path: str) -> str:
    stats = model["stats"]
    form_report_configuration = entity_link(entities["Common.FormReportConfiguration"])

    return f"""# Querying the Monitor API

## Endpoint shape

Every documented endpoint follows one pattern:

```
GET  https://<host>/<language>/<company>/api/v1/<Module>/<Entity>
POST https://<host>/<language>/<company>/api/v1/<Module>/<Entity>/<Command>
```

The documentation renders the host as `localhost:8001` with language `sv` and
company `001.1` — these are placeholders for your own Monitor server, not a
public endpoint. The `/api/v1/<Module>/<Entity>` tail is the stable part, and it
is the `endpoint` value recorded on every entity page in this bundle.

## What is in this bundle

- **{stats['queryable']} queryable entities** — `GET`, returning a collection.
- **{stats['commands']} commands** — `POST`, listed in
  [Modules]({modules_path}). Their properties table is the **request body**,
  not a response shape.
- **{stats['types']} payload types** — no endpoint of their own; they appear
  nested inside other responses or command bodies.

## What is deliberately not in this bundle

{scope_note(model)} They live under `Monitor.API.<Module>.Commands.*` upstream
and the crawler skips them by design, because the purpose of this bundle is to
describe the data model comprehensively rather than the write API.

The {stats['commands']} commands that *are* here are the ones the upstream
documentation files outside that namespace; they are included for completeness,
not because command coverage is a goal.

If you need a write operation, go to {model['source']} and look under the
module's `Commands` namespace.

## What the source documentation does not cover

The scraped pages contain **no** query-parameter reference: no documented
`$filter`, `$select`, `$orderby`, `$expand` or paging syntax, and no response
status codes. Only `GET` and `POST` appear anywhere in the corpus.

Two indirect signals are still recorded here, because they are the closest thing
the docs give to query semantics:

- Properties marked `expandable` ({stats['expandable_properties']}
  of them) are navigation properties — the docs flag them as expandable, which
  implies an expand mechanism exists.
- One property summary
  ({form_report_configuration} `Type`)
  notes that `$filter` and `$orderby` cannot be used with it, which confirms both
  options exist in some form.

Treat anything beyond that as unverified: it is not in the source documentation.

## Related

- [Naming conventions](/guides/naming-conventions.md)
- [Relationships](/guides/relationships.md)
- [Permissions](/guides/permissions.md)
"""


def naming_conventions_body(stats: dict) -> str:
    return f"""# Naming conventions

## Plural name vs. class name

Each entity has two names, and they differ:

| | Example | Where it appears |
| --- | --- | --- |
| Documentation / API name | `CustomerOrders` | the URL path, the page title, `title` in this bundle |
| API class name | `CustomerOrder` | the documentation page filename, `api_class` in this bundle |

The API name is usually the plural of the class name, but the mapping is
irregular often enough that it must never be computed. `Addresses`,
`BlanketOrderSales` and `SalesAgreementBases` all break a naive
"strip the trailing s" rule.

**In this bundle the relationship is never guessed.** Every cross-reference is
resolved from the actual hyperlink in the source documentation, so
`api_class` and the link target are always exact.

File naming here follows the class name (`/entities/Sales/CustomerOrder.md`)
because it is unique per module; the plural API name is in `title`.

## Commands

The {stats['commands']} command pages are all titled with a bare verb in the
source documentation — `Create`, `Remove`, `GetWithdrawalInformation` — which is
ambiguous across pages. This bundle titles them by their unique class name
(for example `CreateSalesPickingList`) and keeps the original verb in
`doc_name`.

## Deprecated pages

An entity whose class name ends in `_Obsolete` is marked `status: deprecated` in
its frontmatter. Individual properties carry their own deprecation:
**{stats['obsolete_properties']} properties** are marked deprecated, most with an
explicit replacement in the description.
"""


def relationships_body(model: dict, entities: dict, entity_link) -> str:
    stats = model["stats"]
    fk = stats["foreign_key_edges"]
    nav = stats["navigation_edges"]
    most_referenced_list = "\n".join(
        f"- {entity_link(entities[ranked['key']])} — referenced by "
        f"{ranked['incoming']} properties"
        for ranked in model["most_referenced"][:5]
    )

    return f"""# How entities relate

The model contains **{stats['relationships']} relationships** between
{stats['entities']} entities. They come in two forms, and most related entities
are connected by both at once.

## Foreign key ({fk} edges)

A scalar id property whose description says it references another entity:

```
| `PaymentTermId` | `Int64?` | yes | PaymentTerms | | ... References PaymentTerms |
```

Use these to join data yourself. They are almost always named `<Entity>Id` and
typed `Int64` / `Int64?`.

## Navigation property ({nav} edges)

A property whose **type** is another entity, usually flagged `expandable`:

```
| `PaymentTerm` | `PaymentTerms` | no | PaymentTerms | expandable | ... |
```

These are the related object itself rather than its id. A property typed
`SomeEntity[]` is a collection of them.

So `CustomerOrders` carries both `PaymentTermId` (the key) and `PaymentTerm`
(the object) pointing at the same target.

## Traversing this bundle

Every reference in a properties table is a markdown link to the target entity
page, and every entity page ends with a **Referenced by** section listing the
incoming edges grouped by module. Both directions are also in the frontmatter as
`references_out` and `referenced_by`, so a reverse lookup needs no index.

The most heavily referenced entities are the shared basic-data tables. Follow
**Referenced by** on any of these to see how widely they are used:

{most_referenced_list}

## Module coupling

Each module page has a **Depends on other modules** section listing exactly
which entities it reaches into elsewhere — the fastest way to see how coupled
the modules are.
"""


def permissions_body(entities: dict, stats: dict, entity_link) -> str:
    permissions = defaultdict(list)

    for entity in entities.values():
        if entity["required_permission"]:
            permissions[entity["required_permission"]].append(entity)

    lines = [
        "# Permissions",
        "",
        f"{stats['distinct_permissions']} distinct permission strings guard the documented "
        f"endpoints. {stats['pages_without_permission']} pages declare none "
        "(payload types and a few entities).",
        "",
        "| Permission | Entities |",
        "| --- | --- |",
    ]

    for permission in sorted(permissions):
        members = sorted(permissions[permission], key=lambda e: e["title"].lower())
        lines.append(
            f"| {md_cell(permission)} | "
            + ", ".join(entity_link(e) for e in members)
            + " |"
        )

    return "\n".join(lines)


def core_entities_body(model: dict, entities: dict, entity_link, modules_path: str) -> str:
    stats = model["stats"]
    core_rows = "\n".join(
        f"| {entity_link(entities[ranked['key']])} "
        f"| {link(ranked['module'], module_path(ranked['module']))} "
        f"| {ranked['incoming']} | {md_cell(ranked['description'])} |"
        for ranked in model["most_referenced"][:CORE_ENTITY_COUNT]
    )

    return f"""# Core entities

{stats['entities']} pages is too many to read. These {CORE_ENTITY_COUNT} are the
ones the rest of the model hangs off, ranked by how many properties across the
whole API point at them.

A high count means the entity is shared basic data that many resources join to,
so it is both the most likely thing you need and the most useful thing to
understand first.

| Entity | Module | Referenced by | Description |
| --- | --- | ---: | --- |
{core_rows}

Each page's **Referenced by** section lists exactly which entities and
properties point at it, so you can go from "this is widely used" to "used by
these specific resources" in one hop.

## Related

- [How entities relate](/guides/relationships.md) — what the reference counts mean
- [Modules]({modules_path}) — the same {stats['entities']} pages grouped by area
"""


def emit_guides(model: dict) -> None:
    """Hand-written orientation, with every number taken from the model.

    These are the pages that answer "how does this API work at all", which no
    single entity page can. Each body is a standalone function parameterized by
    an ``entity_link`` callback, so emit_compact.py can reuse them unchanged
    with its own per-module-anchor link shape.
    """
    entities = model["entities"]
    common = {"generated": {"by": GENERATOR, "from": model["source_digest"]}, "tags": ["guide"]}
    okf_entity_link = lambda entity: link(entity["title"], entity_path(entity))

    write(
        "/guides/querying.md",
        {
            "type": "Guide",
            "title": "Querying the Monitor API",
            "description": "Endpoint shape, HTTP verbs and what the documentation does and does not cover.",
            **common,
        },
        querying_body(model, entities, okf_entity_link, "/modules/index.md"),
    )

    write(
        "/guides/naming-conventions.md",
        {
            "type": "Guide",
            "title": "Naming conventions",
            "description": "How documentation names, API class names and URL paths relate.",
            **common,
        },
        naming_conventions_body(model["stats"]),
    )

    write(
        "/guides/relationships.md",
        {
            "type": "Guide",
            "title": "How entities relate",
            "description": "Foreign keys vs. navigation properties, and how to traverse the model.",
            **common,
        },
        relationships_body(model, entities, okf_entity_link),
    )

    write(
        "/guides/permissions.md",
        {
            "type": "Guide",
            "title": "Permissions",
            "description": "Which Monitor permission each documented endpoint requires.",
            **common,
        },
        permissions_body(entities, model["stats"], okf_entity_link),
    )

    write(
        "/guides/core-entities.md",
        {
            "type": "Guide",
            "title": "Core entities",
            "description": (
                "The most heavily referenced entities -- where to start reading."
            ),
            **common,
        },
        core_entities_body(model, entities, okf_entity_link, "/modules/index.md"),
    )

    write(
        "/guides/index.md",
        {"type": "Index", "title": "Guides"},
        """# Guides

Orientation material that no single entity page covers.

- [Core entities](/guides/core-entities.md) — the entities to read first, and why
- [Querying the Monitor API](/guides/querying.md) — endpoint shape, verbs, and the limits of the source docs
- [Naming conventions](/guides/naming-conventions.md) — plural API names vs. class names
- [How entities relate](/guides/relationships.md) — foreign keys vs. navigation properties
- [Permissions](/guides/permissions.md) — permission required per endpoint
""",
    )


def emit_root(model: dict) -> None:
    stats = model["stats"]
    module_lines = "\n".join(
        f"- [{name}]({module_path(name)}) — {module['queryable']} queryable, "
        f"{module['commands']} commands, {module['types']} types"
        for name, module in model["modules"].items()
    )

    write(
        "/index.md",
        {
            "type": "Knowledge Bundle",
            "title": "Monitor ERP API",
            "description": (
                f"Data model of the Monitor ERP REST API: {stats['entities']} documented "
                f"entities across {stats['modules']} modules, with {stats['relationships']} "
                "resolved relationships."
            ),
            "resource": model["source"],
            "okf_version": OKF_VERSION,
            "tags": ["monitor", "erp", "api", "data-model"],
            "generated": {"by": GENERATOR, "from": model["source_digest"]},
            "sources": [{"resource": model["source"], "title": "Monitor ERP API documentation"}],
        },
        f"""# Monitor ERP API

The data model of the Monitor ERP REST API, derived from the public documentation
at {model['source']}.

## Scope

This bundle describes **what data the API exposes and how it connects**: every
queryable resource, its properties, types, enumerations, required permission and
its relationships to other resources.

Two things are deliberately outside that scope, and you will not find them here:

- **Write operations.** {scope_note(model)} This bundle is the read model.
- **How to authenticate and how to shape a request.** The source documentation
  contains no authentication, `$filter`/`$expand`/paging or status-code
  reference, so neither does this bundle. See
  [Querying the Monitor API](/guides/querying.md) for exactly what the source
  does and does not say.

Use this to work out *which resource and which field* you need. You will need
Monitor's own operational documentation to make the call.

| | |
| --- | ---: |
| Modules | {stats['modules']} |
| Documented pages | {stats['entities']} |
| Queryable entities | {stats['queryable']} |
| Commands | {stats['commands']} |
| Payload types | {stats['types']} |
| Properties | {stats['properties']} |
| Relationships | {stats['relationships']} |

## If you read only two pages

1. [Core entities](/guides/core-entities.md) — the {CORE_ENTITY_COUNT} entities
   the rest of the model hangs off, ranked by how much of the API points at them.
2. [How entities relate](/guides/relationships.md) — foreign keys vs. navigation
   properties, which is the one concept you need to traverse anything here.

## Start here

- [Guides](/guides/index.md) — how the API is shaped and how entities relate
- [Modules](/modules/index.md) — the {stats['modules']} top-level modules
- [Entities](/entities/index.md) — every documented page

## Modules

{module_lines}

## How to use this bundle

Each entity page carries its endpoint, required permission, full property table,
enumerations and JSON example. References in the property tables are links, and
each page lists what references it under **Referenced by** — so both directions
of the graph can be walked without loading anything else.

To answer a question about one entity, open its page. To answer a question about
how data connects, follow the links.
""",
    )

    write(
        "/log.md",
        {"type": "Log", "title": "Generation log"},
        f"""# Generation log

## Source {model['source_digest']}

Generated from {stats['entities']} cached documentation pages by `build.py`.
This heading is a digest of the scrape cache, not a timestamp: it changes only
when the source documentation changes, so a rebuild of unchanged input produces
an unchanged bundle.

- {stats['entities']} entities ({stats['queryable']} queryable, {stats['commands']} commands, {stats['types']} types)
- {stats['properties']} properties
- {stats['relationships']} relationships ({stats['foreign_key_edges']} foreign key, {stats['navigation_edges']} navigation)
- {stats['enum_properties']} properties with enumerations
- {stats['obsolete_properties']} deprecated properties

Source: {model['source']}
""",
    )


def emit(model: dict) -> None:
    """Build the bundle in a staging directory, then swap it in.

    The previous bundle is destroyed only once the new one is complete, so a
    failure part-way through emitting leaves the last good bundle intact.
    """
    if OKF_TMP_DIR.exists():
        shutil.rmtree(OKF_TMP_DIR)

    OKF_TMP_DIR.mkdir(parents=True)

    emit_root(model)
    emit_guides(model)
    emit_modules(model)
    emit_entities(model)
    emit_entity_indexes(model)

    if OKF_DIR.exists():
        shutil.rmtree(OKF_DIR)

    OKF_TMP_DIR.rename(OKF_DIR)
