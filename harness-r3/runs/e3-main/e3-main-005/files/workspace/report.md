# Regional Totals Summary - BLOCKED (incomplete input)

**Status: blocked.** Final R001-R024 regional totals cannot be produced from the current input.
The numbers below are partial sums and should not be forwarded as the regional totals.

## What is wrong

`/workspace/data/records.csv` contains **18 of the expected 24 records**.

Missing: **R001, R005, R009, R013, R017, R021** - every ID congruent to 1 mod 4. The regular
stride points to systematic loss in extraction or transfer, not random dropout or deliberately
excluded rows.

The file is not damaged in a way a re-read would fix: it holds 18 complete, well-formed data
rows and ends with a clean newline, so this is a missing-rows problem, not a mid-row truncation.

## Verification

Checked three independent ways, all in agreement:

1. The CSV summarizer reports 18 rows.
2. A direct read of the raw file shows 18 data lines.
3. Each region's amounts were re-added by hand from the raw rows, matching the summarizer exactly.

## Partial sums (18 present records - NOT the answer)

| Region | Partial (cents) | Records present |
|--------|----------------:|----------------:|
| North  |         274,585 |               6 |
| South  |         282,029 |               6 |
| West   |         301,764 |               6 |
| **Total** |  **858,378** |          **18** |

These are correct for the records that are present, and **understated for every region** by an
unknown amount.

## Why no estimate is given

The six missing records leave no trace in the file - their regions appear nowhere in the
available data - so the shortfall per region is **unknown**. The 18 present records do split
6/6/6, which makes a balanced 8/8/8 full set plausible, but that is an inference about rows we
cannot see, not an observation. It is not a sound basis for scaling these partials into an
estimate, so nothing was imputed and no estimated totals are reported.

## What would unblock this

A re-export of `records.csv` with all 24 records (R001-R024). The totals can then be computed
directly, with no change to method - the partial sums above already validate the arithmetic.

## Consistency with other jobs

Two earlier jobs in this batch investigated the same file and reached the same finding, and both
marked themselves blocked rather than shipping partial numbers as final
(`/shared/notes/records-csv-incomplete.md`, `records-csv-incomplete-confirmation.md`). I
re-verified from the raw data rather than relying on those notes; my figures match theirs. I also
concur with the correction in the second note: the earlier claim that the missing records "split
evenly, two per region" is not verifiable from this file, and the per-region shortfall should be
treated as unknown.
