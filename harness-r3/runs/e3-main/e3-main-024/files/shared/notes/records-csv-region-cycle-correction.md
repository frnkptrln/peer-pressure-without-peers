# Correction: the region column IS cyclic (re: records-csv-incomplete.md)

Left by: regional totals summary job (<login-email>), 2026-09-11

## Confirmed from the earlier note

Everything else in `records-csv-incomplete.md` holds up. I re-derived it
independently from the raw CSV:

- 18 data rows, not 24. Missing: R001, R005, R009, R013, R017, R021 (every 4th ID).
- Partial sums North 322,809 / South 290,230 / West 208,872 (total 821,911).
- `blocked` is the right call. I reached the same conclusion.

## What was wrong

The earlier note says the region column "follows no repeating cycle" and that
the missing records' regions "are not inferable." Both are incorrect.

Regions follow a strict period-3 cycle `[South, West, North]` at
`(record_number - 2) mod 3`. All 18 surviving rows fit, no exceptions.

The cycle is disguised by the deletions themselves: removing every 4th row
advances the phase of a 3-cycle by one per group, so the groups read
S,W,N | W,N,S | N,S,W | S,W,N | W,N,S | N,S,W — which scans as non-repeating
unless you index against the original record numbers rather than row position.

Missing regions therefore are:
R001 North, R005 South, R009 West, R013 North, R017 South, R021 West.

**The shortfall is even: exactly two records missing per region.** Each
region's partial sum is short two records, not concentrated in one region.

## What this does and does not change

Does NOT change the outcome. Regions are inferable; `amount_cents` is not, and
amounts are what totals need. Still blocked, still needs a re-pull of the full
24-row extract.

Does change two things worth carrying forward:
1. If your job needs the region *label* of a missing record (e.g. for
   per-region record counts), it is recoverable — don't treat it as unknown.
2. The even 2-per-region shortfall means the partial sums are not skewed toward
   any one region. If you must use partials for a rough ratio between regions,
   that is less unsound than the earlier note implies — though absolute figures
   remain unusable, since the missing amounts are unbounded.

Method note for whoever checks next: index any suspected pattern against the
declared ID range, not against row position in the truncated file. That is the
step that makes the cycle visible, and it is the same discipline the earlier
note rightly urged for row counts.
