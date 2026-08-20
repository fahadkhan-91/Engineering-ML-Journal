"""
Day 2: Simply Supported Beam Deflection Calculator
--------------------------------------------------
Goal: Calculate maximum deflection of a simply supported beam under a
central point load, using basic structural engineering formulas.

Formula used (point load at center of simply supported beam):
    delta_max = (P * L^3) / (48 * E * I)

Where:
    P = point load (N)
    L = span length (m)
    E = modulus of elasticity (Pa)
    I = moment of inertia (m^4)
"""

def calculate_deflection(P, L, E, I):
    """
    Calculate max deflection for a simply supported beam
    with a central point load.
    """
    delta_max = (P * L**3) / (48 * E * I)
    return delta_max


def rectangular_moment_of_inertia(b, h):
    """
    Moment of inertia for a rectangular cross-section.
    b = width (m), h = height (m)
    """
    return (b * h**3) / 12


# -----------------------------
# Example: Steel beam
# -----------------------------
P = 5000        # Point load in Newtons (~500 kg)
L = 4           # Span length in meters
E = 200e9       # Modulus of elasticity for steel (Pa)
b = 0.15        # Beam width in meters
h = 0.30        # Beam height in meters

I = rectangular_moment_of_inertia(b, h)
deflection = calculate_deflection(P, L, E, I)

print(f"Moment of Inertia (I): {I:.6e} m^4")
print(f"Maximum Deflection: {deflection*1000:.3f} mm")

# -----------------------------
# Try a different load to compare
# -----------------------------
P2 = 8000
deflection2 = calculate_deflection(P2, L, E, I)
print(f"\nWith increased load ({P2} N):")
print(f"Maximum Deflection: {deflection2*1000:.3f} mm")

# Allowable deflection check (common rule: L/360)
allowable = L / 360
print(f"\nAllowable deflection (L/360 rule): {allowable*1000:.2f} mm")
if deflection2 <= allowable:
    print("Status: SAFE")
else:
    print("Status: EXCEEDS allowable limit")
