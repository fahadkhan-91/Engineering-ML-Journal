"""
Day 32 (Week 5, Day 4): Culvert/Pipe Sizing Selector (Automation)
--------------------------------------------------
Goal: Automate selection of the smallest standard circular pipe/culvert
diameter that satisfies a required design discharge, using Manning's
Equation for circular pipes flowing full - a repetitive drainage
design task normally done by manual trial-and-error.
"""

import math

# -----------------------------
# 1. Standard commercially available pipe diameters (mm)
# -----------------------------
standard_diameters_mm = [300, 375, 450, 600, 750, 900, 1050, 1200, 1500, 1800]


def circular_pipe_full_discharge(diameter_mm, slope, n=0.013):
    """
    Calculate discharge for a circular pipe flowing full, using
    Manning's Equation. Returns Q in m3/s.
    """
    D = diameter_mm / 1000  # convert to meters
    A = math.pi * (D ** 2) / 4
    P = math.pi * D
    R = A / P  # = D/4 for full circular pipe
    V = (1 / n) * (R ** (2/3)) * (slope ** 0.5)
    Q = V * A
    return Q


def select_pipe_size(required_discharge_m3s, slope, n=0.013, safety_factor=1.1):
    """
    Automatically select the smallest standard pipe diameter that
    meets the required discharge, including a safety factor.
    """
    target_discharge = required_discharge_m3s * safety_factor

    for diameter in standard_diameters_mm:
        capacity = circular_pipe_full_discharge(diameter, slope, n)
        if capacity >= target_discharge:
            return {
                "selected_diameter_mm": diameter,
                "capacity_m3s": round(capacity, 3),
                "required_with_sf_m3s": round(target_discharge, 3),
                "utilization_pct": round((target_discharge / capacity) * 100, 1),
            }

    return None  # no standard size is adequate


# -----------------------------
# 2. Batch process multiple culvert design points (e.g. across a road project)
# -----------------------------
design_points = [
    {"id": "Culvert-1", "required_Q": 0.15, "slope": 0.005},
    {"id": "Culvert-2", "required_Q": 0.45, "slope": 0.003},
    {"id": "Culvert-3", "required_Q": 0.90, "slope": 0.004},
    {"id": "Culvert-4", "required_Q": 1.80, "slope": 0.002},
    {"id": "Culvert-5", "required_Q": 3.50, "slope": 0.0025},
]

print("=" * 70)
print("CULVERT SIZING SELECTION (with 10% safety factor)")
print("=" * 70)
print(f"{'ID':<12}{'Req. Q (m3/s)':<15}{'Selected (mm)':<16}{'Capacity (m3/s)':<17}{'Util. %':<10}")
print("-" * 70)

for point in design_points:
    result = select_pipe_size(point["required_Q"], point["slope"])
    if result:
        print(f"{point['id']:<12}{point['required_Q']:<15}{result['selected_diameter_mm']:<16}"
              f"{result['capacity_m3s']:<17}{result['utilization_pct']:<10}")
    else:
        print(f"{point['id']:<12}{point['required_Q']:<15}{'NO STANDARD SIZE ADEQUATE':<33}")

print("-" * 70)
print("\nNote: Selection uses smallest standard diameter meeting demand")
print("with safety factor - avoids over-sizing (cost) or under-sizing (flood risk).")
