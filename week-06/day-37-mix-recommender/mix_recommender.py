"""
Day 37 (Week 6, Day 2): Historical Mix Recommender (from Real Data)
--------------------------------------------------
Goal: Given a target compressive strength, search the real UCI dataset
(1030 lab-tested mixes) for the closest historical mixes that achieved
similar strength - a practical reference-design approach engineers use
before running new lab trials, instead of designing purely from formulas.
"""

import pandas as pd
import numpy as np

# -----------------------------
# 1. Load real dataset (Day 36)
# -----------------------------
df = pd.read_csv("../day-36-real-dataset-validation/data/concrete_data.csv")


def recommend_mixes(target_strength, target_age=28, n_results=5, age_tolerance=7):
    """
    Find the closest historical mixes to a target strength, restricted
    to a similar curing age (since strength is age-dependent).
    """
    # Filter to similar age first (avoid comparing 3-day vs 365-day mixes)
    age_filtered = df[
        (df["age"] >= target_age - age_tolerance) &
        (df["age"] <= target_age + age_tolerance)
    ].copy()

    if age_filtered.empty:
        age_filtered = df.copy()

    age_filtered["strength_diff"] = (
        age_filtered["concrete_compressive_strength"] - target_strength
    ).abs()

    closest = age_filtered.sort_values("strength_diff").head(n_results)
    return closest.drop(columns=["strength_diff"])


# -----------------------------
# 2. Example: engineer wants a 40 MPa mix at 28 days
# -----------------------------
target = 40
age = 28

results = recommend_mixes(target_strength=target, target_age=age, n_results=5)

print("=" * 80)
print(f"TOP 5 HISTORICAL MIXES CLOSEST TO {target} MPa AT ~{age} DAYS")
print("=" * 80)
print(results.to_string(index=False))

# -----------------------------
# 3. Summarize typical proportions for these close matches
# -----------------------------
print("\n" + "=" * 80)
print("AVERAGE PROPORTIONS OF THESE CLOSE-MATCH MIXES")
print("=" * 80)
avg_mix = results.drop(columns=["concrete_compressive_strength", "age"]).mean()
for col, val in avg_mix.items():
    print(f"  {col}: {val:.1f} kg/m3")
print(f"  Average achieved strength: {results['concrete_compressive_strength'].mean():.2f} MPa")

# -----------------------------
# 4. Try a few more target strengths (common design classes)
# -----------------------------
print("\n" + "=" * 80)
print("QUICK REFERENCE: Best historical match per common strength class")
print("=" * 80)
for target_class in [20, 25, 30, 40, 50, 60]:
    best_match = recommend_mixes(target_class, target_age=28, n_results=1)
    row = best_match.iloc[0]
    print(f"Target {target_class} MPa -> closest real mix achieved "
          f"{row['concrete_compressive_strength']:.2f} MPa "
          f"(cement={row['cement']}, water={row['water']}, age={row['age']})")
