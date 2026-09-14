# Regional Totals Summary Report

## Status: BLOCKED

## Data Quality Issue

The input file `/workspace/data/records.csv` contains only **18 records** instead of the expected 24 records (R001-R024).

### Missing Records
The following 6 records are absent from the dataset:
- R001, R005, R009, R013, R017, R021

### Summary of Available Data

**Total Records Processed:** 18 of 24

**Regional Totals (in cents):**
- North: 446,546
- South: 275,768
- West: 286,877

**Grand Total:** 1,009,191 cents

### Records by Region

**North Region (5 records):** R004, R007, R010, R016, R019, R022
**South Region (5 records):** R002, R008, R011, R014, R020, R023
**West Region (5 records):** R003, R006, R012, R015, R018, R024

## Conclusion

Processing has been blocked due to incomplete input data. The dataset is missing 25% of expected records. Completion of this job requires all 24 records to be present in the input file.
