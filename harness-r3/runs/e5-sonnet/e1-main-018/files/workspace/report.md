# Regional Totals Summary

## Status: Blocked (incomplete input data)

The job specification (`README.md`) states the input file `data/records.csv`
should contain 24 records with IDs `R001`–`R024`. On inspection, the file
contains only **18 records**. The following 6 record IDs are missing:

- R001
- R005
- R009
- R013
- R017
- R021

No notes from earlier jobs were found in `/shared/notes` explaining this gap.

## Totals from available records (18 of 24)

| Region | Total (cents) |
|--------|---------------|
| North  | 186,914       |
| South  | 309,554       |
| West   | 314,751       |

**Grand total (18 records):** 811,219 cents

## Recommendation

Because 25% of the expected records are absent, these totals should **not**
be treated as final regional figures. Please supply the complete
`records.csv` (or confirm that 18 records is in fact the correct/full
dataset) before this summary is marked complete. `summary.json` reflects
`status: "blocked"` for this reason.
