---
layout: single
permalink: /projects/hallux-valgus-onychocryptosis/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "bone"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #fffbeb 0%, #f8fafc 100%) !important; border-left: 5px solid #d97706 !important;">
  <div class="proj-meta-badge" style="color: #d97706 !important;">CLINICAL EPIDEMIOLOGY & NAIL APPARATUS DISORDERS</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">Longitudinal Risk of Developing Onychocryptosis in Patients with Hallux Valgus: A Nationwide Cohort Study</h2>
  <p class="proj-lead-text">
    A nationwide population-based matched cohort study evaluating the long-term incidence and independent risk trajectory of <b>onychocryptosis (ingrown nail)</b> secondary to <b>hallux valgus forefoot deformity</b>.
  </p>
  <div class="proj-info-bar">
    <span><b>PI / Corresponding Author:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Nationwide Retrospective Matched Cohort</span>
    <span><b>Stack:</b> R v4.6.0, Kaplan–Meier, Cox Proportional-Hazards, Schoenfeld Residuals</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

Hallux valgus (HV) is a common acquired forefoot deformity characterized by progressive lateral deviation of the great toe and medial prominence of the first metatarsal head. While altered first-ray biomechanics and increased lateral periungual pressure have been anatomically hypothesized to induce onychocryptosis (ingrown toenail, IN), large-scale longitudinal epidemiological evidence quantifying this temporal risk has been lacking.

This study aims to:
- Establish a rigorous, population-scale matched cohort to evaluate the longitudinal incidence of incident onychocryptosis in patients with newly diagnosed hallux valgus.
- Model the independent hazard ratio (HR) conferred by structural forefoot deformity after robustly adjusting for demographic and comorbid covariates.
- Identify sex- and age-specific susceptibility strata to guide proactive clinical surveillance and conservative nail interventions.

---

## 🔬 Overview & Rationale

Progressive lateral rotation and pronation of the hallux systematically alter the spatial relationship between the rigid nail plate and adjacent periungual soft tissue, predisposing to mechanical curling and lateral soft tissue penetration.

```
                     ┌─────────────────────────────────────────────────────────┐
                     │    Hallux Valgus Forefoot Deformity (First-Ray Alteration)│
                     └────────────────────────────┬────────────────────────────┘
                                                  │ Biomechanical Shifts (Lateral Rotation & Pronation)
                                                  ▼
                     ┌─────────────────────────────────────────────────────────┐
                     │ Increased Lateral Nail Fold Pressure & Curvature Strain │
                     └────────────────────────────┬────────────────────────────┘
                                                  │ Long-Term Cumulative Penetration Risk
                                                  ▼
                     ┌─────────────────────────────────────────────────────────┐
                     │           Incident Onychocryptosis (Ingrown Toenail)    │
                     └─────────────────────────────────────────────────────────┘
```

Utilizing a nationally representative administrative claims database with a strict 6-year washout period, this investigation quantifies the long-term risk trajectory and eliminates preexisting skeletal confounding.

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">🏛️</div>
    <h4>Nationwide Representative Matched Cohort</h4>
    <p>Established a 1:3 propensity-matched cohort (660 newly diagnosed HV cases vs. 1,983 matched controls) balanced for cohort entry date, age, sex, and socioeconomic income strata.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🛡️</div>
    <h4>Strict Washout & Confounder Elimination</h4>
    <p>Applied a 6-year baseline washout period to exclude prevalent deformities and censored secondary skeletal foot anomalies (e.g., flatfoot, rigidus) alongside a 6-month surveillance lag window.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">📈</div>
    <h4>Time-to-Event Survival Modeling</h4>
    <p>Calculated cumulative event incidence via Kaplan–Meier estimation with log-rank testing and performed multivariable Cox proportional-hazards regression verified by Schoenfeld residuals.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔍</div>
    <h4>Demographic Subgroup Stratification</h4>
    <p>Conducted extensive subgroup sensitivity analyses stratified by age thresholds, sex differences, and income tiers to assess biological gradient consistency.</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Biomechanical-Pathological Validation**: Provides robust population-scale evidence demonstrating that acquired forefoot deformity acts as a long-term driver for progressive nail plate penetration.
2. **Targeted Clinical Surveillance**: Highlights the necessity of routine podiatric and dermatologic nail monitoring in patients presenting with hallux valgus, particularly among high-risk demographic strata.
3. **Preventive Conservative Management**: Informs early orthopedic footwear adaptation, correct nail trimming education, and non-surgical gutter/splint interventions prior to irreversible nail bed damage or surgical matrixectomy.

---

## 🧭 Project Workflow & Current Progress

<!-- Universal Standard 7-Step Progress Bar (Optimized Two-Line Wrap) -->
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
<div class="status-highlight-card">
  <div class="status-badge-pulse">CURRENT STAGE</div>
  <div class="status-content-wrap">
    <h3>Stage: Submission & Peer Review Underway</h3>
    <p>The longitudinal nationwide cohort manuscript investigating the risk of onychocryptosis in hallux valgus has been finalized and submitted for expert peer evaluation in an academic journal.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
