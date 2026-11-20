# EquationSpace: results (2026-11-19). Engine `equation_space.py`; raw output `results_engine_2026-11-19.txt`

Predictions are in `01_holcus_asks.md` (registered before the run). Labels `ESTABLISHED:CALCULATED`.

| | prediction | result | verdict |
|---|---|---|---|
| EQ1 | sign of (ab)c = sign of a(bc) **iff** {a,b,c} closed (c = a⊕b); 0 exceptions of 2,730 | closed ⇒ associative: **210 of 210**. Converse fails: **672** non-closed triples are also associative (882 associative in all). The emerger's H-class agrees with associativity on 2,058 of 2,730 (75 %) | **FAILED as an "iff"** (half holds) |
| EQ2 | 1 or 2 distinct values for every basis-unit word, n ≤ 7 | histograms at n = 3…7: only 1 or 2, worst = 2, 0 words with 3 or more (20,000 per n up to 6; 5,000 at 7) | **CONFIRMED** (by construction: indices are XORs, only the sign moves) |
| EQ3 | measurement: mean number of distinct sign patterns vs Catalan(n−1) | n = 3…7: 1.56, 1.84, 1.96, 1.99, 2.00 against 2, 5, 14, 42, 132; sign patterns seen at n = 7: 1,986 of 2^132 possible | measured |

## EQ1 chased to its source
All 672 exceptions have **one or two upper-half units** (index ≥ 8; 336 each). Counts of non-closed ordered triples by number of upper units, and how many are associative: 0 upper: 168 / 0; 1 upper: 1,008 / 336; 2 upper: 1,008 / 336; 3 upper: 336 / 0. With exactly one upper unit the associative triples have it in **position 0 or 2, never in the middle** (168 each). So associativity of a basis triple is not a property of closure alone: it also depends on **which Cayley–Dickson half each unit is in and where in the word it stands**. The doubling is a second coordinate beside the index (the XOR / PG(3,2) point). `INTERPRETATION`: a point of equation space carries (index, half) per slot, not the index alone.

## Corrections to the stub
The stub's sentence that zero divisors "are not found by sampling words at random" was vacuous: a word of basis units is always ±e_k, never zero. Zero divisors need sums (e₁ + e₁₀) and are outside the sign-space measured here. The 1.8–1.95 "distinct nonzero values" in the stub are the sign splitting of EQ2/EQ3, not a spread over many values.

## Not shown
No claim about the σ = 0 → σ > 0 selection, about 0_RB operators beyond the Cayley–Dickson units, or about words over sums (where zero divisors live).
