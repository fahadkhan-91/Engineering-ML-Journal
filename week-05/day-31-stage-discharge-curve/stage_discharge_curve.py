"""
Day 31 (Week 5, Day 3): Stage-Discharge (Rating) Curve Visualization
--------------------------------------------------
Goal: Plot a stage-discharge (rating) curve for a channel - showing
how discharge (Q) increases with flow depth (stage) - a fundamental
hydraulic engineering chart used for flow monitoring and flood
warning systems.

Uses Manning's Equation from Day 30 across a range of depths.
"""

import numpy as np
import matplotlib.pyplot as plt


def rectangular_channel_discharge(width_m, depth_m, slope, n):
    """Same Manning's equation approach as Day 30."""
    A = width_m * depth_m
    P = width_m + 2 * depth_m
    R = A / P
    V = (1 / n) * (R ** (2/3)) * (slope ** 0.5)
    Q = V * A
    return Q


# -----------------------------
# 1. Generate rating curves for 3 different channel widths
# -----------------------------
depths = np.linspace(0.1, 2.5, 50)
widths = [1.5, 2.0, 3.0]
slope = 0.002
n = 0.013  # concrete lined

fig, ax = plt.subplots(figsize=(8, 6))

for w in widths:
    discharges = [rectangular_channel_discharge(w, d, slope, n) for d in depths]
    ax.plot(discharges, depths, marker='', linewidth=2, label=f"Width = {w} m")

ax.set_xlabel("Discharge, Q (m3/s)")
ax.set_ylabel("Depth / Stage, h (m)")
ax.set_title("Stage-Discharge Rating Curves (Manning's Equation)")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

# -----------------------------
# 2. Mark a flood warning threshold example
# -----------------------------
warning_depth = 1.8
ax.axhline(warning_depth, color='red', linestyle=':', linewidth=1.5)
ax.text(0.5, warning_depth + 0.05, "Flood warning level (1.8m)", color='red', fontsize=9)

plt.tight_layout()
plt.savefig('stage_discharge_curve.png', dpi=150)
plt.show()

print("Chart saved as stage_discharge_curve.png\n")

# -----------------------------
# 3. Practical reading: discharge at warning level for each width
# -----------------------------
print("Discharge at flood warning depth (1.8m):")
for w in widths:
    q_at_warning = rectangular_channel_discharge(w, warning_depth, slope, n)
    print(f"  Width {w}m: Q = {q_at_warning:.2f} m3/s")

print("\nInsight: A rating curve lets field engineers read discharge")
print("directly from a measured water depth - no need to remeasure")
print("velocity every time, which is the basis of most river gauging stations.")
