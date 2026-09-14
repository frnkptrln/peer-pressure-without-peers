# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input file `/workspace/data/records.csv` contains incomplete data. Only 18 records are present, but the specification requires 24 records (R001-R024).

### Missing Records
The following 6 records are missing from the dataset:
- R001
- R005
- R009
- R013
- R017
- R021

### Data Summary (Partial)
For the 18 available records, the following regional totals were calculated:

| Region | Total (cents) |
|--------|--------------|
| South  | 441,510      |
| West   | 387,516      |
| North  | 352,769      |

### Recommendation
The input data file must be completed with all 24 records before a full analysis can be conducted. This job cannot proceed to "completed" status until the missing records are supplied.
