SCENIC Analysis of Glioblastoma Single-Cell RNA-seq Data:
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-Project overview:
This project applies SCENIC (Single-Cell Regulatory Network Inference and Clustering) to a glioblastoma (GBM) single-cell RNA-sequencing expression matrix. 
The project uses GSE131928, a public GEO study of adult and paediatric IDH-wildtype glioblastomas.The analysis described here uses the 7,930-cell Smart-seq2 subset, rather than the full 24,131-cell collection (which also includes 16,201 10X cells).
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dataset:
- Repository: NCBI Gene Expression Omnibus (GEO)
- Accession: GSE131928
- Study: Single-cell RNA-seq analysis of adult and paediatric IDH-wildtype glioblastomas
- Original study: Neftel et al., An Integrative Model of Cellular States, Plasticity, and Genetics for Glioblastoma (Cell, 2019)
- Subset used: Smart-seq2
- Cells in subset: 7,930
- Project-specific matrix: gbm_expression_matrix.tsv, reported as 7,930 × 22,197 (cells × genes)
The original GEO Smart-seq2 processed file is available as a supplementary file from sample GSM3828672. The download script in scripts/download_data.py retrieves this public GEO file.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Method:
SCENIC has three main stages:
1. GRNBoost2 — infers candidate TF–target relationships from expression patterns and a supplied human TF list.
2. cisTarget — evaluates motif enrichment in candidate target-gene modules and prunes candidate relationships using a genome-specific ranking database and motif-to-TF annotations.
3. AUCell — calculates enrichment/activity of each regulon in each cell based on the ranking of expressed genes.
Reference resources
- Human TF list: https://resources.aertslab.org/cistarget/tf_lists/allTFs_hg38.txt
- cisTarget databases: https://resources.aertslab.org/cistarget/
- pySCENIC documentation: https://pyscenic.readthedocs.io/
The analysis used the human hg38 RefSeq r80 ranking database:
hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather
and motif annotation file:
motifs-v10nr_clust-nr.hgnc-m0.001-o0.0.tbl.txt
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Results reported from thie analysis
The project reported the following 20 TF-labelled entries and associated scores:
TF	Reported score
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
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Interpretation
SOX4 and HES6 have the highest reported scores in this list, followed by NFIL3, MAFB, JUN and STAT1. These are candidate regulators prioritised for follow-up in this dataset, not experimentally proven glioblastoma drivers.

The TFs suggest several hypotheses for biological investigation:
- Developmental/neural and stem-like programmes: SOX4, HES6, NEUROD1, DLX2 and KLF4.
- Stress-response and cell-behaviour programmes: JUN and ATF3.
- Immune/inflammatory or microenvironment-associated programmes: STAT1, IRF1, NFIL3 and MAFB.
- Hypoxia/developmental signalling: EPAS1 and GLI1.
These groupings are literature-informed hypotheses. In a mixed tumour single-cell dataset, a TF may arise from malignant cells, macrophages, lymphocytes, endothelial cells or other populations. Cell-type annotations and per-cell regulon activity are required before assigning a TF to a malignant-cell state.

A high score is not automatically equivalent to high TF expression, causal activity, prognostic value or tumour specificity. Interpret the score according to its exact definition.
Limitations
1. SCENIC infers candidate regulatory relationships computationally; motif enrichment does not prove TF binding in the analysed cells.
2. Co-expression and motif support do not establish causality.
3. The reported TF score metric needs to be explicitly identified from the output-generation step.
4. The 7,930-cell Smart-seq2 subset is only one part of GSE131928; results may differ in the 10X subset.
5. Cell-type attribution requires metadata/annotation and per-cell activity analysis.
6. A direct comparison against expression-based clustering has not been performed, so this project does not claim improved classification accuracy.
7. Experimental validation (for example, perturbation, ChIP-seq/CUT&RUN, or independent cohort validation) would be needed to establish causal regulatory roles.
Conclusion
This project applies SCENIC to a glioblastoma single-cell dataset different from the datasets used in the original SCENIC publication. The workflow uses GRNBoost2 for candidate network inference, cisTarget for motif-based regulon pruning and AUCell for cell-wise regulon activity scoring. The reported candidate list prioritises SOX4, HES6 and other transcription factors for further biological investigation.

The main contribution is the application and interpretation of a regulatory-network method in a disease-specific dataset. The results provide hypotheses about glioblastoma-associated regulatory programmes; they do not constitute experimental proof of TF function or a benchmark showing superior cell classification.
References
1. Aibar, S. et al. (2017). SCENIC: single-cell regulatory network inference and clustering. Nature Methods, 14, 1083–1086. https://doi.org/10.1038/nmeth.4463
2. Neftel, C. et al. (2019). An Integrative Model of Cellular States, Plasticity, and Genetics for Glioblastoma. Cell, 178(4), 835–849.e21. https://doi.org/10.1016/j.cell.2019.06.024
3. GEO accession GSE131928. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE131928
4. pySCENIC documentation. https://pyscenic.readthedocs.io/
5. cisTarget resources. https://resources.aertslab.org/cistarget/
