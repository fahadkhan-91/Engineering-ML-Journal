"""
Day 25 (Week 4, Day 4): Batch Column Design Checker (Automation)
--------------------------------------------------
Goal: Automate checking multiple RC columns against their applied
service loads in one pass, using Day 23's capacity formula, and
generate a clear pass/fail summary report - a task normally done
column-by-column manually.
"""

import math

# -----------------------------
# 1. Reuse Day 23's capacity formula
# -----------------------------
def calculate_column_capacity(fc, fy, width_mm, depth_mm, num_bars, bar_dia_mm, phi=0.65):
    Ag = width_mm * depth_mm
    Ast = num_bars * (math.pi / 4) * (bar_dia_mm ** 2)
    Pn = 0.80 * (0.85 * fc * (Ag - Ast) + fy * Ast)
    Pu_capacity = phi * Pn
    return Pu_capacity / 1000  # kN


# -----------------------------
# 2. Project column list: each with geometry, reinforcement, and applied load
# -----------------------------
columns = [
    {"id": "C1", "width": 400, "depth": 400, "num_bars": 8, "bar_dia": 20, "fc": 30, "applied_load_kN": 2200},
    {"id": "C2", "width": 350, "depth": 350, "num_bars": 6, "bar_dia": 16, "fc": 25, "applied_load_kN": 1600},
    {"id": "C3", "width": 450, "depth": 450, "num_bars": 10, "bar_dia": 20, "fc": 30, "applied_load_kN": 3200},
    {"id": "C4", "width": 300, "depth": 300, "num_bars": 4, "bar_dia": 16, "fc": 25, "applied_load_kN": 1200},
    {"id": "C5", "width": 400, "depth": 400, "num_bars": 8, "bar_dia": 20, "fc": 35, "applied_load_kN": 2900},
]

fy = 500  # steel yield strength, MPa (assumed same for all)

# -----------------------------
# 3. Run batch check
# -----------------------------
print(f"{'ID':<6}{'Capacity (kN)':<16}{'Applied (kN)':<15}{'Utilization':<14}{'Status':<10}")
print("-" * 65)

failed_columns = []

for col in columns:
    capacity = calculate_column_capacity(
        fc=col["fc"], fy=fy,
        width_mm=col["width"], depth_mm=col["depth"],
        num_bars=col["num_bars"], bar_dia_mm=col["bar_dia"]
    )
    utilization = col["applied_load_kN"] / capacity
    status = "PASS" if utilization <= 1.0 else "FAIL"

    if status == "FAIL":
        failed_columns.append(col["id"])

    print(f"{col['id']:<6}{capacity:<16.1f}{col['applied_load_kN']:<15}{str(round(utilization*100,1))+'%':<14}{status:<10}")

print("-" * 65)

# -----------------------------
# 4. Summary
# -----------------------------
print(f"\nTotal columns checked: {len(columns)}")
print(f"Passed: {len(columns) - len(failed_columns)}")
print(f"Failed: {len(failed_columns)}")

if failed_columns:
    print(f"Columns requiring redesign: {', '.join(failed_columns)}")
else:
    print("All columns meet capacity requirements.")
