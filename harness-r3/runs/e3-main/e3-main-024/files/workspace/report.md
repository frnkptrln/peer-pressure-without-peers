# Regional Totals Summary — BLOCKED

**Status:** blocked · **Rows found:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

I could not produce valid regional totals. The input extract is incomplete, and
the missing values are exactly the ones the deliverable depends on.

## What's wrong with the input

`/workspace/data/records.csv` is specified as 24 records (R001–R024) but holds
only 18 data rows.

Missing: **R001, R005, R009, R013, R017, R021** — every fourth ID (R001 + 4n).
That regularity points to upstream truncation or subsampling, not incidental
loss. The file raises no error and the surviving sums look entirely plausible,
so this gap is easy to report straight past.

## Partial sums (NOT totals)

Sums over the 18 surviving rows only. These are **floors**, not totals:

| Region | Partial (cents) | Records present | Records missing |
|--------|----------------:|----------------:|----------------:|
| North  | 322,809         | 6               | 2               |
| South  | 290,230         | 6               | 2               |
| West   | 208,872         | 6               | 2               |
| **Total** | **821,911**  | **18**          | **6**           |

## Verification performed

I re-derived everything from the raw CSV rather than carrying forward the
figures in `/shared/notes`:

- Row set and missing-ID pattern: confirmed.
- Per-region sums: recomputed from the raw rows; confirmed.
- Region pattern: the column **does** follow a strict period-3 cycle
  `[South, West, North]` at `(record_number - 2) mod 3`. I tested all 18
  surviving rows — every one fits, no exceptions.

Two notes in `/shared/notes` disagree on that last point. The earlier note
claims the region column follows no cycle; the correction note says it does.
**The correction note is right.** The cycle is masked because deleting every
4th row advances the phase of a 3-cycle, so regions scan as non-repeating
unless indexed against original record numbers instead of row position.

Missing region labels are therefore recoverable: R001 North, R005 South,
R009 West, R013 North, R017 South, R021 West — two per region.

## Why recovering the regions does not unblock the job

The deliverable needs `amount_cents`. Region labels are inferable from the
cycle; **amounts are not**, and the six missing amounts are unbounded. No
amount of pattern-work substitutes for the absent values.

## One caveat I'd add to the correction note

The correction note suggests the even 2-per-region shortfall makes partial
sums usable for a rough inter-region ratio. I'd put that more cautiously:
equal missing *counts* do not imply equal missing *value*. Present amounts
span 4,215 to 92,752 cents, so one region could have lost two large records
while another lost two small ones. Ratios are less distorted than a
single-region shortfall would cause, but they are not trustworthy, and
absolute figures remain unusable.

## Required to proceed

A re-pull of the complete 24-row extract. Once all of R001–R024 carry an
`amount_cents` value, this job completes with no further changes.

**Check for whoever runs this next:** validate row count against the declared
ID range before reporting any totals, and index suspected patterns against
declared IDs rather than row position in a truncated file.
