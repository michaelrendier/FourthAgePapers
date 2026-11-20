"""facet_tests.py: EquationSpace test 4 (see 05_registered_facets.md).  ValaQuenta/.venv/bin/python facet_tests.py"""
import sys, os, math, inspect
sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace"))
import numpy as np
from scipy.integrate import solve_ivp
from ValaQuenta.modules.h_rb_hat import maths as H
from ValaQuenta.modules.relativity import minkowski as Mk

PHI = (1 + 5 ** .5) / 2
print("== F1 audit: what does each facet function compute?")
facets = [n for n in dir(H) if n.startswith("facet_")]
for n in facets:
    r = getattr(H, n)()
    nums = {k: v for k, v in r.items() if isinstance(v, (int, float)) and not isinstance(v, bool)}
    strs = [k for k, v in r.items() if isinstance(v, str)]
    print("%-26s numbers %-52s strings %d" % (n, nums, len(strs)))
print()
print("== F2 R = xp as a dilation generator, flow time ln p")
for p in (2, 3, 5, 7):
    s = solve_ivp(lambda t, x: x, [0, math.log(p)], [1.0], rtol=1e-13, atol=1e-15)       # flow of x d/dx
    scale = s.y[0, -1]; beta = (p * p - 1) / (p * p + 1); lc = Mk.lightcone_dilation_check(beta)
    print("p=%d flow scale %.12f  |scale-p| %.1e | boost Doppler factor %.12f  lightcone residual %.1e  |k-p| %.1e" % (p, scale, abs(scale - p), lc["k"], lc["residual"], abs(lc["k"] - p)))
print()
print("== F3 B = p^2/2 + V(x) with the module's Weierstrass term: Hamilton's equations")
V = lambda x: H.blue_energy_weierstrass(x, 1.0, 0.0)
dV = lambda x, h=1e-6: (V(x + h) - V(x - h)) / (2 * h)
f = lambda t, y: [y[1], -dV(y[0])]
s = solve_ivp(f, [0, 1.0], [0.7, 0.0], rtol=1e-11, atol=1e-13, dense_output=True)
ts = np.linspace(0.2, 0.8, 5); h = 1e-3
for t in ts[1:4]:
    xpp = (s.sol(t + h)[0] - 2 * s.sol(t)[0] + s.sol(t - h)[0]) / h ** 2
    print("t=%.2f  x''=%.6f  -V'(x)=%.6f  rel %.1e" % (t, xpp, -dV(s.sol(t)[0]), abs(xpp + dV(s.sol(t)[0])) / abs(dV(s.sol(t)[0]))))
x0 = 0.3; print("V(x) ~ x^-2 near the pole (double pole):", V(0.01) * 0.01 ** 2, V(0.001) * 0.001 ** 2, "  [a 1/r potential would give V*x -> const, V*x^2 -> 0]")
print("V*x at 0.01, 0.001:", V(0.01) * 0.01, V(0.001) * 0.001)
print()
print("== F4 phi against the facet couplings")
import mpmath as mp
targets = {"phi": PHI, "1/phi": 1 / PHI, "phi^2": PHI ** 2, "1/phi^2": PHI ** -2}
hits = 0; comps = 0
for sigma in (0.5, 1.0, 2.0):
    vals = {"P(sigma) first 20 primes": sum(p ** -sigma for p in H.PRIMES), "zeta(sigma)": float(mp.zeta(sigma)) if sigma != 1.0 else None, "Euler product 20": abs(H.euler_product(sigma, 0.0, 20))}
    for vn, v in vals.items():
        if v is None or not math.isfinite(v): continue
        for tn, t in targets.items():
            comps += 1; rel = abs(v - t) / t
            if rel < 1e-3: hits += 1; print("HIT", sigma, vn, v, tn, t, rel)
    print("sigma", sigma, {k: (round(v, 6) if v is not None else None) for k, v in vals.items()})
print("comparisons %d, hits within 0.1%%: %d" % (comps, hits))
