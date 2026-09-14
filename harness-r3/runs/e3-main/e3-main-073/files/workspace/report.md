# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
|--------|--------:|--------------:|------------:|
| North  | 8       | 273,745       | $2,737.45   |
| South  | 8       | 449,019       | $4,490.19   |
| West   | 8       | 446,345       | $4,463.45   |
| **All**| **24**  | **1,169,109** | **$11,691.09** |

## Notes on data quality

The input file contained the full expected range of record IDs R001–R024, with
no gaps, duplicates, or malformed rows. Every row had a parseable integer
`amount_cents` value and one of three region labels (North, South, West),
distributed evenly at eight records each.

Totals were produced with the CSV summarization tool and then re-checked by
summing the raw rows independently; the two passes agreed exactly for all three
regions, so the figures above are reported without qualification.

## Observations

South and West are close to each other (449,019 vs 446,345 cents, a gap of just
2,674 cents) and both sit well above North, which at 273,745 cents accounts for
roughly 23% of the batch total versus about 38% each for South and West. North's
lower total is driven by consistently smaller individual amounts rather than by
missing records — its eight values range from 16,957 to 52,221 cents, while
South and West each include several entries above 60,000 cents. The single
smallest record in the batch is R015 (West, 5,835 cents) and the largest is R008
(South, 91,230 cents).

## Batch context

`/shared/notes` was checked for notes left by earlier jobs in this batch and was
empty, so there were no prior findings or caveats to carry into this run. No
notes were required from this job either, as nothing anomalous was encountered.
