"""
Day 4: Rebar Weight & Cost Calculator (Automation Tool)
--------------------------------------------------
Goal: Automate the tedious manual task of calculating total rebar
weight and estimated cost for a construction project, given bar
diameters and lengths (common BOQ/estimation task).

Formula used (standard steel rebar unit weight):
    unit_weight (kg/m) = (d^2) / 162
    where d = bar diameter in mm
"""

# -----------------------------
# 1. Standard unit weights (kg/m) for common bar diameters
# -----------------------------
def unit_weight(diameter_mm):
    """Standard formula for steel rebar unit weight (kg/m)."""
    return (diameter_mm ** 2) / 162


# -----------------------------
# 2. Project rebar list
# Format: (diameter_mm, total_length_m, quantity)
# -----------------------------
rebar_list = [
    {"diameter": 10, "length_m": 12, "quantity": 40},
    {"diameter": 12, "length_m": 12, "quantity": 60},
    {"diameter": 16, "length_m": 12, "quantity": 30},
    {"diameter": 20, "length_m": 12, "quantity": 15},
]

# -----------------------------
# 3. Cost per kg (example rate, adjust as needed)
# -----------------------------
rate_per_kg = 280  # PKR per kg (example)

# -----------------------------
# 4. Calculate weight and cost for each bar type
# -----------------------------
total_weight = 0
total_cost = 0

print(f"{'Dia (mm)':<10}{'Unit Wt (kg/m)':<16}{'Total Length (m)':<18}{'Weight (kg)':<14}{'Cost (PKR)':<12}")
print("-" * 70)

for bar in rebar_list:
    d = bar["diameter"]
    total_length = bar["length_m"] * bar["quantity"]
    uw = unit_weight(d)
    weight = uw * total_length
    cost = weight * rate_per_kg

    total_weight += weight
    total_cost += cost

    print(f"{d:<10}{uw:<16.3f}{total_length:<18}{weight:<14.2f}{cost:<12.2f}")

print("-" * 70)
print(f"TOTAL WEIGHT: {total_weight:.2f} kg")
print(f"TOTAL ESTIMATED COST: {total_cost:.2f} PKR")

# -----------------------------
# 5. Quick summary in tons (common BOQ unit)
# -----------------------------
print(f"\nTotal weight in tons: {total_weight/1000:.3f} tons")
