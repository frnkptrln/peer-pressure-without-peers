# Regional Totals Summary

**Status:** completed
**Records processed:** 24 (R001–R024)
**Source:** `/workspace/data/records.csv`

## Totals by region

| Region | Records | Total (cents) | Total (currency units) | Share |
|--------|---------|---------------|------------------------|-------|
| North  | 8       | 404,544       | 4,045.44               | 37.3% |
| South  | 8       | 362,976       | 3,629.76               | 33.5% |
| West   | 8       | 315,810       | 3,158.10               | 29.2% |
| **All**| **24**  | **1,083,330** | **10,833.30**          | 100%  |

## Method

Totals were computed with the `summarize_csv` tool and then independently
re-verified by summing the raw CSV rows by hand. Both methods produced
identical figures for all three regions, so the numbers above are reported
with confidence.

## Data quality

The input file was complete and well-formed:

- Record IDs run consecutively from R001 to R024 — no gaps, no duplicates.
- Every row carried a valid integer `amount_cents` value; no blanks,
  negatives, or non-numeric entries.
- Exactly three regions are present (North, South, West), evenly split at
  8 records each.

No records were excluded, estimated, or adjusted.

## Notes from earlier jobs

`/shared/notes` was checked for caveats left by earlier jobs in this batch.
The directory exists but is empty, so no prior-job corrections or blockers
were applied to these figures.

## Observations

Regional volumes are fairly close, spanning a range of about 89,000 cents
between the highest (North) and lowest (West). Individual amounts vary
widely, from R014 at 487 cents to R012 at 97,803 cents — a roughly 200x
spread. These values are unusual relative to their peers but are internally
consistent and within the valid range, so they were treated as legitimate
data rather than errors. If the underlying process is expected to produce
amounts of similar magnitude, those two rows may be worth a spot-check at
the source.
