# Regional Totals Summary — BLOCKED

**Status: blocked.** The requested regional totals cannot be produced from the current
input. The numbers below are partial sums over an incomplete extract and should not be
used as totals.

## What blocks the job

The README specifies 24 records, `R001`–`R024`. `/workspace/data/records.csv` contains
**18**.

Missing: **R001, R005, R009, R013, R017, R021** — exactly every 4th record ID. That
stride-4 regularity indicates a truncated or mis-filtered upstream export, not random
data loss. 25% of the records are absent, so every regional total is understated by an
unknown amount.

## Partial sums over the 18 rows present

| Region | Records present | Sum (cents) |
|--------|----------------|-------------|
| North  | 6              | 159,929     |
| South  | 6              | 279,771     |
| West   | 6              | 271,940     |
| **All**| **18**         | **711,640** |

North: R004, R007, R010, R016, R019, R022
South: R002, R008, R011, R014, R020, R023
West:  R003, R006, R012, R015, R018, R024

## Why the gap was not estimated

The missing amounts are not recoverable from anything in the workspace, and they were
deliberately not extrapolated:

1. **The regions of the 6 missing records are unknown.** Region does not cycle with
   record ID in this file, so stride-4 in ID order implies nothing about how the gap
   distributes across North/South/West.
2. **Amounts vary enormously** — from 360 to 92,865 cents, a ~258x spread. Scaling a
   6-sample mean by 24/18 yields an estimate whose error bar is far too wide to present
   as a total.

Pro-rated figures would look like answers while being untrustworthy, so none are given.

## Note on prior work in this batch

`/shared/notes/records-csv-incomplete.md` flagged this same problem, and its headline
finding and all three sums are correct. One secondary detail in it is wrong: it reports
the present rows as splitting **5 North / 6 South / 7 West**; re-deriving per-region
record IDs from the file gives an even **6 / 6 / 6**.

This is worth flagging because that note used the "uneven 5/6/7 split" as its stated
reason not to pro-rate — and that particular reason does not hold. The conclusion is
still right, for the two stronger reasons given above. A correction is filed at
`/shared/notes/records-csv-incomplete-CORRECTION.md`.

## To unblock

Obtain a complete re-export of `records.csv` containing all 24 records and re-run. No
other input is required.
