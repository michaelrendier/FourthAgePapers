"""B. L_(I|O) pipeline round trip on a KNOWN lens (no data): numpy only."""
import numpy as np
n = 256
k = np.fft.fftfreq(n)[:, None], np.fft.fftfreq(n)[None, :]
k1, k2 = k; k2sq = k1**2 + k2**2; k2sq[0, 0] = 1.0
y, x = np.mgrid[-n//2:n//2, -n//2:n//2]
kappa = 0.4*np.exp(-(x**2 + y**2)/(2*18.0**2)) + 0.25*np.exp(-((x-40)**2 + y**2)/(2*12.0**2))
kappa -= kappa.mean()                     # mass-sheet: constant is unobservable
kh = np.fft.fft2(kappa)
# forward: shear from convergence (Kaiser & Squires 1993)
g1 = np.fft.ifft2(kh*(k1**2 - k2**2)/k2sq).real
g2 = np.fft.ifft2(kh*(2*k1*k2)/k2sq).real
# inverse: convergence from shear
bh = (np.fft.fft2(g1)*(k1**2 - k2**2) + np.fft.fft2(g2)*2*k1*k2)/k2sq
bh[0, 0] = 0                              # the degenerate point: the mean is not measured
kb = np.fft.ifft2(bh).real
print("kappa round trip max error %.2e (periodic box, k=0 mode dropped)" % np.abs(kb - kappa).max())
# lensing potential and deflection: laplacian(psi) = 2 kappa
psi = np.fft.ifft2(-2*np.fft.fft2(kb)/((2*np.pi)**2*k2sq)).real
a1 = np.fft.ifft2(1j*2*np.pi*k1*np.fft.fft2(psi)).real
a2 = np.fft.ifft2(1j*2*np.pi*k2*np.fft.fft2(psi)).real
print("peak deflection (pixel units) %.4f ; psi range %.3f .. %.3f" % (np.hypot(a1, a2).max(), psi.min(), psi.max()))
# Fermat deficit L_(I|O) - L = -psi
print("deficit -psi: min %.3f max %.3f" % ((-psi).min(), (-psi).max()))
# noise: shape noise sigma_e/sqrt(n_gal) per pixel; error of recovered kappa
rng = np.random.default_rng(1)
for s in (0.01, 0.05, 0.2):
    e1 = g1 + rng.normal(0, s, g1.shape); e2 = g2 + rng.normal(0, s, g2.shape)
    bq = (np.fft.fft2(e1)*(k1**2-k2**2) + np.fft.fft2(e2)*2*k1*k2)/k2sq; bq[0, 0] = 0
    bk = np.fft.ifft2(bq).real
    print("shape noise %.2f: rms kappa error %.3f, peak/rms-noise %.1f" % (s, (bk - kappa).std(), kappa.max()/(bk - kappa).std()))
