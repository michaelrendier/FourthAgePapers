"""
hat_sim.py: the Witch's Hat simulator, step 1 (numbers).  numpy + scipy only, runs cold.

Layers (every layer says what it is):
  ESTABLISHED  the Standard-Model Higgs potential V(h) = -mu^2/2 h^2 + lam/4 h^4 with measured m_h, v
  ESTABLISHED  Schrodinger radial states of a particle in the ring potential (finite differences)
  ESTABLISHED  Maxwell + Higgs (abelian Higgs model): Nielsen-Olesen vortex at critical coupling, flux 2 pi
  ESTABLISHED  classical paths of fixed energy = geodesics of the Jacobi metric, abbreviated action W = int sqrt(2(E-V)) ds
  AUTHOR'S     the bundle of paths from the brim to the hilltop read as the "cone of dynamic action" (L_dynamic, L_(I|O));
               the simulator computes the paths and their action; the reading stays THEORETICAL.
"""
import numpy as np
from scipy.integrate import solve_ivp, solve_bvp
from scipy.linalg import eigh_tridiagonal

# ------------------------------------------------------------------ 1. the Standard-Model hat (units GeV)
M_H, VEV = 125.25, 246.22                      # PDG 2024 Higgs mass, electroweak vev
LAM = M_H**2/(2*VEV**2)                         # quartic coupling, V = -mu^2/2 h^2 + lam/4 h^4 (h real, vev v)
MU2 = LAM*VEV**2                                # mu^2 = m_h^2/2
def V_sm(h): return -0.5*MU2*h**2 + 0.25*LAM*h**4
H_BRIM = VEV                                    # radius of the brim (minimum) in the (Re, Im) field plane
V_BRIM = V_sm(H_BRIM)                           # depth: -lam v^4/4

# ------------------------------------------------------------------ 2. hat family used for the focusing test
def V_family(x, n):                             # x = r/r0, minimum -1 at x = 1, hilltop 0, exponent n (n = 4 is the SM shape)
    return (2*x**n - n*x**2)/(n - 2)

def rmin(psi, E, n):
    """closest approach (units of the brim radius) of a ray leaving the brim at angle psi to the radial, energy E (units of depth)."""
    from scipy.optimize import brentq
    L2 = 2*(E + 1)*np.sin(psi)**2
    f = lambda x: 2*(E - V_family(x, n)) - L2/x**2
    xs = np.logspace(-9, 0, 4000); fv = f(xs)
    idx = np.where((fv[1:] > 0) & (fv[:-1] < 0))[0]
    if len(idx) == 0: return 0.0
    return brentq(f, xs[idx[-1]], xs[idx[-1]+1], xtol=1e-14)

# ------------------------------------------------------------------ 3. paths and their abbreviated action
def trace_path(psi, E=0.0, n=4, T=40.0, npts=4000):
    """Cartesian ray from the brim (1, 0) inward at angle psi; units: brim radius 1, depth 1, mass 1 (time unit r0/sqrt(V0)).
    Returns x, y, V along the path and W(s) = cumulative abbreviated action int sqrt(2(E-V)) ds."""
    def F(t, s):
        x, y, vx, vy = s; r = np.hypot(x, y)
        dV = (2*n*r**(n-1) - 2*n*r)/(n - 2)
        return [vx, vy, -dV*x/r, -dV*y/r]
    v = np.sqrt(2*(E + 1))
    ev = lambda t, s: s[0]*s[2] + s[1]*s[3]; ev.terminal = True; ev.direction = 1.0   # r.rdot turns positive: closest approach
    sol = solve_ivp(F, [0, T], [1, 0, -v*np.cos(psi), v*np.sin(psi)], rtol=1e-11, atol=1e-13, events=ev, dense_output=True)
    t = np.linspace(0, sol.t[-1], npts); p = sol.sol(t)
    x, y = p[0], p[1]; r = np.hypot(x, y)
    speed = np.hypot(p[2], p[3])
    W = np.concatenate([[0], np.cumsum(0.5*(speed[1:] + speed[:-1])*np.diff(t))])      # int p.dq = int v^2 dt for unit mass
    return x, y, V_family(r, n), W

# ------------------------------------------------------------------ 4. Schrodinger: radial m = 0 states on the hat
def schrodinger_ring(n=4, depth_over_hbar=40.0, N=3000, rmax=2.2, states=4):
    """-1/2 u'' + (V_eff) u = e u with u = sqrt(r) R, m = 0 (so V_eff = V - 1/(8 r^2)); units brim radius 1, mass 1,
    hbar^2/(m r0^2) set by depth_over_hbar = V0 m r0^2/hbar^2 (how deep the hat is in quantum units)."""
    r = np.linspace(rmax/N, rmax, N); dr = r[1] - r[0]
    k = depth_over_hbar
    Veff = k*V_family(r, n) - 1.0/(8*r**2)
    d = 1.0/dr**2 + Veff; e = -0.5/dr**2*np.ones(N - 1)
    w, vec = eigh_tridiagonal(d, e, select='i', select_range=(0, states - 1))
    R = vec/np.sqrt(r)[:, None]
    dens = (R**2)*r[:, None]                     # radial probability density |R|^2 r
    dens /= dens.sum(axis=0)*dr
    peak = r[np.argmax(dens, axis=0)]
    return r, w, dens, peak

# ------------------------------------------------------------------ 5. Maxwell + hat: Nielsen-Olesen vortex, critical coupling
def vortex(rmax=12.0):
    """Abelian Higgs, e = v = 1, lam = e^2 (critical): phi = f(r) e^{i theta}, A_theta = a(r)/r (n = 1).
    Second-order equations solved as a boundary-value problem, then checked against the Bogomolny first-order ones."""
    def rhs(r, y):
        f, fp, a, ap = y
        fpp = -fp/r + (1 - a)**2*f/r**2 + 0.5*f*(f**2 - 1)      # lam/2 (f^2-1) f with lam = 1 -> 1/2 in these units
        app = ap/r - (1 - a)*f**2
        return np.vstack([fp, fpp, ap, app])
    def bc(ya, yb): return np.array([ya[0], ya[2], yb[0] - 1, yb[2] - 1])
    r = np.linspace(1e-4, rmax, 800)
    y0 = np.vstack([np.tanh(r), 1/np.cosh(r)**2, np.tanh(r)**2, 2*np.tanh(r)/np.cosh(r)**2])
    sol = solve_bvp(rhs, bc, r, y0, tol=1e-8, max_nodes=100000)
    rr = np.linspace(1e-4, rmax, 600); f, fp, a, ap = sol.sol(rr)
    B = ap/rr                                                     # magnetic field B = a'/r
    flux = 2*np.pi*np.trapezoid(B*rr, rr)                             # should be 2 pi (quantised, n = 1)
    # Bogomolny check at this coupling: f' = (1-a) f / r
    m = rr > 0.05                                                 # the first grid point is pinned to f = 0, which breaks f/r there
    bog = max(np.abs(fp - (1 - a)*f/rr)[m].max(), np.abs(ap - rr*(1 - f**2)/2)[m].max())
    return rr, f, a, B, flux, bog, sol.status

# ------------------------------------------------------------------ 6. electroweak numbers that follow from the vev
def electroweak():
    g, gp = 0.6517, 0.3583                        # SU(2) and U(1) couplings at the Z scale (PDG)
    mW = g*VEV/2; mZ = 0.5*VEV*np.hypot(g, gp); mA = 0.0
    return mW, mZ, mA, np.degrees(np.arctan(gp/g))

if __name__ == "__main__":
    print("== Standard-Model hat (ESTABLISHED numbers)")
    print("m_h = %.2f GeV, v = %.2f GeV  ->  lambda = %.5f, mu^2 = %.1f GeV^2, brim radius %.2f GeV, depth V(brim) = %.4e GeV^4"
          % (M_H, VEV, LAM, MU2, H_BRIM, V_BRIM))
    print("curvature at the hilltop V''(0) = -mu^2 = %.1f GeV^2; at the brim V''(v) = 2 mu^2 = m_h^2 = %.1f (check %.1f)"
          % (-MU2, 2*MU2, M_H**2))
    mW, mZ, mA, thw = electroweak()
    print("from the vev: tree level with the Z-scale couplings: m_W = %.2f (PDG 80.37), m_Z = %.2f (PDG 91.19), m_photon = %.1f GeV, weak angle %.2f deg (the brim circle carries the Goldstone/gauge freedom)" % (mW, mZ, mA, thw))
    print("\n== Paths: closest approach at E = 0 (the hilltop) vs launch angle, n = 4 (SM shape)")
    for psi in (0.01, 0.05, 0.1, 0.2, 0.4):
        x, y, Vp, W = trace_path(psi, 0.0, 4, T=200.0)
        print("  psi=%.2f  r_min=%.4f  analytic sqrt(sin psi)((n-2)/n)^(1/4)=%.4f  action to closest approach W=%.4f"
              % (psi, np.hypot(x, y).min(), np.sqrt(np.sin(psi))*0.5**0.25, W[-1]))
    # radial abbreviated action brim -> hilltop for the quartic hat, in units sqrt(V0) r0 sqrt(m): int_0^1 sqrt(2(2x^2-x^4)... ) 
    xs = np.linspace(0, 1, 200001); Wr = np.trapezoid(np.sqrt(np.maximum(-2*V_family(xs, 4), 0)), xs)
    print("  radial path brim -> hilltop: W = %.6f  (exact int_0^1 sqrt(4x^2-2x^4)dx = %.6f)" % (Wr, np.trapezoid(np.sqrt(4*xs**2 - 2*xs**4), xs)))
    print("\n== Focusing against shape (median r_min of the psi bundle 0.02..0.4 at E=0)")
    ps = np.linspace(0.02, 0.4, 40)
    for nn in (2.2, 3, 4, 6, 10, 20):
        print("  n=%5.1f  median r_min/r0 = %.4f" % (nn, np.median([rmin(p, 0.0, nn) for p in ps])))
    print("\n== Schrodinger on the hat (m = 0 radial states; depth in quantum units 40, 400)")
    for k in (40.0, 400.0):
        r, w, dens, peak = schrodinger_ring(4, k)
        print("  depth %5.0f: energies %s ; radial density peaks at r = %s (brim = 1)" % (k, np.round(w - 0, 2), np.round(peak, 3)))
    print("\n== Maxwell + hat: Nielsen-Olesen vortex, critical coupling")
    rr, f, a, B, flux, bog, status = vortex()
    print("  solver status %d; magnetic flux = %.6f (2 pi = %.6f); max residual of f' = (1-a) f/r and a' = r(1-f^2)/2 (r > 0.05) = %.2e; f(core) -> 0, f(inf) -> 1 = %.5f"
          % (status, flux, 2*np.pi, bog, f[-1]))
