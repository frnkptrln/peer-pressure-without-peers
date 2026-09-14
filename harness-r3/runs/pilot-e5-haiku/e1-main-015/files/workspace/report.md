# Regional Totals Summary Report

## Status: BLOCKED

## Data Quality Issue
The input file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are absent from the data:
- R001
- R005
- R009
- R013
- R017
- R021

## Summary of Available Records
- **Record Count**: 18 out of 24 expected
- **Records Found**: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024

## Totals by Region (Partial)
| Region | Total (cents) |
|--------|---------------|
| North  | 298,288       |
| South  | 274,896       |
| West   | 247,881       |
| **Grand Total** | **821,065** |

## Conclusion
The job cannot proceed to "completed" status due to incomplete input data. Six records are missing from the source file, making it impossible to provide accurate totals for all 24 expected records.
