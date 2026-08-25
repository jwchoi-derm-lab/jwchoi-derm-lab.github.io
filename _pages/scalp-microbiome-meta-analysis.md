---
layout: single
title: "Integrative Pooled Analysis of the Normal Scalp Microbiome: Bacteriome Profiles and Variation Across Public 16S rRNA Datasets"
permalink: /projects/scalp-microbiome-meta-analysis/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "dna"
---

<div class="project-header-box">
  <div class="proj-meta-badge">BIOINFORMATICS & TRANSLATIONAL MICROBIOME</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a;">Integrative Pooled Analysis of the Normal Scalp Microbiome</h2>
  <p class="proj-lead-text">
    Establishing a unified global reference for the healthy human scalp bacteriome by integrating <b>975 normal samples</b> across <b>17 public NCBI BioProjects</b> with a standardized, reproducible computational pipeline.
  </p>
  <div class="proj-info-bar">
    <span><b>PI:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Large-Scale Pooled Meta-Analysis</span>
    <span><b>Stack:</b> R, DADA2, phyloseq, PICRUSt2, SRA-Toolkit</span>
  </div>
</div>

---

## 🧭 Project Workflow & Current Progress

<div class="progress-tracker">
  <div class="step completed">
    <div class="step-num">✓</div>
    <div class="step-label">1. Conceptualization</div>
  </div>
  <div class="step-line active"></div>
  <div class="step completed">
    <div class="step-num">✓</div>
    <div class="step-label">2. Public SRA Mining</div>
  </div>
  <div class="step-line active"></div>
  <div class="step completed">
    <div class="step-num">✓</div>
    <div class="step-label">3. DADA2 Harmonization</div>
  </div>
  <div class="step-line active"></div>
  <div class="step completed">
    <div class="step-num">✓</div>
    <div class="step-label">4. Statistical Modeling</div>
  </div>
  <div class="step-line active"></div>
  <div class="step completed">
    <div class="step-num">✓</div>
    <div class="step-label">5. Manuscript Finalization</div>
  </div>
  <div class="step-line active"></div>
  <div class="step current">
    <div class="step-num">6</div>
    <div class="step-label">6. Peer Review (Current)</div>
  </div>
  <div class="step-line"></div>
  <div class="step pending">
    <div class="step-num">7</div>
    <div class="step-label">7. Publication</div>
  </div>
</div>

<div class="status-callout">
  <span class="status-indicator-dot"></span>
  <b>Current Status: Under Peer Review (2026)</b> — Full research manuscript finalized and submitted for academic journal review.
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
    <p>Mitigated severe cross-study sample size imbalances through 100-iteration random subsampling (yielding permutation-adjusted P-values) and Centered Log-Ratio (CLR) compositional transformations.</p>
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

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
