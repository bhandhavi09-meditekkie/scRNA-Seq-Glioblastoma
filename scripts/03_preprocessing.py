import scanpy as sc
import pandas as pd

# Load expression matrix
file_path = r"data/raw/GSE131928_RAW/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv"

print("Loading data...")

df = pd.read_csv(
    file_path,
    sep="\t",
    index_col=0
)

print("Original shape:", df.shape)

# Transpose because Scanpy expects:
# rows = cells
# columns = genes
adata = sc.AnnData(df.T)

print("AnnData shape:", adata.shape)

# Filter cells
sc.pp.filter_cells(
    adata,
    min_genes=200
)

# Filter genes
sc.pp.filter_genes(
    adata,
    min_cells=3
)

print("Shape after filtering:", adata.shape)

# Save processed data
adata.write(
    "data/processed/gbm_filtered.h5ad"
)

print("Saved: data/processed/gbm_filtered.h5ad")
