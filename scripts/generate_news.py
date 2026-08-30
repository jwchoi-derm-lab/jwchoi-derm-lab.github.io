#!/usr/bin/env python3
"""
generate_news.py
Scrapes EurekAlert!, News-Medical, and Medical News Today for dermatology news
relevant to Jeewoong Derm Lab's research focus (Skin Cancer & Surgery, Microbiome,
Hair & Nail Disorders), keeps only articles published in the PREVIOUS calendar
month relative to run date, caps the result at 15 items, and regenerates the
NEWS_START...NEWS_END block inside _pages/news.md.

Run manually:   python scripts/generate_news.py
Run in CI:      triggered by .github/workflows/monthly-news-update.yml on the 20th
                of every month (covers the prior full calendar month).

Optional: set GEMINI_API_KEY as an environment variable / repo secret to have
Gemini rewrite scraped snippets into polished 2-3 sentence summaries, matching
the same approach already used for journal-updates.md (see GEMINI.md). If the
key is not set, the script falls back to using the raw scraped snippet.
"""

import os
import re
import time
import calendar
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEWS_MD_PATH = os.path.join(REPO_ROOT, "_pages", "news.md")

MAX_ITEMS = 15
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; JeewoongDermLabNewsBot/1.0; +https://jwchoi-derm-lab.github.io/)"}

# Keywords aligned with Jeewoong Derm Lab's research focus areas.
KEYWORDS = [
    "skin cancer", "melanoma", "basal cell", "squamous cell", "mohs",
    "dermatologic surgery", "cutaneous surgery", "nonmelanoma",
    "skin microbiome", "microbiome", "microbiota", "dysbiosis",
    "staphylococcus", "cutibacterium", "malassezia", "candida",
    "alopecia", "hair follicle", "hair loss", "hair regrowth",
    "nail psoriasis", "nail disorder", "onycho",
    "seborrheic dermatitis", "rosacea", "psoriasis", "atopic dermatitis",
    "dermatology", "dermatologist", "cutaneous", "skin disease",
    "epidemiology", "cohort study", "pharmacoepidemiology",
]

CATEGORY_RULES = [
    (["skin cancer", "melanoma", "basal cell", "squamous cell", "mohs",
      "dermatologic surgery", "cutaneous surgery", "nonmelanoma"], "cat-cancer", "Skin Cancer & Surgery"),
    (["microbiome", "microbiota", "dysbiosis", "staphylococcus",
      "cutibacterium", "malassezia", "candida"], "cat-microbiome", "Microbiome"),
    (["alopecia", "hair follicle", "hair loss", "hair regrowth",
      "nail psoriasis", "nail disorder", "onycho"], "cat-hairnail", "Hair & Nail Disorders"),
]

DEFAULT_CATEGORY = ("cat-epi", "Dermatology & Skin Health")


def previous_month_range(ref_date=None):
    """Return (start_date, end_date) for the calendar month before ref_date's month."""
    ref_date = ref_date or datetime.utcnow()
    first_of_this_month = ref_date.replace(day=1)
    last_day_prev_month = first_of_this_month - timedelta(days=1)
    first_day_prev_month = last_day_prev_month.replace(day=1)
    return first_day_prev_month.date(), last_day_prev_month.date()


def keyword_match(text):
    text_l = text.lower()
    return any(k in text_l for k in KEYWORDS)


def classify_category(text):
    text_l = text.lower()
    for keys, css_class, label in CATEGORY_RULES:
        if any(k in text_l for k in keys):
            return css_class, label
    return DEFAULT_CATEGORY


def safe_get(url, **kwargs):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20, **kwargs)
        r.raise_for_status()
        return r
    except Exception as e:
        print(f"[WARN] Request failed for {url}: {e}")
        return None


def scrape_eurekalert():
    """Scrape EurekAlert! dermatology search results."""
    items = []
    url = "https://www.eurekalert.org/news-releases/search/dermatology"
    r = safe_get(url)
    if not r:
        return items
    soup = BeautifulSoup(r.text, "html.parser")
    cards = soup.select("article, div.search-result, div.result-item")
    for card in cards:
        a = card.find("a", href=True)
        title_tag = card.find(["h2", "h3"])
        if not a or not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        link = a["href"]
        if link.startswith("/"):
            link = "https://www.eurekalert.org" + link
        p_tag = card.find("p")
        summary = p_tag.get_text(strip=True) if p_tag else ""
        date_tag = card.find(class_=re.compile("date", re.I))
        pub_date = date_tag.get_text(strip=True) if date_tag else ""
        items.append({
            "title": title, "link": link, "summary": summary,
            "pub_date_raw": pub_date, "source": "EurekAlert!", "source_class": "src-eurekalert",
        })
    return items


def scrape_news_medical():
    """Scrape News-Medical dermatology condition page."""
    items = []
    url = "https://www.news-medical.net/condition/Dermatology"
    r = safe_get(url)
    if not r:
        return items
    soup = BeautifulSoup(r.text, "html.parser")
    cards = soup.select("article, div.article-item, div.newsItem")
    for card in cards:
        a = card.find("a", href=True)
        title_tag = card.find(["h2", "h3"])
        if not a or not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        link = a["href"]
        if link.startswith("/"):
            link = "https://www.news-medical.net" + link
        p_tag = card.find("p")
        summary = p_tag.get_text(strip=True) if p_tag else ""
        date_tag = card.find(class_=re.compile("date", re.I))
        pub_date = date_tag.get_text(strip=True) if date_tag else ""
        items.append({
            "title": title, "link": link, "summary": summary,
            "pub_date_raw": pub_date, "source": "News-Medical", "source_class": "src-newsmedical",
        })
    return items


def scrape_mnt():
    """Scrape Medical News Today dermatology category page."""
    items = []
    url = "https://www.medicalnewstoday.com/categories/dermatology"
    r = safe_get(url)
    if not r:
        return items
    soup = BeautifulSoup(r.text, "html.parser")
    cards = soup.select("article, li, div.css-card")
    for card in cards:
        a = card.find("a", href=True)
        title_tag = card.find(["h2", "h3"])
        if not a or not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        link = a["href"]
        if link.startswith("/"):
            link = "https://www.medicalnewstoday.com" + link
        p_tag = card.find("p")
        summary = p_tag.get_text(strip=True) if p_tag else ""
        items.append({
            "title": title, "link": link, "summary": summary,
            "pub_date_raw": "", "source": "Medical News Today", "source_class": "src-mnt",
        })
    return items


def gemini_polish(title, summary):
    """Optionally use Gemini API to turn a raw scraped snippet into a polished
    2-3 sentence summary. Falls back silently if no API key is configured."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or not summary:
        return summary
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = (
            "Rewrite the following dermatology news snippet into a clear, "
            "polished 2-3 sentence summary suitable for a research lab website. "
            "Keep it factual, do not invent numbers.\n\n"
            f"Title: {title}\nSnippet: {summary}"
        )
        resp = model.generate_content(prompt)
        return resp.text.strip() if resp and resp.text else summary
    except Exception as e:
        print(f"[WARN] Gemini polish skipped: {e}")
        return summary


def dedupe(items):
    seen = set()
    out = []
    for it in items:
        key = it["title"].strip().lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    return out


def render_card(item):
    css_class, label = classify_category(item["title"] + " " + item["summary"])
    date_html = f'<span class="news-date-tag">{item.get("pub_date_display","")}</span><br>' if item.get("pub_date_display") else ""
    return f"""
<details class="news-card">
  <summary>
    <span class="news-source-tag {item['source_class']}">{item['source']}</span>
    <span class="news-cat-badge {css_class}">{label}</span>
    {date_html}{item['title']}
  </summary>
  <div class="news-summary-body">
    {item['summary']}
    <br><br>
    <a class="news-read-btn" href="{item['link']}" target="_blank">Read Full Article ↗</a>
  </div>
</details>
"""


def update_news_md(cards_html, month_label):
    with open(NEWS_MD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    content = re.sub(
        r'Last auto-update covers: <b>.*?</b>',
        f'Last auto-update covers: <b>{month_label}</b>',
        content,
    )

    new_block = "<!-- NEWS_START -->\n" + cards_html + "\n<!-- NEWS_END -->"
    content = re.sub(
        r"<!-- NEWS_START -->.*?<!-- NEWS_END -->",
        new_block,
        content,
        flags=re.DOTALL,
    )

    with open(NEWS_MD_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    start_date, end_date = previous_month_range()
    month_label = f"{calendar.month_name[start_date.month]} {start_date.year}"
    print(f"Target coverage window: {start_date} to {end_date} ({month_label})")

    all_items = []
    all_items += scrape_eurekalert()
    all_items += scrape_news_medical()
    all_items += scrape_mnt()

    print(f"Scraped {len(all_items)} raw items across 3 sources.")

    relevant = [it for it in all_items if keyword_match(it["title"] + " " + it["summary"])]
    relevant = dedupe(relevant)
    print(f"{len(relevant)} items matched lab keyword filters.")

    relevant = relevant[:MAX_ITEMS]

    for it in relevant:
        it["summary"] = gemini_polish(it["title"], it["summary"]) or "No summary available. Please refer to the original article."
        it["pub_date_display"] = it.get("pub_date_raw", "")
        time.sleep(0.5)

    if not relevant:
        print("[WARN] No relevant items found this run — leaving existing news.md untouched.")
        return

    cards_html = "\n".join(render_card(it) for it in relevant)
    update_news_md(cards_html, month_label)
    print(f"news.md updated with {len(relevant)} items for {month_label}.")


if __name__ == "__main__":
    main()
