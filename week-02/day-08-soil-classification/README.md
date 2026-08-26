# Day 8 (Week 2, Day 1): Soil Classification using ML

Goal: Classify soil type (coarse-grained vs fine-grained low/high 
plasticity) based on basic geotechnical index properties, using a 
Decision Tree classifier — a simplified USCS-style approach.

## What I did
- Generated synthetic soil samples using 3 key parameters: % passing 
  #200 sieve, Liquid Limit (LL), Plasticity Index (PI)
- Trained a Decision Tree Classifier to predict soil category
- Evaluated with accuracy score and classification report
- Checked feature importance to see which property drives classification

## Files
- `soil_classification.py` — main script

## Result
Model achieved ~97% accuracy on test data. Liquid Limit and Plasticity 
Index turned out to be the most important features — consistent with 
how the actual USCS/Casagrande plasticity chart works in real 
geotechnical practice.

Status: ✅ Completed
