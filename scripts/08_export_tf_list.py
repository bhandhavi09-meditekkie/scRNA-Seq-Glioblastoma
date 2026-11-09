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

present_tfs = [tf for tf in tfs if tf in expr.columns]

with open("resources/present_TFs.txt", "w") as f:
    for tf in present_tfs:
        f.write(tf + "\n")

print("TFs exported:", len(present_tfs))
