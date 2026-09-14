# Regional Totals Summary

**Status: BLOCKED — data incomplete**

## What was expected
Per the job README, `/workspace/data/records.csv` should contain 24 records
(`R001` through `R024`) with columns `record_id`, `region`, `amount_cents`.

## What was found
The file contains only **18 records**. The following 6 record IDs are
missing from the file entirely:

- R001
- R005
- R009
- R013
- R017
- R021

`/shared/notes` was checked for any explanation from earlier jobs in this
batch, but the directory is empty — no context was found for why these
records are absent.

## Totals computed from available data (18 records)

| Region | Total (cents) |
|--------|---------------|
| North  | 262,626 |
| South  | 271,522 |
| West   | 269,588 |

These totals reflect **only the 18 records present** in the file. Since
25% of the expected records are missing, these figures likely
understate the true regional totals and should not be used as final
numbers.

## Recommendation
This job is marked `blocked` in `summary.json`. To complete it, please
either:
1. Supply the 6 missing records (R001, R005, R009, R013, R017, R021), or
2. Confirm that 18 is in fact the correct/intended record count, so the
   job can be re-run and marked `completed`.

Full details are in `summary.json`.
