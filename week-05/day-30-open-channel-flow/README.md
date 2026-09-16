# Day 30 (Week 5, Day 2): Open Channel Flow Calculator (Manning's Equation)

Goal: Calculate flow capacity of open channels (rectangular and 
trapezoidal) using Manning's Equation — a standard hydraulic tool for 
sizing drains, canals, and culverts — and check adequacy against a 
design runoff requirement from Day 29.

## What I did
- Implemented Manning's Equation for both rectangular and trapezoidal 
  channel geometries
- Included reference Manning's roughness coefficients for common 
  channel linings (concrete, earth, rock)
- Built a design-check function that compares channel capacity 
  against a required design discharge (connecting to Day 29's runoff work)

## Files
- `channel_flow_calculator.py` — main script

## Result
A 2.0m × 1.2m concrete rectangular drain (slope 0.002) has a capacity 
of 5.51 m³/s — adequate for a 5.0 m³/s design flow. A larger 
trapezoidal earth canal (3m bottom width, 1.5m depth) can carry 
13.27 m³/s, showing how channel shape and lining material both 
significantly affect capacity.

Status: ✅ Completed
