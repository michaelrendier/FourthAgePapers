"""factorial_rings.py (registered in 16): ValaQuenta/.venv/bin/python factorial_rings.py"""
import sys, os, io, math, types, importlib.util, contextlib, random
from fractions import Fraction
import numpy as np
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import catalog as C
ARCH = C.ARCH + "/Maths"
spec = importlib.util.spec_from_file_location("A_Fact", os.path.join(ARCH, "Factorial.py")); FM = importlib.util.module_from_spec(spec); spec.loader.exec_module(FM)
F = FM.Factorial()
def V(d): return math.pi ** (d / 2) / math.gamma(d / 2 + 1)
def S(d): return d * V(d)       # surface of the unit sphere S^{d-1}
out = []
def rep(q, ok, msg): out.append(f"{q}: {'PASS' if ok else 'FAIL'}  {msg}")
fact = math.factorial
# Q1
n = 245
ring = lambda k: (k - 1) * fact(k - 1)             # ring area / pi
tot = sum(ring(k) for k in range(1, n + 1))
rep("Q1", tot == fact(n) - 1 and Fraction(ring(n), fact(n)) == Fraction(n - 1, n),
    f"sum of ring areas / pi = n! - 1 (exact); outer ring / n! = 244/245 = {244/245:.6f}; ring widths grow: w_245/w_244 = {math.sqrt(244) * (math.sqrt(245) - 1) / (math.sqrt(244) - 1):.4f} (sqrt 245 = {math.sqrt(245):.4f})")
# Q2
tR = fact(n) ** 2
rep("Q2", Fraction(fact(n) ** 2 - fact(n - 1) ** 2, fact(n) ** 2) == Fraction(n * n - 1, n * n), f"outer ring fraction = {n*n-1}/{n*n} exactly")
# Q3
err = 0.0
for m in range(1, 41):
    a = (math.pi ** m / F.factorial(m)) / (math.pi ** (m - 1) / F.factorial(m - 1)) if m > 1 else math.pi / F.factorial(1)
    err = max(err, abs(a - math.pi / m) / (math.pi / m))
ssum = sum(math.pi ** m / math.factorial(m) for m in range(0, 60))
gt1 = [m for m in range(1, 12) if math.pi / m > 1]
dims = {d: V(d) for d in range(1, 30)}; dmax = max(dims, key=dims.get)
rep("Q3", err < 1e-12 and abs(ssum - math.exp(math.pi)) < 1e-9 and gt1 == [1, 2, 3] and dmax == 5 and abs(V(5) - 8 * math.pi ** 2 / 15) < 1e-12,
    f"max rel err of ratio {err:.2e}; sum V(2m) = {ssum:.12f} vs e^pi = {math.exp(math.pi):.12f}; ratio>1 for m={gt1}; max dimension = {dmax} (V={V(dmax):.4f}); V(6)={V(6):.4f}")
# Q4
rng = np.random.default_rng(0); mc = {}
for d in range(1, 9):
    x = rng.uniform(-1, 1, (500000, d)); mc[d] = (np.sum(x * x, 1) <= 1).mean() * 2 ** d
mcok = all(abs(mc[d] - V(d)) / V(d) < 0.01 for d in mc)
shell = max(abs(S(d) - d * V(d)) for d in range(1, 17))
# independent shell check: S(d) = 2 pi^{d/2} / Gamma(d/2)
shell2 = max(abs(2 * math.pi ** (d / 2) / math.gamma(d / 2) - d * V(d)) / (d * V(d)) for d in range(1, 17))
rep("Q4", mcok and shell2 < 1e-12, "Monte Carlo rel err " + ", ".join(f"d{d}:{abs(mc[d]-V(d))/V(d):.4f}" for d in mc) + f"; shell identity rel err {shell2:.1e}")
# Q5
nn = 245
lg = math.lgamma(nn + 1); st = 0.5 * math.log(2 * math.pi * nn) + nn * math.log(nn) - nn
rep("Q5", abs((lg - st) - (1 / (12 * nn) - 1 / (360 * nn ** 3))) < 1e-12, f"ln n! - Stirling = {lg-st:.12e}; 1/(12n) - 1/(360n^3) = {1/(12*nn)-1/(360*nn**3):.12e}")
# Q6
rep("Q6", all(F.factorial(k) == fact(k) for k in range(1, 21)), "Archimedes Factorial.factorial == math.factorial for 1..20; used in Q3 ratio test")
# Q7
cd = [2, 4, 8, 16, 32]; vv = [V(d) for d in cd]
rep("Q7", all(vv[i] > vv[i + 1] for i in range(1, 4)) and abs(V(16) - math.pi ** 8 / fact(8)) < 1e-12,
    "V at d=2,4,8,16,32: " + ", ".join(f"{v:.4g}" for v in vv))
# Q8
rep("Q8", all(math.pi / m > 0 for m in range(1, 1000)), "pi/k > 0 for all k: no SIGN enters the ring factors (trivial)")
print("\n".join(out))
open(os.path.join(here, "results_factorial_rings_2026-11-20.txt"), "w").write("\n".join(out) + "\n")
