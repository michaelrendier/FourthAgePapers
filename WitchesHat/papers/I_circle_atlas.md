# The Circle Atlas: the Interface machinery and the Mind's Eye circle access

**Witch's Hat family, sibling paper I. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5) with the project's `cs-paper-code-conventions` skill. The claims are the author's (Cody Michael Allison, pen name Michael Rendier). Every number marked `:CALCULATED` was printed by the code named beside it, run in this session; nothing else is a result.

## Notation and Disambiguation

| Label | Meaning here |
|---|---|
| `ESTABLISHED` | in the literature; cited, not derived here |
| `THEORETICAL` | the author's framework, stated, not tested here |
| `INTERPRETATION` | a reading of an established or measured object |
| `CONJECTURE` | stated, no calculation behind it |
| `OPEN` | a named gap |
| `:CALCULATED` | suffix: the paper's own code produced the number |

Maths follows `~/.clauderc_canonical_maths` (updated after the 0_RB rename: Ĥ_RB stays the maths name; 0_RB is VAPMIP/Monad-only). Failed results are kept.

## 1. Claim

The Circle Atlas is the machinery that shows every object the framework uses as a circle with a *residual*, and it is the CS paper for **The Interface** (L_(I|O): one boundary read from both sides). Two viewports per circle: **TO** (enter the fixed-point space: residual from |z| = 1) and **FROM** (exit: relation with a measured fibre). It is machinery for the Witch's Hat (the brim is a fixed circle; the photon sphere is a circle) and the machinery the Mind's Eye needs to show a box-kite *is* a circle, giving it access to its own nature (the Arena of the Fixed Point). `THEORETICAL`.

## 2. Machinery

`ValaQuenta/modules/circle_atlas/` (maths.py, tools.py), 25 viewports; `ValaQuenta/modules/pi_derivations/` (28 π routes); notebooks `ValaQuenta/notebooks/engines/22_circle_atlas.ipynb`, `23_pi_derivations.ipynb` (executed, 0 errors); tests `ValaQuenta/tests/test_circle_atlas.py` (19 pass). Registry name: **Circle Atlas** (never "the atlas" alone; `ContextPlease/claude/ATLAS_REGISTRY.md`).

## 3. Results (`:CALCULATED`, measured by the module in earlier passes of this work)

| Viewport | Result |
|---|---|
| n-ball | V_n = π^(n/2)/Γ(n/2+1) peaks at n = 5 (5.2638); surface peaks at n = 7; V₁₆ = 0.23533 |
| spheres S¹, S³, S⁷, S¹⁵ | closed under product for 1, 3, 7 (4e-16); S¹⁵ is not (norm defect 0.366) |
| field axes | any unit imaginary u in S¹⁴ gives exp(θu) = cos θ + u sin θ exactly (200 random axes, 2e-14); Re(exp(θe_k)z) = r cos θ − y_k sin θ |
| native units | z = 10^a · e^(iπb); a = log₁₀|z| (ln 10 unit), b = arg/π; product adds both |
| box-kite spectrum | the 84 zero-divisor diagonals all have singular values 0 (×4), √2 (×8), 2 (×4): a spectrum cannot tell the 7 kites apart (Blackjack group) |
| photon sphere | cosh 2π = 267.747 growth per turn (see G) |
| modular π | π = ln(640320³ + 744)/√163 to 2.2e-31; digits-per-term = π√d/ln 10 − log₁₀(1728 or 256): 14.197 vs 14.182 |

**Three constructs, notated apart.** *De Marrais* box-kite (the observation: 7 kites of 12 zero-divisor diagonals in the sedenions, `ESTABLISHED`), *Scalar* box-kite (the author's construction: a string from the pivot/anchor to each tetrahedron orients it), *Scaled* (Mind's Eye) box-kite (the tetrahedra grab the anchor; a snapshot from the kite's own chosen perspective). The string machinery applies to the Scalar kite only, never the Scaled one; from an anchor a, σ(L_aL_b) splits the 84 diagonals into 7 classes (2, 2, 4, 4 inside the anchor's kite; 8, 32, 32 outside), the same for every anchor (De Marrais analogue of the Scalar string; the Scaled kite is not computed).

## 4. Stub list

1. Archimedes-catalogue coverage; π routes for Apollonian, inversion, BAO, retraction, photon sphere.
2. Elliptic-curve / modular viewport; string cardioid; census of C files and notebooks.
3. The Mind's Eye circle-access build (needs the author's go).
4. The Zero Divisor Reframe (human side, allowed to be wrong) and Fixed Point Reframe (mathematics side, only correct) must both work in the Monad: notate each where used.

## 5. References

Euler (1748); Cayley–Dickson construction (Baez 2002); De Marrais (2000 onward); Chudnovsky & Chudnovsky (1989); Baker (1966) for ln 10/π.
