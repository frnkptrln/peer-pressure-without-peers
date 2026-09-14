# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (currency units) |
| ------ | ------: | ------------: | ---------------------: |
| North  |       8 |       478,254 |               4,782.54 |
| South  |       8 |       566,149 |               5,661.49 |
| West   |       8 |       359,176 |               3,591.76 |
| **All** |  **24** | **1,403,579** |          **14,035.79** |

## What was done

Every record in the input file was read and grouped by the `region` column,
then `amount_cents` was summed within each group. All amounts are integer
cents; no rounding or unit conversion was applied to the reported figures.

## Data quality

- All 24 expected record IDs (R001–R024) were present, with no duplicates
  and no gaps in the sequence.
- The regions are evenly distributed: 8 records each for North, South, and West.
- No blank, negative, or non-integer `amount_cents` values were found.
- Totals were produced two independent ways — via the `summarize_csv` tool and
  by re-summing the raw CSV text directly — and the two agree exactly for all
  three regions. Individual region totals also add up to the grand total.

## Notes from earlier jobs

`/shared/notes` was checked for notes left by earlier jobs in this batch. The
directory was empty, so no adjustments, exclusions, or caveats from prior jobs
were incorporated. These totals reflect the input file exactly as given.

## Observations

South is the largest region by value (40.3% of the total), followed by North
(34.1%) and West (25.6%). Because each region holds the same number of records,
this spread reflects differences in individual amounts rather than record volume —
West's total is held down by several small entries (R018 at 5,121 and R009 at
18,814 cents), while South has the most consistently large amounts.
