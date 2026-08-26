---
layout: single
permalink: /projects/finasteride-bph-depression-cohort/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "capsules"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #f0fdf4 0%, #f8fafc 100%) !important; border-left: 5px solid #16a34a !important;">
  <div class="proj-meta-badge" style="color: #16a34a !important;">PHARMACOEPIDEMIOLOGY & NEUROPSYCHIATRIC SAFETY</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">No Increased Depression Risk with Add-on Finasteride: A 10-Year Nationwide Cohort Study</h2>
  <p class="proj-lead-text">
    A nationwide population-based cohort study across <b>38,886 Korean men</b> evaluating whether add-on finasteride (5-alpha reductase inhibitor) therapy confers excess depressive disorder risk compared to alpha-blocker monotherapy.
  </p>
  <div class="proj-info-bar">
    <span><b>PI / Corresponding Author:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Nationwide Matched Active-Comparator Cohort</span>
    <span><b>Stack:</b> R v4.5.2, Kaplan–Meier, Cox Proportional-Hazards, Dose-Response Stratification</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

Finasteride (FNS), a selective type II 5α-reductase inhibitor, is widely prescribed for benign prostatic hyperplasia (BPH) and androgenetic alopecia (AGA). Despite its clinical efficacy, substantial controversy persists regarding potential neuropsychiatric adverse effects (termed "post-finasteride syndrome"), largely fueled by pharmacovigilance reports and unadjusted cross-sectional studies.

This study aims to:
- Rigorously assess whether adding finasteride to alpha-blocker (AB) therapy elevates the 10-year cumulative incidence of physician-diagnosed depressive disorders.
- Utilize an **active-comparator design** (AB monotherapy vs. AB + FNS combination) to control for underlying urological symptom burden, chronic illness distress, and indication bias.
- Investigate duration- and exposure-dependent risk thresholds to definitively clarify psychiatric safety in an East Asian cohort.

---

## 🔬 Overview & Rationale

Prior pharmacovigilance signals often suffered from stimulated reporting and nocebo effects, failing to separate the psychological burden of lower urinary tract symptoms (LUTS) and chronic disease from direct pharmacological neurosteroid inhibition.

<!-- Modern 3-Tier Pharmacoepidemiology Flow -->
<div class="study-flow-container">
  
  <div class="flow-tier-box tier-ingest" style="border-top-color: #16a34a !important;">
    <div class="tier-badge" style="background: #dcfce7 !important; color: #15803d !important;">STUDY COHORT INITIATION</div>
    <h3>38,886 Total Subjects (NHIS-NSC 10-Year Follow-up)</h3>
    <p>Systematic extraction of BPH patients with ≥60 days of medication exposure alongside 1:2 matched unexposed healthy controls balanced for age, entry date, and income levels.</p>
  </div>

  <div class="flow-connector-arrow">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #16a34a !important; background: #f0fdf4 !important; border-color: #bbf7d0 !important;">Active-Comparator Tri-Cohort Segmentation</span>
    <span class="connector-line"></span>
  </div>

  <div class="niche-grid">
    
    <div class="niche-card" style="border-top-color: #16a34a !important;">
      <div class="niche-icon">💊</div>
      <h4>AB + Finasteride Group</h4>
      <span class="niche-tag" style="background: #f0fdf4 !important; color: #15803d !important;">Combination (n=4,989)</span>
      <p>BPH patients receiving both alpha-blocker and 5α-reductase inhibitor therapy to test add-on drug toxicity.</p>
    </div>

    <div class="niche-card" style="border-top-color: #0284c7 !important;">
      <div class="niche-icon">🩺</div>
      <h4>AB Monotherapy Group</h4>
      <span class="niche-tag" style="background: #f0f9ff !important; color: #0369a1 !important;">Active Comparator (n=7,973)</span>
      <p>Controls for BPH disease burden, nocturia-induced sleep fragmentation, and urological symptom distress.</p>
    </div>

    <div class="niche-card" style="border-top-color: #64748b !important;">
      <div class="niche-icon">👥</div>
      <h4>Unexposed Controls</h4>
      <span class="niche-tag" style="background: #f1f5f9 !important; color: #475569 !important;">Matched Healthy (n=25,924)</span>
      <p>1:2 matched population controls without BPH or medication exposure to establish natural background rates.</p>
    </div>

  </div>

  <div class="flow-connector-arrow" style="margin-top: 1.2rem;">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #16a34a !important; background: #f0fdf4 !important; border-color: #bbf7d0 !important;">Psychiatrist-Coded Outcome Tracking & Dose-Response Analysis</span>
    <span class="connector-line"></span>
  </div>

  <div class="flow-tier-box tier-cohort" style="border-top-color: #15803d !important;">
    <div class="tier-badge" style="background: #dcfce7 !important; color: #15803d !important;">SAFETY ENDPOINT</div>
    <h3>Definitive Clarification of Finasteride Neuropsychiatric Risk</h3>
    <p>Demonstrating that elevated depression risk stems from underlying chronic disease burden rather than finasteride pharmacological exposure.</p>
  </div>

</div>

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">🏛️</div>
    <h4>Nationwide Representative Cohort</h4>
    <p>Evaluated 38,886 individuals from the National Health Insurance Service-National Sample Cohort (NHIS-NSC) with up to 10 years of longitudinal follow-up.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🛡️</div>
    <h4>Active-Comparator Design</h4>
    <p>Direct comparison between AB monotherapy and AB+FNS combination cohorts effectively mitigating confounding by indication and baseline disease severity.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🧠</div>
    <h4>Psychiatrist-Verified Diagnoses</h4>
    <p>Restricted depressive disorder outcomes exclusively to verified psychiatrist-coded ICD-10 diagnoses, eliminating self-reporting and recall bias.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">⏳</div>
    <h4>Cumulative Dose-Response Stratification</h4>
    <p>Stratified combination users by duration of exposure (<180 vs. ≥180 days) to evaluate dose-response gradients and address immortal time bias.</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Reassessing Neuropsychiatric Concerns**: Provides robust epidemiological evidence that finasteride add-on therapy does not increase depression risk beyond underlying BPH-related disease burden.
2. **Mitigating Patient & Clinician Anxiety**: Dispels unwarranted treatment reluctance, supporting confident long-term medical management of BPH and hair disorders.
3. **East Asian Population Insights**: Delivers critical ethnicity-specific real-world safety data from a major underrepresented demographic group.

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
    <p>The nationwide active-comparator cohort manuscript evaluating the neuropsychiatric safety of finasteride has been submitted for peer-reviewed journal evaluation.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
