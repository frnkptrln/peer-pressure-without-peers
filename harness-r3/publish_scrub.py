#!/usr/bin/env python3
"""Prepare the public copy of the run data (RUNBOOK, Sunday: repository). Outside the frozen instrument.

  python3 publish_scrub.py --email <login e-mail> --out ../publish [--include dryrun,dry-thu]

Copies harness-r3/runs/* (minus the excluded dry runs) to <out>/runs, then in every text file:
  * replaces the login e-mail address by "<login-email>" (it sits in the subject model's context — Claude Code shows
    the account to the model — and appeared once in a deliverable; see EXECUTION_NOTES), keeping a count per file;
  * replaces absolute container paths (/tmp/v5/…, /root/work/…, /home/claude/…) up to the tree root by "<tree>";
  * reports any other e-mail-like string or token-like string it finds (nothing is changed for those — decide by hand).
Writes <out>/REDACTION.md (what was replaced, where, how often) and <out>/MANIFEST.sha256.txt over the copy.
The originals are never modified. Records, transcripts and outcomes are byte-identical apart from the replacements
listed; a reader can verify the e-mail replacement count against EXECUTION_NOTES.
"""
import argparse
import hashlib
import os
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATH_RX = re.compile(r"(/tmp/v5|/root/work(?:/v\d+)?|/home/claude)(?:/sprint_package_20260907|/sprint)?/harness-r3")
EMAIL_RX = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
TOKEN_RX = re.compile(r"(sk-ant-[A-Za-z0-9_-]{8,}|Bearer [A-Za-z0-9._-]{16,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,})")
TEXT_SUFFIXES = {".json", ".jsonl", ".md", ".txt", ".csv", ".log"}


def is_text(p: Path) -> bool:
    return p.suffix in TEXT_SUFFIXES


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", required=True, help="the login e-mail to replace by <login-email>")
    ap.add_argument("--out", default=str(HERE.parent / "publish"))
    ap.add_argument("--include", default="", help="comma-separated run directories to include although they are dry runs")
    ap.add_argument("--runs", default=str(HERE / "runs"))
    a = ap.parse_args()
    src = Path(a.runs).resolve()
    out = Path(a.out).resolve()
    include = {x for x in a.include.split(",") if x}
    if out.exists():
        shutil.rmtree(out)
    (out / "runs").mkdir(parents=True)
    counts, paths, other_emails, tokens = Counter(), Counter(), Counter(), []
    for run in sorted(src.iterdir()):
        if not run.is_dir() or not (run / "plan.json").exists():
            continue
        if run.name.startswith("dry") and run.name not in include:
            continue
        dst = out / "runs" / run.name
        shutil.copytree(run, dst, ignore=shutil.ignore_patterns("__pycache__"))
        for p in dst.rglob("*"):
            if not p.is_file() or not is_text(p):
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            n_mail = text.count(a.email)
            new = text.replace(a.email, "<login-email>")
            new, n_path = PATH_RX.subn("<tree>", new)
            if n_mail:
                counts[str(p.relative_to(out))] += n_mail
            if n_path:
                paths[str(p.relative_to(out))] += n_path
            for m in EMAIL_RX.findall(new):
                if m != "<login-email>" and "@" in m:
                    other_emails[m] += 1
            for m in TOKEN_RX.findall(new):
                tokens.append((str(p.relative_to(out)), m[:12] + "…"))
            if new != text:
                p.write_text(new, encoding="utf-8")
    lines = ["# Redaction record for the published run data", "",
             f"Source: `{src}`; excluded dry runs: {[d.name for d in src.iterdir() if d.is_dir() and d.name.startswith('dry') and d.name not in include]}", "",
             "## Login e-mail → `<login-email>`", ""] + [f"- {k}: {v}" for k, v in sorted(counts.items())] + ["", f"Total replacements: {sum(counts.values())}", "",
             "## Container paths → `<tree>`", "", f"Files touched: {len(paths)}, replacements: {sum(paths.values())}", "",
             "## Other e-mail-like strings found (not changed)", ""] + ([f"- {k}: {v}" for k, v in other_emails.items()] or ["- none"]) + ["",
             "## Token-like strings found (not changed — must be resolved by hand before publishing)", ""] + ([f"- {p}: {t}" for p, t in tokens] or ["- none"]) + [""]
    (out / "REDACTION.md").write_text("\n".join(lines), encoding="utf-8")
    entries = []
    for p in sorted(out.rglob("*")):
        if p.is_file() and p.name != "MANIFEST.sha256.txt":
            entries.append((str(p.relative_to(out)), hashlib.sha256(p.read_bytes()).hexdigest()))
    (out / "MANIFEST.sha256.txt").write_text("".join(f"{h}  ./{rel}\n" for rel, h in entries), encoding="utf-8")
    print(f"published copy: {out} — {len(entries)} files; e-mail replacements {sum(counts.values())} in {len(counts)} file(s); "
          f"path replacements {sum(paths.values())}; other e-mails {len(other_emails)}; token-like strings {len(tokens)}")
    if tokens:
        sys.exit(1)


if __name__ == "__main__":
    main()
