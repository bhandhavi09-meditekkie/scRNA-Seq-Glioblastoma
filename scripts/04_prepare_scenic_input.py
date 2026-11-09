import scanpy as sc
import pandas as pd

print("Loading filtered data...")

adata = sc.read_h5ad(
    "data/processed/gbm_filtered.h5ad"
)

print("Shape:", adata.shape)

# Convert AnnData back to dataframe
expr = adata.to_df()

print("Expression matrix shape:")
print(expr.shape)

output_file = "data/processed/gbm_expression_matrix.tsv"

expr.to_csv(
    output_file,
    sep="\t"
)

print(f"Saved: {output_file}")