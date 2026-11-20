# 13 — Registered before running: how circular are the 65 Python equations, from source and from behaviour

Registered 2026-11-20, before `circles65.py` was run. Author's directions: show the 65 equations in a table; mark which can and cannot be shown circular; detect from the **source** (spore print vs mycelial growth: does reading how a function behaves reshape the classification the words gave?); distinguish relationships from discrete answers (ideal gas law); create a fourth generator if necessary; say what *kind* of circle.

## Evidence classes (each function gets exactly one)
- **S**: circular by source text alone: a static AST detector finds a circle signature (π or 2π, trig of an angle, complex rotation, `abs` of a complex, x²+y² / squared deviation, inversion z/|z|², modulus, cyclic pop/append).
- **B**: circular shown by RUNNING the function: a numerical test on the function's own outputs exhibits a circle, hyperbola, sphere, cyclic group or winding number.
- **I**: inherited: the function calls an S or B function of the same file.
- **X**: outside-source: the equation's textbook arena has a circle/sphere/p-norm ball; checked numerically, but the Archimedes function itself does not show it.
- **N**: cannot show.
Kind of circle recorded for S/B/I/X: round circle, winding, cyclic group Zₙ, hyperbola, sphere, p-norm ball, quarter-turn operator, angle measure, shear-composed rotation, reflection.
Also: **relation** (R: the function solves for any one of its variables, ≥ 3 `is None` branches) vs **evaluation** (E).
Layer-1 operators: for each function the primitive operators used (from the AST), each with its ASS root by the existing roll-down table.

## Predictions
- Q1. The static detector (S) flags ≤ 20 of 65.
- Q2. Running tests (B, after S) show a circle for ≥ 20 of 65 including inherited (S+B+I+X together ≥ 35).
- Q3. Static recall of the behaviourally shown circles is ≤ 50 %: the source alone misses most of what behaviour reveals.
- Q4. Normalised mutual information between the pillar-composition class (dominant letter of the ASS word) and the circle-kind label is < 0.3 and within the 95th percentile of a shuffled-label null: the ASS words alone do not recover the circle kinds.
- Q5. Relation-type functions are exactly the 5 thermodynamics functions (boyle, charles, gaylussac, combined, ideal); the ideal, combined, charles, gaylussac laws are X (kinetic-theory sphere T ∝ ⟨v²⟩) and Boyle is B (hyperbola pV = k).
- Q6. N (cannot show) ≥ 25 of 65.
- Q7. mean, median, midrange are the centres of the minimal L², L¹, L^∞ balls over the data: argmin matches the function for 100 % of 500 random data sets each.
- Q8. z-scores built with the file's own functions lie on a sphere: Σ z² = n (population sd) and n − 1 (estimated sd), error < 10⁻⁹, 100 random sets.
- Q9. Three `ero_replace` shears build a rotation: error < 10⁻¹² at 20 angles.
- Q10. `second_order` with p = 2cos(2π/7), q = −1 is periodic with period 7; with p = q = 1 (Fibonacci) the Cassini invariant F(n+1)F(n−1) − F(n)² = (−1)ⁿ holds; the sign of p² + 4q sorts the recurrences into circle (< 0), line (= 0), hyperbola (> 0).
- Q11. `lucas_lehmer_sequence`: s_k = 2cosh(2ᵏ·arccosh 2) within 10⁻⁹ relative for k ≤ 5 (hyperbolic angle doubling); the test s_{p−2} ≡ 0 (mod 2ᵖ − 1) classifies p = 3, 5, 7, 11, 13, 17, 19 correctly (11 composite).
- Q12. Lorenz: 20,000 steps of the file's own `step` wind a total of ≥ 10 turns around the two lobe centres.
- Q13. The image of the circle |z| = 3 under `stirling_poly_10` winds 9 times about the origin (degree 9).
- Q14. `stirling_inversion_step` (with p1 = 0) maps |z| to 1/|z| and is an involution on 1,000 points.
- Q15. `deBruijn(3,3,"012")`: read as a cycle of length 27, every 3-window occurs exactly once.
- Q16. `col_shift`/`row_shift` have order n (n shifts return the array, no smaller count does for a generic array).
- Q17. Fourth generator K (index 8, "ROT"): {A,S,G,K} generates a group of exactly 32 elements ±e₀..±e₁₅ under the Cayley–Dickson walk; with K assigned by the static circle detector, the fraction of S-class functions whose walk reaches 8–15 is 100 % by construction (mechanical, reported, not a finding).
