---
layout: single
permalink: /projects/dermoscopy-reimbursement-its/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "chart-line"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%) !important; border-left: 5px solid #2563eb !important;">
  <div class="proj-meta-badge" style="color: #2563eb !important;">HEALTH POLICY & CANCER EPIDEMIOLOGY</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">Impact of Integrating Dermoscopy into the Healthcare System on Skin Cancer Detection: An Interrupted Time Series Analysis</h2>
  <p class="proj-lead-text">
    A nationwide quasi-experimental study analyzing <b>1.17 million individuals</b> over 15 years to quantify the population-level impact of specialist-restricted national insurance reimbursement on skin cancer detection trajectories.
  </p>
  <div class="proj-info-bar">
    <span><b>PI / Corresponding Author:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Nationwide Interrupted Time Series (ITS)</span>
    <span><b>Funding:</b> National Research Foundation of Korea (NRF: RS-2026-25469501)</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

While dermoscopy has well-established diagnostic superiority over naked-eye examination in controlled clinical settings, its real-world epidemiological impact following national insurance reimbursement has remained unquantified at the population level.

This study aims to:
- Evaluate whether the introduction of a dedicated, specialist-restricted reimbursement code (March 2019) accelerated population-level skin cancer detection.
- Utilize **Interrupted Time Series (ITS)** segmented regression modeling adjusting for 12-month seasonality and external disruptions (COVID-19 pandemic and vaccine rollout).
- Incorporate **lipoma incidence** as a dermoscopy-independent negative control to confirm policy-specific detection yields.

---

## 🔬 Overview & Rationale

Prior to national policy integration, financial barriers and the lack of a dedicated billing code limited the systematic implementation of dermoscopy.

<!-- Modern 3-Tier Policy Impact Flow -->
<div class="study-flow-container">
  
  <div class="flow-tier-box tier-ingest" style="border-top-color: #2563eb !important;">
    <div class="tier-badge" style="background: #dbeafe !important; color: #1e40af !important;">POLICY INTERVENTION</div>
    <h3>National Dermoscopy Reimbursement Policy (March 2019)</h3>
    <p>Nationwide single-date implementation under universal health coverage, restricting reimbursement strictly to board-certified dermatologists to ensure standardized diagnostic performance.</p>
  </div>

  <div class="flow-connector-arrow">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #2563eb !important; background: #eff6ff !important; border-color: #bfdbfe !important;">15-Year Longitudinal Time Series (2009–2023)</span>
    <span class="connector-line"></span>
  </div>

  <div class="niche-grid">
    
    <div class="niche-card" style="border-top-color: #2563eb !important;">
      <div class="niche-icon">📈</div>
      <h4>Target Malignancies</h4>
      <span class="niche-tag" style="background: #eff6ff !important; color: #1d4ed8 !important;">C43, C44, D03, D04</span>
      <p>Tracking monthly incidence rates of NMSC, cutaneous melanoma, and in situ malignancies per 100,000 person-months.</p>
    </div>

    <div class="niche-card" style="border-top-color: #64748b !important;">
      <div class="niche-icon">🛡️</div>
      <h4>Negative Control (Lipoma)</h4>
      <span class="niche-tag" style="background: #f1f5f9 !important; color: #475569 !important;">Specificity Validation</span>
      <p>Analyzing dermoscopy-independent benign subcutaneous tumors to rule out generic healthcare-seeking confounders.</p>
    </div>

    <div class="niche-card" style="border-top-color: #10b981 !important;">
      <div class="niche-icon">❄️</div>
      <h4>Confounder Adjustments</h4>
      <span class="niche-tag" style="background: #ecfdf5 !important; color: #065f46 !important;">Harmonic Modeling</span>
      <p>Accounting for 12-month harmonic sine/cosine seasonality and exogenous pandemic shocks (outbreak & vaccination).</p>
    </div>

  </div>

  <div class="flow-connector-arrow" style="margin-top: 1.2rem;">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #2563eb !important; background: #eff6ff !important; border-color: #bfdbfe !important;">Segmented Generalized Least-Squares Regression</span>
    <span class="connector-line"></span>
  </div>

  <div class="flow-tier-box tier-cohort" style="border-top-color: #1d4ed8 !important;">
    <div class="tier-badge" style="background: #dbeafe !important; color: #1e40af !important;">HEALTH SYSTEM ENDPOINT</div>
    <h3>Quantification of Policy Detection-Yield & In Situ Proportions</h3>
    <p>Providing definitive evidence on how institutional insurance coverage acts as a catalyst for non-invasive cancer detection at a national scale.</p>
  </div>

</div>

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">🏛️</div>
    <h4>Standardized 1.17M National Cohort</h4>
    <p>Longitudinal tracking of 1,175,244 standardized individuals from the National Health Insurance Service (NHIS) database across a 15-year observation window (2009–2023).</p>
  </div>

  <div class="method-card">
    <div class="method-icon">📊</div>
    <h4>12 Candidate Segmented ITS Models</h4>
    <p>Systematic comparison of 12 candidate regression specifications evaluated by Akaike (AIC) and Bayesian Information Criteria (BIC), prioritizing parsimony and correcting for autocorrelation.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">⚖️</div>
    <h4>Negative Control Verification</h4>
    <p>Parallel modeling of lipoma incidence demonstrating unperturbed baseline trends, confirming the high specificity of the reimbursement-driven detection surge.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔍</div>
    <h4>Stage Distribution Tracking</h4>
    <p>Proportional analysis of carcinoma in situ and melanoma in situ versus invasive malignancies to evaluate stage-shift dynamics under routine clinical consultation.</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Reimbursement as a Public Health Tool**: Demonstrates that dedicated insurance coverage serves as an effective policy catalyst to expand specialist diagnostic access.
2. **Detection-Yield Mechanism**: Clarifies that rapid post-policy rises reflect enhanced identification of previously occult lesions rather than biological incidence surges.
3. **International Healthcare Insights**: Informs healthcare policymakers in systems currently lacking dedicated dermoscopy fee codes (e.g., US, Japan, Taiwan).

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
    <p>The interrupted time series manuscript evaluating national dermoscopy reimbursement has been finalized and submitted for expert peer review.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
