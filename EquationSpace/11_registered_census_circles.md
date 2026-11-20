# 11 — Registered before running: the pair census, the circle entry/exit, and the 8–15 index half

Registered 2026-11-20 before `census.py` and `circles.py` were run. Author's directions: do the pair census, then the per-equation circle entry and exit, monitoring the index 8–15 half.

## Definitions (mine, stated so they can fail)
- **Words** are as in the catalog: A = ADD (e1), S = SCALE (e2), G = SIGN (e4); the two further letters of the catalog, F (unknown function slot) and R (random), are NOT among the pillars. Distinct words of length 1..400, as in `walk.py`.
- **Pair census.** For each word and each generator pair, the pair is *present* if both letters occur; it is *order-sensitive* if the subword restricted to those two letters, reversed, is a different affine map x → a·x + b (A: x+1, S: 2x, G: −x). The three pair types are AS (non-conjugate, [S,A] = A), AG (anticommuting, GAG = −A), SG (commuting). Canonical pairs (x,p), (ln x, θ) are NOT detectable from words; they are not in this census (stated, not hidden).
- **Circle.** The walk of a word (partial products, left to right, Cayley–Dickson product) is a path of ±e_k. Each generator is a quarter turn in its plane (g² = −1, g⁴ = +1), the way wiki 126 reads the circle (SIGN = quarter turn of the imaginary radius). A word *closes* if its endpoint is (+1, e0). The fractal formulas have an entry and an exit by construction: entry = the init section, loop = the iterated body, exit = the bailout section. For a loop with value g the *circle number* is the order of g under repetition: 1 if g = +e0, 2 if g = −e0, 4 if g = ±e_k, k ≠ 0.
- **The 8–15 half.** A, S, G reach only indices 0..7. To monitor 8..15 the unknown-function letter F is given index 8 (my choice; the CD doubling bit, the red/blue bit of the record) and R is ignored. Control: F = 15 (all ones).

## Predictions — pair census
- P1. AS is present in ≥ 70 % of distinct words; AG in ≥ 70 %; SG in ≥ 70 %.
- P2. SG is never order-sensitive (they commute exactly): 0 of all words.
- P3. Of the words with AS, ≥ 90 % are order-sensitive on the AS subword; of those with AG, ≥ 85 % on the AG subword.
- P4. Words containing all three pair types (all three letters): ≥ 60 % of the words.

## Predictions — circles
- C1. Fraction of distinct loop words that close (endpoint (+1,e0)): between 3 % and 12 % (16 addresses, if roughly uniform 6.25 %).
- C2. Every prefix that returns to index 0 has even length (parity: each letter an even number of times): 100 %. Of the returns to (+1,e0) specifically, ≥ 90 % are at lengths divisible by 4.
- C3. Entry/exit letters: ADD is ≤ 20 % of first letters of loop words and ≥ 35 % of last letters (loops end with the constant c).
- C4. Circle number 4 (index ≠ 0 after one pass): ≥ 75 % of distinct loop words (random expectation 87.5 %).
- C5. The bailout (exit) section contains a SIGN letter in 100 % of the formulas that have a bailout (known from C2 of test 5: every one).

## Predictions — 8..15
- H1. Of the distinct words containing F (F = 8), between 35 % and 65 % end in the upper half (index ≥ 8) (parity of the F count).
- H2. The set of words ending in the upper half is identical for F = 8 and F = 15 (membership is the parity of the F count): 100 %; the full address differs for some.
- H3. The upper half is entered in the first 5 letters in ≥ 50 % of words containing F (F is dense: 97,461 F letters in the loop words).
