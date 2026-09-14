# Regional Totals Summary Report

## Status: BLOCKED

### Summary
The input file `/workspace/data/records.csv` contains only 18 complete records instead of the expected 24 records specified in the task requirements.

### Data Received
- **Records Found**: 18 (R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024)
- **Records Missing**: 6 (R001, R005, R009, R013, R017, R021)

### Totals for Available Records
| Region | Amount (cents) |
|--------|---------------:|
| South  | 329,758 |
| West   | 333,531 |
| North  | 422,507 |
| **Total** | **1,085,796** |

### Issue
The task requires processing all 24 records (R001-R024) to produce a valid completion status. With 6 records missing from the input data, the totals cannot be verified against the complete reference dataset. The job cannot be completed without access to the missing records.

### Recommendation
The missing records need to be restored to the input file before this job can be completed successfully.
