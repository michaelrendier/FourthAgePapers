# 10 — Results of 09 (walk address, prefix tree, conjugate pairs)

Run 2026-11-20. Scripts `walk.py`, `conjugates.py`; outputs `results_walk_2026-11-20.txt`, `results_conjugates_2026-11-20.txt`. Predictions are in `09_registered_walk_conjugates.md`.

| # | prediction | result | verdict |
|---|---|---|---|
| W1 | walk determines the word | 3,461 words → 3,461 distinct walks; index-only walks also 3,461 | PASS |
| W2 | indices reachable = {0..7} | exactly 0..7 (8 of 16) | PASS, and it corrects test 5 (below) |
| W3 | prefix-tree nodes ≤ 50 % of letters | 181,292 nodes / 229,826 letters = 0.789 | **FAILED** (words share fewer prefixes than predicted) |
| W4 | no first-letter pillar above 45 % | SIGN 43.3 %, SCALE 41.6 %, ADD 15.1 % | PASS (marginal) |
| X1 | (x,p) Gaussian Δx·Δp = ½ | 0.499999 | PASS |
| X2 | (ln x, θ) lognormal = ½ | 0.500000 (k = 0 and 3) | PASS |
| X3 | (θ,p): Robertson bound holds, saturable | 200 states, 0 violations, min ratio 1.055; chirped-Gaussian family reaches 1.0034 | PASS |
| X4 | (P,p) anticommute | ⟨{P,p}⟩ = 0; the test state was even so ⟨p⟩ = 0 trivially: weak test | PASS (weak) |
| X5 | (θ,P) commute | ‖θPf − Pθf‖ = 6×10⁻¹³ | PASS |
| X6 | ≥ 90 % of A+S loop words order-sensitive | 2,274 of 2,393 (95.0 %) | PASS |
| X7 | ≥ 5 catalog ids naming a transform/conjugate pair | 7 ids, but "Duality", "Dualist", "Dualies", "…DualFractalRayTrace" are fractal names, not conjugate pairs; only `md-fourier-ea`, `MMFg-Transform`, `kpkcircletiletransform` are transforms | PASS as written, **not evidence** |

## What the numbers say
1. **The three pillars give an octonion address, not a sedenion one.** A, S, G are three XOR bits (1, 2, 4); every walk stays on indices 0..7 (the octonion subalgebra). The "16 addresses" of test 5 were 8 indices × 2 signs. To reach index 8 and above a fourth generator is needed. In the project's own record index bit 4 (value 8) is the red/blue (CD doubling) bit, so the pillar word space is the octonion half and the other half is reached by a doubling that A, S, G do not supply. This is a measurement of the construction, not a claim about Ĥ_RB.
2. **Walk = a faithful address.** 3,461 of 3,461 distinct. The tree is the faithful structure, but it is nearly as big as the word list (0.79), so the catalog is mostly branches, not trunk. The shared trunk is short: GGA (442 words), SAS (381), GGG, GGS (361 each).
3. **Conjugate and non-conjugate pairs fall out of the three generators.** Pairs, with the generator algebra from G1–G4:
   - (ln x, θ): canonical conjugate (Mellin), Δu·Δθ = ½ saturated by the lognormal packet.
   - (x, p): canonical conjugate (Fourier), ½ saturated by the Gaussian.
   - (θ, p) = (SCALE, ADD): not canonical. [θ,p] = i·p, so the bound ΔθΔp ≥ ½|⟨p⟩| depends on the state. Tested: holds for 200 states, saturated to 0.3 % by a chirped Gaussian. This is an uncertainty relation that the generator algebra forces and that is not Heisenberg's.
   - (SIGN, ADD): anticommute (P p P = −p). Discrete-continuous: no product bound; instead a selection rule (p maps even to odd parity).
   - (SIGN, SCALE): commute; joint eigenbasis (x^s, even/odd). Complementary in the symmetric sense, not uncertain.
   - In the catalog, 95 % of loops that use both ADD and SCALE are order-sensitive: the non-conjugate (θ,p) relation [S,A] = A is present in almost every escape-time loop, in its group form.
   So three kinds of pair appear (conjugate, non-conjugate with a state-dependent bound, anticommuting). That is a count of kinds, not yet a count of where they sit in the catalog beyond X6.
4. X4 should be redone with a mixed-parity state for ⟨p⟩ ≠ 0 (open).
