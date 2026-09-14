# Regional Totals Summary — BLOCKED (incomplete input)

**Status: blocked.** The requested regional totals could not be produced, because the
source file is missing a quarter of the records the job depends on.

## What was expected vs. what arrived

The README specifies 24 records, `R001`–`R024`. `/workspace/data/records.csv` contains **18**.

Missing: **R001, R005, R009, R013, R017, R021**

These are not scattered. They are exactly every 4th record ID — a clean stride-4 pattern.
That signature points to a truncated or mis-filtered upstream extract, not random data loss
and not records that are legitimately absent. Until that is explained, the file should be
treated as a partial export rather than the full dataset.

## Partial sums (NOT the requested totals)

These are the exact sums of the 18 rows present in the file. They are arithmetically correct
for the data on hand, and they understate every region by an unknown amount.

| Region | Partial total (cents) | Records present |
|--------|----------------------:|----------------:|
| North  | 159,929 | 5 |
| South  | 279,771 | 6 |
| West   | 271,940 | 7 |
| **Total** | **711,640** | **18** |

## Why these were not scaled up

Multiplying the partials by 24/18 would yield numbers that look like a finished answer but
are invented. The amounts on the six missing records are not recoverable from anything in
this workspace, so no estimate was made.

It would also be wrong to assume each region is uniformly ~25% short. The records present
split **5 / 6 / 7** across North / South / West — already uneven. A stride-4 gap laid over a
repeating region cycle can land disproportionately on one region, so the per-region error is
likely unequal and unknown in direction of magnitude. Do not use these partials as a
proportional stand-in for the real totals.

## To unblock

Re-run the export for `R001`–`R024` and confirm all 24 IDs are present. Once the full file
is available the totals can be regenerated directly — the computation itself is trivial and
took no judgment; the incomplete input is the only obstacle.

## Notes

`/shared/notes` was checked for context from earlier jobs in this batch and was empty, so
there is no upstream explanation for the gap. A note describing the missing IDs has been
left there for the other jobs in this batch, since any job reading the same file is affected.
