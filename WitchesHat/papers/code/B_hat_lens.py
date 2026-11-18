"""B. Does the hat potential focus the dynamic-action bundle?  numpy + scipy.

Hat family (x = r/r0):  V(x) = V0 (2 x^n - n x^2)/(n - 2)   minimum -V0 at the brim x = 1, V(0) = 0 the hilltop.
n = 4 is the quartic Mexican hat of the Standard Model Higgs, V0 (x^4 - 2 x^2).
Bundle: unit-mass rays leave the brim ring (x = 1) inward at angle psi to the radial, total energy E.
Resolution = closest approach r_min of a ray (smaller = tighter focus).  Dimensionless: r_min / r0.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp

def V(x, n):  return (2*x**n - n*x**2)/(n - 2)          # in units of V0, x in units of r0

def rmin(psi, E, n):
    """closest approach in units of r0.  speed^2 at the brim = 2(E+1) (units V0, r0=1, m=1)."""
    L2 = 2*(E + 1)*np.sin(psi)**2                          # L^2 = (r v sin psi)^2
    f = lambda x: 2*(E - V(x, n)) - L2/x**2               # = r-dot^2
    xs = np.logspace(-9, 0, 4000); fv = f(xs)
    hit = np.where(fv[:-1] < 0)[0]
    # the turning point nearest the brim, scanning inward
    idx = np.where((fv[1:] > 0) & (fv[:-1] < 0))[0]
    if len(idx) == 0: return 0.0
    i = idx[-1]
    return brentq(f, xs[i], xs[i+1], xtol=1e-14)

# 1. the closed form at the separatrix E = 0:  r_min/r0 = sqrt(sin psi) ((n-2)/n)^(1/4)
print("E=0: numerical r_min/r0 vs the small-psi closed form (valid while r_min << r0)")
for psi in (1e-4, 1e-2, 0.3):
    for n in (4, 10):
        a = rmin(psi, 0.0, n); b = np.sqrt(np.sin(psi))*((n - 2)/n)**0.25
        print("  psi=%-6g n=%2d  %.6f  %.6f  (rel diff %.1e)" % (psi, n, a, b, abs(a - b)/b))

# 2. depth and size drop out: scale V0 and r0 and integrate an actual ray in Cartesian coordinates
def ray(V0, r0, n, psi, E=0.0, T=200.0):
    def F(t, s):
        x, y, vx, vy = s; r = np.hypot(x, y)/r0
        dV = V0*(2*n*r**(n-1) - 2*n*r)/(n - 2)/r0          # dV/dr
        return [vx, vy, -dV*x/np.hypot(x, y), -dV*y/np.hypot(x, y)]
    v = np.sqrt(2*V0*(E/1.0 + 1))                          # E in units of V0
    s0 = [r0, 0, -v*np.cos(psi), v*np.sin(psi)]
    sol = solve_ivp(F, [0, T], s0, rtol=1e-11, atol=1e-13, dense_output=True)
    t = np.linspace(0, T, 200001); p = sol.sol(t)
    return np.hypot(p[0], p[1]).min()/r0
print("integrated ray, n=4, psi=0.3, E=0, closest approach / r0 for different (V0, r0):")
for V0, r0 in ((1, 1), (10, 1), (1, 7), (0.2, 3)):
    print("  V0=%-4g r0=%-3g  %.5f" % (V0, r0, ray(V0, r0, 4, 0.3, T=60/np.sqrt(V0)*r0)))

# 3. the knob is the shape: resolution of a bundle psi in [0.02, 0.4] as the exponent n varies
print("bundle median r_min/r0 at E=0 against exponent n (psi 0.02..0.4):")
ps = np.linspace(0.02, 0.4, 40)
for n in (2.2, 3, 4, 6, 10, 20):
    r = np.array([rmin(p, 0.0, n) for p in ps]); print("  n=%5.1f  median %.4f  spread (max-min) %.4f" % (n, np.median(r), r.max() - r.min()))

# 4. energy below the hilltop: the hump reflects radial rays at r_c; resolution is limited by E
print("radial ray (psi=1e-6), n=4: reflection radius r_c/r0 against E (units V0), closed form sqrt(-E/ (n/(n-2)))")
for E in (-0.5, -0.1, -0.01, -0.001, 0.0):
    print("  E=%7.3f  r_c/r0 = %.4f  closed %.4f" % (E, rmin(1e-6, E, 4), np.sqrt(max(-E, 0)/(4/2))))
