#!/usr/bin/env python3
"""Test the four predictions of 01_predictions.ipynb against the SPARC data in data/SPARC/.

Written 2026-11-14. The predictions are the ones in 01_predictions.ipynb (dated 2026-05-30 in the notebook):
  P1  r_t / R_virial = d*      = 0.246   (transition radius)
  P2  V_flat / V_max,bar = Ω_ZS = 0.56714 (flat velocity ceiling)
  P3  r_s / R_virial = d*      = 0.246   (NFW scale radius)         -> not testable from these tables, see below
  P4  Tully-Fisher exponent = 4          (baryonic mass ~ V_flat^4)

The notebook gives no operational definition of r_t, V_flat, V_max,bar or R_virial. The definitions below are
chosen here, before any result was computed, and are stated so that anyone can choose others and rerun:
  R_virial  = R200 from the SPARC halo-mass table (WP50_M200.mrt, NFW fit): R200 = (G M200 / (100 H0^2))^(1/3), H0 = 70
  V_flat    = Table 1 `Vflat` (Lelli et al. 2016), galaxies with Vflat > 0 (asymptotically flat curves)
  r_t       = first radius (linear interpolation) where V_obs reaches 0.90 V_flat; the 0.80 and 0.95 versions are printed too
  V_max,bar = max over r of the baryonic velocity, V_bar^2 = Vgas|Vgas| + 0.5 Vdisk^2 + 0.7 Vbul^2 (Lelli's 3.6 um values)
Needs numpy only. Run:  python3 -I 03_sparc_test.py   (from this directory)
"""
import glob, os, re
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'data', 'SPARC')
D_STAR, OMEGA = 0.24600, 0.56714
G, H0 = 4.30091e-6, 0.070            # kpc (km/s)^2 / Msun ; km/s/kpc


def rows(path, skip_until='-----'):
    L = open(path).read().split('\n')
    idx = [i for i, l in enumerate(L) if l.startswith('-----')]
    return L[idx[-1] + 1:]


table1, m200, btfr = {}, {}, {}
for l in rows(os.path.join(D, 'SPARC_Lelli2016c.mrt')):
    if l.strip():
        w = l.split(); table1[w[0]] = dict(Vflat=float(w[15]), Rdisk=float(w[11]), Reff=float(w[9]), Q=int(w[17]))
for l in rows(os.path.join(D, 'WP50_M200.mrt')):
    if l.strip():
        w = l.split(); m200[w[0]] = float(w[3])
for l in rows(os.path.join(D, 'BTFR_Lelli2019.mrt')):
    if l.strip():
        w = l.split(); btfr[w[0]] = (float(w[1]), float(w[2]), float(w[5]), float(w[6]))   # logMb, e, Vf, eVf

res = []
for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
    name = os.path.basename(f)[:-len('_rotmod.dat')]
    a = np.loadtxt(f)
    r, vo, vg, vd, vb = a[:, 0], a[:, 1], a[:, 3], a[:, 4], a[:, 5]
    vbar = np.sqrt(np.maximum(vg * np.abs(vg) + 0.5 * vd ** 2 + 0.7 * vb * np.abs(vb), 0))
    t = table1.get(name)
    if not t or t['Vflat'] <= 0 or name not in m200:
        continue
    vf = t['Vflat']
    def rt(frac):
        above = np.where(vo >= frac * vf)[0]
        if not len(above): return np.nan
        i = above[0]
        if i == 0: return r[0]
        return r[i - 1] + (frac * vf - vo[i - 1]) * (r[i] - r[i - 1]) / (vo[i] - vo[i - 1])
    R200 = (G * 10 ** m200[name] / (100 * H0 ** 2)) ** (1 / 3)
    res.append(dict(name=name, vf=vf, R200=R200, r80=rt(.8), r90=rt(.9), r95=rt(.95), vbmax=vbar.max(), rmax=r.max(), rdisk=t['Rdisk']))

n = len(res)
print('galaxies with a rotation curve, a flat Vflat and an NFW halo mass: %d (of 175)' % n)
def stat(x, label, target):
    x = np.asarray(x); x = x[np.isfinite(x)]
    lo, hi = np.percentile(x, [16, 84])
    print('%-44s median %.3f  16-84%% [%.3f, %.3f]  mean %.3f  N=%d   target %.3f  -> %s' % (
        label, np.median(x), lo, hi, x.mean(), len(x), target, 'target inside 16-84%' if lo <= target <= hi else 'target OUTSIDE 16-84%'))

print('\nP1  r_t / R200 (d* = %.3f)' % D_STAR)
for k, lab in (('r80', '0.80'), ('r90', '0.90'), ('r95', '0.95')):
    stat([g[k] / g['R200'] for g in res], 'r_t(V_obs = %s V_flat) / R200' % lab, D_STAR)
print('    for scale: median R200 = %.0f kpc, median r_t(0.90) = %.2f kpc, median disk scale length = %.2f kpc' % (
    np.median([g['R200'] for g in res]), np.nanmedian([g['r90'] for g in res]), np.median([g['rdisk'] for g in res])))
print('    r_t(0.90) / R_disk, the other reading of "natural unit" (engine: r_t = d* x r_max_bar):')
stat([g['r90'] / g['rdisk'] for g in res], 'r_t(0.90) / R_disk', D_STAR)
stat([g['r90'] / g['rmax'] for g in res], 'r_t(0.90) / (last measured radius)', D_STAR)

print('\nP2  V_flat / V_max,bar (Omega_ZS = %.5f)' % OMEGA)
stat([g['vf'] / g['vbmax'] for g in res], 'V_flat / V_max,bar', OMEGA)
print('    fraction of galaxies with V_flat < V_max,bar: %.2f   (the prediction needs V_flat below V_max,bar)' % np.mean([g['vf'] < g['vbmax'] for g in res]))

print('\nP4  baryonic Tully-Fisher slope (log Mb = slope x log Vf + c), BTFR_Lelli2019.mrt, Vf > 0')
x = np.array([np.log10(v[2]) for v in btfr.values() if v[2] > 0]); y = np.array([v[0] for v in btfr.values() if v[2] > 0])
p = np.polyfit(x, y, 1); resid = y - np.polyval(p, x)
se = np.sqrt(np.sum(resid ** 2) / (len(x) - 2) / np.sum((x - x.mean()) ** 2))
print('    N = %d, slope = %.3f +/- %.3f (unweighted least squares, y on x), intercept %.3f, scatter %.3f dex' % (len(x), p[0], se, p[1], resid.std()))
print('    prediction 4 -> deviation (4 - slope)/err = %.1f sigma' % ((4 - p[0]) / se))
print('    the fit regresses log M on log V; the inverse regression gives a steeper slope, so the number depends on that choice:')
q = np.polyfit(y, x, 1); print('    inverse regression slope (1/b) = %.3f' % (1 / q[0]))

print('\nP3  NFW scale radius: not testable here. The tables hold M200 only (WP50_M200.mrt, HMF_*.mrt); the fitted r_s sits in the')
print('    SPARC MassModels archive that was not copied into this repo. d* = 0.246 means concentration c = R200/r_s = %.2f;' % (1 / D_STAR))
print('    the notebook says "c ~ 5-30 ... this is within the expected range": 4.07 is below 5, so that sentence is wrong.')
