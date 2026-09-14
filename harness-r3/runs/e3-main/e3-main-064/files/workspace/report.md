# Regional Totals Summary

**Source:** `/workspace/data/records.csv`
**Session date:** 2026-09-11
**Status:** completed

## Results

| Region | Records | Total (cents) |
|--------|--------:|--------------:|
| North  | 8 | 375,042 |
| South  | 8 | 469,245 |
| West   | 8 | 334,601 |
| **All**| **24** | **1,178,888** |

## Method and data quality

All 24 records (R001–R024) were present, each ID appearing exactly once, split
evenly at 8 records per region. Every `amount_cents` value parsed as a valid
integer. No rows were malformed, duplicated, or otherwise required exclusion, so
the totals above cover the full dataset.

Figures were produced two ways — via the CSV summary tool and by an independent
manual re-add of the raw rows — and the two agreed exactly.

## Note on prior passes

`/shared/notes` already contained three notes from earlier jobs in this batch
(initial, verification, and third pass), all reporting these same numbers. This
pass recomputed the totals from the source data rather than copying those
figures, and the results match. The workspace itself contained no prior
`summary.json` or `report.md`, so the deliverables were written fresh here.

With four independent passes now converging, the numbers are well established
and further re-verification of this dataset is unlikely to add value.
