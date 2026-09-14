#!/usr/bin/env python3
"""Post-hoc answer-line reading of an E4 sweep (DEVIATIONS D6; Paper 1 §4.3) — analysis side, no model call.

  python3 e4_answerline.py <run dir or sweep.jsonl> [--out sweep_answerline.jsonl] [--check existing.jsonl]

The frozen rule of `sweep_e4.py` (D3) accepts a reply only if it contains exactly one bracketed option anywhere.
On `claude-haiku-4-5` that rule rejects 238 of 360 replies, because the model names both options while it
deliberates and then answers on a line of its own. The reading implemented here is *post hoc* and is reported
as a sensitivity analysis, never as the pre-registered result:

  a reply is valid if it contains exactly one *standalone answer line* — a line that, after stripping
  whitespace, is `[A]` or `[B]`, optionally wrapped in Markdown bold markers (`**[A]**`); the choice is that
  line's letter. Replies with no such line or with several are invalid.

Every other field of the record is copied unchanged; the record gains `parse: answer_line_post_hoc`. `--check`
compares the reconstruction field by field with a previously written file (the shipped `sweep_answerline.jsonl`)
and fails loudly on any difference. The script also prints the agreement with the frozen rule on the replies the
frozen rule accepts, and the count of plain and bold answer lines. `report.py e4 <out file> --out <dir>` then
produces the curves from the reconstructed file exactly as for the frozen one.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ANSWER_LINE_RX = re.compile(r"^(\*\*)?\[\s*([AB])\s*\](\*\*)?$", re.I)


def answer_line(reply: str | None):
    """Return (choice, bold) for a reply with exactly one standalone answer line, else (None, None)."""
    hits = []
    for raw in (reply or "").split("\n"):
        m = ANSWER_LINE_RX.match(raw.strip())
        if m:
            hits.append((m.group(2).upper(), bool(m.group(1))))
    if len(hits) != 1:
        return None, None
    return hits[0]


def reread(rows: list[dict]) -> tuple[list[dict], dict]:
    """Apply the answer-line reading to every row; return the new rows and a summary."""
    out, summary = [], {"n": len(rows), "valid": 0, "plain": 0, "bold": 0, "frozen_valid": 0, "frozen_agree": 0}
    for r in rows:
        choice, bold = answer_line(r.get("reply"))
        if r.get("status") != "success" or not r.get("infrastructure_clean", True):
            choice, bold = None, None                       # a call that was not clean stays invalid (D3)
        new = dict(r)
        new["valid"] = choice is not None
        new["choice"] = choice
        new["parse"] = "answer_line_post_hoc"
        out.append(new)
        if choice is not None:
            summary["valid"] += 1
            summary["bold" if bold else "plain"] += 1
        if r.get("valid"):
            summary["frozen_valid"] += 1
            summary["frozen_agree"] += int(r.get("choice") == choice)
    return out, summary


def load(path: Path) -> list[dict]:
    if path.is_dir():
        path = path / "sweep.jsonl"
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def check(new_rows: list[dict], existing: Path) -> int:
    old = {r["call_id"]: r for r in load(existing)}
    if set(old) != {r["call_id"] for r in new_rows}:
        raise SystemExit(f"{existing}: call ids differ")
    diffs = 0
    for r in new_rows:
        o = old[r["call_id"]]
        for k in set(r) | set(o):
            if r.get(k) != o.get(k):
                diffs += 1
                print(f"  {r['call_id']}: {k}: {o.get(k)!r} -> {r.get(k)!r}")
    return diffs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="run directory (with sweep.jsonl) or the sweep file")
    ap.add_argument("--out", help="where to write the reconstructed sweep (default: <run dir>/sweep_answerline.jsonl)")
    ap.add_argument("--check", help="compare with an existing answer-line file instead of writing")
    a = ap.parse_args()
    src = Path(a.path)
    rows = load(src)
    new_rows, s = reread(rows)
    print(f"replies {s['n']}; answer-line valid {s['valid']} (plain {s['plain']}, bold {s['bold']}); "
          f"frozen rule valid {s['frozen_valid']}, agreement on those {s['frozen_agree']}/{s['frozen_valid']}")
    if a.check:
        d = check(new_rows, Path(a.check))
        print(f"check against {a.check}: {d} field differences")
        sys.exit(1 if d else 0)
    out = Path(a.out) if a.out else (src if src.is_dir() else src.parent) / "sweep_answerline.jsonl"
    out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in new_rows), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
