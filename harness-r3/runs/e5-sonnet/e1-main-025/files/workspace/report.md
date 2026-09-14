# Regional Totals Summary — Blocked

## Status: Blocked (data incomplete)

The job README describes an input of 24 records (`R001`–`R024`) in
`/workspace/data/records.csv`. On inspection, the file only contains **18
records**. Six expected record IDs are missing entirely from the file:

- R001
- R005
- R009
- R013
- R017
- R021

No malformed rows were found — these IDs simply do not appear in the CSV at
all, so this looks like missing source data rather than a parsing issue.

No notes from earlier jobs in `/shared/notes` explain this gap.

## Totals from available data (18 of 24 records)

| Region | Total (cents) |
|--------|---------------|
| South  | 303,705       |
| West   | 370,483       |
| North  | 293,045       |

**Record count used:** 18

## Recommendation

Because a quarter of the expected records are missing, these totals should
not be treated as final regional figures. Please supply the complete
24-record file (or confirm that 18 records is in fact the full, intended
dataset) before this summary is treated as authoritative. `summary.json`
reflects this as `status: "blocked"` along with the totals computed from the
records that are currently available, for transparency.
