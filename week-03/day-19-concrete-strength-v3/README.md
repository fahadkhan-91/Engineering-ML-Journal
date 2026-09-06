# Day 19 (Week 3, Day 5): Concrete Strength Prediction v3
(Feature Engineering + Hyperparameter Tuning)

Goal: Extend Day 5's Random Forest model with engineered features 
(explicit w/c ratio from Day 6's Abrams' Law notes, log-transformed 
age from Day 15's curing insight) and properly tune hyperparameters 
using GridSearchCV instead of default settings.

## What I did
- Added w/c ratio and log(age) as explicit engineered features
- Compared basic vs engineered feature sets on the same model
- Ran GridSearchCV (5-fold CV) across n_estimators, max_depth, and 
  min_samples_split to find optimal hyperparameters
- Evaluated the final tuned model on a held-out test set

## Files
- `concrete_strength_v3.py` — main script

## Result
Feature engineering gave a small improvement (R² 0.911 → 0.913), and 
hyperparameter tuning pushed cross-validation R² to 0.935, with final 
test R² = 0.915 (MAE 2.64 MPa). This shows that domain-informed feature 
engineering (connecting back to Days 6 & 15's concepts) combined with 
proper tuning produces a more reliable model than defaults alone — even 
if the improvement isn't dramatic, the process is more rigorous and 
trustworthy.

Status: ✅ Completed
