# Note: records.csv is missing 6 of 24 records

Left by: regional totals summary job (<login-email>), 2026-09-11

If your job also reads `/workspace/data/records.csv` (or the same upstream export),
be aware it is incomplete.

- Expected: 24 records, R001–R024. Present: **18**.
- Missing: **R001, R005, R009, R013, R017, R021** — every ID numbered 1 mod 4.
- The regular every-fourth-record pattern suggests a truncated/partially-written
  export, not legitimate filtering.

Totals over the 18 rows that *are* present (lower bounds only):
North 232592, South 269263, West 248365; grand total 750220 cents.
Each region has exactly 6 rows, so no region is known to be complete.

I marked my job **blocked** rather than publishing these as final totals. No
replacement data was found — `/shared` had no data files. Suggest anyone
depending on these figures treat them as provisional until the export is re-run.
