---
layout: default
permalink: /projects/normal-scalp-shotgun-metagenomics/
title: "Multi-Kingdom Scalp Metagenome Reference: 8 BioProjects"
author_profile: true
---

<div class="project-header-box" style="border-left-color: #0d9488; background: linear-gradient(135deg, #f0fdfa 0%, #f8fafc 100%);">
  <div class="proj-meta-badge" style="color: #0d9488;">PROJECT #12 · INTEGRATIVE SHOTGUN METAGENOMICS</div>
  <h1 class="hero-title" style="margin-bottom: 0.6rem;">Cross-Cohort Shotgun Metagenomic Architecture of the Healthy Human Scalp Microbiome</h1>
  <p class="proj-lead-text">
    A standardized, cross-cohort multi-kingdom meta-analysis synthesizing raw whole-metagenome shotgun sequencing datasets from <strong>8 independent NCBI SRA BioProjects</strong>. This study establishes a unified, ultra-high-resolution reference atlas of the normal scalp microbiome spanning <strong>bacteria, fungi (mycobiome), viruses (virome), and uncultivated microbial dark matter</strong>.
  </p>
  <div class="proj-info-bar">
    <span>🔬 <strong>Modality:</strong> Whole-Genome Shotgun (WGS) & Multi-Kingdom MAGs</span>
    <span>👥 <strong>Data Source:</strong> 8 Public BioProjects (NCBI SRA Scalp Swabs)</span>
    <span>📊 <strong>Taxa Covered:</strong> Bacteria, Fungi (Malassezia spp.), Viruses & Phages</span>
    <span>📍 <strong>Status:</strong> Analysis & Reconstruction</span>
  </div>
</div>

<!-- Standard 7-Stage Workflow Ribbon -->
<div class="arrow-progress-container">
  <div class="arrow-step step-c1">
    <span class="step-badge">01</span>
    <span class="step-name">SRA Acquisition</span>
  </div>
  <div class="arrow-step step-c2">
    <span class="step-badge">02</span>
    <span class="step-name">Host Depletion</span>
  </div>
  <div class="arrow-step step-c3">
    <span class="step-badge">03</span>
    <span class="step-name">Taxonomic Profiling</span>
  </div>
  <div class="arrow-step step-c4">
    <span class="step-badge">04</span>
    <span class="step-name">Multi-Kingdom MAGs</span>
  </div>
  <div class="arrow-step step-c5">
    <span class="step-badge">05</span>
    <span class="step-name">Virome / Mycobiome</span>
  </div>
  <div class="arrow-step step-c6 step-active">
    <span class="step-badge">06</span>
    <span class="step-name">Comparative Profiling</span>
  </div>
  <div class="arrow-step step-c7">
    <span class="step-badge">07</span>
    <span class="step-name">Reference Atlas</span>
  </div>
</div>

<!-- Active Stage Highlight Box -->
<div class="status-highlight-card" style="border-left-color: #0d9488; background: #f0fdfa;">
  <div class="status-badge-pulse" style="background: #0d9488;">CURRENT STAGE: 06</div>
  <div class="status-content-wrap">
    <h3 style="color: #115e59;">Comparative Profiling & Multi-Kingdom Baseline Harmonization</h3>
    <p style="color: #0f766e;">
      Harmonizing cross-study batch effects across 8 BioProjects, integrating bacterial species-level strain abundances with fungal (Malassezia) and viral (phage & eukaryotic virus) genomic assemblies to construct the definitive normal scalp baseline.
    </p>
  </div>
</div>

---

## 📌 Background & Scientific Rationale

The human scalp represents an ecologically distinct, lipid-rich cutaneous niche characterized by high follicular density, active sebum secretion, and continuous exposure to environmental stressors. While prior investigations into scalp disorders (such as alopecia areata, androgenetic alopecia, and seborrheic dermatitis) have largely relied on **16S rRNA amplicon sequencing**, several critical gaps remain:

1. **Resolution Constraints:** 16S amplicon data are limited to genus-level classifications and cannot distinguish pathogenic strains from commensal strains (e.g., specific *Cutibacterium acnes* phylotypes vs. *Staphylococcus epidermidis/capitis* strains).
2. **Kingdom-Blind Blindspots:** 16S sequencing exclusively profiles bacteria, completely omitting fungal communities (such as *Malassezia restricta* and *M. globosa*), bacteriophages, and eukaryotic viruses that play fundamental roles in scalp homeostasis.
3. **Cohort & Batch Heterogeneity:** Independent shotgun datasets exist in the public domain (NCBI SRA), but differences in DNA extraction, sequencing platforms, and informatics pipelines have prevented the establishment of a cohesive baseline.

This project addresses these challenges by applying a **standardized, reproducible bioinformatics pipeline** to 8 publicly available shotgun metagenomic BioProjects, providing a strain-level, multi-kingdom reference for translational scalp research.

---

## 🎯 Research Objectives

<div class="pillars-grid">
  <div class="pillar-card">
    <div class="pillar-icon">🧬</div>
    <div class="pillar-content">
      <h3>Multi-Kingdom Taxonomic Resolution</h3>
      <p>Simultaneously characterize bacterial, fungal (mycobiome), and viral (virome) communities on the normal human scalp surface at species and strain levels.</p>
    </div>
  </div>
  <div class="pillar-card">
    <div class="pillar-icon">🧩</div>
    <div class="pillar-content">
      <h3>Multi-Kingdom MAGs Reconstruction</h3>
      <p>Perform <em>de novo</em> assembly and binning to construct high-quality Metagenome-Assembled Genomes (MAGs) of uncultivated commensal strains and resident phages.</p>
    </div>
  </div>
  <div class="pillar-card">
    <div class="pillar-icon">🌐</div>
    <div class="pillar-content">
      <h3>Cross-Study Harmonization</h3>
      <p>Mitigate cross-cohort technical batch effects across 8 independent BioProjects using CLR transformations and standardized host depletion.</p>
    </div>
  </div>
  <div class="pillar-card">
    <div class="pillar-icon">📈</div>
    <div class="pillar-content">
      <h3>Establish Health Baselines</h3>
      <p>Define quantitative normal ranges for the <em>Cutibacterium</em>-to-<em>Staphylococcus</em> ratio, <em>Malassezia</em> clade distribution, and functional metabolic resistomes.</p>
    </div>
  </div>
</div>

---

## 🔬 Study Design & Multi-Kingdom Pipeline

The study utilizes high-throughput shotgun metagenomic sequencing runs from **8 public BioProjects** deposited in the NCBI Sequence Read Archive (SRA), derived specifically from scalp swab samples of healthy individuals.

```
       [ 8 Public BioProjects (NCBI SRA Scalp Swabs) ]
                              │
                              ▼
        [ Step 1: Preprocessing & Human Host Depletion ]
          - Adapter & Low-Quality Trimming (fastp / MultiQC)
          - Stringent Host Removal (Bowtie2 vs. hg38/GRCh38)
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
 [ 1. Bacteriome ]     [ 2. Mycobiome ]      [ 3. Virome & Phage ]
  • Kraken2 / Bracken   • Fungal Marker DB    • RVDB / Curated NCBI
  • MEGAHIT Assembly    • EukCC / BUSCO       • De novo Prophage Mining
  • GTDB-Tk & dRep MAGs • Malassezia Clades   • Host-Phage Interaction
        └─────────────────────┬─────────────────────┘
                              │
                              ▼
       [ Multi-Kingdom Functional & Ecological Integration ]
         - HUMAnN3 / MetaCyc Core Metabolic Pathway Profiling
         - Trans-Kingdom Inter-Species Correlation Networks
         - Robust Reference Dataset for Scalp Dysbiosis
```

### 1. Quality Control & Host Decontamination
Raw shotgun paired-end reads are filtered to remove low-quality bases (Phred score < 25) and sequencing adapters. Given the high host DNA content typical of cutaneous swab samples, reads are aligned against the human reference genome (`GRCh38/hg38`) via Bowtie2. Only non-human, high-quality microbial reads are retained for downstream multi-kingdom reconstruction.

### 2. Multi-Kingdom MAG Reconstruction & Profiling
- **Bacterial MAGs:** Unmapped reads undergo *de novo* assembly using MEGAHIT. Contigs are binned via tetranucleotide frequency and coverage profiles. Assembly quality and contamination are assessed using CheckM/GUNC, dereplicated at 95% ANI via dRep, and classified with GTDB-Tk.
- **Fungal Profiling (Mycobiome):** High-depth eukaryotic binning combined with EukCC and lineage-specific BUSCO evaluations is applied to resolve *Malassezia restricta*, *Malassezia globosa*, and other cutaneous fungal commensals.
- **Virome & Bacteriophage Discovery:** Both reference-based mapping against the Reference Viral Database (RVDB) and *in silico* prophage identification are implemented to characterize resident scalp bacteriophages (e.g., *Cutibacterium* and *Staphylococcus* phages) and eukaryotic virus families.

---

## 💡 Scientific Significance & Clinical Impact

- **First Multi-Kingdom Scalp Metagenomic Reference:** Bridges the gap left by 16S rRNA surveys by delivering a comprehensive atlas of bacterial strains, fungal species (*Malassezia*), and viral/phage networks on the normal scalp.
- **Foundational Baseline for Hair & Scalp Disorders:** Provides the essential control baseline required to distinguish true microbial dysbiosis from natural physiological variation in alopecia areata, androgenetic alopecia, and seborrheic dermatitis.
- **Open Science & Reproducible Workflows:** All computational pipelines, host-depletion protocols, and curated MAG catalogs are released as open-access bioinformatics workflows for the global dermatologic community.

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects</a>
  <a href="mailto:jwchoi.md@gmail.com" class="btn-inquire">Inquire Collaboration</a>
</div>
