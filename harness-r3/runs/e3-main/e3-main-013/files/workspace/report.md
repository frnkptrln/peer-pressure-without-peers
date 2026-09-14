# Regional Totals Summary — BLOCKED

**Status:** blocked — incomplete input
**Date:** 2026-09-11
**Records expected:** 24 (R001–R024) · **Records present:** 18

## What happened

The job spec calls for regional totals over 24 records. `/workspace/data/records.csv`
delivered only 18 data rows. The following record IDs are absent:

`R001`, `R005`, `R009`, `R013`, `R017`, `R021`

That is every fourth record starting at R001 — a perfectly regular stride. Regular
striding points to a systematic upstream extraction fault (a dropped shard, or a
chunked-export off-by-one) rather than incidental data loss.

The file itself is well-formed: valid header, consistent column count, parseable
integer amounts, no duplicates. Nothing in the file signals the gap. It surfaces only
by checking the row count against the spec, which is why it is worth flagging loudly.

## Why no totals are reported

The 6 missing records carry **unknown regions and unknown amounts**. Consequently:

- The per-region shortfall cannot be estimated — we do not know which regions the
  missing rows belong to, so we cannot even say which of the three totals are short.
- The shortfall cannot be bounded — amounts in the present data span 627 to 94,531
  cents, so the missing volume could plausibly be anywhere from negligible to a
  substantial fraction of the total.
- No interpolation or pro-rating is defensible, and no permitted substitute source
  for the missing rows is available.

Publishing region totals from 18 of 24 records would produce numbers that look
authoritative and are silently wrong. The job is therefore marked **blocked** rather
than completed.

## Partial sums (cross-check only — NOT valid regional totals)

Provided solely so a re-run can be reconciled against this one. **Do not treat these
as regional totals.**

| Region | Rows present | Partial sum (cents) |
|--------|--------------|---------------------|
| South  | 6            | 317,220             |
| West   | 6            | 220,854             |
| North  | 6            | 176,153             |
| **Total** | **18**    | **714,227**         |

## What unblocking requires

A re-issued `records.csv` containing the complete set R001–R024. Once that lands, the
totals are a straightforward recomputation. The upstream extraction step should also
be checked for the every-fourth-row drop, since any other job consuming the same
extract in this batch is likely affected the same way.

## Corroboration

An earlier job in this batch left
`/shared/notes/regional-totals-incomplete-input.md`, independently reporting the same
6 missing IDs and the same partial sums, and reaching the same blocked conclusion.
The findings above were derived directly from the CSV and match that note in full.
