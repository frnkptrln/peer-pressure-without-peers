"""The sprint tooling outside the frozen instrument, exercised without a model: the autonomous runner (both D4 gate
paths, restartability, the analysis-only phase), the results-block generator, and the coding sheet / model-coder stub /
κ pipeline on the E1 gate's real transcripts."""
import csv
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ANALYSIS = ROOT.parent / "analysis"
PY = sys.executable


def run(args, cwd=ROOT):
    r = subprocess.run([PY] + [str(a) for a in args], cwd=cwd, capture_output=True, text=True)
    return r


class TestAutorun(unittest.TestCase):
    def test_d4_continue_and_stop_paths(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ROOT / "sprint_autorun.py", "--phase", "d4", "--backend", "rehearsal", "--runs", tmp, "--rehearsal-policy", "chain_propagate"])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("D4 gate after wave 1: **CONTINUE**", r.stdout)
            self.assertIn("generation=5: done", r.stdout)
            self.assertTrue((Path(tmp) / "d4-haiku" / "d4_gate_verdict.json").exists())
            self.assertEqual(sum(1 for _ in (Path(tmp) / "d4-haiku").glob("e3-main-*/result.json")), 80)
            # restart: nothing rerun, phase completes again
            r2 = run([ROOT / "sprint_autorun.py", "--phase", "d4", "--backend", "rehearsal", "--runs", tmp])
            self.assertEqual(r2.returncode, 0, r2.stderr)
            self.assertIn("already prepared — resuming", r2.stdout)
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ROOT / "sprint_autorun.py", "--phase", "d4", "--backend", "rehearsal", "--runs", tmp, "--rehearsal-policy", "honest"])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("D4 gate after wave 1: **STOP**", r.stdout)
            self.assertNotIn("generation=2", r.stdout)
            self.assertEqual(sum(1 for _ in (Path(tmp) / "d4-haiku").glob("e3-main-*/result.json")), 16)

    def test_friday_phase_and_results_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ROOT / "sprint_autorun.py", "--phase", "friday", "--backend", "rehearsal", "--runs", tmp])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("phase friday done", r.stdout)
            self.assertTrue((Path(tmp) / "e1-main" / "results.md").exists())
            self.assertTrue((Path(tmp) / "e5-haiku" / "reports" / "e1tier-full_outcomes.png").exists() or
                            any((Path(tmp) / "e5-haiku" / "reports").glob("*.png")))
            r = run([ANALYSIS / "results_blocks.py", tmp])
            self.assertEqual(r.returncode, 0, r.stderr)
            text = (Path(tmp) / "RESULTS_BLOCKS.md").read_text(encoding="utf-8")
            self.assertIn("## P1 §4.2 — E1 main", text)
            self.assertIn("| R2×T4 | main | 16 |", text)
            self.assertIn("run `e2-main` not present — placeholder stays", text)
            r = run([ROOT / "sprint_autorun.py", "--phase", "analysis", "--backend", "rehearsal", "--runs", tmp])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("analysis phase done", r.stdout)


class TestCodingPipeline(unittest.TestCase):
    def test_sheet_stub_kappa_on_the_gate(self):
        gate = ROOT / "runs" / "e1-gate"
        if not (gate / "records.jsonl").exists():
            self.skipTest("E1 gate run not present")
        with tempfile.TemporaryDirectory() as tmp:
            r = run([ANALYSIS / "coding_sheet.py", "sheet", gate, "--n", "4", "--seed", "3", "--out", tmp])
            self.assertEqual(r.returncode, 0, r.stderr)
            info = json.loads(r.stdout)
            self.assertEqual(len(info["episodes"]), 4)
            rows = list(csv.DictReader((Path(tmp) / "sheet.csv").open(encoding="utf-8")))
            self.assertEqual(len(rows), 4)
            for row in rows:
                t = (Path(tmp) / row["transcript"]).read_text(encoding="utf-8")
                self.assertIn("**assistant:**", t)
                if row["trace"] == "T2":
                    self.assertIn("[note redacted]", t)
                    self.assertNotIn("I read it from there", t)          # the violating note's text never reaches the coder
            r = run([ANALYSIS / "coding_sheet.py", "code", tmp, "--backend", "stub"])
            self.assertEqual(r.returncode, 0, r.stderr)
            rows = list(csv.DictReader((Path(tmp) / "sheet.csv").open(encoding="utf-8")))
            self.assertTrue(all(row["model_boundary_handling"] in ("held", "crossed", "probed") for row in rows))
            for row in rows:
                for ax in ("boundary_handling", "justification", "social_reference", "injection_framing", "test_awareness"):
                    row["human_" + ax] = row["model_" + ax]
            with (Path(tmp) / "sheet.csv").open("w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
                w.writeheader()
                w.writerows(rows)
            r = run([ANALYSIS / "coding_sheet.py", "kappa", Path(tmp) / "sheet.csv"])
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("| boundary_handling | 4 | 1.00 |", r.stdout)


if __name__ == "__main__":
    unittest.main()
