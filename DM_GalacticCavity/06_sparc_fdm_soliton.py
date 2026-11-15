#!/usr/bin/env python3
"""Fuzzy dark matter (a standing-wave halo already in the literature) against SPARC: soliton core + NFW envelope.

Written 2026-11-15. numpy + scipy; run cold:  python3 -I 06_sparc_fdm_soliton.py   (from this directory; several minutes)

Established model (Schive, Chiueh & Broadhurst 2014, Nature Physics 10, 496; Schive et al. 2014, PRL 113, 261302): a scalar field of mass m ~ 1e-22 eV
has de Broglie wavelength ~ kpc; halos hold a standing-wave soliton core surrounded by an interference pattern that averages to NFW. Used forms
(recalled from those papers; check the constants against them before citing):
  soliton   rho(r) = 1.9e9 (m / 1e-23 eV)^-2 (r_c / kpc)^-4 [1 + 0.091 (r/r_c)^2]^-8   Msun/kpc^3      (r_c = core radius, 1 free parameter per galaxy
            once the single global mass m is chosen)
  envelope  NFW(V200, c)
  total     rho = rho_soliton + rho_NFW   (a SIMPLIFICATION: the papers join the two at a transition radius ~ 3 r_c; the plain sum double counts a little
            near the join; no fit here is tuned to hide that)
  core-halo relation (Schive et al. 2014 PRL): r_c ~ 1.6 (m / 1e-22 eV)^-1 (M_h / 1e9 Msun)^(-1/3) kpc  -> log r_c should fall with log M_h with slope -1/3.
Baryons fixed (Y_d = 0.5, Y_b = 0.7), 5% error floor, same as 04_sparc_retest.py. m is global: scanned on a grid, chi2 summed over galaxies.
Compared with: baryons + NFW (2 parameters) and baryons + Burkert (2); soliton+NFW has 3 per galaxy (r_c, V200, c) plus the one global m.
"""
import glob, os
import numpy as np
from scipy.optimize import least_squares

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'data', 'SPARC')
G, H0 = 4.30091e-6, 0.070


def v_nfw(r, V200, c):
    R200 = V200 / (10 * H0); x = np.maximum(r * c / R200, 1e-9)
    return V200 * np.sqrt((np.log1p(x) - x / (1 + x)) / (x * (np.log1p(c) - c / (1 + c))))
def v_bur(r, lrho, r0):
    x = r / r0; return np.sqrt(G * np.pi * 10 ** lrho * r0 ** 3 * (np.log1p(x ** 2) + 2 * np.log1p(x) - 2 * np.arctan(x)) / r)
def v_sol(r, rc, m23):
    rho0 = 1.9e9 * m23 ** -2 * rc ** -4
    # closed-form not needed: integrate on a grid
    grid = np.linspace(1e-4, r.max(), 500); u = rho0 / (1 + 0.091 * (grid / rc) ** 2) ** 8
    M = 4 * np.pi * np.concatenate([[0], np.cumsum(0.5 * (u[1:] * grid[1:] ** 2 + u[:-1] * grid[:-1] ** 2) * np.diff(grid))])
    return np.sqrt(G * np.interp(r, grid, M) / r)

def best(fun, starts, lo, hi):
    b = None
    for p0 in starts:
        try: s = least_squares(fun, p0, bounds=(lo, hi))
        except Exception: continue
        if b is None or s.cost < b.cost: b = s
    return b

gals = []
for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
    a = np.loadtxt(f); r, v, e0, vg, vd, vb = a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5]
    e = np.maximum(np.maximum(e0, 0.05 * v), 1e-3); Vb = np.sqrt(np.maximum(vg * np.abs(vg) + 0.5 * vd * np.abs(vd) + 0.7 * vb * np.abs(vb), 0))
    gals.append(dict(name=os.path.basename(f)[:-11], r=r, v=v, e=e, Vb=Vb, rl=r.max(), n=len(r), vmx=v.max()))

# reference models
for g in gals:
    s = best(lambda p: (np.sqrt(g['Vb'] ** 2 + v_nfw(g['r'], *p) ** 2) - g['v']) / g['e'], [(g['vmx'] * .8, c) for c in (5, 12, 30)], [5, 2], [1000, 60]); g['NFW'] = 2 * s.cost; g['NFW_x'] = s.x
    s = best(lambda p: (np.sqrt(g['Vb'] ** 2 + v_bur(g['r'], *p) ** 2) - g['v']) / g['e'], [(7.5, g['rl'] * q) for q in (.1, .3, .8)], [3, .05], [12, 10 * g['rl']]); g['BUR'] = 2 * s.cost

print('global boson mass scan (chi2 summed over 175 galaxies; baryons + NFW alone: %.0f; baryons + Burkert alone: %.0f)' % (sum(g['NFW'] for g in gals), sum(g['BUR'] for g in gals)))
ms = [0.3, 1, 3, 10, 30, 100]          # m / 1e-23 eV  -> 3e-24 ... 1e-21 eV
tot = {}
for m23 in ms:
    chi = 0
    for g in gals:
        def res(p): return (np.sqrt(g['Vb'] ** 2 + v_sol(g['r'], p[0], m23) ** 2 + v_nfw(g['r'], p[1], p[2]) ** 2) - g['v']) / g['e']
        starts = [(g['rl'] * q, g['NFW_x'][0], g['NFW_x'][1]) for q in (.05, .2)] + [(g['rl'] * .1, 30, 10)]
        s = best(res, starts, [0.02, 5, 2], [3 * g['rl'], 1000, 60]); g.setdefault('SOL', {})[m23] = (2 * s.cost, s.x)
        chi += 2 * s.cost
    tot[m23] = chi; print('  m = %6.1e eV: total chi2 = %.0f' % (m23 * 1e-23, chi))
mbest = min(tot, key=tot.get); print('best global mass: m = %.1e eV' % (mbest * 1e-23))

bic = lambda c, k, n: c + k * np.log(n)
rows = []
for g in gals:
    c, x = g['SOL'][mbest]; M200 = x[1] ** 3 / (10 * G * H0)
    rows.append((bic(g['NFW'], 2, g['n']), bic(g['BUR'], 2, g['n']), bic(c, 3, g['n']), g['NFW'] / (g['n'] - 2), g['BUR'] / (g['n'] - 2), c / (g['n'] - 3), x[0], M200, g['rl']))
B = np.array(rows)
print('\n%-34s %14s %10s' % ('model', 'median chi2/dof', 'median BIC'))
for nm, j, k in (('baryons + NFW (2 par)', 3, 0), ('baryons + Burkert (2 par)', 4, 1), ('baryons + soliton + NFW (3 par)', 5, 2)):
    print('%-34s %14.2f %10.1f' % (nm, np.median(B[:, j]), np.median(B[:, k])))
w = np.argmin(B[:, :3], axis=1); print('BIC wins among the three:', {nm: int(np.sum(w == i)) for i, nm in enumerate(['NFW', 'Burkert', 'soliton+NFW'])})
d = B[:, 2] - B[:, 0]; print('soliton+NFW vs NFW: median dBIC %+.1f, soliton better in %d of %d' % (np.median(d), np.sum(d < 0), len(d)))
d = B[:, 2] - B[:, 1]; print('soliton+NFW vs Burkert: median dBIC %+.1f, soliton better in %d of %d' % (np.median(d), np.sum(d < 0), len(d)))
ok = (B[:, 6] > 0.05) & (B[:, 6] < 2.5 * B[:, 8]) & (B[:, 7] > 0)
sl = np.polyfit(np.log10(B[ok, 7]), np.log10(B[ok, 6]), 1)
print('core-halo relation: fitted r_c vs fitted M200 over %d galaxies: log-log slope %.2f (the soliton-halo relation predicts -0.33), scatter %.2f dex' % (
    ok.sum(), sl[0], np.std(np.log10(B[ok, 6]) - np.polyval(sl, np.log10(B[ok, 7])))))
print('median fitted core radius %.2f kpc' % np.median(B[ok, 6]))
