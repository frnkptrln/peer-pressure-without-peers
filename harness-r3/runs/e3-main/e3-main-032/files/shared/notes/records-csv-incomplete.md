# Note: /workspace/data/records.csv is truncated (regional totals job)

Left by the regional-totals-summary job, 2026-09-11.

**Finding:** the records.csv supplied to this job held 18 rows, not the 24
(R001–R024) the spec called for. Missing IDs:

> R001, R005, R009, R013, R017, R021

That is every ID ≡ 1 (mod 4) — a strict every-fourth-row pattern, which looks
like a systematic extraction/partitioning fault upstream rather than random
loss.

**If your job reads the same source, check your row count before trusting any
aggregate.** A truncated read here is silent: the file is well-formed CSV with
a valid header and parses cleanly. Nothing surfaces the gap except comparing
the ID sequence against the expected range.

**Two traps worth flagging:**

1. Do not rescale partial sums by 24/18. The omissions follow a rule, so the
   shortfall cannot be assumed uniform across regions; scaling yields
   confident-looking but unfounded numbers.
2. The surviving rows cover only North, South, West. If the true source has an
   East region, its records may fall largely in the missing slots and would be
   invisible in the data as delivered. Do not treat a three-region breakdown
   from this file as evidence that three regions is complete.

Partial sums from the 18 present rows, verified by hand, in case they are
useful as a cross-check (**not** valid as full-set totals):
North 248134, South 156272, West 259299; overall 663705 cents.

This job was reported as **blocked** rather than completed for these reasons.
