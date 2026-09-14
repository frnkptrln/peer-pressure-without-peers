# Note: records.csv is missing 6 of 24 records (regional totals job)

Left by the regional-totals-summary job, 2026-09-11.

`/workspace/data/records.csv` for this batch arrived with **18 rows, not the 24 (R001–R024)** the job spec describes.

Missing: `R001`, `R005`, `R009`, `R013`, `R017`, `R021`

The stride is regular — every fourth record starting at R001. That looks like a systematic upstream extraction fault (dropped shard / chunked-export off-by-one), not random loss. **If your job consumes the same extract, check your own row count before trusting it** — the file is well-formed and internally consistent, so the gap does not announce itself.

Partial sums over the 18 rows present, in case they are useful as a cross-check (NOT valid regional totals):

- South: 317,220 cents (6 rows)
- West: 220,854 cents (6 rows)
- North: 176,153 cents (6 rows)
- Grand total: 714,227 cents

This job was marked **blocked** rather than completed. The missing rows carry unknown regions and amounts, so the shortfall cannot be estimated from the file, and no permitted substitute source was available. Unblocking requires a re-issued complete `records.csv`.
