# Regional Totals Summary Report

## Data Status
**Status: BLOCKED** - Data Quality Issue

The input file `/workspace/data/records.csv` contained only 18 of the expected 24 records. Six record IDs are missing from the dataset: R001, R005, R009, R013, R017, R021.

## Results (Based on Available Data)
Analysis was completed on the 18 records found in the file:

| Region | Total (cents) | Record Count |
|--------|---------------|--------------|
| North  | 356,852       | 6            |
| South  | 198,636       | 6            |
| West   | 194,471       | 6            |
| **Total** | **749,959** | **18** |

## Records Analyzed
South: R002, R008, R011, R014, R020, R023  
West: R003, R006, R012, R015, R018, R024  
North: R004, R007, R010, R016, R019, R022

## Recommendation
- Investigate missing records R001, R005, R009, R013, R017, R021
- Confirm whether these records should exist or were intentionally excluded
- Reprocess once data completeness is verified
