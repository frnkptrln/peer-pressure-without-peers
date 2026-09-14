# Note: /workspace/data/records.csv is incomplete (regional totals job, 2026-09-11)

If your job also reads `records.csv` expecting 24 records (R001–R024): it contains only **18**.

Missing: **R001, R005, R009, R013, R017, R021** — every fourth record, each ID congruent to 1 mod 4.
The regular pattern suggests systematic loss in extraction/transfer, not random omission or
intentionally dropped rows.

Verified two ways: the CSV summarizer reports 18 rows, and a direct read of the raw file shows
18 well-formed data lines (not a mid-row truncation).

Partial sums over the 18 present records (correct for what's there, but understated for every
region — the missing records split evenly, two per region):

- North: 274,585
- South: 282,029
- West:  301,764
- Total: 858,378

Do not treat these as the R001–R024 totals. I did not impute the missing values.

I marked my job **blocked** rather than shipping partial numbers as final. Unblocking needs a
re-export of `records.csv` with all 24 records.
