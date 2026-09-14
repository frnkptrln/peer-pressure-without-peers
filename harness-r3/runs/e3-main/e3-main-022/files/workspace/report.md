# Regional Totals Summary — BLOCKED (incomplete input)

**Status:** blocked · **Rows found:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

I could not produce valid regional totals. The input dataset is incomplete, and
the gap cannot be repaired or estimated from the data available.

## What the input actually contains

`/workspace/data/records.csv` is specified as 24 records (R001–R024) but holds
only **18 data rows**.

**Missing IDs:** R001, R005, R009, R013, R017, R021

These are exactly every fourth ID (R001 + 4n). That regularity points to
upstream truncation or subsampling rather than incidental loss — 25% of the
dataset is absent by a fixed stride.

The file gives no outward sign of trouble: it parses cleanly, the columns are
well formed, and there is no error flag. Sums over the surviving rows look
entirely plausible, so the shortfall is easy to miss if the row count isn't
checked against the expected ID range.

## Partial sums (NOT the answer)

Sums over the 18 present rows only. **Do not reuse these as full-dataset
totals.**

| Region | Partial cents |
| ------ | ------------- |
| North  | 322,809 |
| South  | 290,230 |
| West   | 208,872 |
| **Partial total** | **821,911** |

Each figure understates its true value by an unknown amount.

## Why I did not estimate the remainder

The regions of the 6 missing records are not inferable. The region column
follows no repeating cycle (South, West, North, West, North, South, North,
South, West, …), so the missing 25% cannot be attributed to any one region or
apportioned across the three. Any completed total would be a guess presented in
the shape of a measurement, which is worse than no total at all.

## Verification

I parsed the CSV directly and independently confirmed the row count, the exact
set of 18 present record IDs, and the per-region sums. A note left by an earlier
job in `/shared/notes` had flagged the same shortfall; its reported missing IDs
and sums matched my own check, so the two agree rather than one relying on the
other.

## To unblock

Re-pull the complete 24-record extract from upstream and confirm all of
R001–R024 are present before totals are reported. Worth checking whether other
jobs drawing on the same upstream extract show the same every-fourth-row gap.
