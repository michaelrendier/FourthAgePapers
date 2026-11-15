#!/usr/bin/env python3
"""Whole-dataset retest, mainstream models only, no d* and no framework constant anywhere.

Rewritten 2026-11-15 (the first version, 2026-11-14, carried a d*-based variant; the author's ruling is that a 'shape of gravity'
model needs no d*, and that nothing in the test may be outside established astrophysics literature). numpy + scipy; run cold:
    python3 -I 04_sparc_retest.py        (from this directory; a few minutes)

All 175 SPARC rotation curves (Lelli, McGaugh & Schombert 2016), every model fitted the same way (weighted least squares, 5 % error floor,
the raw-error version printed too), compared by chi2/dof and BIC.  Baryons: V_bar^2 = Vgas|Vgas| + Y_d Vdisk|Vdisk| + Y_b Vbul|Vbul|.

  Mass-to-light ratio: FIXED (Y_d = 0.5, Y_b = 0.7, Lelli et al. 2016) or FREE with the log-normal prior of Li et al. (2020, A&A 615, A3):
  sigma = 0.1 dex around 0.5 (disk) and 0.7 (bulge), added to chi2 as a penalty; a free Y_d counts as one parameter.

  B       baryons only
  RAR     baryons + McGaugh, Lelli & Schombert (2016) relation, g+ = 1.2e-10 m/s^2 (no halo; the MOND-like benchmark)
  ARC     empirical arctan rotation curve, v = vf (2/pi) arctan(r/rt)  (Courteau 1997, PASP 109, 1; the descriptive 'shape of the curve'; no baryons)
  B+ARC   baryons + a halo contribution of the same arctan form, V^2 = Vbar^2 + vc^2 (2/pi arctan(r/rt))^2
  B+NFW   baryons + NFW (Navarro, Frenk & White 1996), parameters V200, c in [2, 60]
  B+BUR   baryons + Burkert (1995), parameters rho0, r0
  B+EIN   baryons + Einasto (Einasto 1965; Navarro et al. 2004) with alpha = 0.17 fixed, parameters rho_-2, r_-2
  B+PIS   baryons + pseudo-isothermal sphere, parameters Vinf, rc
Halo models are run with fixed and with free mass-to-light ratio.
"""
import glob, os
import numpy as np
from scipy.optimize import least_squares
from scipy.special import gammainc, gamma as Gam
from scipy.stats import spearmanr

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'data', 'SPARC')
H0, G, GDAG = 0.070, 4.30091e-6, 1.2e-10 / 3.2408e-14      # km/s/kpc ; kpc (km/s)^2/Msun ; g+ in (km/s)^2/kpc
SIG = 0.1                                                   # dex, Li et al. 2020 prior width


def table1():
    t = {}
    L = open(os.path.join(D, 'SPARC_Lelli2016c.mrt')).read().split('\n')
    i = [k for k, l in enumerate(L) if l.startswith('-----')][-1]
    for l in L[i + 1:]:
        if l.strip():
            w = l.split(); t[w[0]] = dict(Q=int(w[17]), Rdisk=float(w[11]), RHI=float(w[14]))
    return t


arc = lambda r, rt: (2 / np.pi) * np.arctan(r / rt)
def v_nfw(r, V200, c):
    R200 = V200 / (10 * H0); x = np.maximum(r * c / R200, 1e-9)
    return V200 * np.sqrt((np.log1p(x) - x / (1 + x)) / (x * (np.log1p(c) - c / (1 + c))))
def v_bur(r, lrho, r0):
    x = r / r0; M = np.pi * 10 ** lrho * r0 ** 3 * (np.log1p(x ** 2) + 2 * np.log1p(x) - 2 * np.arctan(x)); return np.sqrt(G * M / r)
def v_ein(r, lrho, r2, a=0.17):
    n = 1 / a; x = 2 * n * (r / r2) ** (1 / n); M = 4 * np.pi * 10 ** lrho * r2 ** 3 * n * np.exp(2 * n) * (2 * n) ** (-3 * n) * Gam(3 * n) * gammainc(3 * n, x); return np.sqrt(G * M / r)
v_pis = lambda r, Vi, rc: Vi * np.sqrt(np.maximum(1 - (rc / r) * np.arctan(r / rc), 0))


def best(fun, starts, lo, hi):
    b = None
    for p0 in starts:
        try: s = least_squares(fun, p0, bounds=(lo, hi))
        except Exception: continue
        if b is None or s.cost < b.cost: b = s
    return b


def run(floor):
    T = table1(); out = []
    for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
        name = os.path.basename(f)[:-11]; a = np.loadtxt(f)
        r, v, e0, vg, vd, vb = a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5]
        e = np.maximum(np.maximum(e0, floor * v), 1e-3); n = len(r); rl = r.max(); vmx = v.max()
        hasb = bool(np.any(vb != 0))
        def vbar(yd, yb): return np.sqrt(np.maximum(vg * np.abs(vg) + yd * vd * np.abs(vd) + yb * vb * np.abs(vb), 0))
        Vb0 = vbar(0.5, 0.7)
        R = dict(name=name, Q=T[name]['Q'], n=n, rl=rl, Rd=T[name]['Rdisk'], RHI=T[name]['RHI'])
        chi = lambda m: float(np.sum(((m - v) / e) ** 2))
        R['B'] = (chi(Vb0), 0)
        gb = np.maximum(Vb0 ** 2, 1e-6) / r; R['RAR'] = (chi(np.sqrt(gb / (1 - np.exp(-np.sqrt(gb / GDAG))) * r)), 0)
        s = best(lambda p: (p[0] * arc(r, p[1]) - v) / e, [(vmx, rl * q) for q in (.05, .25, .8)], [1, .01], [1000, 5 * rl]); R['ARC'] = (2 * s.cost, 2); R['ARC_rt'] = s.x[1]
        # halo families: (label, function(r, p) -> V_halo, starts, lo, hi)
        fam = {'B+ARC': (lambda r, p: p[0] * arc(r, p[1]), [(vmx, rl * q) for q in (.05, .25, .8)], [0, .01], [1000, 5 * rl]),
               'B+NFW': (lambda r, p: v_nfw(r, *p), [(vmx * .8, c) for c in (5, 12, 30)], [5, 2], [1000, 60]),
               'B+BUR': (lambda r, p: v_bur(r, *p), [(7.5, rl * q) for q in (.1, .3, .8)], [3, .05], [12, 10 * rl]),
               'B+EIN': (lambda r, p: v_ein(r, *p), [(6.5, rl * q) for q in (.3, 1, 3)], [2, .05], [12, 30 * rl]),
               'B+PIS': (lambda r, p: v_pis(r, *p), [(vmx, rl * q) for q in (.05, .25, .8)], [1, .01], [1000, 5 * rl])}
        for k, (hf, st, lo, hi) in fam.items():
            s = best(lambda p: (np.sqrt(Vb0 ** 2 + hf(r, p) ** 2) - v) / e, st, lo, hi); R[k] = (2 * s.cost, 2)
            if k == 'B+ARC': R['B+ARC_rt'] = s.x[1]
            # free mass-to-light: p = halo params + log10 Yd (+ log10 Yb)
            nh = len(lo); lo2, hi2 = list(lo) + [-1.0], list(hi) + [0.3]
            if hasb: lo2 += [-1.0]; hi2 += [0.3]
            def res(p):
                Vb = vbar(10 ** p[nh], 10 ** p[nh + 1] if hasb else 0.7)
                pen = [(p[nh] - np.log10(0.5)) / SIG] + ([(p[nh + 1] - np.log10(0.7)) / SIG] if hasb else [])
                return np.concatenate([(np.sqrt(Vb ** 2 + hf(r, p[:nh]) ** 2) - v) / e, pen])
            s2 = best(res, [list(s0) + [np.log10(.5)] + ([np.log10(.7)] if hasb else []) for s0 in [s.x]], lo2, hi2)
            vv = (np.sqrt(vbar(10 ** s2.x[nh], 10 ** s2.x[nh + 1] if hasb else 0.7) ** 2 + hf(r, s2.x[:nh]) ** 2) - v) / e
            R[k + ' (free M/L)'] = (float(np.sum(vv ** 2)), 2 + 1 + int(hasb))
            R[k + ' (free M/L) Yd'] = 10 ** s2.x[nh]
        out.append(R)
    return out


FIX = ['B', 'RAR', 'ARC', 'B+ARC', 'B+NFW', 'B+BUR', 'B+EIN', 'B+PIS']
FREE = [m + ' (free M/L)' for m in FIX[3:]]
for floor, label in ((0.05, 'error floor 5% of V_obs'), (0.0, 'raw SPARC errors')):
    res = run(floor)
    print('=' * 104); print('%s;  %d galaxies' % (label, len(res)))
    for title, models in (('fixed M/L (0.5, 0.7); BIC wins within this set', FIX), ('free M/L with the Li et al. 2020 prior, halo models only; BIC wins within this set', FREE)):
        print('--', title)
        print('%-22s %3s %14s %14s %10s %9s' % ('model', 'k', 'median chi2/dof', 'mean chi2/dof', 'median BIC', 'BIC wins'))
        bic = np.array([[R[m][0] + R[m][1] * np.log(R['n']) for R in res] for m in models]); win = np.argmin(bic, axis=0)
        for j, m in enumerate(models):
            k = res[0][m][1]; red = np.array([R[m][0] / max(R['n'] - R[m][1], 1) for R in res])
            print('%-22s %3d %14.2f %14.2f %10.1f %9d' % (m, k, np.median(red), red.mean(), np.median(bic[j]), np.sum(win == j)))
    print('-- pairwise BIC (negative = first model better)')
    for a_, b_ in (('B+ARC', 'B+NFW'), ('B+BUR', 'B+NFW'), ('B+EIN', 'B+NFW'), ('B+PIS', 'B+NFW'), ('B+ARC', 'B+PIS'), ('B+ARC', 'B+BUR'), ('B+ARC (free M/L)', 'B+NFW (free M/L)'), ('B+ARC (free M/L)', 'B+BUR (free M/L)')):
        d = np.array([(R[a_][0] + R[a_][1] * np.log(R['n'])) - (R[b_][0] + R[b_][1] * np.log(R['n'])) for R in res])
        print('  %-18s vs %-18s median dBIC %+6.1f; first better in %3d of %d' % (a_, b_, np.median(d), np.sum(d < 0), len(d)))
    print('-- free mass-to-light ratio found (median Y_d): ' + ', '.join('%s %.2f [16-84%% %.2f-%.2f, %d of %d differ from 0.50 by > 0.01]' % ((m.split(' ')[0], np.median(y)) + tuple(np.percentile(y, [16, 84])) + (int(np.sum(np.abs(y - 0.5) > 0.01)), len(y))) for m in FREE for y in [np.array([R[m + ' Yd'] for R in res])]))
    for key, lab in (('ARC_rt', 'ARC'), ('B+ARC_rt', 'B+ARC')):
        ok = [R for R in res if 0.02 < R[key] / R['rl'] < 2 and R['Rd'] > 0 and R['RHI'] > 0]; y = np.log10([R[key] for R in ok])
        for ref, nm in (('rl', 'last measured radius'), ('Rd', 'disk scale length'), ('RHI', 'HI radius')):
            x = np.log10([R[ref] for R in ok]); print('  %-6s transition radius vs %-21s N=%d  Spearman %.2f  log-log slope %.2f' % (lab, nm, len(ok), spearmanr(x, y)[0], np.polyfit(x, y, 1)[0]))
