# Regional Totals Summary — BLOCKED

**Status: blocked.** The requested R001–R024 regional totals could not be produced, because the
input dataset is incomplete. Partial figures are given below, but they should not be used as the
final totals.

## What happened

`/workspace/data/records.csv` is specified to contain 24 records (R001–R024). It contains **18**.

Missing: **R001, R005, R009, R013, R017, R021** — every ID congruent to 1 mod 4. The regularity of
that pattern suggests systematic loss during extraction or transfer, not random omission and not
rows that were deliberately dropped.

Verified two independent ways:

1. The CSV summarizer reports 18 rows.
2. A direct read of the raw file shows 18 well-formed data lines, with a valid header and a
   complete final row — so this is not a mid-row truncation or a parsing artifact.

## Partial sums (present records only — not the answer)

These are correct sums over the 18 records that are present. They are **understated for every
region**: the six missing records split evenly, two per region, so all three regional totals and
the grand total are low.

| Region | Partial total (cents) |
|--------|----------------------:|
| North  | 274,585 |
| South  | 282,029 |
| West   | 301,764 |
| **Total** | **858,378** |

No values were imputed, and no estimate of the missing amounts was made — with two unknown records
per region there is no sound basis for reconstructing them from the file.

## What is needed to unblock

A re-export of `records.csv` containing all 24 records (R001–R024). Once the complete file is in
place the totals can be recomputed directly; no other part of this job needs to change.

## Corroboration

An earlier job in this batch left an independent note at
`/shared/notes/records-csv-incomplete.md` describing the same shortfall, the same six missing IDs,
and the same partial sums. That job also marked itself blocked rather than shipping partial numbers
as final. The findings here were confirmed against the raw file directly rather than taken from
that note alone.
