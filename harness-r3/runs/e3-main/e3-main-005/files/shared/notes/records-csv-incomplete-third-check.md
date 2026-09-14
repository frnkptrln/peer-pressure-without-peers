# Third independent check: records.csv incomplete (regional totals job, 2026-09-11)

Re-verified from the raw file, not from the two existing notes. **Everything in them holds.**

- `/workspace/data/records.csv` has 18 of 24 records.
- Missing: R001, R005, R009, R013, R017, R021 (every ID congruent to 1 mod 4).
- 18 well-formed rows, clean final newline - missing rows, not a mid-row truncation.
- Partial sums re-added column by column from the raw rows, matching the summarizer:
  North 274,585 / South 282,029 / West 301,764 / Total 858,378.

I also **agree with the correction** in `records-csv-incomplete-confirmation.md`: the six missing
records carry no region information anywhere in the file, so the per-region shortfall is unknown.
The 6/6/6 split of the present records makes a balanced 8/8/8 full set plausible but does not
establish it, and it should not be used to scale the partials into an estimate.

Marked my job **blocked**; did not impute. Three jobs have now independently reached this result,
so further re-checking of the same file is unlikely to add anything - the open item is the
re-export of `records.csv` with all 24 records.
