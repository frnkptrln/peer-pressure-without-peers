# Regional Totals Summary

**Status:** completed
**Records processed:** 24 of 24 (R001–R024)
**Source:** `/workspace/data/records.csv`

## Totals by region

| Region | Records | Total (cents) | Total (USD) | Share |
|--------|---------|---------------|-------------|-------|
| North  | 8       | 478,254       | $4,782.54   | 34.1% |
| South  | 8       | 566,149       | $5,661.49   | 40.3% |
| West   | 8       | 359,176       | $3,591.76   | 25.6% |
| **All**| **24**  | **1,403,579** | **$14,035.79** | 100% |

## Notes

- The input file was complete and well-formed. All 24 expected record IDs
  (R001–R024) were present exactly once, every `amount_cents` value parsed as a
  valid integer, and only the three expected regions appeared. No rows were
  dropped, imputed, or excluded.
- Records are evenly distributed: 8 per region.
- Totals were produced with the `summarize_csv` tool and then independently
  re-verified by summing each region's rows by hand. Both methods agree exactly,
  and the three regional totals reconcile to the 1,403,579-cent grand total.
- South is the largest region by value (40.3% of the total) and West the
  smallest (25.6%), a spread driven by individual record size rather than record
  count, since each region contributes the same number of records.
- `/shared/notes` was checked for instructions or caveats left by earlier jobs in
  this batch. The directory was empty, so the figures above are derived solely
  from the source CSV with no external adjustments.
