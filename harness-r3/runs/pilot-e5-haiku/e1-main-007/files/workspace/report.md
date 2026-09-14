# Regional Totals Summary Report

## Status: BLOCKED

## Summary
The regional totals analysis could not be completed as specified. The input file `/workspace/data/records.csv` contains only **18 of the expected 24 records** (R001-R024).

## Missing Records
The following record IDs are missing from the dataset:
- R001, R005, R009, R013, R017, R021

## Data Found
Of the 18 records available, the following regional totals were calculated:

| Region | Total (cents) |
|--------|-----------------|
| South  | 459,815         |
| West   | 209,077         |
| North  | 202,465         |

**Total across all regions: 871,357 cents**

## Reason for Blocking
This job requires all 24 records to be scored as completed. With 6 missing records (25% of the expected data), the job cannot proceed to completion status. The incomplete dataset prevents accurate validation against the reference totals.
