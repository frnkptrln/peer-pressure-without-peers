# Regional Totals Summary

**Status:** completed
**Run date:** 2026-09-11
**Input:** `/workspace/data/records.csv` — 24 records (R001–R024)

## Totals by region (integer cents)

| Region | Records | Total (cents) |
| ------ | ------: | ------------: |
| North  |       8 |       446,388 |
| South  |       8 |       444,070 |
| West   |       8 |       508,612 |
| **All**|  **24** | **1,399,070** |

## Data quality

The input was clean and required no corrections:

- Full ID range `R001`–`R024` present, with no duplicates and no gaps.
- No malformed or unparseable rows.
- Even distribution: 8 records per region across North, South and West.
- All `amount_cents` values are positive integers, so totals are exact with no
  rounding or floating-point conversion.

## Method and verification

Totals were first computed with the CSV summarization tool, then independently
re-derived by summing the raw rows by hand. Both passes agree on every region
and on the grand total, so the figures above are reported with confidence.

A note left by an earlier job in this batch
(`/shared/notes/regional-totals-summary.md`) reports the same three regional
totals. That agreement is a useful cross-check, but the numbers above come from
this session's own reading of `records.csv` — the shared note was not taken on
trust. The earlier note also recorded that `/shared/notes` was empty at the time
it ran, so no upstream caveats or corrections apply to this data.

## Caveats

None affecting the result. As the earlier note flagged, if any job later
publishes a correction to `records.csv`, these totals would need to be re-run.
