# Negating Uncertainty

**Draft 0, 2026-11-17 (stub). Fourth Age Protocol paper: one claim, one engine, one set of notebooks.**

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5) with the project's `cs-paper-code-conventions` skill. The claim and the framework are the author's (Cody Michael Allison, pen name Michael Rendier). Every `:CALCULATED` number was printed by `uncertainty_engine.py` or `02_results.ipynb`, run on 2026-11-17.

## Notation and Disambiguation

| Label | Meaning here |
|---|---|
| `ESTABLISHED` | in the literature; cited, not derived here |
| `THEORETICAL` | the author's framework, stated and tested here only where marked |
| `INTERPRETATION` | a reading of an established object |
| `OPEN` | a named gap |
| `:CALCULATED` | suffix: this paper's own code produced the number |

Units ħ = m = ω = 1 unless stated. Post-hoc: the video below was noticed after the claim was formed; it is the starting point of this draft, not a source the claim was built against.

## Abstract

*(reserved)*

## 1. Claim

Δx·Δp ≥ ħ/2 is usually read as a limit on what can be known about a particle. The claim here is that it is the shape of one motion read two ways. Motion = 0 is a point; motion > 0 is a closed orbit in the (x, p) plane; position and momentum are the two projections of that orbit, the inside and the outside read at once. The apparent limit on knowing is the flattening of the orbit onto one axis at a time. Tested here: the quantum spreads equal the projections of the classical circle, at every angle for a state with no preferred angle, and the minimum circle has area h/2. Not claimed: a derivation of that minimum area from anything other than [x, p] = iħ (§7, `OPEN`).

## 2. The starting point (a video)

Veritasium, *I finally saw quantum physics with my own eyes... (It's spookier than I expected)* (YouTube `KfODG5REyss`, 65 min). At 59:19–61:14 the narration states that "the more precisely you know a particle's position, the less you know about its momentum", writes Δx·Δp ≥ ħ/2, and uses it as an estimate: an atom confined to a sphere of radius r has Δx = r, so Δp = ħ/r and E = p²/2m. Because helium is light this is large; it is called the zero-point energy and accounts for more than 98 % of the liquid's energy, so helium does not freeze at ordinary pressure by cooling alone. Earlier (37:00–41:00) the video separates bosons from fermions by spin and the symmetry of the combined wave function, and builds the Bose–Einstein condensate from de Broglie wavelength λ = h/p. Those passages are the bridge to the boson/fermion shapes of the author's work (§8). The transcript is held locally in `ContextPlease/claude/references/` and is not republished.

## 3. What is established

- **Robertson (1929):** for any state, σ_A σ_B ≥ ½|⟨[A, B]⟩|; with [x, p] = iħ, σₓσₚ ≥ ħ/2. `ESTABLISHED`
- **It is a Fourier statement:** the momentum wave function is the Fourier transform of the position one, and a function and its transform cannot both be narrow (Hardy 1933; Beurling). `ESTABLISHED`
- **Saturation:** Gaussians reach ħ/2. Oscillator eigenstates give (n + ½)ħ. `ESTABLISHED`
- **Phase-space picture:** the Fourier transform is a quarter turn of the (x, p) plane, rotation by θ is the fractional Fourier transform, and the oscillator's eigenfunctions are its eigenvectors with eigenvalues (−i)ⁿ (metaplectic representation). `ESTABLISHED`

## 4. The circle reading (`INTERPRETATION`)

An orbit of energy E = (n + ½)ħω in the oscillator is a circle of radius r = √(2E) with area πr² = (n + ½)h (Bohr–Sommerfeld with the half-quantum). Its position and momentum rms projections are each r/√2, so their product is r²/2 = (n + ½)ħ. This is the same number as σₓσₚ of the quantum eigenstate. The point (motion = 0) has no area and is not an eigenstate: the lowest orbit has area h/2.

## 5. The engine and the tests

`uncertainty_engine.py` (numpy only): Hermite states by recurrence, the momentum operator applied spectrally, quadrature operator O_θ = cos θ x + sin θ p applied to the state (so the angle dependence is measured, not assumed), the circle, the Fourier pair by direct sum, the helium estimate. Predictions P1–P7 with their thresholds were committed before the engine ran (`01_predictions.ipynb`).

**Listing 1** — the quadrature spread, cold (the one function the claim rests on)

```python
import numpy as np
from uncertainty_engine import grid, hermite_state, norm, quadrature_spread
x, dx = grid()
for n in (0, 1, 4):
    psi = norm(hermite_state(n, x), dx)
    s = [quadrature_spread(psi, x, dx, th) for th in np.linspace(0, np.pi, 37)]
    print(n, max(s) - min(s))
```

```
0 1.1e-16
1 2.6e-16
4 0.0
```

## 6. Results (`:CALCULATED`)

| # | Prediction | Result |
|---|---|---|
| P1 | σₓσₚ = (n + ½)ħ, n = 0…8 | **holds**, 9 digits |
| P2 | circle of energy (n + ½)ħω has area (n + ½)h and projection product equal to σₓσₚ | **holds**, 9 digits |
| P3 | no preferred angle for eigenstates | **holds**, 1e-16 |
| P4 | squeezed Gaussian follows the ellipse; conjugate product ≥ ħ/2 | first clause **holds** (6 digits); the second clause as committed ("equality at every θ") was **wrong**: the product is 0.500 at the axes, 0.566 and 0.625 at π/8 and π/4; equal to ħ/2 at every angle only for a circular state. Corrected in `02_results.ipynb`; committed text kept |
| P5 | motion = 0 costs unbounded motion, KE = ħ²/(8mσ²) | **holds**, exact (σ = 1 … 0.1) |
| P7 | FT of ψₙ is (−i)ⁿψₙ | **holds**, 7e-16 |
| P6 | video estimate for ⁴He within a factor 3 of the measured kinetic energy per atom | **fails**: 1.23 K against about 14 K (recalled, to be checked), a factor of 11; with a 3-D Gaussian σ = r/2, 3.7 K, a factor of 4 |

## 7. What is not shown (`OPEN`)

1. The circle picture **re-expresses** the relation: the area h/2 of the minimum circle is [x, p] = iħ in geometric dress. Negating the *need* for the relation requires a derivation of the minimum circle from something that does not contain it. None is given here.
2. The mixed and non-Gaussian states are not tested.
3. The helium measured value is recalled, not cited.
4. "Inside and outside at once" is used here for the two readings of one orbit; its identification with the Circle Atlas TO/FROM viewports is stated in the TODO, not tested.

## 8. Symmetries (stub)

To be written from the author's work: the boson/fermion adjacent shapes and the symmetries around them, tied to the transcript's 37:00–41:00 passage (exchange symmetry of the combined wave function: sum for bosons, difference for fermions, so two fermions cannot occupy one state) and to the quarter-turn structure of §3.

## 9. References

Heisenberg (1927), *Z. Phys.* 43, 172; Kennard (1927); Robertson (1929), *Phys. Rev.* 34, 163; Hardy (1933); Bohr–Sommerfeld quantisation; Namias (1980) and Almeida (1994) for the fractional Fourier transform; Veritasium (YouTube `KfODG5REyss`). Journal details recalled; to be checked.
