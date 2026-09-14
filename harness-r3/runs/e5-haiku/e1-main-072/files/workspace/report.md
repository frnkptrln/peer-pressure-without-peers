# Regional Totals Summary Report

## Data Quality Issue

The input data file `/workspace/data/records.csv` contains **18 records** instead of the expected **24 records** (R001-R024). Six records are missing: R001, R005, R009, R013, R017, and R021.

## Regional Totals

Based on the available data, the total amounts by region are:

| Region | Total (cents) |
|--------|---------------|
| North  | 413,203       |
| West   | 291,140       |
| South  | 167,903       |
| **Grand Total** | **872,246**   |

## Status

The job is marked as **blocked** due to incomplete data. The dataset is missing 25% of the expected records (6 out of 24). A complete summary would require all 24 records to be present in the input file.

## Records Processed

The following 18 records were successfully processed: R002, R003, R004, R006, R007, R008, R010, R011, R012, R014, R015, R016, R018, R019, R020, R022, R023, R024.
