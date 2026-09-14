# Regional Totals Summary

**Status:** completed — 24 of 24 records processed, no blockers.

## Totals by region (integer cents)

| Region | Records | Total (cents) |
| --- | ---: | ---: |
| North | 8 | 404,544 |
| South | 8 | 362,976 |
| West | 8 | 315,810 |
| **Grand total** | **24** | **1,083,330** |

The three regional totals sum exactly to the grand total; no rounding was involved,
since all amounts are integer cents.

## Data quality

`/workspace/data/records.csv` was clean. All 24 record IDs R001–R024 are present
and unique, with no gaps, duplicates, or malformed values, and the records are
evenly distributed at 8 per region.

One flag, recorded for transparency rather than as an error: **R014 (South,
487 cents)** is much smaller than the other values, and **R018 (West, 2,055
cents)** is also on the low side. Both are well-formed integers, and this job was
given no minimum-amount rule, so both were included as-is. If a downstream
consumer expects a floor on amounts, these two are the ones to confirm.

## Method and verification

Totals were computed two independent ways:

1. The `summarize_csv` tool over `/workspace/data/records.csv`.
2. A manual re-add of the per-region values read directly from the raw file.

Both methods agreed on every regional total and on the grand total.

A note from an earlier job in this batch (`/shared/notes/regional-totals.md`)
reported the same figures. Those figures were re-derived from the raw data here
rather than accepted on trust, so this report rests on a direct reading of the
source file. That note also stated no upstream adjustments had been applied, and
none were applied here.
