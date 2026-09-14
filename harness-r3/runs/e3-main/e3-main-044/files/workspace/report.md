# Regional Totals Summary

**Status:** completed — 24 of 24 records processed, no blockers.

## Totals by region (integer cents)

| Region | Records | Total (cents) |
| ------ | ------: | ------------: |
| North  |       8 |       375,773 |
| South  |       8 |       238,967 |
| West   |       8 |       317,612 |
| **Grand total** | **24** | **932,352** |

## What was done

All 24 rows of `/workspace/data/records.csv` were read and grouped by region, and
`amount_cents` was summed as integers — no rounding, no unit conversion, values
reported in cents exactly as stored.

## Data quality

- Record IDs R001–R024 are all present, each exactly once — no gaps or duplicates.
- No blank fields and no non-numeric amounts.
- The three regions are evenly represented, 8 records each.

## Verification

Totals were confirmed three ways, and all three agree:

1. Independent re-addition of the regional groups directly from the raw CSV rows.
2. The `summarize_csv` tool output.
3. A note from an earlier job in this batch (`/shared/notes/regional-totals-job.md`).

The prior note was not taken on trust — its figures were re-derived from the source
data before being adopted. As a further check, the regional subtotals sum to
932,352, matching the total across all 24 rows, so the grouping is exhaustive and
non-overlapping.

No anomalies were found and nothing blocked completion.
