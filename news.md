---
layout: default
permalink: /news/
title: "News & Updates"
author_profile: true
---

<div class="news-container">
  <div class="news-header-card">
    <div class="news-header-badge">LAB ANNOUNCEMENTS</div>
    <h1 class="news-main-title">News & Research Updates</h1>
    <p class="news-header-desc">
      Latest research milestones, publication digests, grant awards, and lab activities from <strong>Jeewoong Derm Lab</strong>.
    </p>
  </div>

  <div class="news-timeline">
    <!-- 2026.08 -->
    <div class="news-item-card card-highlight">
      <div class="news-date-badge">2026.08</div>
      <div class="news-content">
        <span class="news-tag tag-system">Platform Launch</span>
        <h3 class="news-title">Automated Dermatology Journal Digest System Launched</h3>
        <p class="news-text">
          Launched an automated weekly and monthly digest tracking top dermatology and biomedical literature across JAAD, JAMA Dermatology, BJD, and JID.
        </p>
        <div class="news-links">
          <a href="/journal-updates/" class="news-link-btn">View Journal Updates →</a>
        </div>
      </div>
    </div>

    <!-- 2026.02 -->
    <div class="news-item-card">
      <div class="news-date-badge">2026.02</div>
      <div class="news-content">
        <span class="news-tag tag-pub">Publication</span>
        <h3 class="news-title">Scalp Bacteriome & Dysbiosis Study Published</h3>
        <p class="news-text">
          Our large-scale pooled analysis on scalp microbial signatures in alopecia and inflammatory dermatitis has been accepted for publication in the <em>Journal of Dermatology</em>.
        </p>
        <div class="news-links">
          <a href="/publications/" class="news-link-btn">View Publications →</a>
        </div>
      </div>
    </div>

    <!-- 2024–2025 -->
    <div class="news-item-card">
      <div class="news-date-badge">2024 – 2025</div>
      <div class="news-content">
        <span class="news-tag tag-career">Visiting Research</span>
        <h3 class="news-title">Completed Visiting Fellowship at NIAMS, NIH</h3>
        <p class="news-text">
          Completed advanced translational research on cutaneous microbiome and genomics at the National Institute of Arthritis and Musculoskeletal and Skin Diseases (NIAMS), National Institutes of Health (NIH, Bethesda, MD).
        </p>
      </div>
    </div>

    <!-- 2023 -->
    <div class="news-item-card">
      <div class="news-date-badge">2023.09</div>
      <div class="news-content">
        <span class="news-tag tag-lab">Lab Launch</span>
        <h3 class="news-title">Jeewoong Derm Lab Website & Open Science Repositories Established</h3>
        <p class="news-text">
          Established open-access research repositories bridging clinical dermatologic surgery and computational genomics at Ajou University School of Medicine.
        </p>
        <div class="news-links">
          <a href="/projects/" class="news-link-btn">Explore Projects →</a>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
.news-container {
  width: 100%;
  max-width: 100%;
  margin: 0 auto;
}

.news-header-card {
  background: linear-gradient(135deg, #f0f7ff 0%, #e8f5e9 100%);
  border-left: 5px solid #1976d2;
  border-radius: 12px;
  padding: 1.6rem 1.4rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
}

.news-header-badge {
  font-size: 0.74rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #1976d2;
  margin-bottom: 0.35rem;
}

.news-main-title {
  font-size: 1.5rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 0.6rem 0;
  line-height: 1.3;
}

.news-header-desc {
  font-size: 0.94rem;
  color: #334155;
  line-height: 1.6;
  margin: 0;
}

.news-timeline {
  display: flex;
  flex-direction: column;
  gap: 1.3rem;
}

.news-item-card {
  display: flex;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-left: 4px solid #cbd5e1;
  border-radius: 10px;
  padding: 1.3rem 1.4rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  gap: 1.2rem;
}

.news-item-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(25, 118, 210, 0.08);
}

.card-highlight {
  border-left: 4px solid #1976d2;
  background: #fbfdff;
}

.news-date-badge {
  font-size: 0.84rem;
  font-weight: 800;
  color: #1e3a8a;
  background: #eff6ff;
  border: 1px solid #dbeafe;
  padding: 0.35rem 0.7rem;
  border-radius: 6px;
  height: fit-content;
  white-space: nowrap;
}

.news-content {
  flex: 1;
}

.news-tag {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  margin-bottom: 0.4rem;
}

.tag-system { background: #ccfbf1; color: #115e59; }
.tag-pub    { background: #e0e7ff; color: #3730a3; }
.tag-career { background: #fef3c7; color: #92400e; }
.tag-lab    { background: #f1f5f9; color: #334155; }

.news-title {
  font-size: 1.08rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0 0 0.4rem 0;
  line-height: 1.4;
}

.news-text {
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.55;
  margin: 0 0 0.8rem 0;
}

.news-links {
  display: flex;
  gap: 0.6rem;
}

.news-link-btn {
  display: inline-flex;
  align-items: center;
  font-size: 0.78rem;
  font-weight: 700;
  color: #1d4ed8;
  text-decoration: none;
  background: #f0f7ff;
  padding: 0.25rem 0.65rem;
  border-radius: 4px;
  border: 1px solid #dbeafe;
  transition: all 0.15s ease;
}

.news-link-btn:hover {
  background: #1d4ed8;
  color: #ffffff;
  border-color: #1d4ed8;
}

@media screen and (max-width: 640px) {
  .news-item-card {
    flex-direction: column;
    gap: 0.6rem;
  }
  .news-date-badge {
    width: fit-content;
  }
}
</style>
