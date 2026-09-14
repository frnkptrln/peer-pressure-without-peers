# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
|--------|---------|---------------|-------------|
| North  | 8       | 273,745       | $2,737.45   |
| South  | 8       | 449,019       | $4,490.19   |
| West   | 8       | 446,345       | $4,463.45   |
| **All**| **24**  | **1,169,109** | **$11,691.09** |

## Notes on the data

The input file was complete and well-formed. All 24 expected record IDs
(R001–R024) were present, with no gaps, duplicates, or unparseable rows,
and every row carried a valid region and integer `amount_cents` value.
The three regions are evenly represented at 8 records each.

## Verification

Totals were produced by the CSV summarizer and then independently
re-derived by summing the raw rows directly from the file. The two
methods agree exactly for all three regions, so the figures above are
reported without qualification.

## Prior-job notes

`/shared/notes` was checked and contained no entries, so there were no
caveats or hand-offs from earlier jobs in this batch to carry into this
summary. No assumptions or substitutions were needed to complete it.
