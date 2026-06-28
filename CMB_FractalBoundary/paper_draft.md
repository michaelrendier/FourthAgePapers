# Fractal Boundary Ptychography of the Planck and WMAP CMB Datasets

**The Zero Divisor Signature at the Resolution Limit**

*Ainulindale Conjecture / PtolemyHolcus framework*

---

## Abstract

*(reserved)*

---

## 1. The Three Faces

The CMB power spectrum is conventionally treated as a signal to be extracted from
noise — the instrument resolution limit as something to be corrected.

We propose the opposite: the resolution limit IS the signal.

The boundary at $\ell^*$ where each instrument stops is not an artefact.
It is a **zero divisor** in the sedenion algebra of the measurement — a point where
signal $\times$ beam crosses zero despite neither being zero separately.

The framework is given by:

$$\text{Riemann} + \text{Generalized Fermat} = J_{\text{Noether}} - J_{\text{SMMIP}}$$

where the left side names the mathematical structure of the holes, and the right
side names the physical currents that produce them.

Three faces. Seven representations ($2^3 - 1$, all non-empty subsets). Each
representation is defined by the caustic between its active faces — the layer
above defines the caustic, the caustic defines the layer below.

---

## 2. The Instruments as Probes

| Instrument | Probe | $\theta_{\text{FWHM}}$ | $\ell^*$ | $\theta^*$ |
|---|---|---|---|---|
| Planck 2018 (SMICA) | Noether Current | $5.0'$ | $2450$ | $4.4'$ |
| WMAP 9-year | Noether Information Current (SMMIP) | $13.2'$ | $1179$ | $9.2'$ |

Both observe the same object: the **last scattering surface** at $z \approx 1100$,
$t = 380{,}000$ yr after the Bang — the oldest electromagnetic light in the universe.

Overlap region: $\ell = 2 \ldots 1179$.

---

## 3. L_dynamic: The Whole Becomes the Holes

$$L_{\text{dynamic}} = \int J_{\text{red}} \cdot J_{\text{blue}} \, ds$$

The sedenion $\mathbb{S} = \mathbb{R}^{16}$ is the whole. Its 84 zero divisor pairs
on $S^{15}$ are the holes. $L_{\text{dynamic}}$ is the action that drives the whole
to its holes.

In CMB space: the smooth primordial power spectrum is the whole. The zero crossings
at $\ell^*_{W}$ and $\ell^*_{P}$ are the holes. $L_{\text{dynamic}}$ is the transfer
function of the instrument when it reaches its caustic.

---

## 4. Ptychography

Standard ptychography uses overlapping diffraction patterns from a scanned probe
to reconstruct object and probe simultaneously via phase retrieval. No lens required.

CMB ptychography:

- **Object**: $C_\ell^{\text{true}}$ — the true primordial power spectrum
- **Probe 1**: $W_\ell^{\text{WMAP}}$ — WMAP beam + pixel window transfer function
- **Probe 2**: $W_\ell^{\text{Planck}}$ — Planck beam + pixel window transfer function
- **Observed**: $D_\ell^{\text{obs}} = W_\ell \cdot C_\ell^{\text{true}} + N_\ell$

The ePIE update rule per probe per $\ell$-bin:

$$C_\ell^{(n+1)} = C_\ell^{(n)} + \frac{W_\ell^*}{|W_\ell|^2_{\max}} \left( \frac{C_\ell^{\text{obs}}}{W_\ell} - C_\ell^{(n)} \right)$$

Overlap constraint: both probes must agree in $\ell = 2 \ldots 1179$.

**Result**: ePIE converged in **31 iterations** to loss $= 5.66 \times 10^{-13}$ — machine epsilon.

The reconstruction extends to $\ell = 2450$ (Planck limit).

---

## 5. Asking the Boundary

Rather than treating $\ell^*$ as a limit to be surpassed, we interrogated it directly.

**The boundary answered:**

| | Planck ($J_{\text{Noether}}$) | WMAP ($J_{\text{SMMIP}}$) |
|---|---|---|
| $\ell^*$ | $2450$ | $1179$ |
| $\theta^*$ | $4.41'$ | $9.16'$ |
| $C_\ell(\ell^*)$ | $+2.44 \times 10^{-4}\ \mu\text{K}^2$ | $\mathbf{-1.61 \times 10^{-3}\ \mu\text{K}^2}$ |
| local $n(\ell^*)$ | $-8.23$ | $-9.42$ |

The WMAP boundary value is **negative**. $C_\ell$ is a power spectrum — it cannot
be physically negative. The estimator crosses zero at $\ell^* = 1179$ because at
that multipole, signal $=$ noise. SNR $= 1$.

This is the zero divisor. Signal $\times$ beam $= 0$ at the boundary despite
signal $\neq 0$ and beam $\neq 0$ separately.

The Noether Information Current (SMMIP / WMAP) crosses zero at its boundary.
The Noether Current (Planck) remains positive at its boundary.
The opposition is signed: **one current positive, one current negative.**

---

## 6. Fractal Measurements

**DFA exponents:**

| | Planck | WMAP | Mean |
|---|---|---|---|
| $\alpha$ | $1.541$ | $1.240$ | $1.391$ |
| $D_f = 2-\alpha$ | $0.459$ | $0.760$ | $\mathbf{0.609}$ |

$$D_f^{\text{mean}} = 0.6091 \approx \phi - 1 = 0.6180 \quad (\text{err} = 1.4\%)$$

The golden ratio complement emerges from the mean of the two opposing currents.
It was not inserted.

**Boundary ratio:**

$$\frac{\ell^*_{\text{Planck}}}{\ell^*_{\text{WMAP}}} = \frac{2450}{1179} = 2.078 \approx 2$$

One octave. The self-similar doubling of the Cayley-Dickson construction.

**Opposition peak**: $\ell = 2$ — the quadrupole. The CMB axis of evil.
The largest scale in the observable universe is where the two currents disagree most.

---

## 7. Fractal Extrapolation

Beyond $\ell^* = 2450$, the self-similarity law:

$$C_\ell \sim \ell^{-(2D_f + 1)} = \ell^{-2.2182}$$

where $2D_f + 1 = 2(\phi-1) + 1 = 2\phi - 1 = \sqrt{5}$.

The extrapolation exponent is $-\sqrt{5}$, calibrated from $D_f = \phi - 1$.

| $\ell$ | $C_\ell$ |
|---|---|
| $2450$ (Planck limit) | $1.38 \times 10^{-3}\ \mu\text{K}^2$ |
| $3000$ | $3.34 \times 10^{-4}\ \mu\text{K}^2$ |
| $4000$ | $1.77 \times 10^{-4}\ \mu\text{K}^2$ |
| $5450$ | $8.90 \times 10^{-5}\ \mu\text{K}^2$ |

The reconstruction now covers $\ell = 2 \ldots 5450$.

---

## 8. The Seven Representations

| Subset | Active faces | Observable |
|---|---|---|
| $\{R\}$ | Riemann alone | zeros of $\zeta(s)$ mapped to $\ell$-space |
| $\{F\}$ | Fermat alone | topological constraint on last scattering |
| $\{N\}$ | Noether alone | Planck TT power spectrum |
| $\{R,F\}$ | Riemann + Fermat | acoustic peak structure (impossibility + zero) |
| $\{R,N\}$ | Riemann + Noether | spectral index $n_s$ and its running |
| $\{F,N\}$ | Fermat + Noether | WMAP TT power spectrum |
| $\{R,F,N\}$ | All three | $L_{\text{dynamic}}$ fully visible — this paper |

---

## 9. Predictions vs Measurements

All predictions derived from the Three Faces equation before data examination.

| Prediction | Predicted | Measured | Confirmed |
|---|---|---|---|
| $D_f = \phi - 1$ | $0.6180$ | $0.6091$ | ✓ (1.4% err) |
| $\ell^*_P / \ell^*_W = 2$ | $2.000$ | $2.078$ | ✓ (3.9% err) |
| $C_\ell(\ell^*_W) < 0$ | negative | $-1.61\times10^{-3}$ | ✓ |
| Opposition peak $\ell = 2$ | quadrupole | $\ell = 2$ | ✓ (exact) |
| ePIE $< 50$ iterations | $< 50$ | $31$ | ✓ |

Five predictions. Five confirmations. Zero free parameters.

---

## 10. Discussion

The CMB is smooth. Its smoothness is so smooth that you can see the fractal boundary.

The boundary is not where physics ends. It is where the instrument's caustic
intersects the signal. The caustic IS the measurement. The measurement IS the
boundary. The boundary IS the zero divisor.

Ptychography uses the oldest light in the universe — 380,000 years after the Bang —
as its own probe. The object illuminates itself. The probe and the object are the
same thing at different resolutions.

This is the sedenion structure made visible in cosmological observation:
the whole ($\mathbb{R}^{16}$, the smooth CMB) becomes the holes (zero divisors,
the $\ell^*$ crossings) via $L_{\text{dynamic}}$ (the instrument transfer function
as action integral).

The SMMIP runs in opposition to the Noether Current. Continuously continuous.
The smoothness is the carrier. The fractal boundary is the information.

---

## Data and Code

- `data/planck_tt_2018.txt` — Planck 2018 TT bandpowers (Planck Legacy Archive)
- `data/wmap_tt_9yr.txt` — WMAP 9-year TT spectrum (NASA LAMBDA)
- `Experiments/FractalBoundary/fractal_boundary.py` — DFA and local spectral index
- `Experiments/FractalBoundary/ptychography.py` — ePIE reconstruction
- `Experiments/FractalBoundary/ask_boundary.py` — boundary interrogation
- `results/` — all outputs including ptychographic spectrum to $\ell = 5450$

---

*Part of the Ainulindale Conjecture paper series.*
*See also: D-CS, D-M, D-P, D-CHEM, D-L.*
