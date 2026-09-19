# Day 32 (Week 5, Day 4): Culvert/Pipe Sizing Selector (Automation)

Goal: Automate selection of the smallest standard circular culvert/pipe 
diameter that meets a required design discharge (with safety factor), 
using Manning's Equation for pipes flowing full — replacing manual 
trial-and-error across a table of standard sizes.

## What I did
- Implemented Manning's Equation for circular pipes flowing full
- Built a function that iterates through standard commercial diameters 
  (300mm–1800mm) to find the smallest adequate size
- Applied a 10% safety factor to required discharge before selection
- Batch-processed 5 culvert design points as would occur across a 
  real road/drainage project

## Files
- `culvert_sizing.py` — main script

## Result
Across 5 culvert locations with discharge requirements from 0.15 to 
3.5 m³/s, the tool automatically selected appropriate standard sizes 
(450mm to 1800mm) with utilization ratios between 62–87% — avoiding 
both under-sizing (flood risk) and unnecessary over-sizing (cost), 
without manual trial-and-error for each culvert.

Status: ✅ Completed
