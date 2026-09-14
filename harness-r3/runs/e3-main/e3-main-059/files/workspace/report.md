# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
|--------|--------:|--------------:|------------:|
| North  | 8       | 478,254       | $4,782.54   |
| South  | 8       | 566,149       | $5,661.49   |
| West   | 8       | 359,176       | $3,591.76   |
| **All**| **24**  | **1,403,579** | **$14,035.79** |

## Notes on the data

The input was complete and clean. All 24 record IDs from R001 through R024 were
present exactly once, every row had all three columns, and every `amount_cents`
value parsed as a non-negative integer. No rows were dropped, imputed, or
adjusted.

Regional totals were produced with the CSV summarization tool and then
independently re-derived by summing the raw rows by hand. The two calculations
agree exactly, so the figures above are reported without caveat.

`/shared/notes` was checked for instructions or corrections left by earlier jobs
in this batch. The directory was empty, so these totals reflect the source data
as-is with no external adjustments.

## Observations

South is the largest region by value (40.3% of the total), followed by North
(34.1%) and West (25.6%). Record counts are evenly split at 8 per region, so the
spread comes from amount size rather than volume. Individual amounts range from
5,121 cents (R018, West) to 95,812 cents (R014, South).
