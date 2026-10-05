"""
Day 39 (Week 6, Day 4): Automated Mix Design Report Generator
--------------------------------------------------
Goal: Automate generating a design report for multiple target strength
classes in one run - combining Day 36's trained real-data model with
Day 37's historical mix recommender - instead of looking up each
strength class manually. Outputs a clean CSV report, as would be
handed to a design team.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# -----------------------------
# 1. Load real dataset (Day 36)
# -----------------------------
df = pd.read_csv("../day-36-real-dataset-validation/data/concrete_data.csv")

feature_cols = [c for c in df.columns if c != "concrete_compressive_strength"]
X = df[feature_cols].values
y = df["concrete_compressive_strength"].values

# -----------------------------
# 2. Train a model once (reused for every target in the batch)
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)


def recommend_mix(target_strength, target_age=28, age_tolerance=7):
    """Find the closest historical mix (Day 37's approach)."""
    age_filtered = df[
        (df["age"] >= target_age - age_tolerance) &
        (df["age"] <= target_age + age_tolerance)
    ].copy()
    if age_filtered.empty:
        age_filtered = df.copy()

    age_filtered["diff"] = (age_filtered["concrete_compressive_strength"] - target_strength).abs()
    best = age_filtered.sort_values("diff").iloc[0]
    return best.drop("diff")


def generate_report(target_classes, target_age=28):
    """Build a design report for a batch of target strength classes."""
    rows = []
    for target in target_classes:
        historical = recommend_mix(target, target_age)

        # Predict what the model thinks this historical mix would achieve
        mix_features = historical[feature_cols].values.reshape(1, -1)
        model_prediction = model.predict(mix_features)[0]

        rows.append({
            "target_strength_MPa": target,
            "recommended_cement_kgm3": historical["cement"],
            "recommended_water_kgm3": historical["water"],
            "recommended_slag_kgm3": historical["blast_furnace_slag"],
            "recommended_flyash_kgm3": historical["fly_ash"],
            "recommended_superplasticizer_kgm3": historical["superplasticizer"],
            "recommended_coarse_agg_kgm3": historical["coarse_aggregate"],
            "recommended_fine_agg_kgm3": historical["fine_aggregate"],
            "historical_actual_strength_MPa": historical["concrete_compressive_strength"],
            "model_predicted_strength_MPa": round(model_prediction, 2),
            "age_days": int(historical["age"]),
        })

    return pd.DataFrame(rows)


# -----------------------------
# 3. Generate a batch report across common design strength classes
# -----------------------------
target_classes = [20, 25, 30, 35, 40, 45, 50, 60]
report = generate_report(target_classes, target_age=28)

print("=" * 100)
print("AUTOMATED MIX DESIGN REPORT (Batch of 8 Target Strength Classes)")
print("=" * 100)
print(report.to_string(index=False))

# -----------------------------
# 4. Save as CSV (a real deliverable a design team could use)
# -----------------------------
report.to_csv("mix_design_report.csv", index=False)
print("\nSaved mix_design_report.csv")

# -----------------------------
# 5. Flag any target where model prediction and historical actual
# strength disagree significantly - a quality/consistency check
# -----------------------------
report["prediction_gap"] = (
    report["model_predicted_strength_MPa"] - report["historical_actual_strength_MPa"]
).abs()

flagged = report[report["prediction_gap"] > 3]
print(f"\nMixes flagged for review (model vs actual gap > 3 MPa): {len(flagged)}")
if not flagged.empty:
    print(flagged[["target_strength_MPa", "historical_actual_strength_MPa",
                    "model_predicted_strength_MPa", "prediction_gap"]].to_string(index=False))
else:
    print("All recommended mixes are consistent between model and historical record.")
