---
layout: single
permalink: /projects/alopecia-areata-nail-disorders/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "hand-dots"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%) !important; border-left: 5px solid #2563eb !important;">
  <div class="proj-meta-badge" style="color: #2563eb !important;">PHARMACOEPIDEMIOLOGY & ECTODERMAL APPENDAGE DISORDERS</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">Longitudinal Risk of Developing Nail Disorders in Patients with Alopecia Areata: A Nationwide Population-Based Matched Cohort Study</h2>
  <p class="proj-lead-text">
    A nationwide population-based 1:5 matched cohort study evaluating the long-term cumulative incidence and independent risk trajectory of <b>nail apparatus disorders (nail pitting, dystrophy, and onycholysis)</b> according to <b>alopecia areata (AA) severity and disease duration</b>.
  </p>
  <div class="proj-info-bar">
    <span><b>PI / Corresponding Author:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Nationwide Retrospective Matched Cohort (1:5 Matched)</span>
    <span><b>Stack:</b> NHIS-NSC Database, Kaplan–Meier, Multivariable Cox Proportional-Hazards, Schoenfeld Residuals</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

Alopecia areata (AA) is a well-established autoimmune, non-scarring hair loss disorder driven by the collapse of hair follicle immune privilege. Because hair follicles and the nail apparatus both originate from the embryonic ectoderm and share structural, biological, and keratinized features, autoimmune attacks targeting follicular epitopes frequently extend to the nail matrix.

While small-scale observational studies have reported various nail abnormalities (e.g., geometric pitting, trachyonychia, Beau's lines, and nail dystrophy) in patients with AA, large-scale, population-level longitudinal evidence assessing real-world incidence and risk factors has been lacking.

This study aims to:
- Establish a rigorous, nationwide population-based matched cohort (1:5 matching) using the Korean National Health Insurance Service (NHIS) database (2004–2023).
- Quantify the long-term cumulative incidence and independent hazard ratio (HR) of developing incident nail disorders in patients with AA compared with matched controls.
- Evaluate the biological gradient by stratifying the risk of nail disorders according to **AA disease severity (alopecia totalis/universalis vs. patchy AA)** and **clinical course duration (long-standing vs. episodic AA)**.

---

## 🔬 Overview & Rationale

Both the hair follicle and nail apparatus represent specialized ectodermal appendages. Autoimmune-mediated lymphocytic infiltration targeting the proximal nail matrix disrupts hard keratin synthesis, inducing structural nail plate abnormalities.

<!-- Modern 3-Tier Pathophysiological & Longitudinal Cohort Flow -->
<div class="study-flow-container">
  
  <!-- Tier 1: Shared Autoimmune Trigger -->
  <div class="flow-tier-box tier-ingest" style="border-top-color: #2563eb !important;">
    <div class="tier-badge" style="background: #dbeafe !important; color: #1e40af !important;">PRIMARY AUTOIMMUNE TRIGGER</div>
    <h3>Alopecia Areata (Shared Ectodermal Autoimmune Attack)</h3>
    <p>Autoimmune-mediated destruction and inflammatory cytokine release targeting hair follicle and nail matrix keratinocytes sharing embryonic ectodermal origins.</p>
  </div>

  <div class="flow-connector-arrow">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #2563eb !important; background: #eff6ff !important; border-color: #bfdbfe !important;">Shared Epitope & Matrix Keratinization Defect</span>
    <span class="connector-line"></span>
  </div>

  <!-- Tier 2: 3 Pathophysiological Vectors (3 Columns) -->
  <div class="niche-grid">
    
    <div class="niche-card" style="border-top-color: #2563eb !important;">
      <div class="niche-icon">🔍</div>
      <h4>Pitting & Trachyonychia</h4>
      <span class="niche-tag" style="background: #eff6ff !important; color: #1d4ed8 !important;">Proximal Matrix Defect</span>
      <p>Focal lymphocytic inflammation in the proximal nail matrix leads to defective parakeratosis and classical geometric pitting and roughness.</p>
    </div>

    <div class="niche-card" style="border-top-color: #4f46e5 !important;">
      <div class="niche-icon">⚡</div>
      <h4>Nail Dystrophy & Beau's Lines</h4>
      <span class="niche-tag" style="background: #e0e7ff !important; color: #3730a3 !important;">Mitotic Arrest</span>
      <p>Episodic, severe inflammatory surges cause transient mitotic arrest of matrix keratinocytes, resulting in horizontal grooves and brittle dystrophic plates.</p>
    </div>

    <div class="niche-card" style="border-top-color: #7c3aed !important;">
      <div class="niche-icon">🩺</div>
      <h4>Onycholysis & Bed Damage</h4>
      <span class="niche-tag" style="background: #ede9fe !important; color: #5b21b6 !important;">Hyponychial Detachment</span>
      <p>Distal nail bed involvement destabilizes nail plate adhesion, resulting in secondary distal detachment and chronic subungual inflammation.</p>
    </div>

  </div>

  <div class="flow-connector-arrow" style="margin-top: 1.2rem;">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #2563eb !important; background: #eff6ff !important; border-color: #bfdbfe !important;">Long-Term Longitudinal Nationwide Cohort Tracking (1:5 Matched)</span>
    <span class="connector-line"></span>
  </div>

  <!-- Tier 3: Endpoint -->
  <div class="flow-tier-box tier-cohort" style="border-top-color: #1e40af !important;">
    <div class="tier-badge" style="background: #dbeafe !important; color: #1e40af !important;">EPIDEMIOLOGICAL CLINICAL ENDPOINT</div>
    <h3>Incident Nail Apparatus Disorder Risk & Severity Gradients</h3>
    <p>Time-to-event survival modeling (Kaplan–Meier & multivariable Cox regression) across the nationwide AA cohort vs. 1:5 matched controls to determine independent hazard ratios stratified by severity (AT/AU) and chronicity.</p>
  </div>

</div>

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">🏛️</div>
    <h4>Nationwide Representative 1:5 Matched Cohort</h4>
    <p>Constructed a representative cohort from the Korean NHIS claims database (2004–2023, 2.2% population sample), matching AA patients to controls at a 1:5 ratio by index year, age, sex, and income level.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🛡️</div>
    <h4>Strict Washout & Confounder Elimination</h4>
    <p>Applied a 4-year baseline washout period (2002–2005) to capture incident nail disorders, excluded malignancies to remove chemotherapy-induced onychotoxicity, and adjusted for systemic & cutaneous confounders.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">📈</div>
    <h4>Rigorous Time-to-Event Survival Modeling</h4>
    <p>Calculated cumulative event incidence via Kaplan–Meier estimation with log-rank testing and performed multivariable Cox proportional-hazards regression verified by Schoenfeld residuals.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔬</div>
    <h4>Severity & Chronicity Stratification</h4>
    <p>Evaluated biological gradients by categorizing severe AA (alopecia totalis L63.0 / universalis L63.1) and long-standing AA (>1 year duration and ≥12 visits) to delineate disease burden impacts.</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Ectodermal Appendage Cross-Talk Validation**: Provides definitive, population-level epidemiological evidence confirming the common autoimmune susceptibility linking the follicular and nail matrix compartments.
2. **Proactive Nail Unit Surveillance**: Demonstrates that patients with severe (AT/AU) or long-standing AA harbor an elevated risk of severe onychodystrophy, emphasizing the necessity of early baseline nail examinations in clinical practice.
3. **Comprehensive Management Strategy**: Informs holistic dermatologic care where unexplained nail changes in AA patients are recognized as integral manifestations of systemic appendage autoimmunity, rather than isolated mechanical trauma.

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
  <div class="arrow-step step-done step-c5">
    <span class="step-name">Manuscript<br>Prep</span>
  </div>
  <div class="arrow-step step-active step-c6">
    <span class="step-badge">CURRENT</span>
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
    <h3 style="color: #1e3a8a !important;">Stage: Submission & Peer Review Underway</h3>
    <p style="color: #3b82f6 !important;">The nationwide longitudinal matched cohort manuscript investigating the cumulative incidence and severity-stratified risk of nail disorders in alopecia areata is currently under expert peer review.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.md@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
