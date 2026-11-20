# EquationSpace test 5: results (2026-11-19). Predictions: `07_registered_grammar_catalog_address.md`

Scripts: `grammar.py`, `catalog.py`, `address.py`, `address_discrimination.py`, `word_address.py`. Outputs: `results_grammar_2026-11-19.txt` (and `…run1_complex_symbol…`), `results_catalog_2026-11-19.txt`, `catalog/*.csv`, `results_address_2026-11-19.txt`, `results_address_discrimination_2026-11-19.txt`, `results_word_address_2026-11-19.txt`. Vocabulary: **emergent** = derivable, **constructed** = found in. Task: the Ĥ_RB exploration mapping (Σ_RB is its old notation, Ainulindale wiki 14 §1).

## Foundation read first (context harvested)
- ASS (`add_scale_sign`, `VAPMIP/add_scale_sign.py`): Aff(1, ℝ) = ADD ⋊ (SCALE × SIGN), the one non-trivial bracket [SCALE, ADD] = ADD, a roll-down that places every named operation under one of the three (reflect, rotate, vector, boundary, balance, fulcrum, leverage, associator → SIGN; dilate, unit, fractal, gcd, spiral → SCALE; derivative-like flow, pathway, orbit-trap → ADD).
- Ĥ_RB (wiki 14, 22, 123): R̂ = xp (Red), B̂ = ½p² + ℘ (Blue), ∂̂ the boundary (Green); σ_ζ the facet pointer; **wiki 22 had withdrawn its "DERIVED" claims for φ, π, e** (they enter as inputs or termwise identities); wiki 14 §4 calls the σ-facet table "correspondences, not solutions".
- Circle catalogue (wiki 126): in u = ln r the diameter and circumference are shifts (ADD), the area a slope of 2 (SCALE), an imaginary radius a quarter turn u → u + iπ/2 (SIGN): the three generators already act on circles this way.
- GL unit lattice (`units.py`): N = kg·m·s⁻² is a node with J, W, V, Wb, T below it: F = ma is the root of that tree.

## Part G: the grammar, 7 of 7 emergent derivations pass (exact, symbolic)
| | derivation | result |
|---|---|---|
| G1 | θ = xD satisfies [θ, D] = −D and θ = i(x p), p = −iD | **the SCALE generator is exactly Berry–Keating's xp (the Red term R̂)**; the floor's bracket is the Lie algebra of {D, θ} |
| G2 | P D P = −D, [P, θ] = 0 | SIGN reverses ADD, commutes with SCALE |
| G3 | eigen-equations of the generators | D f = λf → C e^{λx}; θ f = s f → C x^s (run 1 left s complex and sympy split the result: harness issue, kept) |
| G4 | flows | exp(hD) f = f(x+h) and exp(tθ) f = f(eᵗx), residual 0 |
| G5 | **entropy**: f(xy) = f(x) + f(y) differentiable forces x f′ = const, f = k ln x | S = k ln W is the form forced by multiplicative counts: SCALE ≅ ADD in the log chart |
| G6 | **inertia / F = ma**: over (kg, m, s) the variables F, m, x, t have rank 3, nullity 1, group F t²/(m x) | F = k m x/t², with a = D²x: F = k m a: the form of Newton's second law is forced by SCALE-covariance up to the dimensionless k |
| G7 | **℘ is ASS-closed**: ODE and first integral map to themselves under SCALE with weights (4, 6), even under SIGN, periodic under an ADD lattice; Laurent coefficients g₂/20, g₃/28, g₂²/1200 follow | the Blue term's function is the function fixed by all three generators |

Reading (`INTERPRETATION`, supported by G1 and G7): Ĥ_RB's three terms line up with the three pillars: R̂ = the SCALE generator, ∂̂ = the ADD generator, ℘ (in B̂) = the object closed under all three. G1–G7 are textbook mathematics; none is new to the literature.

## Part C: the catalog (constructed placement)
65 named formula functions and **6,268** fractal formulas that have a loop section (the 6,739 of the earlier pool also counted formulas with no loop section), each reduced to its ASS-word in source order. Files `catalog/archimedes_py.csv`, `catalog/archimedes_ufm.csv`.
- **C1 FAILED.** Predicted ≤ 2,500 distinct loop skeletons; found **4,500** (4,381 distinct loop words), a duplication of only ×1.4. Most common: `FFFSA|GGG` (160 formulas: a user-function slot, a scale, an add, three bailout bits), the empty word (142), `SA|GG` (44: z → z^n + c with a bailout test).
- **C2 passed.** Of 5,922 escape-time formulas, 5,795 (97.9 %) have a SIGN primitive and an ADD in the loop; 100 % have a SIGN primitive in the bailout.
- **C3 (alignment with the permutation space).** Occupied words / possible 3ⁿ: n = 1: 3/3; 2: 6/9; 3: 20/27; 4: 49/81; 5: 72/243; 6: 95/729; 7: 128/2,187; 8: 153/6,561 (2.3 %). The firing-order points at n = 8 are 3⁸·Catalan(7) = 2,814,669. Root totals over all words: ADD 482,559, SCALE 563,448, SIGN 544,143 (roughly one third each; unknown function slots 97,636, random 3,076).

## Part A: the sedenion address
Registered encoding: unit exponents (kg, m, s, A, K, mol, cd) on e₁…e₇. The 16-in 16-out operator is the Emerger's σ_RB (ψ[k]·conj ψ[k⊕4]).
- **A1 passed (trivially by the structure).** All 13 mechanical quantities have tilt = axis = 0; entropy J/K and molar entropy are the first quantities with a non-zero tilt (kg paired with K across the XOR-4 partner; any of K, mol or cd added to F = ma switches the tilt from 0 to 4).
- **A2 control: no specialness.** Over all 5,040 assignments the mechanical quantities are all tilt-null in 57.1 %; the registered assignment's count of non-zero-tilt quantities (2) sits at the 22.9th percentile of 5,040, not extreme.
- **A3 passed.** The F = ma address (kg, m, s ↔ e₁, e₂, e₃) is not a zero divisor, closes as a quaternion triple (domain H), σ = ½ with T1 holding, gain class unit (the "NOW"), canonical lineage {1:15} → {2:14} → {8:8} → {4:4:4:4} → {4:8:4}, precession step 6 of 12, entry bracket 1. One iterator step (exponent ± 1) of kg, m, s keeps the tilt at 0; a step of A changes the domain to FRAGMENT; a step of K, mol or cd gives tilt 4.
- **A4 (weak).** Entropy (G5) and inertia (G6) each use two generators (SCALE ≅ ADD; SCALE-covariance with D²), ℘ (G7) uses all three: they come before ℘ in generator count. The order is my own, so this confirms little.
- **Discrimination: the address collapses.** Of 25 named quantities the 16-out result takes **4 distinct values**; 19 quantities (mass, length, time, velocity, acceleration, momentum, force, energy, power, action, pressure, frequency, G, charge, voltage, resistance, capacitance, ε₀, μ₀) share one. For random exponent vectors in [−3, 3]⁷, 1,255 of 2,000 differ. So with this input encoding the 16-out result says which XOR-4 pairs of dimensions are coupled; it does not identify an equation. F = ma, energy and momentum are indistinguishable.

## Exploratory (post-hoc, not registered): a word as a walk through the sedenion
A word over the generators (ADD = e₁, SCALE = e₂, SIGN = e₄, multiplied left to right) has the value ±e_k: k is the XOR of the generator indices (the parity of the counts), the sign is set by the order. Over 3,461 distinct catalog words: all 16 (sign, index) addresses occupied, distribution essentially the same as after shuffling each word's letters; 50.5 % of words change address when their order is shuffled; the index never does. **No structure beyond the parity of the counts.** F = ma (D, D, then m) → −e₂; entropy (count, then log) → +e₃; boost (a scale) → +e₂. The end point is a 16-bucket summary; it cannot be the full address of an equation.

## Answers to the questions put
- **Can the equations be reached from Ĥ_RB, and how?** Reached with a witness (emergent): G1–G7. The recipe is: take the three generators (ADD = D, SCALE = θ = xD, SIGN = P), require covariance, additivity, closure or an eigen-condition, and read the equation off. Everything else in the Archimedes inventory is placed (constructed) but not derived.
- **The interface operator.** Not found. With the Emerger's σ_RB as the 16-in 16-out map, the output depends only on which dimension pairs are coupled, so it cannot carry an equation. A faithful address must keep the *walk* (the partial products), not only the end point: the walk determines the word uniquely, since multiplication by a basis unit is invertible.
- **Equations "laying around" not in the established literature.** None. Everything derived is textbook; the only readings that go beyond are the INTERPRETATION lines (the three terms of Ĥ_RB against the three generators).
- **Not done:** the exhaustive derivation of the 6,268 + 65 equations (only the placement); the circle entry and exit of each equation; the walk-address and the prefix tree.
