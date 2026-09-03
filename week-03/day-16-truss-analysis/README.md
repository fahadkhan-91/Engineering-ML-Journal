# Day 16 (Week 3, Day 2): Truss Analysis Solver (Method of Joints)

Goal: Automate the classic structural engineering task of solving 
member forces in a statically determinate triangular truss, using 
the Method of Joints formulated as a linear algebra (matrix) problem.

## What I did
- Defined truss geometry (3 joints, 3 members) with pin + roller supports
- Set up equilibrium equations (ΣFx=0, ΣFy=0) at each joint
- Solved the resulting system of 6 equations using NumPy's linear 
  algebra solver
- Classified each member force as tension or compression

## Files
- `truss_solver.py` — main script

## Result
For a symmetric triangular truss with a 10 kN downward load at the 
apex: both diagonal members carry ~6.01 kN compression, and the 
bottom chord carries 3.33 kN tension — with support reactions splitting 
evenly (5 kN each), as expected for a symmetric geometry and loading.

Status: ✅ Completed
