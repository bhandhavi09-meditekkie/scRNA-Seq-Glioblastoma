Identification and Analysis of Transcription Factor Regulatory Networks in Glioblastoma Using SCENIC
Project overview
This project applies the SCENIC workflow to a single-cell RNA-sequencing expression matrix derived from the glioblastoma dataset GSE131928 to infer candidate transcription factor (TF)-target regulatory relationships and assess regulon activity across cells.

The analysis is intended to investigate transcriptional regulatory programmes associated with glioblastoma cellular heterogeneity.
Research question
Can transcription-factor regulatory network inference from single-cell RNA-sequencing data identify candidate regulatory programmes that may help characterise cellular heterogeneity in glioblastoma?
Dataset
- Dataset: GSE131928
- Study: Neftel et al. (2019), An Integrative Model of Cellular States, Plasticity, and Genetics for Glioblastoma
- GEO record: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131928
- Expression matrix used in this project: gbm_expression_matrix.tsv
- Reported matrix dimensions: 7,930 cells × 22,197 genes
- Important: This is the project’s selected subset/matrix, not the full cell count of the original GEO study.
Workflow
1. Prepare the gene-expression matrix and select highly variable genes (HVGs).
2. Infer candidate TF-target relationships using GRNBoost2.
3. Refine candidate regulons using cisTarget motif-enrichment analysis.
4. Calculate regulon activity across cells using AUCell.
5. Rank and biologically interpret selected TF-labelled entries using relevant literature.
SCENIC stages
- GRNBoost2: Infers candidate TF-target relationships from expression patterns.
- cisTarget: Uses motif enrichment to refine candidate TF-target relationships into regulons.
- AUCell: Estimates the enrichment/activity of regulon target genes among highly expressed genes in individual cells.
These are computational inferences. Motif enrichment and AUCell scores do not, by themselves, prove direct TF binding or causal regulation.
Reported results
The following 20 TF-labelled entries and scores were reported:
TF-labelled entry	Reported score
SOX4(+)	0.173455
HES6(+)	0.141375
NFIL3(+)	0.085255
MAFB(+)	0.075977
JUN(+)	0.073063
STAT1(+)	0.065558
ZNF671(+)	0.062062
IRF1(+)	0.061367
GSX1(+)	0.057273
ATF3(+)	0.053751
DLX5(+)	0.053173
ZNF208(+)	0.051650
BHLHE40(+)	0.051286
NEUROD1(+)	0.048881
OTX2(+)	0.046082
DLX2(+)	0.045098
KLF4(+)	0.044453
EPAS1(+)	0.043626
GLI1(+)	0.042237
ZNF782(+)	0.041086


Score-metric caveat: The source file and column name for this score list must be recorded before interpreting the values as AUCell activity, regulon specificity, GRNBoost2 importance, or another metric.
Preliminary interpretation
SOX4 and HES6 have the two highest reported scores. SOX4 is particularly interesting in light of the GBM cellular-state framework described by Neftel et al. (2019), which includes neural progenitor-like (NPC-like) malignant cell states. HES6 has also been investigated in glioma proliferation.

Other TFs suggest hypotheses for further investigation:
- JUN and ATF3: stress-responsive and adaptive transcriptional programmes.
- STAT1 and IRF1: interferon/cytokine-associated programmes.
- MAFB: potentially myeloid/macrophage-associated regulation.
- DLX5, DLX2, NEUROD1 and GSX1: neural developmental or lineage-associated programmes.
- EPAS1: hypoxia-associated transcriptional regulation.
- GLI1: Hedgehog pathway-associated transcriptional regulation.
  
Reproducibility: example commands
The commands below reflect the reported project workflow. 
# GRNBoost2 network inference
pyscenic grn \
  data/processed/gbm_hvg_5000.tsv \
  resources/tf_lists/allTFs_hg38.txt \
  --method grnboost2 \
  --output results/grnboost2/grnboost2_network.csv \
  --num_workers 8

# cisTarget regulon refinement
pyscenic ctx \
  results/grnboost2/grnboost2_network.csv \
  resources/databases/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather \
  --annotations_fname resources/annotations/motifs-v10nr_clust-nr.hgnc-m0.001-o0.0.tbl.txt \
  --expression_mtx_fname data/processed/gbm_hvg_5000.tsv \
  --output results/regulons/regulons.csv \
  --num_workers 8

# AUCell regulon activity scoring
pyscenic aucell \
  data/processed/gbm_hvg_5000.tsv \
  results/regulons/regulons.csv \
  --output results/aucell/aucell_scores.csv \
  --num_workers 2
Check pyscenic grn --help, pyscenic ctx --help, and pyscenic aucell --help for syntax supported by the installed pySCENIC version. The TF list and database must match the organism/genome build and gene identifiers in the expression matrix.
Resources
- SCENIC paper: Aibar et al. (2017), SCENIC: single-cell regulatory network inference and clustering. https://doi.org/10.1038/nmeth.4463
- Glioblastoma dataset paper: Neftel et al. (2019), An Integrative Model of Cellular States, Plasticity, and Genetics for Glioblastoma. https://doi.org/10.1016/j.cell.2019.06.024
- GEO dataset: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131928
- cisTarget resources: https://resources.aertslab.org/cistarget/
- Human TF list: https://resources.aertslab.org/cistarget/tf_lists/allTFs_hg38.txt
Limitations and next steps
1. Record the exact origin and meaning of the reported score column.
2. Examine regulon target-gene counts and the target genes for the top TFs.
3. Map AUCell activity to cell-type and malignant-cell-state annotations.
4. Check whether immune-associated TFs (for example, MAFB, STAT1 and IRF1) arise from non-malignant populations.

Suggested repository structure
project/
├── README.md
├── environment.yml
├── data/
│   ├── raw/                 
│   └── processed/
├── resources/
│   ├── tf_lists/
│   ├── databases/
│   └── annotations/
├── scripts/
│   ├── download_data.py
│   └── preprocessing.py
└── results/
    ├── grnboost2/
    ├── regulons/
    └── aucell/
Citation
If you use this workflow or interpret the results in a report, cite Aibar et al. (2017) for SCENIC and Neftel et al. (2019) for the glioblastoma dataset and cellular-state framework.
