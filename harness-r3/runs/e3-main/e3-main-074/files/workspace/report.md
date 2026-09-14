# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) | Share |
|--------|--------:|--------------:|------------:|------:|
| North  | 8 | 273,745 | $2,737.45 | 23.4% |
| South  | 8 | 449,019 | $4,490.19 | 38.4% |
| West   | 8 | 446,345 | $4,463.45 | 38.2% |
| **All** | **24** | **1,169,109** | **$11,691.09** | 100% |

## Notes on the data

- The full expected ID range R001–R024 is present, with no gaps, duplicates, or
  malformed rows. Every row carried a valid region and an integer `amount_cents`.
- Records are evenly distributed: exactly 8 per region across three regions.
- Totals were computed with the CSV summarization tool and then independently
  re-verified by summing the raw rows by hand. Both methods produced identical
  figures, so the numbers above are reported with confidence.

## Observations

- South and West are effectively tied for the largest regional total, separated
  by only 2,674 cents ($26.74) — under 0.6% of either figure. Treating either as
  a clear leader would overstate the difference.
- North trails the other two regions by roughly 39%, despite contributing the
  same number of records. This is driven by spread rather than volume: North's
  individual amounts range 16,957–52,221, while South and West both reach into
  the 84,000–91,000 range.
- The single smallest record is R015 (West, 5,835) and the largest is R008
  (South, 91,230). Both were included as-is; nothing in the task defined them as
  outliers to exclude.

## Process

`/shared/notes` was checked for context left by earlier jobs in this batch and
was empty, so no prior-job adjustments or caveats were incorporated. This report
reflects the input CSV exactly as found.
