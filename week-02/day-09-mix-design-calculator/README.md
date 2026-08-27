# Day 9 (Week 2, Day 2): ACI Concrete Mix Design Calculator (Simplified)

Goal: Automate a simplified version of the ACI 211.1 mix design method 
to estimate water-cement ratio, water content, and cement content for 
a given target compressive strength.

## What I did
- Built lookup tables approximating ACI 211.1 strength vs w/c ratio 
  and water content vs max aggregate size relationships
- Created a function that outputs full mix design proportions
- Compared proportions across different target strengths (20-40 MPa)

## Files
- `mix_design_calculator.py` — main script

## Result
Confirmed expected trend: as target strength increases, w/c ratio 
decreases and cement content increases. For 30 MPa target: w/c=0.55, 
cement ≈ 345.5 kg/m³, water = 190 kg/m³.

Note: This is a simplified/educational version. Real ACI mix design 
also accounts for aggregate fineness modulus, admixtures, air content, 
and requires lab trial batches for verification.

Status: ✅ Completed
