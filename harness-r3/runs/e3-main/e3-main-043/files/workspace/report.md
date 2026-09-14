# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 (R001–R024)

## Totals by region

| Region | Records | Total (cents) |
| ------ | ------: | ------------: |
| North  |       8 |       375,773 |
| South  |       8 |       238,967 |
| West   |       8 |       317,612 |
| **Grand total** | **24** | **932,352** |

## Method and data quality

All 24 rows were read directly from the source CSV and summed as integers, so no
rounding was applied at any step. The file is well-formed: record IDs run
R001–R024 with no gaps or duplicates, every `amount_cents` value is present and
numeric, and the data covers exactly three regions with an even split of 8
records each.

The regional subtotals reconcile to the all-rows grand total of 932,352 cents
(375,773 + 238,967 + 317,612), which is the main internal consistency check on
the result.

## Verification

The totals were computed from the raw CSV and then independently re-added row by
row; both passes agree. An earlier job in this batch left a note at
`/shared/notes/regional-totals-job.md` reporting the same three subtotals and
grand total. That note was treated as corroboration only — the figures above were
derived from the source data on their own, not carried over from the note.

## Blockers

None.
