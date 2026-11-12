auc = pd.read_csv(
    "results/aucell/aucell_scores.csv",
    index_col=0
)
mean_activity = auc.mean(axis=0) #Calculating overall activity of the regulon from the entire dataset
top20 = (
    mean_activity
    .sort_values(ascending=False)
    .head(20)
)
print(top20)
top20.to_csv(
    "results/top20_regulons.csv"
)

