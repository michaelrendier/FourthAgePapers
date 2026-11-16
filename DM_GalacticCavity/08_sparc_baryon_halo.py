#!/usr/bin/env python3
"""Does the halo follow the baryons?  Radial acceleration relation, halo parameters against baryon properties, and age.

Written 2026-11-16. numpy + scipy; run cold:  python3 -I 08_sparc_baryon_halo.py   (from this directory)

The author's assumption tested here: the halo is a shape of gravity, not independent of the matter ('a give and take a la Maxwell'); and
older galaxies have less or no halo.  Mainstream literature only: McGaugh, Lelli & Schombert (2016, PRL 117, 201101) radial acceleration relation;
Lelli et al. (2017, ApJ 836, 152) for its scatter; Burkert (1995) halo; Hubble type as the only age proxy SPARC carries (a WEAK proxy: type is
confounded with mass, gas fraction and environment; it is used because nothing better is in the table).

PART A  the radial acceleration relation: g_obs = V_obs^2/r against g_bar = V_bar^2/r, all points, fixed mass-to-light (0.5, 0.7);
        fit g+ in g_obs = g_bar / (1 - exp(-sqrt(g_bar/g+))); scatter in dex; scatter of per-galaxy mean offsets.
PART B  baryons + Burkert per galaxy; the halo's mass inside the last measured radius, its core radius and its central density,
        against the baryons' mass inside the same radius, disk scale length and flat velocity: Spearman and log-log slope.
        If the halo were independent of the baryons these would be uncorrelated after the obvious size scaling; the scatter of log M_halo
        at fixed log M_bar is reported.
PART C  Hubble type T (0 = S0 ... 10 = irregular, 11 = BCD) as an age proxy: dark-matter fraction f_DM = 1 - V_bar^2/V_obs^2 at the last measured
        radius and at 2.2 disk scale lengths, against T, raw and with the baryonic mass removed (partial Spearman).
"""
import glob, os, warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)
import numpy as np
from scipy.optimize import least_squares, minimize_scalar
from scipy.stats import spearmanr

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'data', 'SPARC')
G = 4.30091e-6; CONV = 1e6 / 3.0857e19            # (km/s)^2/kpc -> m/s^2
rng = np.random.default_rng(0)


def table1():
    t = {}
    L = open(os.path.join(D, 'SPARC_Lelli2016c.mrt')).read().split('\n')
    i = [k for k, l in enumerate(L) if l.startswith('-----')][-1]
    for l in L[i + 1:]:
        if l.strip():
            w = l.split(); t[w[0]] = dict(T=int(w[1]), Rdisk=float(w[11]), RHI=float(w[14]), Vflat=float(w[15]), Q=int(w[17]))
    return t


def v_bur(r, lrho, r0):
    x = r / r0; M = np.pi * 10 ** lrho * r0 ** 3 * (np.log1p(x ** 2) + 2 * np.log1p(x) - 2 * np.arctan(x)); return np.sqrt(G * M / r)


def best(fun, starts, lo, hi):
    b = None
    for p0 in starts:
        try: s = least_squares(fun, p0, bounds=(lo, hi))
        except Exception: continue
        if b is None or s.cost < b.cost: b = s
    return b


def partial_spearman(x, y, z):
    rk = lambda a: np.argsort(np.argsort(a)).astype(float)
    x, y, z = rk(x), rk(y), rk(z)
    fx = x - np.polyval(np.polyfit(z, x, 1), z); fy = y - np.polyval(np.polyfit(z, y, 1), z)
    return np.corrcoef(fx, fy)[0, 1]


T = table1(); gals = []
for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
    name = os.path.basename(f)[:-11]; a = np.loadtxt(f)
    r, v, e0, vg, vd, vb = a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5]
    e = np.maximum(np.maximum(e0, 0.05 * v), 1e-3)
    Vb = np.sqrt(np.maximum(vg * np.abs(vg) + 0.5 * vd * np.abs(vd) + 0.7 * vb * np.abs(vb), 0))
    gals.append(dict(name=name, r=r, v=v, e=e, Vb=Vb, rl=r.max(), n=len(r), vmx=v.max(), **T[name]))

print('PART A  radial acceleration relation, %d galaxies' % len(gals))
gb = np.concatenate([g['Vb'] ** 2 / g['r'] for g in gals]) * CONV; go = np.concatenate([g['v'] ** 2 / g['r'] for g in gals]) * CONV
gid = np.concatenate([[i] * g['n'] for i, g in enumerate(gals)]); ok = gb > 0
rar = lambda gbar, gd: gbar / (1 - np.exp(-np.sqrt(gbar / gd)))
sc = lambda lgd: np.sqrt(np.mean((np.log10(go[ok]) - np.log10(rar(gb[ok], 10 ** lgd))) ** 2))
m = minimize_scalar(sc, bounds=(-11, -9), method='bounded'); gd = 10 ** m.x
resid = np.log10(go[ok]) - np.log10(rar(gb[ok], gd)); gi = gid[ok]
print('  %d points; best g+ = %.2e m/s^2 (McGaugh et al. 2016 report 1.20e-10); rms scatter about the relation = %.3f dex' % (ok.sum(), gd, resid.std()))
off = np.array([resid[gi == i].mean() for i in np.unique(gi) if (gi == i).sum() >= 5]); print('  per-galaxy mean offsets (N=%d): rms %.3f dex; median point-wise scatter inside a galaxy %.3f dex' % (
    len(off), off.std(), np.median([resid[gi == i].std() for i in np.unique(gi) if (gi == i).sum() >= 5])))
print('  the relation is one-parameter and holds across 4 decades of g_bar: a halo fixed by an independent formation history would not give this;')
print('  a halo that depends on the baryons would (the standard reading of the RAR is exactly this dependence, not any one model)')

print('\nPART B  baryons + Burkert, per galaxy; halo against baryons')
rows = []
for g in gals:
    s = best(lambda p: (np.sqrt(g['Vb'] ** 2 + v_bur(g['r'], *p) ** 2) - g['v']) / g['e'], [(7.5, g['rl'] * q) for q in (.1, .3, .8)], [3, .05], [12, 10 * g['rl']])
    Mh = v_bur(np.array([g['rl']]), *s.x)[0] ** 2 * g['rl'] / G; Mb = g['Vb'][-1] ** 2 * g['rl'] / G
    rows.append(dict(g, lrho=s.x[0], r0=s.x[1], Mh=Mh, Mb=Mb, chi=2 * s.cost / max(g['n'] - 2, 1)))
R = [x for x in rows if x['Mb'] > 0 and x['Rdisk'] > 0 and x['Q'] <= 2 and x['r0'] < 9.9 * x['rl'] and x['Mh'] > 0]
print('  %d galaxies with Q <= 2, a bulge/disk scale length, a baryon mass and an interior core radius' % len(R))
L = lambda k: np.log10([x[k] for x in R])
pairs = [('Mh', 'Mb', 'log M_halo(<R_last)  vs  log M_bar(<R_last)'), ('r0', 'Rdisk', 'log r0 (core radius)   vs  log R_disk'),
         ('lrho', 'Rdisk', 'log rho0 (central density) vs  log R_disk'), ('Mh', 'Vflat', 'log M_halo(<R_last)  vs  log V_flat')]
for a_, b_, lab in pairs:
    xa = np.array([x[a_] for x in R]) if a_ == 'lrho' else L(a_); xb = L(b_)
    ok2 = np.isfinite(xa) & np.isfinite(xb) & (np.array([x['Vflat'] for x in R]) > 0)
    print('  %-46s Spearman %+.2f   log-log slope %+.2f' % (lab, spearmanr(xb[ok2], xa[ok2])[0], np.polyfit(xb[ok2], xa[ok2], 1)[0]))
lm, lb = L('Mh'), L('Mb'); c = np.polyfit(lb, lm, 1)
print('  scatter of log M_halo at fixed log M_bar (about the fitted line, slope %.2f): %.2f dex' % (c[0], np.std(lm - np.polyval(c, lb))))
lrl = L('rl')
print('  both masses share the factor R_last (M = V^2 R / G), so the shared radius alone inflates the correlation; with log R_last removed (partial Spearman): %+.2f; halo velocity vs baryon velocity at R_last: Spearman %+.2f' % (
    partial_spearman(lb, lm, lrl), spearmanr([x['Vb'][-1] for x in R], [v_bur(np.array([x['rl']]), x['lrho'], x['r0'])[0] for x in R])[0]))
Rs = np.array([x['Rdisk'] for x in R])
print('  size null: shuffling which R_disk belongs to which galaxy changes the r0-R_disk Spearman from %+.2f to %.2f +- %.2f (100 shuffles)' % (
    spearmanr(Rs, [x['r0'] for x in R])[0], np.mean([spearmanr(rng.permutation(Rs), [x['r0'] for x in R])[0] for _ in range(100)]),
    np.std([spearmanr(rng.permutation(Rs), [x['r0'] for x in R])[0] for _ in range(100)])))

print('\nPART C  age proxy: Hubble type T against dark-matter fraction')
H = [x for x in rows if x['Mb'] > 0 and x['Rdisk'] > 0 and x['Q'] <= 2]
fl, f22 = [], []
for x in H:
    fl.append(1 - x['Vb'][-1] ** 2 / x['v'][-1] ** 2)
    k = np.argmin(abs(x['r'] - 2.2 * x['Rdisk'])); f22.append(1 - x['Vb'][k] ** 2 / x['v'][k] ** 2)
Tt = np.array([x['T'] for x in H]); lmb = np.log10([x['Mb'] for x in H]); fl = np.array(fl); f22 = np.array(f22)
print('  N = %d' % len(H))
for lab, f_ in (('last measured radius', fl), ('2.2 disk scale lengths', f22)):
    print('  f_DM at %-24s vs T: Spearman %+.2f; partial (baryon mass removed) %+.2f; median f_DM early (T<=3) %.2f, late (T>=7) %.2f' % (
        lab, spearmanr(Tt, f_)[0], partial_spearman(Tt, f_, lmb), np.median(f_[Tt <= 3]), np.median(f_[Tt >= 7])))
print('  numbers of galaxies: T<=3 %d, 4..6 %d, T>=7 %d' % (np.sum(Tt <= 3), np.sum((Tt > 3) & (Tt < 7)), np.sum(Tt >= 7)))
print('  early types (S0..Sab) with f_DM at the last radius below 0.2: %d of %d; late types with it below 0.2: %d of %d' % (
    np.sum(fl[Tt <= 3] < 0.2), np.sum(Tt <= 3), np.sum(fl[Tt >= 7] < 0.2), np.sum(Tt >= 7)))
print('  note: SPARC is late-type dominated; its 175 galaxies are spirals and irregulars (it has 0 true ellipticals), so \'no halo\' ellipticals are not in this test.')
