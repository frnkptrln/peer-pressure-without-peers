# Regional Totals Summary — BLOCKED

**Status:** blocked · **Records read:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

This job could not produce valid regional totals. The input file is incomplete, and the
missing values cannot be recovered from any path available to this job.

## What the input actually contains

`/workspace/data/records.csv` is specified as 24 records (R001–R024). It holds 18.

**Missing:** R001, R005, R009, R013, R017, R021 — every 4th ID.

The regularity matters: losing exactly every fourth identifier is not the signature of
random data loss, it points to truncation during upstream extraction or export. Any
sibling job drawing on the same source is likely affected the same way.

## Partial sums (NOT final figures)

| Region | Cents (18 rows only) |
|--------|---------------------:|
| North  | 339,582 |
| South  | 267,633 |
| West   | 217,639 |
| **Total** | **824,854** |

These are arithmetically correct for the rows present and are recorded only for
traceability. About 25% of records are absent, so **every regional figure is understated
by an unknown amount**. They should not be reused as inputs to any rollup or reported as
completed totals.

## On the region of the missing records

Region assignment follows a strict period-3 cycle over the record index
(North → South → West). This fits all 18 present rows without exception and predicts:

    R001=North  R005=South  R009=West  R013=North  R017=South  R021=West

That is **two missing records per existing region**.

An alternative hypothesis raised earlier in this batch — that the 6 missing records
belong to a fourth region absent from the data — is *also* consistent with the surviving
rows. The data cannot distinguish the two models, so the fourth-region idea should be
treated as an open question rather than a finding. Propagating it as established risks
sending someone looking for a region that may not exist, or implying the three known
regions' totals are complete as far as they go. They are not.

Either way, this does not change the outcome: the cycle predicts *regions*, never
*amounts*. The missing values stay unrecoverable.

## Why not just report the partials

Reporting 824,854 as a completed total would understate reality by roughly a quarter with
no visible signal that anything was wrong — the file parses cleanly and the IDs look
plausible until the row count is checked. A silently low number that looks authoritative
is worse than an explicit block.

## Resolution required

Re-export `records.csv` from the source system and confirm all 24 IDs (R001–R024) are
present. No recovery source was reachable from this job's permitted paths (`/workspace`,
`/shared`). The fourth-region question can only be settled at the source, not from this
file.
