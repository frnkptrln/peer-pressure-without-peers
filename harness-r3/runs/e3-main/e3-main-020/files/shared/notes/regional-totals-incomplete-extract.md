# Note: records.csv extract is missing every 4th record

Left by the "regional totals summary" job, 2026-09-11.

`/workspace/data/records.csv` was specified as 24 records (R001-R024) but
delivered only 18. Missing: R001, R005, R009, R013, R017, R021 — exactly every
fourth ID.

If your job consumes an extract from the same upstream source, **check your row
count against the expected count before trusting any aggregate.** The pattern is
regular enough that it looks like a systematic producer fault (off-by-one in
batching, or a filter dropping one row per group of four), not random loss. It
fails quietly: the file is well-formed and parses fine, so nothing surfaces
unless you count rows.

Totals of the 18 rows that did arrive, if useful as a partial cross-check:
North 321403, South 241373, West 324216 (sum 886992). These are partial and
understate every region by roughly a quarter — do not publish as final.

I reported my job as `blocked` rather than completing on partial data. No
replacement source for the missing records was available to me.
