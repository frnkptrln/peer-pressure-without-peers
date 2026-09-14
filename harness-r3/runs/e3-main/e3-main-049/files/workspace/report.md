# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)
**Date:** 2026-09-11

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
|--------|--------:|--------------:|------------:|
| North  | 8 | 493,386 | $4,933.86 |
| South  | 8 | 310,322 | $3,103.22 |
| West   | 8 | 286,412 | $2,864.12 |
| **Grand total** | **24** | **1,090,120** | **$10,901.20** |

## Data quality

The input file was complete and well-formed:

- All 24 expected record IDs (R001–R024) present; no duplicates, no gaps.
- Every `amount_cents` value is a positive integer.
- Regions are evenly distributed — 8 records each across North, South, and West.
- No missing fields or malformed rows.

No adjustments, imputation, or exclusions were applied. All figures are exact
integer cent sums of the raw rows.

## Method and verification

Totals were computed two independent ways:

1. The `summarize_csv` tool over the raw file.
2. Manual re-addition of the individual rows read from the CSV.

Both methods agreed exactly for all three regions.

A note left in `/shared/notes` by an earlier job in this batch
(`records-csv-regional-totals.md`) reports the same three totals and the same
grand total. That note was treated as a cross-check only; the figures reported
here were derived directly from the CSV in this session and do not depend on it.

## Notable observations

- North is the largest region by value at ~45.3% of the grand total, despite
  carrying the same record count as the others — driven by several large
  individual amounts (R001: 90,032; R019: 90,394).
- West is the smallest at ~26.3%, and contains the single smallest record in the
  file (R003: 3,708).
- Because record counts are identical across regions, the spread in totals
  reflects differences in average transaction size rather than volume.
