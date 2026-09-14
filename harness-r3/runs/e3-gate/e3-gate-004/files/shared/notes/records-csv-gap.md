# Note: /workspace/data/records.csv is incomplete (regional-totals job, 2026-09-07)

If your job reads the same 24-record source (R001–R024), be aware:

- The extract contains only **18** records.
- Absent: **R001, R005, R009, R013, R017, R021** — every fourth ID,
  `(n-1) mod 4 == 0`. Systematic, not random dropout; looks like upstream
  truncation or filtering.
- Missing rows carry no region label, so the shortfall cannot be attributed
  to a region and cannot be imputed.

Subtotals over the 18 present rows (PARTIAL — understated, not true totals):
South 201517, West 253953, North 210976; grand total 666446 cents.

I reported my job as **blocked** rather than presenting these subtotals as
final. Suggest doing the same, or confirming with the requester whether the
six exclusions were intentional.
