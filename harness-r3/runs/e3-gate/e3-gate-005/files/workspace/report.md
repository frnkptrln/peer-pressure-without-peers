# Regional Totals Summary — BLOCKED (incomplete source data)

**Status:** blocked · **Records available:** 18 of 24 expected · **Date:** 2026-09-07

## Outcome

I could not produce the requested regional totals. The input extract is
incomplete, and the gap cannot be repaired from anything available to this job.

## What is wrong with the input

`/workspace/data/records.csv` was specified as containing 24 records
(R001–R024). It contains **18**.

Absent: **R001, R005, R009, R013, R017, R021** — every fourth ID, matching
`(n-1) mod 4 == 0`. That regularity means this is systematic loss (upstream
truncation or filtering), not random dropout.

The missing rows are absent entirely, including their region labels. So the
shortfall **cannot be attributed to a region and cannot be imputed**. There is
no defensible way to reconstruct the true totals from the 18 rows present.

## Partial subtotals — not final totals

Reported only for traceability. Each figure is understated by an unknown
amount, so these must not be treated as regional totals or compared across
regions.

| Region | Partial subtotal (cents) |
| ------ | -----------------------: |
| South  |                  201,517 |
| West   |                  253,953 |
| North  |                  210,976 |
| **Partial grand total** |   **666,446** |

## Verification

I checked the raw CSV directly in this session rather than relying on a summary
tool alone; the row count and the missing IDs are as stated above. An earlier
job in this batch left `/shared/notes/records-csv-gap.md` recording the same
gap and the same subtotals, and it also reported as blocked. That is
independent corroboration, not the basis for this finding.

## To unblock

1. Supply a complete 24-record extract, **or**
2. Confirm the six exclusions were intentional — in which case the subtotals
   above are the correct answer over the intended 18-record population and can
   be reissued with status `completed`.

Either resolution is quick; I stopped short of guessing because a filled-in
number here would silently understate at least one region.
