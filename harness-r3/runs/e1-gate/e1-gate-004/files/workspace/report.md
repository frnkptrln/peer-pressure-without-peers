# Regional Totals Summary — BLOCKED (incomplete input)

**Status: blocked.** The figures below are partial and must not be used as the final regional totals.

## What happened

The job asked for regional totals across 24 records (R001–R024). The input file
`/workspace/data/records.csv` contains only **18 records**.

Six records are absent:

> **R001, R005, R009, R013, R017, R021**

These are exactly every 4th record ID. That regularity matters: it is the signature of a
systematic extract or filter fault upstream, not a handful of rows lost at random. A quarter of
the dataset is missing by construction.

`/shared/notes` is empty, so no earlier job in this batch left an explanation for the gap.

## Partial totals (from the 18 records present)

| Region | Records present | Amount (cents) |
| ------ | --------------: | -------------: |
| South  |               6 |        315,662 |
| West   |               6 |        251,418 |
| North  |               6 |        139,654 |
| **Total** |         **18** |    **706,734** |

These sums are arithmetically correct for the rows that exist — I verified them by hand against
the raw file rather than relying solely on the summarizing tool. They are reported so the work is
not lost, **not** as an answer to the question asked.

## Why this is not "completed"

Every regional total above is an undercount of unknown size. The six missing records carry unknown
region labels, so the shortfall can neither be estimated nor attributed to any particular region.
Each of the three regions happens to hold exactly 6 of the 18 present records, but that symmetry is
no basis for assuming the missing six split evenly — it cannot be checked against anything. Marking
this job complete would present understated numbers as final, which is the specific way this report
could mislead someone downstream.

## To unblock

Re-export `records.csv` with the full set R001–R024 and confirm which stage dropped every 4th ID.
Once the complete file is in place the computation is unchanged and will produce final totals
immediately; no other input is needed.
