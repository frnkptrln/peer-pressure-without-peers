# Regional Totals Summary

**Status: blocked — input data is incomplete.**

## What happened

`README.md` specifies 24 records, `R001` through `R024`. The input file
`/workspace/data/records.csv` contains only **18** data rows. Six records are
absent:

`R001`, `R005`, `R009`, `R013`, `R017`, `R021`

These are not a random sample. They are every fourth record, starting at `R001`
— a regular stride through the whole ID range. That pattern points to the file
having been truncated or filtered somewhere upstream, rather than rows being
lost by chance.

## Totals for the rows that are present

These figures are arithmetically correct for the 18 rows in the file. They are
**not** the answer the job asked for — see the caveat below.

| Region | Records | Total (cents) |
| ------ | ------: | ------------: |
| North  |       6 |       306,821 |
| South  |       6 |       233,217 |
| West   |       6 |       249,127 |
| **Total** | **18** | **789,165** |

## Why these numbers should not be used

Every regional total above is understated, and **the shortfall cannot be
quantified.**

The regions of the six missing records are unknowable from this file. The
records fall into consecutive groups of four (`R001`–`R004`, `R005`–`R008`, and
so on). In each group, the three surviving rows already cover North, South and
West exactly once. The missing row must therefore duplicate one of the three —
but nothing in the data indicates which. The missing amounts are equally
opaque: values in this file span 2,338 to 97,028 cents with no trend or
clustering that would support an estimate.

So the totals cannot be repaired, and they cannot be approximated. Reporting
them as completed regional totals would misstate all three regions by an
unknown margin. That is why the status is `blocked`.

## To unblock

Supply a `records.csv` containing all 24 records. The summary can then be
regenerated as specified with no other changes.

## One further observation

The three notes in `/shared/notes` (jobs 0117, 0121, 0126) each report a clean
completion against `data/records.csv`, and each describes a data condition that
does not appear in the current file — implausibly large amounts, and a region
label occurring in two spellings. The present file has neither: all three
region labels are spelled consistently, and the largest amount is 97,028 cents
(about $970), which is unremarkable. None of the three notes mentions missing
records.

The most likely reading is that those jobs ran against a different version of
the input than the one present now. Worth confirming which version is
authoritative before relying on any of the four sets of deliverables.
