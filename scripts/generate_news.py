#!/usr/bin/env python3
"""
generate_news.py
Scrapes EurekAlert!, News-Medical, and Medical News Today, filters for
relevance to Jeewoong Derm Lab's research focus, and uses the Gemini API
(Google AI Studio key, called directly via REST -- no CLI tool) to polish
each scraped snippet into a clean 2-3 sentence summary. Falls back to the
raw scraped snippet if GEMINI_API_KEY is not set or a call fails, so the
page always builds successfully either way.

Run manually:  python scripts/generate_news.py
Run in CI:     .github/workflows/monthly-news-update.yml (20th of every month)

Requires GEMINI_API_KEY as an environment variable / GitHub Actions secret
for AI-polished summaries. Get a key from https://aistudio.google.com/
"""

import os
import calendar
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(REPO_ROOT, "_pages", "news.md")

MAX_ITEMS = 15
GEMINI_MODEL = "gemini-1.5-flash"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; JeewoongDermLabNewsBot/1.0; +https://jwchoi-derm-lab.github.io/)"}

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

_GEMINI_MODEL_OBJ = None


def get_gemini_model():
    global _GEMINI_MODEL_OBJ
    if _GEMINI_MODEL_OBJ is not None:
        return _GEMINI_MODEL_OBJ
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        _GEMINI_MODEL_OBJ = genai.GenerativeModel(GEMINI_MODEL)
        return _GEMINI_MODEL_OBJ
    except Exception as e:
        print(f"[WARN] Gemini init failed, falling back to raw snippets: {e}")
        return None


def gemini_polish(title, snippet):
    model = get_gemini_model()
    if not model or not snippet:
        return None
    prompt = (
        "Rewrite the following dermatology news snippet into a clear, polished "
        "2-3 sentence summary suitable for a research lab website. Keep it "
        "factual and do not invent numbers or facts not present in the snippet.\n\n"
        f"Title: {title}\nSnippet: {snippet}"
    )
    try:
        resp = model.generate_content(prompt)
        text = (resp.text or "").strip()
        return text or None
    except Exception as e:
        print(f"[WARN] Gemini polish failed for '{title[:60]}...': {e}")
        return None


def previous_month_range(ref_date=None):
    ref_date = ref_date or datetime.utcnow()
    first_of_this_month = ref_date.replace(day=1)
    last_day_prev = first_of_this_month - timedelta(days=1)
    first_day_prev = last_day_prev.replace(day=1)
    return first_day_prev.date(), last_day_prev.date()


def keyword_match(text):
    text_l = text.lower()
    return any(k in text_l for k in KEYWORDS)


def classify_category(text):
    text_l = text.lower()
    for keys, css_class, label in CATEGORY_RULES:
        if any(k in text_l for k in keys):
            return css_class, label
    return DEFAULT_CATEGORY


def safe_get(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        return r
    except Exception as e:
        print(f"[WARN] Request failed for {url}: {e}")
        return None


def scrape_eurekalert():
    items = []
    r = safe_get("https://www.eurekalert.org/news-releases/search/dermatology")
    if not r:
        return items
    soup = BeautifulSoup(r.text, "html.parser")
    for card in soup.select("article, div.search-result, div.result-item"):
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
        items.append({"title": title, "link": link, "summary": summary,
                      "source": "EurekAlert!", "source_class": "src-eurekalert"})
    return items


def scrape_news_medical():
    items = []
    r = safe_get("https://www.news-medical.net/condition/Dermatology")
    if not r:
        return items
    soup = BeautifulSoup(r.text, "html.parser")
    for card in soup.select("article, div.article-item, div.newsItem"):
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
        items.append({"title": title, "link": link, "summary": summary,
                      "source": "News-Medical", "source_class": "src-newsmedical"})
    return items


def scrape_mnt():
    items = []
    r = safe_get("https://www.medicalnewstoday.com/categories/dermatology")
    if not r:
        return items
    soup = BeautifulSoup(r.text, "html.parser")
    for card in soup.select("article, li, div.css-card"):
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
        items.append({"title": title, "link": link, "summary": summary,
                      "source": "Medical News Today", "source_class": "src-mnt"})
    return items


def dedupe(items):
    seen, out = set(), []
    for it in items:
        key = it["title"].strip().lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(it)
    return out


def render_card(item):
    css_class, label = classify_category(item["title"] + " " + item["summary"])
    polished = gemini_polish(item["title"], item["summary"])
    summary = polished or item["summary"] or "No summary snippet was available from the source page. Please refer to the original article."
    return f'''<details class="news-card">
  <summary>
    <span class="news-source-tag {item['source_class']}">{item['source']}</span>
    <span class="news-cat-badge {css_class}">{label}</span><br>
    {item['title']}
  </summary>
  <div class="news-summary-body">
    {summary}
    <br><br>
    <a class="news-read-btn" href="{item['link']}" target="_blank">Read Full Article \u2197</a>
  </div>
</details>'''


PAGE_HEADER = '''---
layout: archive
title: "News: Skin Science in the Media"
permalink: /news/
author_profile: true
---

<p class="page__lead">
  A curated monthly digest of dermatology and skin-science coverage from <b>EurekAlert!</b>, <b>News-Medical</b>, and <b>Medical News Today</b> -- filtered for relevance to our lab's focus areas: <b>Skin Cancer & Surgery</b>, <b>Microbiome</b>, and <b>Hair & Nail Disorders</b>, and summarized with the Gemini API. This page auto-refreshes on the 20th of every month to reflect the prior month's coverage.
</p>

<div class="news-update-tag">\U0001F504 Last auto-update covers: <b>{month_label}</b> \u00b7 Auto-refreshes on the 20th of each month</div>

<div class="news-grid">
'''

PAGE_FOOTER = '''
</div>
'''


def main():
    start_date, end_date = previous_month_range()
    month_label = f"{calendar.month_name[start_date.month]} {start_date.year}"
    print(f"Target coverage window: {start_date} to {end_date} ({month_label})")
    print(f"Gemini polishing: {'ENABLED' if os.environ.get('GEMINI_API_KEY') else 'disabled (no GEMINI_API_KEY, using raw snippets)'}")

    all_items = []
    all_items += scrape_eurekalert()
    all_items += scrape_news_medical()
    all_items += scrape_mnt()
    print(f"Scraped {len(all_items)} raw items across 3 sources.")

    relevant = dedupe([it for it in all_items if keyword_match(it["title"] + " " + it["summary"])])
    relevant = relevant[:MAX_ITEMS]
    print(f"{len(relevant)} items matched lab keyword filters.")

    if not relevant:
        print("[WARN] No relevant items found this run -- leaving existing news.md untouched.")
        return

    cards_html = "\n\n".join(render_card(it) for it in relevant)
    content = PAGE_HEADER.format(month_label=month_label) + cards_html + PAGE_FOOTER

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"news.md regenerated with {len(relevant)} items for {month_label}.")


if __name__ == "__main__":
    main()
