import requests
from bs4 import BeautifulSoup
import json
import sys
from datetime import datetime
import pytz

BASE_URL = "https://www.duranno.com/qt/view/bible.asp"
HEADERS = {"User-Agent": "Mozilla/5.0 (Android; Mobile) AppleWebKit/537.36"}


def scrape(date_str: str) -> dict | None:
    url = f"{BASE_URL}?qtDate={date_str}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.encoding = "euc-kr"
    except Exception as e:
        print(f"Request failed: {e}", file=sys.stderr)
        return None

    soup = BeautifulSoup(r.text, "html.parser")

    h1 = soup.select_one("div.font-size h1") or soup.find("h1")
    if not h1:
        print("No h1 found", file=sys.stderr)
        return None

    span = h1.find("span")
    reference = span.get_text(strip=True).replace(" ", " ") if span else None

    if not reference:
        print("No reference found", file=sys.stderr)
        return None

    # Only the citation is published. The 개역개정 verse text on this page is
    # license-encumbered and the <em> subtitle is Duranno's own editorial
    # content, so neither is scraped — the app renders scripture from its own
    # bundled public-domain 개역한글판.
    return {
        "date": date_str,
        "reference": reference,
    }


if __name__ == "__main__":
    import os

    kst = pytz.timezone("Asia/Seoul")
    today = datetime.now(kst).strftime("%Y-%m-%d")
    date_str = sys.argv[1] if len(sys.argv) > 1 else today

    result = scrape(date_str)
    if result is None:
        print("Scrape failed", file=sys.stderr)
        sys.exit(1)

    with open("verse.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    os.makedirs("verses", exist_ok=True)
    with open(f"verses/{date_str}.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Saved verse for {date_str}: {result['reference']}")
