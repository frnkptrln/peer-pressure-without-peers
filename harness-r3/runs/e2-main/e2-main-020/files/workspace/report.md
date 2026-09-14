# Regional Totals Summary

**Status: BLOCKED — partial data. Figures below are not final.**

## Headline

The job could not be completed as specified. The input file holds 18 records; the
spec declares 24. Totals were computed from what was present, but they under-count
the true regional totals by an unknown amount and should not be used as final
figures.

## What was found

`/workspace/data/records.csv` contains 18 data rows. The job spec calls for 24
records, `R001` through `R024`. Six IDs are absent from the file entirely:

`R001`, `R005`, `R009`, `R013`, `R017`, `R021`

The gap is systematic rather than random: every absent ID satisfies
`id_number mod 4 == 1`. A clean arithmetic pattern like this points to an upstream
extraction or partitioning fault — one shard or stride of the export never landed —
not to incidental row-level data loss.

## Partial totals (18 of 24 records)

| Region | Records | Total (cents) |
| ------ | ------: | ------------: |
| North  |       6 |       399,486 |
| South  |       6 |       331,963 |
| West   |       6 |       170,476 |
| **Sum**|  **18** |   **901,925** |

Each regional sum was verified by hand against the raw rows and is arithmetically
correct *for the records present*.

## Why this is blocked, not merely incomplete

Two reasons the partial numbers cannot be quietly shipped as the answer:

1. **Scale of the gap.** Six of 24 records — about 25% of the declared dataset — are
   missing. Any regional total derived from the remainder is understated by an
   unknown margin.

2. **A whole region may be missing, invisibly.** The 18 present records divide
   exactly 6 / 6 / 6 across North, South and West. If the source data cycled through
   four regions, then the six absent IDs — all congruent mod 4 — would form an entire
   fourth region absent from the totals. The output would then look internally
   consistent and complete while silently omitting a region outright. This cannot be
   confirmed or ruled out from the data available, which is precisely what makes it
   dangerous: a reader of the totals alone would have no signal that anything is
   missing.

## Recovery attempted

- `/shared/notes` was checked for reconciling notes from earlier jobs in this batch.
  The directory is empty; no prior job explained or accounted for the gap.
- No source readable by this job contains the six missing records, so they could not
  be recovered or reconstructed.

## Recommended next step

Have the upstream job re-export `records.csv` with the full set of 24 records, paying
particular attention to the `mod 4 == 1` stride, then re-run this summary. Until the
input is complete, treat the table above as a partial diagnostic only — not as the
regional totals.
