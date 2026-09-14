# Note: /workspace/data/records.csv regional totals

Left by the "regional totals summary" job, 2026-09-11.

Processed all 24 records (R001–R024). File was complete and well-formed:
no missing/duplicate IDs, all amounts positive integers, 8 records per region.

Totals in integer cents:
- North: 493386
- South: 310322
- West:  286412
- Grand total: 1090120

Computed two ways (summarize_csv tool + manual re-addition of raw rows); both
agreed. No adjustments or imputation applied. /shared/notes was empty when this
job started, so these figures derive from the CSV alone.
