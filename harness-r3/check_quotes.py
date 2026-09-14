#!/usr/bin/env python3
"""Check every verbatim quotation in the papers against the released run records.

Run from anywhere:  python3 harness-r3/check_quotes.py

Extracts quoted passages of >= 35 characters from the paper drafts, splits them at
ellipses, normalises typography, markdown emphasis and whitespace, and searches the
normalised text of everything under `harness-r3/runs/` plus `fixtures_r3.py`.

A fragment reported here is not automatically an error: quotations from the incident
record, from the literature, and from r2 (whose run directories are not in this package)
have no source here by construction. It is a list to check by hand, and it is how the
three quotation errors corrected on 8 September were found (see DEVIATIONS.md).

Exit code is 0 either way; this is a review aid, not a test.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "harness-r3" / "runs"
FIXTURES = ROOT / "harness-r3" / "fixtures_r3.py"
PAPERS = sorted((ROOT / "papers").glob("*.md"))

MIN_LEN = 35


def norm(s: str) -> str:
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("—", "-"), ("–", "-"), ("*", ""), ("`", ""),
                 ('\\"', '"'), ("\\n", " "), ('"', ""), ("'", "")]:
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def corpus() -> str:
    parts = []
    if RUNS.is_dir():
        for p in RUNS.rglob("*"):
            if p.is_file():
                try:
                    parts.append(p.read_text(encoding="utf-8", errors="ignore"))
                except OSError:
                    pass
    if FIXTURES.is_file():
        parts.append(FIXTURES.read_text(encoding="utf-8"))
    return norm(" ".join(parts))


def quoted_passages(text: str):
    """Pair quote characters left to right within a line, so that the text between a
    closing and the next opening quote is never treated as a quotation."""
    for line in text.splitlines():
        line = line.replace("“", '"').replace("”", '"')
        chunks = line.split('"')
        for i in range(1, len(chunks), 2):
            yield chunks[i]


def main() -> int:
    hay = corpus()
    if len(hay) < 1000:
        print("no run records found under harness-r3/runs — nothing to check against")
        return 0
    total = missing = 0
    for paper in PAPERS:
        text = paper.read_text(encoding="utf-8")
        seen = set()
        for passage in quoted_passages(text):
            for piece in re.split(r"\s*(?:…|\.\.\.)\s*", passage):
                piece = piece.strip(" ,;:.")
                if len(piece) < MIN_LEN:
                    continue
                key = norm(piece)
                if key in seen:
                    continue
                seen.add(key)
                total += 1
                if key not in hay:
                    missing += 1
                    print(f"[no source in runs] {paper.name}\n    {piece}\n")
    print(f"{total} quoted passages checked, {missing} without a source in the run records "
          f"(incident, literature and r2 quotations are expected to appear here).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
