# Day 22 (Week 4, Day 1): Reinforcement Steel Corrosion Rate Prediction

Goal: Predict corrosion rate of reinforcement steel in concrete based 
on key durability factors — chloride content, humidity, temperature, 
and concrete cover depth — using ML regression.

## What I did
- Generated synthetic corrosion data based on known physical 
  relationships (chloride-induced corrosion, cover depth protection)
- Trained and compared Linear Regression vs Random Forest
- Analyzed feature importance to identify the dominant corrosion driver
- Tested how varying cover depth affects predicted corrosion rate

## Files
- `corrosion_prediction.py` — main script

## Result
Linear Regression slightly outperformed Random Forest here (R²=0.957 
vs 0.936) since the underlying relationship was mostly linear. Chloride 
content was by far the most important feature (69.8% importance) — 
consistent with real-world RC durability engineering, where 
chloride-induced corrosion is the leading cause of reinforcement 
deterioration. Increasing cover depth from 20mm to 65mm nearly halved 
the predicted corrosion rate.

Status: ✅ Completed
