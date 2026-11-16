#!/usr/bin/env python3
"""Vertical motion of the Milky Way disk from Gaia DR3: how fast does the warp / vertical wave move?

Written 2026-11-16. numpy + astropy; run cold:  python3 -I 10_gaia_vertical_wave.py   (from this directory; needs data/Gaia/gaia_dr3_rvs_sample.csv,
re-fetch with data/Gaia/fetch_gaia.py, one public ESA TAP request)

The author's assumption: the halo is a standing wave of wavelength ~ half the galactic diameter travelling at c, with period lambda/c ~ 1e5 years.
Matter that rolls up and down the wave (the 'undulation of the galactic plane') would then have to follow a wave of that period.  Gaia measures the
vertical velocity V_z of ~10^5-10^6 disk stars directly, so the fastest vertical motion of the plane is measured, and the period it implies is a number.

Method (mainstream: Galactocentric transform by astropy defaults, i.e. Galactocentric frame of astropy 4.0: R_sun = 8.122 kpc, z_sun = 20.8 pc, solar motion
(12.9, 245.6, 7.78) km/s; Gaia DR3 astrometry and radial velocities, parallax_over_error > 10, RUWE < 1.4, rv error < 10 km/s).  Distance = 1/parallax.
  PART A  sample, selection, the volume covered.
  PART B  mean V_z and mean z in bins of Galactocentric R (6-12 kpc) and azimuth phi: the warp in position and in velocity.
  PART C  a warp that does not move would still produce V_z = Omega dz/dphi for stars on circular orbits in it. Fit z_w(R,phi) = A(R) sin(phi - phi0(R)) and
          compare the measured mean V_z with Omega(R) dz_w/dphi; the remainder is the vertical speed of the warp pattern itself, dz_w/dt.
  PART D  the period implied: an oscillation of amplitude A and period P has peak speed 2 pi A / P, so the observed |dz/dt| bounds P from below; compared with the
          lambda/c = 1e5 yr (Milky Way sized) of the wave and with the 'billion year' period of the original draft.
Caveats: the selection (bright stars with RVS velocities, parallax cut) is incomplete beyond ~3 kpc and shaped by extinction; the warp amplitude here is a
LOWER-quality number than a dedicated study; the sample is a random fraction of Gaia (random_index < 8e7).
"""
import os, warnings
import numpy as np
import astropy.units as u
from astropy.coordinates import SkyCoord, Galactocentric
warnings.filterwarnings('ignore')
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.join(HERE, 'data', 'Gaia', 'gaia_dr3_rvs_sample.csv')
KMS_PER_KPC_MYR = 1 / 977.792      # 1 km/s = 1.0227e-3 kpc/Myr
a = np.genfromtxt(F, delimiter=',', names=True)
print('PART A  %d stars; G median %.1f; parallax_over_error > 10; distance range (median, 95th pct) %.2f, %.2f kpc' % (
    len(a), np.nanmedian(a['phot_g_mean_mag']), np.median(1 / a['parallax']), np.percentile(1 / a['parallax'], 95)))
c = SkyCoord(ra=a['ra'] * u.deg, dec=a['dec'] * u.deg, distance=(1 / a['parallax']) * u.kpc, pm_ra_cosdec=a['pmra'] * u.mas / u.yr,
             pm_dec=a['pmdec'] * u.mas / u.yr, radial_velocity=a['radial_velocity'] * u.km / u.s)
g = c.transform_to(Galactocentric())
x, y, z = g.x.to_value(u.kpc), g.y.to_value(u.kpc), g.z.to_value(u.kpc)
vx, vy, vz = g.v_x.to_value(u.km / u.s), g.v_y.to_value(u.km / u.s), g.v_z.to_value(u.km / u.s)
R = np.hypot(x, y); phi = np.arctan2(y, x); vphi = -(x * vy - y * vx) / R          # Galactic rotation positive (astropy: Sun at x = -8.1, moving +y)
ok = (R > 6) & (R < 12) & (abs(z) < 1.5) & (abs(vz) < 100) & (abs(vphi) < 400)
print('  %d stars with 6 < R < 12 kpc, |z| < 1.5 kpc; median R %.2f kpc, median V_phi %.0f km/s, median V_z %.2f km/s, std V_z %.1f km/s' % (
    ok.sum(), np.median(R[ok]), np.median(vphi[ok]), np.median(vz[ok]), vz[ok].std()))
R, phi, z, vz, vphi = R[ok], phi[ok], z[ok], vz[ok], vphi[ok]

print('\nPART B  mean z and mean V_z in R x phi cells (cells with >= 300 stars; azimuth measured from the Sun-Galactic-centre line, Sun at phi = 180 deg)')
Rb = np.arange(6, 12.01, 1.0); pb = np.radians(np.arange(135, 226, 15))
print('  R bin (kpc)   N      mean z (pc)   mean V_z (km/s)   [by azimuth 135..225 deg: V_z]')
for i in range(len(Rb) - 1):
    m = (R >= Rb[i]) & (R < Rb[i + 1]); line = []
    for j in range(len(pb) - 1):
        mm = m & (phi % (2 * np.pi) >= pb[j]) & (phi % (2 * np.pi) < pb[j + 1]); line.append('%+5.1f' % vz[mm].mean() if mm.sum() >= 300 else '   - ')
    print('  %4.1f-%4.1f  %7d   %+8.1f       %+7.2f         %s' % (Rb[i], Rb[i + 1], m.sum(), 1000 * z[m].mean(), vz[m].mean(), ' '.join(line)))

print('\nPART C  warp pattern: dz_w/dt = V_z - Omega dz_w/dphi, with z_w = mean z per (R, phi) cell; Omega = V_phi/R measured in the same cell')
rows = []
for i in range(len(Rb) - 1):
    m = (R >= Rb[i]) & (R < Rb[i + 1]); Rm = R[m].mean(); ph = phi[m] % (2 * np.pi); ws = []
    for j in range(len(pb) - 1):
        mm = (ph >= pb[j]) & (ph < pb[j + 1])
        if mm.sum() >= 300: ws.append((ph[mm].mean(), z[m][mm].mean(), vz[m][mm].mean(), vphi[m][mm].mean() / Rm, mm.sum()))
    if len(ws) < 4: continue
    w = np.array(ws); dzdphi = np.polyfit(w[:, 0], w[:, 1], 1)[0]
    # Omega [km/s/kpc] * dz/dphi [kpc] = km/s
    om = np.mean(w[:, 3]); dzdt = np.mean(w[:, 2]) - om * dzdphi
    rows.append((Rm, dzdphi * 1000, np.mean(w[:, 2]), om * dzdphi, dzdt, np.ptp(w[:, 1]) * 1000))
print('  R (kpc)  dz/dphi (pc/rad)  mean V_z   Omega*dz/dphi   residual dz_w/dt (km/s)   z range across azimuth (pc)')
for r_ in rows: print('  %5.2f   %+12.0f      %+7.2f   %+11.2f      %+10.2f               %6.0f' % r_)

print('  (the 3 cells per ring that exist near the Sun cover only +-45 degrees of azimuth: dz/dphi is a local slope, not a whole-ring warp fit. Systematics not propagated:')
print('   the solar vertical velocity (7.78 km/s), z_sun (20.8 pc), the Gaia parallax zero point, and the selection function; I take 2 km/s as the systematic floor)')

print('\nPART D  period bound: an oscillation of amplitude A and period P has peak vertical speed 2 pi A / P; P >= 2 pi A / v_max')
vmax = max(abs(r_[4]) for r_ in rows) + 2.0          # largest residual plus the 2 km/s systematic floor
for A_kpc, lab in ((0.1, 'A = 0.1 kpc (the z range seen across azimuth above)'), (1.0, 'A = 1 kpc (an undulation of kiloparsec amplitude)')):
    P = 2 * np.pi * A_kpc / vmax * 977.792e6
    print('  %-52s v_max = %.1f km/s  ->  P >= %.2e years' % (lab, vmax, P))
lam_ly = 1e5; Pc = lam_ly                                # lambda / c in years
for A_kpc in (0.1, 1.0):
    v = 2 * np.pi * A_kpc / (Pc / 1e6) / 977.792 * 1e0   # kpc/Myr -> km/s : 1 kpc/Myr = 977.8 km/s
    print('  matter following a wave of period lambda/c = %.0e yr (lambda = 100,000 ly) with A = %.1f kpc would move vertically at %.2e km/s (%.2f of the speed of light)' % (
        Pc, A_kpc, 2 * np.pi * A_kpc / (Pc / 1e6) * 977.792, 2 * np.pi * A_kpc / (Pc / 1e6) * 977.792 / 299792.458))
print('  so the measured vertical motion of the plane is >= 3 orders of magnitude slower than a c-speed wave of galactic wavelength; the observed plane does not')
print('  oscillate with the wave. A period of ~1e9 years (the original draft) is consistent with the warp for kpc amplitude, and is not lambda/c.')
