# Day 1: Concrete Compressive Strength Prediction

Goal: Predict concrete compressive strength using basic ML regression, 
based on mix ingredients (cement, water, aggregate, age).

## What I did
- Built a small dataset of concrete mixes (cement, water, aggregate, age → strength)
- Trained a Linear Regression model using scikit-learn
- Tested predictions on a custom mix

## Files
- `concrete_strength.py` — main script

## Result
Model runs and gives a strength prediction (MPa) for a given mix. 
Dataset is small for now — next step is to use a larger real dataset (e.g. UCI Concrete Compressive Strength dataset).

Status: ✅ Completed
