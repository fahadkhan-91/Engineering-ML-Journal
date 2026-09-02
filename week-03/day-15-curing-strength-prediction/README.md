# Day 15 (Week 3, Day 1): Concrete Curing Strength Gain Prediction

Goal: Model how concrete compressive strength develops over curing 
time using the ACI-style hyperbolic strength-gain relationship, and 
fit a regression model (using log-transformed time) to predict 
strength at any curing age.

## What I did
- Generated realistic curing strength data (day 1 to day 365) using 
  the empirical formula: strength(t) = f28 * (t / (a + b*t))
- Fit a Linear Regression model using ln(day) as the input feature
- Predicted strength at custom curing ages
- Calculated % of 28-day strength achieved at key milestones (3, 7, 
  14, 28 days)

## Files
- `curing_strength.py` — main script

## Result
Model achieved R² = 0.885. Confirmed the well-known engineering rule 
of thumb: concrete reaches ~70% of its 28-day strength by day 7, and 
~88% by day 14 — useful for planning formwork removal and construction 
schedules on site.

Status: ✅ Completed
