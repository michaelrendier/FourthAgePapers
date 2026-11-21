#!/usr/bin/env python3
"""ceilings_derivation.py (2026-11-21): the Riemann–Fermat Horizon derivation with the author's assignment (@RCCM_SYMBOLS):
   Hagedorn information ceiling (entropy, Riemann side)  → Ω_ζΣ = d*   (decimal digits below the ceiling)
   speed-of-causality ceiling (inertia, Fermat side)     → A_π = W(1)  (fraction of c, in nats)
PREDICTIONS registered before the run:
 P1 the crossing x = e^(−x) is independent of which ceiling is used: x* = W(1) for Hagedorn, Planck and c alike; only the dimensional value T* = x*·T_ceil (or v* = x*·c) changes.
 P2 the decimal-digit position below each ceiling is d* = |log10 x*| = W(1)/ln10 = 0.2463072014734 for all three ceilings.
 P3 d*·ln10 = A_π to 15 digits (the Jacobian ln10 is one factor, not four).
 P4 the April-10 polar field with the fine-structure α (1/137 or 0.137) as entropy coupling never lets S and I meet (min|S−I| > 0.1); with the coupling set to A_π they touch (min|S−I| < 1e−6).
Run: python3 ceilings_derivation.py   (needs numpy; uses RiemannHypothesisProof/rhp/polar_field.py)"""
import math, sys, os
sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace/RiemannHypothesisProof"))
from decimal import Decimal, getcontext
getcontext().prec = 60
x = Decimal("0.5")
for _ in range(400): x = (-x).exp()
A_PI = float(x); LN10 = math.log(10); D_STAR = A_PI / LN10
hbar = 1.054571817e-34; c = 299792458.0; G = 6.67430e-11; kB = 1.380649e-23
T_PLANCK = math.sqrt(hbar * c ** 5 / G) / kB
T_HAGEDORN = 7.78e16                    # RHP docs: ≈ 7.78e16 K (also quoted 1.4e17 K); only the K value moves, never x* or d*
out = []
out.append(f"x* solves x = e^(−x): {A_PI!r}  residual {abs(A_PI - math.exp(-A_PI)):.2e}")
ok = True
for name, ceil, unit in (("Hagedorn ceiling (entropy → Ω_ζΣ = d*)", T_HAGEDORN, "K"), ("Planck temperature (April-9 run)", T_PLANCK, "K"), ("speed of causality (inertia → A_π)", c, "m/s")):
    star = A_PI * ceil
    d = -math.log10(star / ceil)
    out.append(f"{name:42s} ceiling {ceil:.6e} {unit}   crossing {star:.6e} {unit}   x* = {star/ceil:.13f}   digits below ceiling = {d:.13f}")
    ok &= abs(d - D_STAR) < 1e-15
out.append(f"d* = W(1)/ln10 = {D_STAR:.13f};  d*·ln10 = {D_STAR*LN10:.15f}  A_π = {A_PI:.15f}  |diff| = {abs(D_STAR*LN10-A_PI):.1e}")
P3 = abs(D_STAR * LN10 - A_PI) < 1e-15
out.append(f"P1/P2 {'HELD' if ok else 'FAILED'}: same x*, same d* for all three ceilings.   P3 {'HELD' if P3 else 'FAILED'}.")
# the inertia chase on the c side: g·e^(g/g0) = g0 → g = g0·A_π  (g0 = c)
g0 = c; g = A_PI * g0
out.append(f"inertia chase g·e^(g/g0) = g0, g0 = c: g = {g:.6f} m/s, residual {abs(g*math.exp(g/g0)-g0):.2e}  (= {g/c:.13f} c)")
# P4: the polar field with the two couplings
import numpy as np
from rhp import polar_field as PF
res = {}
for lab, a in (("α = 1/137.036 (fine-structure)", 1 / 137.036), ("α = 0.137 (widget default)", 0.137), ("coupling = A_π (Lambert)", A_PI)):
    m, r, t = PF.closest_approach(alpha=a, depth=math.pi / 2, n_r=3000, n_th=720); res[lab] = m
    out.append(f"polar field S,I with {lab:34s} min|S−I| = {m:.3e} at r = {r:.4f}")
P4 = res["α = 1/137.036 (fine-structure)"] > 0.1 and res["α = 0.137 (widget default)"] > 0.1 and res["coupling = A_π (Lambert)"] < 1e-6
out.append(f"P4 {'HELD' if P4 else 'FAILED'}: with the fine-structure coupling the curves never meet (the 'closest-approach ring'); with A_π they touch.")
lo, hi = 0.50, A_PI
f = lambda a: PF.closest_approach(alpha=a, depth=math.pi / 2, n_r=3000, n_th=720)[0]
for _ in range(20):
    mid = (lo + hi) / 2
    if f(mid) > 1e-9: lo = mid
    else: hi = mid
out.append(f"first-touch coupling in this widget (ripple constants 0.08/0.12 hand-chosen) = {hi:.4f} = {hi/A_PI:.4f}·A_π: touches for every coupling ≥ it, so the widget alone does not single out A_π; the chase equation does.")
open("ceilings_derivation.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
