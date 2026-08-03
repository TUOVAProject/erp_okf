"""Build the Monitor ERP API knowledge bundle.

    python build.py             parse cached HTML -> build/model.json + okf/
    python build.py --scrape    fetch pages missing from the cache, then build
    python build.py --refresh   re-fetch every page even if cached, then build

Scraping is opt-in because html/ is a cache: pages already on disk are never
re-downloaded, so a normal build is offline and deterministic. Use --refresh to
pick up upstream documentation changes.
"""

import argparse
import sys

from monitor_api import emit_compact, emit_json, emit_okf, scrape
from monitor_api.model import ValidationError, build
from monitor_api.paths import HTML_DIR, MODEL_JSON, OKF_COMPACT_DIR, OKF_DIR


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scrape",
        action="store_true",
        help="crawl api.monitor.se before building (downloads only missing pages)",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="re-fetch every page, replacing the cache (implies --scrape)",
    )
    args = parser.parse_args()

    if args.scrape or args.refresh:
        scrape.main(force=args.refresh)

    if not HTML_DIR.exists() or not any(HTML_DIR.glob("*/*.html")):
        sys.exit(f"No cached pages in {HTML_DIR}. Run: python build.py --scrape")

    print("Building model...")

    try:
        model = build()
    except ValidationError as error:
        sys.exit(f"\n{error}")

    for label, value in model["stats"].items():
        print(f"  {label:20} {value}")

    emit_json.emit(model)
    print(f"\nWrote {MODEL_JSON}")

    emit_okf.emit(model)
    print(f"Wrote {OKF_DIR} ({sum(1 for _ in OKF_DIR.rglob('*.md'))} markdown files)")

    emit_compact.emit(model)
    print(f"Wrote {OKF_COMPACT_DIR} ({sum(1 for _ in OKF_COMPACT_DIR.rglob('*.md'))} markdown files)")


if __name__ == "__main__":
    main()
