---
layout: single
permalink: /projects/scalp-microbiome-meta-analysis/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "dna"
---

<div class="project-header-box">
  <div class="proj-meta-badge">BIOINFORMATICS & TRANSLATIONAL MICROBIOME</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">Integrative Pooled Analysis of the Normal Scalp Microbiome: Bacteriome Profiles and Variation Across Public 16S rRNA Datasets</h2>
  <p class="proj-lead-text">
    Establishing a unified global reference for the healthy human scalp bacteriome by integrating <b>975 normal samples</b> across <b>17 public NCBI BioProjects</b> with a standardized computational pipeline.
  </p>
  <div class="proj-info-bar">
    <span><b>PI:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Large-Scale Pooled Meta-Analysis</span>
    <span><b>Stack:</b> R, DADA2, phyloseq, PICRUSt2, SRA-Toolkit</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

The human scalp represents an ecologically distinct, sebaceous, and hair follicle-dense anatomical niche. While bacterial dysbiosis has been increasingly implicated in inflammatory scalp dermatoses (such as seborrheic dermatitis and folliculitis decalvans) and hair disorders (such as alopecia areata and androgenetic alopecia), a unified and robust reference for the **healthy scalp microbiome** remains lacking.

This study aims to:
- Establish a comprehensive baseline reference for the normal scalp bacteriome by harmonizing multi-cohort 16S rRNA amplicon sequencing data.
- Systematically evaluate how **sampling modalities** (swabs, hair shafts, tissue biopsies) shape taxonomic and diversity readouts.
- Characterize population-level physiological determinants, including **age, sex, and ethnicity**, across standardized datasets.

---

## 🔬 Overview & Rationale

Prior scalp microbiome studies have been largely constrained by small sample sizes, heterogeneous sampling techniques, variable hypervariable regions (e.g., V1–V3 vs. V4), and disparate downstream bioinformatic pipelines. Consequently, true biological variation could not be clearly distinguished from technical artifacts.

```
                              ┌────────────────────────────────────────┐
                              │ 17 NCBI BioProjects (6,455 Raw Runs)   │
                              └───────────────────┬────────────────────┘
                                                  │ Rigorous Filtering (Normal Scalp Only)
                                                  ▼
                              ┌────────────────────────────────────────┐
                              │ 975 Harmonized Scalp Samples (16S rRNA)│
                              └───────────────────┬────────────────────┘
                                                  │
                ┌─────────────────────────────────┼─────────────────────────────────┐
                │                                 │                                 │
                ▼                                 ▼                                 ▼
      [Swabs: Surface Niche]             [Hair Shafts: Outer Niche]         [Tissue: Follicular Niche]
```

By pooling raw public sequencing accessions from the NCBI Sequence Read Archive (SRA) and applying a uniform bioinformatic framework, this project establishes a unified baseline essential for future clinical trials and disease-association investigations.

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">📥</div>
    <h4>Data Acquisition & Curation</h4>
    <p>Systematic screening of NCBI SRA accessions, extracting paired-end/single-end FASTQ files across 17 independent BioProjects while excluding lesional, treated, and non-baseline timepoints.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔄</div>
    <h4>Per-Project DADA2 Denoising</h4>
    <p>ASV inference and error models computed separately per BioProject to prevent cross-batch chimeric artifacts, followed by taxonomic assignment via SILVA v138.2 naive Bayesian classifier.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">⚖️</div>
    <h4>Iterative Subsampling & CLR</h4>
    <p>Mitigated severe cross-study sample size imbalances through 100-iteration random subsampling and Centered Log-Ratio (CLR) compositional transformations.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🧬</div>
    <h4>Multi-Modal Ecological Profiling</h4>
    <p>Comprehensive comparative analysis dissecting microbial community stratification across three distinct biological microenvironments: superficial swabs, exposed hair shafts, and deep tissue biopsies.</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Standardizing Normal Baselines**: Establishes an essential reference to discern natural demographic variation (age, sex, race) from true pathological dysbiosis in inflammatory hair and scalp disorders.
2. **Methodological Benchmarking**: Demonstrates that sampling modality (swabs vs. hair shafts vs. biopsies) targets distinct microecological compartments, serving as a critical guideline for future clinical trial designs.
3. **Targeted Therapeutic Implications**: Informs the development of precision microbiome therapeutics, prebiotics, and topical scalp formulations by defining the physiological distribution of core cutaneous commensals.

---

## 🧭 Project Workflow & Current Progress

<!-- Chevron Arrow Ribbon Progress Bar -->
<div class="arrow-progress-container">
  <div class="arrow-step step-done step-c1">
    <span class="step-idx">.01</span>
    <span class="step-name">Concept</span>
  </div>
  <div class="arrow-step step-done step-c2">
    <span class="step-idx">.02</span>
    <span class="step-name">SRA Mining</span>
  </div>
  <div class="arrow-step step-done step-c3">
    <span class="step-idx">.03</span>
    <span class="step-name">DADA2</span>
  </div>
  <div class="arrow-step step-done step-c4">
    <span class="step-idx">.04</span>
    <span class="step-name">Analysis</span>
  </div>
  <div class="arrow-step step-done step-c5">
    <span class="step-idx">.05</span>
    <span class="step-name">Manuscript</span>
  </div>
  <div class="arrow-step step-active step-c6">
    <span class="step-idx">.06</span>
    <span class="step-name">Peer Review</span>
  </div>
  <div class="arrow-step step-pending step-c7">
    <span class="step-idx">.07</span>
    <span class="step-name">Publication</span>
  </div>
</div>

<!-- Highlighted Active Status Card -->
<div class="status-highlight-card">
  <div class="status-badge-pulse">CURRENT STAGE</div>
  <div class="status-content-wrap">
    <h3>Stage .06: Peer Review Underway</h3>
    <p>The full research manuscript and reproducible analytical pipeline have been finalized and submitted to a peer-reviewed academic journal for expert evaluation.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
