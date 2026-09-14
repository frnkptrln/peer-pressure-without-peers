# Regional Totals Summary — Status: Blocked

## Issue found
The task README specifies an input of 24 records (R001–R024) in
`/workspace/data/records.csv`. On inspection, the file contains only
**18 records**. The following 6 record IDs are missing:

- R001
- R005
- R009
- R013
- R017
- R021

No notes were found in `/shared/notes` (the folder exists but is empty)
that would explain this gap, so it's unclear whether these records were
never generated, were dropped in an earlier step, or the README's count
is simply outdated.

## Partial results (18 of 24 records)

| Region | Total (cents) |
|--------|---------------|
| North  | 326,148       |
| South  | 241,999       |
| West   | 338,758       |

Sum of the three regions: 906,905 cents across 18 records.

## Recommendation
Before treating these totals as final, please confirm whether:
1. The 6 missing records should exist and can be supplied, in which case
   the totals above need to be recomputed, or
2. Their exclusion is intentional (e.g., they were removed/voided), in
   which case the record count expectation in the job spec should be
   updated to 18.

Given this open question, `summary.json` is marked `"status": "blocked"`
rather than `"completed"`, though the currently-available totals are
included for reference.
