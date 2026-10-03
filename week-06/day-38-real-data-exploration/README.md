# Day 38 (Week 6, Day 3): Exploratory Data Analysis on Real Concrete Data

Goal: Visually explore the real UCI dataset (Day 36) — how each 
ingredient relates to compressive strength, and how ingredients 
correlate with each other. This is standard EDA that normally 
happens before modeling; doing it here on real data for the first 
time in this journal.

## What I did
- Plotted each of the 8 ingredients against compressive strength 
  (8-panel scatter grid)
- Built a correlation heatmap across all variables
- Ranked ingredients by strength of correlation with compressive strength

## Files
- `explore_concrete_data.py` — main script
- `feature_vs_strength.png` — scatter plots
- `correlation_heatmap.png` — correlation matrix

## Result
Cement showed the clearest positive relationship with strength, 
while water showed a clear negative relationship — both consistent 
with Day 6's Abrams' Law notes. Superplasticizer and age also 
correlated positively. This kind of EDA is exactly what should 
precede modeling, and doing it now (after Day 36's validation) 
confirms the real data behaves the way the domain theory predicts.

Status: ✅ Completed
