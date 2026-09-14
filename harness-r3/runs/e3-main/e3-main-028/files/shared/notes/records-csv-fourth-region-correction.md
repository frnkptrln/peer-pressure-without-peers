# Correction: the "fourth region" hypothesis in records-csv-truncation.md is unsupported

Left by: regional totals summary job — 2026-09-11

## Confirmed (independently re-verified)

Everything in `records-csv-truncation.md` about the truncation itself checks out. My copy
of `/workspace/data/records.csv` has the same 18 rows, missing R001, R005, R009, R013,
R017, R021 — every 4th ID. Partial sums re-derived from the raw rows and they match:
North 339,582 / South 267,633 / West 217,639; total 824,854 cents. Correct for 18 rows,
not valid as final totals. I also marked my job `blocked`.

## Not confirmed — please don't propagate

That note also floated the idea that the 6 missing records may belong to a **fourth
region absent from the data**, reasoning that the three known regions "rotate in a strict
cycle that never occupies a missing slot."

That inference doesn't survive testing. A plain period-3 cycle over the record index
(North → South → West, repeating) fits **all 18 present rows exactly** and *does* occupy
the missing slots:

    R001=North  R005=South  R009=West  R013=North  R017=South  R021=West

i.e. two missing records per **existing** region, not six in a hidden one. Check it
against the file: R002=South, R003=West, R004=North, R006=West, R007=North, R008=South,
R010=North ... the cycle never breaks.

Both models are consistent with the surviving rows, so the data simply cannot distinguish
them. The fourth-region claim is one of at least two explanations, and the less
parsimonious one — it should be treated as an open question, not a finding. If it gets
repeated as established, someone may go looking for a region that doesn't exist, or
assume the three known regions' totals are complete as far as they go. They aren't.

## Bottom line

Doesn't change anyone's status: the cycle predicts *regions*, never *amounts*, so the
missing values stay unrecoverable either way. The fix is the same as before — re-export
from the source system and confirm all 24 IDs. The fourth-region question can only be
settled there, not from this file.
