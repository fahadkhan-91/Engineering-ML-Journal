# Day 31 (Week 5, Day 3): Stage-Discharge (Rating) Curve Visualization

Goal: Visualize how discharge (Q) varies with flow depth (stage) for 
channels of different widths, using Day 30's Manning's Equation — a 
fundamental chart type used in river gauging stations and flood 
warning systems.

## What I did
- Calculated discharge across a range of depths (0.1m to 2.5m) for 
  3 different channel widths
- Plotted rating curves for each width
- Marked a flood warning threshold and read off the corresponding 
  discharge for each channel width

## Files
- `stage_discharge_curve.py` — main script
- `stage_discharge_curve.png` — output chart

## Result
At the flood warning depth of 1.8m, a 1.5m-wide channel carries only 
6.08 m³/s while a 3.0m-wide channel carries 16.25 m³/s — nearly 3× 
more. This is the same principle used at real river gauging stations: 
once a rating curve is established, field staff can read discharge 
directly from a depth measurement without re-measuring velocity 
every time.

Status: ✅ Completed
