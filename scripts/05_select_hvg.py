import scanpy as sc

adata = sc.read_h5ad(
    "data/processed/gbm_filtered.h5ad"
)

sc.pp.highly_variable_genes(
    adata,
    n_top_genes=5000
)

adata_hvg = adata[:, adata.var.highly_variable]

print(adata_hvg.shape)

adata_hvg.write(
    "data/processed/gbm_hvg_5000.h5ad"
)