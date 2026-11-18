"""A. The hat as geometry: inversion lemma and the halo test. Cold: numpy only."""
import numpy as np
rng = np.random.default_rng(0)
R = 1.0
# Lemma: r -> R^2/r is an involution, fixes r = R, swaps inside/outside
r = rng.uniform(0.2, 5.0, 100000)
inv = lambda x: R*R/x
print("involution max |inv(inv(r)) - r| =", np.abs(inv(inv(r)) - r).max())
print("fixed set |inv(R) - R| =", abs(inv(R) - R))
print("exterior -> interior:", bool(np.all(inv(r[r > R]) < R)))
# Jacobian (R/r)^6 in 3-D, checked by finite difference on the volume element r^2 dr
x, h = 1.7, 1e-6
vol = lambda a, b: (b**3 - a**3) / 3
ratio = vol(inv(x + h), inv(x)) / vol(x, x + h)
print("volume ratio %.6f  vs (R/r)^6 = %.6f" % (ratio, (R/x)**6))
# Halo test: uniform exterior density, inverted
n = 2_000_000
rr = (R**3 + rng.random(n) * (64 - 1)) ** (1/3)
bins = np.linspace(0.25, 1.0, 16); mid = (bins[1:] + bins[:-1]) / 2
hist, _ = np.histogram(inv(rr), bins)
dens = hist / (4*np.pi*mid**2*np.diff(bins))
print("inverted uniform density slope %.2f (isothermal halo needs -2)" %
      np.polyfit(np.log(mid), np.log(dens), 1)[0])
# What source density gives -2 after inversion?  rho'(r') = rho(r) (r/R)^6, r = R^2/r'
for p in (-4, -3, -2, 0):
    src = lambda q: q**p
    rp = mid; q = R*R/rp
    out = src(q) * (q/R)**6
    print("source r^%d -> image slope %.2f" % (p, np.polyfit(np.log(rp), np.log(out), 1)[0]))
