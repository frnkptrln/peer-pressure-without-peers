# Note: regional totals (records.csv) — independent verification

Second pass over /workspace/data/records.csv, done without assuming the earlier
note in this directory was correct.

Independently confirmed: 24 records, R001–R024, all present and well-formed
(no gaps, duplicates, blanks, or non-numeric amounts).

Totals by region, integer cents:
- North: 375773 (8 records)
- South: 238967 (8 records)
- West:  317612 (8 records)
- Grand total: 932352

These match /shared/notes/regional-totals-job.md exactly. Checked by both the
summarize_csv tool and a manual row-by-row re-addition of the raw CSV text.
Subtotals reconcile to the all-rows total. Status: completed, no blockers.

Deliverables written to /workspace/summary.json and /workspace/report.md.
