"""
Compact bundle for coding agents with a hard context-file cap (for example
GitHub Copilot's ~50-file limit). Same already-built ``model`` dict as
emit_okf.py -- no new parsing, no new relationship traversal. One file per
module holding every entity as a section, plus a root index and a handful of
guides.

Unlike okf/, this is not an OKF bundle: no YAML frontmatter, no reserved
index.md/log.md semantics. It exists purely to fit inside a small context
window, so every byte spent on metadata here is a byte not spent on data.
Dropped relative to okf/: JSON examples, full per-member enum tables (kept as
one compact line per enum property).
"""

import shutil

from .emit_okf import (
    core_entities_body,
    link,
    md_cell,
    module_path,
    naming_conventions_body,
    permissions_body,
    querying_body,
    relationships_body,
)
from .paths import OKF_COMPACT_DIR, OKF_COMPACT_TMP_DIR

# How many entities the root index lists under "Most-referenced entities".
# A rendering choice of this emitter, kept independent of emit_okf's own
# CORE_ENTITY_COUNT rather than imported, since each bundle picks its own cut.
CORE_ENTITY_COUNT = 20


def entity_ref(entity: dict) -> str:
    """Link target: the entity's module file plus its own key as an anchor."""
    return f"{module_path(entity['module'])}#{entity['key']}"


def entity_link(entity: dict) -> str:
    return link(entity["title"], entity_ref(entity))


def write(relative_path: str, body: str) -> None:
    path = OKF_COMPACT_TMP_DIR / relative_path.lstrip("/")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body.rstrip() + "\n", encoding="utf-8")


def compact_property_rows(entity: dict, entities: dict) -> list[str]:
    """Same reference resolution as emit_okf.property_rows, 4 columns only."""
    rows = []

    for prop in entity["properties"]:
        references = ", ".join(
            entity_link(entities[ref["target"]]) for ref in prop["references"]
        )
        rows.append(
            f"| `{md_cell(prop['name'])}` | `{md_cell(prop['type'])}` "
            f"| {'yes' if prop['nullable'] else 'no'} | {references} |"
        )

    return rows


def compact_enum_lines(entity: dict) -> list[str]:
    """One comma-separated line per enum property, not a per-member table."""
    lines = []

    for prop in entity["properties"]:
        if not prop["enum_values"]:
            continue

        values = ", ".join(f"{member['name']}={member['value']}" for member in prop["enum_values"])
        bitmask = " (bitmask)" if prop["bitmask"] else ""
        lines.append(f"- `{prop['name']}`{bitmask} — {values}")

    return lines


def linked_names(entities: dict, keys) -> str:
    members = sorted((entities[key] for key in set(keys)), key=lambda e: e["title"].lower())

    return ", ".join(entity_link(e) for e in members)


def compact_entity_section(entity: dict, entities: dict) -> str:
    """One entity as a level-3 section with a stable anchor.

    Trimmed analogue of emit_okf.entity_body: description, endpoint,
    permission, introduced_in, a 4-column property table, compact enum lines,
    and references_out/referenced_by as name lists. No JSON example, no
    per-member enum table.
    """
    heading = f"### {entity['title']}"

    if entity["status"] == "deprecated":
        heading += " _(deprecated)_"

    parts = [f'<a id="{entity["key"]}"></a>', heading, "", entity["description"], ""]

    facts = []

    if entity["endpoint"]:
        facts.append(f"- **Endpoint:** `{entity['endpoint']['method']} {entity['endpoint']['path']}`")
    if entity["required_permission"]:
        facts.append(f"- **Required permission:** {entity['required_permission']}")
    if entity["introduced_in"]:
        facts.append(f"- **Introduced in:** {entity['introduced_in']}")

    if facts:
        parts += facts + [""]

    if entity["properties"]:
        parts += ["| Property | Type | Nullable | References |", "| --- | --- | --- | --- |"]
        parts += compact_property_rows(entity, entities)
        parts.append("")

    enum_lines = compact_enum_lines(entity)

    if enum_lines:
        parts += enum_lines + [""]

    out_keys = {ref["target"] for ref in entity["references_out"]}
    in_keys = {ref["source"] for ref in entity["referenced_by"]}

    if out_keys:
        parts.append(f"**References out:** {linked_names(entities, out_keys)}")
    if in_keys:
        parts.append(f"**Referenced by:** {linked_names(entities, in_keys)}")

    return "\n".join(parts)


def emit_modules(model: dict) -> None:
    entities = model["entities"]
    groups = (
        ("entity", "Queryable entities"),
        ("command", "Commands"),
        ("type", "Payload types"),
    )

    for name, module in model["modules"].items():
        members = [entities[key] for key in module["entities"]]
        lines = [
            f"# {name}",
            "",
            f"Monitor API module `{name}`: {module['queryable']} queryable entities, "
            f"{module['commands']} commands, {module['types']} payload types.",
        ]

        for kind, heading in groups:
            group = [entity for entity in members if entity["kind"] == kind]

            if not group:
                continue

            lines += ["", f"## {heading}", ""]

            for entity in group:
                lines.append(compact_entity_section(entity, entities))
                lines.append("")

        dependencies = module["dependencies"]

        if dependencies:
            lines += ["", "## Depends on other modules", ""]
            for other in sorted(dependencies):
                targets = ", ".join(entity_link(entities[key]) for key in dependencies[other])
                lines.append(f"- {link(other, module_path(other))}: {targets}")

        write(module_path(name), "\n".join(lines))


def emit_guides(model: dict) -> None:
    """Reuses the same guide bodies as emit_okf.py, with compact anchors."""
    entities = model["entities"]

    write("/guides/querying.md", querying_body(model, entities, entity_link, "/index.md"))
    write("/guides/naming-conventions.md", naming_conventions_body(model["stats"]))
    write("/guides/relationships.md", relationships_body(model, entities, entity_link))
    write("/guides/permissions.md", permissions_body(entities, model["stats"], entity_link))
    write("/guides/core-entities.md", core_entities_body(model, entities, entity_link, "/index.md"))


def emit_root(model: dict) -> None:
    stats = model["stats"]
    entities = model["entities"]

    module_lines = "\n".join(
        f"- [{name}]({module_path(name)}) — {module['queryable']} queryable, "
        f"{module['commands']} commands, {module['types']} types"
        for name, module in model["modules"].items()
    )
    top_lines = "\n".join(
        f"- {entity_link(entities[ranked['key']])} — referenced by {ranked['incoming']} properties"
        for ranked in model["most_referenced"][:CORE_ENTITY_COUNT]
    )

    write(
        "/index.md",
        f"""# Monitor ERP API (compact)

Compact, coding-agent-friendly view of the Monitor ERP API data model at
{model['source']}. The full bundle (`okf/`) documents the same
{stats['entities']} entities one file per entity; this bundle condenses every
module's entities into a single file so the whole API fits inside a small
agent context budget. Dropped versus `okf/`: JSON examples and full
per-member enum tables (kept as one compact line per enum property).

| | |
| --- | ---: |
| Modules | {stats['modules']} |
| Documented pages | {stats['entities']} |
| Queryable entities | {stats['queryable']} |
| Commands | {stats['commands']} |
| Payload types | {stats['types']} |
| Properties | {stats['properties']} |
| Relationships | {stats['relationships']} |

## Modules

{module_lines}

## Most-referenced entities

{top_lines}

## Guides

- [Querying the Monitor API](/guides/querying.md)
- [Naming conventions](/guides/naming-conventions.md)
- [How entities relate](/guides/relationships.md)
- [Permissions](/guides/permissions.md)
- [Core entities](/guides/core-entities.md)
""",
    )


def emit(model: dict) -> None:
    """Stage in okf-compact.tmp/, then swap in -- same atomicity guarantee as emit_okf.emit."""
    if OKF_COMPACT_TMP_DIR.exists():
        shutil.rmtree(OKF_COMPACT_TMP_DIR)

    OKF_COMPACT_TMP_DIR.mkdir(parents=True)

    emit_root(model)
    emit_guides(model)
    emit_modules(model)

    if OKF_COMPACT_DIR.exists():
        shutil.rmtree(OKF_COMPACT_DIR)

    OKF_COMPACT_TMP_DIR.rename(OKF_COMPACT_DIR)
