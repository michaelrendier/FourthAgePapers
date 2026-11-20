"""weierstrass_gr.py: EXPLORATORY (post-hoc: chosen after reading h_rb_hat's Blue term; not in 05_registered_facets.md).
(1) The Schwarzschild orbit equation u'' + u = M/L^2 + 3 M u^2 IS the Weierstrass equation P'' = 6 P^2 - g2/2 with u = (2/M) P + 1/(6M) and g2 = 1/12 - M^2/L^2.
(2) The first integral fixes g3; checked along a numerically integrated orbit.
(3) How good is the module's 4-term Laurent  blue_energy_weierstrass  against the true function?
   ValaQuenta/.venv/bin/python weierstrass_gr.py"""
import sys, os, math
sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace"))
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
from ValaQuenta.modules.h_rb_hat import maths as H
M, L, P, g2, g3, u = sp.symbols("M L P g2 g3 u", positive=True)
# (1) symbolic
uP = 2 * P / M + 1 / (6 * M)
resid = sp.simplify(3 * M * uP ** 2 - uP + M / L ** 2 - (2 / M) * (6 * P ** 2 - g2 / 2))
sol_g2 = sp.solve(resid, g2)[0]; print("orbit equation = Weierstrass equation iff  g2 =", sp.simplify(sol_g2), "  (check 1/12 - M^2/L^2:", sp.simplify(sol_g2 - (sp.Rational(1, 12) - M ** 2 / L ** 2)) == 0, ")")
# (2) first integral -> g3
C = sp.symbols("C")
fi = sp.expand((M ** 2 / 4) * (2 * M * uP ** 3 - uP ** 2 + 2 * M * uP / L ** 2 + C))      # (P')^2 as a polynomial in P
c3, c2, c1, c0 = [sp.simplify(fi.coeff(P, k)) for k in (3, 2, 1, 0)]
print("P'^2 =", sp.collect(fi, P)); print("coefficients  P^3:", c3, "  P^2:", c2, "  P^1:", sp.simplify(c1 - (-sol_g2.subs({}))), " (should equal -g2:", sp.simplify(c1 + sol_g2) == 0, ")")
g3_expr = sp.simplify(-c0); print("g3 =", g3_expr)
Mv, Lv, p_, e_ = 1.0, math.sqrt(100.0), 100.0, 0.3          # L^2 = M p
u0 = (1 + e_) / p_; Cv = -(2 * Mv * u0 ** 3 - u0 ** 2 + 2 * Mv * u0 / Lv ** 2)
f = lambda phi, y: [y[1], Mv / Lv ** 2 - y[0] + 3 * Mv * y[0] ** 2]
s = solve_ivp(f, [0, 6], [u0, 0.0], rtol=1e-12, atol=1e-14, dense_output=True)
g2v = float(sol_g2.subs({M: Mv, L: Lv})); g3v = float(g3_expr.subs({M: Mv, L: Lv, C: Cv}))
worst = 0.0
for phi in np.linspace(0.3, 5.5, 8):
    uu, up = s.sol(phi); Pv = (Mv / 2) * (uu - 1 / (6 * Mv)); Pp = (Mv / 2) * up
    worst = max(worst, abs(Pp ** 2 - (4 * Pv ** 3 - g2v * Pv - g3v)))
print("numerical Schwarzschild orbit (p=100M, e=0.3): g2 = %.9f, g3 = %.3e ; max |P'^2 - (4P^3 - g2 P - g3)| along the orbit = %.2e" % (g2v, g3v, worst))
print("light (no M/L^2 term): g2 = 1/12 =", 1 / 12)
# (3) the module's truncated Laurent against the true wp (g2=1, g3=0), built by the ODE wp'' = 6 wp^2 - g2/2 from a Laurent start at x0
G2, G3 = 1.0, 0.0
laur = lambda x: 1 / x ** 2 + G2 * x ** 2 / 20 + G3 * x ** 4 / 28 + G2 ** 2 * x ** 6 / 1200
dlaur = lambda x, h=1e-6: (laur(x + h) - laur(x - h)) / (2 * h)
x0 = 0.12; sol = solve_ivp(lambda x, y: [y[1], 6 * y[0] ** 2 - G2 / 2], [x0, 1.0], [laur(x0), dlaur(x0)], rtol=1e-12, atol=1e-12, dense_output=True)
for x in (0.2, 0.4, 0.6, 0.8):
    true = sol.sol(x)[0]; mod = H.blue_energy_weierstrass(x, G2, G3); print("x=%.1f  true wp %.8f  module %.8f  rel error %.2e" % (x, true, mod, abs(mod - true) / true))
