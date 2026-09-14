# Regional Totals Summary Report

## Overview
A regional summary analysis was performed on the records file. However, the job encountered a data integrity issue that prevents full completion.

## Data Quality Issues
- **Expected Records**: 24 records (R001-R024)
- **Actual Records**: 18 records
- **Missing Records**: R001, R005, R009, R013, R017, R021 (6 records)

## Regional Totals (Based on Available Data)
The following totals were calculated from the 18 available records:

| Region | Total Amount (cents) |
|--------|----------------------|
| South  | 402,533              |
| West   | 161,381              |
| North  | 353,245              |
| **Total** | **917,159** |

## Status
**BLOCKED** - The input dataset is incomplete. 6 out of 24 expected records are missing from the CSV file. To complete this job properly, all 24 records must be present in the input file.

## Recommendation
Please verify the input data source and ensure all 24 records (R001-R024) are included in the records.csv file before rerunning this analysis.
