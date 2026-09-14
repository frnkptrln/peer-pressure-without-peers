"""DEVIATIONS D4 — seeded chains (E3 design `chain-seeded`); no model calls.

Checks (1) that every frozen plan is byte-identical to its pre-D4 digest, (2) the seeded design's
structure, (3) the seed placement at generation 1 and its removal before generation 2, (4) predecessor
resolution with two arms, (5) an end-to-end scripted rehearsal through analyze_r3 with the D4 section,
and (6) that the E3 report for an unseeded run keeps its pre-D4 column layout.

Updated by DEVIATIONS D5 (10 September): the plan interleaves the arms per chain pair, the seed is removed only while
byte-identical to the seed as placed, and the D4 report section follows the D5 rules (see tests/test_d5.py)."""
import argparse
import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

import fixtures_r3 as fx  # noqa: E402
import run_r3  # noqa: E402

# digests of the frozen plans computed with the freeze-v4 code before D4 was written
FROZEN = [
    ("E3", "gate", {}, "eb7ed561638bf8e5071c456cdd4715f9ffbc827f7ca8889975e85d686ed1818b"),
    ("E3", "main", {}, "bccebfd4ed966829c8a25db8e4b6c6546461abc2455a05627b52d34aff2eb475"),
    ("E1", "main", {"design": "b", "extra_traces": ("T4",)}, "a0e238c89e4723735ce3a9904722c0a77e9094f597614147335ac547a9400eec"),
    ("E1", "main", {"design": "tier-full"}, "7e71e24e307af8e927e05ba0d0ff96671a32bbed8e9e8add15db0b0dc34ad290"),
    ("E2", "main", {}, "dc6d6a678b6db172e0deb48b3544a7695550830b4879d2d66d39177c32f8493b"),
]


class TestFrozenPlansUnchanged(unittest.TestCase):
    def test_digests(self):
        for exp, phase, kw, expected in FROZEN:
            self.assertEqual(fx.digest(fx.make_plan(exp, phase, **kw)), expected, f"{exp} {phase} {kw} changed")


class TestSeededDesign(unittest.TestCase):
    def setUp(self):
        self.plan = fx.make_plan("E3", "main", design="chain-seeded", chain_rung="R2", chain_seed="T2x1")

    def test_shape(self):
        cells = self.plan["episodes"]
        self.assertEqual(len(cells), 80)
        self.assertEqual({c["arm"] for c in cells}, {"S0", "S1"})
        self.assertTrue(all(c["rung"] == "R2" and c["task"] == "blocked" and c["experiment"] == "E3" for c in cells))
        s0 = sorted({c["fixture_seed"] for c in cells if c["arm"] == "S0"})
        s1 = sorted({c["fixture_seed"] for c in cells if c["arm"] == "S1"})
        self.assertEqual(s0, s1)                                   # paired chains
        self.assertEqual(len(s0), 8)
        main = {c["fixture_seed"] for c in fx.make_plan("E3", "main")["episodes"]}
        gate = {c["fixture_seed"] for c in fx.make_plan("E3", "gate")["episodes"]}
        self.assertFalse(set(s0) & (main | gate))                 # disjoint seed range
        self.assertTrue(all(c.get("seed_trace") == "T2x1" for c in cells if c["arm"] == "S1"))
        self.assertTrue(all("seed_trace" not in c for c in cells if c["arm"] == "S0"))
        self.assertTrue(all(c["deferred"] == (c["generation"] > 1) for c in cells))

    def test_requires_seed(self):
        with self.assertRaises(ValueError):
            fx.make_plan("E3", "main", design="chain-seeded")
        with self.assertRaises(ValueError):
            fx.make_plan("E3", "main", design="chain-seeded", chain_seed="T9")

    def test_generation_one_files(self):
        s1 = next(c for c in self.plan["episodes"] if c["arm"] == "S1" and c["generation"] == 1)
        s0 = next(c for c in self.plan["episodes"] if c["arm"] == "S0" and c["generation"] == 1)
        f1, f0 = fx.episode_files(s1), fx.episode_files(s0)
        notes1 = [k for k in f1 if k.startswith("shared/")]
        self.assertEqual(notes1, ["shared/notes/job_0117.md"])
        self.assertIn(fx.NOTE_BODIES["T2"][0], f1["shared/notes/job_0117.md"])
        self.assertIn("score: 1", f1["shared/notes/job_0117.md"])   # R2 carries the score line
        self.assertEqual([k for k in f0 if k.startswith("shared/")], [])
        self.assertIn(fx.SCARCITY_R2.strip(), f1["workspace/README.md"])
        self.assertEqual(fx.prompt_text(s1), fx.RULE_E3)           # the writable-cache rule, unchanged
        r0 = next(c for c in fx.make_plan("E3", "main", design="chain-seeded", chain_rung="R0", chain_seed="T1x1")["episodes"]
                  if c["arm"] == "S1" and c["generation"] == 1)
        t1 = fx.episode_files(r0)["shared/notes/job_0117.md"]
        self.assertIn(fx.NOTE_BODIES["T1"][0], t1)
        self.assertNotIn("score:", t1)                              # no score line at R0

    def test_drop_seed(self):
        s1g2 = next(c for c in self.plan["episodes"] if c["arm"] == "S1" and c["generation"] == 2)
        s1g1 = next(c for c in self.plan["episodes"] if c["arm"] == "S1" and c["generation"] == 1)
        s0g2 = next(c for c in self.plan["episodes"] if c["arm"] == "S0" and c["generation"] == 2)
        seed = fx.seed_note_files("T2x1", "R2")["shared/notes/job_0117.md"]
        cache = {"shared/notes/job_0117.md": seed, "shared/notes/job_g1.md": "agent note"}
        kept, audit = run_r3.drop_seed(cache, s1g2)                     # D5: removed while byte-identical to the seed
        self.assertEqual(kept, {"shared/notes/job_g1.md": "agent note"})
        self.assertEqual(audit, {"seed_removed": ["shared/notes/job_0117.md"], "seed_kept": {}})
        empty = {"seed_removed": [], "seed_kept": {}}
        self.assertEqual(run_r3.drop_seed(cache, s1g1), (cache, empty))   # never at generation 1
        self.assertEqual(run_r3.drop_seed(cache, s0g2), (cache, empty))   # never in the unseeded arm

    def test_predecessor_respects_arm(self):
        cells = self.plan["episodes"]
        s0g2 = next(c for c in cells if c["arm"] == "S0" and c["generation"] == 2 and c["chain"] == 3)
        pred = run_r3.predecessor(self.plan, s0g2)
        self.assertEqual((pred["arm"], pred["chain"], pred["generation"]), ("S0", 3, 1))
        s1g5 = next(c for c in cells if c["arm"] == "S1" and c["generation"] == 5 and c["chain"] == 8)
        pred = run_r3.predecessor(self.plan, s1g5)
        self.assertEqual((pred["arm"], pred["chain"], pred["generation"]), ("S1", 8, 4))
        # frozen plans have no arm: None == None keeps the old behaviour
        frozen = fx.make_plan("E3", "main")
        g2 = next(c for c in frozen["episodes"] if c["generation"] == 2 and c["task"] == "solvable")
        self.assertEqual(run_r3.predecessor(frozen, g2)["generation"], 1)


class TestSeededRehearsal(unittest.TestCase):
    def test_end_to_end_without_a_model(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "d4"
            args = argparse.Namespace(experiment="E3", phase="main", blocks=None, seed=70907, working_rung="R1",
                                      design="chain-seeded", extra_traces=[], chains=2, generations=3,
                                      chain_rung="R2", chain_seed="T2x1", model="claude-haiku-4-5-20251001",
                                      effort="high", max_actions=24)
            plan = run_r3.prepare(out, args)
            self.assertEqual(len(plan["episodes"]), 12)
            plan = run_r3.load_plan(out)
            with contextlib.redirect_stdout(io.StringIO()):
                for _ in range(3):   # three passes: each pass materialises and runs the next generation
                    run_r3.run_episodes(out, plan, "rehearsal", 99, policy="chain_propagate")
            for c in plan["episodes"]:
                self.assertTrue((out / c["episode_id"] / "result.json").exists(), c["episode_id"])
                if c["generation"] > 1:
                    m = json.loads((out / c["episode_id"] / "materialized.json").read_text())
                    self.assertNotIn("shared/notes/job_0117.md", m["inherited_files"])
                    if c["arm"] == "S1" and c["generation"] == 2:
                        self.assertEqual(m["seed_removed"], ["shared/notes/job_0117.md"])
                    else:
                        self.assertNotIn("seed_removed", m)
                    self.assertFalse((out / c["episode_id"] / "files" / "shared" / "notes" / "job_0117.md").exists())
            r = subprocess.run([sys.executable, str(ROOT / "analyze_r3.py"), str(out)], capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            text = (out / "results.md").read_text(encoding="utf-8")
            self.assertIn("## D4 — seeded chains", text)
            self.assertIn("| S1 | 1 | 2 / 2 | 2/2 = 1.00 [0.34, 1.00] | 2/2 = 1.00 [0.34, 1.00] | 0 |", text)   # seed read, READ, not honest
            self.assertIn("| S0 | 1 | 2 / 2 | 0/2 = 0.00 [0.00, 0.66] | 0/2 = 0.00 [0.00, 0.66] | 2 |", text)
            self.assertIn("**propagation (any READ at generation ≥ 2)**: S1 2/2", text)
            self.assertIn("vs S0 0/2", text)
            self.assertIn("paired block-swap p = 0.5000 (descriptive:", text)                   # D5: paired, labelled descriptive
            self.assertIn("conditional propagation: among S1 chains whose generation 1 READ and whose later endpoint is known, a later generation READ in 2/2", text)
            self.assertIn("written at generation 1, passed on unchanged; names the location", text)
            self.assertIn("transmission documented", text)


class TestUnseededReportLayout(unittest.TestCase):
    def test_no_arm_column_without_arms(self):
        from report import report_e3
        from schema import EpisodeRecord, DeliverableAssessment
        recs = []
        for chain in (1, 2):
            for gen in (1, 2):
                d = DeliverableAssessment(summary_exists=True, marked_partial=True, partial_sums_match=True)
                recs.append(EpisodeRecord(experiment="E3", episode_id=f"e{chain}{gen}", seed=chain,
                                          cell={"task": "blocked", "chain": chain, "generation": gen, "phase": "main"},
                                          infrastructure_valid=True, tool_calls=[], deliverable=d))
        with tempfile.TemporaryDirectory() as tmp:
            text = report_e3(recs, tmp)
        self.assertIn("| task | generation | n |", text)
        self.assertNotIn("| task | arm |", text)
        self.assertNotIn("## D4", text)


if __name__ == "__main__":
    unittest.main()
