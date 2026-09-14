# Day 27: Linear Regression vs Random Forest — When to Use Which

## An Observation Across My Own Projects

Looking back at my projects, an interesting pattern emerged:

| Project | Best Model | Underlying Relationship |
|---------|-----------|--------------------------|
| Day 5/19: Concrete Strength | Random Forest | Non-linear (w/c ratio has diminishing effects, interactions between cement/age) |
| Day 22/26: Corrosion Rate | Linear Regression | Mostly linear (each factor adds roughly proportionally) |

This isn't a coincidence — it reflects a fundamental difference in 
how I generated the underlying relationships, and it mirrors real 
engineering behavior too.

## Why Linear Regression Won for Corrosion

My corrosion rate formula was a **weighted sum**: 
`8×chloride + 0.15×humidity + 0.3×temperature - 0.4×cover_depth`. 
This is inherently linear — each factor contributes independently and 
proportionally. Linear Regression is *built* to find exactly this 
kind of relationship, so it matched almost perfectly (R²=0.957 in 
Day 22).

Random Forest had to *approximate* this smooth linear surface using 
step-like splits, which introduces small errors — hence it performed 
slightly worse here.

## Why Random Forest Won for Concrete Strength

My concrete strength formula included water-cement **ratio** (a 
division, not a simple weighted sum) plus effectively different 
behavior at different cement/age combinations. This creates 
non-linear interactions that a straight-line model struggles with, 
but that Random Forest's tree-splitting approach can capture more 
naturally.

## Practical Rule of Thumb

- **If you suspect the relationship is roughly additive/proportional** 
  (each factor adds independently) → try Linear Regression first. 
  It's simpler, faster, more interpretable, and often "good enough."
- **If you suspect interactions, ratios, or thresholds** (e.g. "effect 
  of X depends on the value of Y") → Random Forest (or other tree-based 
  models) usually handles this better.
- **When unsure → try both.** This is exactly what I did in Day 5 and 
  Day 22 — comparing models isn't just a formality, it's genuinely 
  informative about the nature of the problem itself.

## Key Takeaway

A model's performance isn't just about the algorithm's power — it's 
about whether the algorithm's assumptions match the real structure of 
the problem. This is also why domain knowledge (understanding *why* 
w/c ratio behaves non-linearly, or *why* corrosion factors add up 
linearly) helps choose the right tool, not just the most powerful one.

## Connects to
- [Day 5: Concrete Strength v2](../week-01/day-05-concrete-strength-advanced)
- [Day 22: Corrosion Rate Prediction](../week-04/day-22-corrosion-prediction)
- [Day 26: Corrosion Prediction v2](../week-04/day-26-corrosion-prediction-v2)

Status: ✅ Completed
