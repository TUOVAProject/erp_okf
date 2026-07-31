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

from monitor_api import emit_okf
from monitor_api.model import build
from monitor_api.paths import BASELINE_JSON, HTML_DIR, OKF_DIR, REPO_ROOT
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

LINK_PATTERN = re.compile(r"\]\((/[^)\s]+)\)")


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
    """Every bundle-relative link resolves to a file that exists.

    Relationships in this bundle *are* the links, so a broken one is a broken
    fact, not a cosmetic problem.
    """
    broken = []

    for path in sorted(OKF_DIR.rglob("*.md")):
        for target in LINK_PATTERN.findall(path.read_text(encoding="utf-8")):
            if not (OKF_DIR / target.lstrip("/")).exists():
                broken.append(f"{path.relative_to(OKF_DIR)} -> {target}")

    assert not broken, f"{len(broken)} broken links, e.g. " + "; ".join(broken[:5])


def check_encoding():
    """No UTF-8-decoded-as-latin-1 corruption anywhere in the bundle."""
    mangled = [
        str(path.relative_to(OKF_DIR))
        for path in sorted(OKF_DIR.rglob("*.md"))
        if re.search(r"[-]", path.read_text(encoding="utf-8"))
    ]

    assert not mangled, f"{len(mangled)} files contain mojibake, e.g. {mangled[:3]}"


CHECKS = [
    ("parser fixtures", check_fixtures),
    ("deterministic output", check_determinism),
    ("baseline floor", check_baseline),
    ("link integrity", check_links),
    ("character encoding", check_encoding),
]


def main():
    if not OKF_DIR.exists():
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
