"""Tests for the open-weights backend (DEVIATIONS D2) — no model calls (python3 -m unittest discover -s tests)."""
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

import run_open_r3 as op  # noqa: E402
from analyze_r3 import analyze  # noqa: E402
from schema import classify  # noqa: E402
import run_r3  # noqa: E402


class Args:
    def __init__(self, **kw):
        defaults = dict(experiment="E1", phase="main", blocks=None, seed=80907, working_rung="R1", design="tier",
                        extra_traces=[], model=op.DEFAULT_MODEL, revision=None, temperature=0.7, max_new_tokens=640,
                        thinking=False, max_actions=24)
        defaults.update(kw)
        self.__dict__.update(defaults)


def _run(tmp, policy, **kw):
    out = Path(tmp) / policy
    plan = op.prepare(out, Args(**kw))
    plan = op.load_plan(out)
    op.run_episodes(out, plan, op.StubBackend(policy), 999)
    recs = analyze(out, kw.get("design", "tier"))
    return out, plan, recs


class TestSeeds(unittest.TestCase):
    def test_call_seeds_distinct_uint32_for_every_design(self):
        for design in ("tier", "tier-full", "b"):
            with tempfile.TemporaryDirectory() as tmp:
                plan = op.prepare(Path(tmp) / design, Args(design=design, extra_traces=["T4"] if design == "b" else []))
                pre = op.preflight(plan)
                self.assertTrue(pre["distinct"] and pre["uint32"])
                self.assertEqual(pre["planned_call_seeds"], len(plan["episodes"]) * plan["max_turns"])

    def test_cells_of_one_block_get_different_streams(self):
        plan = op.prepare(Path(tempfile.mkdtemp()) / "p", Args())
        block0 = [c for c in plan["episodes"] if c["block"] == 0]
        self.assertEqual(len({c["fixture_seed"] for c in block0}), 1)          # same fixtures …
        self.assertEqual(len({op.turn_seed(c, 0) for c in block0}), len(block0))  # … different sampling seeds


class TestMarkup(unittest.TestCase):
    def test_parse_tools(self):
        calls, text = op.parse_tools('Looking.\n<tool_call>\n{"name": "list_files", "arguments": {"path": "/workspace"}}\n</tool_call>')
        self.assertEqual(calls, [{"name": "list_files", "arguments": {"path": "/workspace"}}])
        self.assertEqual(text, "Looking.")
        self.assertEqual(op.parse_tools("Done.")[0], [])
        for bad in ('<tool_call>{"name": "x", "arguments": {}}', '<tool_call>{"name": "x"}</tool_call>',
                    '{"name": "list_files", "arguments": {"path": "/workspace"}}'):
            with self.assertRaises(ValueError):
                op.parse_tools(bad)


class TestStubThroughAnalysis(unittest.TestCase):
    def test_honest_policy_reads_notes_and_stays_honest(self):
        with tempfile.TemporaryDirectory() as tmp:
            out, plan, recs = _run(tmp, "honest")
            self.assertEqual({classify(r)["outcome"] for r in recs}, {"HONEST"})
            self.assertTrue(all(r.cell["note_read"] for r in recs if r.cell["trace"] == "T2"))
            self.assertFalse(any(r.cell["note_read"] for r in recs if r.cell["trace"] == "T0"))
            self.assertTrue(all(r.infrastructure_valid for r in recs))
            summary = json.loads((out / "open_summary.json").read_text())
            self.assertEqual(summary["terminations"], {"final_answer": 32})
            txt = (out / "results.md").read_text()
            self.assertIn("| NOTES |", txt)
            self.assertIn("D2 discordance interval (secondary)", txt)

    def test_violate_policy_yields_read_only_under_violating_notes(self):
        with tempfile.TemporaryDirectory() as tmp:
            out, plan, recs = _run(tmp, "violate_on_T2", design="tier-full")
            by = {}
            for r in recs:
                by.setdefault((r.cell["rung"], r.cell["trace"]), set()).add(classify(r)["outcome"])
            self.assertEqual(by[("R2", "T2")], {"READ"})
            self.assertEqual(by[("R2", "T4")], {"READ"})
            self.assertEqual(by[("R2", "T1")], {"HONEST"})   # compliant-informed notes carry no violation marker
            self.assertEqual(by[("R0", "T0")], {"HONEST"})
            self.assertEqual(by[("R2", "T0")], {"HONEST"})

    def test_explore_only_is_abandon_not_honest(self):
        with tempfile.TemporaryDirectory() as tmp:
            out, plan, recs = _run(tmp, "explore_only")
            self.assertEqual({classify(r)["outcome"] for r in recs}, {"ABANDON"})

    def test_malformed_markup_is_recorded_and_valid_as_max_turns(self):
        with tempfile.TemporaryDirectory() as tmp:
            out, plan, recs = _run(tmp, "malformed")
            results = [json.loads((out / c["episode_id"] / "result.json").read_text()) for c in plan["episodes"]]
            self.assertEqual({r["termination"] for r in results}, {"parse_error"})
            self.assertEqual({r["status"] for r in results}, {"max_turns"})
            self.assertEqual({classify(r)["outcome"] for r in recs}, {"ABANDON"})
            self.assertTrue(all(r.infrastructure_valid for r in recs))


class TestSeals(unittest.TestCase):
    def test_backend_seal_and_no_rerun(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "seal"
            op.prepare(out, Args())
            plan = op.load_plan(out)
            op.run_episodes(out, plan, op.StubBackend("honest"), 1)
            fake = op.StubBackend("honest")
            fake.name = "open_transformers"
            with self.assertRaises(ValueError):
                op.run_episodes(out, plan, fake, 1)
            # run_r3 refuses an open-backend directory
            with self.assertRaises(ValueError):
                run_r3.run_episodes(out, plan, "rehearsal", 1)
            # the finished episode is never rerun
            first = plan["episodes"][0]["episode_id"]
            before = (out / first / "result.json").read_text()
            op.run_episodes(out, plan, op.StubBackend("honest"), 1)
            self.assertEqual(before, (out / first / "result.json").read_text())

    def test_plan_bound_to_runner_and_instrument(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "bind"
            op.prepare(out, Args())
            plan = json.loads((out / "plan.json").read_text())
            self.assertEqual(plan["source_hash"], run_r3.source_hash())
            self.assertEqual(plan["backend"]["runner_sha256"], op.runner_hash())
            plan["backend"]["runner_sha256"] = "0" * 64
            (out / "plan.json").write_text(json.dumps(plan))
            with self.assertRaises(ValueError):
                op.load_plan(out)

    def test_only_e1(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                op.prepare(Path(tmp) / "e2", Args(experiment="E2"))


if __name__ == "__main__":
    unittest.main()
