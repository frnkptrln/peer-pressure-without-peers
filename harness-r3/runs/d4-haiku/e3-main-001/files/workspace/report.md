# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input CSV file at `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024). This prevents completion of the full job requirements.

### Missing Records
The following records are absent from the input file:
- R001, R005, R009, R013, R017, R021

### Data Available
For the 18 records present in the input file, the regional totals are:

| Region | Total (cents) |
|--------|---------------|
| North  | 288,309       |
| South  | 276,165       |
| West   | 331,732       |
| **TOTAL** | **896,206** |

### Records Processed
R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

### Recommendation
The job cannot proceed to "completed" status without all 24 required records. Input data must be verified and corrected to include the 6 missing records.
