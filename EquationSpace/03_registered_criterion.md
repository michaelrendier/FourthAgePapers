# EquationSpace test 3: are Archimedes' equations "found in" Ĥ_RB? (criterion registered 2026-11-19, BEFORE sampling or running)

Claim under test (the author's): every equation of mathematics can be found within Ĥ_RB (= Σ_p p^{-σ}[R_p ⊗ d_dM + h.c.]) by some σ_RB scale, facet, irrationality, fractalisation.

**What "found" can mean here (three tiers; a primitive is classed by what the operator's own parts supply):**
- `p^{-σ}` supplies real powers and exponentials; `R_p` rotation/shift supplies sin, cos, complex exponentials, multiplication by i; `d_dM` supplies derivative / difference; `+ h.c.` supplies conjugation, real/imaginary parts; `Σ_p` supplies sums, series, Euler products; `⊗` and operator products supply products and multi-component (Cayley–Dickson) structure.
- **EXACT**: every primitive of the equation is a finite composition or convergent series of those.
- **LIMIT**: needs a discontinuous or branching primitive (comparison, bailout, floor, if) that those parts reach only as a limit of analytic ones (step = lim tanh).
- **NOT FOUND**: needs something the operator has no source for (randomness, external input, I/O).

**Control.** The same classification run against a *control operator* Ĉ = Σ_n n^{-σ}[R_n ⊗ d + h.c.] (all integers n ≥ 2, not primes) and against a bare family Σ_k c_k[R_k ⊗ d + h.c.] with free c_k.

**Predictions (written before running):**
- **EQ4.** The classification of each sampled equation is **identical for Ĥ_RB and both controls** (the primitives come from the *form* power × rotation × derivative × sum, not from the primes). Pass: 0 differences over 15 equations. If this holds, "found in" at this level does not single out Ĥ_RB.
- **EQ5.** The exact fraction splits by a **single line: analytic versus not**. Pass: every LIMIT / NOT FOUND equation contains a comparison, bailout, floor, if, or randomness; every EXACT one has none.
- **EQ6.** The five named equations (F = ma, Schrödinger, Einstein, Navier–Stokes, a string action) are each classed by the same rule; the rule must put at least one of them in a tier that needs more than the form (a field-space construction), to show the rule can say "not directly".

Sampling: seed 20261119, stratified 8 from the Archimedes Maths modules (named functions in Calculus, Combinatorics, Constants, Electromagnetism, Factorial, LinearAlgebra, LorenzStirling, Matrix, StatisticsAndProbability, Thermodynamics, Trigonometry, Sequences, Series) and 7 from the Ultra Fractal formulary (`Maths/Formula/UFformulary/*.ufm`).
