"""
Day 36 (Week 6, Day 1): Validating Concrete Strength Models on REAL Data
--------------------------------------------------
Goal: Re-run the modeling approach from Day 1, Day 5, and Day 19 on the
REAL UCI Concrete Compressive Strength dataset (1030 lab-tested samples,
I-Cheng Yeh, 1998) instead of synthetic data - a critical validation
step after 5 weeks of synthetic-data practice.

Dataset source: UCI Machine Learning Repository
https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------
# 1. Load the REAL dataset
# -----------------------------
df = pd.read_csv("data/concrete_data.csv")

print("=" * 55)
print("DATASET OVERVIEW (Real UCI Data)")
print("=" * 55)
print(f"Shape: {df.shape}")
print(df.describe().round(2))

# -----------------------------
# 2. Prepare features (same 4 used in Day 1/5, plus full feature set)
# -----------------------------
X_basic = df[["cement", "water", "coarse_aggregate", "age"]].values
X_full = df.drop(columns=["concrete_compressive_strength"]).values
y = df["concrete_compressive_strength"].values

# -----------------------------
# 3. Re-run Day 1 style: Linear Regression, basic features
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X_basic, y, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)

print("\n" + "=" * 55)
print("STEP 1: Day 1 style - Linear Regression (4 basic features)")
print("=" * 55)
print(f"R2 Score: {r2_score(y_test, lr_pred):.3f}")
print(f"MAE: {mean_absolute_error(y_test, lr_pred):.2f} MPa")

# -----------------------------
# 4. Re-run Day 5 style: Random Forest, basic features
# -----------------------------
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)

print("\n" + "=" * 55)
print("STEP 2: Day 5 style - Random Forest (4 basic features)")
print("=" * 55)
print(f"R2 Score: {r2_score(y_test, rf_pred):.3f}")
print(f"MAE: {mean_absolute_error(y_test, rf_pred):.2f} MPa")

# -----------------------------
# 5. Use ALL 8 real features (cement, slag, fly ash, water,
# superplasticizer, coarse agg, fine agg, age) - not available in
# my synthetic version, which only had 4 features
# -----------------------------
X_train_f, X_test_f, y_train_f, y_test_f = train_test_split(X_full, y, test_size=0.2, random_state=42)

rf_full = RandomForestRegressor(n_estimators=200, max_depth=None, random_state=42)
rf_full.fit(X_train_f, y_train_f)
rf_full_pred = rf_full.predict(X_test_f)

print("\n" + "=" * 55)
print("STEP 3: Random Forest with ALL 8 real features")
print("=" * 55)
print(f"R2 Score: {r2_score(y_test_f, rf_full_pred):.3f}")
print(f"MAE: {mean_absolute_error(y_test_f, rf_full_pred):.2f} MPa")

feature_names = df.drop(columns=["concrete_compressive_strength"]).columns
print("\nFeature Importance (all 8 features):")
for name, imp in sorted(zip(feature_names, rf_full.feature_importances_), key=lambda x: -x[1]):
    print(f"  {name}: {imp:.3f}")

# -----------------------------
# 6. Cross-validation on real data (Day 13's method)
# IMPORTANT: real datasets are often NOT randomly ordered (this one
# groups similar mixes together), so we must shuffle before splitting
# into folds - otherwise folds can be biased and CV scores become
# unstable, which is exactly what happens if you skip this step.
# -----------------------------
from sklearn.model_selection import KFold

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(RandomForestRegressor(n_estimators=200, random_state=42),
                             X_full, y, cv=kfold, scoring="r2")
print(f"\n5-Fold CV R2 (all features, shuffled): {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# -----------------------------
# 7. Comparison summary: synthetic vs real
# -----------------------------
print("\n" + "=" * 55)
print("SYNTHETIC vs REAL DATA COMPARISON")
print("=" * 55)
print("Day 1  (synthetic, Linear Reg, 4 features):  R2 ~ 0.88 (self-generated)")
print(f"Day 36 (REAL data, Linear Reg, 4 features):  R2 = {r2_score(y_test, lr_pred):.3f}")
print("Day 5  (synthetic, Random Forest, 4 feat):    R2 ~ 0.91 (self-generated)")
print(f"Day 36 (REAL data, Random Forest, 4 feat):    R2 = {r2_score(y_test, rf_pred):.3f}")
print(f"Day 36 (REAL data, Random Forest, ALL feat):  R2 = {r2_score(y_test_f, rf_full_pred):.3f}")
