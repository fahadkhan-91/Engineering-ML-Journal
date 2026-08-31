# Day 13: Understanding Cross-Validation (Why It Matters)

## The Problem with a Single Train/Test Split

In Day 1 and Day 8, I used a single train/test split (e.g. 80/20) to 
evaluate models. The problem: results depend heavily on *which* 
samples randomly ended up in the test set. A lucky or unlucky split 
can make a model look better or worse than it really is.

## What Cross-Validation Does

**K-Fold Cross-Validation** (used in Day 12) splits the dataset into 
`k` equal parts (folds). The model trains on `k-1` folds and tests on 
the remaining fold — this repeats `k` times, with each fold getting 
a turn as the test set.

Example: 5-Fold Cross-Validation

Fold 1: [TEST] [train] [train] [train] [train]
Fold 2: [train] [TEST] [train] [train] [train]
Fold 3: [train] [train] [TEST] [train] [train]
Fold 4: [train] [train] [train] [TEST] [train]
Fold 5: [train] [train] [train] [train] [TEST]


The final accuracy is the **average across all 5 folds** — a much 
more reliable estimate than one lucky/unlucky split.

## Why This Matters for Engineering ML Projects

In Day 12's soil classification, cross-validation gave both a mean 
accuracy AND a standard deviation (e.g. 95% ± 1.8%). That standard 
deviation is important — it tells us how *stable* the model is across 
different data subsets. A model with low std is more trustworthy for 
real engineering decisions than one that varies wildly between folds.

## Key Takeaway

For engineering applications — where a wrong prediction could mean a 
real structural or material risk — a single train/test split isn't 
enough to trust a model. Cross-validation is a minimum standard for 
any ML model before considering it reliable enough to inform actual 
engineering decisions.

## Connects to
- [Day 8: Soil Classification](../week-02/day-08-soil-classification)
- [Day 12: Soil Classification v2](../week-02/day-12-soil-classification-advanced)

Status: ✅ Completed
