"""
Day 26 (Week 4, Day 5): Corrosion Prediction v2
(Cross-Validation + Tuning + Service Life Estimation)
--------------------------------------------------
Goal: Extend Day 22's corrosion model with 5-fold cross-validation and
GridSearchCV tuning (Day 13/19's workflow), then use the tuned model
to estimate structure service life before corrosion-related repair
is needed - turning a raw prediction into an engineering decision.
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score

np.random.seed(42)

# -----------------------------
# 1. Generate dataset (same approach as Day 22, larger sample)
# -----------------------------
n_samples = 300

chloride = np.random.uniform(0, 5, n_samples)
humidity = np.random.uniform(40, 95, n_samples)
temperature = np.random.uniform(10, 40, n_samples)
cover_depth = np.random.uniform(20, 75, n_samples)

corrosion_rate = (
    8 * chloride
    + 0.15 * humidity
    + 0.3 * temperature
    - 0.4 * cover_depth
    + np.random.normal(0, 3, n_samples)
)
corrosion_rate = np.clip(corrosion_rate, 0.5, None)  # avoid zero for life calc

X = np.column_stack([chloride, humidity, temperature, cover_depth])
y = corrosion_rate

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# 2. Cross-validation baseline (Day 13's workflow)
# -----------------------------
baseline_model = RandomForestRegressor(n_estimators=100, random_state=42)
cv_scores = cross_val_score(baseline_model, X, y, cv=5, scoring="r2")

print("=" * 55)
print("STEP 1: Baseline Cross-Validation (5-fold)")
print("=" * 55)
print(f"Mean R2: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# -----------------------------
# 3. Hyperparameter tuning (Day 19's workflow)
# -----------------------------
print("\n" + "=" * 55)
print("STEP 2: Hyperparameter Tuning (GridSearchCV)")
print("=" * 55)

param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
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
print(f"Test MAE: {mean_absolute_error(y_test, test_pred):.2f} um/year")

# -----------------------------
# 4. Engineering application: Service life estimation
# Assumption: corrosion becomes a structural concern after steel
# section loses ~10% of its diameter (simplified rule of thumb)
# -----------------------------
def estimate_service_life(corrosion_rate_um_per_year, bar_dia_mm=16, allowable_loss_pct=10):
    """
    Estimate years until steel bar diameter loss reaches the
    allowable threshold, based on predicted corrosion rate.
    """
    allowable_loss_mm = bar_dia_mm * (allowable_loss_pct / 100)
    allowable_loss_um = allowable_loss_mm * 1000
    years = allowable_loss_um / corrosion_rate_um_per_year
    return years


print("\n" + "=" * 55)
print("STEP 3: Estimated Service Life (16mm bars, 10% loss limit)")
print("=" * 55)

scenarios = [
    {"label": "Low risk (chloride=1, humidity=60%, temp=20C, cover=50mm)",
     "input": [1, 60, 20, 50]},
    {"label": "Moderate risk (chloride=3, humidity=75%, temp=28C, cover=40mm)",
     "input": [3, 75, 28, 40]},
    {"label": "High risk (chloride=4.5, humidity=90%, temp=35C, cover=25mm)",
     "input": [4.5, 90, 35, 25]},
]

for sc in scenarios:
    pred_rate = best_model.predict([sc["input"]])[0]
    life_years = estimate_service_life(pred_rate)
    print(f"\n{sc['label']}")
    print(f"  Predicted corrosion rate: {pred_rate:.2f} um/year")
    print(f"  Estimated service life before repair needed: {life_years:.1f} years")
