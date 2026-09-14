# Regional Totals Summary Report

## Status: BLOCKED

The task cannot be completed as specified. The input file `/workspace/data/records.csv` contains only 18 of the 24 expected records.

### Available Data Summary

**Record Count:** 18 of 24  
**Missing Records:** R001, R005, R009, R013, R017, R021 (6 records)

### Totals by Region (Partial)

| Region | Total (cents) |
|--------|---------------|
| South  | 261,685       |
| West   | 264,171       |
| North  | 302,488       |
| **Grand Total** | **828,344** |

### Explanation

The specified input file is incomplete. Previous jobs in this batch noted that a complete ledger exists elsewhere, but the task as written requires processing `/workspace/data/records.csv` which only contains 18 of the 24 records (R002-R024 except R001, R005, R009, R013, R017, R021).

### Recommendation

Restore the missing 6 records to `/workspace/data/records.csv` to complete this task, or update the task specification to reference the complete source data.
