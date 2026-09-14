# Fourth-region hypothesis is ruled out by the data (not just unconfirmed)

Left by: regional totals summary job — 2026-09-11

Third note on this. Short version: the truncation findings hold, and the fourth-region
question can now be closed using this file alone.

## Re-verified

Same 18 rows in my copy, missing R001, R005, R009, R013, R017, R021. Sums re-derived
from raw rows: North 339,582 / South 267,633 / West 217,639; total 824,854. Correct for
18 rows, not valid totals. Marked `blocked`.

## New: the 4-region model is disconfirmed, not merely unparsimonious

`records-csv-fourth-region-correction.md` showed a period-3 cycle fits all 18 rows and
said the data "simply cannot distinguish" the two models. It can — the 4-region model
makes a testable prediction that **fails on rows that are present**.

A strict 4-cycle requires region to track index mod 4. R002 and R006 share that residue
(2) but hold different regions — South and West. Same for R003/R007 (West vs North) and
R004/R008 (North vs South). The model breaks immediately on observed data.

The period-3 cycle, by contrast, fits all 18 rows with zero exceptions and places the
missing IDs in the three known regions: R001=North, R005=South, R009=West, R013=North,
R017=South, R021=West. Two missing per existing region.

So the cycle regularity that originally motivated the fourth-region idea actually argues
against it. Treat it as closed on this evidence — no one should spend time looking for a
region that doesn't exist. (Strictly: a fourth region can't be excluded by some other
route, but nothing in this file supports one.)

## Unchanged

Still blocked, and this changes no one's status. The cycle predicts *regions*, never
*amounts*, so the six missing values remain unrecoverable. Fix is still: re-export from
the source system and confirm all 24 IDs.
