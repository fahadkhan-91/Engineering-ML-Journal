"""
Day 8 (Week 2, Day 1): Soil Classification using ML
--------------------------------------------------
Goal: Classify soil type based on basic geotechnical parameters
(percent passing #200 sieve, liquid limit, plasticity index) using
a Decision Tree classifier - a simplified ML approach to USCS
(Unified Soil Classification System) style classification.

Simplified classes used here:
    0 = Coarse-grained (Gravel/Sand) -> e.g. GW, SW type
    1 = Fine-grained Low Plasticity  -> e.g. ML, CL type
    2 = Fine-grained High Plasticity -> e.g. MH, CH type
"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)

# -----------------------------
# 1. Generate synthetic soil samples
# Features: [% passing #200 sieve, liquid limit (LL), plasticity index (PI)]
# -----------------------------
n_samples = 150

# Coarse-grained soils: low fines content, low LL/PI
coarse = np.column_stack([
    np.random.uniform(2, 45, n_samples // 3),      # % passing #200
    np.random.uniform(0, 20, n_samples // 3),       # LL
    np.random.uniform(0, 5, n_samples // 3),        # PI
])

# Fine-grained, low plasticity: high fines, moderate LL
fine_low = np.column_stack([
    np.random.uniform(50, 100, n_samples // 3),
    np.random.uniform(20, 50, n_samples // 3),
    np.random.uniform(4, 25, n_samples // 3),
])

# Fine-grained, high plasticity: high fines, high LL
fine_high = np.column_stack([
    np.random.uniform(50, 100, n_samples // 3),
    np.random.uniform(50, 90, n_samples // 3),
    np.random.uniform(25, 60, n_samples // 3),
])

X = np.vstack([coarse, fine_low, fine_high])
y = np.array(
    [0] * len(coarse) + [1] * len(fine_low) + [2] * len(fine_high)
)

class_names = ["Coarse-grained (Gravel/Sand)", "Fine-grained Low Plasticity", "Fine-grained High Plasticity"]

# -----------------------------
# 2. Split data
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 3. Train Decision Tree Classifier
# -----------------------------
model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 4. Evaluate
# -----------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=class_names))

# -----------------------------
# 5. Feature importance
# -----------------------------
feature_names = ["% Passing #200 Sieve", "Liquid Limit", "Plasticity Index"]
print("Feature Importance:")
for name, imp in sorted(zip(feature_names, model.feature_importances_), key=lambda x: -x[1]):
    print(f"  {name}: {imp:.3f}")

# -----------------------------
# 6. Classify a new soil sample
# -----------------------------
new_sample = np.array([[65, 45, 22]])  # passing #200=65%, LL=45, PI=22
prediction = model.predict(new_sample)[0]

print(f"\nNew soil sample (passing #200=65%, LL=45, PI=22):")
print(f"Predicted classification: {class_names[prediction]}")
