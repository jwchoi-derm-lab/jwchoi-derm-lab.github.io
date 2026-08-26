---
layout: single
permalink: /projects/seborrheic-dermatitis-rosacea/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "fire"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #fef2f2 0%, #f8fafc 100%) !important; border-left: 5px solid #dc2626 !important;">
  <div class="proj-meta-badge" style="color: #dc2626 !important;">CHRONIC INFLAMMATION & CLINICAL EPIDEMIOLOGY</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">Epidemiology of Seborrheic Dermatitis and Risk of Incident Rosacea: A Nationwide Retrospective Cohort Study</h2>
  <p class="proj-lead-text">
    A nationwide population-based matched cohort study investigating the longitudinal risk of developing <b>rosacea</b> in patients with <b>seborrheic dermatitis (SD)</b>, highlighting shared pilosebaceous barrier dysfunction and chronicity-dependent risk surges.
  </p>
  <div class="proj-info-bar">
    <span><b>PI / Corresponding Author:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Nationwide Matched Cohort (1:3 Ratio)</span>
    <span><b>Stack:</b> R v4.6.0, Cox Proportional-Hazards, Schoenfeld Diagnostics, STROBE Guideline</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

Seborrheic dermatitis (SD) and rosacea are prevalent chronic inflammatory disorders of the pilosebaceous unit that share key pathogenic features, including sebaceous gland dysfunction, innate immune hyperactivation (TLR2/cathelicidin), and altered microbial colonization (*Malassezia*, *Demodex*). However, longitudinal epidemiological evidence defining the temporal sequence and risk of incident rosacea following SD has been lacking.

This study aims to:
- Determine the population-level secular trends in the annual prevalence of seborrheic dermatitis over a 16-year observation window (2008–2023).
- Quantify the independent hazard ratio (HR) for incident rosacea among newly diagnosed SD patients compared with 1:3 matched controls.
- Evaluate whether **long-standing, persistent SD** confers an augmented risk trajectory compared to episodic disease.

---

## 🔬 Overview & Rationale

Both disorders target sebaceous-rich facial regions. Recurrent host inflammatory responses to commensal microbes and barrier impairment in chronic SD are hypothesized to prime the facial microenvironment for secondary rosacea onset.

<!-- Modern 3-Tier Inflammatory Progression Flow -->
<div class="study-flow-container">
  
  <div class="flow-tier-box tier-ingest" style="border-top-color: #dc2626 !important;">
    <div class="tier-badge" style="background: #fee2e2 !important; color: #991b1b !important;">PRIMARY PILOSEBACEOUS DYSFUNCTION</div>
    <h3>Seborrheic Dermatitis (Chronic Sebaceous-Rich Inflammation)</h3>
    <p>Disrupted epidermal barrier homeostasis driven by abnormal sebum lipid composition, Malassezia colonization, and recurrent cutaneous inflammation.</p>
  </div>

  <div class="flow-connector-arrow">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #dc2626 !important; background: #fef2f2 !important; border-color: #fecaca !important;">16-Year Nationwide Matched Cohort (1:3 Ratio, 1-Year Lag Window)</span>
    <span class="connector-line"></span>
  </div>

  <div class="niche-grid">
    
    <div class="niche-card" style="border-top-color: #dc2626 !important;">
      <div class="niche-icon">🛡️</div>
      <h4>Barrier Impairment</h4>
      <span class="niche-tag" style="background: #fef2f2 !important; color: #991b1b !important;">Stratum Corneum</span>
      <p>Sustained transepidermal water loss and altered lipid microenvironment promote persistent tissue reactivity.</p>
    </div>

    <div class="niche-card" style="border-top-color: #ea580c !important;">
      <div class="niche-icon">🔬</div>
      <h4>Microbial Overlap</h4>
      <span class="niche-tag" style="background: #fff7ed !important; color: #9a3412 !important;">Demodex & Commensals</span>
      <p>Shared microbial triggers and follicular microenvironment shifts facilitate innate immune receptor activation.</p>
    </div>

    <div class="niche-card" style="border-top-color: #7c3aed !important;">
      <div class="niche-icon">⏳</div>
      <h4>Chronicity Phenotyping</h4>
      <span class="niche-tag" style="background: #f5f3ff !important; color: #5b21b6 !important;">Long-Standing vs. Episodic</span>
      <p>Stratifying disease patterns by longitudinal healthcare utilization (>2 years interval and ≥12 clinical visits).</p>
    </div>

  </div>

  <div class="flow-connector-arrow" style="margin-top: 1.2rem;">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #dc2626 !important; background: #fef2f2 !important; border-color: #fecaca !important;">Cox Proportional-Hazards Regression (Multivariable Adjusted)</span>
    <span class="connector-line"></span>
  </div>

  <div class="flow-tier-box tier-cohort" style="border-top-color: #b91c1c !important;">
    <div class="tier-badge" style="background: #fee2e2 !important; color: #991b1b !important;">CLINICAL RISK ENDPOINT</div>
    <h3>Longitudinal Incident Rosacea Trajectory & Risk Stratification</h3>
    <p>Demonstrating how persistent facial dermatoses prime the pilosebaceous unit for secondary rosacea, guiding targeted early facial surveillance.</p>
  </div>

</div>

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">🏛️</div>
    <h4>Nationwide Representative Cohort</h4>
    <p>Utilized a 2% standardized random sample of the South Korean population (NHIS-NSC), matching newly diagnosed SD cases 1:3 with controls by index date, age, sex, and income tertiles.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🛡️</div>
    <h4>Strict 6-Year Washout & 1-Year Lag</h4>
    <p>Implemented a 2002–2007 washout window to eliminate prevalent cases and applied a 1-year landmark exclusion lag period to prevent concurrent diagnostic surveillance bias.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">📊</div>
    <h4>Longitudinal Chronicity Stratification</h4>
    <p>Defined long-standing SD based on a >2-year claim span with ≥12 visits, performing robust multivariable Cox models adjusting for Charlson comorbidities and systemic covariates.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔍</div>
    <h4>Extensive Subgroup Sensitivity Testing</h4>
    <p>Evaluated risk gradient consistency across sex, age groups, and socioeconomic status with Schoenfeld residual testing to confirm proportional-hazards validity.</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Shared Pilosebaceous Pathophysiology**: Validates population-scale epidemiological links between facial seborrheic dermatitis and downstream rosacea susceptibility.
2. **Clinical Surveillance in Long-Standing SD**: Identifies patients with persistent, recurrent SD as a high-risk cohort warranting proactive barrier restoration and rosacea monitoring.
3. **Preventive Facial Skincare**: Supports early dermocosmetic and anti-inflammatory maintenance to prevent secondary vascular and papulopustular rosacea progression.

---

## 🧭 Project Workflow & Current Progress

<div class="arrow-progress-container">
  <div class="arrow-step step-done step-c1"><span class="step-name">Concept</span></div>
  <div class="arrow-step step-done step-c2"><span class="step-name">IRB &<br>Initiation</span></div>
  <div class="arrow-step step-done step-c3"><span class="step-name">Data<br>Acquisition</span></div>
  <div class="arrow-step step-done step-c4"><span class="step-name">Analysis &<br>Viz</span></div>
  <div class="arrow-step step-done step-c5"><span class="step-name">Manuscript<br>Prep</span></div>
  <div class="arrow-step step-active step-c6"><span class="step-badge">CURRENT</span><span class="step-name">Peer Review</span></div>
  <div class="arrow-step step-pending step-c7"><span class="step-name">Publication</span></div>
</div>

<div class="status-highlight-card">
  <div class="status-badge-pulse">CURRENT STAGE</div>
  <div class="status-content-wrap">
    <h3>Stage: Submission & Peer Review Underway</h3>
    <p>The nationwide retrospective cohort study examining the longitudinal risk of incident rosacea in seborrheic dermatitis is currently under journal peer review.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
