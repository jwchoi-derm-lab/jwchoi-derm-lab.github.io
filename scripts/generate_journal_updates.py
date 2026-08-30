#!/usr/bin/env python3
"""
generate_journal_updates.py
PubMed E-utilities (NCBI public API) + Gemini API (Google AI Studio, REST
call via google-generativeai) automation for _pages/journal-updates.md.

For each of JAAD / JAMA Dermatology / BJD / JID:
  1. Query PubMed for articles published in the PREVIOUS calendar month.
  2. Fetch full records (title, abstract, authors, pub types, volume/issue/pages, DOI).
  3. Classify Original Article vs Non-Original using PubMed's own
     <PublicationType> tags + presence/absence of a structured abstract.
  4. For Original Articles WITH an abstract, ask Gemini to rewrite the
     abstract into a Background & Method / Key Findings / Clinical Takeaway
     3-part summary. If GEMINI_API_KEY is not set or the call fails, falls
     back to showing the raw PubMed abstract untouched -- the page always
     builds successfully either way.
  5. Non-Original entries (Letter/Editorial/Comment/no abstract) are never
     sent to Gemini -- they just show a "refer to original" note, since
     there's no abstract to summarize.
  6. Fully regenerate _pages/journal-updates.md (whole-file rewrite).

Run manually:  python scripts/generate_journal_updates.py
Run in CI:     .github/workflows/monthly-journal-update.yml (20th of every month)

Requires GEMINI_API_KEY as an environment variable / GitHub Actions secret
for the AI-polished 3-part summaries. Get a key from https://aistudio.google.com/
"""

import os
import time
import calendar
from datetime import datetime, timedelta
from xml.etree import ElementTree as ET

import requests

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(REPO_ROOT, "_pages", "journal-updates.md")

EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; JeewoongDermLabJournalBot/1.0)"}
MAX_ARTICLES_PER_JOURNAL = 8
GEMINI_MODEL = "gemini-1.5-flash"

JOURNALS = [
    {"label": "Journal of the American Academy of Dermatology (JAAD)",
     "pubmed_name": "J Am Acad Dermatol", "anchor": "jaad", "title_class": "title-jaad"},
    {"label": "JAMA Dermatology",
     "pubmed_name": "JAMA Dermatol", "anchor": "jama", "title_class": "title-jama"},
    {"label": "British Journal of Dermatology (BJD)",
     "pubmed_name": "Br J Dermatol", "anchor": "bjd", "title_class": "title-bjd"},
    {"label": "Journal of Investigative Dermatology (JID)",
     "pubmed_name": "J Invest Dermatol", "anchor": "jid", "title_class": "title-jid"},
]

CATEGORY_RULES = [
    (["skin cancer", "melanoma", "basal cell", "squamous cell", "mohs",
      "surgical", "surgery", "carcinoma", "nonmelanoma"], "cat-cancer", "Skin Cancer & Surgery", "label-cancer"),
    (["microbiome", "microbiota", "dysbiosis", "staphylococcus",
      "cutibacterium", "malassezia", "candida", "commensal"], "cat-microbiome", "Microbiome & Cutaneous Biology", "label-microbiome"),
    (["alopecia", "hair follicle", "hair loss", "trichology",
      "nail psoriasis", "nail disorder", "onycho"], "cat-hairnail", "Hair & Nail Disorders", "label-hair"),
]
DEFAULT_CATEGORY = ("cat-epi", "General Dermatology", "label-epi")

NON_ORIGINAL_TYPES = {
    "letter", "editorial", "comment", "news", "biography", "portrait",
    "historical article", "congress", "interview", "published erratum",
    "retraction of publication", "retraction notice", "bibliography",
}

_GEMINI_MODEL_OBJ = None


def get_gemini_model():
    """Lazily initialize the Gemini client. Returns None if no key / import fails."""
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
        print(f"[WARN] Gemini init failed, falling back to raw abstracts: {e}")
        return None


def gemini_structured_summary(title, abstract):
    """Ask Gemini to rewrite a PubMed abstract into a 3-part HTML summary.
    Returns None on any failure so the caller can fall back to the raw abstract."""
    model = get_gemini_model()
    if not model or not abstract:
        return None
    prompt = (
        "You are helping build a dermatology research lab website. Rewrite the "
        "following PubMed abstract into exactly three short HTML paragraphs, "
        "each starting with a bolded label, in this exact format and nothing else:\n"
        "<p><b>Background & Method:</b> ...</p>\n"
        "<p><b>Key Findings:</b> ...</p>\n"
        "<p><b>Clinical Takeaway:</b> ...</p>\n"
        "Do not invent numbers or facts not present in the abstract. Keep each "
        "paragraph to 1-2 sentences.\n\n"
        f"Title: {title}\nAbstract: {abstract}"
    )
    try:
        resp = model.generate_content(prompt)
        text = (resp.text or "").strip()
        if "<b>Background" in text and "<b>Key Findings" in text:
            return text
        return None
    except Exception as e:
        print(f"[WARN] Gemini summary call failed for '{title[:60]}...': {e}")
        return None


def previous_month_range(ref_date=None):
    ref_date = ref_date or datetime.utcnow()
    first_of_this_month = ref_date.replace(day=1)
    last_day_prev = first_of_this_month - timedelta(days=1)
    first_day_prev = last_day_prev.replace(day=1)
    return first_day_prev.date(), last_day_prev.date()


def classify_category(text):
    text_l = text.lower()
    for keys, css_class, label, focus_class in CATEGORY_RULES:
        if any(k in text_l for k in keys):
            return css_class, label, focus_class
    return DEFAULT_CATEGORY


def esearch_pmids(pubmed_journal, start_date, end_date):
    params = {
        "db": "pubmed",
        "term": f'("{pubmed_journal}"[Journal]) AND ("{start_date:%Y/%m/%d}"[PDAT] : "{end_date:%Y/%m/%d}"[PDAT])',
        "retmax": "60",
        "retmode": "json",
    }
    try:
        r = requests.get(f"{EUTILS_BASE}/esearch.fcgi", params=params, headers=HEADERS, timeout=20)
        r.raise_for_status()
        return r.json().get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"[WARN] esearch failed for {pubmed_journal}: {e}")
        return []


def efetch_records(pmids):
    if not pmids:
        return []
    params = {"db": "pubmed", "id": ",".join(pmids), "retmode": "xml"}
    try:
        r = requests.get(f"{EUTILS_BASE}/efetch.fcgi", params=params, headers=HEADERS, timeout=30)
        r.raise_for_status()
        root = ET.fromstring(r.content)
    except Exception as e:
        print(f"[WARN] efetch failed: {e}")
        return []

    records = []
    for article in root.findall(".//PubmedArticle"):
        try:
            pmid = article.findtext(".//PMID", default="").strip()
            title = article.findtext(".//Article/ArticleTitle", default="").strip()

            abstract_parts = []
            for ab in article.findall(".//Article/Abstract/AbstractText"):
                label = ab.get("Label")
                text = (ab.text or "").strip()
                if not text:
                    continue
                abstract_parts.append(f"{label}: {text}" if label else text)
            abstract = " ".join(abstract_parts).strip()

            pub_types = [pt.text.strip() for pt in article.findall(".//Article/PublicationTypeList/PublicationType") if pt.text]

            authors = []
            for au in article.findall(".//Article/AuthorList/Author"):
                last = au.findtext("LastName", default="")
                initials = au.findtext("Initials", default="")
                if last:
                    authors.append(f"{last} {initials}".strip())
            author_str = authors[0] + ", et al." if len(authors) > 1 else (authors[0] if authors else "")

            volume = article.findtext(".//Article/Journal/JournalIssue/Volume", default="")
            issue = article.findtext(".//Article/Journal/JournalIssue/Issue", default="")
            pages = article.findtext(".//Article/Pagination/MedlinePgn", default="")

            year = article.findtext(".//Article/Journal/JournalIssue/PubDate/Year", default="")
            month = article.findtext(".//Article/Journal/JournalIssue/PubDate/Month", default="")
            medline_date = article.findtext(".//Article/Journal/JournalIssue/PubDate/MedlineDate", default="")
            date_str = f"{month} {year}".strip() if year else medline_date

            doi = ""
            for eloc in article.findall(".//Article/ELocationID"):
                if eloc.get("EIdType") == "doi":
                    doi = eloc.text or ""

            is_non_original = any(pt.lower() in NON_ORIGINAL_TYPES for pt in pub_types)
            is_original = (not is_non_original) and bool(abstract)

            records.append({
                "pmid": pmid, "title": title, "abstract": abstract,
                "pub_types": pub_types, "author_str": author_str,
                "volume": volume, "issue": issue, "pages": pages,
                "date_str": date_str, "doi": doi, "is_original": is_original,
            })
        except Exception as e:
            print(f"[WARN] failed to parse one record: {e}")
            continue
    return records


def render_focus_list(records):
    grouped = {}
    for rec in records:
        css_class, label, focus_class = classify_category(rec["title"] + " " + rec["abstract"])
        grouped.setdefault((label, focus_class), []).append(rec)

    if not grouped:
        return ""

    blocks = []
    for (label, focus_class), recs in grouped.items():
        items = "\n".join(
            f'            <li><a href="https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/" target="_blank">{r["title"]} (PMID: {r["pmid"]})</a>.</li>'
            for r in recs[:3]
        )
        blocks.append(f'''        <div class="focus-group">
          <span class="focus-label {focus_class}">{label}</span>
          <ul class="focus-list">
{items}
          </ul>
        </div>''')
    return '      <div class="focus-box">\n        <h3>\u2b50 Featured Focus Highlights</h3>\n' + "\n".join(blocks) + "\n      </div>"


def render_article_card(rec, journal_label):
    citation_bits = [journal_label]
    if rec["date_str"]:
        citation_bits.append(rec["date_str"])
    vol_issue = ""
    if rec["volume"]:
        vol_issue = f"{rec['volume']}"
        if rec["issue"]:
            vol_issue += f"({rec['issue']})"
    if vol_issue and rec["pages"]:
        citation_bits.append(f"{vol_issue}:{rec['pages']}")
    elif vol_issue:
        citation_bits.append(vol_issue)
    citation = "; ".join(citation_bits)
    doi_part = f" doi: {rec['doi']}" if rec["doi"] else ""

    meta_line = f'<b>Authors:</b> {rec["author_str"]} | ' if rec["author_str"] else ""
    meta_line += f'<b>Citation:</b> <i>{citation}</i>.{doi_part} | <b>PMID:</b> <a href="https://pubmed.ncbi.nlm.nih.gov/{rec["pmid"]}/" target="_blank">{rec["pmid"]}</a>'

    if rec["is_original"]:
        gemini_html = gemini_structured_summary(rec["title"], rec["abstract"])
        if gemini_html:
            summary_html = gemini_html
        else:
            abstract_display = rec["abstract"]
            if len(abstract_display) > 700:
                abstract_display = abstract_display[:700].rsplit(" ", 1)[0] + "..."
            summary_html = f"<p>{abstract_display}</p>"

        return f'''      <div class="article-card">
        <div class="art-title">
          <span class="art-type-badge type-original">Original Article</span>
          <a href="https://pubmed.ncbi.nlm.nih.gov/{rec["pmid"]}/" target="_blank">{rec["title"]}</a>
        </div>
        <div class="art-meta">{meta_line}</div>
        <div class="art-summary">
{summary_html}
        </div>
      </div>'''
    else:
        ptype_label = rec["pub_types"][0] if rec["pub_types"] else "Article"
        return f'''      <div class="article-card non-original">
        <div class="art-title">
          <span class="art-type-badge type-nonoriginal">{ptype_label} / No Abstract</span>
          <a href="https://pubmed.ncbi.nlm.nih.gov/{rec["pmid"]}/" target="_blank">{rec["title"]}</a>
        </div>
        <div class="art-meta">{meta_line}</div>
        <div class="no-abstract-note">\U0001F4CC This entry is a {ptype_label} and does not include a structured abstract on PubMed. <b>Please refer to the original article (PMID link) for full details.</b></div>
      </div>'''


def render_journal_section(journal, records, month_label):
    focus_html = render_focus_list(records)
    cards = records[:MAX_ARTICLES_PER_JOURNAL]

    if not cards:
        body = '      <p style="color:#718096;">No new indexed articles were found for this journal in the covered period. Please check back next month.</p>'
    else:
        cards_html = "\n\n".join(render_article_card(r, journal["label"]) for r in cards)
        body = (focus_html + "\n\n" if focus_html else "") + \
               f'      <h3 class="articles-header">\U0001F4D1 Selected Articles & Abstract Summaries</h3>\n\n{cards_html}'

    return f'''<div id="{journal["anchor"]}" class="journal-section-block" style="margin-top: 2rem;">
  <h2 class="section-title {journal["title_class"]}">{journal["label"]}</h2>

  <details class="monthly-issue-accordion">
    <summary class="issue-summary">
      <span class="issue-date">{month_label}</span>
      <span class="issue-tag">Auto-Updated Review</span>
    </summary>

    <div class="issue-body">
{body}
    </div>
  </details>
</div>'''


PAGE_HEADER = '''---
layout: archive
title: "Journal Updates (Academic Briefs)"
permalink: /journal-updates/
author_profile: true
---

<style>
.art-type-badge {{
  display: inline-block; padding: 2px 10px; border-radius: 12px;
  font-size: 0.72rem; font-weight: 700; margin-right: 8px;
  vertical-align: middle; letter-spacing: 0.2px;
}}
.art-type-badge.type-original {{ background: #E3F2FD; color: #1565C0; }}
.art-type-badge.type-nonoriginal {{ background: #F3E5F5; color: #6A1B9A; }}
.article-card.non-original {{ opacity: 0.94; }}
.no-abstract-note {{
  margin-top: 0.7rem; padding: 0.6rem 0.9rem; background: #FFF8E1;
  border-left: 3px solid #FFB300; border-radius: 6px;
  font-size: 0.85rem; color: #7a5b00;
}}
.no-abstract-note b {{ color: #5c4400; }}
</style>

<p class="page__lead">
  Curated literature reviews and computational summaries from leading dermatology journals. Sourced automatically each month via the PubMed E-utilities API and summarized with the Gemini API, filtered for relevance to our lab's focus areas: <b>Skin Cancer & Surgery</b>, <b>Microbiome</b>, and <b>Hair & Nail Disorders</b>.
</p>

<div class="news-update-tag">\U0001F504 Last auto-update covers: <b>{month_label}</b> \u00b7 Auto-refreshes on the 20th of each month</div>

<div class="journal-nav-bar">
  <a href="#jaad" class="jlink jlink-jaad">JAAD</a>
  <a href="#jama" class="jlink jlink-jama">JAMA Dermatology</a>
  <a href="#bjd" class="jlink jlink-bjd">BJD</a>
  <a href="#jid" class="jlink jlink-jid">JID</a>
</div>

<hr style="margin: 2.5rem 0 1.5rem 0; border: 0; border-top: 1px solid #e2e8f0;">
'''


def main():
    start_date, end_date = previous_month_range()
    month_label = f"{calendar.month_name[start_date.month]} {start_date.year}"
    print(f"Target coverage window: {start_date} to {end_date} ({month_label})")
    print(f"Gemini polishing: {'ENABLED' if os.environ.get('GEMINI_API_KEY') else 'disabled (no GEMINI_API_KEY, using raw abstracts)'}")

    sections = []
    for journal in JOURNALS:
        pmids = esearch_pmids(journal["pubmed_name"], start_date, end_date)
        print(f"{journal['label']}: {len(pmids)} PMIDs found.")
        time.sleep(0.4)
        records = efetch_records(pmids)
        time.sleep(0.4)
        sections.append(render_journal_section(journal, records, month_label))

    content = PAGE_HEADER.format(month_label=month_label) + "\n\n" + "\n\n".join(sections) + "\n"

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"journal-updates.md regenerated for {month_label}.")


if __name__ == "__main__":
    main()
