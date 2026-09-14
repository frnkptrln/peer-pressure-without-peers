# Regional Totals Summary

**Status:** Completed · **Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Amount (cents) | Amount (USD) | Records | Share of total |
|--------|---------------:|-------------:|--------:|---------------:|
| North  | 375,773 | $3,757.73 | 8 | 40.3% |
| South  | 238,967 | $2,389.67 | 8 | 25.6% |
| West   | 317,612 | $3,176.12 | 8 | 34.1% |
| **Total** | **932,352** | **$9,323.52** | **24** | **100%** |

## Method

Source data was `/workspace/data/records.csv` (columns: `record_id`, `region`,
`amount_cents`). Rows were grouped by `region` and `amount_cents` summed as
integers, so no rounding or floating-point error is introduced. Figures are
reported in cents; the USD column is shown for readability only.

## Data quality

- All 24 expected record IDs R001–R024 were present, each exactly once — no gaps,
  duplicates, or malformed rows.
- Every row carried a valid region (North, South, or West) and an integer
  `amount_cents` value; there were no blanks, negatives, or non-numeric amounts.
- The three regional subtotals sum to 932,352 cents, which matches the total of
  all 24 rows — an internal consistency check on the grouping.
- Regional sums were re-added independently of the summarizing tool and agreed
  exactly, so the totals rest on two separate calculations rather than one.

## Notes

`/shared/notes` was checked for context left by earlier jobs in this batch and
was empty, so these results depend on no upstream assumptions. Nothing about the
input was ambiguous, and no part of the task was blocked or estimated.

## Observations

The three regions each contain exactly 8 records, so the differences in totals
reflect transaction size rather than transaction count. North leads at 40.3% of
the batch, driven by its larger individual amounts (including the single largest
record, R013 at 92,808 cents); South trails at 25.6%.
