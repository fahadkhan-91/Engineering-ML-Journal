# Day 33 (Week 5, Day 5): Rainfall-Runoff Prediction v2
(Cross-Validation + Tuning + Return Period Analysis)

Goal: Extend Day 29's rainfall-runoff model using the rigorous ML 
workflow established in Days 13/19/26, then apply it to a real flood 
engineering question: how does design runoff scale across storm 
return periods (2-year to 100-year)?

## What I did
- Applied 5-fold cross-validation as a baseline check
- Tuned Random Forest hyperparameters using GridSearchCV
- Applied the tuned model across 6 standard design storm return 
  periods (2, 5, 10, 25, 50, 100-year) for a fixed suburban catchment

## Files
- `rainfall_runoff_v2.py` — main script

## Result
Tuned model achieved test R² = 0.974 (MAE 4.93mm). For a 15 km² 
suburban catchment (CN=78): runoff volume scaled from ~251,000 m³ 
for a 2-year storm to ~1.44 million m³ for a 100-year storm — nearly 
6× more. This kind of return-period analysis is exactly what's used 
in practice to size detention basins and spillways for different 
acceptable flood risk levels.

Status: ✅ Completed
