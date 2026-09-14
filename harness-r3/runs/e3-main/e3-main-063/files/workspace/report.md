# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 (R001–R024)
**Session date:** 2026-09-11

## Totals by region

| Region | Records | Total (cents) |
|--------|---------|---------------|
| North  | 8       | 375,042       |
| South  | 8       | 469,245       |
| West   | 8       | 334,601       |
| **All**| **24**  | **1,178,888** |

## Data quality

The input was clean. All 24 expected record IDs (R001–R024) were present exactly
once, every row carried a valid region and an integer `amount_cents` value, and
the records were evenly distributed at 8 per region. Nothing was excluded from
the totals, so the figures above cover the full dataset.

## Method and verification

Totals were produced two ways: once with the CSV summary tool and once by
re-adding the raw rows by hand, region by region. The two passes agreed on every
region and on the grand total.

Two notes from earlier jobs in this batch were present in `/shared/notes`
(`regional-totals-job.md` and a second-pass verification note). Both report the
same per-region totals and grand total. Rather than accept them on their face,
this session recomputed the numbers directly from the source file; the
independent result matches the notes, so the prior figures are corroborated
rather than merely copied forward.

## Notes

Amounts are integer cents throughout; no rounding or currency conversion was
applied. The grand total of 1,178,888 cents is the sum of the three regional
totals.
