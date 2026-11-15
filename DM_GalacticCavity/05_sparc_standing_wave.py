#!/usr/bin/env python3
"""Does SPARC support a halo that is a standing wave?  Only established physics: the time-averaged energy density of a standing wave.

Written 2026-11-15. numpy + scipy; run cold:  python3 -I 05_sparc_standing_wave.py   (from this directory)

The assumptions tested (the author's): the halo is a standing wave of wavelength comparable to the galactic radius, travelling at c,
so that it looks static over a human lifetime; its time-averaged energy gravitates (Isaacson 1968: the averaged stress-energy of a gravitational
wave is a source of gravity; Wheeler 1955 'geons'). Nothing from the framework (no d*, no Omega) enters.

PART A  the model. A standing wave psi = f(r) Y_lm cos(wt), w = ck, f = j_l(kr): the energy density averaged over time and angle is
      u_l(r) = (A^2 c^2 k^2 / 4) [ j_l(x)^2 + j_l'(x)^2 + l(l+1) j_l(x)^2 / x^2 ],  x = kr.
   This is a SCALAR-wave template (the tensor harmonics of a real gravitational wave change the angular factor, not the 1/r^2 envelope).
   Properties derived here and checked numerically below: for kr >> 1 u falls as 1/r^2 for every l (radiation energy conservation), so
   M(<r) ~ r and the circular speed tends to a constant: a flat rotation curve; for l = 0 and 1 the centre has a finite density (a core of
   size ~ 1/k); for l = 2 u -> 0 at the centre (a central hole, 'cavity'). Birkhoff's theorem forbids a spherically symmetric
   gravitational wave, so for gravity the lowest multipole is l = 2; l = 0 is the scalar-wave case only.
   Fit: parameters (log10 rho_s, k), 2 per galaxy, same as NFW / Burkert / pseudo-isothermal in 04_sparc_retest.py; baryons fixed (Y = 0.5, 0.7).
PART B  the wavelength of the best fit against galaxy size and the wave period lambda/c.
PART C  the residual test: for the best smooth cored model (baryons + Burkert) the residual V_obs - V_model is searched for a periodic radial
   pattern of wavelength q * R_ref (R_ref = HI radius), stacked over galaxies; the null distribution is made by permuting each galaxy's residuals.
PART D  orders of magnitude for a wave of wavelength lambda at speed c: period, phase advance in 76 years, and the strain h whose averaged
   energy density equals a halo's (u = c^2 w^2 h^2 / (32 pi G), Isaacson), against the galaxy's own potential depth (V/c)^2.
"""
import glob, os
import numpy as np
from scipy.optimize import least_squares
from scipy.special import spherical_jn

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'data', 'SPARC')
G = 4.30091e-6; C_KMS = 299792.458; KPC_M = 3.0857e19; LY_PER_KPC = 3261.56; YR_S = 3.15576e7
rng = np.random.default_rng(0)


def table1():
    t = {}
    L = open(os.path.join(D, 'SPARC_Lelli2016c.mrt')).read().split('\n')
    i = [k for k, l in enumerate(L) if l.startswith('-----')][-1]
    for l in L[i + 1:]:
        if l.strip():
            w = l.split(); t[w[0]] = dict(Rdisk=float(w[11]), RHI=float(w[14]), Q=int(w[17]))
    return t


def bracket(x, l):
    j = spherical_jn(l, x); jp = spherical_jn(l, x, derivative=True)
    return j ** 2 + jp ** 2 + l * (l + 1) * j ** 2 / x ** 2


def v_wave(r, lrho, k, l, rmax):
    grid = np.linspace(1e-4, rmax, 600); u = 10 ** lrho * bracket(k * grid, l)
    M = 4 * np.pi * np.concatenate([[0], np.cumsum(0.5 * (u[1:] * grid[1:] ** 2 + u[:-1] * grid[:-1] ** 2) * np.diff(grid))])
    return np.sqrt(G * np.interp(r, grid, M) / r)


def v_bur(r, lrho, r0):
    x = r / r0; return np.sqrt(G * np.pi * 10 ** lrho * r0 ** 3 * (np.log1p(x ** 2) + 2 * np.log1p(x) - 2 * np.arctan(x)) / r)


def best(fun, starts, lo, hi):
    b = None
    for p0 in starts:
        try: s = least_squares(fun, p0, bounds=(lo, hi))
        except Exception: continue
        if b is None or s.cost < b.cost: b = s
    return b


# ---- numerical checks of the properties claimed in the docstring --------------------------------------------------------------------
print('CHECK  large-radius envelope: u * r^2 / (k^2) tends to a constant (1/2) for every l; centre value u(0)/u_max:')
x = np.array([30., 60., 120., 240.])
for l in (0, 1, 2, 3):
    print('  l=%d  u x^2 at x = 30, 60, 120, 240: %s   u(x=1e-3)/max u: %.3g' % (l, np.round(bracket(x, l) * x ** 2, 3), bracket(np.array([1e-3]), l)[0] / bracket(np.linspace(1e-3, 20, 4000), l).max()))

T = table1(); gals = []
for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
    name = os.path.basename(f)[:-11]; a = np.loadtxt(f)
    r, v, e0, vg, vd, vb = a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5]
    e = np.maximum(np.maximum(e0, 0.05 * v), 1e-3)
    Vb = np.sqrt(np.maximum(vg * np.abs(vg) + 0.5 * vd * np.abs(vd) + 0.7 * vb * np.abs(vb), 0))
    gals.append(dict(name=name, r=r, v=v, e=e, Vb=Vb, rl=r.max(), RHI=T[name]['RHI'] if T[name]['RHI'] > 0 else r.max(), n=len(r), vmx=v.max()))

print('\nPART A/B  fits, all %d galaxies, 5%% error floor, fixed mass-to-light' % len(gals))
for g in gals:
    chi = lambda m: float(np.sum(((m - g['v']) / g['e']) ** 2))
    s = best(lambda p: (np.sqrt(g['Vb'] ** 2 + v_bur(g['r'], *p) ** 2) - g['v']) / g['e'], [(7.5, g['rl'] * q) for q in (.1, .3, .8)], [3, .05], [12, 10 * g['rl']])
    g['BUR'] = 2 * s.cost; g['BUR_res'] = g['v'] - np.sqrt(g['Vb'] ** 2 + v_bur(g['r'], *s.x) ** 2)
    for l in (0, 1, 2, 3):
        st = [(np.log10(g['vmx'] ** 2 / G / g['rl'] / (4 * np.pi) * 3), 2 * np.pi / (g['rl'] * q)) for q in (0.3, 1, 3)]
        s = best(lambda p: (np.sqrt(g['Vb'] ** 2 + v_wave(g['r'], p[0], p[1], l, g['rl']) ** 2) - g['v']) / g['e'], st,
                 [0, 2 * np.pi / (30 * g['rl'])], [14, 2 * np.pi / (0.2 * g['rl'])])
        g['W%d' % l] = 2 * s.cost; g['W%d_lam' % l] = 2 * np.pi / s.x[1]
res = gals; n = np.array([g['n'] for g in res])
print('%-26s %14s %10s %9s' % ('model (2 parameters each)', 'median chi2/dof', 'median BIC', 'BIC wins'))
mods = ['BUR', 'W0', 'W1', 'W2', 'W3']; names = {'BUR': 'baryons + Burkert (reference)', 'W0': 'baryons + standing wave l=0', 'W1': 'baryons + standing wave l=1', 'W2': 'baryons + standing wave l=2', 'W3': 'baryons + standing wave l=3'}
bic = np.array([[g[m] + 2 * np.log(g['n']) for g in res] for m in mods]); win = np.argmin(bic, axis=0)
for j, m in enumerate(mods): print('%-26s %14.2f %10.1f %9d' % (names[m], np.median([g[m] / (g['n'] - 2) for g in res]), np.median(bic[j]), np.sum(win == j)))
for l in (0, 1, 2, 3):
    d = bic[mods.index('W%d' % l)] - bic[0]; print('  l=%d vs Burkert: median dBIC %+.1f, wave better in %d of %d' % (l, np.median(d), np.sum(d < 0), len(d)))

print('\nPART B  fitted wavelength (best of l = 0..3 per galaxy is NOT taken; l = 2, the gravitational-wave multipole, and l = 0 shown)')
for l in (0, 2):
    lam = np.array([g['W%d_lam' % l] for g in res]); R = np.array([g['RHI'] for g in res]); Rl = np.array([g['rl'] for g in res])
    ok = (lam > 0.25 * Rl) & (lam < 19 * Rl)
    print('  l=%d  wavelength / HI radius: median %.2f, 16-84%% [%.2f, %.2f]; log-log slope vs HI radius %.2f; %d of %d fits are interior (not at a bound)' % (
        l, np.median(lam / R), *np.percentile(lam / R, [16, 84]), np.polyfit(np.log10(R[ok]), np.log10(lam[ok]), 1)[0], ok.sum(), len(ok)))
    print('       median wavelength %.1f kpc = %.0f thousand ly; wave period lambda/c = %.0f thousand years' % (np.median(lam), np.median(lam) * LY_PER_KPC / 1e3, np.median(lam) * LY_PER_KPC / 1e3))

print('\nPART C  residuals of the baryons + Burkert fit: is there a common radial wiggle with wavelength q x R_HI?')
qs = np.linspace(0.1, 1.2, 45)
def stat(Rref):
    S = np.zeros(len(qs)); cnt = np.zeros(len(qs))
    for g, Rg in zip(res, Rref):
        res_ = g['BUR_res'] / g['e']
        for i, q in enumerate(qs):
            lam = q * Rg
            if g['rl'] < 1.5 * lam or g['n'] < 12: continue
            A = np.vstack([np.sin(2 * np.pi * g['r'] / lam), np.cos(2 * np.pi * g['r'] / lam)]).T
            c, *_ = np.linalg.lstsq(A, res_, rcond=None); S[i] += np.sum((A @ c) ** 2) / g['n']; cnt[i] += 1
    return S / np.maximum(cnt, 1), cnt
Rtrue = np.array([g['RHI'] for g in res])
obs, cnt = stat(Rtrue); prom = lambda S: S.max() - np.median(S)
# Null: keep every galaxy's residuals exactly as they are (smooth misfit included) and shuffle which size goes with which galaxy.
# If the wiggles scale with galaxy size, the true assignment concentrates the stacked power at one q and beats the shuffles.
null = np.array([prom(stat(rng.permutation(Rtrue))[0]) for _ in range(100)])
imax = int(np.argmax(obs))
print('  galaxies contributing at each q: min %d, max %d' % (cnt.min(), cnt.max()))
print('  stacked power S(q): maximum at q = %.2f; peak prominence (max - median over q) = %.4f; shuffled-size null: mean %.4f, 95th percentile %.4f, fraction of shuffles >= observed: %.3f' % (
    qs[imax], prom(obs), null.mean(), np.percentile(null, 95), np.mean(null >= prom(obs))))
print('  S(q) at q = 0.25, 0.5, 0.67, 1.0:', {q: round(float(obs[np.argmin(abs(qs - q))]), 4) for q in (0.25, 0.5, 0.67, 1.0)})
print('  (a first version permuted each galaxy\'s residuals; that null is white noise and any smooth misfit then looks like a signal, z = 11.5. It was wrong and is replaced by the shuffled-size null above.)')

print('\nPART D  orders of magnitude (a wave at speed c; Milky-Way-sized: wavelength = 100,000 ly = 30.7 kpc, V = 220 km/s)')
lam_m = 30.7 * KPC_M; w = 2 * np.pi * 299792458 / lam_m; T = lam_m / 299792458 / YR_S
print('  period lambda/c = %.3g years; phase advanced in 76 years = %.2g of a cycle (%.2g degrees); wave cycles in 200,000 years = %.2f' % (T, 76 / T, 360 * 76 / T, 2e5 / T))
rho_loc = 0.01 * 1.989e30 / (3.0857e16) ** 3                 # 0.01 Msun/pc^3 in kg/m^3
h = np.sqrt(32 * np.pi * 6.674e-11 * rho_loc / w ** 2)       # u = rho c^2 = c^2 w^2 h^2/(32 pi G)
print('  strain whose averaged energy density equals a local halo density of 0.01 Msun/pc^3 at this wavelength: h = %.2g' % h)
print('  the galaxy\'s own potential depth (V/c)^2 = %.2g, so the required wave amplitude exceeds it by a factor %.0f' % ((220 / C_KMS) ** 2, h / (220 / C_KMS) ** 2))
