pySCENIC Execution: https://pyscenic.readthedocs.io/en/latest/

pySCENIC workflow was executed using command-line interfaces.Due to software compatibility and dependency issues encountered during installation on Windows,the analysis was performed in a mixed Windows and Linux environment.At staring preprocessing and data preparation were carried out in a Python environment on Windows,while the computationally intensive pySCENIC steps were executed through command-line interfaces in WSL to due to compatibility with required packages.
---------------------------------------------------------------------------------------
Step 1: GRN Inference using GRNBoost2

pyscenic grn \
data/processed/gbm_hvg_5000.tsv \
resources/present_TFs.txt \
-o results/grnboost2/grnboost2_network.csv \
--num_workers 8

Input:
gbm_hvg_5000.tsv : filtered expression matrix containing highly variable genes
present_TFs.txt : list of transcription factors used as candidate regulators
Output:
grnboost2_network.csv : inferred TF-target network with importance scores
------------------------------------------------------------------------------------------------
Step 2: Regulon Construction using RcisTarget

pyscenic ctx \
results/grnboost2/grnboost2_network.csv \
resources/databases/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather \
--annotations_fname resources/annotations/motifs-v10nr_clust-nr.hgnc-m0.001-o0.0.tbl.txt \
--expression_mtx_fname data/processed/gbm_hvg_5000.tsv \
--output results/regulons/regulons.csv \
--num_workers 2

Input:
GRNBoost2 network
Human motif-ranking database
Motif annotation file
Expression matrix
Output:
regulons.csv containing transcription factors and their predicted direct target genes.
-----------------------------------------------------------------------------------------------------
Step 3: Regulon Activity Scoring using AUCell

pyscenic aucell \
data/processed/gbm_hvg_5000.tsv \
results/regulons/regulons.csv \
--output results/aucell/aucell_scores.csv \
--num_workers 2

Input:
Expression matrix
Regulon definitions
Output:
aucell_scores.csv containing regulon activity scores for each cell
