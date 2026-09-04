---
layout: single
permalink: /projects/alopecia-areata-nail-disorders/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "chart-line"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%) !important; border-left: 5px solid #2563eb !important;">
  <div class="proj-meta-badge" style="color: #2563eb !important;">CLINICAL EPIDEMIOLOGY & RISK ANALYSIS</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">Longitudinal Risk of Developing Nail Disorders in Patients with Alopecia Areata: A Nationwide Population-Based Matched Cohort Study</h2>
  <p class="proj-lead-text">
    A nationwide, population-based 1:5 matched cohort study evaluating the long-term cumulative incidence, longitudinal hazard ratios, and risk trajectories of <b>nail disorders (pitting, dystrophy, Beau's lines, and onycholysis)</b> according to <b>alopecia areata severity and clinical course duration</b>.
  </p>
  <div class="proj-info-bar">
    <span><b>PI / Corresponding Author:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Nationwide Retrospective Matched Cohort (1:5 Matched)</span>
    <span><b>Stack:</b> NHIS Administrative Claims (2004–2023), Kaplan–Meier, Cox Proportional Hazards, Schoenfeld Residuals</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

Alopecia areata (AA) is a representative autoimmune, non-scarring hair loss disorder. Hair follicles and the nail apparatus originate from the embryonic ectoderm and share significant structural, biological, and keratinized properties. Prior small-scale observational studies have suggested that nail abnormalities occur frequently in patients with AA, likely due to shared immunological targets between the hair follicle and the nail matrix.

However, large-scale, population-based epidemiological studies quantifying the exact cumulative incidence, excess risk compared with the general population, and the impact of AA clinical duration and severity on subsequent nail disorder risk have been lacking.

This study aims to:
- Establish a nationwide representative matched cohort from the Korean National Health Insurance Service (NHIS) claims database (2004–2023, 2.2% population sample) to track the long-term incidence of nail disorders in patients with AA compared with 1:5 matched controls.
- Quantify the cumulative incidence (Kaplan–Meier) and estimate independent hazard ratios (HRs) via multivariable Cox proportional hazards modeling after rigorous adjustment for demographic and systemic confounding factors.
- Perform epidemiological risk stratification to evaluate biological risk gradients across **disease severity (alopecia totalis/universalis vs. other AA)** and **clinical duration (long-standing vs. episodic AA)**.

---

## 🔬 Overview & Epidemiological Framework

By leveraging a 20-year longitudinal claims database, this study tracks incident nail disorders while eliminating misclassification through strict diagnostic thresholds, washout periods, and multivariable risk modeling.

<!-- Modern 3-Tier Epidemiological Risk Architecture Flow -->
<div class="study-flow-container">
  
  <!-- Tier 1: Cohort Ingestion & Matching -->
  <div class="flow-tier-box tier-ingest" style="border-top-color: #2563eb !important;">
    <div class="tier-badge" style="background: #dbeafe !important; color: #1e40af !important;">STEP 1 · NATIONWIDE COHORT INGESTION & 1:5 MATCHING</div>
    <h3>NHIS Claims Database (2004–2023) · AA Cohort vs. Matched Controls</h3>
    <p>Identification of incident AA cases (≥3 separate diagnostic claims; ICD-10 L63) and 1:5 exact matching with non-AA controls based on index year, age, sex, and socioeconomic income strata after applying a 4-year washout period (2002–2005).</p>
  </div>

  <div class="flow-connector-arrow">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #2563eb !important; background: #eff6ff !important; border-color: #bfdbfe !important;">Longitudinal Follow-up & Confounder Adjustment</span>
    <span class="connector-line"></span>
  </div>

  <!-- Tier 2: 3 Outcome & Stratification Vectors (3 Columns) -->
  <div class="niche-grid">
    
    <div class="niche-card" style="border-top-color: #2563eb !important;">
      <div class="niche-icon">📊</div>
      <h4>AA-Associated Nail Changes</h4>
      <span class="niche-tag" style="background: #eff6ff !important; color: #1d4ed8 !important;">Primary Endpoint</span>
      <p>Tracking incident nail dystrophy (L60.3), pitting (L60.8), Beau's lines (L60.4), and onycholysis (L60.1) during longitudinal follow-up.</p>
    </div>

    <div class="niche-card" style="border-top-color: #4f46e5 !important;">
      <div class="niche-icon">⚖️</div>
      <h4>Mechanical Comparator</h4>
      <span class="niche-tag" style="background: #e0e7ff !important; color: #3730a3 !important;">Ingrown Nail Control</span>
      <p>Analyzing ingrown nails (L60.0) as a distinct mechanical/traumatic comparator to validate disease-specific autoimmune risk.</p>
    </div>

    <div class="niche-card" style="border-top-color: #7c3aed !important;">
      <div class="niche-icon">📈</div>
      <h4>Severity & Duration Gradients</h4>
      <span class="niche-tag" style="background: #ede9fe !important; color: #5b21b6 !important;">Subgroup Stratification</span>
      <p>Evaluating risk gradients across severe AA (AT L63.0 / AU L63.1) and long-standing disease (>1 year duration and ≥12 outpatient visits).</p>
    </div>

  </div>

  <div class="flow-connector-arrow" style="margin-top: 1.2rem;">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #2563eb !important; background: #eff6ff !important; border-color: #bfdbfe !important;">Time-to-Event Survival Modeling (Kaplan–Meier & Cox Regression)</span>
    <span class="connector-line"></span>
  </div>

  <!-- Tier 3: Epidemiological Outcome -->
  <div class="flow-tier-box tier-cohort" style="border-top-color: #1e40af !important;">
    <div class="tier-badge" style="background: #dbeafe !important; color: #1e40af !important;">EPIDEMIOLOGICAL CLINICAL ENDPOINT</div>
    <h3>Definitive Risk Quantification & Long-Term Prognostic Evidence</h3>
    <p>Providing population-scale cumulative incidence curves and adjusted hazard ratios (aHRs) to guide targeted clinical nail surveillance in alopecia areata patients.</p>
  </div>

</div>

---

## 🛠️ Methodological & Epidemiological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">🏛️</div>
    <h4>Nationwide Population-Based 1:5 Matching</h4>
    <p>Extracted a representative cohort from the Korean NHIS database (2004–2023, 2.2% population sample), matching AA patients to controls at a 1:5 ratio by index year, age, sex, and income level.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🛡️</div>
    <h4>Strict Washout & Confounder Elimination</h4>
    <p>Applied a 4-year baseline washout period (2002–2005) to capture incident cases only. Excluded malignancies to eliminate treatment-induced onychotoxicity and adjusted for systemic comorbidities and pre-existing inflammatory dermatoses.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">📈</div>
    <h4>Time-to-Event Survival Analysis</h4>
    <p>Estimated cumulative incidence via Kaplan–Meier curves with log-rank testing. Quantified independent risk using multivariable Cox proportional hazards models rigorously verified with Schoenfeld residuals.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔍</div>
    <h4>Severity & Chronicity Subgroup Analysis</h4>
    <p>Stratified risk by AA disease severity (alopecia totalis/universalis vs. patchy AA) and clinical course (long-standing vs. episodic AA) to determine the dose-response relationship of disease burden.</p>
  </div>

</div>

---

## 💡 Epidemiological & Clinical Significance

1. **First Nationwide Longitudinal Risk Quantification**: Overcomes the limitations of small cross-sectional surveys by establishing the true population-level risk of incident nail disorders in patients with alopecia areata.
2. **Biological Gradient & Severity Correlation**: Demonstrates that patients with extensive (AT/AU) or long-standing AA have a substantially higher hazard of developing severe onychodystrophy, confirming a strong clinical risk gradient.
3. **Evidence-Based Clinical Surveillance**: Informs clinical guidelines on the necessity of proactive nail examination and early dermatologic intervention in patients presenting with chronic or severe alopecia areata.

---

## 🧭 Project Workflow & Current Progress

<!-- Universal Standard 7-Step Progress Bar -->
<div class="arrow-progress-container">
  <div class="arrow-step step-done step-c1">
    <span class="step-name">Concept</span>
  </div>
  <div class="arrow-step step-done step-c2">
    <span class="step-name">IRB &<br>Initiation</span>
  </div>
  <div class="arrow-step step-done step-c3">
    <span class="step-name">Data<br>Acquisition</span>
  </div>
  <div class="arrow-step step-done step-c4">
    <span class="step-name">Analysis &<br>Viz</span>
  </div>
  <div class="arrow-step step-active step-c5">
    <span class="step-badge">CURRENT</span>
    <span class="step-name">Manuscript<br>Prep</span>
  </div>
  <div class="arrow-step step-pending step-c6">
    <span class="step-name">Peer Review</span>
  </div>
  <div class="arrow-step step-pending step-c7">
    <span class="step-name">Publication</span>
  </div>
</div>

<!-- Highlighted Active Status Card -->
<div class="status-highlight-card" style="background: #eff6ff !important; border-left-color: #2563eb !important;">
  <div class="status-badge-pulse" style="background: #2563eb !important;">CURRENT STAGE</div>
  <div class="status-content-wrap">
    <h3 style="color: #1e3a8a !important;">Stage: Manuscript Preparation Underway</h3>
    <p style="color: #3b82f6 !important;">All population-based 1:5 matched cohort statistical analyses, Kaplan–Meier cumulative incidence estimates, and severity/duration stratified Cox proportional hazards regressions have been completed. The manuscript is actively being drafted for submission.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.md@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
