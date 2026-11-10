import pandas as pd

auc = pd.read_csv(
    "results/aucell/aucell_scores.csv",
    index_col=0
)

mean_activity = auc.mean(axis=0)

top20 = (
    mean_activity
    .sort_values(ascending=False)
    .head(20)
)

print("\nTop 20 Regulons:\n")
print(top20)

top20.to_csv(
    "results/top20_regulons.csv"
)

print("\nSaved to results/top20_regulons.csv")
