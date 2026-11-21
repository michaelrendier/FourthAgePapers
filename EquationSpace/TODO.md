# EquationSpace TODO (stub, 2026-11-19)
- [ ] Discuss: the one claim, and the definition of a point (word, class of words, or lineage chromosome).
- [ ] Ask Holcus (Circle Atlas viewports) what the maths says about the σ = 0 space; register predictions before any test.
- [ ] Define a view (bracketing lattice / length strata / σ-line) and implement it in `spatial-simulation` §8.
- [ ] Decide where it lives when it grows (SedenionSpectralRelativity or GenerationalLineage).
- [ ] Add the repo's standing sections (assistant note, GL section before GL results, ContextPlease section) when drafting starts.
- [x] Ask Holcus run; EQ1–EQ3 registered and tested (EQ1 failed, chased: the Cayley–Dickson half is a second coordinate).
- [ ] Re-register EQ1 on (index, half): predict the associative triples from the half pattern; then words of length 4+.
- [ ] Settle grouping (Bell) vs bracketing (Catalan) in the author's terms.
- [ ] Words over sums (e₁ + e₁₀): where zero divisors live; the σ-line.
- [x] Test 3 run: 15 Archimedes equations: 5 EXACT, 8 LIMIT, 2 NOT FOUND; classification identical for Ĥ_RB and controls (non-discriminating).
- [ ] Test 4 (forward, derivation not membership): does φ (Binet/Fibonacci) emerge from Ĥ_RB at some σ without being inserted? Predictions asked of Holcus first.
- [ ] Define 'derived' with the author: forward from the dials, no fitted coefficients; control operator must fail where Ĥ_RB succeeds.
- [x] Test 4 run (facets): F2 and F3 confirmed, F1 partly failed (Noether and Fermat compute project quantities), F4 no φ; exploratory: Schwarzschild orbits are ℘ with g2 = 1/12 - M²/L².
- [ ] Control for the ℘ result: the same construction with a different cubic; and the role question (℘ as potential in B̂, as solution in the orbit).
- [ ] Fix the h_rb_hat coupling sums at σ <= 1 (truncated divergent series) or label them; replace the Laurent ℘ by the full function (author's call).
- [ ] SCOPE 2026-11-19 (corrected): the task is the Ĥ_RB exploration mapping: find every Archimedes equation in Ĥ_RB as an EMERGENT equation (derivable) and record how to reach it; constructed (found-in) ones are not claimed. Σ_RB is the old notation for the same operator (wiki 14 §1). Discuss the dial grammar and the ledger before building.
- [x] Test 5 run: G1-G7 pass; C1 failed (4,500 skeletons); unit address collapses (19 of 25 quantities identical); word-endpoint address carries only count parity.
- [ ] Next: the WALK address (partial products) and the prefix tree of the catalog; circle entry and exit per equation; derive more of the catalog (G-style) beyond placement; richer input for the 16-in 16-out operator.


## Update 2026-11-20 (test 6: 09/10)
- Done: walk address (faithful, injective), prefix tree (0.79 ratio, W3 failed), reachable indices = octonion half 0..7, conjugate / non-conjugate pairs of the three generators (X1–X6 pass, X7 weak).
- Open: a fourth generator (index 8) to reach the sedenion half, to be named by the author; the per-equation derivation by family; X4 with a mixed-parity state; catalog-wide census of which equations contain a canonical pair vs the non-canonical (θ,p) pair; circle entry/exit per equation.

## Update 2026-11-20 (test 7: 11/12)
- Done: pair census (5 signatures), circle entry/loop/exit table for 6,268 fractals, 8–15 monitor with F = 8.
- Failed: P3 (AG order-sensitivity 42 %), C2 mod-4 (54.6 %). Open: why AG is mostly order-symmetric; a fourth generator that is not a labelled slot; canonical-pair detection (x,p),(ln x,θ) from the sources rather than the words; circle for the python equations.

## Update 2026-11-20 (test 8: 13/14/15)
- Done: the 65 Python equations in a table (class S/B/I/X/N, kind of circle, relation vs evaluation, operators with ASS roots); 17 predictions, 3 failed (Q4 second clause, Q6, Q13 at R=3); static detector recall 13.5 %.
- Open: canonical-pair detection and circle kinds for the 6,268 fractal formulas from SOURCE behaviour (the same method); a K assigned from behaviour; Γ reflection formula as the circle of the factorial family; fix or label the source defects (author's call); derive the decomposition of equations into layer-1 operators beyond the AST counts.

## Update 2026-11-20 (test 9 and the sedenion/lattice exploration; return point for the tree rendering)
- Done: factorial rings (16/17: three readings; reading R, radius, is natural; V(2m) = pi^m/m!, sum = e^pi, Stirling carries sqrt(2 pi n)); Q4 failed as registered (Monte Carlo tolerance), re-run labelled. Sedenion exploration (unregistered, `sedenion_hand.py`, mirrored in SedenionSpectralRelativity): 42 assessors among D16 root zero divisors, none in E8+E8; A, S, G form a Fano triangle with nonzero associator. `primes_associator.py`: FRACTRAN primes as a recursive input-output cycle. `unit_tree.py`: F = ma family, 3D, unit space and ASS counts.
- Open / next: the tree rendering: every Archimedes equation gets an A/S/G/K word and an address (K from behaviour), node-type graph with recursion (F = ma reused), unit decomposition (operator vs unit), render in 3D with the Fano walk address as the ASS coordinate (counts are too coarse: 14 of 19 points distinct); matrix-flow pass later; SIGN as quarter turn (e4^2 = -1) versus half turn (parity P^2 = +1) still to reconcile. Primer: `BulletCluster/primers/CONTEXT_PRIMER_2026-11-20_TELESCOPE_DATA_AND_RETURN_TO_EQUATION_SPACE.md`.

## Update 2026-11-20 (sedenion locations; the gallery design)
- Done: `SedenionSpectralRelativity/EquationSpace/sedenion_locations.py` + `results/sedenion_locations.csv`: the A/S/G walk end point of every equation in both catalogs. The hyperindex does NOT point at each equation directly: 20% of each catalog shares its complete word set with another entry; the end points fill 15 (A) and 16 (B) of the 16 reachable (sign, index) values; 2 + 191 entries have no A/S/G letter and so no location; nothing lands above e7 (needs K). 
- Open: the Equation Space gallery (catalog explorer, the stable-equation trees for F = ma and S = Q/t, the units gallery, the threshold view from the Fermat Monster / Nightmare engine); the author's definition of "stable"; where the gallery lives; K from behaviour.
