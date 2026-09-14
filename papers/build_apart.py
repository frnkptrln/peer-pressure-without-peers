#!/usr/bin/env python3
"""Build a paper in the Apart Research submission-template layout (PDF via pandoc/xelatex; DOCX via pandoc).

  python3 build_apart.py <paper.md> <out.pdf> [--docx out.docx]

Needs pandoc, xelatex (TeX Live) and the Old Standard TT font (OldStandard-{Regular,Bold,Italic}.ttf, e.g. from the
Google Fonts repository, installed under ~/.fonts). Letter, 11 pt, 0.8 in margins, as in the sprint's template.

The Markdown carries YAML front matter: title, subtitle (optional), track, authors (list of {name, affiliation}),
abstract. Section headings are plain (`## Introduction`); pandoc numbers them (1., 2., …); headings with `{-}` stay
unnumbered (Code and Data, Author Contributions, References, Appendix …, LLM Usage Statement). Tables get a
`Table: …` caption line, figures `![caption](path){width=…}`; pandoc numbers both. Prints the page on which the
References heading starts (main text = the pages before it).
"""
import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

TEMPLATE = Path(__file__).resolve().parent / "apart_template.tex"   # the pandoc/LaTeX template next to this script


def author_grid(authors, per_row=4):
    """Author grid as in the template: name over affiliation, up to `per_row` authors per row."""
    cols = min(per_row, len(authors))
    rows = []
    for i in range(0, len(authors), cols):
        chunk = authors[i:i + cols]
        names = " & ".join(a["name"] for a in chunk)
        affs = " & ".join(a.get("affiliation", "") for a in chunk)
        pad = " & " * (cols - len(chunk))
        rows.append(f"{names}{pad} \\\\\n{affs}{pad} \\\\[6pt]")
    return "\\begin{tabular}{" + "c" * cols + "}\n" + "\n".join(rows) + "\n\\end{tabular}"


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("no YAML front matter")
    return yaml.safe_load(m.group(1)), m.group(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--docx")
    a = ap.parse_args()
    src = Path(a.src)
    meta, body = split_front_matter(src.read_text(encoding="utf-8"))
    grid = author_grid(meta["authors"])
    body_pdf = body
    # Old Standard TT has no Greek or set-theory glyphs; typeset those few characters as math in the PDF only.
    for ch, tex in {"β": r"$\beta$", "κ": r"$\kappa$", "α": r"$\alpha$", "∪": r"$\cup$", "∈": r"$\in$"}.items():
        body_pdf = body_pdf.replace(ch, tex)
    with tempfile.NamedTemporaryFile("w", suffix=".md", dir=src.parent, delete=False, encoding="utf-8") as fh:
        fh.write("---\n" + yaml.safe_dump({k: v for k, v in meta.items() if k != "authors"}, allow_unicode=True) + "---\n" + body_pdf)
        tmp = Path(fh.name)
    try:
        cmd = ["pandoc", str(tmp), "-o", a.out, "--pdf-engine=xelatex", f"--template={TEMPLATE}", "--number-sections",
               "--shift-heading-level-by=-1", "-V", f"author-grid={grid}", f"--resource-path={src.parent}"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            print(r.stderr[-4000:]); sys.exit(1)
        if a.docx:
            authors_line = "; ".join(f"{x['name']} ({x.get('affiliation','')})" for x in meta["authors"])
            docx_md = ("---\n" + yaml.safe_dump({"title": meta["title"], "subtitle": meta.get("subtitle", ""),
                       "author": authors_line, "abstract": meta["abstract"]}, allow_unicode=True) + "---\n" + body)
            tmp2 = tmp.with_suffix(".docx.md"); tmp2.write_text(docx_md, encoding="utf-8")
            r2 = subprocess.run(["pandoc", str(tmp2), "-o", a.docx, "--number-sections", "--shift-heading-level-by=-1",
                                 f"--resource-path={src.parent}"], capture_output=True, text=True)
            tmp2.unlink(missing_ok=True)
            if r2.returncode:
                print(r2.stderr[-2000:]); sys.exit(1)
    finally:
        tmp.unlink(missing_ok=True)
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", a.out], capture_output=True, text=True).stdout).group(1))
    ref_page = None
    for p in range(1, pages + 1):
        lines = [ln.strip() for ln in subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", a.out, "-"],
                                                     capture_output=True, text=True).stdout.splitlines()]
        lines = [ln for ln in lines if ln]
        for i, ln in enumerate(lines):
            if ln == "References" and any(x.startswith("1.") for x in lines[i + 1:i + 3]):
                ref_page = p; break
        if ref_page:
            break
    words = len(re.sub(r"<!--.*?-->", "", body.split("## References {-}")[0], flags=re.S).split())
    print(f"{a.out}: {pages} pages; References start on page {ref_page}; main-text words ≈ {words}")


if __name__ == "__main__":
    main()
