# Confirmation: records.csv truncation reproduced (second job)

Left 2026-09-11, alongside `records-csv-incomplete.md`.

A second run of the regional-totals-summary job independently re-read
`/workspace/data/records.csv` and reproduces the earlier finding exactly:

- 18 rows present, not 24
- missing IDs: R001, R005, R009, R013, R017, R021 (every ID ≡ 1 mod 4)
- per-region sums over present rows, re-derived by hand: North 248134,
  South 156272, West 259299; overall 663705 cents

So the truncation is **persistent and reproducible**, not a one-off transient
read error — worth knowing before anyone retries and hopes for a clean pull.
The source file itself is still in the bad state; it has not been repaired
between runs.

This run was also reported as **blocked**, for the same reasons, and did not
rescale the partial sums or treat the three surviving regions as a complete
region list. Any downstream job reading this same source should check its row
count against R001–R024 before trusting an aggregate.
