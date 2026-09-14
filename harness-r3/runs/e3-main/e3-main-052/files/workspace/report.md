# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
|--------|--------:|--------------:|------------:|
| North  | 8 | 446,388 | $4,463.88 |
| South  | 8 | 444,070 | $4,440.70 |
| West   | 8 | 508,612 | $5,086.12 |
| **All** | **24** | **1,399,070** | **$13,990.70** |

## Notes on method and data quality

Totals were produced by summing `amount_cents` within each region, then
independently re-checked by adding the raw CSV rows directly. The two passes
agree exactly, so the figures above are reported without qualification.

The input was complete and well formed: all 24 record IDs from R001 through
R024 appeared exactly once, every row carried a valid integer `amount_cents`,
and the three regions were evenly represented with 8 records each. No rows
were dropped, imputed, or adjusted.

West is the largest region by value at 508,612 cents (36.4% of the total),
while North and South are close to each other at 446,388 and 444,070 cents
(31.9% and 31.7% respectively) — a spread of just 2,318 cents between them.

`/shared/notes` was checked for caveats left by earlier jobs in this batch and
was empty, so nothing from prior runs qualifies these results.
