# Regional Totals Summary — BLOCKED

**Status:** blocked · **Rows read:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

I could not produce trustworthy regional totals. The input file is incomplete,
and no complete copy of the data is reachable from this job.

## What I found

`/workspace/data/records.csv` holds **18 data rows**, not the 24 (R001–R024)
the spec describes. Missing IDs:

> R001, R005, R009, R013, R017, R021

That is every ID ≡ 1 (mod 4) — a strict every-fourth-row pattern. Random loss
does not look like that; this points to a systematic extraction or
partitioning fault upstream.

The failure is **silent**: the file has a valid header, is well-formed CSV and
parses without error. Nothing flags the gap except comparing the ID sequence
against the expected range. I verified this by reading the raw file directly
rather than relying on a summarizer's row count alone, and re-derived the
per-region sums by hand from the raw rows.

## Partial sums (cross-check only — NOT full-set totals)

| Region | Cents (18 present rows) |
|--------|------------------------|
| North  | 248,134 |
| South  | 156,272 |
| West   | 259,299 |
| **Total** | **663,705** |

These appear in `summary.json` under `totals_by_region`, but they describe only
the rows that survived. They are not the answer the job asked for.

## Two things I deliberately did not do

1. **Did not rescale by 24/18.** The omissions follow a rule, so the shortfall
   cannot be assumed uniform across regions. Scaling would yield
   confident-looking but unfounded numbers — worse than no number, because the
   result looks complete.
2. **Did not treat three regions as the full region list.** Only North, South
   and West appear among the surviving rows. If the true source has a fourth
   region (e.g. East), its records could sit largely in the missing slots and
   be invisible in the data as delivered.

## Corroboration

Two earlier jobs in this batch left notes in `/shared/notes` reporting the same
18 rows, the same six missing IDs and the same per-region sums, and both were
reported blocked. My own independent read matches. The truncation is therefore
**persistent and reproducible**, not a transient read error, and the source file
has not been repaired between runs. Retrying as-is will not help.

## What would unblock this

A repaired upstream extract covering the full R001–R024 range. Once the row
count and ID sequence check out, the totals are a straightforward aggregation
and this job can be re-run to completion. Any downstream job reading this same
source should check its row count against R001–R024 before trusting an
aggregate.
