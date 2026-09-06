"""
Day 19 (Week 3, Day 5): Concrete Strength Prediction v3
(Feature Engineering + Hyperparameter Tuning)
--------------------------------------------------
Goal: Build on Day 5's model - add engineered features (explicit w/c
ratio, log-transformed age based on Day 15's curing insight) and use
GridSearchCV to properly tune a Random Forest model instead of using
default settings.
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)

# -----------------------------
# 1. Generate dataset (same base approach as Day 5, larger sample)
# -----------------------------
n_samples = 300

cement = np.random.uniform(150, 550, n_samples)
water = np.random.uniform(140, 240, n_samples)
coarse_agg = np.random.uniform(800, 1100, n_samples)
age = np.random.choice([3, 7, 14, 28, 56, 90], n_samples)

water_cement_ratio = water / cement
strength = (
    0.09 * cement
    - 40 * water_cement_ratio
    + 0.15 * age
    + np.random.normal(0, 4, n_samples)
)
strength = np.clip(strength, 5, None)

# -----------------------------
# 2. Feature Engineering
# - Add w/c ratio as an EXPLICIT feature (Day 6's Abrams' Law insight)
# - Add log(age) as a feature (Day 15's curing curve insight)
# -----------------------------
log_age = np.log(age)

X_basic = np.column_stack([cement, water, coarse_agg, age])
X_engineered = np.column_stack([cement, water, coarse_agg, age, water_cement_ratio, log_age])

y = strength

# -----------------------------
# 3. Compare basic vs engineered features (same model, same params)
# -----------------------------
X_train_b, X_test_b, y_train, y_test = train_test_split(X_basic, y, test_size=0.2, random_state=42)
X_train_e, X_test_e, _, _ = train_test_split(X_engineered, y, test_size=0.2, random_state=42)

baseline_model = RandomForestRegressor(n_estimators=100, random_state=42)
baseline_model.fit(X_train_b, y_train)
baseline_pred = baseline_model.predict(X_test_b)
baseline_r2 = r2_score(y_test, baseline_pred)

engineered_model = RandomForestRegressor(n_estimators=100, random_state=42)
engineered_model.fit(X_train_e, y_train)
engineered_pred = engineered_model.predict(X_test_e)
engineered_r2 = r2_score(y_test, engineered_pred)

print("=" * 55)
print("STEP 1: Basic Features vs Engineered Features")
print("=" * 55)
print(f"Basic features (cement, water, agg, age):        R2 = {baseline_r2:.3f}")
print(f"Engineered features (+ w/c ratio, + log(age)):    R2 = {engineered_r2:.3f}")

# -----------------------------
# 4. Hyperparameter tuning with GridSearchCV (on engineered features)
# -----------------------------
print("\n" + "=" * 55)
print("STEP 2: Hyperparameter Tuning (GridSearchCV)")
print("=" * 55)

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5],
}

grid_search = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1,
)
grid_search.fit(X_train_e, y_train)

print(f"Best parameters found: {grid_search.best_params_}")
print(f"Best cross-validation R2: {grid_search.best_score_:.3f}")

# -----------------------------
# 5. Final evaluation with tuned model
# -----------------------------
best_model = grid_search.best_estimator_
final_pred = best_model.predict(X_test_e)
final_r2 = r2_score(y_test, final_pred)
final_mae = mean_absolute_error(y_test, final_pred)

print(f"\nFinal tuned model on test set:")
print(f"  R2 Score: {final_r2:.3f}")
print(f"  MAE: {final_mae:.2f} MPa")

print(f"\nImprovement summary:")
print(f"  Day 5 (basic RF, default params):     R2 ~ {baseline_r2:.3f}")
print(f"  Day 19 (engineered + tuned RF):        R2 = {final_r2:.3f}")
