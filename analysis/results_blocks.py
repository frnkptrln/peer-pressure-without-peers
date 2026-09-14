#!/usr/bin/env python3
"""Assemble the [MAIN RESULTS] blocks for Papers 1 and 2 from the run directories — analysis side, no model call.

  python3 results_blocks.py <runs directory> [--out RESULTS_BLOCKS.md]

Reads results.md (and the E4 report, the D4 gate verdict, the figure files) of every run directory the runbook
names, and writes one block per placeholder in the papers, in the papers' order, each headed by the placeholder it
replaces. A block whose run is missing says so instead of pretending. The tables and contrast lines are copied
verbatim from results.md — the numbers in the papers therefore come from the analysis, not from a retyping.
Prose (one sentence per contrast for the abstract) is drafted from the contrast lines and marked as a draft.
"""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

RUNS = {
    "e1-main": "E1 main (b + T4)", "e5-haiku": "E5 Haiku tier-full", "e5-sonnet": "E5 Sonnet tier", "e2-main": "E2 main",
    "e3-main": "E3 main", "d4-haiku": "D4 seeded chains", "e4": "E4 declarative sweep",
}


def sections(text: str) -> dict[str, str]:
    """Split a results.md into {heading: body} (headings of level 1–2; the first heading wins on duplicates)."""
    out, cur, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith("#"):
            if cur is not None and cur not in out:
                out[cur] = "\n".join(buf).strip()
            cur, buf = line.lstrip("#").strip(), []
        else:
            buf.append(line)
    if cur is not None and cur not in out:
        out[cur] = "\n".join(buf).strip()
    return out


def main_rows(table_body: str, phase="main") -> str:
    """Keep the header and the rows of one phase from an outcomes-by-cell table."""
    lines = [l for l in table_body.splitlines() if l.startswith("|")]
    if not lines:
        return table_body
    head = lines[:2]
    rows = [l for l in lines[2:] if f"| {phase} |" in l]
    return "\n".join(head + rows)


def contrast_sentences(contrasts: str) -> list[str]:
    """Draft one sentence per pre-registered contrast line (abstract material; marked as draft by the caller)."""
    out = []
    for line in contrasts.splitlines():
        m = re.match(r"- \*\*(.+?)\*\* \((\w+)\): diff = ([+-]\d\.\d+) over (\d+) seeds; exact block-swap p = ([\d.]+)", line)
        if m:
            name, flag, diff, n, p = m.groups()
            out.append(f"{name}: paired difference in {flag} {diff} over {n} fixture seeds, exact block-swap p = {p}.")
    return out


def load(runs: Path, name: str):
    d = runs / name
    if not (d / "results.md").exists():
        return None
    text = (d / "results.md").read_text(encoding="utf-8")
    return {"dir": d, "text": text, "sections": sections(text), "figures": sorted(str(p.relative_to(runs)) for p in (d / "reports").glob("*.png")) if (d / "reports").exists() else []}


def block(title, placeholder, body_lines):
    return [f"## {title}", f"*Replaces:* `{placeholder}`", ""] + body_lines + [""]


def missing(name):
    return [f"_run `{name}` not present — placeholder stays_"]


def e1_block(r, cells_note):
    if not r:
        return missing("e1-main")
    s = r["sections"]
    tab = main_rows(s.get("Outcomes by cell (gate and main phases listed separately; contrasts use main only)", ""))
    return [tab, "", s.get("Pre-registered contrasts", ""), "", f"Figures: {', '.join(r['figures']) or 'none'}", "", cells_note]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("runs")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    runs = Path(a.runs).resolve()
    R = {k: load(runs, k) for k in RUNS}
    L = [f"# RESULTS BLOCKS — assembled from `{runs}` (verbatim tables and contrast lines; prose marked as draft)", ""]

    # ---- Paper 1
    L += block("P1 Abstract — one sentence per contrast (DRAFT prose from the contrast lines)", "[MAIN RESULTS: one sentence per contrast.]",
               [f"- {s}" for r in (R["e1-main"], R["e5-haiku"], R["e5-sonnet"]) if r for s in contrast_sentences(r["sections"].get("Pre-registered contrasts", ""))] or missing("e1-main / e5-*"))
    L += block("P1 §4.2 — E1 main: table and pre-registered contrasts",
               "[table: R0×T2, R1×T2, R2×T2, R2×T4 — READ / FAB / HONEST / ABANDON with Wilson intervals; Figure 1 stacked outcome shares by rung] + [H: R0×T2 vs R2×T2, exact block-swap p, Hoeffding interval; R2×T2 vs R2×T4 exploratory]",
               e1_block(R["e1-main"], "Cells: R0×T2, R1×T2, R2×T2 (pre-registered ladder) and R2×T4 (exploratory)."))
    e4 = R["e4"]
    e4_body = []
    if e4 is None and (runs / "e4" / "reports" / "e4_report.md").exists():
        e4_body = [(runs / "e4" / "reports" / "e4_report.md").read_text(encoding="utf-8"), "",
                   f"Figures: {', '.join(str(p.relative_to(runs)) for p in (runs / 'e4' / 'reports').glob('*.png'))}"]
    L += block("P1 §4.3 — E4 declarative sweep", "[E4 placeholder in §4.3]", e4_body or missing("e4"))
    e2, e3 = R["e2-main"], R["e3-main"]
    e2_body = ([e2["sections"].get("E2 — reporting route", "").split("## ")[0], "", e2["sections"].get("Pre-registered contrasts", ""), "", f"Figures: {', '.join(e2['figures']) or 'none'}"] if e2 else missing("e2-main"))
    e3_body = ([e3["sections"].get("Per-generation write and read rates", ""), "",
                "### H7", e3["sections"].get("H7 — any write in the chain, blocked vs solvable (chain level, exact; three-state endpoints — D5)", ""), "",
                "### H8", e3["sections"].get("H8 — LOC_MENTION among written notes (blocked)", ""), "",
                "### Existence cases", e3["sections"].get("Existence cases", ""), "", f"Figures: {', '.join(e3['figures']) or 'none'}"] if e3 else missing("e3-main"))
    L += block("P1 §4.4 — E2 and E3 main", "[MAIN RESULTS] in §4.4", ["### E2"] + e2_body + ["", "### E3"] + e3_body)
    tier = []
    for key, label in (("e5-haiku", "Haiku 4.5, tier-full (D1)"), ("e5-sonnet", "Sonnet 5, tier")):
        r = R[key]
        tier += [f"### {label}"] + (e1_block(r, "") if r else missing(key)) + [""]
    L += block("P1 §4.5 — model tier", "[Haiku: R0×{T0,T2}, R2×{T0,T1,T2,T4} × 16 — …; Sonnet: {R0,R2} × {T0,T2} × 8; the comparative statement a lab can use]", tier)
    L += block("P1 §4.6 — coding", "[shares by axis; injection framing; test awareness; κ human-vs-model]",
               ["_from the coding sheet: run `python3 ../analysis/kappa.py <filled sheet>` and paste its table here_"])

    # ---- Paper 2
    L += block("P2 §2.4 — Check 1 main", "[table by cell with Wilson intervals; H4 exact paired test; H5 false-alarm interval under neutral notes; H6 route effect vs the P0 deliverable-only baseline]", e2_body)
    L += block("P2 §3.4 — Check 2 main", "[per-generation table; chain-level exact test blocked vs solvable; LOC_MENTION interval; drift; convention emergence; existence cases]",
               e3_body + ["", "_drift and convention emergence: from the coded notes (coding sheet), not mechanical_"])
    d4 = R["d4-haiku"]
    d4_body = []
    if d4:
        s = d4["sections"]
        key = next((k for k in s if k.startswith("D4 — seeded chains")), None)
        verdict = d4["dir"] / "d4_gate_verdict.json"
        d4_body = ["### Continuation gate (DEVIATIONS D5, rule iii)",
                   (json.dumps(json.loads(verdict.read_text(encoding="utf-8")), indent=2) if verdict.exists() else "_no verdict file — was the gate evaluated?_"), "",
                   "### D4 section of results.md", s.get(key, "_D4 section not found_") if key else "_D4 section not found_", "",
                   f"Figures: {', '.join(d4['figures']) or 'none'}"]
    L += block("P2 §3.6.5 — Check 2b seeded chains",
               "[generation-1 table with exposure; the paired generation-1 contrast; whether the continuation rule was met; …]", d4_body or missing("d4-haiku"))

    out = Path(a.out) if a.out else runs / "RESULTS_BLOCKS.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    present = [k for k, v in R.items() if v]
    print(json.dumps({"out": str(out), "runs_present": present, "runs_missing": [k for k in RUNS if k not in present]}))


if __name__ == "__main__":
    main()
