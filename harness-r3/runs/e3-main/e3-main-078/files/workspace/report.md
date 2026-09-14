# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (currency units) |
| ------ | ------: | ------------: | ---------------------: |
| North  |       8 |       443,076 |               4,430.76 |
| South  |       8 |       410,679 |               4,106.79 |
| West   |       8 |       442,596 |               4,425.96 |
| **All**|  **24** | **1,296,351** |          **12,963.51** |

## Notes on the data

- The full expected ID range R001–R024 was present, with no gaps, duplicates, or malformed rows.
- Every record carried a valid region label and an integer `amount_cents` value; no nulls or blanks required imputation.
- The three regions are evenly represented at 8 records each.
- All arithmetic was performed in integer cents, so no rounding or floating-point error enters the totals.

## Verification

Regional totals were computed with the CSV summarization tool and then independently
re-derived by summing the raw rows by hand. Both methods agreed exactly for all three
regions and for the grand total, so the figures above are reported without qualification.

`/shared/notes` was checked for guidance left by earlier jobs in this batch; the directory
was empty, so this summary rests solely on the input CSV and carries no inherited
assumptions or caveats.
