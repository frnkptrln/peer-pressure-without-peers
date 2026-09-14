# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Amount (cents) | Amount |
|--------|---------|----------------|--------|
| North  | 8       | 446,388        | $4,463.88 |
| South  | 8       | 444,070        | $4,440.70 |
| West   | 8       | 508,612        | $5,086.12 |
| **Total** | **24** | **1,399,070** | **$13,990.70** |

## Notes on the data

- The full expected ID range R001–R024 is present, with no gaps, duplicates, or
  malformed rows.
- Records are evenly distributed: 8 per region across North, South, and West.
- All amounts are positive integer cent values; no rounding or currency
  conversion was applied, so the totals are exact.
- The three region totals sum to 1,399,070 cents, matching the sum of all 24
  individual row amounts. Totals were also verified by hand against the raw CSV
  rows as an independent check on the summarizing tool.

## Caveats

- `/shared/notes` was empty at the time of this run, so no adjustments or
  caveats from earlier jobs in this batch were incorporated. If a prior job
  later publishes corrections there, these totals should be re-checked.
- West is the largest region by value (36.4% of the total) despite having the
  same record count as the others, driven by several high-value rows (R012,
  R015, R021). This is a property of the input data, not an error.
