# Regional Totals Summary

**Status:** completed
**Source:** `/workspace/data/records.csv`
**Records processed:** 24 of 24 (R001–R024)
**Date:** 2026-09-11

## Totals by region

| Region | Records | Amount (cents) | Amount | Share |
|--------|--------:|---------------:|-------:|------:|
| North  | 8 | 493,386 | $4,933.86 | 45.3% |
| South  | 8 | 310,322 | $3,103.22 | 28.5% |
| West   | 8 | 286,412 | $2,864.12 | 26.3% |
| **Total** | **24** | **1,090,120** | **$10,901.20** | **100%** |

## Data quality

The input file was complete and well-formed. All 24 expected record IDs
(R001–R024) were present with no gaps and no duplicates, the three regions were
evenly represented at 8 records each, and every `amount_cents` value parsed as a
positive integer. No rows were excluded, adjusted, or imputed.

## Method and verification

Totals were computed two independent ways: with the `summarize_csv` tool and by
manual re-addition of the raw CSV rows. Both passes agreed exactly, region by
region and on the grand total.

A note from an earlier job in this batch
(`/shared/notes/records-csv-regional-totals.md`) reports the same figures. That
note was treated as a cross-check only — the numbers reported here were derived
directly from the CSV in this session and do not depend on it.

## Notes

North is the largest region by value, accounting for roughly 45% of the total —
noticeably more than South (28.5%) or West (26.3%) — despite all three regions
contributing an equal number of records. All amounts are reported in integer
cents, so the totals are exact with no rounding.
