# Day 24 (Week 4, Day 3): Column Capacity Trend Visualization

Goal: Turn Day 23's column capacity calculations into visual design 
charts showing how capacity varies with reinforcement bar count and 
concrete grade.

## What I did
- Reused Day 23's capacity formula across a range of bar counts and 
  concrete grades
- Created a 2-panel chart: capacity vs bar count (for 3 concrete 
  grades), and capacity vs concrete grade (for 3 bar counts)
- Calculated the % capacity gain from upgrading concrete grade

## Files
- `column_capacity_charts.py` — main script
- `column_capacity_charts.png` — output charts

## Result
Both relationships are clearly linear, as expected from the ACI 
formula structure. Upgrading concrete from 25 to 35 MPa (same 
reinforcement) increased capacity by 29.1% — a useful insight for 
comparing "add more steel" vs "use higher grade concrete" as design 
strategies.

Status: ✅ Completed
