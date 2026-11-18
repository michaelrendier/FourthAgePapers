"""D. QED vacuum birefringence ratio, and Faraday scaling: numpy only."""
import numpy as np
alpha = 1/137.035999; Bc = 4.414e9
for B in (1e-4, 1e4, 1e8):            # tesla: ISM-scale gauss, lab, pulsar-scale
    f = alpha/(45*np.pi)*(B/Bc)**2
    dpar, dperp = 3.5*f, 2*f            # the deviations n-1, kept as deviations (1+1e-40 rounds to 1)
    print("B=%.0e T: n_par-1=%.3e n_perp-1=%.3e ratio=%.6f" % (B, dpar, dperp, dpar/dperp))
# Faraday rotation: chi = RM lambda^2 ; two bands recover RM from angles (n-pi ambiguity)
rm = 150.0                              # rad/m^2, a Crab-order value for the test only
lam = np.array([0.09, 0.235])           # 3 GHz-ish and 1.3 GHz-ish wavelengths, metres
chi = (rm*lam**2) % np.pi
rm_back = (chi[1]-chi[0])/(lam[1]**2 - lam[0]**2)
print("RM in %.1f, two-band estimate %.1f (n-pi ambiguity: %.1f per step)" % (rm, rm_back, np.pi/(lam[1]**2-lam[0]**2)))
