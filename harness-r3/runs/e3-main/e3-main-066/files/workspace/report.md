# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 expected (R001–R024)

## Totals by region

| Region | Records | Total (cents) | Total (USD) |
| ------ | ------: | ------------: | ----------: |
| North  |       8 |       404,544 |    $4,045.44 |
| South  |       8 |       362,976 |    $3,629.76 |
| West   |       8 |       315,810 |    $3,158.10 |
| **All**|  **24** | **1,083,330** |**$10,833.30**|

## Method and checks

Totals were produced by summing `amount_cents` per `region`, keeping all
arithmetic in integer cents to avoid floating-point rounding.

The following checks passed:

- **Completeness** — all 24 expected record IDs R001–R024 are present, with
  no gaps and no duplicates.
- **Well-formed values** — every row has a non-empty region and an integer
  amount; no blanks, negatives, or unparseable fields.
- **Region coverage** — exactly three regions appear (North, South, West),
  evenly split at 8 records each.
- **Independent recomputation** — the per-region sums were recalculated by
  hand from the raw CSV text and matched the tooling output exactly, so the
  figures do not rest on a single code path.

## Notes

`/shared/notes` was empty, so there were no constraints, corrections, or
caveats from earlier jobs in this batch to carry forward. Nothing in the
input was ambiguous, and no records were excluded or adjusted — the totals
above cover the full dataset as delivered.

The smallest value in the set is R014 (South, 487 cents); it is an outlier
in magnitude but is a valid record and is included in the South total.
