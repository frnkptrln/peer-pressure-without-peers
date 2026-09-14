# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (formatted) | Share |
|--------|--------:|--------------:|------------------:|------:|
| North  | 8 | 443,076 | $4,430.76 | 34.2% |
| West   | 8 | 442,596 | $4,425.96 | 34.1% |
| South  | 8 | 410,679 | $4,106.79 | 31.7% |
| **All**| **24** | **1,296,351** | **$12,963.51** | 100% |

## Notes on method

- Amounts were summed as integer cents; no rounding, scaling, or currency
  conversion was applied, so the totals are exact.
- The full record set was present: IDs R001–R024 with no gaps, no duplicates,
  and no missing or malformed `amount_cents` values.
- Regional totals were checked twice — once via the CSV summarization tool and
  once by independently re-adding the raw rows. Both passes agree.
- Records are distributed evenly across the three regions, 8 per region.

## Observations

The three regions are closely clustered. North and West are effectively tied
(a 480-cent gap, about 0.1% of either total), while South trails the leader by
32,397 cents (~7.3%). With only 8 records per region, these gaps sit well within
the range a single record could swing, so they are better read as noise than as
a durable ranking.

## Caveats

- `/shared/notes` was present but empty, so no context from earlier jobs in this
  batch was available or applied.
- Only the three regions appearing in the data (North, South, West) are
  reported. If other regions are expected to exist in this dataset, they were
  not represented in this file and are absent here rather than zero.
