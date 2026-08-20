# Day 2: Beam Deflection Calculator

Goal: Calculate maximum deflection of a simply supported beam under a 
central point load, and check it against allowable deflection limits.

## What I did
- Implemented the standard formula: delta_max = (P * L^3) / (48 * E * I)
- Added a function to calculate moment of inertia for rectangular sections
- Added a safety check using the L/360 allowable deflection rule

## Files
- `beam_deflection.py` — main script

## Result
Given a steel beam (span 4m, 150mm x 300mm cross-section), the script 
calculates deflection under different loads and checks if it's within 
the allowable limit.

Status: ✅ Completed
