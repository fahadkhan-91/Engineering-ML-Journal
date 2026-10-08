"""
Day 40 (Week 6, Day 5): Final Concrete Strength Model (Real Data)
Feature Engineering + Cross-Validation + Hyperparameter Tuning
--------------------------------------------------
Goal: Bring together everything learned across this journal - feature
engineering (Day 19), cross-validation (Day 13), hyperparameter tuning
(Day 19/26/33) - and apply the full rigorous workflow to the REAL UCI
dataset (Day 36) for the first time, producing the most trustworthy
model in this repository.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------
# 1. Load real dataset (Day 36)
# -----------------------------
df = pd.read_csv("../day-36-real-dataset-validation/data/concrete_data.csv")

# -----------------------------
# 2. Feature engineering (Day 19's approach, applied to real data)
# - water/cement ratio (Day 6's Abrams' Law)
# - log(age) (Day 15's curing curve insight)
# - total binder content (cement + slag + fly ash) - a known real
#   concrete engineering metric not used anywhere earlier in this repo
# -----------------------------
df["water_cement_ratio"] = df["water"] / df["cement"]
df["log_age"] = np.log(df["age"])
df["total_binder"] = df["cement"] + df["blast_furnace_slag"] + df["fly_ash"]

base_features = ["cement", "blast_furnace_slag", "fly_ash", "water",
                  "superplasticizer", "coarse_aggregate", "fine_aggregate", "age"]
engineered_features = base_features + ["water_cement_ratio", "log_age", "total_binder"]

X_base = df[base_features].values
X_eng = df[engineered_features].values
y = df["concrete_compressive_strength"].values

# -----------------------------
# 3. Compare base vs engineered features (same model, same split)
# -----------------------------
X_train_b, X_test_b, y_train, y_test = train_test_split(X_base, y, test_size=0.2, random_state=42)
X_train_e, X_test_e, _, _ = train_test_split(X_eng, y, test_size=0.2, random_state=42)

baseline = RandomForestRegressor(n_estimators=200, random_state=42)
baseline.fit(X_train_b, y_train)
baseline_pred = baseline.predict(X_test_b)

engineered = RandomForestRegressor(n_estimators=200, random_state=42)
engineered.fit(X_train_e, y_train)
engineered_pred = engineered.predict(X_test_e)

print("=" * 60)
print("STEP 1: Base features vs Engineered features (Real Data)")
print("=" * 60)
print(f"Base (8 raw features):            R2 = {r2_score(y_test, baseline_pred):.3f}, "
      f"MAE = {mean_absolute_error(y_test, baseline_pred):.2f} MPa")
print(f"Engineered (+wc_ratio, log_age, total_binder): R2 = {r2_score(y_test, engineered_pred):.3f}, "
      f"MAE = {mean_absolute_error(y_test, engineered_pred):.2f} MPa")

# -----------------------------
# 4. Cross-validation (shuffled - Day 36 taught us this matters)
# -----------------------------
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(RandomForestRegressor(n_estimators=200, random_state=42),
                             X_eng, y, cv=kfold, scoring="r2")

print("\n" + "=" * 60)
print("STEP 2: 5-Fold Cross-Validation (shuffled, engineered features)")
print("=" * 60)
print(f"Mean R2: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# -----------------------------
# 5. Hyperparameter tuning (GridSearchCV)
# -----------------------------
print("\n" + "=" * 60)
print("STEP 3: Hyperparameter Tuning (GridSearchCV)")
print("=" * 60)

param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 15, 25],
    "min_samples_split": [2, 5],
}

grid_search = GridSearchCV(
    RandomForestRegressor(random_state=42), param_grid, cv=kfold, scoring="r2", n_jobs=-1
)
grid_search.fit(X_train_e, y_train)

best_model = grid_search.best_estimator_
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV R2: {grid_search.best_score_:.3f}")

final_pred = best_model.predict(X_test_e)
final_r2 = r2_score(y_test, final_pred)
final_mae = mean_absolute_error(y_test, final_pred)

print(f"\nFinal tuned model on held-out test set:")
print(f"  R2 Score: {final_r2:.3f}")
print(f"  MAE: {final_mae:.2f} MPa")

# -----------------------------
# 6. Feature importance of the final model
# -----------------------------
print("\nFeature Importance (final tuned model):")
for name, imp in sorted(zip(engineered_features, best_model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {name}: {imp:.3f}")

# -----------------------------
# 7. Full journey summary
# -----------------------------
print("\n" + "=" * 60)
print("FULL JOURNEY: Day 1 (synthetic) -> Day 40 (real, tuned)")
print("=" * 60)
print("Day 1  (synthetic data, Linear Regression):        R2 ~ 0.88 (not real)")
print("Day 36 (real data, same 4 features, Linear Reg):   R2 = 0.522 (reality check)")
print("Day 36 (real data, Random Forest, 4 features):     R2 = 0.829")
print(f"Day 40 (real data, engineered + tuned, 8+3 feat):  R2 = {final_r2:.3f}")
