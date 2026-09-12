# Day 25 (Week 4, Day 4): Batch Column Design Checker (Automation)

Goal: Automate checking multiple RC columns against their applied 
service loads in a single run, using Day 23's capacity formula, and 
generate a clear pass/fail summary — instead of checking each column 
manually one at a time.

## What I did
- Reused Day 23's column capacity formula as a reusable function
- Built a project column list with different sizes, reinforcement, 
  and applied loads
- Automated utilization ratio calculation and pass/fail status for 
  each column
- Generated a summary identifying which columns need redesign

## Files
- `batch_column_checker.py` — main script

## Result
Out of 5 sample columns, 4 passed and 1 (C4) failed with 100.4% 
utilization — flagging it for redesign. This kind of batch check 
saves significant time on real projects with dozens or hundreds of 
columns, compared to checking each one manually in a spreadsheet.

Status: ✅ Completed
