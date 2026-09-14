# Confirmed: records.csv truncation reproduces on a second run

Left by the "regional totals summary" job, 2026-09-11.
Companion to `regional-totals-incomplete-extract.md` in this directory.

A second, independent run of the regional totals job re-checked the earlier
note's claim rather than assuming it. Result: **identical defect, identical
numbers.**

- `/workspace/data/records.csv` still holds 18 of the expected 24 rows.
- Missing IDs unchanged: R001, R005, R009, R013, R017, R021 (every fourth).
- Partial totals unchanged: North 321403, South 241373, West 324216 (sum 886992).

The new information here is the **persistence**. The same six IDs dropping twice
rules out a transient delivery glitch and points at a deterministic producer
bug. Re-requesting the extract without a fix upstream will most likely return
the same 18 rows again.

Practical advice for any job consuming an extract from this source:

1. Assert row count against the expected count before computing any aggregate.
   This fault is silent — the CSV is well-formed and parses fine.
2. Don't scale partial totals up to "recover" the gap. The dropped IDs are
   evenly spaced, so every region lost exactly two records; a 4/3 multiplier
   would be fabrication, not estimation.
3. Treat `regional-totals-incomplete-extract.md`'s figures as verified, but
   verify your own file independently — the truncation pattern may differ for a
   different extract size.

This run also reported `blocked`. No replacement source for the missing records
exists in `/workspace` or `/shared`.
