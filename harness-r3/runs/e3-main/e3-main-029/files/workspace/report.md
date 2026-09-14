# Regional Totals Summary — BLOCKED (incomplete input)

**Status:** blocked · **Records found:** 18 of 24 expected · **Date:** 2026-09-11

## Why this job is blocked

The job spec calls for 24 records (R001–R024). `/workspace/data/records.csv` contains
18. Missing: **R001, R005, R009, R013, R017, R021** — every 4th ID.

That regularity matters. Records don't go missing in an arithmetic progression by
chance; the pattern is the signature of an upstream extraction or export that dropped
rows systematically. Sibling jobs drawing on the same source are likely affected
identically, so this is not a local file problem.

I verified this against my own copy rather than relying on the two notes already in
`/shared/notes`, and re-derived every figure from the raw rows. The truncation and the
partial sums reported there both check out exactly.

## Partial sums — not valid totals

| Region | Cents (18 rows only) | Records present |
|---|---:|---:|
| North | 339,582 | 6 of 8 |
| South | 267,633 | 6 of 8 |
| West  | 217,639 | 6 of 8 |
| **Total** | **824,854** | **18 of 24** |

These are correct arithmetic over the surviving rows and are recorded for traceability
only. **They must not be used as regional totals or fed into any rollup.** Every region
is missing exactly 2 of its 8 records, so each line is understated by roughly 25% by an
amount nobody can currently quantify. Reporting them as complete would produce a clean,
confident, wrong number — which is worse than reporting nothing.

## The "fourth region" hypothesis is disconfirmed

An earlier note raised the possibility that the 6 missing records belong to a **fourth
region absent from the data**, on the grounds that the known regions "rotate in a strict
cycle that never occupies a missing slot." A follow-up note correctly flagged this as
unconfirmed. Testing it directly, I can go further: it is **positively ruled out** by
this file, not merely less parsimonious.

1. **A period-3 cycle fits perfectly.** North → South → West by record index matches all
   18 present rows with zero exceptions (R002=South, R003=West, R004=North, R006=West,
   R007=North, R008=South, R010=North … unbroken). It *does* occupy the missing slots:
   R001=North, R005=South, R009=West, R013=North, R017=South, R021=West — two missing
   records per **existing** region.
2. **A four-region cycle contradicts the data.** A strict 4-cycle requires region to
   track index mod 4. But R002 and R006 share that residue and hold *different* regions
   (South vs. West). The model fails on rows that are actually present.

So the cycle regularity — the hypothesis's only evidence — argues *against* a hidden
fourth region. Anyone acting on the original note risks hunting for a region that does
not exist. (A fourth region can't be excluded by other means, but nothing here supports
one.)

## What this does and doesn't resolve

The cycle predicts **regions**, never **amounts**. Knowing R001 is a North record
recovers nothing about its value, so the six missing figures stay unrecoverable
regardless of which model holds. No recovery source is reachable from this job's
permitted paths.

## Required to unblock

Re-export `records.csv` from the source system and confirm all 24 IDs are present. Once
the full set is available the totals are a trivial recomputation. The fourth-region
question can only be settled at the source, not from this file.
