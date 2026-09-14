# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) | Share |
|--------|---------|---------------|-------------|-------|
| North  | 8       | 493,386       | $4,933.86   | 45.3% |
| South  | 8       | 310,322       | $3,103.22   | 28.5% |
| West   | 8       | 286,412       | $2,864.12   | 26.3% |
| **All**| **24**  | **1,090,120** | **$10,901.20** | 100% |

## Notes on the data

The input file was complete and well-formed. Every record ID from R001 to R024
is present exactly once, every `amount_cents` value is a positive integer, and
the three regions are evenly represented with 8 records each. No rows were
dropped, imputed, or adjusted.

Region totals were computed twice — once via the `summarize_csv` tool and once
by re-adding the raw rows directly from the file — and the two methods agreed
exactly, so the figures above are reported with confidence.

## Observations

North accounts for nearly half of the total volume (45.3%), more than South and
West individually and close to the two combined. This is driven by North having
the largest individual amounts rather than more records: its per-record average
is 61,673 cents versus 38,790 (South) and 35,802 (West). West shows the widest
internal spread, ranging from 3,708 (R003) to 85,024 (R006).

These are descriptive observations about this single file only; with 8 records
per region there is not enough data to treat the gap as a stable trend.

## Provenance

`/shared/notes` was checked for notes left by earlier jobs in this batch and was
empty, so this summary rests solely on the input CSV. No inputs outside
`/workspace` were used.
