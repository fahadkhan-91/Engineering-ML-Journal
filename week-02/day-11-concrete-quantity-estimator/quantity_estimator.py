"""
Day 11 (Week 2, Day 4): Concrete Quantity Estimator (Automation)
--------------------------------------------------
Goal: Automate the common site-engineering task of calculating total
concrete volume for structural elements (footings, columns, slabs),
and breaking it down into cement, sand, aggregate, and water quantities
based on a given mix ratio.
"""

# -----------------------------
# 1. Structural elements list
# Format: name, shape, dimensions (m), quantity
# -----------------------------
elements = [
    {"name": "Footing F1", "length": 1.5, "width": 1.5, "depth": 0.5, "quantity": 12},
    {"name": "Column C1", "length": 0.3, "width": 0.3, "depth": 3.0, "quantity": 12},
    {"name": "Slab S1", "length": 10, "width": 8, "depth": 0.15, "quantity": 1},
]

# -----------------------------
# 2. Mix ratio (by volume) - e.g. 1:1.5:3 (cement:sand:aggregate)
# -----------------------------
mix_ratio = {"cement": 1, "sand": 1.5, "aggregate": 3}
dry_volume_factor = 1.54  # accounts for voids/shrinkage in wet concrete
cement_bag_volume_m3 = 0.035  # volume of 1 bag (50kg) of cement in m3
water_cement_ratio = 0.5


def calculate_volume(element):
    """Calculate volume for one element (single unit)."""
    return element["length"] * element["width"] * element["depth"]


def calculate_material_quantities(total_volume_m3):
    """Break down total concrete volume into material quantities."""
    dry_volume = total_volume_m3 * dry_volume_factor
    total_ratio = sum(mix_ratio.values())

    cement_volume = (mix_ratio["cement"] / total_ratio) * dry_volume
    sand_volume = (mix_ratio["sand"] / total_ratio) * dry_volume
    aggregate_volume = (mix_ratio["aggregate"] / total_ratio) * dry_volume

    cement_bags = cement_volume / cement_bag_volume_m3
    cement_weight_kg = cement_bags * 50
    water_liters = cement_weight_kg * water_cement_ratio

    return {
        "cement_volume_m3": round(cement_volume, 3),
        "cement_bags": round(cement_bags, 1),
        "sand_volume_m3": round(sand_volume, 3),
        "aggregate_volume_m3": round(aggregate_volume, 3),
        "water_liters": round(water_liters, 1),
    }


# -----------------------------
# 3. Process all elements
# -----------------------------
total_volume = 0

print(f"{'Element':<15}{'Volume/unit (m3)':<18}{'Qty':<6}{'Total Volume (m3)':<20}")
print("-" * 60)

for el in elements:
    unit_vol = calculate_volume(el)
    total_el_volume = unit_vol * el["quantity"]
    total_volume += total_el_volume
    print(f"{el['name']:<15}{unit_vol:<18.3f}{el['quantity']:<6}{total_el_volume:<20.3f}")

print("-" * 60)
print(f"TOTAL CONCRETE VOLUME: {total_volume:.3f} m3\n")

# -----------------------------
# 4. Material breakdown
# -----------------------------
materials = calculate_material_quantities(total_volume)

print("Material Requirements (Mix Ratio 1:1.5:3):")
for key, value in materials.items():
    print(f"  {key}: {value}")
