# Day 34: Understanding Return Periods & Design Storms

## What Does "100-Year Storm" Actually Mean?

A common misconception: a "100-year storm" does NOT mean it happens 
once every 100 years like clockwork. It means a storm of that 
magnitude has a **1% probability of occurring in any given year** 
(1/100 = 1%). Two 100-year storms could occur in consecutive years — 
it's a probability, not a schedule.

### The math behind it

Annual Exceedance Probability (AEP) = 1 / Return Period

2-year storm -> AEP = 1/2 = 50% chance per year
10-year storm -> AEP = 1/10 = 10% chance per year
100-year storm -> AEP = 1/100 = 1% chance per year


## Why Different Return Periods Matter for Design

Not every structure needs the same level of protection — this is a 
cost vs. risk tradeoff:

- **Minor drains/culverts:** often designed for 2-10 year storms 
  (occasional flooding of a road is acceptable, not catastrophic)
- **Major drainage/detention basins:** typically 25-50 year storms
- **Dam spillways, critical infrastructure:** 100-year or even 
  1000-year storms (failure consequences are severe/life-threatening)

This is exactly why Day 33's analysis compared multiple return periods 
side-by-side — a real design decision requires knowing capacity 
requirements across several risk levels, not just one number.

## Connection to Probability Over a Structure's Lifetime

A subtlety worth knowing: over a structure's design life, the 
probability of experiencing at least one "100-year" event is higher 
than most people assume:

P(at least one event in N years) = 1 - (1 - 1/T)^N


For a 100-year storm (T=100) over a 30-year design life:

P = 1 - (1 - 0.01)^30 ≈ 26%


So a "100-year storm" actually has roughly a **1-in-4 chance** of 
occurring at least once during a typical 30-year building lifespan — 
much higher than the name suggests, and an important point when 
communicating risk to non-engineers (e.g. clients, the public).

## Key Takeaway

Return periods describe probability, not certainty or scheduling. 
Good engineering design isn't about eliminating flood risk entirely — 
it's about consciously choosing an acceptable probability of failure 
based on the consequences, and that choice should be understood, not 
just applied as a standard number from a table.

## Connects to
- [Day 29: Rainfall-Runoff Prediction](../week-05/day-29-rainfall-runoff)
- [Day 33: Rainfall-Runoff v2 - Return Period Analysis](../week-05/day-33-rainfall-runoff-v2)

Status: ✅ Completed
