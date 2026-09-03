"""
Day 16 (Week 3, Day 2): Truss Analysis Solver (Method of Joints)
--------------------------------------------------
Goal: Automate the classic structural engineering task of solving
member forces in a statically determinate truss, using the Method
of Joints (via matrix/linear algebra approach).

Example structure: Simple triangular truss with 3 joints, 3 members,
one point load applied, supported by a pin and a roller.
"""

import numpy as np

# -----------------------------
# 1. Define truss geometry
# Joints: A (pin support), B (roller support), C (load applied)
# -----------------------------
joints = {
    "A": (0, 0),
    "B": (4, 0),
    "C": (2, 3),
}

members = [
    ("A", "B"),  # bottom chord
    ("A", "C"),  # left diagonal
    ("B", "C"),  # right diagonal
]

# -----------------------------
# 2. Applied load at joint C
# -----------------------------
load_C = (0, -10)  # 10 kN downward force at joint C

# -----------------------------
# 3. Support reactions
# A = pin (2 reactions: Ax, Ay), B = roller (1 reaction: By)
# -----------------------------

def member_length(j1, j2):
    x1, y1 = joints[j1]
    x2, y2 = joints[j2]
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def unit_vector(j1, j2):
    """Unit vector pointing FROM j1 TO j2."""
    x1, y1 = joints[j1]
    x2, y2 = joints[j2]
    L = member_length(j1, j2)
    return ((x2 - x1) / L, (y2 - y1) / L)


# -----------------------------
# 4. Set up equilibrium equations for each joint (Method of Joints)
# Unknowns: F_AB, F_AC, F_BC (member forces), Ax, Ay, By (reactions)
# -----------------------------
unknowns = ["F_AB", "F_AC", "F_BC", "Ax", "Ay", "By"]
n = len(unknowns)

A_matrix = np.zeros((n, n))
b_vector = np.zeros(n)

# Joint A: sum Fx = 0, sum Fy = 0
ux_AB, uy_AB = unit_vector("A", "B")
ux_AC, uy_AC = unit_vector("A", "C")

A_matrix[0] = [ux_AB, ux_AC, 0, 1, 0, 0]   # Fx at A
b_vector[0] = 0
A_matrix[1] = [uy_AB, uy_AC, 0, 0, 1, 0]   # Fy at A
b_vector[1] = 0

# Joint B: sum Fx = 0, sum Fy = 0
ux_BA, uy_BA = unit_vector("B", "A")
ux_BC, uy_BC = unit_vector("B", "C")

A_matrix[2] = [ux_BA, 0, ux_BC, 0, 0, 0]   # Fx at B
b_vector[2] = 0
A_matrix[3] = [uy_BA, 0, uy_BC, 0, 0, 1]   # Fy at B
b_vector[3] = 0

# Joint C: sum Fx = 0, sum Fy = 0 (external load applied here)
ux_CA, uy_CA = unit_vector("C", "A")
ux_CB, uy_CB = unit_vector("C", "B")

A_matrix[4] = [0, ux_CA, ux_CB, 0, 0, 0]   # Fx at C
b_vector[4] = -load_C[0]
A_matrix[5] = [0, uy_CA, uy_CB, 0, 0, 0]   # Fy at C
b_vector[5] = -load_C[1]

# -----------------------------
# 5. Solve the system
# -----------------------------
solution = np.linalg.solve(A_matrix, b_vector)

print("=" * 45)
print("TRUSS ANALYSIS RESULTS (Method of Joints)")
print("=" * 45)
for name, value in zip(unknowns, solution):
    label = "Member Force" if name.startswith("F_") else "Reaction"
    nature = ""
    if name.startswith("F_"):
        nature = "(Tension)" if value > 0 else "(Compression)"
    print(f"{name:<8} = {value:>8.2f} kN   {label} {nature}")

print("\nNote: Positive member force = Tension, Negative = Compression")
