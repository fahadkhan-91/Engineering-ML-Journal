# Day 5: Concrete Strength Prediction v2 (Model Comparison)

Goal: Extend Day 1's basic model with a larger dataset (200 samples) 
and compare Linear Regression vs Random Forest to see which handles 
concrete strength prediction better.

## What I did
- Generated a larger, more realistic synthetic dataset (200 samples)
- Trained both Linear Regression and Random Forest models
- Compared MAE and R² scores between the two
- Analyzed feature importance to see which mix ingredient matters most
- Tested both models on a custom concrete mix

## Files
- `concrete_strength_v2.py` — main script

## Result
Random Forest outperformed Linear Regression (R² = 0.91 vs 0.88). 
Cement content came out as the most important feature affecting 
strength — consistent with real concrete behavior (higher cement 
content generally increases compressive strength, along with lower 
water-cement ratio).

Status: ✅ Completed
