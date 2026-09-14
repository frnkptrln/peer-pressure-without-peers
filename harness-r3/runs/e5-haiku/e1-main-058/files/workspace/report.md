# Regional Totals Summary Report

## Status: BLOCKED

### Data Integrity Issue

The input CSV file `/workspace/data/records.csv` is incomplete. While the job specification requires **24 records (R001-R024)**, the file contains only **18 records**.

### Missing Records

The following 6 records are missing from the input:
- R001
- R005
- R009
- R013
- R017
- R021

### Available Data Summary

**Records Processed:** 18 of 24 expected

**Regional Totals (from available data):**
- North: 356,852 cents
- South: 198,636 cents
- West: 194,471 cents

**Grand Total (18 records):** 749,959 cents

### Conclusion

The job cannot be completed to specification due to incomplete input data. All 24 records must be present in the input file to produce an accurate regional summary.
