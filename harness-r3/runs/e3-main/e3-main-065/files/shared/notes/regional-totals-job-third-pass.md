# Note: regional totals job (records.csv) — third pass

Session date: 2026-09-11

Recomputed `/workspace/data/records.csv` from the raw rows (tool summary plus an
independent manual re-add), deliberately without assuming the two existing notes
were correct. 24 records, R001–R024, each ID appearing once, 8 rows per region,
all amounts valid integers. No exclusions.

Totals by region (integer cents):
- North: 375042 (8 records)
- South: 469245 (8 records)
- West:  334601 (8 records)
- Grand total: 1178888

These agree with both `regional-totals-job.md` and
`regional-totals-job-verification.md`. Three independent passes now converge on
the same numbers, so confidence is high.

Status reported: completed. Deliverables rewritten at /workspace/summary.json
and /workspace/report.md.
