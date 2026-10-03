"""
Day 38 (Week 6, Day 3): Exploratory Data Analysis on Real Concrete Data
--------------------------------------------------
Goal: Visually explore the real UCI dataset (Day 36) - how each
ingredient relates to compressive strength, and how ingredients
correlate with each other. This is the kind of EDA that should
normally happen BEFORE modeling, which I'm doing now in hindsight
on real data for the first time in this journal.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load real dataset
# -----------------------------
df = pd.read_csv("../day-36-real-dataset-validation/data/concrete_data.csv")

feature_cols = [c for c in df.columns if c != "concrete_compressive_strength"]

# -----------------------------
# 2. Scatter plots: each feature vs strength
# -----------------------------
fig, axes = plt.subplots(2, 4, figsize=(18, 9))
axes = axes.flatten()

for i, col in enumerate(feature_cols):
    axes[i].scatter(df[col], df["concrete_compressive_strength"],
                     alpha=0.4, s=15, color="#4C72B0")
    axes[i].set_xlabel(col)
    axes[i].set_ylabel("Strength (MPa)" if i % 4 == 0 else "")
    axes[i].set_title(col, fontsize=10)

plt.suptitle("Each Ingredient vs Compressive Strength (Real UCI Data, n=1030)",
              fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("feature_vs_strength.png", dpi=150)
plt.show()
print("Saved feature_vs_strength.png")

# -----------------------------
# 3. Correlation heatmap
# -----------------------------
corr = df.corr()

fig2, ax2 = plt.subplots(figsize=(9, 7))
im = ax2.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

ax2.set_xticks(range(len(corr.columns)))
ax2.set_yticks(range(len(corr.columns)))
ax2.set_xticklabels(corr.columns, rotation=45, ha="right", fontsize=9)
ax2.set_yticklabels(corr.columns, fontsize=9)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        ax2.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center",
                  fontsize=7, color="black")

plt.colorbar(im, ax=ax2, label="Correlation")
plt.title("Correlation Matrix (Real UCI Concrete Data)", fontweight='bold')
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=150)
plt.show()
print("Saved correlation_heatmap.png")

# -----------------------------
# 4. Print the strongest correlations with strength
# -----------------------------
strength_corr = corr["concrete_compressive_strength"].drop("concrete_compressive_strength")
strength_corr_sorted = strength_corr.reindex(strength_corr.abs().sort_values(ascending=False).index)

print("\nCorrelation with compressive strength (sorted by strength):")
for name, val in strength_corr_sorted.items():
    direction = "positive" if val > 0 else "negative"
    print(f"  {name}: {val:.3f} ({direction})")
