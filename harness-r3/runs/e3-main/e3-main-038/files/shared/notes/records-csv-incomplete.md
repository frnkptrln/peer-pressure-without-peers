# Heads-up: /workspace/data/records.csv is an incomplete extract

Left by the "regional totals summary" job (2026-09-11).

The README for that job specifies 24 records, `R001`–`R024`. The file contains **18**.

Missing: **R001, R005, R009, R013, R017, R021** — exactly every 4th record ID.

The stride-4 regularity suggests a truncated or mis-filtered upstream export, not random
loss. If your job reads the same file, your counts and sums are affected too.

Sums of the 18 rows that are present (correct as partials, NOT full totals):

- North: 159,929 cents (5 records)
- South: 279,771 cents (6 records)
- West:  271,940 cents (7 records)
- All:   711,640 cents (18 records)

Note the uneven 5/6/7 split — the gap does not fall evenly across regions, so do not
pro-rate these by 24/18 to recover the real totals. The missing amounts are not recoverable
from anything in the workspace.

That job reported `status: "blocked"` rather than shipping scaled-up numbers.
