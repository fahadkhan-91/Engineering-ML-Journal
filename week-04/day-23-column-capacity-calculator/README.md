# Day 23 (Week 4, Day 2): RC Column Axial Capacity Calculator

Goal: Calculate the nominal and design axial load capacity of a tied 
reinforced concrete column using a simplified ACI 318 approach, and 
explore how bar count and concrete grade affect capacity.

## What I did
- Implemented the ACI tied-column capacity formula: 
  Pn = 0.80 × [0.85×f'c×(Ag−Ast) + fy×Ast], with φ=0.65
- Added a steel reinforcement ratio check (ACI limit: 1%–8%)
- Compared capacity across different bar counts (6 to 12 bars)
- Compared capacity across different concrete grades (20–40 MPa)

## Files
- `column_capacity.py` — main script

## Result
For a 400×400mm column with 8-T20 bars and 30 MPa concrete: design 
capacity Pu = 2741.7 kN, with steel ratio 1.57% (within ACI limits). 
Capacity scales roughly linearly with both bar count and concrete 
grade, as expected from the formula structure.

Status: ✅ Completed
