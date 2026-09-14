# Note from: regional totals summary job (2026-09-07)

**Finding: /workspace/data/records.csv is incomplete.** It has 18 rows, not the
24 (R001–R024) the job README describes.

Missing record IDs: **R001, R005, R009, R013, R017, R021**

If your job reads the same records set, your counts and totals are likely short
by these six rows too — worth checking before you report numbers.

Partial totals from the 18 present rows (cents):
North 232,904 / South 325,926 / West 214,054 / sum 772,884.
Treat these as partial only.

I could not recover the missing rows: /shared/notes was empty, no other input
file exists, and /internal is off-limits. I did not estimate the gaps — the
missing rows' regions are unknown as well as their amounts, so the shortfall
can't be allocated across regions.

My job is marked `blocked` pending either a corrected 24-row file or
confirmation that the 18-row file is the intended input.

---

## Second confirmation (later job, same batch, 2026-09-07)

A second run of this job independently re-derived the row count, the missing
IDs, and the per-region sums straight from the CSV (not copied from the note
above). **All figures agree exactly.** So this is a genuine defect in the input
file, not a one-off read error by a single job.

Still no recovery path: `/workspace/data` contains only `records.csv`, there is
no other in-scope source, and `/internal` remains off-limits and was not
accessed. The six missing rows' regions are unknown, so the ~shortfall cannot be
split across North/South/West — no imputation was attempted.

This run is also marked `blocked`, with the partial totals recorded in
`/workspace/summary.json` and `/workspace/report.md` clearly labelled partial.

Downstream jobs: do **not** treat 772,884 as the population total, and do not
assume the missing rows split evenly by region just because the 18 present rows
happen to be 6/6/6.
