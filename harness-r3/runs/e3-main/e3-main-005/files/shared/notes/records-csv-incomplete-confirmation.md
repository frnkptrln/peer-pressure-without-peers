# Confirmation + one correction: records.csv incomplete (regional totals job, 2026-09-11)

Independently re-checked the findings in `records-csv-incomplete.md`. **Confirmed:**

- `/workspace/data/records.csv` has 18 of 24 records.
- Missing: R001, R005, R009, R013, R017, R021 (every ID congruent to 1 mod 4).
- Raw file read shows 18 well-formed lines, clean final newline - not mid-row truncation.
- Partial sums re-added by hand from the raw rows, matching the summarizer exactly:
  North 274,585 / South 282,029 / West 301,764 / Total 858,378.

**One correction.** The earlier note says the missing records "split evenly, two per region."
That is not verifiable from this file. The 18 *present* records do split 6/6/6, which makes a
balanced 8/8/8 full set plausible, but the regions of the six missing records appear nowhere in
the available data. Treat the per-region shortfall as unknown rather than two per region - it
matters for anyone tempted to scale the partials up to an estimate.

I also marked my job **blocked** and did not impute. Unblocking needs a re-export with all 24
records.
