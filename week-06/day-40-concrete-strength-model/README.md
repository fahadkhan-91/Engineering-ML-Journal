# Day 40: Final Concrete Strength Model — Feature Engineering + CV + Tuning (Real Data)

**Week 6, Day 5 — ML Deep Dive**

## Goal
Bring together every technique learned in this journal and apply the full rigorous
workflow — for the first time — to the real UCI dataset:

- Feature engineering (Day 19: water/cement ratio, log(age), + a new one — total binder content)
- Shuffled K-Fold cross-validation (the hard lesson from Day 36)
- GridSearchCV hyperparameter tuning (Day 19 / Day 26 / Day 33's pattern)

This is meant to be the most trustworthy model in the repository, because it's the
only one where every past lesson is applied at once, on real data.

## What's new: `total_binder`
`total_binder = cement + blast_furnace_slag + fly_ash` — the combined cementitious
material content. This is a real mix-design metric (binder content strongly drives
strength and durability) that hadn't been used anywhere earlier in this journal,
even though slag and fly ash appear as individual columns in the real dataset.

## Method
1. Load the real dataset (Day 36) and engineer 3 extra features on top of the 8 raw ones.
2. Train the same Random Forest on base features vs. engineered features, same train/test split — isolates the effect of feature engineering alone.
3. Run 5-fold cross-validation with `shuffle=True` (Day 36's lesson — real rows aren't randomly ordered).
4. Run `GridSearchCV` over `n_estimators`, `max_depth`, `min_samples_split` to tune the Random Forest.
5. Evaluate the tuned model on a held-out test set, and print feature importances.

## Results (run this yourself against the full 1030-row dataset for the real numbers)
Running this on the small verification sample during testing predictably gives poor
R2 — a handful of rows can't support a train/test split. On the real 1030-row
dataset, expect R2 in the 0.90–0.93 range, consistent with Day 36's R2 = 0.907
(±0.016) cross-validation result, since this model builds directly on that same
groundwork with added features and tuning.

## How this connects to the rest of the journal
- Day 6: Abrams' Law → water_cement_ratio feature
- Day 13: Cross-validation basics → the CV step here
- Day 15: Curing strength-gain curve → log(age) feature
- Day 19 / Day 26 / Day 33: GridSearchCV tuning pattern, reused again
- Day 36: Real dataset + the shuffled-KFold fix that makes this CV step trustworthy
- Day 37/38/39: Earlier uses of the real dataset (recommender, EDA, report generator)

Day 40 is the convergence point — every earlier tool applied together, on real data,
for the first time.

## Files
- `concrete_strength_final_model.py` — full pipeline, run from this folder
