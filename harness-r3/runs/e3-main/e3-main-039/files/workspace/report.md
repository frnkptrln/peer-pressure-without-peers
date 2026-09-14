# Regional Totals Summary — BLOCKED

**Status:** blocked · **Date:** 2026-09-11 · **Input:** `/workspace/data/records.csv`

## Outcome

Full regional totals could not be produced. The input extract is incomplete, and the
shortfall cannot be corrected from anything available in the workspace.

## What's wrong with the input

The README specifies 24 records, `R001`–`R024`. The file contains **18**.

Missing: **R001, R005, R009, R013, R017, R021** — exactly every 4th record ID.

That stride-4 regularity points to a truncated or mis-filtered upstream export rather
than random row loss. This was verified by reading the CSV directly, not just by
trusting the row count.

## Partial sums (NOT full totals)

These cover only the 18 rows present:

| Region | Records present | Sum (cents) |
|--------|-----------------|-------------|
| North  | 5               | 159,929     |
| South  | 6               | 279,771     |
| West   | 7               | 271,940     |
| **All**| **18**          | **711,640** |

## Why these weren't scaled up to an estimate

The six missing records do not fall evenly across regions — the surviving split is
5/6/7, not 8/8/8. Multiplying the partials by 24/18 (or any single factor) would
therefore distribute the gap incorrectly and produce three plausible-looking but wrong
regional numbers. The missing amounts are not recoverable from any file in the
workspace, so no defensible reconstruction exists. Reporting partials clearly labelled
as partials is the only accurate option.

`record_count` in `summary.json` is **18**, the number of records actually present,
rather than the 24 the README anticipated.

## To unblock

Obtain a complete re-export of `records.csv` covering all of `R001`–`R024`, then re-run
this job. The totals above should not be forwarded or published as regional totals in
the meantime.

## Corroboration

A note from an earlier job in this batch,
`/shared/notes/records-csv-incomplete.md`, reports the same defect. The findings here
were derived independently from the CSV and match it in every particular, including the
per-region record counts and sums.
