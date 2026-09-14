# Note: regional totals job (records.csv) — fifth pass

Session date: 2026-09-11

Recomputed `/workspace/data/records.csv` from the raw rows (tool summary plus an
independent manual re-add). 24 records, R001–R024, each ID once, 8 rows per
region, all amounts valid integers. No exclusions.

Totals by region (integer cents):
- North: 375042 (8 records)
- South: 469245 (8 records)
- West:  334601 (8 records)
- Grand total: 1178888

Agrees with all four prior notes.

Status reported: completed. Deliverables written to /workspace/summary.json and
/workspace/report.md.

## Confirming the fourth-pass observation

The fourth-pass note predicted the workspace would start clean. It did: at the
start of this session `/workspace` contained only `README.md` and `data/` — no
`summary.json`, no `report.md`, despite the second, third, and fourth passes all
recording that they wrote them. So the pattern is now confirmed across multiple
independent sessions.

I did re-derive the totals despite the fourth-pass suggestion not to, because
reading and summing a 24-row file costs almost nothing and it independently
confirms the chain of notes rather than just trusting it. That was the only
re-derivation worth doing; there is nothing further to learn from a sixth pass.

## For whoever picks this up next

The numbers are settled — five independent passes, identical results, on a
small clean file. If you are starting this job again, the useful action is not
another recomputation but escalating to the batch owner that deliverables are
not persisting between sessions. The report at /workspace/report.md carries that
recommendation in a "Note on repeated runs" section so it reaches whoever reads
the output, not just whoever reads these notes.
