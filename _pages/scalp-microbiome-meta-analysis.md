---
layout: single
title: "Meta-Analysis of the Normal Scalp Microbiome: Bacteriome Profiles and Variation Across Public 16S Datasets"
permalink: /projects/scalp-microbiome-meta-analysis/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "dna"
---

<div class="project-header-box">
  <div class="proj-meta-badge">BIOINFORMATICS & TRANSLATIONAL MICROBIOME</div>
  <p class="proj-lead-text">
    Establishing a unified reference for the normal scalp bacteriome by harmonizing <b>975 normal samples</b> across <b>17 public BioProjects</b> using standardized bioinformatics workflows.
  </p>
  <div class="proj-info-bar">
    <span><b>Study Design:</b> Integrative Meta-Analysis</span>
    <span><b>Stack:</b> R, phyloseq, DADA2, Snakemake</span>
    <span><b>Code:</b> <a href="https://github.com/jwchoi-derm-lab" target="_blank">GitHub Repository</a></span>
  </div>
</div>

---

## 📌 Overview & Rationale

The human scalp harbors a complex and dynamic microbial ecosystem. While bacterial dysbiosis has been implicated in common scalp disorders—including **alopecia areata, androgenetic alopecia, seborrheic dermatitis, and folliculitis**—a globally unified baseline reference for the *healthy* scalp microbiome has been lacking. Previous individual studies have suffered from small sample sizes, heterogeneous sampling protocols, and disparate bioinformatic pipelines.

### Purpose of this Study
To systematically characterize the normal scalp bacteriome across multiple sampling modalities (hair shafts, swabs, tissue biopsies) and demographic strata (age, sex, ethnicity), establishing an essential baseline for differentiating healthy physiological variations from disease-associated dysbiosis.

---

## 🛠️ Key Pipeline & Methodological Features

<div class="feature-grid">
  <div class="feature-card">
    <h4>🔄 Data Harmonization</h4>
    <p>Pooled raw 16S rRNA sequencing reads from 17 independent NCBI BioProjects, re-processed with a uniform DADA2 / amplicon sequence variant (ASV) pipeline.</p>
  </div>
  <div class="feature-card">
    <h4>🔬 Multi-Modal Comparison</h4>
    <p>Rigorous comparative profiling across hair shaft, surface swab, and tissue biopsy sampling techniques.</p>
  </div>
  <div class="feature-card">
    <h4>📊 Demographic Stratification</h4>
    <p>Quantitative assessment of microbial diversity, taxonomic composition, and age/sex/racial determinants.</p>
  </div>
  <div class="feature-card">
    <h4>💻 Open & Reproducible</h4>
    <p>Complete statistical and visualization workflows implemented in R with reproducible scripts.</p>
  </div>
</div>

---

## 📊 Abstract & Core Findings

```
========================================================================================
[Dataset Scale] 17 BioProjects  |  975 Healthy Scalp Samples  |  Multi-Cohort Harmonized
========================================================================================
```

### 1. Sampling Modality Disparities
- **Swab & Tissue Biopsies**: Heavily dominated by *Actinomycetota* and *Bacillota*, with high relative abundance of ***Cutibacterium***.
- **Hair Shafts**: Displayed a markedly distinct microbial landscape enriched with ***Pseudomonadota*** and a notable depletion of *Cutibacterium*.

### 2. Demographic Determinants of Scalp Bacteriome
- **Age-Dependent Shifts**: *Cutibacterium* abundance exhibited a statistically significant positive correlation with advancing age.
- **Sex Differences**: Relative abundance of *Cutibacterium* was significantly higher in females, whereas ***Staphylococcus*** predominated in males.
- **Racial Variations**: *Staphylococcus* was dominant in African and Caucasian cohorts, whereas *Cutibacterium* prevailed in Asian populations.

---

## 🧬 Clinical & Translational Significance

1. **Distinguishing Baseline from Disease**: Provides quantitative thresholds to differentiate true pathological dysbiosis in inflammatory hair/scalp diseases from normal variation.
2. **Standardization for Future Trials**: Demonstrates that sampling methodology (swab vs. hair vs. tissue) significantly dictates microbial readouts, establishing clear guidelines for clinical trial designs.
3. **Targeted Therapeutics**: Informs the development of precision prebiotics, postbiotics, and microbial therapeutics tailored to scalp biogeography.

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to All Projects</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire About this Pipeline</a>
</div>
