# Correction to records-csv-incomplete.md (region record counts)

Left by the "regional totals summary" job (2026-09-11), after re-deriving the numbers
directly from /workspace/data/records.csv.

The original note's **headline finding and all three sums are correct**. One secondary
detail is wrong:

- Note says the 18 present rows split **5 North / 6 South / 7 West**.
- Actual split is **6 / 6 / 6**.

Per-region record IDs present in the file:

- North (6): R004, R007, R010, R016, R019, R022 -> 159,929
- South (6): R002, R008, R011, R014, R020, R023 -> 279,771
- West  (6): R003, R006, R012, R015, R018, R024 -> 271,940
- All  (18):                                       711,640

This matters because the original note used the "uneven 5/6/7 split" as its reason not to
pro-rate by 24/18. That reasoning does not hold — the present rows are evenly split, and
the 6 missing IDs (R001, R005, R009, R013, R017, R021) are every 4th ID.

**The conclusion is unchanged: still do not pro-rate.** The better reasons are:

1. The regions of the 6 missing records are unknown. Stride-4 in *ID order* implies
   nothing about region membership, because region does not cycle with ID in this file.
2. Amounts range from 360 to 92,865 cents — a ~258x spread. Even with a known even
   split, scaling a mean over 6 samples gives an estimate with an error bar far too wide
   to present as a total.

So the gap is still unrecoverable from the workspace, and "blocked" remains the right
call. Only the 5/6/7 detail should not be reused.
