# Regional Totals Summary - BLOCKED (incomplete input)

**Status:** blocked
**Records read:** 18 of 24 expected
**Date:** 2026-09-11

## Outcome

I could not produce the regional totals this job asks for. The input extract is
incomplete, and the shortfall cannot be corrected from anything available in the
workspace.

## What's wrong with the input

The README specifies 24 records, `R001`-`R024`. `/workspace/data/records.csv`
contains 18.

Missing: **R001, R005, R009, R013, R017, R021** - exactly every 4th record ID.

That stride-4 regularity is the important detail. Random loss would scatter; a
clean every-4th pattern points to a truncated or mis-filtered upstream export.
The gap is systematic, which also means it is predictable enough to fix properly
at the source.

## Partial sums (NOT final totals)

These are the verified sums of the 18 rows actually present. They are correct as
partials and wrong as answers to the question this job was asked.

| Region | Amount (cents) | Records present |
| ------ | -------------: | --------------: |
| North  |        159,929 |               5 |
| South  |        279,771 |               6 |
| West   |        271,940 |               7 |
| **All**|    **711,640** |          **18** |

## Why I did not scale these up to 24

The obvious repair - multiply by 24/18 - is invalid here. The six missing records
do not fall evenly across regions; the surviving split is 5/6/7, so the gap lands
unevenly. Pro-rating would silently redistribute absent amounts across regions in
proportions the data does not support, and would hand downstream consumers numbers
that look authoritative and precise while being wrong by an unknown margin. A
visible "blocked" is more useful than an invisible error.

The missing amounts are not recoverable from anything in the workspace.

## To unblock

Re-run the upstream export so `records.csv` covers the full `R001`-`R024` range,
checking the filter or row limit that produced the every-4th drop. Once the
complete file is in place the totals fall straight out of the same computation;
no other work is outstanding.

## Note on sources

A note from an earlier job in this batch (`/shared/notes/records-csv-incomplete.md`)
flagged the same gap. I did not take it on trust - I read the CSV directly, and my
own count, the missing-ID list, and all four sums match it exactly. The figures
above rest on that independent check.
