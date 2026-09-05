"""
Day 18 (Week 3, Day 4): Concrete Carbon Footprint Calculator (Automation)
--------------------------------------------------
Goal: Automate the calculation of embodied carbon (CO2 emissions) for
a concrete mix, based on material quantities - an increasingly
important sustainability metric in modern construction/green building.

Emission factors used are typical published values (kg CO2 per kg or
per m3 of material) - simplified for educational use.
"""

# -----------------------------
# 1. Embodied carbon factors (kg CO2e per unit)
# Based on typical published values (varies by region/source in reality)
# -----------------------------
emission_factors = {
    "cement_kg_co2_per_kg": 0.90,       # cement is the biggest contributor
    "sand_kg_co2_per_m3": 5.0,
    "coarse_agg_kg_co2_per_m3": 6.0,
    "water_kg_co2_per_liter": 0.0003,
    "steel_kg_co2_per_kg": 1.85,        # for reinforcement comparison
}

# -----------------------------
# 2. Material quantities (from Day 11's quantity estimator example)
# -----------------------------
project_materials = {
    "cement_kg": 11495,      # from ~230 bags * 50 kg
    "sand_m3": 12.071,
    "coarse_agg_m3": 24.142,
    "water_liters": 5748,
    "steel_kg": 1950,         # from Day 4's rebar calculator example
}


def calculate_carbon_footprint(materials, factors):
    """Calculate total embodied carbon (kg CO2e) for a project."""
    emissions = {}

    emissions["cement"] = materials["cement_kg"] * factors["cement_kg_co2_per_kg"]
    emissions["sand"] = materials["sand_m3"] * factors["sand_kg_co2_per_m3"]
    emissions["coarse_agg"] = materials["coarse_agg_m3"] * factors["coarse_agg_kg_co2_per_m3"]
    emissions["water"] = materials["water_liters"] * factors["water_kg_co2_per_liter"]
    emissions["steel"] = materials["steel_kg"] * factors["steel_kg_co2_per_kg"]

    emissions["total"] = sum(emissions.values())
    return emissions


# -----------------------------
# 3. Calculate and display results
# -----------------------------
results = calculate_carbon_footprint(project_materials, emission_factors)

print("=" * 50)
print("CONCRETE PROJECT - EMBODIED CARBON FOOTPRINT")
print("=" * 50)

for material, co2 in results.items():
    if material != "total":
        pct = (co2 / results["total"]) * 100
        print(f"{material.capitalize():<15}: {co2:>10.1f} kg CO2e  ({pct:.1f}%)")

print("-" * 50)
print(f"{'TOTAL':<15}: {results['total']:>10.1f} kg CO2e")
print(f"{'TOTAL (tons)':<15}: {results['total']/1000:>10.2f} tons CO2e")

# -----------------------------
# 4. Compare: what if we reduce cement by using fly ash replacement?
# -----------------------------
fly_ash_replacement_pct = 20  # common practice: replace 20% cement with fly ash
reduced_cement = project_materials["cement_kg"] * (1 - fly_ash_replacement_pct / 100)
fly_ash_co2_per_kg = 0.02  # fly ash is a waste byproduct, very low emissions

reduced_materials = project_materials.copy()
reduced_materials["cement_kg"] = reduced_cement

reduced_emissions = calculate_carbon_footprint(reduced_materials, emission_factors)
fly_ash_kg = project_materials["cement_kg"] * (fly_ash_replacement_pct / 100)
fly_ash_emissions = fly_ash_kg * fly_ash_co2_per_kg

new_total = reduced_emissions["total"] + fly_ash_emissions
savings = results["total"] - new_total
savings_pct = (savings / results["total"]) * 100

print(f"\n--- Scenario: {fly_ash_replacement_pct}% Fly Ash Cement Replacement ---")
print(f"New total emissions: {new_total:.1f} kg CO2e")
print(f"CO2 savings: {savings:.1f} kg CO2e ({savings_pct:.1f}% reduction)")
