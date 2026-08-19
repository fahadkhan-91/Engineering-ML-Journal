"""
Day 1: Concrete Compressive Strength Prediction
--------------------------------------------------
Goal: Predict concrete compressive strength (MPa) based on mix
ingredients (cement, water, aggregate, age) using Linear Regression.

This uses a small sample dataset to keep things simple for Day 1.
Later, we can swap this with a real dataset (e.g. UCI Concrete dataset).
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------
# 1. Sample dataset
# Columns: cement(kg/m3), water(kg/m3), coarse_agg(kg/m3), age(days)
# Target: compressive_strength (MPa)
# -----------------------------
X = np.array([
    [540, 162, 1040, 28],
    [332, 228, 932, 28],
    [198, 192, 978, 28],
    [266, 228, 932, 28],
    [380, 214, 932, 90],
    [380, 214, 932, 28],
    [475, 228, 932, 28],
    [239, 200, 968, 28],
    [239, 200, 968, 90],
    [190, 200, 1092, 28],
    [304, 214, 932, 28],
    [500, 180, 900, 28],
])

y = np.array([
    79.99, 40.27, 41.05, 46.11, 52.91,
    41.68, 44.30, 33.90, 47.03, 22.53,
    39.29, 61.89
])

# -----------------------------
# 2. Split into train/test
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -----------------------------
# 3. Train the model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# 4. Evaluate
# -----------------------------
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Predicted strengths:", np.round(y_pred, 2))
print("Actual strengths:   ", y_test)
print(f"Mean Absolute Error: {mae:.2f} MPa")
print(f"R2 Score: {r2:.2f}")

# -----------------------------
# 5. Try a custom prediction
# Example: cement=350, water=190, coarse_agg=950, age=28
# -----------------------------
sample_mix = np.array([[350, 190, 950, 28]])
predicted_strength = model.predict(sample_mix)
print(f"\nPredicted strength for custom mix: {predicted_strength[0]:.2f} MPa")
