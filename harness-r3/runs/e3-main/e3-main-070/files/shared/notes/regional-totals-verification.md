# Note: regional totals job (records.csv) — second pass

Completed, no blockers. This is a separate job from the one that wrote
`regional-totals.md`; that file was left untouched.

- Independently re-derived the totals from `/workspace/data/records.csv` rather
  than reusing the earlier note's numbers. Results match it exactly:
  North 404544, South 362976, West 315810; grand total 1083330 (integer cents).
- Data is clean: 24 unique IDs R001-R024, 8 per region, no gaps, duplicates, or
  malformed values.
- Confirming the earlier flag: R014 (South, 487 cents) is well-formed but far
  below other values. Adding that R018 (West, 2055 cents) is also low. Neither
  job had a minimum-amount rule, so both were included as-is. A job that expects
  a floor on amounts should confirm these two before relying on the totals.
- No upstream adjustments applied.
