# Day 11 (Week 2, Day 4): Concrete Quantity Estimator (Automation)

Goal: Automate calculation of total concrete volume for multiple 
structural elements (footings, columns, slabs) and break it down 
into cement, sand, aggregate, and water quantities based on a mix ratio.

## What I did
- Built a system to input multiple structural elements with dimensions 
  and quantities
- Auto-calculated total concrete volume across all elements
- Applied dry volume factor (1.54) and mix ratio (1:1.5:3) to get 
  material breakdown
- Converted cement volume into practical units (number of 50kg bags)

## Files
- `quantity_estimator.py` — main script

## Result
For a sample project (12 footings, 12 columns, 1 slab), the script 
calculated total concrete volume of 28.74 m³, requiring ~230 cement 
bags, ~12 m³ sand, ~24 m³ aggregate, and ~5748 liters of water — a 
task that would normally take manual calculation time on site.

Status: ✅ Completed
