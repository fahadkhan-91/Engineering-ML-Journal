# Day 29 (Week 5, Day 1): Rainfall-Runoff Prediction

Goal: Predict surface runoff from a catchment using rainfall depth, 
curve number (land use + soil), catchment area, and slope — a core 
task in drainage design, flood estimation, and stormwater management.

New domain: this is my first hydrology/water resources project, 
extending beyond the concrete/structures focus of Weeks 1-4.

## What I did
- Implemented the SCS Curve Number (CN) method — a standard hydrology 
  approach: Q = (P − 0.2S)² / (P + 0.8S)
- Generated catchment scenarios across realistic CN ranges (55–95)
- Trained and compared Linear Regression vs Random Forest
- Applied the model to estimate design runoff volumes for rural, 
  suburban, and dense urban catchments

## Files
- `rainfall_runoff.py` — main script

## Result
Random Forest clearly outperformed Linear Regression (R²=0.973 vs 
0.896) — consistent with Day 27's note, since the SCS-CN formula is 
inherently non-linear.

For the same 100mm rainfall over a 10 km² catchment: a rural catchment 
(CN=60) produced ~248,600 m³ of runoff, while a dense urban catchment 
(CN=92) produced ~828,400 m³ — over 3× more. This quantifies exactly 
why urbanization drives increased flood risk and why stormwater 
infrastructure must scale with development.

Status: ✅ Completed
