#https://scanpy.readthedocs.io/en/latest/tutorials/basics/clustering-2017.html the values taken from this tutorial for filtering
# importing expression matrix
file_path = r"data/raw/GSE131928_RAW/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv"
df = pd.read_csv(
    file_path,
    sep="\t",
    index_col=0 
)
print(df.shape)
# Transpose because Scanpy expects:
# rows = cells
# columns = genes
adata = sc.AnnData(df.T)
print(adata.shape)

# filtering cells that have genes expressing less than 200
sc.pp.filter_cells(
    adata,
    min_genes=200
)

# filtering genes that have are in less than 3 cells 
sc.pp.filter_genes(
    adata,
    min_cells=3
)

print(adata.shape)
# Saved the processed data
adata.write(
    "data/processed/gbm_filtered.h5ad"
)


