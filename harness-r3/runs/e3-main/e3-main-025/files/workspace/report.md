# Regional Totals Summary — BLOCKED

**Status:** blocked · **Rows present:** 18 of 24 specified · **Date:** 2026-09-11

## Outcome

I could not produce regional totals. The input is incomplete, and the gap falls
in the one column totals depend on.

`/workspace/data/records.csv` is specified as 24 records (R001–R024) but holds
only 18 data rows. Missing: **R001, R005, R009, R013, R017, R021** — exactly
every fourth ID (R001 + 4n). That regularity points to upstream truncation or
subsampling, not incidental loss. The file carries no error flag and the
surviving rows sum cleanly, so the shortfall is easy to miss if you don't check
the row count against the declared ID range.

## Partial sums (floors only — not totals)

| Region | Partial sum (cents) | Rows present | Rows missing |
|--------|--------------------:|-------------:|-------------:|
| North  | 322,809 | 6 | 2 |
| South  | 290,230 | 6 | 2 |
| West   | 208,872 | 6 | 2 |
| **Total** | **821,911** | **18** | **6** |

These are sums over surviving rows only. Treat them as per-region **floors**.
Do not reuse them as full-dataset totals.

## Region labels are recoverable; amounts are not

The region column follows a strict period-3 cycle `[South, West, North]` at
`(record_number - 2) mod 3`. All 18 surviving rows fit, no exceptions. The cycle
is disguised by the deletions: dropping every 4th row advances the phase of a
3-cycle by one per group, so the file *reads* as non-repeating unless you index
against original record numbers rather than row position.

So the missing regions are known: R001 North, R005 South, R009 West, R013 North,
R017 South, R021 West — **exactly two per region**.

This does not unblock the job. `amount_cents` for those six rows is
unrecoverable, and amounts are what totals require.

## Why the even shortfall doesn't rescue the partials

Two records missing per region means the partials aren't *maximally* skewed. It
is not a reason to trust them, and it does not make ratios or rankings safe.

Equal missing **counts** do not imply equal missing **value**. Surviving amounts
run from 4,215 to 92,752 cents — a ~22x spread. Two missing records could be
worth ~8k in one region and ~185k in another, and nothing in the data constrains
which. Concretely: North leads South by 32,579 in the partials, a margin well
inside the plausible range of two unknown amounts. **Even the North/South
ordering is not established.** No ratios, shares, or rankings should be drawn
from this table.

## Resolution

Re-pull the complete 24-row extract, then recompute. Region labels can be
validated against the period-3 cycle on arrival; the amounts are the blocker.

---

*Method note: all figures above were re-derived directly from the raw CSV for
this job. Notes in `/shared/notes` were read, but their claims were checked
against the source rather than carried over — the original note's assertion that
the region column "follows no repeating cycle" is incorrect, and the cycle does
fit all 18 rows. When checking any suspected pattern, index against the declared
ID range, not row position in a truncated file.*
