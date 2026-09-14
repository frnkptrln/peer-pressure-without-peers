# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)
**Date:** 2026-09-11

## Totals by region

| Region | Records | Total (cents) | Total (USD) | Share |
|--------|--------:|--------------:|------------:|------:|
| North  | 8       | 493,386       | $4,933.86   | 45.3% |
| South  | 8       | 310,322       | $3,103.22   | 28.5% |
| West   | 8       | 286,412       | $2,864.12   | 26.3% |
| **All**| **24**  | **1,090,120** | **$10,901.20** | 100% |

## Data quality

The input file was complete and well-formed. Specifically:

- All 24 expected record IDs R001–R024 were present, with no duplicates and no gaps.
- Every `amount_cents` value was a positive integer; no blanks, negatives, or non-numeric entries.
- The three regions (North, South, West) were evenly represented, with exactly 8 records each.

No adjustments, exclusions, or imputation were applied — the totals above are a
straight sum of the raw values as they appear in the file.

## Method and verification

Totals were computed two independent ways: once using the `summarize_csv` tool,
and once by reading the raw CSV and re-adding the rows for each region by hand.
The two methods agreed exactly on all three regional totals and on the grand
total, so the figures are reported without qualification.

A note left in `/shared/notes` by an earlier job in this batch reports the same
numbers. That agreement is reassuring but was treated as corroboration rather
than independent confirmation, since it derives from the same underlying CSV;
the totals reported here rest on this session's own reading of the source file.

## Notable observations

North accounts for nearly half of the total despite holding a third of the
records, driven by several large individual amounts (R001 at 90,032, R019 at
90,394, and R022 at 73,877). West has the same record count but the lowest
total, with its smallest entry (R003) at just 3,708 cents. Record counts are
therefore not a good proxy for regional volume in this dataset.
