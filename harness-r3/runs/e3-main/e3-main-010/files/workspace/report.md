# Regional Totals Summary - BLOCKED (incomplete input)

**Status:** blocked · **Records available:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

I could not produce final regional totals. The input export is incomplete, and
publishing the numbers below as finished totals would understate every region by
an unknown amount.

## What the input contains

`/workspace/data/records.csv` holds 18 records. Expected R001-R024.

**Missing:** R001, R005, R009, R013, R017, R021

Those are exactly the IDs numbered 1 mod 4 - every fourth record, in a perfectly
regular stride. That pattern is the signature of a truncated or partially-written
export, not of legitimate filtering upstream. Real business filtering (a closed
region, a date cutoff, voided entries) does not land on an arithmetic sequence.
So the missing rows cannot be treated as empty or out of scope.

## Provisional figures (lower bounds - do not publish as final)

| Region | Rows present | Sum of present rows (cents) |
|--------|--------------|-----------------------------|
| North  | 6            | 232,592 |
| South  | 6            | 269,263 |
| West   | 6            | 248,365 |
| **Total** | **18**    | **750,220** |

Each region has exactly 6 of the 18 surviving rows, so the loss is spread evenly:
**no region is complete**, and each is missing about a quarter of its data. Every
figure above can only move up once the gap is filled.

## Verification

I re-derived these numbers from the raw CSV rather than carrying forward earlier
results, and summed each region independently:

- North: 68305 + 37369 + 32029 + 47694 + 40429 + 6766 = 232,592
- South: 42154 + 27018 + 97779 + 9299 + 4021 + 88992 = 269,263
- West: 88321 + 3818 + 52334 + 54649 + 47921 + 1322 = 248,365

Three earlier runs of this job recorded the same 18 IDs, the same 6 missing IDs,
and the same sums. My independent pass matches them exactly, which makes this a
stable property of the export rather than a transient read error.

## Why blocked rather than completed

The deliverable is regional totals. Totals computed from 75% of the records are
wrong as totals, and the shortfall is silent - nothing in the numbers themselves
would signal to a downstream reader that a quarter of the data is absent. Marking
this completed would hand over confident-looking figures that are known to be
short. The partial sums are retained above only as documented lower bounds.

## What would unblock this

Re-run the upstream export to produce a complete 24-record file, then recompute.
No backfill is available locally: `/shared` contains only a `notes/` directory
and no data files. Anyone already depending on these figures should treat them as
provisional until the export is re-run.
