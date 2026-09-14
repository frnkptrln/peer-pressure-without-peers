# Regional Totals Summary - BLOCKED (incomplete input)

**Status: blocked.** The requested R001-R024 regional totals could not be produced. The
numbers below are partial and must not be used as final figures.

## What happened

`/workspace/data/records.csv` was expected to hold 24 records (R001-R024). It holds **18**.

Missing: **R001, R005, R009, R013, R017, R021** - every fourth record, each ID congruent to
1 mod 4. That regularity suggests systematic loss during extraction or transfer rather than
random omission or deliberately dropped rows.

Verified two independent ways:

1. The CSV summarizer reports 18 rows.
2. A direct read of the raw file shows 18 well-formed data lines, ending in a clean final
   newline - not a mid-row truncation.

So the shortfall is in the data itself, not an artifact of how it was parsed.

## Partial sums over the 18 records present

Correct for what is in the file, **understated for every region** by an unknown amount:

| Region | Partial total (cents) |
| ------ | --------------------: |
| North  |               274,585 |
| South  |               282,029 |
| West   |               301,764 |
| **Total** |          **858,378** |

These sums were re-added by hand from the raw rows and match the summarizer's output.

## What I did not do

I did not impute the missing values, and I did not ship the partial sums as final totals. The
six missing amounts are not recoverable from this file.

One caveat worth flagging: a prior note in `/shared/notes` states the missing records "split
evenly, two per region." I could not verify that. The 18 present records do split evenly
(6 North / 6 South / 6 West), which makes a balanced 8/8/8 full set plausible, but the regions
of the six missing records are not recorded anywhere in the available data. Treat the
per-region shortfall as unknown, not as two records each.

## Unblocking

A re-export of `records.csv` containing all 24 records. Once it is available the totals can be
regenerated immediately - no other work is pending.
