# 09 — Registered before running: the walk address, the prefix tree, and conjugate / non-conjugate pairs

Registered 2026-11-20, before any of `walk.py` or `conjugates.py` was run. Author's directions: (1) test the walk address and the prefix tree; (2) the three ADD/SCALE/SIGN operators of Ĥ_RB are the data worked with; (3) expect many symmetric, complementary and conjugate pairs, and non-conjugate pairs that give uncertainty. Letters: A = ADD (e1), S = SCALE (e2), G = SIGN (e4). Predictions are mine, stated as numbers so they can fail.

## W — the walk
- W1. The walk (the sequence of partial products, each ±e_k) determines the word uniquely: 100 % of distinct catalog words give distinct walks. Index steps alone already do it (the XOR of successive indices is the letter).
- W2. The walk lives on indices 0..7 only: 8 of the 16 sedenion indices, so the 16 (sign,index) addresses of test 5 were an octonion-subalgebra address, not a sedenion one. A sedenion address needs a fourth generator (index 8). Prediction: reachable indices = exactly {0,…,7}.
- W3. Prefix tree of the distinct words (ADD, SCALE, SIGN letters only): nodes ≤ 50 % of total letters (heavy sharing of prefixes).
- W4. The tree is not a binary-searchable tree at a single pillar: the first-letter split of the words has no pillar above 45 %.

## X — conjugate and non-conjugate pairs
- X1. (x, p): Gaussian saturates Robertson, Δx·Δp = ½ (ħ = 1) to 10⁻⁶.
- X2. (u = ln x, θ = xD generator in the log chart): a log-normal packet saturates Δu·Δθ = ½ (the Mellin pair; SCALE is conjugate to u).
- X3. (θ, p), the non-canonical SCALE–ADD pair, [θ, p] = i p (from G1): the Robertson bound ΔθΔp ≥ ½|⟨p⟩| holds with no violation for 200 random states, and is saturated by some squeezed states (ratio ≤ 1.01).
- X4. (P, p), SIGN against ADD: anticommute; for a parity-definite state ⟨p⟩ = 0 and P has no spread, so there is no product bound; for a mixed-parity state ⟨{P,p}⟩ = 0 holds.
- X5. (θ, P) commute: the two have a joint eigenbasis; test that the eigenfunctions x^s (even/odd) diagonalise both.
- X6. Catalog: of the distinct loop words containing both A and S, ≥ 90 % are order-sensitive (the reversed word is a different map of x → a·x + b), i.e. the non-commutativity [S,A] = A is present in nearly every escape-time loop, which is the affine non-conjugate pair.
- X7. Catalog names: a search of the Archimedes ids for Fourier / Laplace / Mellin / wavelet / uncertainty / Heisenberg finds ≥ 5 equations that name a conjugate pair.
