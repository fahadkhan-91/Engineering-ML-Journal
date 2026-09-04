# Day 17 (Week 3, Day 3): Truss Force Diagram Visualization

Goal: Visualize the Day 16 truss analysis results as a labeled 
engineering diagram — showing tension/compression members with color 
coding and force magnitudes, instead of just raw numbers.

## What I did
- Plotted truss geometry using matplotlib
- Color-coded members: red = tension, blue = compression
- Varied line thickness based on force magnitude
- Added support symbols (pin, roller) and load arrow
- Labeled each member with its force value and T/C state

## Files
- `truss_diagram.py` — main script
- `truss_force_diagram.png` — output diagram

## Result
Produced a clear, textbook-style force diagram directly from Day 16's 
calculated values — makes the analysis results immediately readable 
without needing to look at raw numbers in a table.

Status: ✅ Completed
