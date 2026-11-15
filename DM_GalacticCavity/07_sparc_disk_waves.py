#!/usr/bin/env python3
"""Disk density waves (the mainstream galactic resonant cavity) against SPARC: what the data can and cannot show.

Written 2026-11-15. numpy + scipy; run cold:  python3 -I 07_sparc_disk_waves.py   (from this directory)

Established theory used: epicyclic frequency kappa^2 = 2 Omega^2 (1 + dlnV/dlnR), Omega = V/R; Lindblad resonances Omega_p = Omega -/+ kappa/2
(Lin & Shu 1964; Binney & Tremaine 2008, ch. 6); Toomre's critical wavelength lambda_crit = 4 pi^2 G Sigma / kappa^2 (Toomre 1964).
What SPARC holds: azimuthally averaged 3.6 um surface-brightness profiles (sfb_LTG, mag/arcsec^2, radius in arcsec, converted with the Table 1
distance; Sigma_L = 10^(-0.4 (mu - 24.812)) Lsun/pc^2, M_sun[3.6] = 3.24, Lelli et al. 2016) and rotation curves. It holds NO spiral phase (an azimuthal
average hides a spiral arm), NO stellar velocity dispersion, and NO pattern speed, so a spiral wave itself cannot be seen here; this script tests what can be:
  PART 1  the kinematics: kappa/Omega profiles, and the radial width of the region in which an m=2 wave can propagate (between the inner and outer
          Lindblad resonance) for a pattern speed set at corotation = 2.2 R_d (an assumption, stated);
  PART 2  Toomre's critical wavelength at r = 2 R_d from the stellar surface density (Y = 0.5): lambda_crit / R_d, the radial wavelength scale a stellar
          density wave should have;
  PART 3  whether the surface-brightness profiles show a common radial undulation with wavelength proportional to R_d: residuals about a smooth
          3rd-order polynomial in log Sigma(r), stacked over galaxies, null = shuffle which R_d goes with which galaxy (residuals kept intact).
"""
import glob, os
import numpy as np
from scipy.interpolate import UnivariateSpline

HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, 'data', 'SPARC'); GPC = 4.30091e-3     # pc (km/s)^2 / Msun
rng = np.random.default_rng(0)

def table1():
    t = {}; L = open(os.path.join(D, 'SPARC_Lelli2016c.mrt')).read().split('\n'); i = [k for k, l in enumerate(L) if l.startswith('-----')][-1]
    for l in L[i + 1:]:
        if l.strip(): w = l.split(); t[w[0]] = dict(D=float(w[2]), Rd=float(w[11]), Q=int(w[17]))
    return t
T = table1(); out = []
for f in sorted(glob.glob(os.path.join(D, 'Rotmod_LTG', '*_rotmod.dat'))):
    name = os.path.basename(f)[:-11]; sf = os.path.join(D, 'sfb_LTG', name + '.sfb')
    if not os.path.exists(sf): continue
    a = np.loadtxt(f); r, v = a[:, 0], a[:, 1]; Rd = T[name]['Rd']
    try: s = np.loadtxt(sf, skiprows=1)
    except Exception: continue
    s = s[s[:, 2] == 1]
    if len(s) < 8 or Rd <= 0 or len(r) < 8: continue
    rk = s[:, 0] * T[name]['D'] * 1e3 * 4.848137e-6            # arcsec -> kpc
    out.append(dict(name=name, r=r, v=v, Rd=Rd, rk=rk, mu=s[:, 1], err=s[:, 3], Q=T[name]['Q']))
print('galaxies with a rotation curve, a surface-brightness profile and R_d: %d of 175' % len(out))
print('unit check: median (last profile radius in kpc) / (last rotation-curve radius) = %.2f (about 1 if the radius unit is arcsec)' % np.median([g['rk'].max() / g['r'].max() for g in out]))

print('\nPART 1  kinematics')
wid, ilr_ok = [], 0
for g in out:
    sp = UnivariateSpline(np.log(g['r']), np.log(g['v']), s=len(g['r']) * 0.02, k=3)
    rr = np.linspace(g['r'].min(), g['r'].max(), 400); lv = sp(np.log(rr)); V = np.exp(lv); dl = sp.derivative()(np.log(rr))
    Om = V / rr; kap = np.sqrt(np.maximum(2 * Om ** 2 * (1 + dl), 1e-12)); g['kappa_over_Omega_median'] = np.median(kap / Om)
    rcr = 2.2 * g['Rd']
    if not (rr.min() < rcr < rr.max()): continue
    Op = np.interp(rcr, rr, Om)
    inner = rr[Om - kap / 2 > Op]; outer = rr[Om + kap / 2 > Op]           # ILR exists where Omega - kappa/2 crosses Op inside corotation
    rin = rr[np.argmin(np.abs(Om - kap / 2 - Op))] if np.any(Om - kap / 2 > Op) else np.nan; rout = rr[np.argmin(np.abs(Om + kap / 2 - Op))]
    wid.append((rin / g['Rd'], rout / g['Rd'], rcr / g['Rd']))
w = np.array(wid)
print('  kappa/Omega median over radius and galaxies: %.2f (1.41 = flat rotation curve, 2 = solid body)' % np.median([g['kappa_over_Omega_median'] for g in out]))
print('  corotation placed at 2.2 R_d: outer Lindblad resonance at %.1f R_d (16-84%% %.1f-%.1f); inner Lindblad resonance exists in %d of %d galaxies at median %.2f R_d' % (
    np.nanmedian(w[:, 1]), *np.nanpercentile(w[:, 1], [16, 84]), np.sum(np.isfinite(w[:, 0])), len(w), np.nanmedian(w[:, 0])))

print('\nPART 2  Toomre critical wavelength from the stellar surface density, at r = 2 R_d  (stars only, Y_d = 0.5; gas and dark matter ignored)')
lam = []
for g in out:
    sp = UnivariateSpline(np.log(g['r']), np.log(g['v']), s=len(g['r']) * 0.02, k=3); r0 = 2 * g['Rd']
    if not (g['rk'].min() < r0 < g['rk'].max() and g['r'].min() < r0 < g['r'].max()): continue
    Sig = 0.5 * 10 ** (-0.4 * (np.interp(r0, g['rk'], g['mu']) - 24.812))            # Msun/pc^2
    V = float(np.exp(sp(np.log(r0)))); dl = float(sp.derivative()(np.log(r0))); kap = np.sqrt(max(2 * (V / r0) ** 2 * (1 + dl), 1e-12)) / 1e3   # km/s/pc
    lam.append(4 * np.pi ** 2 * GPC * Sig / kap ** 2 / 1e3 / g['Rd'])                 # lambda_crit in kpc / R_d
lam = np.array(lam); print('  N = %d; lambda_crit / R_d: median %.2f, 16-84%% [%.2f, %.2f]  (lambda_crit in kpc: median %.2f)' % (len(lam), np.median(lam), *np.percentile(lam, [16, 84]), np.median(lam) * np.median([g['Rd'] for g in out])))

print('\nPART 3  radial undulations in the surface-brightness profiles')
qs = np.linspace(0.15, 1.5, 40)
def stat(Rref):
    S = np.zeros(len(qs)); cnt = np.zeros(len(qs))
    for g, Rg in zip(out, Rref):
        x = g['rk']; y = 2.5 * np.log10(np.maximum(10 ** (-0.4 * (g['mu'] - 24.812)), 1e-9)); keep = np.isfinite(y)
        x, y = x[keep], y[keep]
        if len(x) < 12: continue
        p = np.polyfit(x, y, 3); res = (y - np.polyval(p, x)); res = res / max(res.std(), 1e-6)
        for i, q in enumerate(qs):
            lamq = q * Rg
            if x.max() - x.min() < 1.5 * lamq: continue
            A = np.vstack([np.sin(2 * np.pi * x / lamq), np.cos(2 * np.pi * x / lamq)]).T
            c, *_ = np.linalg.lstsq(A, res, rcond=None); S[i] += np.sum((A @ c) ** 2) / len(x); cnt[i] += 1
    return S / np.maximum(cnt, 1), cnt
Rtrue = np.array([g['Rd'] for g in out]); obs, cnt = stat(Rtrue); prom = lambda S: S.max() - np.median(S)
null = np.array([prom(stat(rng.permutation(Rtrue))[0]) for _ in range(100)]); i = int(np.argmax(obs))
print('  galaxies contributing per q: min %d, max %d; stacked power peaks at q = %.2f (wavelength = %.2f R_d)' % (cnt.min(), cnt.max(), qs[i], qs[i]))
print('  peak prominence %.4f; shuffled-size null mean %.4f, 95th percentile %.4f; fraction of shuffles >= observed %.3f' % (prom(obs), null.mean(), np.percentile(null, 95), np.mean(null >= prom(obs))))
