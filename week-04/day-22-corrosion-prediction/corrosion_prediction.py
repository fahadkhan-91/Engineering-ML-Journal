"""
Day 22 (Week 4, Day 1): Reinforcement Steel Corrosion Rate Prediction
--------------------------------------------------
Goal: Predict corrosion rate of reinforcement steel in concrete based
on environmental factors (chloride content, humidity, temperature,
concrete cover depth) using ML regression - a key durability concern
in reinforced concrete structures.
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)

# -----------------------------
# 1. Generate synthetic corrosion dataset
# Features: chloride content (kg/m3), relative humidity (%),
#           temperature (C), concrete cover depth (mm)
# Target: corrosion rate (micrometers/year) - simplified model
# -----------------------------
n_samples = 250

chloride = np.random.uniform(0, 5, n_samples)          # kg/m3
humidity = np.random.uniform(40, 95, n_samples)         # %
temperature = np.random.uniform(10, 40, n_samples)      # Celsius
cover_depth = np.random.uniform(20, 75, n_samples)       # mm

# Simplified physical relationship:
# - Higher chloride -> more corrosion
# - Higher humidity (up to a point) -> more corrosion (needs moisture + oxygen)
# - Higher temperature -> faster reaction rate -> more corrosion
# - Greater cover depth -> chloride takes longer to reach steel -> less corrosion
corrosion_rate = (
    8 * chloride
    + 0.15 * humidity
    + 0.3 * temperature
    - 0.4 * cover_depth
    + np.random.normal(0, 3, n_samples)
)
corrosion_rate = np.clip(corrosion_rate, 0, None)

X = np.column_stack([chloride, humidity, temperature, cover_depth])
y = corrosion_rate

feature_names = ["Chloride Content", "Humidity", "Temperature", "Cover Depth"]

# -----------------------------
# 2. Train/test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 3. Train two models for comparison
# -----------------------------
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

print("=" * 50)
print("CORROSION RATE PREDICTION - MODEL RESULTS")
print("=" * 50)

for name, pred in [("Linear Regression", lr_pred), ("Random Forest", rf_pred)]:
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    print(f"{name}: MAE = {mae:.2f} um/year, R2 = {r2:.3f}")

# -----------------------------
# 4. Feature importance (Random Forest)
# -----------------------------
print("\nFeature Importance (Random Forest):")
for name, imp in sorted(zip(feature_names, rf_model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {name}: {imp:.3f}")

# -----------------------------
# 5. Practical scenario: compare cover depth impact
# -----------------------------
print("\n--- Effect of Cover Depth on Corrosion Rate ---")
print("(Chloride=3 kg/m3, Humidity=75%, Temp=25C)")
for depth in [20, 30, 40, 50, 65]:
    sample = np.array([[3, 75, 25, depth]])
    pred = rf_model.predict(sample)[0]
    print(f"  Cover depth {depth}mm -> Predicted corrosion rate: {pred:.2f} um/year")
