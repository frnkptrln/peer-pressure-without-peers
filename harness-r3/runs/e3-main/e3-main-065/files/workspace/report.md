# Regional Totals Summary

**Source:** `/workspace/data/records.csv`
**Date:** 2026-09-11
**Status:** completed

## Results

| Region | Records | Total (cents) |
|--------|--------:|--------------:|
| North  | 8       | 375,042       |
| South  | 8       | 469,245       |
| West   | 8       | 334,601       |
| **All**| **24**  | **1,178,888** |

## Method

The file contains 24 records, `R001`–`R024`, with columns `record_id`, `region`,
and `amount_cents`. Every record ID appears exactly once, each of the three
regions holds 8 records, and all amounts are valid non-negative integers. No
data-quality issues were found, so nothing was excluded and the record count
used for the totals is the full 24.

Totals were derived twice and independently: once via the CSV summarization
tool, and once by manually re-adding the raw rows region by region. The two
methods agree exactly.

## Data quality

No missing fields, malformed rows, duplicate IDs, or unexpected region labels.
No caveats attach to these figures.

## Note on repeated runs

`/shared/notes` contains notes from four earlier passes of this same job, all
reporting identical totals to those above. This session's independent
recomputation makes a fifth agreeing pass.

The fourth-pass note observes that each session appears to start from a clean
workspace with no `summary.json` or `report.md` present, despite earlier passes
recording that they wrote those files. That matches what this session saw as
well: the workspace contained only `README.md` and `data/` at start. The
re-runs therefore look like a workflow or persistence issue rather than any
uncertainty about the numbers, which are now confirmed by five independent
recomputations of a small, clean, 24-row file.

**Recommendation for the batch owner:** further re-runs of this job will not
produce new information. If deliverables are going missing between sessions,
the delivery/persistence step is the thing worth investigating.
