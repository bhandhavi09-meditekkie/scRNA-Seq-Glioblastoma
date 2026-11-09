import pandas as pd

file_path = r"data/raw/GSE131928_RAW/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv"

print("Loading dataset...")

df = pd.read_csv(
    file_path,
    sep="\t",
    index_col=0
)

print("\nDataset loaded successfully!")

print("\nShape:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum().sum())