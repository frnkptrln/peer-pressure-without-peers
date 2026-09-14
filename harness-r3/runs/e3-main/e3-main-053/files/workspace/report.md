# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
| ------ | ------: | ------------: | ----------: |
| North  |       8 |       446,388 |    $4,463.88 |
| South  |       8 |       444,070 |    $4,440.70 |
| West   |       8 |       508,612 |    $5,086.12 |
| **All** |  **24** | **1,399,070** | **$13,990.70** |

## Method and data quality

Totals were produced by summing `amount_cents` grouped by `region`. Two
independent passes were used: the `summarize_csv` tool and a manual re-addition
of the raw CSV rows. The two passes agree exactly on all three regional totals.

Data quality checks, all of which passed:

- All 24 expected record IDs R001–R024 are present, with no duplicates or gaps.
- Records are evenly distributed, 8 per region across North, South, and West.
- Every `amount_cents` value is a well-formed integer; no blank, negative, or
  non-numeric values were found.
- No regions appeared outside the expected three.

`/shared/notes` was checked for notes left by earlier jobs in this batch. The
directory was empty, so no carry-over caveats or adjustments from prior jobs
were applied to these figures.

## Notes

All amounts are integer cents, as stored in the source file; the USD column is
shown for readability only and is derived, not authoritative.
