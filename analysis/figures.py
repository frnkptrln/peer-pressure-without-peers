#!/usr/bin/env python3
"""Figures for E2, E3 and the D4 seeded chains — analysis side, outside the frozen instrument.

  python3 figures.py <run directory> [--out <dir>]        # reads <run>/records.jsonl, writes PNGs to <run>/reports/

The instrument's `report.py` draws the E1 stacked-outcome figure; this module draws the three figures the papers
still lacked, in the same style (matplotlib if importable, dpi 200, legend below the axes, shares on [0, 1]):

  e2_reporting.png   — E2: the reporting outcome of every cell with the route (REPORT_PEER / REPORT_BLOCKED / other
                       report / no report), and, in a second panel, MENTION — the violation named in the deliverable —
                       for the P0 cells (where it is the only route) and the P1 cells, side by side;
  e3_channel.png     — E3: channel formation over generations — the share of episodes that wrote to the cache against
                       the share that read an inherited note, per task condition;
  d4_chains.png      — D4: chain-level READ per generation, S1 against S0, with generation 1 (the seed's own effect)
                       set apart from generations ≥ 2 (propagation), unobserved chains shown as such, and the
                       cumulative "any READ up to generation g" per arm as a dashed line.

The numbers behind each figure come from the same predicates as `report.py` (`classify`, `planned_windows`,
`endpoint_state`); nothing is re-derived from transcripts. Every function that computes data is pure and testable
without matplotlib; only `draw_*` touch the plotting library. No new dependency.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from report import classify, load_records, planned_windows, endpoint_state, _chain_key  # noqa: E402

E2_CATEGORIES = ("REPORT_PEER", "REPORT_BLOCKED", "other report", "no report")


# ---------------------------------------------------------------------------- data

def e2_data(records):
    """Per cell (route, trace): counts of the four reporting categories among valid episodes, and MENTION counts.
    Returns (cells, reporting, mention) with cells sorted, reporting[cell] = {category: n}, mention[cell] = (k, n)."""
    valid = [r for r in records if r.infrastructure_valid]
    reporting, mention = defaultdict(lambda: defaultdict(int)), defaultdict(lambda: [0, 0])
    for r in valid:
        cell = (r.cell.get("route"), r.cell.get("trace"))
        c = classify(r)
        if c["REPORT_PEER"]:
            cat = "REPORT_PEER"
        elif c["REPORT_BLOCKED"]:
            cat = "REPORT_BLOCKED"
        elif c["REPORT"]:
            cat = "other report"
        else:
            cat = "no report"
        reporting[cell][cat] += 1
        mention[cell][0] += int(bool(r.cell.get("mention_predecessor_violation")))
        mention[cell][1] += 1
    cells = sorted(reporting)
    return cells, {c: dict(reporting[c]) for c in cells}, {c: tuple(mention[c]) for c in cells}


def e3_data(records):
    """Per (task, generation): n valid, episodes that wrote to the cache, episodes that read an inherited note."""
    out = defaultdict(lambda: {"n": 0, "wrote": 0, "read": 0})
    for r in records:
        if not r.infrastructure_valid or r.cell.get("arm"):
            continue                                   # the seeded design has its own figure
        c = classify(r)
        g = out[(r.cell.get("task"), r.cell.get("generation"))]
        g["n"] += 1
        g["wrote"] += int(c["SHARED_WRITE"])
        g["read"] += int(bool(r.cell.get("inherited_note_read")))
    return {k: dict(v) for k, v in out.items()}


def d4_data(records):
    """Chain-level READ per generation and arm, over the *planned* chains: for every (arm, generation) the number of
    chains with a valid READ, a valid non-READ, and no valid episode (unobserved); plus per arm the cumulative
    three-state endpoint "any READ up to generation g" (positive / negative / unknown counts) for every g."""
    planned, valid_gens = planned_windows(records)
    chains = defaultdict(list)
    for r in records:
        if r.infrastructure_valid:
            chains[_chain_key(r)].append((r.cell.get("generation"), r, classify(r)))
    keys = sorted(k for k in planned if k[1] in ("S0", "S1"))
    gens = sorted({g for k in keys for g in planned[k]})
    per = {arm: {g: {"read": 0, "no_read": 0, "unobserved": 0} for g in gens} for arm in ("S0", "S1")}
    cum = {arm: {g: {"positive": 0, "negative": 0, "unknown": 0} for g in gens} for arm in ("S0", "S1")}
    for key in keys:
        arm = key[1]
        items = chains.get(key, [])
        by_gen = {gen: c for gen, r, c in items}
        for g in planned[key]:
            if g in by_gen:
                per[arm][g]["read" if by_gen[g]["READ"] else "no_read"] += 1
            else:
                per[arm][g]["unobserved"] += 1
        for g in gens:
            window = [x for x in planned[key] if x <= g]
            st = endpoint_state(items, planned[key], lambda r, c: c["READ"], window)
            cum[arm][g][st] += 1
    n_chains = {arm: sum(1 for k in keys if k[1] == arm) for arm in ("S0", "S1")}
    return {"generations": gens, "per_generation": per, "cumulative": cum, "chains": n_chains}


# ---------------------------------------------------------------------------- drawing

def _plt():
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        return plt
    except Exception:
        return None


def draw_e2(records, path):
    plt = _plt()
    cells, reporting, mention = e2_data(records)
    if plt is None or not cells:
        return None
    p1 = [c for c in cells if c[0] == "P1"]
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(max(7, 1.3 * len(cells) + 3), 3.8), gridspec_kw={"width_ratios": [max(1, len(p1)), max(1, len(cells))]})
    labels = [f"{c[0]}×{c[1]}" for c in p1]
    bottom = [0.0] * len(p1)
    for cat in E2_CATEGORIES:
        share = [reporting[c].get(cat, 0) / max(1, sum(reporting[c].values())) for c in p1]
        ax.bar(labels, share, bottom=bottom, label=cat)
        bottom = [b + s for b, s in zip(bottom, share)]
    ax.set_ylim(0, 1)
    ax.set_ylabel("share of episodes")
    ax.set_title("E2 — reporting outcome with the route (P1)\n(share of episodes by report category)")
    ax.legend(fontsize=8, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.15))
    labels_all = [f"{c[0]}×{c[1]}" for c in cells]
    shares = [mention[c][0] / mention[c][1] if mention[c][1] else 0 for c in cells]
    colors = ["#888888" if c[0] == "P0" else "#4c72b0" for c in cells]
    bx.bar(labels_all, shares, color=colors)
    for i, c in enumerate(cells):
        bx.text(i, shares[i] + 0.02, f"{mention[c][0]}/{mention[c][1]}", ha="center", fontsize=8)
    bx.set_ylim(0, 1.08)
    bx.set_title("MENTION — violation named in the deliverable\n(grey: P0, the only route there; blue: P1)")
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def draw_e3(records, path):
    plt = _plt()
    data = e3_data(records)
    if plt is None or not data:
        return None
    tasks = sorted({k[0] for k in data}, key=str)
    gens = sorted({k[1] for k in data})
    fig, ax = plt.subplots(figsize=(max(4.5, 1.1 * len(gens) + 2), 3.6))
    styles = {"blocked": "#c44e52", "solvable": "#55a868"}
    for task in tasks:
        col = styles.get(task, "#4c72b0")
        xs = [g for g in gens if (task, g) in data]
        wrote = [data[(task, g)]["wrote"] / data[(task, g)]["n"] for g in xs]
        read = [data[(task, g)]["read"] / data[(task, g)]["n"] for g in xs]
        ax.plot(xs, wrote, marker="o", color=col, label=f"{task}: wrote to the cache")
        ax.plot(xs, read, marker="s", linestyle="--", color=col, label=f"{task}: read an inherited note")
        for g, w in zip(xs, wrote):
            ax.annotate(f"n={data[(task, g)]['n']}", (g, w), textcoords="offset points", xytext=(0, 6), ha="center", fontsize=7, color=col)
    ax.set_xticks(gens)
    ax.set_xlabel("generation")
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("share of episodes")
    ax.set_title("E3 — channel formation over generations")
    ax.legend(fontsize=8, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.22))
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


def draw_d4(records, path):
    plt = _plt()
    data = d4_data(records)
    gens = data["generations"]
    if plt is None or not gens:
        return None
    fig, ax = plt.subplots(figsize=(max(5, 1.2 * len(gens) + 2.5), 4.3))
    width = 0.38
    colors = {"S1": "#c44e52", "S0": "#4c72b0"}
    for j, arm in enumerate(("S1", "S0")):
        N = max(1, data["chains"][arm])
        xs = [g + (j - 0.5) * width for g in gens]
        read = [data["per_generation"][arm][g]["read"] / N for g in gens]
        unobs = [data["per_generation"][arm][g]["unobserved"] / N for g in gens]
        ax.bar(xs, read, width, color=colors[arm], label=f"{arm}: chains with a READ at this generation")
        ax.bar(xs, unobs, width, bottom=read, color="none", edgecolor=colors[arm], hatch="///", label=f"{arm}: unobserved chains")
        cum = [data["cumulative"][arm][g]["positive"] / N for g in gens]
        ax.plot(xs, cum, linestyle="--", marker="o", markersize=3, color=colors[arm], label=f"{arm}: any READ up to generation g (positive chains)")
        for g, rd in zip(gens, read):
            k = data["per_generation"][arm][g]["read"]
            u = data["per_generation"][arm][g]["unobserved"]
            ax.text(g + (j - 0.5) * width, rd + (u / N) + 0.02, f"{k}/{N}" + (f" (+{u}?)" if u else ""), ha="center", fontsize=7, color=colors[arm])
    if len(gens) > 1:
        ax.axvline(1.5, color="#444444", linewidth=1)
        ax.text(1.0, 1.13, "generation 1:\nthe seed's own effect", ha="center", va="center", fontsize=8)
        ax.text((gens[-1] + 2) / 2, 1.13, "generations ≥ 2: propagation\n(seed removed; agent-written notes only)", ha="center", va="center", fontsize=8)
    ax.set_xticks(gens)
    ax.set_xlabel("generation")
    ax.set_ylim(0, 1.24)
    ax.set_ylabel(f"share of planned chains (S1 n={data['chains']['S1']}, S0 n={data['chains']['S0']})")
    ax.set_title("D4 — seeded chains: forbidden READ per generation, chain level")
    ax.legend(fontsize=7, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.2))
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)
    return path


# ---------------------------------------------------------------------------- CLI

def make_figures(run_dir, out=None):
    records = load_records(os.path.join(run_dir, "records.jsonl"))
    out = out or os.path.join(run_dir, "reports")
    os.makedirs(out, exist_ok=True)
    exp = records[0].experiment if records else None
    made = []
    if exp == "E2":
        made.append(draw_e2(records, os.path.join(out, "e2_reporting.png")))
    elif exp == "E3":
        if any(r.cell.get("arm") for r in records):
            made.append(draw_d4(records, os.path.join(out, "d4_chains.png")))
        else:
            made.append(draw_e3(records, os.path.join(out, "e3_channel.png")))
    return [m for m in made if m]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_directory")
    ap.add_argument("--out")
    a = ap.parse_args()
    made = make_figures(a.run_directory, a.out)
    print(json.dumps({"figures": made, "model_calls_made": 0}))


if __name__ == "__main__":
    main()
