# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) |
|--------|---------|---------------|
| North  | 8       | 375,773       |
| South  | 8       | 238,967       |
| West   | 8       | 317,612       |
| **Grand total** | **24** | **932,352** |

## Data quality

The input was complete and clean. All 24 expected record IDs were present exactly
once, with no gaps or duplicates. Every row carried a valid region label (North,
South, or West) and a non-blank, numeric `amount_cents` value. No rows were
dropped, imputed, or excluded.

## Method

Amounts were summed as integers in cents, so no rounding or floating-point error
enters the figures. Totals were read from the raw CSV and re-added by hand per
region as an independent check; the three regional subtotals reconcile exactly to
the all-rows grand total of 932,352 cents. The same figures are produced by the
`summarize_csv` tool and match a note left by an earlier job in this batch
(`/shared/notes/regional-totals-job.md`), giving three independent agreeing
sources. The distribution across regions is also even at 8 records each, which is
consistent with the input being a complete set.

## Blockers

None.
