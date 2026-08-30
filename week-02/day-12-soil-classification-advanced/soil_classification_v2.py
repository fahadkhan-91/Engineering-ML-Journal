"""
Day 12 (Week 2, Day 5): Soil Classification v2
(Model Comparison + Cross-Validation + Confusion Matrix)
--------------------------------------------------
Goal: Build on Day 8's soil classification model - compare 3 ML models
(Decision Tree, Random Forest, SVM) using proper cross-validation,
and visualize results with a confusion matrix. This demonstrates a
more rigorous ML evaluation workflow than a single train/test split.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

# -----------------------------
# 1. Generate synthetic soil dataset (same approach as Day 8, more samples)
# -----------------------------
n_samples = 300

coarse = np.column_stack([
    np.random.uniform(2, 55, n_samples // 3),
    np.random.uniform(0, 28, n_samples // 3),
    np.random.uniform(0, 10, n_samples // 3),
])

fine_low = np.column_stack([
    np.random.uniform(40, 100, n_samples // 3),
    np.random.uniform(18, 52, n_samples // 3),
    np.random.uniform(3, 28, n_samples // 3),
])

fine_high = np.column_stack([
    np.random.uniform(40, 100, n_samples // 3),
    np.random.uniform(45, 90, n_samples // 3),
    np.random.uniform(22, 60, n_samples // 3),
])

# Add some measurement noise to make classification more realistic
noise = np.random.normal(0, 3, (n_samples // 3 * 3, 3))

X = np.vstack([coarse, fine_low, fine_high]) + noise
X = np.clip(X, 0, None)
y = np.array([0] * len(coarse) + [1] * len(fine_low) + [2] * len(fine_high))
class_names = ["Coarse-grained", "Fine LL/PI Low", "Fine LL/PI High"]

# -----------------------------
# 2. Scale features (important for SVM)
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42, stratify=y
)

# -----------------------------
# 3. Define models to compare
# -----------------------------
models = {
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM (RBF)": SVC(kernel="rbf", random_state=42),
}

# -----------------------------
# 4. Cross-validation comparison (5-fold)
# -----------------------------
print("=" * 55)
print("5-FOLD CROSS-VALIDATION COMPARISON")
print("=" * 55)

cv_results = {}
for name, model in models.items():
    scores = cross_val_score(model, X_scaled, y, cv=5)
    cv_results[name] = scores
    print(f"{name:<15} Mean Accuracy: {scores.mean()*100:.2f}%  (+/- {scores.std()*100:.2f}%)")

best_model_name = max(cv_results, key=lambda k: cv_results[k].mean())
print(f"\nBest model (by CV): {best_model_name}")

# -----------------------------
# 5. Train best model on train set, evaluate on test set
# -----------------------------
best_model = models[best_model_name]
best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)

# -----------------------------
# 6. Confusion matrix visualization
# -----------------------------
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)

fig, ax = plt.subplots(figsize=(7, 6))
disp.plot(ax=ax, cmap="Blues", colorbar=True)
plt.title(f"Confusion Matrix - {best_model_name}")
plt.tight_layout()
plt.savefig("soil_confusion_matrix.png", dpi=150)
plt.show()

print(f"\nConfusion matrix saved as soil_confusion_matrix.png")
print(f"Test set accuracy: {(y_pred == y_test).mean()*100:.2f}%")
