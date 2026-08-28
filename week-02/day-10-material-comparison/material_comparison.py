"""
Day 10 (Week 2, Day 3): Construction Material Properties Comparison
--------------------------------------------------
Goal: Visually compare key engineering properties of common
construction materials (Steel, Concrete, Timber, Aluminum) to build
intuition for material selection decisions.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Material properties data (typical/representative values)
# -----------------------------
materials = ["Steel", "Concrete", "Timber", "Aluminum"]

density = [7850, 2400, 600, 2700]                  # kg/m3
compressive_strength = [400, 30, 40, 200]          # MPa (approx, for comparison)
elastic_modulus = [200, 25, 11, 69]                # GPa
approx_cost_index = [3.5, 1.0, 1.8, 5.0]           # relative cost index (concrete = 1.0)

# -----------------------------
# 2. Create a 2x2 subplot comparison dashboard
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2']

# Density
axes[0, 0].bar(materials, density, color=colors)
axes[0, 0].set_title('Density (kg/m³)')
axes[0, 0].set_ylabel('kg/m³')

# Compressive Strength
axes[0, 1].bar(materials, compressive_strength, color=colors)
axes[0, 1].set_title('Compressive Strength (MPa)')
axes[0, 1].set_ylabel('MPa')

# Elastic Modulus
axes[1, 0].bar(materials, elastic_modulus, color=colors)
axes[1, 0].set_title('Elastic Modulus (GPa)')
axes[1, 0].set_ylabel('GPa')

# Relative Cost Index
axes[1, 1].bar(materials, approx_cost_index, color=colors)
axes[1, 1].set_title('Relative Cost Index (Concrete = 1.0)')
axes[1, 1].set_ylabel('Cost Index')

plt.suptitle('Construction Material Properties Comparison', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('material_comparison.png', dpi=150)
plt.show()

print("Chart saved as material_comparison.png\n")

# -----------------------------
# 3. Strength-to-weight ratio (useful engineering insight)
# -----------------------------
print("Strength-to-Weight Ratio (Compressive Strength / Density):")
for m, s, d in zip(materials, compressive_strength, density):
    ratio = s / d * 1000  # scaled for readability
    print(f"  {m}: {ratio:.3f} (MPa per 1000 kg/m3)")

best_ratio_material = materials[np.argmax([s/d for s, d in zip(compressive_strength, density)])]
print(f"\nBest strength-to-weight ratio: {best_ratio_material}")
