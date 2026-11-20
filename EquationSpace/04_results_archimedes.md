# EquationSpace test 3: results (2026-11-19). Criterion: `03_registered_criterion.md`; code `archimedes_sample.py`; output `results_archimedes_sample_2026-11-19.txt`

Pool: 65 named functions in the Archimedes Maths modules, 6,739 Ultra Fractal formulas with a loop. Sample: 8 + 7, seed 20261119.

**Run 1 had a classifier bug and is kept** (`…_run1_classifier_bug.txt`): `#pixel` (the fractal's own parameter c, a variable) and `print`/`plt` (presentation) were counted as external input, giving 9 NOT FOUND. Run 2 counts only randomness and file/socket access as NOT FOUND. The registered criterion did not change; the implementation of it did, after seeing run 1.

| tier | n | which |
|---|---|---|
| EXACT | 5 | Lucas number, Lucas series, Fibonacci explicit (Binet) formula, z-score, Shuffle (a finite enumeration of permutations) |
| LIMIT | 8 | matrix row interchange, de Bruijn DFS, the Lorenz iteration, and five escape-time fractals (bailout comparisons) |
| NOT FOUND | 2 | two fractal formulas that call a random number |

| | prediction | result |
|---|---|---|
| EQ4 | classification identical for Ĥ_RB and both controls | **0 differences of 15: confirmed**, and by the nature of the rule: the primitives come from the *form* (power × rotation × derivative × sum), so any operator of that form passes the same equations. At this level "found in" **does not single out Ĥ_RB** |
| EQ5 | EXACT vs not splits on analytic vs branching/random | true **by construction** (the classifier tests exactly those tokens), so it is not an independent test; recorded as such |
| EQ6 | at least one named equation lands in a tier needing more than the form | see the table in the discussion: Navier–Stokes, Einstein and string actions need a field-space construction; F = ma and Schrödinger do not |

Reading: the three tiers line up with kinds of equation: closed forms and recurrences (EXACT), iteration with a threshold, i.e. every escape-time fractal (LIMIT: the bailout is the step), and stochastic rules (NOT FOUND). Nothing here derives any equation; it classifies what is expressible.
