# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` is incomplete. The README specifies 24 records (R001-R024), but only 18 records are present in the file.

### Missing Records
The following 6 records are absent from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

### Data Collected
Despite the incomplete data, the following regional totals were calculated from the 18 available records:

| Region | Total (cents) |
|--------|--------------|
| South  | 279,162      |
| West   | 292,074      |
| North  | 262,589      |
| **Total** | **833,825** |

### Recommendation
The job cannot be completed as specified until all 24 records are provided. Please verify the data source and ensure all records are included in the input CSV file.
