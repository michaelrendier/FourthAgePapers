#!/usr/bin/env python3
"""Whole-dataset retest: the author's cavity assumptions against standard halo models, on all SPARC rotation curves.

Written 2026-11-14. numpy + scipy; run cold:  python3 -I 04_sparc_retest.py   (from this directory; ~1 min)

Question asked by the author: applied across the whole data set, is the cavity picture a better model or not?
Every galaxy with a rotation curve (175) is fitted with each model below by weighted least squares, and compared by chi2/dof,
AIC and BIC. Baryons use Lelli et al.'s 3.6 um values, fixed: Upsilon_disk = 0.5, Upsilon_bulge = 0.7 (no free mass-to-light ratio, so
the baryon part has no free parameter in any model). V_bar^2 = Vgas|Vgas| + 0.5 Vdisk|Vdisk| + 0.7 Vbul|Vbul|.

  B     baryons only                                   0 parameters
  RAR   baryons + McGaugh 2016 relation (g+ = 1.2e-10)  0 parameters
  CAV   cavity mode alone: v = vf (2/pi) arctan(r/rt)  2 (vf, rt)   [the shape used in dark_matter_cavity.py]
  CAVd  the same with rt = d* x r_last                 1 (vf)       [author's assumption d* = 0.246, r_last = last measured radius]
  B+CAV baryons + cavity halo, V^2 = Vbar^2 + vc^2 (2/pi arctan(r/rt))^2        2 (vc, rt)
  B+CAVd the same with rt = d* x r_last                1 (vc)
  B+NFW baryons + NFW halo                              2 (V200, c)   c in [2, 60]
  B+PIS baryons + pseudo-isothermal halo                2 (Vinf, rc)

Errors: the quoted errV, with a floor of 5% of V_obs (SPARC errors on well-measured curves are far below what a smooth model can meet).
The raw-error version is printed as well. Nothing is tuned to improve any model; the fitting set-up is the same for all.
"""
import glob, os
import numpy as np
from scipy.optimize import least_squares

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'data', 'SPARC')
D_STAR, H0, GDAG = 0.24600, 0.070, 1.2e-10 / 3.2408e-14      # d*, km/s/kpc, g+ in (km/s)^2/kpc

def table1():
    t = {}
    L = open(os.path.join(D, 'SPARC_Lelli2016c.mrt')).read().split('\n')
    i = [k for k, l in enumerate(L) if l.startswith('-----')][-1]
    for l in L[i + 1:]:
        if l.strip():
            w = l.split(); t[w[0]] = dict(Q=int(w[17]), Vflat=float(w[15]), Rdisk=float(w[11]), RHI=float(w[14]))
    return t

def arc(r, rt): return (2 / np.pi) * np.arctan(r / rt)
def vnfw(r, V200, c):
    R200 = V200 / (10 * H0); x = np.maximum(r * c / R200, 1e-9)
    return V200 * np.sqrt((np.log1p(x) - x / (1 + x)) / (x * (np.log1p(c) - c / (1 + c))))
def vpis(r, Vinf, rc): return Vinf * np.sqrt(np.maximum(1 - (rc / r) * np.arctan(r / rc), 0))

def fit(fun, p0s, lo, hi, r, v, e):
    best = None
    for p0 in p0s:
        try:
            s = least_squares(lambda p: (fun(r, *p) - v) / e, p0, bounds=(lo, hi))
        except Exception:
            continue
        if best is None or s.cost < best.cost: best = s
    return best

def run(floor):
    T = table1(); out = []
    for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
        name = os.path.basename(f)[:-11]; a = np.loadtxt(f)
        r, v, e0, vg, vd, vb = a[:, 0], a[:, 1], a[:, 2], a[:, 3], a[:, 4], a[:, 5]
        e = np.maximum(e0, floor * v); e = np.maximum(e, 1e-3)
        vb2 = vg * np.abs(vg) + 0.5 * vd * np.abs(vd) + 0.7 * vb * np.abs(vb)
        Vb = np.sqrt(np.maximum(vb2, 0)); rl = r.max(); vmx = v.max(); n = len(r)
        gb = np.maximum(vb2, 1e-6) / r
        Vrar = np.sqrt(np.maximum(gb / (1 - np.exp(-np.sqrt(gb / GDAG))) * r, 0))
        chi = lambda m: np.sum(((m - v) / e) ** 2)
        R = dict(name=name, Q=T.get(name, {}).get('Q', 9), n=n, rl=rl, Rd=T[name]['Rdisk'], RHI=T[name]['RHI'])
        R['B'] = (chi(Vb), 0); R['RAR'] = (chi(Vrar), 0)
        s = fit(lambda r, vf, rt: vf * arc(r, rt), [(vmx, rl * q) for q in (.05, .25, .8)], [1, .01], [1000, 5 * rl], r, v, e); R['CAV'] = (2 * s.cost, 2); R['CAV_rt'] = s.x[1] / rl; R['CAV_rtk'] = s.x[1]
        s = fit(lambda r, vf: vf * arc(r, D_STAR * rl), [(vmx,)], [1], [1000], r, v, e); R['CAVd'] = (2 * s.cost, 1)
        s = fit(lambda r, vc, rt: np.sqrt(Vb ** 2 + (vc * arc(r, rt)) ** 2), [(vmx, rl * q) for q in (.05, .25, .8)], [0, .01], [1000, 5 * rl], r, v, e); R['B+CAV'] = (2 * s.cost, 2); R['B+CAV_rt'] = s.x[1] / rl; R['B+CAV_rtk'] = s.x[1]
        s = fit(lambda r, vc: np.sqrt(Vb ** 2 + (vc * arc(r, D_STAR * rl)) ** 2), [(vmx,)], [0], [1000], r, v, e); R['B+CAVd'] = (2 * s.cost, 1)
        s = fit(lambda r, V, c: np.sqrt(Vb ** 2 + vnfw(r, V, c) ** 2), [(vmx * .8, c) for c in (5, 12, 30)], [5, 2], [1000, 60], r, v, e); R['B+NFW'] = (2 * s.cost, 2)
        s = fit(lambda r, V, rc: np.sqrt(Vb ** 2 + vpis(r, V, rc) ** 2), [(vmx, rl * q) for q in (.05, .25, .8)], [1, .01], [1000, 5 * rl], r, v, e); R['B+PIS'] = (2 * s.cost, 2)
        out.append(R)
    return out

MODELS = ['B', 'RAR', 'CAV', 'CAVd', 'B+CAV', 'B+CAVd', 'B+NFW', 'B+PIS']
for floor, label in ((0.05, 'error floor 5% of V_obs'), (0.0, 'raw SPARC errors')):
    res = run(floor)
    print('=' * 100); print('%s;  %d galaxies' % (label, len(res)))
    print('%-8s %4s %12s %12s %10s %10s' % ('model', 'k', 'median chi2/dof', 'mean chi2/dof', 'median BIC', 'BIC wins'))
    bic = {m: np.array([R[m][0] + R[m][1] * np.log(R['n']) for R in res]) for m in MODELS}
    allb = np.array([bic[m] for m in MODELS]); win = np.argmin(allb, axis=0)
    for j, m in enumerate(MODELS):
        k = res[0][m][1]; red = np.array([R[m][0] / max(R['n'] - k, 1) for R in res])
        print('%-8s %4d %12.2f %12.2f %10.1f %10d' % (m, k, np.median(red), red.mean(), np.median(bic[m]), np.sum(win == j)))
    sub = [i for i, R in enumerate(res) if R['Q'] <= 2]
    print('  restricted to Q = 1, 2 (%d galaxies): BIC wins' % len(sub), {m: int(np.sum(win[sub] == j)) for j, m in enumerate(MODELS)})
    for a_, b_ in (('B+CAV', 'B+NFW'), ('CAV', 'B+NFW'), ('B+CAVd', 'B+CAV'), ('CAVd', 'CAV')):
        d = bic[a_] - bic[b_]
        print('  BIC(%s) - BIC(%s): median %+.1f; %s better in %d of %d galaxies' % (a_, b_, np.median(d), a_, np.sum(d < 0), len(d)))
    for key, lab in (('CAV_rt', 'CAV'), ('B+CAV_rt', 'B+CAV')):
        x = np.array([R[key] for R in res]); lo, hi = np.percentile(x, [16, 84])
        print('  free r_t / r_last in %-6s median %.3f, 16-84%% [%.3f, %.3f]; d* = %.3f %s' % (lab, np.median(x), lo, hi, D_STAR, 'inside' if lo <= D_STAR <= hi else 'OUTSIDE'))
    # what does the fitted transition radius track?  (log-log Spearman and slope; r_t in kpc, interior fits only: 0.02 < r_t/r_last < 2)
    from scipy.stats import spearmanr
    for key, lab in (('CAV_rtk', 'CAV'), ('B+CAV_rtk', 'B+CAV')):
        ok = [R for R in res if 0.02 < R[key] / R['rl'] < 2 and R['Rd'] > 0 and R['RHI'] > 0]
        y = np.log10([R[key] for R in ok])
        for ref, nm in (('rl', 'last measured radius'), ('Rd', 'disk scale length'), ('RHI', 'HI radius')):
            x = np.log10([R[ref] for R in ok]); rho = spearmanr(x, y)[0]; b = np.polyfit(x, y, 1)[0]
            print('  %-6s fitted r_t (kpc) vs %-22s N=%d  Spearman %.2f  log-log slope %.2f' % (lab, nm, len(ok), rho, b))
