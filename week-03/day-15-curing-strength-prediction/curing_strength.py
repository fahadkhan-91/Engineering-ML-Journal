"""
Day 15 (Week 3, Day 1): Concrete Curing Strength Gain Prediction
--------------------------------------------------
Goal: Model how concrete compressive strength develops over curing
time (days), using the well-known logarithmic strength gain pattern,
and fit an ML regression model to predict strength at any given age.

Real-world context: Concrete gains most of its strength in the first
28 days, then continues gaining (slower) for months/years.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

np.random.seed(42)

# -----------------------------
# 1. Generate synthetic curing data
# Based on a common empirical model:
#   strength(t) = strength_28 * (t / (a + b*t))
# (ACI-style hyperbolic strength-gain relationship)
# -----------------------------
strength_28 = 30  # MPa, target 28-day strength
a, b = 4.0, 0.85  # empirical constants (typical for normal Portland cement)

days = np.array([1, 3, 7, 14, 21, 28, 56, 90, 180, 365])
true_strength = strength_28 * (days / (a + b * days))

# Add small measurement noise (realistic lab variability)
noisy_strength = true_strength + np.random.normal(0, 1.0, len(days))

print("Day  |  True Strength (MPa)  |  Noisy Strength (MPa)")
print("-" * 50)
for d, ts, ns in zip(days, true_strength, noisy_strength):
    print(f"{d:<5}|  {ts:<20.2f}|  {ns:.2f}")

# -----------------------------
# 2. Fit ML model using log(time) as a feature
# (Linear regression works well after log transform)
# -----------------------------
X = np.log(days).reshape(-1, 1)
y = noisy_strength

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

print(f"\nModel R2 Score: {r2:.3f}")
print(f"Model equation: strength = {model.coef_[0]:.2f} * ln(day) + {model.intercept_:.2f}")

# -----------------------------
# 3. Predict strength at custom curing ages
# -----------------------------
custom_days = [2, 10, 45, 120]
print("\nPredictions for custom curing ages:")
for d in custom_days:
    pred = model.predict([[np.log(d)]])[0]
    print(f"  Day {d}: predicted strength = {pred:.2f} MPa")

# -----------------------------
# 4. Estimate % of 28-day strength gained at key milestones
# -----------------------------
print("\n% of 28-day strength gained (using true model):")
for d in [3, 7, 14, 28]:
    pct = (strength_28 * (d / (a + b * d))) / strength_28 * 100
    print(f"  Day {d}: {pct:.1f}%")
