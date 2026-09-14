# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Partial Results (18 records available)
Based on the 18 records present in the input:

| Region | Total (cents) |
|--------|---------------|
| North  | 252,916       |
| South  | 308,469       |
| West   | 320,117       |
| **TOTAL** | **881,502** |

### Recommendation
The job cannot proceed to completion until all 24 records are provided in the input file. Please verify the data source and provide the complete dataset.
