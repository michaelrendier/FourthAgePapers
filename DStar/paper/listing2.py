# Listing 2 — one crossing under three ceilings (stand-alone; constants are CODATA 2018 / SI)
import math
A_PI = 0.5671432904097838                           # from Listing 1
hbar, c, G, kB = 1.054571817e-34, 299792458.0, 6.67430e-11, 1.380649e-23
ceilings = {
    "Hagedorn (entropy side)":       7.78e16,                                   # K, RiemannHypothesisProof/docs
    "Planck temperature":            math.sqrt(hbar * c**5 / G) / kB,           # K
    "speed of causality (inertia)":  c,                                         # m/s
}
for name, ceil in ceilings.items():
    star = A_PI * ceil                              # crossing: T*/T_ceil = exp(−T*/T_ceil)  or  g·exp(g/g0) = g0, g0 = c
    print(f"{name:30s} ceiling {ceil:.6e}  crossing {star:.6e}  digits below ceiling {-math.log10(star / ceil):.13f}")
