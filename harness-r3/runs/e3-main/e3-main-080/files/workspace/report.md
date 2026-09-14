# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
|--------|--------:|--------------:|------------:|
| North  | 8 | 443,076 | $4,430.76 |
| South  | 8 | 410,679 | $4,106.79 |
| West   | 8 | 442,596 | $4,425.96 |
| **All** | **24** | **1,296,351** | **$12,963.51** |

## Notes on the data

- Every expected record ID from R001 through R024 was present exactly once. No
  gaps, duplicates, or malformed rows were found.
- The three regions are evenly represented, with 8 records each.
- All amounts were treated as integer cents and summed without any rounding or
  unit conversion, so the totals above are exact.
- Region totals were re-added by hand directly from the raw CSV rows as a check
  against the CSV summarizer tool; both agree on all three figures.
- North and West are close to each other (a difference of 480 cents), with South
  trailing both by roughly 32,000 cents.

## Caveats

None. `/shared/notes` contained no notes from earlier jobs in this batch, so
there were no upstream caveats or corrections to carry forward into this
summary. The figures reflect the input file exactly as supplied.
