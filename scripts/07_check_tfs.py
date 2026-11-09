import pandas as pd

expr = pd.read_csv(
    "data/processed/gbm_hvg_5000.tsv",
    sep="\t",
    index_col=0
)

tfs = pd.read_csv(
    "resources/allTFs_hg38.txt",
    header=None
)[0].tolist()

gene_set = set(expr.columns)

present_tfs = [tf for tf in tfs if tf in gene_set]

print("Total TFs in list:", len(tfs))
print("TFs present in dataset:", len(present_tfs))

print("\nFirst 20 TFs:")
print(present_tfs[:20])