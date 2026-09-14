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

---

## Re-verified on a later pass (2026-09-11)

A subsequent run of this same job re-read the CSV from scratch and independently
reproduced everything above: same 18 record IDs, same 6 missing IDs, same
per-region sums and grand total. So this is a stable property of the export, not
a one-off read error.

Still no replacement data — `/shared` contains only this `notes/` directory.
That run also concluded **blocked**. Fix remains: re-run the upstream export.

---

## Third pass, same result (2026-09-11)

A third run re-read the raw CSV and re-added the per-region sums by hand: same 18
IDs, same 6 missing, same totals. `/shared` still holds only this `notes/` file —
no backfill has appeared. Also **blocked**. Nothing new to add; the export itself
still needs to be re-run upstream.
