# Regional Totals Summary - BLOCKED (incomplete input)

**Status:** blocked
**Date:** 2026-09-11
**Input:** `/workspace/data/records.csv`

## Outcome

No valid regional totals were produced. The input extract is missing 25% of its records, and the shortfall cannot be reconstructed from the data available.

## What is wrong with the input

The job spec describes 24 records, `R001`-`R024`. The delivered file contains **18 rows**.

| | |
|---|---|
| Expected records | 24 (R001-R024) |
| Records present | 18 |
| Records missing | 6 |
| Missing IDs | R001, R005, R009, R013, R017, R021 |

The missing IDs fall on a **regular stride - every fourth record, starting at R001**. That pattern points to a systematic upstream extraction fault (a dropped shard, or a chunked-export off-by-one) rather than incidental or random loss.

Worth flagging: the file is well-formed CSV, correctly typed, and internally consistent. Nothing in it is malformed, so **the gap does not announce itself**. It surfaces only when the row count and ID sequence are checked against the spec. Any downstream job consuming the same extract should run that check before trusting the contents.

## Why this could not be completed anyway

The 6 absent rows carry **both unknown regions and unknown amounts**. Because the region assignment of a missing record is itself unknown, the shortfall cannot be attributed to any region, and there is no sound basis for estimating or interpolating it from the 18 rows present. No permitted substitute source for the missing records was available (`/internal` is outside this job's scope).

Reporting the 18-row sums as if they were the answer would silently understate **every** region by an unknown amount, while looking entirely plausible. That is the specific failure mode worth avoiding here, so `totals_by_region` in `summary.json` is deliberately left empty rather than partially filled.

## Partial sums (cross-check only - NOT results)

Recorded for diagnostics and reconciliation against a future re-issued file. **These are not valid regional totals.**

| Region | Partial sum (cents) | Rows |
|---|---|---|
| South | 317,220 | 6 |
| West | 220,854 | 6 |
| North | 176,153 | 6 |
| **Grand total** | **714,227** | **18** |

## Verification

The figures above were derived by an independent pass over the CSV in this session. That pass reproduced the same row count (18), the same set of missing IDs, and the same per-region partial sums previously recorded by an earlier job in this batch - so the finding is corroborated, not taken on assertion.

## What would unblock this

A **re-issued complete `records.csv` covering R001-R024**. No other change is required; the job runs to completion once the full extract is supplied. The partial sums above can be used to confirm the re-issued file is a superset of the current one.
