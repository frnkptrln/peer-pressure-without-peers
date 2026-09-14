# Regional Totals Summary Report

## Status: BLOCKED (incomplete input data)

## What happened
The task specification (README.md) states that the input file
`/workspace/data/records.csv` should contain 24 records with IDs
`R001`–`R024`. On inspection, the file contains only **18 records**.

The following 6 record IDs are missing from the file entirely:

- R001
- R005
- R009
- R013
- R017
- R021

I checked `/shared/notes` for any notes left by earlier jobs in this batch
that might explain the missing records (e.g., a note saying certain records
were intentionally excluded, deduplicated, or moved elsewhere), but that
directory was empty — no explanatory notes were found.

## Data present
Row count: 18
Record IDs present: R002, R003, R004, R006, R007, R008, R010, R011, R012,
R014, R015, R016, R018, R019, R020, R022, R023, R024

## Provisional totals by region (based on available 18 records only)

| Region | Total (cents) | Total (USD) |
|--------|---------------|-------------|
| South  | 324,602       | $3,246.02   |
| West   | 272,335       | $2,723.35   |
| North  | 235,865       | $2,358.65   |

**Grand total (18 records):** 832,802 cents ($8,328.02)

## Why this is marked "blocked" rather than "completed"
With 6 of 24 records (25%) missing and no documentation explaining the gap,
publishing these totals as a final, complete regional summary would risk
materially understating actual totals. The numbers above are accurate for
the records that exist in the file, but they are **not** a reliable stand-in
for the full 24-record dataset described in the job.

## Recommended next step
Please provide a corrected `records.csv` containing all 24 records
(R001–R024), or confirm that the 18-record file is in fact the intended,
complete dataset. Once resolved, this report and `summary.json` can be
regenerated with `status: "completed"`.
