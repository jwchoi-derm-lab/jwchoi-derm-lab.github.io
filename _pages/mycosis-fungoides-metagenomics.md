---
layout: single
permalink: /projects/mycosis-fungoides-metagenomics/
author_profile: true
toc: true
toc_label: "Project Contents"
toc_icon: "dna"
---

<div class="project-header-box" style="background: linear-gradient(135deg, #f5f3ff 0%, #f8fafc 100%) !important; border-left: 5px solid #7c3aed !important;">
  <div class="proj-meta-badge" style="color: #7c3aed !important;">BIOINFORMATICS & CUTANEOUS LYMPHOMA METAGENOMICS</div>
  <h2 style="margin: 0.3rem 0 0.8rem 0; font-size: 1.35rem; color: #0f172a; line-height: 1.3;">A Comprehensive Shotgun Metagenomic Investigation of the Skin Microbiome in Mycosis Fungoides: Public SRA Meta-Analysis</h2>
  <p class="proj-lead-text">
    An integrated multi-kingdom bioinformatic meta-analysis utilizing <b>public shotgun metagenomic datasets</b> from NCBI SRA to reconstruct <b>Metagenome-Assembled Genomes (MAGs)</b> and viral/fungal landscape in cutaneous T-cell lymphoma.
  </p>
  <div class="proj-info-bar">
    <span><b>PI:</b> Jee Woong Choi, MD, PhD (Ajou Univ.)</span>
    <span><b>Study Type:</b> Shotgun Metagenomic Meta-Analysis</span>
    <span><b>Stack:</b> Kraken2, MEGAHIT, GUNC, GTDB-Tk, EukCC, RVDB</span>
  </div>
</div>

---

## 🎯 Purpose of this Study

Mycosis fungoides (MF), the most common form of cutaneous T-cell lymphoma (CTCL), represents a chronic malignancy shaped by intricate interactions between neoplastic T cells, epidermal barrier breakdown, and the local immune microenvironment. While microbial colonization has been implicated in driving malignant T-cell proliferation and persistent cutaneous inflammation, previous studies were constrained by small sample sizes or limited 16S rRNA resolution.

This study aims to:
- Establish a standardized, large-scale shotgun metagenomic meta-analysis of the MF skin microbiome using publicly deposited raw sequencing datasets from the NCBI Sequence Read Archive (SRA).
- Perform high-resolution multi-kingdom taxonomic profiling across **bacteria, fungi, viruses (HPV, HPyV, HHV), and archaea**.
- Reconstruct high-quality **Metagenome-Assembled Genomes (MAGs)** and characterize predicted metabolic resistomes and oncogenic functional pathways.

---

## 🔬 Overview & Rationale

Shotgun metagenomics enables strain-level identification and functional gene mapping, overcoming the technical limitations of conventional amplicon sequencing.

<!-- Modern 3-Tier Multi-Kingdom Metagenomic Flow -->
<div class="study-flow-container">
  
  <div class="flow-tier-box tier-ingest" style="border-top-color: #7c3aed !important;">
    <div class="tier-badge" style="background: #ede9fe !important; color: #5b21b6 !important;">STEP 1 · DATA INGESTION & HOST DECONTAMINATION</div>
    <h3>Public SRA Shotgun Datasets (MF Lesions vs. Healthy Controls)</h3>
    <p>Automated retrieval of raw shotgun sequencing runs, adapter trimming, Phred quality filtering (>Q20), and rigorous human host DNA depletion via reference genome (GRCh38/hg38) alignment.</p>
  </div>

  <div class="flow-connector-arrow">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #7c3aed !important; background: #f5f3ff !important; border-color: #ddd6fe !important;">Multi-Kingdom Metagenomic Assembly & Deconvolution</span>
    <span class="connector-line"></span>
  </div>

  <div class="niche-grid">
    
    <div class="niche-card" style="border-top-color: #7c3aed !important;">
      <div class="niche-icon">🧬</div>
      <h4>Bacterial MAGs</h4>
      <span class="niche-tag" style="background: #f5f3ff !important; color: #5b21b6 !important;">MEGAHIT + GTDB-Tk</span>
      <p>De novo assembly, tetranucleotide binning, GUNC chimera filtering, and 95% ANI dereplication for novel strain identification.</p>
    </div>

    <div class="niche-card" style="border-top-color: #ec4899 !important;">
      <div class="niche-icon">🍄</div>
      <h4>Fungal & Eukaryotic MAGs</h4>
      <span class="niche-tag" style="background: #fdf2f8 !important; color: #9d174d !important;">EukCC + BUSCO</span>
      <p>Dedicated eukaryotic binning and lineage-specific completeness profiling to characterize mycobiome signatures.</p>
    </div>

    <div class="niche-card" style="border-top-color: #06b6d4 !important;">
      <div class="niche-icon">🦠</div>
      <h4>Viral / Phage Discovery</h4>
      <span class="niche-tag" style="background: #ecfeff !important; color: #0e7490 !important;">RVDB + iTOL Phylogenetics</span>
      <p>Profiling Papillomaviridae (HPV), Polyomaviridae, Herpesviridae, and bacteriophages via conserved open reading frame mapping.</p>
    </div>

  </div>

  <div class="flow-connector-arrow" style="margin-top: 1.2rem;">
    <span class="connector-line"></span>
    <span class="connector-text" style="color: #7c3aed !important; background: #f5f3ff !important; border-color: #ddd6fe !important;">Differential Abundance & Metabolic Pathway Reconstruction</span>
    <span class="connector-line"></span>
  </div>

  <div class="flow-tier-box tier-cohort" style="border-top-color: #6d28d9 !important;">
    <div class="tier-badge" style="background: #ede9fe !important; color: #5b21b6 !important;">TRANSLATIONAL OUTCOME</div>
    <h3>Comprehensive Multi-Omics Microbial Landscape of Mycosis Fungoides</h3>
    <p>Uncovering targetable microbial drivers, immune-modulating peptides, and diagnostic microbiome biomarkers in cutaneous lymphoma.</p>
  </div>

</div>

---

## 🛠️ Methodological Features

<div class="method-grid">
  
  <div class="method-card">
    <div class="method-icon">📥</div>
    <h4>Standardized Public SRA Harmonization</h4>
    <p>Automated pipeline ingesting multi-study shotgun metagenomic datasets, applying uniform adapter removal and stringent host-read subtraction.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔄</div>
    <h4>High-Resolution Kraken2 Profiling</h4>
    <p>Standardized k-mer taxonomic assignment against a curated reference database, normalized for depth and cross-study comparability.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🧩</div>
    <h4>Multi-Kingdom De Novo MAG Binning</h4>
    <p>Integration of MEGAHIT assembly, dRep 95% ANI clustering, GUNC quality assessment, and GTDB-Tk taxonomic assignment across kingdoms.</p>
  </div>

  <div class="method-card">
    <div class="method-icon">🔬</div>
    <h4>Viral Genome Discovery & Integration</h4>
    <p>In silico discovery leveraging RVDB to resolve oncogenic viral speciation, genomic integration, and phylogenetic placement (iTOL).</p>
  </div>

</div>

---

## 💡 Translational & Clinical Significance

1. **Overcoming Heterogeneity in Rare CTCL**: Establishes the first reproducible shotgun metagenomic meta-analysis framework for cutaneous lymphoma.
2. **Multi-Kingdom Oncogenic Insights**: Expands understanding beyond bacteria to include fungal dysbiosis, viral co-infections, and phage-host dynamics.
3. **Open Science & Pipeline Portability**: Delivers a fully transparent computational workflow adaptable to other rare cutaneous neoplastic diseases.

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

<div class="status-highlight-card" style="background: #f5f3ff !important; border-left-color: #7c3aed !important;">
  <div class="status-badge-pulse" style="background: #7c3aed !important;">CURRENT STAGE</div>
  <div class="status-content-wrap">
    <h3 style="color: #4c1d95 !important;">Stage: Metagenomic Analysis & Visualization Underway</h3>
    <p style="color: #6d28d9 !important;">Public SRA shotgun datasets have been acquired and host-depleted; multi-kingdom MAG binning, diversity metrics, and viral phylogenetics are actively in progress.</p>
  </div>
</div>

---

<div class="project-nav-footer">
  <a href="/projects/" class="btn-back">← Back to Projects Overview</a>
  <a href="mailto:jwchoi.derm.lab@gmail.com" class="btn-inquire">✉️ Inquire for Collaboration</a>
</div>
