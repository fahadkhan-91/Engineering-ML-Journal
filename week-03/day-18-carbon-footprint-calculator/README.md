# Day 18 (Week 3, Day 4): Concrete Carbon Footprint Calculator (Automation)

Goal: Automate embodied carbon (CO2e) calculation for a concrete 
project's material quantities, and evaluate a common sustainability 
strategy (fly ash cement replacement).

## What I did
- Applied typical embodied carbon factors for cement, sand, aggregate, 
  water, and steel
- Calculated total CO2e emissions and breakdown by material (using 
  quantities from Day 11's estimator as input)
- Modeled a 20% fly ash cement replacement scenario to estimate 
  potential carbon savings

## Files
- `carbon_calculator.py` — main script

## Result
For the sample project, cement alone contributed 73.1% of total 
embodied carbon (14.16 tons CO2e), confirming its outsized environmental 
impact compared to other materials. Replacing 20% of cement with fly 
ash reduced total emissions by ~14.3% — a realistic and commonly used 
sustainability strategy in real construction projects.

Status: ✅ Completed
