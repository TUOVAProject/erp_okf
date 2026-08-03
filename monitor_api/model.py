"""
This is the only place relationship traversal happens. The previous pipeline
walked the same source -> property -> target structure in five different places
across four files, each with slightly different field names, which is how the
navigation-property edges came to be missing from some outputs and not others.

The model is built once here; every emitter is a pure projection of it.
"""

import hashlib
import json
import re

from .parse import parse_all
from .paths import BASELINE_JSON, ENDPOINT_INDEX, HTML_DIR

SOURCE_ROOT = "https://api.monitor.se/api/"

API_PATH_PATTERN = re.compile(r"(/api/v\d+/.*)$")

# Pages that legitimately document no properties. Marker attribute classes carry
# behaviour, not data, so their tables are empty upstream.
EMPTY_PROPERTIES_ALLOWLIST = {"Infrastructure.ApiMultipartFormCommandAttribute"}

# Queryable and command pages must declare an endpoint line. If a page ever
# legitimately lacks one, add its key here with a reason rather than relaxing
# the check -- an unexplained missing endpoint means the parser broke.
EMPTY_ENDPOINT_ALLOWLIST: set[str] = set()

# UTF-8 decoded as ISO-8859-1 turns every multi-byte character into a run whose
# continuation bytes land in the C1 control block. Real documentation prose never
# contains a C1 control, so their presence is proof of a decoding error rather
# than a guess about which characters look wrong.
MOJIBAKE_PATTERN = re.compile(r"[-]")


# How far a count may fall below the recorded baseline before the build fails.
# Extraction shrinking by a twentieth is not drift; it is a broken regex.
BASELINE_TOLERANCE = 0.95


class ValidationError(Exception):
    """Raised when the built model fails a correctness check."""


def source_digest() -> str:
    """Fingerprint of the scrape cache the model was built from.

    This replaces a generation timestamp deliberately. A timestamp rewrites all
    405 bundle files on every run and tells you nothing; a digest changes only
    when the input actually changed, which makes a rebuild byte-identical and
    the bundle's diff meaningful.
    """
    digest = hashlib.sha256()

    for path in sorted(HTML_DIR.rglob("*.html")):
        digest.update(str(path.relative_to(HTML_DIR)).encode("utf-8"))
        digest.update(path.read_bytes())

    return digest.hexdigest()[:12]


def scrape_scope() -> dict:
    """What the crawl deliberately left out, as recorded by the scraper.

    The command pages are excluded on purpose -- this bundle documents the
    queryable data model. Reading the count back from the crawl manifest means
    the bundle can state the size of that gap without anyone typing a number
    that will later go stale.
    """
    if not ENDPOINT_INDEX.exists():
        return {}

    index = json.loads(ENDPOINT_INDEX.read_text(encoding="utf-8"))

    # Older manifests were a bare list of endpoints with no scope information.
    if not isinstance(index, dict):
        return {}

    return {
        "excluded_pages": index.get("excluded_pages", 0),
        "excluded_patterns": index.get("excluded_patterns", []),
    }


def api_path(url: str) -> str:
    match = API_PATH_PATTERN.search(url or "")

    return match.group(1) if match else (url or "")


def entity_title(page: dict) -> str:
    """Display name.

    For queryable entities and types the <h1> is the API-facing name
    (``CustomerOrders``). Command pages all use bare verbs as their <h1>
    (``Create``, ``Remove``), which is meaningless out of context, so commands
    are titled by their unique class name instead.
    """
    if page["kind"] == "command":
        return page["api_class"]

    return page["name"]


def build_entity(page: dict) -> dict:
    endpoint = page["endpoint"]

    return {
        "key": page["key"],
        "title": entity_title(page),
        "doc_name": page["name"],
        "api_class": page["api_class"],
        "module": page["category"],
        "kind": page["kind"],
        "status": "deprecated" if page["api_class"].endswith("_Obsolete") else "stable",
        "description": page["description"],
        "notes": page["notes"],
        "introduced_in": page["introduced_in"],
        "endpoint": (
            {
                "method": endpoint["method"],
                "url": endpoint["url"],
                "path": api_path(endpoint["url"]),
            }
            if endpoint
            else None
        ),
        "guid": page["guid"],
        "required_permission": page["required_permission"],
        "properties": page["properties"],
        "example": page["example"],
        "doc_url": page["source_url"],
        "source_file": page["source_file"],
        "references_out": [],
        "referenced_by": [],
    }


def navigation_target(entity: dict, property_name: str) -> dict | None:
    """The entity a sibling property points at via its Type-cell link."""
    for prop in entity["properties"]:
        if prop["name"] != property_name:
            continue

        for ref in prop["references"]:
            if ref["kind"] == "navigation":
                return ref

    return None


def resolve_crefs(entities: dict) -> tuple[int, list[str]]:
    """Turn unrendered docfx cross-references into real foreign keys.

    This is not pluralisation guessing, which the rest of the pipeline forbids.
    Each form is resolved through data that is already in the corpus:

    ``P:<Module>.<Class>.<Prop>``
        Names a sibling property on an entity page. That property's *Type* cell
        holds a genuine hyperlink to the target entity, so the edge is read from
        a real link -- just one hop away. A sibling whose type is a .NET
        primitive yields no edge.
    ``M:<Module>.<Class>.#ctor``
        Names a type directly. Accepted only when that page exists in the corpus.
    ``F:<Module>.<Enum>.<Member>``
        An enum member, not an entity. Never an edge.

    Any other prefix is reported so new docfx markup fails the build instead of
    being silently dropped -- the same escape hatch as ``other_bullets``.
    """
    resolved = 0
    problems = []

    for entity in entities.values():
        for prop in entity["properties"]:
            for cref in prop["pending_crefs"]:
                prefix, member = cref["prefix"], cref["member"]

                if prefix == "F":
                    continue

                if prefix == "M":
                    target_key = member.rsplit(".", 1)[0]
                    label = target_key.rsplit(".", 1)[-1]
                elif prefix in ("P", "T"):
                    owner_key, _, sibling = member.rpartition(".")
                    owner = entities.get(owner_key)

                    if owner is None:
                        continue

                    sibling_ref = navigation_target(owner, sibling)

                    # The sibling is typed as a .NET primitive: no entity to link.
                    if sibling_ref is None:
                        continue

                    target_key, label = sibling_ref["target"], sibling_ref["label"]
                else:
                    problems.append(
                        f"{entity['key']}.{prop['name']}: unknown cref prefix "
                        f"{prefix!r} in {member!r}"
                    )
                    continue

                if target_key not in entities:
                    continue

                if any(ref["target"] == target_key for ref in prop["references"]):
                    continue

                prop["references"].append(
                    {"target": target_key, "label": label, "kind": "foreign_key"}
                )
                resolved += 1

    return resolved, problems


def build_relationships(entities: dict) -> tuple[list[dict], list[str]]:
    """One edge per (entity, property, target). Targets are resolved keys.

    Unresolved targets are collected rather than raised on, so validate() can
    report every one of them at once. Raising on the first hid the scale of a
    breakage behind a single example.
    """
    edges = []
    dangling = []

    for entity in entities.values():
        for prop in entity["properties"]:
            for ref in prop["references"]:
                target = entities.get(ref["target"])

                if target is None:
                    dangling.append(
                        f"{entity['key']}.{prop['name']} references unknown page "
                        f"{ref['target']!r}"
                    )
                    continue

                edges.append(
                    {
                        "source": entity["key"],
                        "source_title": entity["title"],
                        "source_module": entity["module"],
                        "property": prop["name"],
                        "target": target["key"],
                        "target_title": target["title"],
                        "target_module": target["module"],
                        "kind": ref["kind"],
                        "type": prop["type"],
                        "nullable": prop["nullable"],
                        "expandable": prop["expandable"],
                        "is_collection": prop["is_collection"],
                    }
                )

    return edges, dangling


def attach_graph(entities: dict, relationships: list[dict]) -> None:
    """Populate both directions of the graph on each entity."""
    for edge in relationships:
        entities[edge["source"]]["references_out"].append(
            {
                "property": edge["property"],
                "target": edge["target"],
                "target_title": edge["target_title"],
                "target_module": edge["target_module"],
                "kind": edge["kind"],
                "nullable": edge["nullable"],
                "is_collection": edge["is_collection"],
            }
        )
        entities[edge["target"]]["referenced_by"].append(
            {
                "source": edge["source"],
                "source_title": edge["source_title"],
                "source_module": edge["source_module"],
                "property": edge["property"],
                "kind": edge["kind"],
            }
        )


def rank_by_incoming(entities: dict) -> list[dict]:
    """Entities ordered by how many properties point at them.

    Incoming edge count is the best available proxy for "central to the data
    model": the shared basic-data tables everything joins to come out on top.
    Ranked once here so every guide that shows a top-N projects the same list
    instead of recomputing its own.
    """
    return [
        {
            "key": entity["key"],
            "title": entity["title"],
            "module": entity["module"],
            "description": entity["description"],
            "incoming": len(entity["referenced_by"]),
        }
        for entity in sorted(
            entities.values(),
            key=lambda e: (-len(e["referenced_by"]), e["title"].lower()),
        )
    ]


def build_modules(entities: dict) -> dict:
    modules = {}

    for entity in sorted(entities.values(), key=lambda e: e["title"].lower()):
        module = modules.setdefault(
            entity["module"],
            {"name": entity["module"], "entities": [], "queryable": 0, "commands": 0, "types": 0},
        )
        module["entities"].append(entity["key"])
        module[
            {"entity": "queryable", "command": "commands", "type": "types"}[entity["kind"]]
        ] += 1

    return dict(sorted(modules.items()))


def module_dependencies(modules: dict, relationships: list[dict]) -> dict:
    """Which other modules' entities each module's data reaches into.

    Computed once here, alongside the rest of the graph, so emitters read
    ``module["dependencies"]`` instead of each filtering ``relationships``
    themselves.
    """
    outgoing = {name: {} for name in modules}

    for edge in relationships:
        if edge["source_module"] == edge["target_module"]:
            continue

        targets = outgoing[edge["source_module"]].setdefault(edge["target_module"], set())
        targets.add(edge["target"])

    return {
        name: {other: sorted(targets) for other, targets in deps.items()}
        for name, deps in outgoing.items()
    }


def mojibake_problems(entities: dict) -> list[str]:
    """Catch UTF-8 decoded as latin-1.

    api.monitor.se serves no charset, so requests guesses ISO-8859-1 and mangles
    every non-ASCII character. That corruption is invisible in the counts and
    silently poisons text -- including permission strings, which then no longer
    match Monitor's real ones. fetch_html forces UTF-8; this makes sure a
    regression there can never reach the bundle again.
    """
    problems = []

    for key, entity in entities.items():
        texts = [entity["description"], entity["required_permission"], *entity["notes"]]
        texts += [prop["summary"] for prop in entity["properties"]]

        for text in texts:
            if MOJIBAKE_PATTERN.search(text or ""):
                problems.append(f"{key}: mojibake in {text[:60]!r}")

    return problems


def baseline_problems(stats: dict) -> list[str]:
    """Catch extraction quietly shrinking.

    Every other check is structural: it notices a page that is malformed, not a
    regex that stopped matching and simply produced less. A recorded floor is the
    only thing that turns "half the relationships vanished" into a failure.

    When a drop is legitimate -- upstream removed pages -- update baseline.json
    deliberately, as a reviewable change, rather than loosening this.
    """
    if not BASELINE_JSON.exists():
        return []

    baseline = json.loads(BASELINE_JSON.read_text(encoding="utf-8"))
    problems = []

    for name, recorded in sorted(baseline.get("stats", {}).items()):
        current = stats.get(name)

        if current is None:
            problems.append(f"baseline: stat {name!r} is no longer produced")
            continue

        floor = recorded * BASELINE_TOLERANCE

        if current < floor:
            problems.append(
                f"baseline: {name} fell to {current}, below {floor:.0f} "
                f"({BASELINE_TOLERANCE:.0%} of the recorded {recorded})"
            )

    return problems


def validate(model: dict, page_count: int, dangling: list[str]) -> list[str]:
    """Fail loudly.

    The old pipeline exited 0 whether it produced correct output or nothing at
    all, which is precisely why several defects survived unnoticed. Anything
    that indicates the parser lost data raises here.
    """
    problems = []
    entities = model["entities"]

    if len(entities) != page_count:
        problems.append(f"{page_count} pages produced {len(entities)} entities (key collision?)")

    for key, entity in entities.items():
        if not entity["properties"] and key not in EMPTY_PROPERTIES_ALLOWLIST:
            problems.append(f"{key}: no properties parsed")

        if (
            entity["kind"] in ("entity", "command")
            and not entity["endpoint"]
            and key not in EMPTY_ENDPOINT_ALLOWLIST
        ):
            problems.append(f"{key}: {entity['kind']} page has no endpoint")

        if entity["kind"] == "unknown":
            problems.append(f"{key}: could not determine page kind")

        if not entity["api_class"]:
            problems.append(f"{key}: missing api_class")

    problems += dangling
    problems += mojibake_problems(entities)
    problems += baseline_problems(model["stats"])

    unclassified = [
        f"{key}.{prop['name']}: {bullet}"
        for key, entity in entities.items()
        for prop in entity["properties"]
        for bullet in prop["other_bullets"]
    ]

    if unclassified:
        problems.append(
            f"{len(unclassified)} unclassified property bullets, e.g. {unclassified[0]}"
        )

    return problems


def build() -> dict:
    pages = parse_all()
    entities = {page["key"]: build_entity(page) for page in pages}

    cref_edges, cref_problems = resolve_crefs(entities)
    relationships, dangling = build_relationships(entities)
    attach_graph(entities, relationships)

    properties = [prop for entity in entities.values() for prop in entity["properties"]]

    modules = build_modules(entities)
    dependencies = module_dependencies(modules, relationships)

    for name, module in modules.items():
        module["dependencies"] = dependencies[name]

    model = {
        "source_digest": source_digest(),
        "source": SOURCE_ROOT,
        "scope": scrape_scope(),
        "modules": modules,
        "most_referenced": rank_by_incoming(entities),
        "entities": dict(sorted(entities.items())),
        "relationships": sorted(
            relationships, key=lambda e: (e["source"], e["property"], e["target"])
        ),
    }

    model["stats"] = {
        "pages": len(pages),
        "entities": len(entities),
        "queryable": sum(1 for e in entities.values() if e["kind"] == "entity"),
        "commands": sum(1 for e in entities.values() if e["kind"] == "command"),
        "types": sum(1 for e in entities.values() if e["kind"] == "type"),
        "modules": len(model["modules"]),
        "properties": len(properties),
        "relationships": len(relationships),
        "foreign_key_edges": sum(1 for e in relationships if e["kind"] == "foreign_key"),
        "navigation_edges": sum(1 for e in relationships if e["kind"] == "navigation"),
        "enum_properties": sum(1 for p in properties if p["enum_values"]),
        "obsolete_properties": sum(1 for p in properties if p["obsolete"]),
        "expandable_properties": sum(1 for p in properties if p["expandable"]),
        "cref_edges": cref_edges,
        "distinct_permissions": len(
            {e["required_permission"] for e in entities.values() if e["required_permission"]}
        ),
        "pages_without_permission": sum(
            1 for e in entities.values() if not e["required_permission"]
        ),
    }

    problems = validate(model, len(pages), dangling + cref_problems)

    if problems:
        raise ValidationError(
            "model validation failed:\n  " + "\n  ".join(problems[:20])
            + (f"\n  ... and {len(problems) - 20} more" if len(problems) > 20 else "")
        )

    return model
