"""Pure-Python statistics for r3: Wilson intervals, Hoeffding radius for a paired
difference of rates, exact block-swap permutation test (paired by seed), exact
two-sample permutation test over chains (unpaired), Fisher's exact test.

No dependencies. All tests are exact (full enumeration), which is feasible for the
r3 sizes: 2^16 = 65,536 swap assignments; C(16, 8) = 12,870 chain assignments.
"""
from __future__ import annotations

import math
from itertools import combinations
from typing import Sequence


# ------------------------------------------------------------------ intervals

def wilson(k: int, n: int, z: float = 1.959964) -> tuple[float, float, float]:
    """Wilson score interval; returns (point, lower, upper)."""
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (p, max(0.0, centre - half), min(1.0, centre + half))


def hoeffding_radius_paired(n_blocks: int, alpha: float = 0.05) -> float:
    """Two-sided Hoeffding radius for the mean of n_blocks paired differences in [-1, 1].

    P(|mean - E| >= t) <= 2 exp(-2 B t^2 / (b-a)^2) with (b-a) = 2  ->  t = sqrt(2 ln(2/alpha) / B).
    B = 8 gives 0.960 (the r2 value); B = 16 gives 0.679.
    """
    return math.sqrt(2.0 * math.log(2.0 / alpha) / n_blocks)


def clopper_pearson(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact two-sided (1 - alpha) Clopper–Pearson interval for a binomial proportion, pure Python.

    Bisection on the binomial CDF; no scipy. k = 0 gives lower 0, k = n gives upper 1.
    """
    if n <= 0:
        return (0.0, 1.0)

    def cdf(j, p):
        return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(j + 1))

    def solve(j, target):
        lo, hi = 0.0, 1.0
        for _ in range(80):
            mid = (lo + hi) / 2
            if cdf(j, mid) > target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    lower = 0.0 if k == 0 else solve(k - 1, 1 - alpha / 2)
    upper = 1.0 if k == n else solve(k, alpha / 2)
    return (lower, upper)


def discordance_interval(x: Sequence[float], y: Sequence[float], alpha: float = 0.05) -> dict:
    """Conservative (1 - alpha) interval for the paired risk difference mean(y) - mean(x) of 0/1 outcomes.

    Secondary interval added before the main data (DEVIATIONS D2). With B paired blocks the
    difference equals p_up - p_down, where p_up = P(y=1, x=0) and p_down = P(x=1, y=0) are the
    two discordance probabilities. Each is bounded by an exact Clopper–Pearson interval at level
    1 - alpha/2 (Bonferroni over the two), and the interval for the difference is
    [lower_up - upper_down, upper_up - lower_down], clipped to [-1, 1]. Coverage assumes
    independent identically distributed blocks from the fixture generator; it is not a claim
    about other tasks or models. Much tighter than the Hoeffding radius when discordance is
    rare (B = 16, no discordant block: ±0.24 instead of ±0.68); the Hoeffding interval remains
    the pre-registered primary interval. Method adapted from the Codex working package of
    7 September 2026 (uncertainty.py).
    """
    assert len(x) == len(y)
    n = len(x)
    up = sum(1 for xi, yi in zip(x, y) if yi > 0.5 and xi < 0.5)
    down = sum(1 for xi, yi in zip(x, y) if xi > 0.5 and yi < 0.5)
    if n == 0:
        return {"up": 0, "down": 0, "n_blocks": 0, "lower": float("nan"), "upper": float("nan")}
    lo_up, hi_up = clopper_pearson(up, n, alpha / 2)
    lo_down, hi_down = clopper_pearson(down, n, alpha / 2)
    return {"up": up, "down": down, "n_blocks": n,
            "lower": max(-1.0, lo_up - hi_down), "upper": min(1.0, hi_up - lo_down)}


# ----------------------------------------------------- exact block-swap test (paired)

def block_swap_test(x: Sequence[float], y: Sequence[float]) -> dict:
    """Exact permutation test for paired blocks.

    x[b], y[b] are the outcomes (0/1 or any real) of block b in cell X and cell Y.
    Under H0 the labels within a block are exchangeable, so each of the 2^B swap
    assignments is equally likely. Statistic: mean(y - x). Two-sided p-value =
    share of assignments with |stat| >= |observed| (observed assignment included).
    """
    assert len(x) == len(y)
    d = [yi - xi for xi, yi in zip(x, y)]
    B = len(d)
    if B == 0:
        return {"stat": float("nan"), "p": float("nan"), "n_blocks": 0, "n_assignments": 0}
    obs = sum(d) / B
    # enumerate all sign flips; each flip negates d[b]
    count = 0
    total = 1 << B
    abs_obs = abs(obs) - 1e-12
    for mask in range(total):
        s = 0.0
        for b in range(B):
            s += -d[b] if (mask >> b) & 1 else d[b]
        if abs(s / B) >= abs_obs:
            count += 1
    return {"stat": obs, "p": count / total, "n_blocks": B, "n_assignments": total}


# --------------------------------------------- exact two-sample permutation (unpaired)

def two_sample_permutation_test(a: Sequence[float], b: Sequence[float]) -> dict:
    """Exact permutation test for two independent groups (e.g. 8 vs 8 chains).

    Statistic: mean(b) - mean(a). Enumerates all C(n_a + n_b, n_a) relabelings.
    """
    pooled = list(a) + list(b)
    n_a, n = len(a), len(a) + len(b)
    obs = (sum(b) / len(b)) - (sum(a) / len(a))
    total_sum = sum(pooled)
    count = 0
    n_assign = 0
    abs_obs = abs(obs) - 1e-12
    for idx in combinations(range(n), n_a):
        sa = sum(pooled[i] for i in idx)
        sb = total_sum - sa
        stat = sb / (n - n_a) - sa / n_a
        n_assign += 1
        if abs(stat) >= abs_obs:
            count += 1
    return {"stat": obs, "p": count / n_assign, "n_assignments": n_assign}


# -------------------------------------------------------------- Fisher exact

def fisher_exact_2x2(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact p for table [[a, b], [c, d]] (sum of probabilities <= observed)."""
    def hyper(a_, r1, r2, c1, n):
        return (math.comb(r1, a_) * math.comb(r2, c1 - a_)) / math.comb(n, c1)
    r1, r2, c1 = a + b, c + d, a + c
    n = r1 + r2
    p_obs = hyper(a, r1, r2, c1, n)
    p = 0.0
    for a_ in range(max(0, c1 - r2), min(r1, c1) + 1):
        pa = hyper(a_, r1, r2, c1, n)
        if pa <= p_obs + 1e-12:
            p += pa
    return min(1.0, p)


# ----------------------------------------------------------- tanh law fit (E4)

def tanh_law(m: float, beta: float, h: float) -> float:
    return 0.5 * (1.0 + math.tanh(beta * (m + h)))


def fit_tanh_law(points: Sequence[tuple[float, int, int]], beta_grid=None, h_grid=None) -> dict:
    """Maximum-likelihood fit of P(A|m) = ½[1 + tanh(β(m + h))].

    points: iterable of (m, k_A, n_valid). Grid search then local refinement; pure Python.
    Returns beta, h, loglik, and the grid used. Bootstrap is done by the caller.
    """
    import itertools
    if beta_grid is None:
        beta_grid = [i / 20 for i in range(0, 161)]        # 0 … 8
    if h_grid is None:
        h_grid = [i / 50 for i in range(-150, 151)]        # −3 … 3

    def ll(beta, h):
        s = 0.0
        for m, k, n in points:
            p = min(max(tanh_law(m, beta, h), 1e-9), 1 - 1e-9)
            s += k * math.log(p) + (n - k) * math.log(1 - p)
        return s

    best = (-float("inf"), 0.0, 0.0)
    for beta, h in itertools.product(beta_grid, h_grid):
        v = ll(beta, h)
        if v > best[0]:
            best = (v, beta, h)
    # local refinement
    _, beta, h = best
    step_b, step_h = 0.05, 0.02
    for _ in range(40):
        improved = False
        for db, dh in ((step_b, 0), (-step_b, 0), (0, step_h), (0, -step_h)):
            nb, nh = max(0.0, beta + db), h + dh
            v = ll(nb, nh)
            if v > best[0] + 1e-12:
                best = (v, nb, nh)
                beta, h = nb, nh
                improved = True
        if not improved:
            step_b /= 2
            step_h /= 2
    return {"beta": best[1], "h": best[2], "loglik": best[0]}


def bootstrap_tanh(points: Sequence[tuple[float, int, int]], reps: int = 1000, seed: int = 0) -> dict:
    """Percentile bootstrap over calls within each m (binomial resampling)."""
    import random
    rng = random.Random(seed)
    betas, hs = [], []
    for _ in range(reps):
        resampled = []
        for m, k, n in points:
            if n == 0:
                resampled.append((m, 0, 0))
                continue
            p = k / n
            kk = sum(1 for _ in range(n) if rng.random() < p)
            resampled.append((m, kk, n))
        f = fit_tanh_law(resampled, beta_grid=[i / 10 for i in range(0, 81)], h_grid=[i / 25 for i in range(-75, 76)])
        betas.append(f["beta"])
        hs.append(f["h"])
    betas.sort()
    hs.sort()

    def q(v, a):
        return v[max(0, min(len(v) - 1, int(a * len(v))))]

    return {"beta_ci": (q(betas, 0.025), q(betas, 0.975)), "h_ci": (q(hs, 0.025), q(hs, 0.975)), "reps": reps}
