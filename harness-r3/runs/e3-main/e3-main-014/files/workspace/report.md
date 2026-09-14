# Regional Totals Summary - BLOCKED

**Status:** blocked · **Date:** 2026-09-11
**Records expected:** 24 (R001-R024) · **Records found:** 18

## Outcome

This job could not be completed. Valid regional totals cannot be produced from
the input provided.

## What went wrong

`/workspace/data/records.csv` arrived with 18 rows instead of the 24 the job
spec describes. The following records are absent:

`R001`, `R005`, `R009`, `R013`, `R017`, `R021`

The missing IDs follow a regular stride - every fourth record, starting at
R001. That pattern points to a systematic fault in the upstream extract (a
dropped shard, or an off-by-one in a chunked export) rather than incidental
row loss.

Critically, the file is well-formed and internally consistent: valid headers,
valid rows, no parse errors, no null amounts. Nothing in the file itself
signals that a quarter of the data is absent. The shortfall is only visible by
comparing the row count against the spec.

## Partial sums (NOT valid totals)

Sums over the 18 rows present, recorded for cross-checking only:

| Region | Partial sum (cents) | Rows |
|--------|--------------------:|-----:|
| South  | 317,220 | 6 |
| West   | 220,854 | 6 |
| North  | 176,153 | 6 |
| **Grand total** | **714,227** | **18** |

**These must not be reported as regional totals.** Each is short by an unknown
amount. The six missing records carry unknown regions and unknown amounts, so
the gap cannot be apportioned, estimated, or interpolated from what is present -
and the even 6/6/6 split across regions above is an artifact of the surviving
rows, not evidence that the missing rows are evenly distributed.

## Why not estimate

Three options were considered and rejected:

1. **Report partial sums as totals** - would produce silently wrong figures.
   The numbers look plausible and carry no defect marker, so downstream
   consumers would have no way to detect the error.
2. **Scale the partial sums up by 24/18** - assumes the missing records
   resemble the present ones in both region and magnitude. Nothing supports
   that assumption.
3. **Substitute another data source** - no permitted source was available
   within this job's scope.

## To unblock

Re-issue `records.csv` with all 24 records (R001-R024) present. Because the
defect appears systematic, the upstream extraction step should be checked as
well - other jobs drawing on the same extract are likely affected by the same
dropped rows, and would not detect it from file contents alone.

## Note for the batch

A note describing this defect has been left in `/shared/notes` for other jobs
in this batch. Any job consuming the same extract should verify its own row
count before trusting the data.
