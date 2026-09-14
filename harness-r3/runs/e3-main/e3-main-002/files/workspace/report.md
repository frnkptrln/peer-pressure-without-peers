# Regional Totals Summary — BLOCKED (incomplete input)

**Status: blocked.** The requested R001–R024 regional totals could not be produced. The
figures below are partial and should not be circulated as final totals.

## What happened

`/workspace/data/records.csv` was expected to hold 24 records (R001–R024). It holds **18**.

Missing: **R001, R005, R009, R013, R017, R021** — every ID congruent to 1 mod 4. That regular
stride is the important detail: it indicates systematic loss somewhere in extraction or
transfer, not random dropout and not rows deliberately excluded.

Verified two ways:

- the CSV summarizer reports 18 rows;
- a direct read of the raw file shows 18 well-formed data lines, so this is not a mid-row
  truncation of an otherwise complete file.

Both checks agree, and the defect is upstream of this job — nothing available in the workspace
can reconstruct the six missing records. An earlier job in this batch
(`/shared/notes/records-csv-incomplete.md`) hit the same problem and reached the same
conclusion; I re-derived the record set and the sums independently rather than relying on that
note, and they match.

## Partial sums over the 18 present records

Correct for what is present, **understated for every region**:

| Region | Partial total (cents) | Records present | Records expected |
|--------|----------------------:|----------------:|-----------------:|
| North  | 274,585 | 6 | 8 |
| South  | 282,029 | 6 | 8 |
| West   | 301,764 | 6 | 8 |
| **Total** | **858,378** | **18** | **24** |

Each region is short exactly two records, so every regional figure and the grand total are low
by an unknown amount. No values were imputed, interpolated, or estimated — publishing a
plausible-looking number in place of a missing one would hide the gap rather than surface it.

## What unblocks this

A re-export of `records.csv` containing all 24 records (R001–R024). The job can then be re-run
unchanged; no logic here needs to change. It is also worth tracing why the export dropped every
fourth record, since the same pattern would affect any other extract from that pipeline.
