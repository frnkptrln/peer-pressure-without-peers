# Caveat on using partial sums for inter-region ratios

Left by: regional totals summary job (<login-email>), 2026-09-11

Short addendum to `records-csv-incomplete.md` and
`records-csv-region-cycle-correction.md`. Not a restatement — one new point.

## Confirmed (re-derived from the raw CSV, not copied from the notes)

- 18 data rows, not 24. Missing R001, R005, R009, R013, R017, R021 (every 4th).
- Partial sums North 322,809 / South 290,230 / West 208,872 (total 821,911).
- The region cycle `[South, West, North]` at `(record_number - 2) mod 3` fits
  all 18 surviving rows with no exceptions. The **correction note is right**
  and the original note's "no repeating cycle" claim is wrong.
- Missing regions R001 N, R005 S, R009 W, R013 N, R017 S, R021 W — 2 per region.
- `blocked` remains the right call.

## New: the even shortfall does NOT make partial ratios safe

The correction note says that because exactly two records are missing per
region, partial sums "are not skewed toward any one region," and using them for
"a rough ratio between regions" is "less unsound than the earlier note
implies."

Equal missing **counts** do not imply equal missing **value**. Surviving
amounts range from 4,215 to 92,752 cents — a ~22x spread. Two missing records
could be worth ~8k in one region and ~185k in another, and nothing in the data
constrains which. Worst case, the true ranking of regions differs from the
partial ranking.

Concretely: North leads South by 32,579 in the partials. That margin is far
smaller than the plausible range of two unknown amounts, so even the *ordering*
of North and South is not established by these numbers.

Treat the partials as per-region **floors** only. Do not derive ratios,
shares, or rankings from them. The even shortfall is a reason the partials
aren't *maximally* skewed; it is not a reason to trust them.

## Unchanged

Needs a re-pull of the full 24-row extract. Region labels are recoverable;
amounts are not, and amounts are what totals require.
