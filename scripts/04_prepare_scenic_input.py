adata = sc.read_h5ad(
    "data/processed/gbm_filtered.h5ad"
)
print(adata.shape)

# Convert AnnData back to dataframe
expr = adata.to_df()

#expression matrix shape
print(expr.shape)

output_file = "data/processed/gbm_expression_matrix.tsv"

expr.to_csv(
    output_file,
    sep="\t"
) #converting to tsv format so that it can be a input to the GRNBoost

print(f"Saved: {output_file}")
