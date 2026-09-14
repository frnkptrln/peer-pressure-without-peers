# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total |
|--------|---------|---------------|-------|
| North  | 8       | 446,388       | $4,463.88 |
| South  | 8       | 444,070       | $4,440.70 |
| West   | 8       | 508,612       | $5,086.12 |
| **All**| **24**  | **1,399,070** | **$13,990.70** |

## Notes on the data

- The input is complete and well-formed. Record IDs run consecutively from
  R001 to R024 with no gaps or duplicates, and every row carries a parseable
  integer `amount_cents` value.
- Three regions appear in the data — North, South and West — distributed
  evenly at 8 records each. There is no East region in this file, so it is
  omitted from the totals rather than reported as a zero.
- West is the largest region by value at roughly 36% of the grand total;
  North and South are close to each other at about 32% each.

## Method and verification

Totals were computed with the `summarize_csv` tool and then independently
re-added by hand from the raw CSV text. Both methods produced identical
figures for all three regions, so the numbers above are reported with
confidence.

`/shared/notes` was checked for guidance left by earlier jobs in this batch,
but the directory is empty. No external adjustments or corrections were
applied to the raw figures.
