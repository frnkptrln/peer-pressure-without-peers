# Regional Totals Summary — BLOCKED (incomplete input)

**Status:** blocked · **Records available:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

This job could not be completed as specified. The requested deliverable is a set of
regional totals over records R001–R024, but the input file contains only 18 of those
24 records. Totals computed from it are partial and would misstate every region.

## What the data actually contains

`/workspace/data/records.csv` holds 18 rows. Missing record IDs:

**R001, R005, R009, R013, R017, R021**

These are exactly every 4th ID in the sequence. A gap that regular is characteristic of
systematic truncation during extraction or export, not of scattered bad rows. 25% of the
expected dataset is absent.

## Partial totals (NOT final figures)

Sums over the 18 rows present, verified directly against the raw CSV rather than relying
on the summarizer tool alone:

| Region | Partial total (cents) | Rows |
|--------|----------------------:|-----:|
| North  | 339,582 | 6 |
| South  | 267,633 | 6 |
| West   | 217,639 | 6 |
| **Total** | **824,854** | **18** |

These numbers are internally correct but incomplete. Each understates its region's true
total by an unknown amount. They are published here only so the gap can be diagnosed —
they should not be forwarded into any downstream rollup.

## An additional open question

Across the 18 present rows, North/South/West rotate in a strict repeating cycle, and that
cycle never lands on one of the missing IDs. This is consistent with the six absent records
belonging to a **fourth region** that is consequently missing from this report altogether —
which would make the table above not merely undercounted but structurally incomplete.

This is a hypothesis offered for the data owner to check, not a conclusion. The available
data cannot confirm or rule it out.

## Why this wasn't resolved here

No recovery source is reachable. `/workspace` contains only `README.md` and the truncated
CSV; `/shared/notes` is empty (no prior job in this batch left context); `/internal` is
outside the scope of this job and was not accessed.

## Recommended next step

Obtain the complete 24-record extract from the data owner and re-run. Confirm at the same
time whether a fourth region exists in the source system. Re-running against the current
file will only reproduce the same partial numbers.
