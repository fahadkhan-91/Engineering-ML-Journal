"""
Day 23 (Week 4, Day 2): RC Column Axial Capacity Calculator
--------------------------------------------------
Goal: Calculate the nominal and design axial load capacity of a
tied reinforced concrete column, based on a simplified version of
the ACI 318 approach.

Formula (tied column, simplified):
    Pn = 0.80 * [0.85 * f'c * (Ag - Ast) + fy * Ast]
    Pu (design capacity) = phi * Pn   (phi = 0.65 for tied columns)

Where:
    f'c  = concrete compressive strength (MPa)
    fy   = steel yield strength (MPa)
    Ag   = gross cross-sectional area of column (mm2)
    Ast  = total area of longitudinal steel reinforcement (mm2)
"""

import math


def calculate_column_capacity(fc, fy, width_mm, depth_mm, num_bars, bar_dia_mm, phi=0.65):
    """
    Calculate axial load capacity of a tied RC column.
    """
    Ag = width_mm * depth_mm
    Ast = num_bars * (math.pi / 4) * (bar_dia_mm ** 2)

    # Check steel ratio is within typical ACI limits (1% - 8%)
    steel_ratio = Ast / Ag

    Pn = 0.80 * (0.85 * fc * (Ag - Ast) + fy * Ast)  # Newtons
    Pu = phi * Pn

    return {
        "Ag_mm2": round(Ag, 1),
        "Ast_mm2": round(Ast, 1),
        "steel_ratio_pct": round(steel_ratio * 100, 2),
        "Pn_kN": round(Pn / 1000, 1),
        "Pu_kN": round(Pu / 1000, 1),
    }


# -----------------------------
# Example: 400mm x 400mm column, 30 MPa concrete, Fe500 steel
# 8 bars of 20mm diameter
# -----------------------------
result = calculate_column_capacity(
    fc=30, fy=500,
    width_mm=400, depth_mm=400,
    num_bars=8, bar_dia_mm=20
)

print("=" * 50)
print("RC COLUMN AXIAL CAPACITY (400x400mm, 8-T20 bars)")
print("=" * 50)
for key, value in result.items():
    print(f"{key}: {value}")

if 1.0 <= result["steel_ratio_pct"] <= 8.0:
    print("\nSteel ratio: OK (within ACI 1%-8% limit)")
else:
    print("\nSteel ratio: WARNING - outside typical ACI limits")

# -----------------------------
# Compare capacity across different bar counts
# -----------------------------
print("\n--- Capacity vs Number of Bars (20mm dia) ---")
for n_bars in [6, 8, 10, 12]:
    r = calculate_column_capacity(fc=30, fy=500, width_mm=400, depth_mm=400,
                                    num_bars=n_bars, bar_dia_mm=20)
    print(f"  {n_bars} bars -> Pu = {r['Pu_kN']} kN  (steel ratio: {r['steel_ratio_pct']}%)")

# -----------------------------
# Compare capacity across different concrete grades
# -----------------------------
print("\n--- Capacity vs Concrete Grade (8-T20 bars) ---")
for fc in [20, 25, 30, 35, 40]:
    r = calculate_column_capacity(fc=fc, fy=500, width_mm=400, depth_mm=400,
                                    num_bars=8, bar_dia_mm=20)
    print(f"  f'c={fc} MPa -> Pu = {r['Pu_kN']} kN")
