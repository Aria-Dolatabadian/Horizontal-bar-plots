import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv (r'ChrRLKRLP.csv')
print (df)
sns.set_theme(style="whitegrid")
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("pastel")
sns.barplot(x="RLK", y="Chromosomes", data=df,
            label="RLK", color="b")
sns.set_color_codes("muted")
sns.barplot(x="RLP", y="Chromosomes", data=df,
            label="RLP", color="b")
ax.legend(ncol=2, loc="center right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="RLK and RLP distributions across the chromosomes")
sns.despine(left=True, bottom=True)
plt.show()
