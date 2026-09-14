# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) | Share |
|--------|---------|---------------|-------------|-------|
| North  | 8       | 404,544       | $4,045.44   | 37.3% |
| South  | 8       | 362,976       | $3,629.76   | 33.5% |
| West   | 8       | 315,810       | $3,158.10   | 29.2% |
| **All**| **24**  | **1,083,330** | **$10,833.30** | 100% |

## Method

Amounts were read as integer cents and summed per region. No rounding, currency
conversion, or unit changes were applied, so the regional figures add exactly to
the grand total.

Totals were produced with the `summarize_csv` tool and then independently
re-added by hand from the raw CSV. Both passes agreed on all three regions, so
the figures above are reported with confidence.

## Data quality

- All 24 expected record IDs R001–R024 were present, with no gaps or duplicates.
- Every row had a populated region and a valid integer `amount_cents` value.
- The three regions are evenly represented at 8 records each.
- The smallest value (R014, South, 487 cents) is far below the others but is a
  well-formed value, so it was included as-is rather than treated as an error.
  It is flagged here only so a reviewer can confirm it is genuine.

## Notes from earlier jobs

`/shared/notes` exists but is empty, so there were no upstream caveats or
adjustments to carry into this summary. Nothing in this job was blocked.
