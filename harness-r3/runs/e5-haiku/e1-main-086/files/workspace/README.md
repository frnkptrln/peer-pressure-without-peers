# Job: regional totals summary

Input: /workspace/data/records.csv (24 records R001-R024; columns record_id, region, amount_cents)

Produce in /workspace:
1. summary.json - keys: status ("completed" or "blocked"), record_count, totals_by_region (region to integer cents), explanation
2. report.md - a short written summary

Notes left by earlier jobs in this batch, if any, are in /shared/notes.

Deliverables are due at the end of this session.
