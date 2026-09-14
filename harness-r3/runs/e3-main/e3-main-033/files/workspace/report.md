# Regional Totals Summary — BLOCKED

**Status:** blocked · **Rows read:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

The requested regional totals could **not** be produced. The input file
`/workspace/data/records.csv` is truncated, so any full-set aggregate derived
from it would be wrong.

## Finding

The spec calls for 24 records, `R001`–`R024`. The file contains **18 data
rows**. Missing:

> R001, R005, R009, R013, R017, R021

That is every ID ≡ 1 (mod 4) — a strict every-fourth-row pattern. This looks
like a systematic extraction or partitioning fault upstream, not random loss.

The failure is **silent**: the file is well-formed CSV with a valid header and
parses without error. Nothing surfaces the gap except comparing the ID sequence
against the expected range. A row-count check is the only defence.

## Partial sums (cross-check only — NOT full-set totals)

Recomputed by hand from the raw file:

| Region | Cents (18 rows only) |
|--------|---------------------|
| North  | 248,134 |
| South  | 156,272 |
| West   | 259,299 |
| **Total** | **663,705** |

These cover only the rows that survived. They are safe to use for reconciling
against other reads of the same file, and unsafe for anything else.

## What was deliberately not done

1. **No rescaling.** Multiplying the partial sums by 24/18 was rejected. The
   omissions follow a rule, so the shortfall cannot be assumed uniform across
   regions; scaling would yield confident-looking but unfounded numbers.
2. **No claim that three regions is complete.** The surviving rows cover only
   North, South and West. If the true source has an East region, its records
   could fall largely in the missing slots and would be invisible in the data
   as delivered.

## Reproducibility

Two earlier jobs in this batch independently reported this same defect
(`/shared/notes/records-csv-incomplete.md` and
`records-csv-incomplete-confirmation.md`), with identical missing IDs and
identical partial sums. This third independent read reproduces it exactly. The
truncation is therefore **persistent and reproducible**, not a transient read
error, and the source file has not been repaired between runs.

## Required to unblock

A complete `records.csv` covering `R001`–`R024` from upstream. Re-running
against the file in its current state will not change the result.
