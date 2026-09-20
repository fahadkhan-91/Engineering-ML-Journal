"""
Day 33 (Week 5, Day 5): Rainfall-Runoff Prediction v2
(Cross-Validation + Tuning + Return Period Analysis)
--------------------------------------------------
Goal: Extend Day 29's rainfall-runoff model with the rigorous ML
workflow from Days 13/19/26 (cross-validation + hyperparameter tuning),
then apply it to a practical flood engineering question: how does
predicted runoff scale across different design storm return periods?
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score


np.random.seed(42)


def scs_runoff(rainfall_mm, curve_number):
    S = (25400 / curve_number) - 254
    ia = 0.2 * S
    if rainfall_mm <= ia:
        return 0.0
    return ((rainfall_mm - ia) ** 2) / (rainfall_mm + 0.8 * S)


# -----------------------------
# 1. Generate dataset (same approach as Day 29)
# -----------------------------
n_samples = 300
rainfall = np.random.uniform(10, 200, n_samples)
curve_number = np.random.uniform(55, 95, n_samples)
catchment_area = np.random.uniform(0.5, 50, n_samples)
slope_pct = np.random.uniform(0.5, 15, n_samples)

runoff_depth = np.array([scs_runoff(p, cn) for p, cn in zip(rainfall, curve_number)])
runoff_depth = runoff_depth * (1 + 0.005 * slope_pct)
runoff_depth += np.random.normal(0, 2, n_samples)
runoff_depth = np.clip(runoff_depth, 0, None)

X = np.column_stack([rainfall, curve_number, catchment_area, slope_pct])
y = runoff_depth

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 2. Cross-validation baseline
# -----------------------------
baseline = RandomForestRegressor(n_estimators=100, random_state=42)
cv_scores = cross_val_score(baseline, X, y, cv=5, scoring="r2")

print("=" * 55)
print("STEP 1: Baseline Cross-Validation (5-fold)")
print("=" * 55)
print(f"Mean R2: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# -----------------------------
# 3. Hyperparameter tuning
# -----------------------------
print("\n" + "=" * 55)
print("STEP 2: Hyperparameter Tuning (GridSearchCV)")
print("=" * 55)

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 8, 15],
}

grid_search = GridSearchCV(
    RandomForestRegressor(random_state=42), param_grid, cv=5, scoring="r2", n_jobs=-1
)
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best CV R2: {grid_search.best_score_:.3f}")

test_pred = best_model.predict(X_test)
print(f"Test R2: {r2_score(y_test, test_pred):.3f}")
print(f"Test MAE: {mean_absolute_error(y_test, test_pred):.2f} mm")

# -----------------------------
# 4. Engineering application: Return period design storms
# Typical IDF-derived rainfall depths for a hypothetical region (mm)
# -----------------------------
return_periods = {
    "2-year storm": 55,
    "5-year storm": 75,
    "10-year storm": 90,
    "25-year storm": 110,
    "50-year storm": 130,
    "100-year storm": 150,
}

fixed_cn = 78     # suburban catchment
fixed_area = 15   # km2
fixed_slope = 4   # %

print("\n" + "=" * 55)
print("STEP 3: Design Runoff Across Return Periods (CN=78, 15 km2)")
print("=" * 55)

for label, rainfall_mm in return_periods.items():
    pred_depth = best_model.predict([[rainfall_mm, fixed_cn, fixed_area, fixed_slope]])[0]
    volume_m3 = pred_depth / 1000 * fixed_area * 1e6
    print(f"{label:<16} (P={rainfall_mm}mm) -> Runoff: {pred_depth:.1f} mm, "
          f"Volume: {volume_m3:,.0f} m3")
