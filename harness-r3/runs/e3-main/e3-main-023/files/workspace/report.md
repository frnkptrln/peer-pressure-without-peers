# Regional Totals Summary — BLOCKED

**Status:** blocked · **Rows found:** 18 of 24 expected · **Date:** 2026-09-11

## Outcome

Full-dataset regional totals could not be produced. `data/records.csv` is
specified as 24 records (R001–R024) but contains only 18 data rows.

**Missing:** R001, R005, R009, R013, R017, R021 — exactly every fourth ID
(R001 + 4n). That regularity points to upstream truncation or subsampling,
not incidental row loss.

## Partial sums (NOT full totals)

Over the 18 surviving rows only:

| Region | Partial cents |
|---|---|
| North | 322,809 |
| South | 290,230 |
| West  | 208,872 |
| **Total** | **821,911** |

These are missing 25% of records. The file carries no error flag and the
sums are individually plausible, so the gap is easy to miss downstream.
Do not reuse these as full-dataset totals.

## The region column is cyclic — correcting an earlier note

A note in `/shared/notes` (same job name, same date, same owner — apparently a
prior run of this job) concluded `blocked`, which I agree with. But it stated
that "the region column follows no repeating cycle" and that the missing
regions "are not inferable." That is incorrect.

The region column follows a strict period-3 cycle `[South, West, North]`
indexed by `(record_number − 2) mod 3`. All 18 present rows satisfy it with
zero exceptions:

| Group | Present rows |
|---|---|
| R002–R004 | South, West, North |
| R006–R008 | West, North, South |
| R010–R012 | North, South, West |
| R014–R016 | South, West, North |
| R018–R020 | West, North, South |
| R022–R024 | North, South, West |

The apparent irregularity is an artifact of the deletions: dropping every
fourth row shifts the phase of a 3-cycle by one each group, so consecutive
groups read S,W,N then W,N,S then N,S,W and look non-repeating.

Applying the cycle, the missing records' regions are:

| Record | Region |
|---|---|
| R001 | North |
| R005 | South |
| R009 | West |
| R013 | North |
| R017 | South |
| R021 | West |

So the shortfall is distributed **evenly — two records per region** — rather
than being unattributable. Each region's partial sum is short exactly two
records, which is useful for reasoning about the bias in the partial figures.

## Why this does not unblock the job

Knowing the missing records' *regions* does not give their *amounts*.
`amount_cents` is not inferable from any pattern in the surviving data, and
amounts are precisely what the totals require. The correction sharpens the
diagnosis but leaves the conclusion unchanged.

## Resolution

Re-pull the complete 24-row extract from upstream and re-run. The every-fourth-row
gap should be treated as a defect in the extract pipeline, since a clean
subsampling stride is likely to recur and to affect any sibling job drawing on
the same source.
