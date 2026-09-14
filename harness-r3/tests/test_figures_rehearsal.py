"""The analysis-side figure generators against rehearsal data (no model calls; `analysis/figures.py` is outside the
frozen instrument). Prepares small E2, E3 and seeded-chain plans, runs them with the rehearsal backend through
`analyze_r3.py`, then draws e2_reporting.png, e3_channel.png and d4_chains.png from the resulting records."""
import argparse
import contextlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

import run_r3  # noqa: E402

FIGURES = ROOT.parent / "analysis" / "figures.py"


def have_mpl():
    try:
        import matplotlib  # noqa: F401
        return True
    except Exception:
        return False


def rehearse(out, args, passes=1, policy="honest", only=None):
    run_r3.prepare(out, args)
    plan = run_r3.load_plan(out)
    with contextlib.redirect_stdout(io.StringIO()):
        for _ in range(passes):
            run_r3.run_episodes(out, plan, "rehearsal", 999, policy=policy, only=only)
    r = subprocess.run([sys.executable, str(ROOT / "analyze_r3.py"), str(out)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    r = subprocess.run([sys.executable, str(FIGURES), str(out)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout


@unittest.skipUnless(have_mpl(), "matplotlib not importable")
class TestFiguresFromRehearsal(unittest.TestCase):
    def test_e2_e3_d4(self):
        with tempfile.TemporaryDirectory() as tmp:
            e2 = Path(tmp) / "e2"
            rehearse(e2, argparse.Namespace(experiment="E2", phase="main", blocks=2, seed=90907, working_rung="R1", design="a",
                                            extra_traces=[], chains=8, generations=5, chain_rung="R0", chain_seed=None,
                                            model="claude-opus-5", effort="high", max_actions=24))
            self.assertTrue((e2 / "reports" / "e2_reporting.png").exists())
            e3 = Path(tmp) / "e3"
            rehearse(e3, argparse.Namespace(experiment="E3", phase="gate", blocks=None, seed=90907, working_rung="R1", design="a",
                                            extra_traces=[], chains=2, generations=3, chain_rung="R0", chain_seed=None,
                                            model="claude-opus-5", effort="high", max_actions=24), passes=3)
            self.assertTrue((e3 / "reports" / "e3_channel.png").exists())
            self.assertFalse((e3 / "reports" / "d4_chains.png").exists())
            d4 = Path(tmp) / "d4"
            out = rehearse(d4, argparse.Namespace(experiment="E3", phase="main", blocks=None, seed=90907, working_rung="R1",
                                                  design="chain-seeded", extra_traces=[], chains=2, generations=3, chain_rung="R2",
                                                  chain_seed="T2x1", model="claude-haiku-4-5-20251001", effort="high", max_actions=24),
                           passes=3, policy="chain_propagate")
            self.assertIn("d4_chains.png", out)
            self.assertGreater(os.path.getsize(d4 / "reports" / "d4_chains.png"), 20000)
            # a generation-1-only run (the first wave) draws too, with generations ≥ 2 shown as unobserved
            w1 = Path(tmp) / "wave1"
            rehearse(w1, argparse.Namespace(experiment="E3", phase="main", blocks=None, seed=90907, working_rung="R1",
                                            design="chain-seeded", extra_traces=[], chains=2, generations=3, chain_rung="R2",
                                            chain_seed="T2x1", model="claude-haiku-4-5-20251001", effort="high", max_actions=24),
                     passes=1, policy="chain_propagate", only="generation=1")
            self.assertTrue((w1 / "reports" / "d4_chains.png").exists())


if __name__ == "__main__":
    unittest.main()
