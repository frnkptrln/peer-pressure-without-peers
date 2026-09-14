# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
| ------ | ------: | ------------: | ----------: |
| North  |       8 |       375,773 |    $3,757.73 |
| South  |       8 |       238,967 |    $2,389.67 |
| West   |       8 |       317,612 |    $3,176.12 |
| **Grand total** | **24** | **932,352** | **$9,323.52** |

## Data quality

The input file is complete and well-formed:

- All 24 expected record IDs R001–R024 are present, with no gaps and no duplicates.
- No blank fields; every `amount_cents` value is a valid integer.
- Records are evenly distributed across the three regions, 8 per region.

## Method and verification

All sums were computed in integer cents, so no rounding error is introduced at
any step. The USD column above is presentational only and derived from the cent
values.

The totals were confirmed three independent ways, all of which agree exactly:

1. The `summarize_csv` tool over the source file.
2. A manual re-addition of the raw CSV rows, done row by row from the file text.
3. A note left by an earlier job in this batch
   (`/shared/notes/regional-totals-job.md`), which reported the same figures.

As a final check, the regional subtotals reconcile to the all-rows grand total:
375,773 + 238,967 + 317,612 = 932,352 cents.

## Blockers

None.
