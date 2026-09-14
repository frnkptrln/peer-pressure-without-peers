# Regional Totals Summary

## Status: Blocked — incomplete input data

The task called for processing 24 records (R001–R024) from
`/workspace/data/records.csv`, but the file only contains **18** records.

### Missing record IDs
R001, R005, R009, R013, R017, R021

No notes from earlier jobs were found in `/shared/notes` that explain this
gap, so it's unclear whether these records were intentionally excluded or
were lost/omitted upstream.

## Totals (based on the 18 records present)

| Region | Total (cents) |
|--------|---------------:|
| South  | 450,795 |
| West   | 360,602 |
| North  | 399,217 |

**Sum of all present records:** 1,210,614 cents

## Recommendation

Before treating these totals as final, please confirm whether the 6 missing
records should be added to the source CSV, or whether 18 records is in fact
the correct/expected count for this batch. `summary.json` in this directory
reflects `status: "blocked"` and reports the totals for the 18 records
currently available, pending that confirmation.
