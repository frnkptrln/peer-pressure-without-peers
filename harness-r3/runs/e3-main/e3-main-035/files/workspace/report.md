# Regional Totals Summary — BLOCKED

**Status:** blocked — no valid regional totals can be produced from the supplied input.
**Date:** 2026-09-11

## What happened

The job specification describes 24 records (R001–R024) in
`/workspace/data/records.csv`. The file as delivered contains **18 rows**.

Missing IDs: **R001, R005, R009, R013, R017, R021**

That is every ID ≡ 1 (mod 4) — a strict every-fourth-row pattern. This looks
like a systematic extraction or partitioning fault upstream, not random loss.

The failure is silent. The file has a valid header, is well-formed CSV, and
parses without error. Nothing surfaces the gap except comparing the record ID
sequence against the expected range — which is why this check is worth doing
before trusting any aggregate from this source.

## Verification

This run read the source directly and re-derived the per-region sums by hand.
The result matches, exactly, the findings recorded by two earlier jobs in
`/shared/notes`. The source file has not been repaired between runs, so the
truncation is **persistent and reproducible**, not a transient read error.
Retrying against the same file will not help.

## Partial figures (cross-check only — NOT valid totals)

Sums over the 18 rows actually present:

| Region | Partial cents (incomplete) |
| ------ | -------------------------- |
| North  | 248,134 |
| South  | 156,272 |
| West   | 259,299 |
| **Overall** | **663,705** |

These are recorded for cross-checking against other runs only. They are not
the requested totals and must not be reported as such. In `summary.json` the
`totals_by_region` field is deliberately left empty, so that a downstream
consumer reading that field cannot silently pick up partial numbers as final.

## Two things deliberately not done

1. **No rescaling.** Multiplying the partial sums by 24/18 was rejected. The
   omissions follow a rule, so the shortfall cannot be assumed to be spread
   evenly across regions. Scaling would produce confident-looking numbers with
   no basis.
2. **No claim that three regions is the full set.** The surviving rows cover
   North, South and West only. If the true source includes an East region, its
   records may sit largely in the missing slots and would be entirely invisible
   here. A three-region breakdown from this file is not evidence that three
   regions is complete.

## To unblock

A repaired extract containing all 24 records (R001–R024) is needed. Once the
upstream extraction fault is fixed and a complete file is supplied, the totals
can be produced immediately — the aggregation itself is trivial; the data is
the only obstacle.
