"""
Day 9 (Week 2, Day 2): ACI Concrete Mix Design Calculator (Simplified)
--------------------------------------------------
Goal: Automate a simplified version of the ACI 211.1 mix design method
to estimate water-cement ratio, cement content, and approximate mix
proportions for a target compressive strength.

Note: This is a simplified educational version. Real mix design
requires full ACI tables, admixture considerations, and lab trials.
"""

def estimate_water_cement_ratio(target_strength_mpa):
    """
    Simplified w/c ratio estimation based on target 28-day strength.
    Based on typical ACI 211.1 strength vs w/c ratio relationships
    (approximate values for non-air-entrained concrete).
    """
    strength_wc_table = {
        45: 0.38,
        40: 0.43,
        35: 0.48,
        30: 0.55,
        25: 0.62,
        20: 0.68,
        15: 0.75,
    }

    # Find closest match (simplified - real design interpolates properly)
    closest_strength = min(strength_wc_table.keys(), key=lambda x: abs(x - target_strength_mpa))
    return strength_wc_table[closest_strength]


def estimate_water_content(max_agg_size_mm, slump_mm=75):
    """
    Simplified water content estimate (kg/m3) based on max aggregate
    size, for a target slump (workability). Based on typical ACI
    tables for angular aggregate, non-air-entrained concrete.
    """
    water_table = {
        10: 208,
        12.5: 199,
        20: 190,
        25: 179,
        40: 166,
        50: 154,
    }
    closest_size = min(water_table.keys(), key=lambda x: abs(x - max_agg_size_mm))
    return water_table[closest_size]


def calculate_mix_design(target_strength_mpa, max_agg_size_mm=20, slump_mm=75):
    """Calculate simplified mix design proportions."""
    wc_ratio = estimate_water_cement_ratio(target_strength_mpa)
    water_content = estimate_water_content(max_agg_size_mm, slump_mm)
    cement_content = water_content / wc_ratio

    # Simplified coarse aggregate estimate (kg/m3) - typical range
    coarse_agg_estimate = 1100  # placeholder, real value depends on fineness modulus

    return {
        "target_strength_mpa": target_strength_mpa,
        "wc_ratio": round(wc_ratio, 2),
        "water_kg_m3": water_content,
        "cement_kg_m3": round(cement_content, 1),
        "coarse_agg_kg_m3": coarse_agg_estimate,
    }


# -----------------------------
# Example: Design mix for 30 MPa target strength
# -----------------------------
mix = calculate_mix_design(target_strength_mpa=30, max_agg_size_mm=20, slump_mm=75)

print("=" * 45)
print("ACI Mix Design (Simplified) - Target: 30 MPa")
print("=" * 45)
for key, value in mix.items():
    print(f"{key}: {value}")

# -----------------------------
# Compare a few different target strengths
# -----------------------------
print("\n--- Comparison across target strengths ---")
for strength in [20, 25, 30, 35, 40]:
    result = calculate_mix_design(strength)
    print(f"Target {strength} MPa -> w/c={result['wc_ratio']}, "
          f"Cement={result['cement_kg_m3']} kg/m3, Water={result['water_kg_m3']} kg/m3")
