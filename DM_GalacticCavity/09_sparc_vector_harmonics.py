#!/usr/bin/env python3
"""Standing-wave halos with vector-harmonic angular structure and multipole mixing.

Written 2026-11-16. numpy + scipy; run cold:  python3 -I 09_sparc_vector_harmonics.py   (from this directory; a few minutes)

05_sparc_standing_wave.py used a SCALAR wave.  A real gravitational wave is spin 2 and a light wave spin 1.  This script does the spin-1 step, which is
textbook (Jackson, Classical Electrodynamics, 3rd ed., section 9.7): the standing multipole fields of the vector Helmholtz equation, with
    E = j_l(kr) X_lm  (magnetic-type multipole),  B = (-i/k) curl E, whose angle-integrated components give
    u_l(x) ~ j_l(x)^2 + [ j_l'(x) + j_l(x)/x ]^2 + l(l+1) j_l(x)^2 / x^2,   x = kr,  l >= 1
(first term: E; second: transverse B; third: radial B; the electric-type multipole has E and B exchanged and the same time average).
It differs from the scalar bracket j^2 + j'^2 + l(l+1) j^2/x^2 by the cross term 2 j j'/x + j^2/x^2.  There is no l = 0 vector multipole.
The spin-2 radial functions (Regge-Wheeler / Zerilli) are NOT derived here; they would change the same small terms; the large-radius envelope u x^2 -> const
is common to all spins (energy conservation of a radiation field) and so is the flat rotation curve it gives.

PART A  the vector bracket versus the scalar one: large-radius envelope and centre, numerically.
PART B  fits, baryons (fixed M/L 0.5, 0.7) + one vector multipole l = 1, 2, 3, two parameters (log rho_s, k) as in 05; Burkert and scalar l = 1 for reference.
PART C  multipole mixing: u = rho_s [ b_1 + a_2 b_2 + a_3 b_3 ] with a_2, a_3 >= 0 and one k (4 parameters), against the best single multipole and Burkert (BIC).
"""
import glob, os, warnings
import numpy as np
from scipy.optimize import least_squares
from scipy.special import spherical_jn
warnings.filterwarnings('ignore', category=RuntimeWarning)

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'data', 'SPARC'); G = 4.30091e-6


def bs(x, l):
    j = spherical_jn(l, x); jp = spherical_jn(l, x, derivative=True); return j ** 2 + jp ** 2 + l * (l + 1) * j ** 2 / x ** 2
def bv(x, l):
    j = spherical_jn(l, x); jp = spherical_jn(l, x, derivative=True); return j ** 2 + (jp + j / x) ** 2 + l * (l + 1) * j ** 2 / x ** 2


def v_from_u(r, u, grid):
    M = 4 * np.pi * np.concatenate([[0], np.cumsum(0.5 * (u[1:] * grid[1:] ** 2 + u[:-1] * grid[:-1] ** 2) * np.diff(grid))]); return np.sqrt(G * np.interp(r, grid, M) / r)
def v_single(r, lrho, k, l, rmax, b):
    grid = np.linspace(1e-4, rmax, 600); return v_from_u(r, 10 ** lrho * b(k * grid, l), grid)
def v_mix(r, lrho, k, a2, a3, rmax):
    grid = np.linspace(1e-4, rmax, 600); x = k * grid; return v_from_u(r, 10 ** lrho * (bv(x, 1) + a2 * bv(x, 2) + a3 * bv(x, 3)), grid)
def v_bur(r, lrho, r0):
    x = r / r0; return np.sqrt(G * np.pi * 10 ** lrho * r0 ** 3 * (np.log1p(x ** 2) + 2 * np.log1p(x) - 2 * np.arctan(x)) / r)


def best(fun, starts, lo, hi):
    b = None
    for p0 in starts:
        try: s = least_squares(fun, p0, bounds=(lo, hi))
        except Exception: continue
        if b is None or s.cost < b.cost: b = s
    return b


print('PART A  brackets')
x = np.array([30., 60., 120., 240.])
for l in (1, 2, 3):
    print('  l=%d  u x^2 at x = 30, 60, 120, 240: scalar %s  vector %s;  centre u(1e-3)/max: scalar %.3g  vector %.3g' % (
        l, np.round(bs(x, l) * x ** 2, 3), np.round(bv(x, l) * x ** 2, 3), bs(np.array([1e-3]), l)[0] / bs(np.linspace(1e-3, 20, 4000), l).max(), bv(np.array([1e-3]), l)[0] / bv(np.linspace(1e-3, 20, 4000), l).max()))

gals = []
for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
    name = os.path.basename(f)[:-11]; a = np.loadtxt(f)
    r, v, e0, vg, vd, vb = a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5]
    e = np.maximum(np.maximum(e0, 0.05 * v), 1e-3)
    gals.append(dict(name=name, r=r, v=v, e=e, Vb=np.sqrt(np.maximum(vg * np.abs(vg) + 0.5 * vd * np.abs(vd) + 0.7 * vb * np.abs(vb), 0)), rl=r.max(), n=len(r), vmx=v.max()))

print('\nPART B/C  fits, %d galaxies, 5%% floor, fixed M/L' % len(gals))
for g in gals:
    r, v, e, Vb, rl, vm = g['r'], g['v'], g['e'], g['Vb'], g['rl'], g['vmx']
    s = best(lambda p: (np.sqrt(Vb ** 2 + v_bur(r, *p) ** 2) - v) / e, [(7.5, rl * q) for q in (.1, .3, .8)], [3, .05], [12, 10 * rl]); g['BUR'] = (2 * s.cost, 2)
    st = [(np.log10(vm ** 2 / G / rl / (4 * np.pi) * 3), 2 * np.pi / (rl * q)) for q in (0.3, 1, 3)]; lo, hi = [0, 2 * np.pi / (30 * rl)], [14, 2 * np.pi / (0.2 * rl)]
    for lab, b, l in (('S1', bs, 1), ('V1', bv, 1), ('V2', bv, 2), ('V3', bv, 3)):
        s = best(lambda p: (np.sqrt(Vb ** 2 + v_single(r, p[0], p[1], l, rl, b) ** 2) - v) / e, st, lo, hi); g[lab] = (2 * s.cost, 2)
    s = best(lambda p: (np.sqrt(Vb ** 2 + v_mix(r, p[0], p[1], p[2], p[3], rl) ** 2) - v) / e, [list(q) + [0.5, 0.5] for q in st], lo + [0, 0], hi + [10, 10]); g['MIX'] = (2 * s.cost, 4); g['MIXp'] = s.x
mods = ['BUR', 'S1', 'V1', 'V2', 'V3', 'MIX']
nm = {'BUR': 'baryons + Burkert (reference)', 'S1': 'scalar l=1 (from 05)', 'V1': 'vector multipole l=1', 'V2': 'vector multipole l=2', 'V3': 'vector multipole l=3', 'MIX': 'vector mix l=1+2+3, one k (4 par)'}
bic = np.array([[g[m][0] + g[m][1] * np.log(g['n']) for g in gals] for m in mods]); win = np.argmin(bic, axis=0)
print('%-36s %3s %15s %10s %9s' % ('model', 'k', 'median chi2/dof', 'median BIC', 'BIC wins'))
for j, m in enumerate(mods):
    print('%-36s %3d %15.2f %10.1f %9d' % (nm[m], gals[0][m][1], np.median([g[m][0] / (g['n'] - g[m][1]) for g in gals]), np.median(bic[j]), np.sum(win == j)))
bs1 = np.min(bic[2:5], axis=0)
print('  mix vs best single vector multipole: median dBIC %+.1f, mix better in %d of %d; mix vs Burkert: median dBIC %+.1f, mix better in %d' % (
    np.median(bic[5] - bs1), np.sum(bic[5] < bs1), len(gals), np.median(bic[5] - bic[0]), np.sum(bic[5] < bic[0])))
a2 = np.array([g['MIXp'][2] for g in gals]); a3 = np.array([g['MIXp'][3] for g in gals])
print('  fitted mixing weights: a2 median %.2f (16-84%% %.2f-%.2f), a3 median %.2f (16-84%% %.2f-%.2f); at a bound (0 or 10): %d of %d' % (
    np.median(a2), *np.percentile(a2, [16, 84]), np.median(a3), *np.percentile(a3, [16, 84]), np.sum((a2 < 1e-3) | (a2 > 9.99) | (a3 < 1e-3) | (a3 > 9.99)), len(gals)))
