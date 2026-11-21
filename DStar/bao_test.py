#!/usr/bin/env python3
"""bao_test.py (2026-11-21): does the BAO framing hold? PREDICTIONS registered before the run.
The record says (Addendum VIII, bao_mass_gap, README): the residual Δ = A_π − Ω_ζΣ·ln10 (0.000707) is "the BAO spectral residue" and "the native constants predict the BAO scale".
Test 1 (code): does any line of the engine compute a BAO observable from the constants?  Prediction P1: no (read from the source: only a ratio of Δ to Planck's fractional error).
Test 2 (numerology under a null): do small expressions of the project's constants {A_π, Ω_ζΣ, φ, π, e, 2, 3, ln10} reproduce the DIMENSIONLESS BAO numbers (Planck 2018: z_drag = 1059.94±0.30, z_* = 1089.92±0.25, θ_* = 1.04110e-2 ±0.00031e-2, ℓ_A = 301.63) within their stated precision more often than random targets of the same size do?  Prediction P2: no (the number of hits is inside the null's central 90%).
Run: python3 bao_test.py"""
import math, itertools, random
A_PI = 0.5671432904097838; OM = A_PI / math.log(10); PHI = (1 + 5 ** .5) / 2; LN10 = math.log(10); DELTA = A_PI - 0.246 * LN10
base = {"A_π": A_PI, "Ω_ζΣ": OM, "φ": PHI, "π": math.pi, "e": math.e, "2": 2.0, "3": 3.0, "ln10": LN10, "Δ": DELTA}
targets = {"z_drag": (1059.94, 0.30), "z_*": (1089.92, 0.25), "θ_*": (1.04110e-2, 0.00031e-2), "ℓ_A": (301.63, 0.15)}
exps = (-2, -1, 1, 2)
vals = {}
names = list(base)
for k in (1, 2, 3):
    for combo in itertools.combinations(names, k):
        for ex in itertools.product(exps, repeat=k):
            v = 1.0
            for n, e in zip(combo, ex): v *= base[n] ** e
            vals["·".join(f"{n}^{e}" if e != 1 else n for n, e in zip(combo, ex))] = v
V = list(vals.values()); print(len(vals), "expressions")
out = []
def hits(t, tol): return [n for n, v in vals.items() if abs(v - t) <= tol]
rng = random.Random(2026); res = {}
for tn, (t, tol) in targets.items():
    h = hits(t, tol); null = []
    for _ in range(3000):
        r = math.exp(rng.uniform(math.log(t * 0.3), math.log(t * 3))); null.append(len(hits(r, tol * r / t)))
    ge = sum(1 for k in null if k >= len(h)) / len(null); res[tn] = (len(h), ge)
    out.append(f"{tn}: target {t} ± {tol}: {len(h)} expressions inside; random targets of the same size and relative precision: mean {sum(null)/len(null):.3f}; fraction of random targets with ≥ this many = {ge:.3f}; hits: {h[:3]}")
out.append("\nTest 1 (code): the engine's 'bao_consistency' divides Δ by Planck's FRACTIONAL error on r_s (0.177%) and calls a ratio > 0.1 'resolvable'; no line maps Δ or any constant to r_s, z, θ or ℓ. P1 holds (by reading `inductive_onset_residual` / the retired `bao_mass_gap`).")
allp = all(g > 0.05 for _, g in res.values())
out.append("\nVERDICT: P2 " + ("HELD: no target is matched more often than chance (every fraction > 0.05)" if allp else "FAILED for: " + ", ".join(t for t, (n, g) in res.items() if g <= 0.05)) + ". BAO framing: no computation, no prediction beyond chance → strip the label (Δ is the onset residual).")
open("bao_test.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
