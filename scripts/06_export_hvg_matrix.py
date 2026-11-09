import scanpy as sc

adata = sc.read_h5ad(
    "data/processed/gbm_hvg_5000.h5ad"
)

expr = adata.to_df()

print("Shape:", expr.shape)

expr.to_csv(
    "data/processed/gbm_hvg_5000.tsv",
    sep="\t"
)

print("Saved HVG matrix.")
