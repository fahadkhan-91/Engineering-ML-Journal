"""
Day 29 (Week 5, Day 1): Rainfall-Runoff Prediction
--------------------------------------------------
Goal: Predict surface runoff from a catchment based on rainfall depth,
catchment characteristics, and soil conditions - a core task in
drainage design, flood estimation, and stormwater management.

Physical basis: The SCS Curve Number (CN) method, widely used in
hydrology:
    Q = (P - 0.2*S)^2 / (P + 0.8*S)   [when P > 0.2*S]
    S = (25400 / CN) - 254            [S in mm]

Where:
    Q  = runoff depth (mm)
    P  = rainfall depth (mm)
    CN = curve number (30-100; higher = more runoff, less infiltration)
    S  = potential maximum retention (mm)
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)


# -----------------------------
# 1. SCS Curve Number method (the physical model)
# -----------------------------
def scs_runoff(rainfall_mm, curve_number):
    """Calculate runoff depth using SCS-CN method."""
    S = (25400 / curve_number) - 254
    initial_abstraction = 0.2 * S

    if rainfall_mm <= initial_abstraction:
        return 0.0

    Q = ((rainfall_mm - initial_abstraction) ** 2) / (rainfall_mm + 0.8 * S)
    return Q


# -----------------------------
# 2. Generate dataset from real catchment scenarios
# CN values reflect land use + soil group (typical published ranges)
# -----------------------------
n_samples = 300

rainfall = np.random.uniform(10, 200, n_samples)        # mm
curve_number = np.random.uniform(55, 95, n_samples)      # dimensionless
catchment_area = np.random.uniform(0.5, 50, n_samples)   # km2
slope_pct = np.random.uniform(0.5, 15, n_samples)        # %

# Runoff depth from SCS method, with slope adding a small effect
runoff_depth = np.array([
    scs_runoff(p, cn) for p, cn in zip(rainfall, curve_number)
])
runoff_depth = runoff_depth * (1 + 0.005 * slope_pct)  # steeper = slightly more runoff
runoff_depth += np.random.normal(0, 2, n_samples)       # measurement noise
runoff_depth = np.clip(runoff_depth, 0, None)

X = np.column_stack([rainfall, curve_number, catchment_area, slope_pct])
y = runoff_depth

feature_names = ["Rainfall (mm)", "Curve Number", "Catchment Area (km2)", "Slope (%)"]

# -----------------------------
# 3. Train and compare models
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

print("=" * 55)
print("RAINFALL-RUNOFF PREDICTION - MODEL COMPARISON")
print("=" * 55)

for name, pred in [("Linear Regression", lr_pred), ("Random Forest", rf_pred)]:
    print(f"{name}: MAE = {mean_absolute_error(y_test, pred):.2f} mm, "
          f"R2 = {r2_score(y_test, pred):.3f}")

# -----------------------------
# 4. Feature importance
# -----------------------------
print("\nFeature Importance (Random Forest):")
for name, imp in sorted(zip(feature_names, rf_model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {name}: {imp:.3f}")

# -----------------------------
# 5. Practical application: runoff volume for drainage design
# -----------------------------
print("\n" + "=" * 55)
print("DESIGN APPLICATION: Runoff Volume Estimation")
print("=" * 55)

design_scenarios = [
    {"label": "Rural catchment, light soil (CN=60)", "rainfall": 100, "cn": 60, "area": 10, "slope": 3},
    {"label": "Suburban area (CN=75)", "rainfall": 100, "cn": 75, "area": 10, "slope": 3},
    {"label": "Dense urban, paved (CN=92)", "rainfall": 100, "cn": 92, "area": 10, "slope": 3},
]

for sc in design_scenarios:
    pred_depth = rf_model.predict([[sc["rainfall"], sc["cn"], sc["area"], sc["slope"]]])[0]
    volume_m3 = pred_depth / 1000 * sc["area"] * 1e6  # mm -> m, km2 -> m2

    print(f"\n{sc['label']}")
    print(f"  Predicted runoff depth: {pred_depth:.2f} mm")
    print(f"  Total runoff volume: {volume_m3:,.0f} m3")
