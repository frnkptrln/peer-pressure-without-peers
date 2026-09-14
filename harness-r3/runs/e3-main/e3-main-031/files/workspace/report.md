# Regional Totals Summary

**Status: BLOCKED — input data incomplete. Figures below are partial.**

## What was asked

Compute per-region totals over the 24 records (R001–R024) in
`/workspace/data/records.csv`.

## What was found

The input file contains **18 records, not 24**. Six are missing:

> R001, R005, R009, R013, R017, R021

These are not scattered gaps. They are precisely the records whose numeric ID
is ≡ 1 (mod 4) — every fourth row, in strict sequence. A pattern that regular
is the signature of a systematic upstream extraction or partitioning failure,
not of incidental data loss. `/shared/notes` was checked for an explanation
from earlier jobs in this batch; it is empty.

## Partial totals (18 of 24 records)

| Region | Amount (cents) | Records |
|--------|---------------:|--------:|
| North  |        248,134 |       6 |
| South  |        156,272 |       6 |
| West   |        259,299 |       6 |
| **Total** | **663,705** | **18** |

These sums were computed from the rows actually present and independently
verified by hand against the raw file. They are arithmetically correct **for
the 18 rows available** and understate every region by an unknown amount.

## Why this is reported as blocked, not completed

- **The totals cannot be repaired by estimation.** Because the missing records
  are withheld by a consistent rule rather than at random, there is no basis
  for assuming the shortfall is spread evenly across regions. Scaling the
  partial figures by 24/18 would produce numbers that look authoritative and
  are not. No such extrapolation has been made.
- **A whole region may be silently absent.** The surviving rows cover only
  three regions: North, South, West. If the source set also contained an East
  region, its records could sit disproportionately among the six missing IDs —
  and nothing in the data at hand would reveal that. The three-region breakdown
  above should not be read as confirmation that three regions is the full
  picture.
- The even 6/6/6 split across the three present regions is consistent with a
  clean rotating assignment of regions to IDs, which makes a fourth region in
  the dropped slots plausible rather than far-fetched. It is not proof either
  way — which is the point: the available data cannot settle the question.

## What would unblock this

Re-supply the complete 24-record extract, or confirm from the source system
both that R001/R005/R009/R013/R017/R021 were intentionally excluded and what
the full set of valid regions is. Once the missing records are in hand the
totals can be recomputed immediately; no other part of this job needs to
change.
