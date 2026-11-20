# 15 — Results of 13 (the 65 Archimedes Python equations: circle from source, from behaviour)

Run 2026-11-20 (`circles65.py`; output `results_circles65_2026-11-20.txt`; first run kept as `results_circles65_2026-11-20_run1.txt` and `catalog/py65_circles_run1.csv`). Full table: `14_table_65.md` and `catalog/py65_circles.csv`. Predictions: `13_registered_65_circles.md`.

## Two things changed between run 1 and the final run (both recorded)
1. The static detector's CYCLE feature fired on `boxplot_data` (it pops index 0 and index −1 of a sorted list; there is no append, so it is not a rotation). A false positive. Fixed: a rotation needs `pop(0)` and `append`.
2. `non_sympy_derivative`: the first D⁴ check (finite differences applied four times) had an error of 1.9×10⁻², which is noise amplification, not a defect of the claim. Replaced by the 2×2 matrix of D on {sin, cos} (projection), which gives [[0,−1],[1,0]] with D⁴ = 1 to 7×10⁻⁸.
Also removed my hand-assigned N for `quartiles`, `sample`, `boxplot_data` so that the rule "linked to a shown-circle function" decides (they call `median`, `dev`, `devsqr`); they became I.

## Counts
S 4 (+ 5 that run also shows) · B 31 · I 10 · X 6 · N 14. Static detector flags 9 of 65.

## Predictions graded
| # | prediction | result | verdict |
|---|---|---|---|
| Q1 | static flags ≤ 20 | 9 | PASS |
| Q2 | S+B+I+X ≥ 35, B ≥ 20 | 51; B = 31 | PASS |
| Q3 | static recall of shown circles ≤ 50 % | 5 of 37 = 13.5 % | PASS |
| Q4 | NMI(pillar class, kind) < 0.3 AND inside the 95th percentile of the shuffled null | NMI 0.293, null 95th pct 0.261, 0.6 % of null ≥ observed | first clause PASS, **second FAILED**: the words do carry weak information about the kind (N = 65, a few kinds) |
| Q5 | relation-type = the 5 thermodynamics functions; 4 are X, Boyle is B | exactly those 5; charles/gay-lussac/combined/ideal X; Boyle B | PASS |
| Q6 | N ≥ 25 | 14 | **FAILED** (more is shown than predicted) |
| Q7 | mean/median/midrange argmins of L2/L1/L∞ balls, 100 % | 500 of 500 each (+ range = 2 × L∞ radius, 200 of 200) | PASS |
| Q8 | Σz² = n and n − 1 to 1e-9 | 3.6e-15 and 7.1e-15 | PASS |
| Q9 | three `ero_replace` shears = rotation, 1e-12 | 1.2e-15 over 20 angles | PASS |
| Q10 | `second_order`: period 7, Cassini, regime by sign(p²+4q) | all hold (298 of 298 regimes) | PASS |
| Q11 | Lucas–Lehmer: 2cosh(2ᵏ arccosh 2), and the mod test | 4.3e-15; p = 3,5,7,11,13,17,19 classified correctly | PASS |
| Q12 | Lorenz ≥ 10 turns in 20,000 steps | 137.3 turns | PASS |
| Q13 | image of |z| = 3 under `stirling_poly_10` winds 9 times | **8.000** at R = 3; 9.000 at R = 10 | **FAILED** as registered: one zero of the polynomial lies at |z| = 5.12 (outside the circle); winding = number of zeros inside |z| = R |
| Q14 | inversion: |f(z)| = 1/|z|, involution | 1.8e-15 | PASS |
| Q15 | de Bruijn windows each once | 27 of 27 | PASS |
| Q16 | shifts have order n | n = 5 (columns) and 4 (rows) | PASS |
| Q17 | {A,S,G,K = e8} generate 32 elements | 32, indices 0..15 | PASS; K letters (from the static circle features) occur in only 6 of 65 functions, and those 6 end in 8–15 by construction |

## The 65, grouped by kind of circle
- **Round circle / angle:** `first_order` (p = e^{iφ}, q = 0: circle, period 7 for φ = 2π/7), `stirling_inversion_step` (inversion in the unit circle), `stirlingApprox` (π, the circle's area constant), `degRad`, `radDeg` (full turn 360° = 2π; the two are swapped and return None).
- **Winding / cone:** `stirling_poly_10` (winding number = zeros inside), Lorenz `step` (137 turns round the two lobes), `seed_from_basin` (plane lifted to the cone z = 2r; conics are the slices of a cone).
- **Cyclic group Zₙ:** `col_shift`, `row_shift`, `deBruijn` (Eulerian circuit of 27); `Shuffle` contains Z₄ ⊂ S₄ (X).
- **Hyperbola (the unit hyperbola, the Lorentz-plane circle):** `boyleslaw`, `second_order` (the recurrence conic: sign of p²+4q picks circle, line or hyperbola), `fibonacci_series`, `fibonacci_number`, `explicit_formula_fibonacci_number`, `lucas_number`, `lucas_series`, `lucas_lehmer_sequence`, `lucas_lehmer_number` (hyperbolic angle doubling; mod 2ᵖ − 1 a finite circle).
- **Sphere:** `zscore`, `zscores`, `samplevar`, `samplestandev`, `estsamplevar`, `estsamplestandev`, `devsqr` (z-scores on Σz² = n or n − 1), `dev` (hyperplane Σ = 0 through the centre); gas laws X (T ∝ ⟨v²⟩, radius² in velocity space).
- **p-norm ball:** `mean` (L2 round), `median` (L1 diamond), `midrange` (L∞ square), `range` (L∞ diameter). Three different shapes of "circle".
- **Rotation / reflection from the matrix operations:** `ero_replace` (three shears make a rotation, so the circle comes from ADD alone), `ero_interchange` (reflection, order 2).
- **Quarter-turn operator:** `non_sympy_derivative` (X: D on {sin, cos} is the quarter turn, D⁴ = 1; the function itself only does polynomials).
- **Not shown (N, 14):** `bills2100`, `all2100`, the seven integer factorials, `mersenne` (pure SCALE about the fixed point −1), `divide`, `ero_scaling`, `splitlist`, `mode`. Linked (I, 10): `iterate`… the pipeline functions that call a shown circle.

## What the circle kinds say about "what kind of circle"
In this set the circle is not one object. Round circles (first_order, inversion), hyperbolas (the Fibonacci family, Boyle, Lucas–Lehmer), spheres (variance), L¹/L²/L∞ balls (median, mean, midrange), cyclic groups, windings and a cone all occur, and the sign of a single discriminant (p² + 4q) sorts the recurrence family into circle, line and hyperbola. That is the kind of difference the "which kind of circle" question needs: the quadratic form, not just "circle". Relation-type functions (the gas laws) show their circle only by their arena (velocity-space sphere) or their conic (Boyle), not in their own code: this is the case you described, and it is measured here as 4 X of 5.

## Source versus words (the spore print against the mycelium)
Words alone (the pillar composition) and the circle kind share some information (NMI 0.293, null 0.261, p ≈ 0.006) but only weakly; the static detector sees 13.5 % of what running shows. So the classification by ASS-word and the classification by what the function does are different partitions, as the mushroom comparison predicted.

## Defects found in the source (recorded, not repaired)
- `charleslaw(V=2, k=4)` returns 8.0 for T; V/T = k gives T = 0.5.
- `idealgaslaw` raises TypeError for every float input (`1.0 * Decimal`); it can never run as written. Its `R is None` branch is unreachable (R is overwritten).
- `degRad` and `radDeg` have the conversions swapped and return None.
- `lucas_series` returns the Fibonacci numbers (starts 1, 1).
- `fibonacci_number(1)` and `(2)` return 0, not 1.
- `explicit_formula_fibonacci_number` agrees with the recurrence only up to n = 71.
- `non_sympy_derivative` prints and returns nothing.
- `boyleslaw` prints its locals on every call.

## Fourth generator K
Index 8 completes the XOR basis: {A, S, G, K} generate a group of exactly 32 elements ±e₀..±e₁₅ under the Cayley–Dickson walk. Assigning K to the static circle features gives K letters in only 6 of 65 functions, so the 8–15 half is monitored but nearly empty with this assignment. The behavioural circles that the static detector misses (31 of 37) are the ones a K assigned from behaviour would carry. Whether K should be the circle (rotation), the doubling (hyperbolic/Cayley–Dickson) or something else is for the author; the construction only shows that a fourth bit is needed to reach 8–15.
