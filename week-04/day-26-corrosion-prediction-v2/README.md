# Day 26 (Week 4, Day 5): Corrosion Prediction v2
(Cross-Validation + Tuning + Service Life Estimation)

Goal: Extend Day 22's corrosion model using the rigorous ML workflow 
from Days 13 & 19 (cross-validation + hyperparameter tuning), then 
translate the prediction into a practical engineering output: 
estimated structure service life before repair is needed.

## What I did
- Applied 5-fold cross-validation as a baseline check (Day 13's method)
- Tuned Random Forest hyperparameters using GridSearchCV (Day 19's method)
- Built a service life estimator: converts predicted corrosion rate 
  into estimated years until 10% bar diameter loss (a common 
  durability threshold)
- Tested 3 risk scenarios (low/moderate/high) end-to-end

## Files
- `corrosion_prediction_v2.py` — main script

## Result
Tuned model achieved test R² = 0.918 (MAE 3.21 μm/year). Applied to 
3 realistic scenarios: low-risk conditions gave an estimated 186-year 
service life, while high-risk conditions (high chloride, low cover) 
dropped this to just 37.2 years — a clear, actionable illustration of 
why cover depth and chloride exposure control matter so much in 
durable RC design.

Status: ✅ Completed
