---
layout: single
permalink: /projects/normal-scalp-shotgun-metagenomics/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "dna"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #f0fdf4 0%, #f8fafc 100%) !important; border-left: 5px solid #059669 !important;">
  <div class="proj-meta-badge" style="color: #059669 !important;">BIOINFORMATICS & SCALP SHOTGUN METAGENOMICS</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">A Comprehensive Shotgun Metagenomic Investigation of the Normal Scalp Microbiome: Public SRA Meta-Analysis Across 8 BioProjects</h2>
  <p class="proj-lead-text">
    An integrated multi-kingdom bioinformatic meta-analysis utilizing <b>public shotgun metagenomic datasets</b> from 8 NCBI SRA BioProjects to reconstruct <b>Metagenome-Assembled Genomes (MAGs)</b> and map the comprehensive bacterial, fungal (mycobiome), and viral (virome) landscape of the healthy human scalp.
  </p>
  <div class="proj-info-bar">
    <span><b>PI:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Shotgun Metagenomic Meta-Analysis (8 BioProjects)</span>
    <span><b>Stack:</b> Kraken2, MEGAHIT, GUNC, GTDB-Tk, EukCC, RVDB</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

The human scalp represents a unique and complex cutaneous microenvironment characterized by dense terminal hair follicles, rich sebum excretion, and constant environmental exposure. Although bacterial dysbiosis has been implicated in scalp disorders such as alopecia areata, androgenetic alopecia, and seborrheic dermatitis, establishing a definitive baseline has been constrained by small cohorts and the kingdom-restricted resolution of 16S rRNA amplicon sequencing.

This study aims to:
- Establish a standardized, large-scale shotgun metagenomic meta-analysis of the normal scalp surface microbiome across **8 public NCBI SRA BioProjects** using swab-derived datasets.
- Perform high-resolution multi-kingdom taxonomic profiling across **bacteria, fungi (Malassezia spp.), viruses (bacteriophages & eukaryotic viruses), and archaea**.
- Reconstruct high-quality **Metagenome-Assembled Genomes (MAGs)** and delineate the core metabolic pathways and trans-kingdom ecological equilibrium of the healthy scalp.

---

## 🔬 Overview & Rationale

Shotgun metagenomics enables species- and strain-level identification, viral detection, and functional gene mapping, providing a comprehensive multi-kingdom reference atlas for dermatologic research.

<!-- Modern 3-Tier Multi-Kingdom Metagenomic Flow -->
<div class="study-flow-container">
  
  <div class="flow-tier-box tier-ingest" style="border-top-color: #059669 !important;">
    <div class="tier-badge" style="background: #d1fae5 !important; color: #065f46 !important;">STEP 1 · DATA INGESTION & HOST DECONTAMINATION</div>
    <h3>Public SRA Shotgun Datasets (8 Scalp Swab BioProjects)</h3>
    <p>Automated retrieval of raw whole-metagenome sequencing runs from 8 NCBI SRA BioProjects, adapter trimming, Phred quality filtering (>Q20), and rigorous human host DNA depletion via reference genome (GRCh38/hg38) alignment.</p>
  </div>

  <div class="flow-connector-arrow">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #059669 !important; background: #f0fdf4 !important; border-color: #a7f3d0 !important;">Multi-Kingdom Metagenomic Assembly & Deconvolution</span>
    <span class="connector-line"></span>
  </div>

  <div class="niche-grid">
    
    <div class="niche-card" style="border-top-color: #059669 !important;">
      <div class="niche-icon">🧬</div>
      <h4>Bacterial MAGs & Strains</h4>
      <span class="niche-tag" style="background: #f0fdf4 !important; color: #065f46 !important;">MEGAHIT + GTDB-Tk</span>
      <p>De novo assembly, tetranucleotide binning, GUNC chimera filtering, and 95% ANI dereplication to resolve Cutibacterium and Staphylococcus strain variations.</p>
    </div>

    <div class="niche-card" style="border-top-color: #d97706 !important;">
      <div class="niche-icon">🍄</div>
      <h4>Fungal & Eukaryotic MAGs</h4>
      <span class="niche-tag" style="background: #fef3c7 !important; color: #92400e !important;">EukCC + BUSCO</span>
      <p>Dedicated eukaryotic binning and lineage-specific completeness profiling to characterize Malassezia restricta, M. globosa, and uncultured fungal clades.</p>
    </div>

    <div class="niche-card" style="border-top-color: #0284c7 !important;">
      <div class="niche-icon">🦠</div>
      <h4>Virome & Phage Discovery</h4>
      <span class="niche-tag" style="background: #e0f2fe !important; color: #0369a1 !important;">RVDB + iTOL Phylogenetics</span>
      <p>Profiling scalp bacteriophages (Cutibacterium/Staphylococcus phages) and eukaryotic viral families via conserved marker mapping and de novo assembly.</p>
    </div>

  </div>

  <div class="flow-connector-arrow" style="margin-top: 1.2rem;">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #059669 !important; background: #f0fdf4 !important; border-color: #a7f3d0 !important;">Cross-Cohort Normalization & Metabolic Pathway Reconstruction</span>
    <span class="connector-line"></span>
  </div>

  <div class="flow-tier-box tier-cohort" style="border-top-color: #047857 !important;">
    <div class="tier-badge" style="background: #d1fae5 !important; color: #065f46 !important;">TRANSLATIONAL OUTCOME</div>
    <h3>Comprehensive Multi-Kingdom Reference Atlas of the Healthy Scalp</h3>
    <p>Establishing the foundational multi-kingdom baseline to differentiate normal physiological variation from pathologic dysbiosis across hair and scalp disorders.</p>
  </div>

</div>

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">📥</div>
    <h4>Standardized Public SRA Harmonization</h4>
    <p>Automated pipeline ingesting whole-genome shotgun datasets from 8 independent BioProjects, applying uniform adapter removal and stringent host-read subtraction.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔄</div>
    <h4>Multi-Kingdom Kraken2 Profiling</h4>
    <p>Standardized k-mer taxonomic assignment against a curated multi-kingdom database (bacteria, fungi, viruses), normalized for sequencing depth and cross-study comparability.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🧩</div>
    <h4>Multi-Kingdom De Novo MAG Binning</h4>
    <p>Integration of MEGAHIT assembly, dRep 95% ANI clustering, GUNC quality assessment, and GTDB-Tk/EukCC taxonomic assignment across kingdoms.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔬</div>
    <h4>Viral & Phage Community Characterization</h4>
    <p>In silico discovery leveraging RVDB and curated prophage databases to resolve scalp phage-host dynamics, viral speciation, and phylogenetic placement (iTOL).</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Definitive Multi-Kingdom Reference Baseline**: Establishes the first standardized, multi-kingdom shotgun metagenomic reference atlas for the normal human scalp across multiple independent public cohorts.
2. **Beyond Bacteria to Fungi and Virome**: Expands beyond 16S amplicon limitations to systematically resolve *Malassezia* clade equilibrium, bacteriophage-bacteria regulation, and eukaryotic viral residents.
3. **Open Science & Benchmarking Platform**: Provides a transparent, reproducible computational workflow to benchmark disease-specific dysbiosis in alopecia areata, androgenetic alopecia, and seborrheic dermatitis.

---

## 🧭 Project Workflow & Current Progress

<div class="arrow-progress-container">
  <div class="arrow-step step-done step-c1"><span class="step-name">Concept</span></div>
  <div class="arrow-step step-done step-c2"><span class="step-name">IRB &<br>Initiation</span></div>
  <div class="arrow-step step-done step-c3"><span class="step-name">Data<br>Acquisition</span></div>
  <div class="arrow-step step-active step-c4"><span class="step-badge">CURRENT</span><span class="step-name">Analysis &<br>Viz</span></div>
  <div class="arrow-step step-pending step-c5"><span class="step-name">Manuscript<br>Prep</span></div>
  <div class="arrow-step step-pending step-c6"><span class="step-name">Peer Review</span></div>
  <div class="arrow-step step-pending step-c7"><span class="step-name">Publication</span></div>
</div>

<div class="status-highlight-card" style="background: #f0fdf4 !important; border-left-color: #059669 !important;">
  <div class="status-badge-pulse" style="background: #059669 !important;">CURRENT STAGE</div>
  <div class="status-content-wrap">
    <h3 style="color: #064e3b !important;">Stage: Metagenomic Analysis & Visualization Underway</h3>
    <p style="color: #047857 !important;">Public SRA shotgun datasets from 8 BioProjects have been acquired and host-depleted; multi-kingdom MAG binning, fungal/viral profiling, and diversity metrics are actively in progress.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.md@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
