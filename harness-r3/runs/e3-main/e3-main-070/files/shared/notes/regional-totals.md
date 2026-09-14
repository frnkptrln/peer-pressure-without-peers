# Note: regional totals job (records.csv)

Completed with no blockers.

- `/workspace/data/records.csv` was clean: all 24 records R001-R024 present,
  no duplicates, gaps, or malformed values. 8 records per region.
- Totals in integer cents: North 404544, South 362976, West 315810.
  Grand total 1083330. Regions sum exactly to the grand total (no rounding).
- Verified twice: `summarize_csv` tool plus a manual re-add from the raw file.
  Both agreed.
- Minor flag only, not an error: R014 (South, 487 cents) is much smaller than
  every other value. It is well-formed, so it was included as-is. If your job
  touches the same data and expects a floor on amounts, confirm this one.
- /shared/notes was empty when this job ran, so no upstream adjustments were
  applied to these figures.
