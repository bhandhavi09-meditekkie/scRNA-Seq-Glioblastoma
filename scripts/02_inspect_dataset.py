
file_path = r"data/raw/GSE131928_RAW/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv/GSM3828672_Smartseq2_GBM_IDHwt_processed_TPM.tsv" #importing the file

df = pd.read_csv(
    file_path,
    sep="\t",
    index_col=0 #Uses the first column as the row names
) #converting the tsv file to csv file

#Analyzing the file data
print(df.shape) #to check the no of columns and rows
print(df.head()) #to see the first 5 lines
print(df.isnull().sum().sum()) #Checking missing values
