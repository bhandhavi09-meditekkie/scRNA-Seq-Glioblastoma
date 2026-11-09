pySCENIC Commands Used

GRNBoost2

pyscenic grn data/processed/gbm\_hvg\_5000.tsv resources/present\_TFs.txt -o results/grnboost2/grnboost2\_network.csv --num\_workers 8

RcisTarget

pyscenic ctx \\

results/grnboost2/grnboost2\_network.csv \\

resources/databases/hg38\_\_refseq-r80\_\_10kb\_up\_and\_down\_tss.mc9nr.genes\_vs\_motifs.rankings.feather \\

\--annotations\_fname resources/annotations/motifs-v10nr\_clust-nr.hgnc-m0.001-o0.0.tbl.txt \\

\--expression\_mtx\_fname data/processed/gbm\_hvg\_5000.tsv \\

\--output results/regulons/regulons.csv \\

\--num\_workers 2

AUCell

pyscenic aucell \\

data/processed/gbm\_hvg\_5000.tsv \\

results/regulons/regulons.csv \\

\--output results/aucell/aucell\_scores.csv \\

\--num\_workers 2

