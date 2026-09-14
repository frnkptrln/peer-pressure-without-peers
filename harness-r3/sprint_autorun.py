#!/usr/bin/env python3
"""Autonomous runner for the sprint batches — the runbook, executed by a script (outside the frozen instrument).

  python3 sprint_autorun.py --phase friday                     # E1 main (b + T4, 64) → E5 Haiku tier-full (96)
  python3 sprint_autorun.py --phase saturday                   # E3 main (80) → D4 seeded chains (wave 1, gate, waves 2–5)
                                                               #   → E2 main (48) → E5 Sonnet (32) → E4 sweep (360 calls)
  python3 sprint_autorun.py --phase d4                         # the seeded chains alone
  python3 sprint_autorun.py --phase all                        # friday then saturday
  python3 sprint_autorun.py --phase analysis                   # re-analyse and redraw every run directory; no model call
  python3 sprint_autorun.py --phase check                      # before a start: doctor, freeze verification, tests, quota; no model call
  … --backend rehearsal [--rehearsal-policy chain_propagate]   # the same mechanics without a model (tests, dry runs)

What it does per batch, exactly as RUNBOOK_sprint.md: quota check (§12.4: no batch above 80 % seven-day / 85 % five-hour;
if above, it waits for the window to reset — the reading comes from the last live episode's rate_limit_event) → prepare
(skipped when the directory already holds a plan: the script is restartable and never reruns an episode) → four
streams → wait → continuation rounds for streams that stopped on a transport/infrastructure error (finished and
interrupted episodes are skipped by the runner itself) → analyze → figures. Chain designs run wave-wise (one generation
per wave across all chains, both arms adjacent in slot order). The seeded chains apply the D5 continuation rule after
wave 1 through d4_gate.py and log the verdict with its numbers. Everything is appended to runs/AUTORUN_LOG.md.

Nothing here changes a plan, a prompt or an outcome; it only issues the runbook's commands in the runbook's order.
"""
import argparse
import glob
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = sys.executable
LOG_DIR = HERE / "logs"          # set per run root in main(): <runs>/_logs
HAIKU = "claude-haiku-4-5-20251001"
SONNET = "claude-sonnet-5"


# ---------------------------------------------------------------------------- batches

def batches(phase, runs):
    """The runbook as data. kind: 'stream' (one wave), 'waves' (chain designs), 'd4' (seeded chains with the gate), 'e4'."""
    fri = [
        dict(name="E1 main (b + T4)", out=f"{runs}/e1-main", kind="stream", design="b",
             prepare=["run_r3.py", "prepare", "--experiment", "E1", "--phase", "main", "--design", "b", "--extra-traces", "T4"]),
        dict(name="E5 Haiku tier-full (D1)", out=f"{runs}/e5-haiku", kind="stream", design="tier-full",
             prepare=["run_r3.py", "prepare", "--experiment", "E1", "--phase", "main", "--design", "tier-full", "--model", HAIKU]),
    ]
    d4 = [
        dict(name="D4 seeded chains on Haiku (D5 waves + gate)", out=f"{runs}/d4-haiku", kind="d4", design=None, generations=5,
             prepare=["run_r3.py", "prepare", "--experiment", "E3", "--phase", "main", "--design", "chain-seeded",
                      "--chain-rung", "R2", "--chain-seed", "T2x1", "--model", HAIKU]),
    ]
    sat = [
        dict(name="E3 main (chains, blocked + solvable)", out=f"{runs}/e3-main", kind="waves", design=None, generations=5,
             prepare=["run_r3.py", "prepare", "--experiment", "E3", "--phase", "main"]),
    ] + d4 + [
        dict(name="E2 main (reporting route)", out=f"{runs}/e2-main", kind="stream", design=None,
             prepare=["run_r3.py", "prepare", "--experiment", "E2", "--phase", "main"]),
        dict(name="E5 Sonnet tier", out=f"{runs}/e5-sonnet", kind="stream", design="tier",
             prepare=["run_r3.py", "prepare", "--experiment", "E1", "--phase", "main", "--design", "tier", "--model", SONNET]),
        dict(name="E4 declarative sweep (D3 plan)", out=f"{runs}/e4", kind="e4", design=None,
             prepare=["sweep_e4.py", "prepare", "--nsim", "10"]),
    ]
    return {"friday": fri, "saturday": sat, "d4": d4, "all": fri + sat, "analysis": [], "check": []}[phase]


# ---------------------------------------------------------------------------- helpers

class Log:
    def __init__(self, path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def __call__(self, msg):
        line = f"- {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())} — {msg}"
        print(line, flush=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")


def quota_reading(runs):
    """Last rate_limit_event under runs/ (the same source as quota.py). Returns (five_hour, seven_day, resets) or None."""
    files = sorted(glob.glob(os.path.join(runs, "*", "*", "stdout.jsonl")), key=os.path.getmtime)
    last = None
    for f in files[-5:]:
        try:
            for line in open(f, encoding="utf-8"):
                if '"rate_limit_event"' in line:
                    try:
                        last = json.loads(line)
                    except json.JSONDecodeError:
                        pass
        except OSError:
            pass
    if not last:
        return None
    info = last["rate_limit_info"]["unifiedWindows"]
    return {"five_hour": info["five_hour"]["utilization"], "seven_day": info["seven_day"]["utilization"],
            "resets": {w: info[w]["resetsAt"] for w in ("five_hour", "seven_day")}}


def wait_for_quota(runs, log, backend, max_wait_h):
    """§12.4. With no reading at all (first live batch of a fresh tree) the batch starts and produces one."""
    if backend != "claude":
        return True
    deadline = time.time() + max_wait_h * 3600
    while True:
        q = quota_reading(runs)
        if q is None:
            log("quota: no rate_limit_event under runs/ yet — starting; the first episode produces a reading")
            return True
        ok = q["seven_day"] <= 0.80 and q["five_hour"] <= 0.85
        log(f"quota: five_hour {q['five_hour']:.0%}, seven_day {q['seven_day']:.0%} → {'allowed' if ok else 'NOT allowed'} (§12.4)")
        if ok:
            return True
        over = "seven_day" if q["seven_day"] > 0.80 else "five_hour"
        until = q["resets"][over] + 120
        if until > deadline:
            log(f"quota: {over} window resets at {time.strftime('%H:%M UTC', time.gmtime(until))}, beyond the wait limit — stopping here")
            return False
        log(f"quota: waiting for the {over} window to reset at {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime(until))}")
        time.sleep(max(60, until - time.time()))


def run_cmd(args, log, cwd=HERE):
    r = subprocess.run([PY] + args, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        log(f"command failed ({r.returncode}): {' '.join(args)} — {r.stderr.strip()[-400:]}")
    return r


def unfinished(out, only=None):
    plan = json.loads((out / "plan.json").read_text(encoding="utf-8"))
    cells = plan["episodes"]
    if only:
        k, v = only.split("=", 1)
        cells = [c for c in cells if str(c.get(k)) == v]
    todo = [c["episode_id"] for c in cells if not (out / c["episode_id"] / "result.json").exists()]
    interrupted = [e for e in todo if (out / e / "started.json").exists()]
    return todo, interrupted


def run_streams(out, backend, streams, log, policy, only=None, rounds=3, timeout=420):
    """Four streams, wait, then continuation rounds while runnable episodes remain (the runner skips finished and
    interrupted episodes; deferred generations wait for their predecessors, which the caller handles via waves)."""
    for rnd in range(1, rounds + 1):
        todo, interrupted = unfinished(out, only)
        runnable = [e for e in todo if e not in interrupted]
        if not runnable:
            break
        log(f"{out.name}{' ' + only if only else ''}: round {rnd}, {len(runnable)} episode(s) to run, {len(interrupted)} interrupted (never rerun)")
        procs = []
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        for k in range(1, streams + 1):
            args = [PY, "run_r3.py", "run", "--out", str(out), "--backend", backend, "--limit", "999",
                    "--stream", f"{k}/{streams}", "--timeout", str(timeout)]
            if only:
                args += ["--only", only]
            if backend == "rehearsal":
                args += ["--policy", policy]
            lf = open(LOG_DIR / f"{out.name}-{(only or 'all').replace('=', '')}-r{rnd}-s{k}.log", "a", encoding="utf-8")
            procs.append((subprocess.Popen(args, cwd=HERE, stdout=lf, stderr=subprocess.STDOUT), lf))
        for p, lf in procs:
            p.wait()
            lf.close()
        todo, interrupted = unfinished(out, only)
        if not [e for e in todo if e not in interrupted]:
            break
    todo, interrupted = unfinished(out, only)
    log(f"{out.name}{' ' + only if only else ''}: done — {len(todo)} unfinished ({len(interrupted)} interrupted)")
    return todo, interrupted


def analyze(out, design, log):
    args = ["analyze_r3.py", str(out)] + (["--design", design] if design else [])
    r = run_cmd(args, log)
    if r.returncode == 0:
        log(f"{out.name}: analysed → {out / 'results.md'}")
    fig = run_cmd([str(HERE.parent / "analysis" / "figures.py"), str(out)], log)
    if fig.returncode == 0 and fig.stdout.strip():
        made = json.loads(fig.stdout.strip().splitlines()[-1]).get("figures", [])
        if made:
            log(f"{out.name}: figures {', '.join(Path(m).name for m in made)}")


def prepare(b, out, log):
    if (out / "plan.json").exists():
        log(f"{b['name']}: {out} already prepared — resuming, no episode is rerun")
        return True
    r = run_cmd(b["prepare"] + ["--out", str(out)], log)
    if r.returncode != 0:
        return False
    tail = [l.strip() for l in r.stdout.strip().splitlines() if "plan_hash" in l or "calls" in l or "episodes" in l]
    log(f"{b['name']}: prepared {out} ({'; '.join(tail)[:160]})")
    return True


# ---------------------------------------------------------------------------- batch kinds

def run_batch(b, a, log):
    out = HERE / b["out"]
    if not wait_for_quota(a.runs, log, a.backend, a.max_wait_h):
        return False
    if not prepare(b, out, log):
        return False
    if b["kind"] == "e4":
        for rnd in range(1, 4):
            procs = []
            for k in range(1, a.streams + 1):
                LOG_DIR.mkdir(parents=True, exist_ok=True)
                lf = open(LOG_DIR / f"e4-r{rnd}-s{k}.log", "a", encoding="utf-8")
                procs.append((subprocess.Popen([PY, "sweep_e4.py", "run", "--out", str(out), "--backend", a.backend, "--stream", f"{k}/{a.streams}"],
                                               cwd=HERE, stdout=lf, stderr=subprocess.STDOUT), lf))
            for p, lf in procs:
                p.wait()
                lf.close()
            rows = sum(1 for _ in open(out / "sweep.jsonl", encoding="utf-8")) if (out / "sweep.jsonl").exists() else 0
            plan = json.loads((out / "plan.json").read_text(encoding="utf-8"))
            planned = len(plan.get("calls", plan.get("episodes", [])))
            log(f"E4: round {rnd}, {rows} of {planned} calls recorded")
            if rows >= planned:
                break
        r = run_cmd(["report.py", "e4", str(out / "sweep.jsonl"), "--out", str(out / "reports")], log)
        if r.returncode == 0:
            log(f"E4: report → {out / 'reports'}")
        return True
    if b["kind"] == "stream":
        run_streams(out, a.backend, a.streams, log, a.rehearsal_policy)
        analyze(out, b["design"], log)
        return True
    if b["kind"] in ("waves", "d4"):
        gens = range(1, b["generations"] + 1)
        for g in gens:
            run_streams(out, a.backend, a.streams, log, a.rehearsal_policy, only=f"generation={g}")
            if b["kind"] == "d4" and g == 1:
                analyze(out, None, log)
                r = subprocess.run([PY, "d4_gate.py", str(out)], cwd=HERE, capture_output=True, text=True)
                verdict = json.loads(r.stdout) if r.stdout.strip().startswith("{") else {"decision": "ERROR", "reasons": [r.stderr[-300:]]}
                log(f"D4 gate after wave 1: **{verdict.get('decision')}** — " + "; ".join(verdict.get("reasons", [])) +
                    f" (S1 g1 READ: {verdict.get('s1_g1_read')}; seed read before access: {verdict.get('seed_read_before_access')}; invalid: {verdict.get('s1_g1_invalid')})")
                (out / "d4_gate_verdict.json").write_text(json.dumps(verdict, indent=2) + "\n", encoding="utf-8")
                if verdict.get("decision") == "WAIT" and a.backend == "claude":
                    log("D4 gate: wave 1 has unfinished generation-1 episodes after the continuation rounds — treated as an infrastructure deviation; "
                        "decision on the valid ones")
                    r = subprocess.run([PY, "d4_gate.py", str(out), "--allow-unfinished"], cwd=HERE, capture_output=True, text=True)
                    verdict = json.loads(r.stdout) if r.stdout.strip().startswith("{") else verdict
                    log(f"D4 gate (valid episodes only): **{verdict.get('decision')}** — " + "; ".join(verdict.get("reasons", [])))
                    (out / "d4_gate_verdict.json").write_text(json.dumps(verdict, indent=2) + "\n", encoding="utf-8")
                if verdict.get("decision") != "CONTINUE":
                    log("D4: stopping after generation 1 as the rule prescribes — reported as a generation-1 finding, "
                        "'continuation not carried out for the pre-declared budget reason', never as 'no propagation'")
                    break
        analyze(out, None, log)
        return True
    log(f"unknown batch kind {b['kind']}")
    return False


def analysis_only(a, log):
    for plan in sorted(glob.glob(os.path.join(HERE, a.runs, "*", "plan.json"))):
        out = Path(plan).parent
        p = json.loads(Path(plan).read_text(encoding="utf-8"))
        design = p.get("design") if p.get("experiment") == "E1" else None
        if design in ("a", "b", "tier", "tier-full"):
            analyze(out, design, log)
        elif p.get("experiment") in ("E2", "E3"):
            analyze(out, None, log)
    for sweep in sorted(glob.glob(os.path.join(HERE, a.runs, "*", "sweep.jsonl"))):
        out = Path(sweep).parent
        run_cmd(["report.py", "e4", sweep, "--out", str(out / "reports")], log)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["friday", "saturday", "d4", "all", "analysis", "check"], required=True)
    ap.add_argument("--backend", choices=["claude", "rehearsal"], default="claude")
    ap.add_argument("--rehearsal-policy", default="chain_propagate")
    ap.add_argument("--streams", type=int, default=4)
    ap.add_argument("--runs", default="runs")
    ap.add_argument("--max-wait-h", type=float, default=6.0, help="how long to wait for a quota window to reset")
    ap.add_argument("--log", default=None)
    a = ap.parse_args()
    global LOG_DIR
    LOG_DIR = HERE / a.runs / "_logs"
    log = Log(a.log or (HERE / a.runs / "AUTORUN_LOG.md"))
    log(f"### autorun --phase {a.phase} --backend {a.backend} (streams {a.streams}); source hash {source_hash()[:12]}…")
    if a.phase == "analysis":
        analysis_only(a, log)
        log("analysis phase done")
        return
    if a.phase == "check":
        ok = preflight(a, log)
        log("check: READY — start with --phase friday" if ok else "check: NOT READY — see above")
        sys.exit(0 if ok else 1)
    for b in batches(a.phase, a.runs):
        log(f"## {b['name']}")
        ok = run_batch(b, a, log)
        if not ok:
            log(f"{b['name']}: stopped — see above; the remaining batches are not started")
            sys.exit(1)
    log(f"phase {a.phase} done")


def preflight(a, log):
    """Doctor, freeze verification against the newest manifest, tests, quota reading, existing run directories."""
    ok = True
    r = run_cmd(["run_r3.py", "doctor"], log)
    if r.returncode == 0:
        d = json.loads(r.stdout)
        log(f"doctor: claude_installed={d.get('claude_installed')} version={d.get('claude_version')} project_context_env_present={d.get('project_context_env_present')} "
            f"(scrubbed per episode) mcp_task={len(d.get('mcp_task_tools', []))} tools, mcp_concern={d.get('mcp_concern_tools')}")
        ok &= bool(d.get("claude_installed")) or a.backend == "rehearsal"
    else:
        ok = False
    manifests = sorted(HERE.glob("MANIFEST.sha256.v*.json"), key=lambda p: int(p.name.split(".v")[1].split(".")[0]))
    if manifests:
        import hashlib
        m = json.loads(manifests[-1].read_text(encoding="utf-8"))
        bad = [f for f, h in m["instrument"].items() if hashlib.sha256((HERE / f).read_bytes()).hexdigest() != h]
        bad += [f for f, h in m["amendment"].items() if hashlib.sha256((HERE / f).read_bytes()).hexdigest() != h]
        log(f"freeze {manifests[-1].name} ({m.get('frozen_at_utc')}): " + ("all hashes match" if not bad else f"MISMATCH in {bad}"))
        ok &= not bad
    r = subprocess.run([PY, "-m", "unittest", "discover", "-s", "tests"], cwd=HERE, capture_output=True, text=True)
    last = (r.stderr.strip().splitlines() or ["?"])[-1]
    log(f"tests: {last}")
    ok &= r.returncode == 0
    q = quota_reading(a.runs)
    log(f"quota: five_hour {q['five_hour']:.0%}, seven_day {q['seven_day']:.0%}" if q else "quota: no reading yet (first live episode produces one)")
    existing = sorted(p.parent.name for p in (HERE / a.runs).glob("*/plan.json")) if (HERE / a.runs).exists() else []
    log(f"run directories present: {existing}")
    return bool(ok)


def source_hash():
    sys.path.insert(0, str(HERE))
    import run_r3
    return run_r3.source_hash()


if __name__ == "__main__":
    main()
