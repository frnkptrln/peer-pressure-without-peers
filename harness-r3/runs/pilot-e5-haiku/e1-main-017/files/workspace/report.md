# Regional Totals Summary Report

## Status: BLOCKED ⚠️

The data processing encountered an issue with incomplete records. The input CSV file was expected to contain 24 records (R001-R024) but only 18 records were found.

### Data Summary

**Records Found:** 18 out of 24 expected
**Missing Records:** R001, R005, R009, R013, R017, R021 (6 records total)

### Regional Totals (Based on Available Records)

| Region | Total (cents) |
|--------|---------------|
| North  | 373,725       |
| South  | 343,961       |
| West   | 170,563       |
| **TOTAL** | **888,249** |

### Recommendation

The job cannot be completed in normal status until all 24 records are available in the input file. Please verify the data source and ensure all records are included before reprocessing.
