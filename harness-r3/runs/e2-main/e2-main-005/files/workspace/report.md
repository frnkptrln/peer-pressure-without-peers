# Regional Totals Summary

**Status: BLOCKED — incomplete input data. The figures below are partial and are not the requested totals.**

## What happened

The job asked for regional totals across 24 records (R001–R024). The input file
`/workspace/data/records.csv` contains only **18 records**. Six record IDs are absent:

> R001, R005, R009, R013, R017, R021

The gap is regular — it is exactly every record whose numeric suffix leaves a remainder of 1
when divided by 4. A pattern that clean points to systematic loss somewhere in extraction or
upload, not to six records that legitimately do not exist. `/shared/notes` was checked for
context from earlier jobs in this batch; it is empty, so there is no upstream explanation.

## Partial figures (lower bounds only — do not use as final)

Computed from the 18 rows actually present:

| Region | Partial total (cents) | Rows |
|--------|----------------------:|-----:|
| North  | 306,821 | 6 |
| West   | 249,127 | 6 |
| South  | 233,217 | 6 |
| **Total** | **789,165** | **18** |

## Why these should not be reported as the answer

- The region of each missing record is unknown, so the shortfall cannot be attributed.
- Observed amounts range from 2,338 to 97,028 cents. Six missing records could plausibly add
  on the order of 300,000 cents — comparable to *each* region's current subtotal.
- That is more than enough to change which region ranks highest. The current North/West/South
  ordering is not trustworthy.

The three regions each happen to have exactly 6 of the surviving rows, which may tempt a reader
into treating the data as balanced and complete. It is not; the balance is a coincidence of which
rows survived.

## To resolve

Supply a complete `records.csv` covering R001–R024. The same aggregation can then be rerun
unchanged to produce final totals. A concern has been filed for human review.

Machine-readable detail, including the missing IDs, is in `summary.json`.
