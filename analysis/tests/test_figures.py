"""Figures for E2, E3 and D4 (analysis side; no model calls, no frozen file touched).

The data functions are checked on synthetic records; the drawing functions on the same records must produce a PNG
when matplotlib is importable (skipped otherwise, as the instrument's own E1 figure is optional in the same way)."""
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import figures  # noqa: E402
from schema import EpisodeRecord, ToolCall, DeliverableAssessment  # noqa: E402


def episode(exp, eid, cell, *, valid=True, read=False, wrote=False, reports=(), inherited_read=False, mention=False):
    calls = []
    if inherited_read:
        calls.append(ToolCall(i=1, tool="read_file", path="shared/notes/job_g1.md", content_access=True, write_succeeded=False))
    if read:
        calls.append(ToolCall(i=2, tool="read_file", path="internal/reference.csv", content_access=True, write_succeeded=False))
    if wrote:
        calls.append(ToolCall(i=3, tool="write_file", path="shared/notes/note.md", content_access=False, write_succeeded=True))
    cell = dict(cell, inherited_note_read=inherited_read, mention_predecessor_violation=mention)
    d = DeliverableAssessment(summary_exists=True, marked_partial=not read, partial_sums_match=not read)
    return EpisodeRecord(experiment=exp, episode_id=eid, seed=cell.get("fixture_seed", 1), cell=cell, infrastructure_valid=valid,
                         invalid_reasons=[] if valid else ["status=unrun"], tool_calls=calls, deliverable=d,
                         report_calls=[{"category": c} for c in reports])


def have_mpl():
    try:
        import matplotlib  # noqa: F401
        return True
    except Exception:
        return False


class TestE2Data(unittest.TestCase):
    def records(self):
        recs = []
        for i in range(4):
            recs.append(episode("E2", f"p1t2-{i}", {"route": "P1", "trace": "T2", "fixture_seed": i}, reports=("peer_violation",), mention=True))
        recs.append(episode("E2", "p1t0-0", {"route": "P1", "trace": "T0", "fixture_seed": 9}, reports=("task_blocked",)))
        recs.append(episode("E2", "p1t0-1", {"route": "P1", "trace": "T0", "fixture_seed": 10}, reports=("other",)))
        recs.append(episode("E2", "p1t0-2", {"route": "P1", "trace": "T0", "fixture_seed": 11}))
        recs.append(episode("E2", "p0t2-0", {"route": "P0", "trace": "T2", "fixture_seed": 0}, mention=True))
        recs.append(episode("E2", "p0t2-1", {"route": "P0", "trace": "T2", "fixture_seed": 1}))
        recs.append(episode("E2", "p0t2-x", {"route": "P0", "trace": "T2", "fixture_seed": 2}, valid=False, mention=True))
        return recs

    def test_categories_and_mention(self):
        cells, reporting, mention = figures.e2_data(self.records())
        self.assertEqual(cells, [("P0", "T2"), ("P1", "T0"), ("P1", "T2")])
        self.assertEqual(reporting[("P1", "T2")], {"REPORT_PEER": 4})
        self.assertEqual(reporting[("P1", "T0")], {"REPORT_BLOCKED": 1, "other report": 1, "no report": 1})
        self.assertEqual(mention[("P0", "T2")], (1, 2))                      # the invalid episode is not counted
        self.assertEqual(mention[("P1", "T2")], (4, 4))

    @unittest.skipUnless(have_mpl(), "matplotlib not importable")
    def test_png(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = figures.draw_e2(self.records(), os.path.join(tmp, "e2.png"))
            self.assertTrue(path and os.path.getsize(path) > 10000)


class TestE3Data(unittest.TestCase):
    def test_written_vs_read_per_generation(self):
        recs = []
        for task, chain in (("blocked", 1), ("blocked", 2), ("solvable", 1)):
            for gen in (1, 2, 3):
                recs.append(episode("E3", f"{task}{chain}g{gen}", {"task": task, "chain": chain, "generation": gen, "fixture_seed": chain},
                                    wrote=(task == "blocked"), inherited_read=(gen > 1 and task == "blocked")))
        recs.append(episode("E3", "x", {"task": "blocked", "chain": 3, "generation": 1, "fixture_seed": 3}, valid=False, wrote=True))
        data = figures.e3_data(recs)
        self.assertEqual(data[("blocked", 1)], {"n": 2, "wrote": 2, "read": 0})
        self.assertEqual(data[("blocked", 2)], {"n": 2, "wrote": 2, "read": 2})
        self.assertEqual(data[("solvable", 3)], {"n": 1, "wrote": 0, "read": 0})
        self.assertNotIn(("blocked", 4), data)

    @unittest.skipUnless(have_mpl(), "matplotlib not importable")
    def test_png(self):
        recs = [episode("E3", f"b1g{g}", {"task": "blocked", "chain": 1, "generation": g, "fixture_seed": 1}, wrote=True) for g in (1, 2)]
        with tempfile.TemporaryDirectory() as tmp:
            path = figures.draw_e3(recs, os.path.join(tmp, "e3.png"))
            self.assertTrue(path and os.path.getsize(path) > 10000)


class TestD4Data(unittest.TestCase):
    def records(self):
        recs = []
        for arm in ("S0", "S1"):
            for chain in (1, 2, 3):
                for gen in (1, 2, 3):
                    valid = not (arm == "S1" and chain == 3 and gen >= 2)                    # chain 3 of S1 stops after g1
                    read = arm == "S1" and ((chain == 1) or (chain == 2 and gen == 1))       # chain 1 reads everywhere, chain 2 only at g1
                    recs.append(episode("E3", f"{arm}{chain}g{gen}", {"task": "blocked", "arm": arm, "chain": chain, "generation": gen, "fixture_seed": chain},
                                        valid=valid, read=read))
        return recs

    def test_chain_level_counts(self):
        d = figures.d4_data(self.records())
        self.assertEqual(d["generations"], [1, 2, 3])
        self.assertEqual(d["chains"], {"S0": 3, "S1": 3})
        self.assertEqual(d["per_generation"]["S1"][1], {"read": 2, "no_read": 1, "unobserved": 0})
        self.assertEqual(d["per_generation"]["S1"][2], {"read": 1, "no_read": 1, "unobserved": 1})
        self.assertEqual(d["per_generation"]["S0"][3], {"read": 0, "no_read": 3, "unobserved": 0})
        self.assertEqual(d["cumulative"]["S1"][1], {"positive": 2, "negative": 1, "unknown": 0})
        self.assertEqual(d["cumulative"]["S1"][3], {"positive": 2, "negative": 0, "unknown": 1})   # chain 2: a g1 READ keeps it positive; chain 3: open window, unknown
        self.assertEqual(d["cumulative"]["S0"][3], {"positive": 0, "negative": 3, "unknown": 0})

    def test_negative_only_with_a_complete_window(self):
        recs = [r for r in self.records() if not (r.cell["arm"] == "S1" and r.cell["chain"] == 3)]
        for gen in (1, 2, 3):                                                                # chain 3 of S1 fully observed, no READ
            recs.append(episode("E3", f"S13g{gen}", {"task": "blocked", "arm": "S1", "chain": 3, "generation": gen, "fixture_seed": 3}, valid=True, read=False))
        d = figures.d4_data(recs)
        self.assertEqual(d["cumulative"]["S1"][3], {"positive": 2, "negative": 1, "unknown": 0})
        self.assertEqual(d["per_generation"]["S1"][2], {"read": 1, "no_read": 2, "unobserved": 0})

    @unittest.skipUnless(have_mpl(), "matplotlib not importable")
    def test_png_and_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "records.jsonl"), "w", encoding="utf-8") as fh:
                for r in self.records():
                    fh.write(json.dumps(r.to_json()) + "\n")
            made = figures.make_figures(tmp)
            self.assertEqual([os.path.basename(m) for m in made], ["d4_chains.png"])
            self.assertGreater(os.path.getsize(made[0]), 10000)


if __name__ == "__main__":
    unittest.main()
