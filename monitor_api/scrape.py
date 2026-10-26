"""
Unchanged in behaviour from the original scrape_monitor_api.py — only the paths
are now repo-anchored and the dead BASE_URL constant / unused re import are gone.
"""

import datetime
import json
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag

import requests
from bs4 import BeautifulSoup

from .paths import HTML_DIR, ENDPOINT_INDEX

START_URLS = [
    "https://api.monitor.se/api/toc.html",
    "https://api.monitor.se/api/index.html",
]

REQUEST_TIMEOUT_SECONDS = 30
REQUEST_DELAY_SECONDS = 0.2
MAX_PAGES_TO_SCAN = 3000

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0 Safari/537.36"
)

# Komentosivut rajataan tietoisesti pois: tämä paketti kuvaa kyseltävän
# tietomallin, ei kirjoitusoperaatioita. Pois jäävien sivujen määrä tallennetaan
# endpoint_index.json:iin, jotta rajaus voidaan kertoa lukijalle lukuna eikä
# arviona.
EXCLUDED_PATTERNS = [".Commands."]


def fetch_html(url: str) -> str:
    response = requests.get(
        url,
        headers={"User-Agent": USER_AGENT},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()

    # Palvelin lähettää "Content-Type: text/html" ilman charsetiä, jolloin
    # requests olettaa ISO-8859-1:n ja rikkoo kaikki UTF-8-merkit (esim.
    # "supplier's" -> "supplierâ<80><99>s"). Sivut ovat UTF-8, joten pakotetaan se.
    if "charset" not in response.headers.get("Content-Type", "").lower():
        response.encoding = "utf-8"

    return response.text


def clean_url(url: str) -> str:
    url, _fragment = urldefrag(url)
    return url


def is_internal_api_url(url: str) -> bool:
    parsed = urlparse(url)
    return (
        parsed.scheme in ("http", "https")
        and parsed.netloc == "api.monitor.se"
        and parsed.path.startswith("/api/")
    )


def is_excluded_url(url: str) -> bool:
    return any(pattern in url for pattern in EXCLUDED_PATTERNS)


def parse_monitor_endpoint_url(url):
    if is_excluded_url(url):
        return None

    filename = Path(urlparse(url).path).name

    if not filename.endswith(".html"):
        return None

    filename = filename.replace(".html", "")
    parts = filename.split(".")

    if len(parts) != 4:
        return None

    if parts[0] != "Monitor":
        return None

    if parts[1] != "API":
        return None

    return {
        "category": parts[2],
        "api_class": parts[3],
    }


def discover_endpoint_links():
    """
    Crawlaa API-dokumentaation sisäisiä sivuja ja etsii kaikki
    Monitor.API.Category.Entity.html -linkit.

    Suodattaa komentosivut pois jo ennen kuin ne lisätään crawl-jonoon, mutta
    laskee ne, jotta rajauksen laajuus voidaan kertoa paketissa.

    Palauttaa (endpoints, excluded_urls).
    """
    queue = [clean_url(url) for url in START_URLS]
    queued = set(queue)
    visited_pages = set()
    endpoints_by_url = {}
    excluded_urls = set()

    while queue and len(visited_pages) < MAX_PAGES_TO_SCAN:
        current_url = clean_url(queue.pop(0))

        if current_url in visited_pages:
            continue

        if not is_internal_api_url(current_url):
            continue

        if is_excluded_url(current_url):
            continue

        visited_pages.add(current_url)

        print(f"Scanning [{len(visited_pages)}]: {current_url}")

        try:
            html = fetch_html(current_url)
        except Exception as error:
            print(f"  Failed: {error}")
            continue

        soup = BeautifulSoup(html, "html.parser")

        for a in soup.find_all("a", href=True):
            href_value = a.get("href")

            if not isinstance(href_value, str):
                continue

            absolute_url = clean_url(urljoin(current_url, href_value.strip()))

            if not is_internal_api_url(absolute_url):
                continue

            # TÄRKEIN KOHTA:
            # Suodatetaan komentosivut pois ennen endpoint-parsintaa ja ennen
            # queueen lisäämistä. Talletetaan silti, jotta tiedämme montako
            # sivua rajaus jättää ulkopuolelle.
            if is_excluded_url(absolute_url):
                excluded_urls.add(absolute_url)
                continue

            parsed_endpoint = parse_monitor_endpoint_url(absolute_url)

            if parsed_endpoint:
                endpoints_by_url[absolute_url] = {
                    "category": parsed_endpoint["category"],
                    "api_class": parsed_endpoint["api_class"],
                    "url": absolute_url,
                }

            # Jatketaan crawlingia vain sallittuihin sisäisiin api-sivuihin.
            if absolute_url not in visited_pages and absolute_url not in queued:
                queue.append(absolute_url)
                queued.add(absolute_url)

        time.sleep(REQUEST_DELAY_SECONDS)

    endpoints = sorted(
        endpoints_by_url.values(),
        key=lambda x: (x["category"].lower(), x["api_class"].lower()),
    )

    print("")
    print(f"Visited pages: {len(visited_pages)}")
    print(f"Discovered endpoints: {len(endpoints)}")
    print(f"Excluded command pages: {len(excluded_urls)}")

    return endpoints, sorted(excluded_urls)


def download_endpoint(endpoint: dict, force: bool = False) -> bool:
    """Palauttaa True, jos välimuistin sisältö muuttui (uusi tai erilainen sivu)."""
    category = endpoint["category"]
    api_class = endpoint["api_class"]
    url = endpoint["url"]

    category_dir = HTML_DIR / category
    category_dir.mkdir(parents=True, exist_ok=True)

    output_file = category_dir / f"{api_class}.html"

    # Välimuistissa olevaa sivua ei koskaan päivitetä ilman --refresh:iä.
    if output_file.exists() and not force:
        print(f"  SKIP existing: {output_file}")
        return False

    print(f"  Downloading: {category}/{api_class}")

    html = fetch_html(url)
    changed = not output_file.exists() or output_file.read_text(encoding="utf-8") != html
    output_file.write_text(html, encoding="utf-8")

    time.sleep(REQUEST_DELAY_SECONDS)

    return changed


def previous_fetched_on() -> str | None:
    """Edellisen manifestin hakupäivä, jos sellainen on tallennettu."""
    if not ENDPOINT_INDEX.exists():
        return None

    index = json.loads(ENDPOINT_INDEX.read_text(encoding="utf-8"))

    return index.get("fetched_on") if isinstance(index, dict) else None


def save_index(endpoints: list[dict], excluded_urls: list[str], fetched_on: str | None):
    """Crawl-manifesti.

    Mukana myös rajauksen laajuus, jotta paketti voi kertoa montako komentosivua
    jää ulkopuolelle ilman että luku kirjoitetaan käsin mihinkään.

    fetched_on on päivä, jolloin välimuistin sisältö viimeksi muuttui -- ei
    ajon aikaleima. Se päivitetään vain kun jokin sivu oikeasti muuttui, joten
    muuttumattoman lähteen uudelleenhaku ei muuta pakettia.
    """
    ENDPOINT_INDEX.write_text(
        json.dumps(
            {
                "fetched_on": fetched_on,
                "endpoints": endpoints,
                "excluded_patterns": EXCLUDED_PATTERNS,
                "excluded_pages": len(excluded_urls),
                "excluded_urls": excluded_urls,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def main(force: bool = False):
    HTML_DIR.mkdir(parents=True, exist_ok=True)

    endpoints, excluded_urls = discover_endpoint_links()

    if not endpoints:
        print("No endpoints found.")
        print("If this happens, toc.html may not contain the links directly.")
        return

    fetched_on = previous_fetched_on()
    save_index(endpoints, excluded_urls, fetched_on)

    print("")
    print("Downloading endpoint HTML files...")

    changed = False

    for index, endpoint in enumerate(endpoints, start=1):
        print(
            f"[{index}/{len(endpoints)}] "
            f"{endpoint['category']} / {endpoint['api_class']}"
        )

        try:
            changed = download_endpoint(endpoint, force=force) or changed
        except Exception as error:
            print(f"  ERROR: {endpoint['url']}")
            print(f"  {error}")

    if changed or fetched_on is None:
        save_index(endpoints, excluded_urls, datetime.date.today().isoformat())

    print("")
    print("Done.")
    print(f"HTML output: {HTML_DIR}")
    print(f"Endpoint index: {ENDPOINT_INDEX}")


if __name__ == "__main__":
    main()
