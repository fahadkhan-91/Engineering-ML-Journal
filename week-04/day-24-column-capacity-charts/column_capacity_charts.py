"""
Day 24 (Week 4, Day 3): Column Capacity Trend Visualization
--------------------------------------------------
Goal: Visualize how RC column axial capacity (from Day 23) changes
with reinforcement bar count and concrete grade, turning tabular
results into intuitive design charts.
"""

import math
import numpy as np
import matplotlib.pyplot as plt


def calculate_column_capacity(fc, fy, width_mm, depth_mm, num_bars, bar_dia_mm, phi=0.65):
    """Same formula as Day 23."""
    Ag = width_mm * depth_mm
    Ast = num_bars * (math.pi / 4) * (bar_dia_mm ** 2)
    Pn = 0.80 * (0.85 * fc * (Ag - Ast) + fy * Ast)
    Pu = phi * Pn
    return Pu / 1000  # kN


# -----------------------------
# 1. Data: Capacity vs Number of Bars (for 3 concrete grades)
# -----------------------------
bar_counts = [4, 6, 8, 10, 12, 14, 16]
concrete_grades = [25, 30, 35]

fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Left plot: Capacity vs Bar Count, multiple concrete grades
for fc in concrete_grades:
    capacities = [
        calculate_column_capacity(fc, 500, 400, 400, n, 20) for n in bar_counts
    ]
    axes[0].plot(bar_counts, capacities, marker='o', label=f"f'c = {fc} MPa")

axes[0].set_xlabel("Number of 20mm Bars")
axes[0].set_ylabel("Design Capacity Pu (kN)")
axes[0].set_title("Column Capacity vs Reinforcement (400x400mm)")
axes[0].legend()
axes[0].grid(True, linestyle='--', alpha=0.6)

# -----------------------------
# 2. Data: Capacity vs Concrete Grade (for 3 bar counts)
# -----------------------------
fc_range = np.arange(20, 45, 2.5)
bar_options = [6, 8, 10]

for n_bars in bar_options:
    capacities = [
        calculate_column_capacity(fc, 500, 400, 400, n_bars, 20) for fc in fc_range
    ]
    axes[1].plot(fc_range, capacities, marker='s', label=f"{n_bars} bars")

axes[1].set_xlabel("Concrete Strength f'c (MPa)")
axes[1].set_ylabel("Design Capacity Pu (kN)")
axes[1].set_title("Column Capacity vs Concrete Grade (400x400mm)")
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.suptitle("RC Column Design Charts (Day 23 Data Visualized)", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('column_capacity_charts.png', dpi=150)
plt.show()

print("Charts saved as column_capacity_charts.png")

# -----------------------------
# 3. Quick insight: cost-efficiency comparison
# -----------------------------
print("\nInsight: Increasing concrete grade from 25 to 35 MPa (8 bars):")
cap_25 = calculate_column_capacity(25, 500, 400, 400, 8, 20)
cap_35 = calculate_column_capacity(35, 500, 400, 400, 8, 20)
print(f"  Capacity gain: {cap_25:.1f} kN -> {cap_35:.1f} kN ({(cap_35/cap_25 - 1)*100:.1f}% increase)")
