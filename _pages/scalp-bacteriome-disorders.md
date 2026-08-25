---
layout: single
permalink: /projects/scalp-bacteriome-disorders/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "dna"
---

<div class="project-header-box">
  <div class="proj-meta-badge">CLINICAL DYSBIOSIS & COMPARATIVE METAGENOMICS</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">Scalp Bacteriome Profiles Across Patients with Alopecia Areata, Androgenetic Alopecia, and Seborrheic Dermatitis: Analysis of Public 16S rRNA Datasets</h2>
  <p class="proj-lead-text">
    A comparative integrative pooled analysis across <b>683 multi-cohort subjects</b> spanning <b>6 NCBI BioProjects</b> to uncover disease-specific bacterial dysbiosis patterns in inflammatory and non-scarring scalp disorders.
  </p>
  <div class="proj-info-bar">
    <span><b>PI / Corresponding Author:</b> Jeewoong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Multi-Disease Comparative Meta-Analysis</span>
    <span><b>Funding:</b> National Research Foundation of Korea (NRF: RS-2026-25469501)</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

Bacterial dysbiosis has been increasingly implicated in the pathogenesis of common hair loss and inflammatory scalp conditions. However, comparative microbiome profiles across distinct scalp disorders remain poorly defined due to methodological heterogeneity across isolated small-scale studies.

This study aims to:
- Establish a unified comparative landscape of the scalp bacteriome in patients with **Alopecia Areata (AA)**, **Androgenetic Alopecia (AGA)**, and **Seborrheic Dermatitis (SD)**.
- Determine whether condition-specific taxonomic signatures (particularly regarding dominant commensals *Cutibacterium* and *Staphylococcus*) serve as surface-detectable microbial biomarkers.
- Evaluate the functional metabolic stability of microbial communities across differing scalp disease states.

---

## 🔬 Overview & Rationale

While independent investigations have identified disease-associated bacterial shifts, direct comparisons across conditions have been hindered by disparate extraction protocols, differing hypervariable primer sets, and platform-specific artifacts.

```
                              ┌────────────────────────────────────────┐
                              │ 6 NCBI BioProjects (683 Total Subjects)│
                              └───────────────────┬────────────────────┘
                                                  │ Swab-based Standardized Harmonization
                                                  ▼
             ┌────────────────────────────────────┼────────────────────────────────────┐
             │                                    │                                    │
             ▼                                    ▼                                    ▼
┌──────────────────────────┐         ┌──────────────────────────┐         ┌──────────────────────────┐
│  Alopecia Areata (AA)    │         │ Androgenetic Alopecia    │         │  Seborrheic Dermatitis   │
│  (Patients vs. Controls) │         │ (AGA) (Cases vs. Controls│         │  (SD) (Cases vs. Controls│
└──────────────────────────┘         └──────────────────────────┘         └──────────────────────────┘
```

By curating 6 BioProjects with platform-matched healthy controls and applying uniform computational workflows, this project reveals how localized microenvironmental stress and host physiology shape condition-specific dysbiosis.

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">🗂️</div>
    <h4>Multi-Disease Case-Control Curation</h4>
    <p>Systematic harmonization of 683 subjects across 6 NCBI BioProjects, matching AA (n=40), AGA (n=118), and SD (n=213) cohorts against within-project platform-matched healthy controls (n=312 total controls).</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🧬</div>
    <h4>Standardized DADA2 Genus-Level Resolution</h4>
    <p>ASVs inferred through a unified DADA2 pipeline and classified against full-length 16S rRNA reference databases, resolving primer-specific heterogeneity to robust genus-level comparisons.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">📐</div>
    <h4>Compositional Data Analysis (CLR & PERMANOVA)</h4>
    <p>Applied Total-Sum Scaling (TSS) and Centered Log-Ratio (CLR) transformations with False Discovery Rate (FDR) corrections to eliminate library-size biases in relative abundance testing.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">⚙️</div>
    <h4>Predictive Functional Profiling (PICRUSt2)</h4>
    <p>Reconstructed metagenomic functional repertoires, mapping predicted enzyme commissions, KEGG orthology pathways, and MetaCyc metabolic categories across healthy and disease states.</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Condition-Specific Microbial Biomarkers**: Identifies distinct taxonomic shifts in *Cutibacterium* and *Staphylococcus* that reflect underlying follicular distress and altered surface lipid microenvironments across AA, AGA, and SD.
2. **Functional Plasticity vs. Compositional Shift**: Demonstrates that while core metabolic pathways remain conserved across scalp disorders, differing taxa execute these shared functions, potentially producing distinct bioactive metabolic outputs.
3. **Informing Precision Scalp Therapeutics**: Provides rational microbiological targets for anti-inflammatory topical formulations, pre/probiotic interventions, and personalized scalp care regimens.

---

## 🧭 Project Workflow & Current Progress

<!-- Universal Standard 7-Step Progress Bar -->
<div class="arrow-progress-container">
  <div class="arrow-step step-done step-c1">
    <span class="step-name">Conceptualization</span>
  </div>
  <div class="arrow-step step-done step-c2">
    <span class="step-name">IRB & Study Initiation</span>
  </div>
  <div class="arrow-step step-done step-c3">
    <span class="step-name">Data Acquisition</span>
  </div>
  <div class="arrow-step step-done step-c4">
    <span class="step-name">Analysis & Viz</span>
  </div>
  <div class="arrow-step step-done step-c5">
    <span class="step-name">Manuscript Prep</span>
  </div>
  <div class="arrow-step step-active step-c6">
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
    <h3>Submission & Peer Review Underway</h3>
    <p>The research manuscript investigating comparative scalp dysbiosis across AA, AGA, and SD has been completed and submitted for peer-reviewed journal evaluation.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
