"""
Day 3: Stress-Strain Curve Visualization
--------------------------------------------------
Goal: Plot stress-strain curves for different materials (mild steel,
concrete, aluminum) to visually compare their mechanical behavior.

This is a simplified/idealized representation for learning purposes,
not lab-measured data.
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Mild Steel (idealized elastic-plastic behavior)
# -----------------------------
strain_steel = np.array([0, 0.001, 0.002, 0.0025, 0.01, 0.05, 0.15, 0.20])
stress_steel = np.array([0, 200, 250, 250, 260, 350, 400, 380])  # MPa

# -----------------------------
# 2. Concrete (parabolic rise, brittle drop - compression only)
# -----------------------------
strain_concrete = np.linspace(0, 0.0035, 50)
fc = 30  # MPa, characteristic compressive strength
strain_0 = 0.002
stress_concrete = fc * (2 * (strain_concrete / strain_0) - (strain_concrete / strain_0) ** 2)
stress_concrete = np.clip(stress_concrete, 0, None)

# -----------------------------
# 3. Aluminum (smoother curve, lower stiffness than steel)
# -----------------------------
strain_alu = np.array([0, 0.001, 0.003, 0.005, 0.01, 0.03, 0.08, 0.12])
stress_alu = np.array([0, 70, 120, 140, 150, 170, 190, 195])  # MPa

# -----------------------------
# 4. Plot all three
# -----------------------------
plt.figure(figsize=(8, 6))

plt.plot(strain_steel, stress_steel, marker='o', label='Mild Steel', color='blue')
plt.plot(strain_concrete, stress_concrete, label='Concrete (compression)', color='gray')
plt.plot(strain_alu, stress_alu, marker='s', label='Aluminum', color='orange')

plt.xlabel('Strain (mm/mm)')
plt.ylabel('Stress (MPa)')
plt.title('Stress-Strain Curves: Steel vs Concrete vs Aluminum')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.savefig('stress_strain_comparison.png', dpi=150)
plt.show()

print("Plot saved as stress_strain_comparison.png")
print("\nKey observations:")
print(f"- Mild Steel: yields around {stress_steel[2]} MPa, then strain hardens")
print(f"- Concrete: brittle, peak stress ~{fc} MPa at strain ~{strain_0}")
print(f"- Aluminum: no clear yield point, more gradual curve")
