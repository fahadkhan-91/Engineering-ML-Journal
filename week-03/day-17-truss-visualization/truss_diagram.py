"""
Day 17 (Week 3, Day 3): Truss Force Diagram Visualization
--------------------------------------------------
Goal: Visualize the truss from Day 16 with members color-coded by
tension/compression, and force magnitudes labeled - turning raw
numbers into an intuitive engineering diagram.
"""

import matplotlib.pyplot as plt

# -----------------------------
# 1. Truss geometry (same as Day 16)
# -----------------------------
joints = {
    "A": (0, 0),
    "B": (4, 0),
    "C": (2, 3),
}

# Member forces from Day 16 results (kN)
member_forces = {
    ("A", "B"): 3.33,    # Tension
    ("A", "C"): -6.01,   # Compression
    ("B", "C"): -6.01,   # Compression
}

load_joint = "C"
load_magnitude = 10  # kN

# -----------------------------
# 2. Plot the truss
# -----------------------------
fig, ax = plt.subplots(figsize=(8, 7))

# Draw members
for (j1, j2), force in member_forces.items():
    x1, y1 = joints[j1]
    x2, y2 = joints[j2]

    color = "red" if force > 0 else "blue"  # red = tension, blue = compression
    linewidth = 2 + abs(force) * 0.5

    ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth, zorder=1)

    # Label force at midpoint
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    label = f"{abs(force):.2f} kN\n{'T' if force > 0 else 'C'}"
    ax.text(mid_x, mid_y + 0.15, label, fontsize=10, ha='center',
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray"))

# Draw joints
for name, (x, y) in joints.items():
    ax.plot(x, y, 'ko', markersize=10, zorder=2)
    ax.text(x - 0.15, y - 0.35, name, fontsize=13, fontweight='bold')

# Draw supports (simplified symbols)
ax.plot(joints["A"][0], joints["A"][1], '^', markersize=20, color='green', zorder=0)
ax.text(joints["A"][0] - 0.3, joints["A"][1] - 0.6, "Pin Support", fontsize=9, color='green')

ax.plot(joints["B"][0], joints["B"][1], 'o', markersize=18, color='purple', zorder=0)
ax.text(joints["B"][0] - 0.4, joints["B"][1] - 0.6, "Roller Support", fontsize=9, color='purple')

# Draw applied load arrow
load_x, load_y = joints[load_joint]
ax.annotate('', xy=(load_x, load_y - 1), xytext=(load_x, load_y),
            arrowprops=dict(facecolor='black', shrink=0, width=3, headwidth=12))
ax.text(load_x + 0.15, load_y - 0.5, f"{load_magnitude} kN", fontsize=11, fontweight='bold')

# Legend
ax.plot([], [], color='red', linewidth=3, label='Tension')
ax.plot([], [], color='blue', linewidth=3, label='Compression')
ax.legend(loc='upper right', fontsize=11)

ax.set_xlim(-1, 5)
ax.set_ylim(-1.5, 4)
ax.set_aspect('equal')
ax.set_title('Truss Force Diagram (Method of Joints Result)', fontsize=13, fontweight='bold')
ax.axis('off')

plt.tight_layout()
plt.savefig('truss_force_diagram.png', dpi=150)
plt.show()

print("Truss force diagram saved as truss_force_diagram.png")
print("\nSummary:")
for (j1, j2), force in member_forces.items():
    state = "Tension" if force > 0 else "Compression"
    print(f"  Member {j1}-{j2}: {abs(force):.2f} kN ({state})")
