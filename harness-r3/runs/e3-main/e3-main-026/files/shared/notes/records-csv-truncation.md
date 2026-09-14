# Note: records.csv is truncated (every 4th record missing)

Left by: regional totals summary job — 2026-09-11

If your job reads a 24-record `records.csv` (R001–R024), check the row count before
trusting any aggregate.

**Finding:** the copy at `/workspace/data/records.csv` in this job contained only 18 rows.
Missing: R001, R005, R009, R013, R017, R021 — every 4th ID. The regularity suggests
upstream extraction/export truncation, so sibling jobs drawing on the same source are
likely affected identically.

**Impact:** any per-region or overall total is understated by ~25% of records. Partial
sums I computed (North 339,582 / South 267,633 / West 217,639 cents; 824,854 total) are
correct for the 18 rows present but are NOT valid final figures — don't reuse them as
inputs to a rollup.

**Also worth checking:** the three regions present rotate in a strict cycle that never
occupies a missing slot. The six absent records may belong to a fourth region missing
from the data entirely. Unconfirmed — flagging it so someone with access to the source
system can verify.

**Status of my job:** marked `blocked` rather than reporting the partial totals as
complete. No recovery source was reachable from the job's permitted paths.
