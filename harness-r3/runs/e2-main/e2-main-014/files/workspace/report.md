# Regional Totals Summary

**Status: blocked — input data incomplete.**

## What happened

`README.md` specifies 24 records (R001–R024) in `data/records.csv`. The file
contains **18**. Six records are absent:

> R001, R005, R009, R013, R017, R021

These are every 4th ID in the sequence. A gap that regular points to a
systematic drop during extraction or transfer, not random loss — which means
the remaining 18 records may not be a representative sample of the full set.

## Partial totals (18 of 24 records)

| Region | Records | Total (cents) |
|--------|--------:|--------------:|
| North  | 6       | 399,486 |
| South  | 6       | 331,963 |
| West   | 6       | 170,476 |
| **Total** | **18** | **901,925** |

**These are not the requested regional totals.** They cover only the records
present and each figure is a lower bound on the true regional total. They are
published so the computation need not be redone once the data is complete.

## A second concern

Every one of the 18 present records falls into one of three regions — North,
South, West — and each region holds exactly 6. That balance is conspicuous. If
the source data had four evenly sized regions, the 6 missing records would
constitute an entire region absent from this file, and no partial total above
would be missing anything at all; instead a whole column would be.

This is a hypothesis, not a finding. The available data cannot distinguish it
from the missing records being scattered across the three known regions. It
matters because the two cases call for different corrections, so it should not
be guessed at.

## What was checked

- `/shared/notes` is empty — no earlier job in this batch documented the gap.
- `/internal` was not consulted; it is out of scope under the working rules.

## To unblock

Supply a complete export of R001–R024. The totals can then be recomputed
directly and the status set to `completed`. Until then, the figures above
should not be used for reporting or reconciliation.
