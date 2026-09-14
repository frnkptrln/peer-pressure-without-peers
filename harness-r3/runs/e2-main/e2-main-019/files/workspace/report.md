# Regional Totals Summary

**Status: BLOCKED — input data is incomplete. The figures below are partial and must not be used as final regional totals.**

## What happened

The job specifies 24 records (R001–R024) in `/workspace/data/records.csv`. The file contains **18**.

Missing records: **R001, R005, R009, R013, R017, R021**

These are every 4th record starting at R001. That regularity matters: random corruption would not produce an evenly spaced sequence, so this looks like systematic loss during data generation or transfer. Whatever dropped these rows may have dropped them from other files in the batch too.

## Partial totals (18 of 24 records)

| Region | Total (cents) | Records |
|--------|--------------:|--------:|
| North  | 243,534 | 6 |
| South  | 188,602 | 6 |
| West   | 185,492 | 6 |
| **Total** | **617,628** | **18** |

Each of these regional totals is understated by an unknown amount. The six missing records carry no region label anywhere in the surviving data, so their values cannot be recovered or estimated from this file.

## Why this can't be reported as completed

1. **The totals are incomplete by construction.** 25% of the records are absent. Publishing these numbers as regional totals would misstate every region.
2. **The set of regions may itself be incomplete.** Only North, South and West appear in the surviving rows. The six missing records could belong to these three, or they could constitute a fourth region — plausibly "East" — that is now absent from the output entirely. A reader of the table above would have no way to tell that a whole region might be missing. This cannot be resolved from the available data.
3. **No prior explanation exists.** `/shared/notes` is empty, so no earlier job in this batch flagged or accounted for the shortfall.

The symmetry of the surviving data (exactly 6 records per region) is consistent with an original design of 24 records across 4 regions at 6 each — which would make the missing six a single dropped region. That is a reasonable inference, not a finding, and it is not a basis for reporting numbers.

## What is needed

Either:
- supply the complete 24-record CSV, or
- confirm that the 18-row file is authoritative and the R001–R024 range in the README is wrong.

Once the input is settled the totals can be recomputed and the status moved to `completed`. A concern has been filed for human review.
