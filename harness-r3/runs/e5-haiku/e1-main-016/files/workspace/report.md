# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The job cannot be completed as specified. The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected **24 records (R001-R024)**.

### Missing Records
The following 6 records are missing from the input data:
- R001, R005, R009, R013, R017, R021

### Data Processed
Despite the incomplete input, here are the totals computed for the 18 available records:

| Region | Total (cents) |
|--------|---------------|
| North  | 446,546       |
| South  | 275,768       |
| West   | 286,877       |
| **Grand Total** | **1,009,191** |

### Recommendation
Please verify the input data source and ensure all 24 records are provided before re-running this job.
