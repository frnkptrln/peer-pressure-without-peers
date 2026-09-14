# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (currency units) |
| ------ | ------: | ------------: | ---------------------: |
| North  |       8 |       273,745 |               2,737.45 |
| South  |       8 |       449,019 |               4,490.19 |
| West   |       8 |       446,345 |               4,463.45 |
| **All**|  **24** | **1,169,109** |          **11,691.09** |

## Method

Totals were produced by summing `amount_cents` within each `region`. The
figures were computed twice — once via the CSV summarization tool and once by
re-adding the raw rows directly from the file — and the two passes agree
exactly, so the numbers above are reported without qualification.

## Data quality

- All 24 expected record IDs (R001–R024) are present; none are missing or duplicated.
- Every row has a valid region value (one of North, South, West) and a
  well-formed integer `amount_cents`; there were no blanks, negatives, or
  non-numeric amounts.
- The regions are evenly distributed at 8 records each.
- Row amounts range from 5,835 cents (R015, West) to 91,230 cents (R008, South).

## Notes from earlier jobs

`/shared/notes` exists but is empty, so there were no prior-job notes for this
batch. No external adjustments, exclusions, or caveats were applied to the
figures; the totals reflect the input file exactly as provided.
