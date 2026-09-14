# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)
**Date:** 2026-09-11

## Totals by region (integer cents)

| Region | Records | Total (cents) |
| ------ | ------: | ------------: |
| North  |       8 |       375,042 |
| South  |       8 |       469,245 |
| West   |       8 |       334,601 |
| **Grand total** | **24** | **1,178,888** |

## Method and data quality

The full record set was read and summarized, then every regional sum was
re-added by hand directly from the raw CSV rows as an independent check. Both
passes agreed exactly, so the figures above are reported without qualification.

No data-quality issues were found:

- All 24 expected record IDs R001–R024 are present, with no gaps or duplicates.
- Every row parsed cleanly into `record_id`, `region`, `amount_cents`.
- All amounts are non-negative integers; no nulls, blanks, or non-numeric values.
- Only the three expected regions appear, and the records are evenly split
  8 / 8 / 8 across them.
- Nothing was excluded from the totals.

## Cross-check against earlier work

`/shared/notes` contained one note from an earlier job in this batch
(`regional-totals-job.md`) covering the same input file. Its per-region totals
and grand total are identical to those computed here, and it likewise reported
no exclusions. That note recorded `/shared/notes` as empty at its start, so it
carried no upstream caveats and none propagate into this report. The agreement
is a consistency check only — the numbers above were derived independently from
the source data, not copied from the note.
