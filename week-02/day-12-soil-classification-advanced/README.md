# Day 12 (Week 2, Day 5): Soil Classification v2
(Model Comparison + Cross-Validation)

Goal: Extend Day 8's soil classification with a more rigorous ML 
workflow - compare 3 models using 5-fold cross-validation, and 
visualize results with a confusion matrix.

## What I did
- Regenerated soil dataset with more realistic overlap/noise between classes
- Scaled features using StandardScaler (important for SVM)
- Compared Decision Tree, Random Forest, and SVM (RBF kernel) using 
  5-fold cross-validation instead of a single train/test split
- Selected the best model and visualized its performance with a 
  confusion matrix

## Files
- `soil_classification_v2.py` — main script
- `soil_confusion_matrix.png` — output confusion matrix

## Result
SVM (RBF) performed best with ~95% mean cross-validation accuracy, 
followed by Random Forest (~94%) and Decision Tree (~90%). The 
confusion matrix showed most misclassifications occurred between 
"Fine LL/PI Low" and adjacent classes — expected since real soil 
classification boundaries aren't perfectly sharp either.

Status: ✅ Completed
