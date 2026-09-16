"""
Day 30 (Week 5, Day 2): Open Channel Flow Calculator (Manning's Equation)
--------------------------------------------------
Goal: Calculate flow capacity of an open channel/drain (rectangular
or trapezoidal) using Manning's Equation - a standard hydraulic
engineering tool used to size drains, canals, and culverts.

Formula (Manning's Equation):
    V = (1/n) * R^(2/3) * S^(1/2)
    Q = V * A

Where:
    V = flow velocity (m/s)
    n = Manning's roughness coefficient
    R = hydraulic radius (m) = A / P
    S = channel bed slope (m/m)
    A = cross-sectional flow area (m2)
    P = wetted perimeter (m)
    Q = discharge/flow rate (m3/s)
"""

import math

# -----------------------------
# 1. Typical Manning's roughness coefficients (reference)
# -----------------------------
manning_n_values = {
    "concrete_lined": 0.013,
    "earth_channel_clean": 0.022,
    "earth_channel_weedy": 0.030,
    "rock_cut": 0.035,
}


def rectangular_channel_flow(width_m, depth_m, slope, n):
    """Calculate flow for a rectangular channel."""
    A = width_m * depth_m
    P = width_m + 2 * depth_m
    R = A / P
    V = (1 / n) * (R ** (2/3)) * (slope ** 0.5)
    Q = V * A
    return {"area_m2": round(A, 3), "wetted_perimeter_m": round(P, 3),
            "hydraulic_radius_m": round(R, 3), "velocity_mps": round(V, 3),
            "discharge_m3s": round(Q, 3)}


def trapezoidal_channel_flow(bottom_width_m, depth_m, side_slope_h_per_v, slope, n):
    """Calculate flow for a trapezoidal channel."""
    A = depth_m * (bottom_width_m + side_slope_h_per_v * depth_m)
    P = bottom_width_m + 2 * depth_m * math.sqrt(1 + side_slope_h_per_v ** 2)
    R = A / P
    V = (1 / n) * (R ** (2/3)) * (slope ** 0.5)
    Q = V * A
    return {"area_m2": round(A, 3), "wetted_perimeter_m": round(P, 3),
            "hydraulic_radius_m": round(R, 3), "velocity_mps": round(V, 3),
            "discharge_m3s": round(Q, 3)}


# -----------------------------
# 2. Example: Concrete-lined rectangular drain
# -----------------------------
print("=" * 55)
print("EXAMPLE 1: Rectangular Concrete Drain")
print("=" * 55)
result_rect = rectangular_channel_flow(
    width_m=2.0, depth_m=1.2, slope=0.002, n=manning_n_values["concrete_lined"]
)
for key, value in result_rect.items():
    print(f"{key}: {value}")

# -----------------------------
# 3. Example: Trapezoidal earth canal
# -----------------------------
print("\n" + "=" * 55)
print("EXAMPLE 2: Trapezoidal Earth Canal")
print("=" * 55)
result_trap = trapezoidal_channel_flow(
    bottom_width_m=3.0, depth_m=1.5, side_slope_h_per_v=1.5,
    slope=0.0015, n=manning_n_values["earth_channel_clean"]
)
for key, value in result_trap.items():
    print(f"{key}: {value}")

# -----------------------------
# 4. Connect to Day 29: check if channel can carry design runoff
# -----------------------------
print("\n" + "=" * 55)
print("DESIGN CHECK: Can this drain carry the Day 29 runoff volume?")
print("=" * 55)

design_runoff_m3s = 5.0  # example required design discharge

channel_capacity = result_rect["discharge_m3s"]
print(f"Required design discharge: {design_runoff_m3s} m3/s")
print(f"Rectangular drain capacity: {channel_capacity} m3/s")

if channel_capacity >= design_runoff_m3s:
    print("Status: ADEQUATE - drain can handle design flow")
else:
    print("Status: INADEQUATE - drain needs to be enlarged")
    print(f"Capacity shortfall: {design_runoff_m3s - channel_capacity:.3f} m3/s")
