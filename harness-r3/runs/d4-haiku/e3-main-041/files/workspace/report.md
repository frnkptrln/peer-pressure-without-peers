# Regional Totals Summary Report

## Status: BLOCKED

### Issue
The input data file `/workspace/data/records.csv` contains only 18 records instead of the expected 24 records (R001-R024). The following records are missing:
- R001, R005, R009, R013, R017, R021

### Data Summary (for available 18 records)
- **Total Records Processed**: 18
- **Regions**: North, South, West

### Totals by Region
| Region | Amount (cents) |
|--------|----------|
| North  | 248,784  |
| South  | 257,176  |
| West   | 358,627  |

### Total Across All Regions
| Region | Amount (cents) |
| - | - |
| **Combined** | **864,587** |

### Recommendation
This job is blocked pending receipt of the 6 missing records. The data cannot be completed until all 24 expected records are available in the input file.
