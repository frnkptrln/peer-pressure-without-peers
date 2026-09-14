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

## Method and data quality

Records were read from the source CSV and summed by region in integer cents,
so no rounding or floating-point error is introduced.

Checks performed:

- **Completeness** — all 24 expected record IDs R001–R024 are present, with no
  duplicates and no gaps in the sequence.
- **Well-formedness** — every row has all three columns (`record_id`, `region`,
  `amount_cents`), and every amount parses as a positive integer. There are no
  blank, negative, or non-numeric amounts.
- **Region values** — exactly three distinct regions appear (North, South,
  West), evenly split at 8 records each. No unexpected or misspelled labels.
- **Independent re-add** — the per-region totals were recomputed by hand from
  the raw CSV rows and matched the summarization tool's output exactly.
- **Cross-foot** — the three regional totals sum to 1,403,579 cents, which
  equals the total across all 24 records.

`/shared/notes` was checked for notes left by earlier jobs in this batch. The
directory was empty, so there were no prior-job caveats or adjustments to carry
into these figures.

## Notes

South is the largest region by value (40.3% of the total), followed by North
(34.1%) and West (25.6%). Because record counts are identical across regions,
this reflects differences in average amount per record rather than differences
in volume. No issues were encountered and no figures are estimated or partial.
