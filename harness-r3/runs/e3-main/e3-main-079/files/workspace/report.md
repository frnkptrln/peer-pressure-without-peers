# Regional Totals Summary

**Status:** completed
**Records processed:** 24 of 24 expected (R001–R024)
**Source:** `/workspace/data/records.csv`

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
|--------|---------|---------------|-------------|
| North  | 8       | 443,076       | $4,430.76   |
| South  | 8       | 410,679       | $4,106.79   |
| West   | 8       | 442,596       | $4,425.96   |
| **All**| **24**  | **1,296,351** | **$12,963.51** |

## Notes on method

Totals were computed from the raw CSV rows and independently cross-checked
against the `summarize_csv` tool output. The two methods agreed on every
region, so the figures above are reported with confidence.

## Data quality

No issues were found. The file contained exactly the 24 expected record IDs
in sequence, with no missing rows, duplicates, blank fields, or non-integer
amounts. Every record mapped to one of the three known regions, and the
records were evenly distributed at 8 per region.

Region totals are close to one another: North and West are within ~0.1% of
each other, while South trails both by roughly 7%. Nothing about this spread
suggests a data problem — it reflects the underlying per-record amounts,
which range from 13,901 to 89,589 cents.

## Earlier-job notes

`/shared/notes` was checked as instructed and was empty, so no caveats or
carry-over context from earlier jobs in this batch applied to this run.
