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
    em = h1.find("em")
    reference = span.get_text(strip=True).replace(" ", " ") if span else None
    title = em.get_text(strip=True).replace(" ", " ") if em else ""

    if not reference:
        print("No reference found", file=sys.stderr)
        return None

    bible_div = soup.select_one("div.bible")
    if not bible_div:
        print("No div.bible found", file=sys.stderr)
        return None

    parts = []
    for el in bible_div.children:
        if not hasattr(el, "name") or not el.name:
            continue
        if el.name == "p" and "title" in el.get("class", []):
            if parts:
                parts.append("")
            parts.append(el.get_text(strip=True))
        elif el.name == "table":
            th = el.find("th")
            td = el.find("td")
            num = th.get_text(strip=True) if th else ""
            body = td.get_text(strip=True) if td else ""
            if num == "1" and parts:
                parts.append("")
            parts.append(f"{num}. {body}" if num else body)

    text = "\n".join(parts).strip()
    if not text:
        print("No verse text parsed", file=sys.stderr)
        return None

    return {
        "date": date_str,
        "reference": reference,
        "title": title,
        "text": text,
        "translation": "개역개정",
    }


if __name__ == "__main__":
    kst = pytz.timezone("Asia/Seoul")
    today = datetime.now(kst).strftime("%Y-%m-%d")
    date_str = sys.argv[1] if len(sys.argv) > 1 else today

    result = scrape(date_str)
    if result is None:
        print("Scrape failed", file=sys.stderr)
        sys.exit(1)

    with open("verse.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"Saved verse for {date_str}: {result['reference']}")
