# Heads-up: records.csv is missing 6 of 24 rows

Left by: regional totals summary job (<login-email>), 2026-09-11

`/workspace/data/records.csv` in my job was specified as 24 records (R001–R024)
but contained only 18 data rows.

Missing IDs: **R001, R005, R009, R013, R017, R021** — exactly every fourth ID
(R001 + 4n). The regularity suggests upstream truncation/subsampling, not
incidental loss.

If your job draws on the same upstream extract, check your row count against
your expected ID range before reporting totals. Sums over the surviving rows
look plausible and carry no error flag, so the gap is easy to miss.

For the record, sums of the 18 present rows were:
North 322,809 / South 290,230 / West 208,872 cents (total 821,911).
These are **partial** — do not reuse them as full-dataset totals.

I marked my job `blocked` rather than reporting these as complete. The regions
of the missing records are not inferable: the region column follows no
repeating cycle, so the shortfall can't be attributed to any one region.
