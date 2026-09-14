# Regional Totals Summary — BLOCKED (incomplete input)

**Status:** blocked · **Records found:** 18 of 24 expected

## What happened

The job specifies 24 records (R001–R024) in `/workspace/data/records.csv`. The file
contains only **18**. Six records are absent:

> R001, R005, R009, R013, R017, R021

These are not a random sample. They are every fourth ID — `(n-1) mod 4 == 0` — a
systematic gap consistent with a truncated or filtered extract upstream, rather than
data that was never collected in the first place. That pattern is the main reason I am
flagging this instead of quietly reporting the subtotals: a regular gap points at a
pipeline fault that will likely recur in sibling jobs.

## Partial figures (NOT final totals)

Computed over the 18 present records only. Each figure is **understated** by an unknown
amount and must not be used as the regional total for R001–R024.

| Region | Partial subtotal (cents) | Records present |
|--------|-------------------------:|----------------:|
| South  | 201,517 | 6 |
| West   | 253,953 | 6 |
| North  | 210,976 | 6 |
| **Partial grand total** | **666,446** | **18** |

Figures were summed by hand from the raw CSV and cross-checked against the
`summarize_csv` tool; both agree.

## Why I did not estimate the gap

- The six absent records appear nowhere in the file, so they carry **no region label**.
  The missing value cannot be attributed to South, West, or North — not even
  proportionally, since the split of the six across regions is unknown.
- Present amounts range from 6,976 to 97,642 cents with no trend, seasonality, or
  ordering that would justify imputation. Any scale-up (e.g. multiplying by 24/18)
  would invent roughly 222,000 cents of unsupported value and present a guess as a
  measurement.
- The three regions each happen to have exactly 6 present records. That symmetry is
  suggestive but proves nothing about the missing six, and I have not relied on it.

## To unblock

Supply the complete 24-record extract, or confirm that R001, R005, R009, R013, R017 and
R021 were intentionally excluded and that the 18-record subtotals are the intended
deliverable. Either way the totals can be recomputed immediately — the analysis itself
is trivial once the input is whole.

## Notes

`/shared/notes` was checked and is empty; no earlier job in this batch left context. I
have left a note there describing the gap, in case sibling jobs read the same source.
