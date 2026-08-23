"""
Day 5: Concrete Strength Prediction v2 (Model Comparison)
--------------------------------------------------
Goal: Build on Day 1's concrete strength model - use a larger synthetic
dataset and compare two ML models (Linear Regression vs Random Forest)
to see which handles the material behavior better.

This is a natural progression: Day 1 = basic model, Day 5 = comparing
approaches and picking the better one (a real ML workflow habit).
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)

# -----------------------------
# 1. Generate a larger synthetic dataset
# Based on realistic ranges for concrete mix ingredients
# -----------------------------
n_samples = 200

cement = np.random.uniform(150, 550, n_samples)       # kg/m3
water = np.random.uniform(140, 240, n_samples)         # kg/m3
coarse_agg = np.random.uniform(800, 1100, n_samples)   # kg/m3
age = np.random.choice([3, 7, 14, 28, 56, 90], n_samples)

# Simplified strength model with some noise (mimics real behavior:
# more cement + less water/cement ratio + more curing age = more strength)
water_cement_ratio = water / cement
strength = (
    0.09 * cement
    - 40 * water_cement_ratio
    + 0.15 * age
    + np.random.normal(0, 4, n_samples)  # noise
)
strength = np.clip(strength, 5, None)  # strength can't be negative

X = np.column_stack([cement, water, coarse_agg, age])
y = strength

# -----------------------------
# 2. Split data
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 3. Train both models
# -----------------------------
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# -----------------------------
# 4. Evaluate both
# -----------------------------
lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

rf_mae = mean_absolute_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

print("=" * 50)
print("MODEL COMPARISON: Concrete Strength Prediction")
print("=" * 50)
print(f"\nLinear Regression:")
print(f"  MAE: {lr_mae:.2f} MPa")
print(f"  R2 Score: {lr_r2:.3f}")

print(f"\nRandom Forest:")
print(f"  MAE: {rf_mae:.2f} MPa")
print(f"  R2 Score: {rf_r2:.3f}")

better_model = "Random Forest" if rf_r2 > lr_r2 else "Linear Regression"
print(f"\nBetter performing model: {better_model}")

# -----------------------------
# 5. Feature importance (Random Forest only)
# -----------------------------
feature_names = ["Cement", "Water", "Coarse Aggregate", "Age"]
importances = rf_model.feature_importances_

print("\nFeature Importance (Random Forest):")
for name, imp in sorted(zip(feature_names, importances), key=lambda x: -x[1]):
    print(f"  {name}: {imp:.3f}")

# -----------------------------
# 6. Predict for a custom mix
# -----------------------------
custom_mix = np.array([[400, 180, 950, 28]])
lr_custom = lr_model.predict(custom_mix)[0]
rf_custom = rf_model.predict(custom_mix)[0]

print(f"\nCustom mix prediction (cement=400, water=180, agg=950, age=28):")
print(f"  Linear Regression: {lr_custom:.2f} MPa")
print(f"  Random Forest:     {rf_custom:.2f} MPa")
