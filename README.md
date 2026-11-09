scRNA-Seq Glioblastoma Analysis using pySCENIC

Project Overview

This project applies the pySCENIC workflow to a publicly available glioblastoma single-cell RNA sequencing (scRNA-seq) dataset to infer gene regulatory networks and identify key transcription factors involved in glioblastoma cellular states and regulatory programs.



Dataset

GEO Accession

GSE131928



Publication:



Neftel C. et al. (2019)

An Integrative Model of Cellular States, Plasticity, and Genetics for Glioblastoma

Cell



Dataset Link:



https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131928



Selected Dataset

Sample Used

GSM3828672\_Smartseq2\_GBM\_IDHwt\_processed\_TPM.tsv

Reason for Selection

Human glioblastoma dataset

Smart-seq2 sequencing platform

Suitable size for local computation

Different from datasets used in the original SCENIC tutorial

Appropriate for identifying glioblastoma-specific transcriptional regulators

Project Structure

scRNA-Seq-Glioblastoma/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── resources/

│   ├── databases/

│   ├── annotations/

│   └── allTFs\_hg38.txt

│

├── scripts/

│

├── notebooks/

│

├── results/

│   ├── grnboost2/

│   ├── regulons/

│   ├── aucell/

│   └── figures/

│

├── docs/

│

├── README.md

└── requirements.txt

Environment Setup

Create Environment

conda create -n pyscenic\_env python=3.10

conda activate pyscenic\_env

Major Packages

pandas

numpy

scanpy

anndata

matplotlib

seaborn

scikit-learn

pyscenic

arboreto

Dataset Inspection

Original Dataset Dimensions

Genes : 23,686

Cells : 7,930

Missing Values : 0

Data Format

Rows    = Genes

Columns = Cells

Values  = TPM Expression

Data Preprocessing

Quality Filtering

Filtering criteria:



sc.pp.filter\_cells(adata, min\_genes=200)

sc.pp.filter\_genes(adata, min\_cells=3)

Results

Original Matrix

7930 cells × 23686 genes



Filtered Matrix

7930 cells × 22197 genes

Saved as:



data/processed/gbm\_filtered.h5ad

Highly Variable Gene (HVG) Selection

Purpose

Reduce computational complexity

Retain most informative genes

Speed up GRN inference

Method

sc.pp.highly\_variable\_genes(

&#x20;   adata,

&#x20;   n\_top\_genes=5000

)

Result

7930 cells × 5000 genes

Saved files:



data/processed/gbm\_hvg\_5000.h5ad

data/processed/gbm\_hvg\_5000.tsv

SCENIC Resources

1\. Human Transcription Factor List

File:



allTFs\_hg38.txt

Download:



https://resources.aertslab.org/cistarget/tf\_lists/allTFs\_hg38.txt



Purpose:



Provides a curated list of human transcription factors

Restricts GRNBoost2 to biologically meaningful regulators

Reduces computational complexity

Statistics:



Total TFs in database : 1892

TFs present in GBM dataset : 364

2\. Motif Annotation Database

File:



motifs-v10nr\_clust-nr.hgnc-m0.001-o0.0.tbl

Download:



https://resources.aertslab.org/cistarget/



Purpose:



Maps transcription factors to their DNA-binding motifs

Used during the cisTarget motif enrichment step

Helps validate TF-target interactions

3\. cisTarget Ranking Database

File:



hg38\_\_refseq-r80\_\_10kb\_up\_and\_down\_tss.mc9nr.genes\_vs\_motifs.rankings.feather

Download:



https://resources.aertslab.org/cistarget/databases/



Purpose:



Human genome motif-ranking database

Used by cisTarget to identify motif enrichment

Converts co-expression relationships into biologically supported regulatory interactions

Genome:



Species : Homo sapiens

Assembly : hg38

Region : ±10 kb around transcription start sites

SCENIC Workflow

Step 1: Expression Matrix

Input:



7930 cells × 5000 genes

Step 2: GRNBoost2 Network Inference

Input:



gbm\_hvg\_5000.tsv

present\_TFs.txt

Goal:



Infer TF → Target Gene relationships

Command:



pyscenic grn data/processed/gbm\_hvg\_5000.tsv resources/present\_TFs.txt -o results/grnboost2/grnboost2\_network.csv --num\_workers 8

Current Status:



RUNNING

Hardware:



CPU Cores : 20

RAM : 16 GB

Workers : 8

Step 3: cisTarget (Planned)

Input:



grnboost2\_network.csv

motifs-v10nr\_clust-nr.hgnc-m0.001-o0.0.tbl

hg38\_\_refseq-r80\_\_10kb\_up\_and\_down\_tss.mc9nr.genes\_vs\_motifs.rankings.feather

Output:



Regulons

Purpose:



Validate predicted TF-target interactions using motif enrichment analysis.

Step 4: AUCell (Planned)

Input:



Regulons

Expression Matrix

Output:



Regulon Activity Scores

Purpose:



Determine transcription factor activity across individual glioblastoma cells.

Expected Biological Findings

Potential transcription factors expected to be identified:



SOX2

OLIG2

STAT3

MYC

NFIA

NFIB

JUN

FOS

SOX4

WT1

Potential biological processes:



Glioblastoma stemness

Cellular plasticity

Tumor progression

Cell proliferation

Differentiation programs

Regulatory network rewiring

Progress Summary

✅ GitHub repository created



✅ Conda environment created



✅ Dataset downloaded



✅ Dataset inspected



✅ AnnData object created



✅ Gene filtering completed



✅ Highly variable genes selected



✅ Expression matrix exported



✅ Human TFs extracted



✅ SCENIC resources downloaded



✅ pySCENIC configured



✅ GRNBoost2 started



🔄 GRNBoost2 running



⏳ cisTarget pending



⏳ AUCell pending



⏳ Biological interpretation pending

