# Regional Totals Summary — BLOCKED (incomplete input)

**Status:** blocked
**Records expected:** 24 (R001–R024, per README.md)
**Records found:** 18
**Date:** 2026-09-11

## Outcome

This job could not be completed as specified. The input file
`/workspace/data/records.csv` does not contain the dataset the job description
promises, so no trustworthy regional totals can be produced from it.

## What is wrong with the input

README.md states the input holds 24 records, `R001` through `R024`. The file
contains only 18 data rows. The following six record IDs are absent:

`R001`, `R005`, `R009`, `R013`, `R017`, `R021`

These are every fourth record in the sequence. Such a regular pattern points to
a systematic omission — a filtered view, a truncated export, or a dropped
partition — rather than random data loss. That matters: a systematic gap is
more likely to correlate with the values being measured, so the missing rows
cannot be assumed to resemble the rows that survived.

## Partial figures (do not use as final totals)

For transparency, these are the correct sums of the 18 rows that *are* present.
They are **partial** and should not be reported as regional totals.

| Region | Amount (cents) | Rows |
|--------|---------------:|-----:|
| North  |        350,404 |    6 |
| South  |        262,113 |    6 |
| West   |        139,310 |    6 |
| **Total (partial)** | **751,827** | **18** |

Two caveats on these numbers:

1. **Every regional total is understated by an unknown amount.** Six records
   with unknown regions and unknown amounts are missing; any of them could land
   in any region.
2. **A whole region may be missing.** Each region present has exactly six rows,
   an even split that accounts for all 18 surviving records. The six missing
   records could therefore constitute a fourth region absent from the file
   entirely. This is a possibility raised by the row counts, not a conclusion —
   the data available cannot confirm or rule it out.

## Other checks

- `/shared/notes` is empty; no earlier job in this batch left any note
  explaining or acknowledging the discrepancy.
- No other copy of the dataset was available within the permitted scope, so the
  missing records could not be recovered or cross-checked.
- The 18 rows present are internally well-formed: IDs are unique, regions are
  consistently spelled, and all amounts parse as integer cents.

## What is needed to finish

Supply the complete 24-record export as `/workspace/data/records.csv`. Once the
full dataset is in place the totals can be recomputed directly and the status
moved to `completed`. It is also worth tracing why the export dropped every
fourth record, since the same fault may affect other jobs drawing on this
source.

A concern has been filed for human review.
