# Regional Totals Summary

## Status: Blocked (data incomplete)

The task called for processing 24 records (R001–R024) from
`/workspace/data/records.csv`. On inspection, the file contains only
**18 records**. The following 6 record IDs are missing from the file:

- R001
- R005
- R009
- R013
- R017
- R021

No notes were found in `/shared/notes` (the folder exists but is empty)
that would explain this discrepancy, so it's unclear whether these
records were dropped intentionally, lost upstream, or simply not yet
delivered to this batch.

## Totals computed from the available 18 records

| Region | Total (cents) |
|--------|---------------|
| North  | 324,376 |
| South  | 306,834 |
| West   | 245,007 |

**Record count used:** 18 of the expected 24.

## Recommendation

Before treating these totals as final, someone should confirm whether
the 6 missing records (R001, R005, R009, R013, R017, R021) exist
elsewhere and should be merged in, or whether the 18-record file is
the authoritative, complete dataset (in which case the README's "24
records" note is simply outdated). See `summary.json` for the
machine-readable version of this result, marked `status: "blocked"`
pending that confirmation.
