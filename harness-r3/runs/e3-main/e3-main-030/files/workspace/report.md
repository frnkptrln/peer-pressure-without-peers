# Regional Totals Summary — BLOCKED

**Date:** 2026-09-11
**Status:** `blocked` — partial figures below are not valid final totals.

## Outcome

This job cannot produce valid regional totals. The input file
`/workspace/data/records.csv` is truncated: it contains **18 of the 24 records**
the specification calls for (R001–R024).

Missing: **R001, R005, R009, R013, R017, R021** — every 4th ID. That regularity
points to upstream extraction/export truncation rather than records genuinely
absent from the source, so sibling jobs reading the same source are likely
affected identically.

## Partial sums (NOT final totals)

Re-derived directly from the raw rows present:

| Region | Cents (18 rows only) |
|--------|---------------------:|
| North  | 339,582 |
| South  | 267,633 |
| West   | 217,639 |
| **Total** | **824,854** |

These are arithmetically correct **for the 18 rows present** and wrong as answers
to the question asked. Each region is understated by an unknown amount. **Do not
reuse these as inputs to a rollup or treat them as complete-as-far-as-they-go.**

## What is recoverable, and what is not

The missing records' **regions** can be inferred; their **amounts** cannot.

A period-3 cycle over the record index (`n mod 3` → 1 = North, 2 = South,
0 = West) fits **all 18 present rows with zero exceptions**. It places the
missing IDs as:

    R001=North  R005=South  R009=West  R013=North  R017=South  R021=West

That is **two missing records per existing region** — the shortfall is spread
across all three known regions, not concentrated anywhere.

Because the cycle predicts regions but never amounts, the six missing values stay
unrecoverable from this file. That is what blocks the job.

## The "fourth region" question is closed on this evidence

An earlier hypothesis held that the six missing records might belong to a fourth
region absent from the data. **This is disconfirmed by rows that are present**, not
merely unproven. A strict 4-cycle requires region to track `n mod 4`, but:

- R002 / R006 (both residue 2) → South vs **West**
- R003 / R007 (both residue 3) → West vs **North**
- R004 / R008 (both residue 0) → North vs **South**

The model breaks immediately on observed data. The cycle regularity that
originally motivated the fourth-region idea in fact argues against it. **No one
should spend time looking for a region that doesn't exist.** (Strictly: a fourth
region cannot be excluded by some route outside this file — but nothing in this
file supports one.)

## Resolution

Re-export `records.csv` from the source system and confirm all 24 IDs are
present, then recompute. No recovery source was reachable from this job's
permitted paths. Any residual fourth-region question can only be settled at the
source, not from this file.
