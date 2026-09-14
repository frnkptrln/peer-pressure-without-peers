"""Freeze r3: hash the amendment, the instrument files and the fixtures into MANIFEST.sha256.json.

  python3 freeze.py --amendment ../amendment/AMENDMENT_r3.md --note "working rung R1; design a"

Refuses to run if a main-phase run directory already contains a started episode.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTRUMENT = ("fixtures_r3.py", "run_r3.py", "analyze_r3.py", "sweep_e4.py", "workspace_server.py", "concern_server.py",
              "schema.py", "stats.py", "report.py", "run_open_r3.py")   # run_open_r3.py since DEVIATIONS D2


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--amendment", required=True)
    ap.add_argument("--note", default="")
    ap.add_argument("--version", default="", help="suffix for a re-freeze after a logged deviation, e.g. v2")
    a = ap.parse_args()
    for run in (HERE / "runs").glob("*-main*"):
        if any((ep / "started.json").exists() for ep in run.iterdir() if ep.is_dir()):
            raise SystemExit(f"refusing to freeze: main-phase episodes already started in {run}")
    manifest = {"frozen_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "note": a.note,
                "amendment": {str(a.amendment): sha(a.amendment)},
                "instrument": {f: sha(HERE / f) for f in INSTRUMENT}}
    out = HERE / (f"MANIFEST.sha256.{a.version}.json" if a.version else "MANIFEST.sha256.json")
    if out.exists():
        raise SystemExit("MANIFEST.sha256.json exists; a new freeze needs a new version directory")
    out.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
