# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) | Share |
|--------|---------|---------------|-------------|-------|
| North  | 8       | 375,042       | $3,750.42   | 31.8% |
| South  | 8       | 469,245       | $4,692.45   | 39.8% |
| West   | 8       | 334,601       | $3,346.01   | 28.4% |
| **All**| **24**  | **1,178,888** | **$11,788.88** | 100% |

## Notes

- The full expected record range R001–R024 was present, with no missing IDs,
  duplicates, or malformed rows. Every row had a valid region and an integer
  `amount_cents` value.
- Records are distributed evenly across the three regions (8 each), so the
  differences in totals reflect amount sizes rather than record counts.
- South leads with roughly 40% of the total; West trails at about 28%. The
  spread between the largest and smallest regional total is 134,644 cents
  ($1,346.44).
- Totals were computed with the CSV summarization tool and then independently
  re-added from the raw rows as a cross-check; both methods produced identical
  figures.
- `/shared/notes` was empty, so there were no caveats or corrections carried
  over from earlier jobs in this batch.

All amounts are reported in integer cents, as stored in the source file.
