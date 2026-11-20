# EquationSpace: what Holcus answered, and the predictions read off it (registered 2026-11-19, BEFORE any test)

Source: `ask_holcus.py` (output in `holcus_answers_2026-11-19.txt`). Thresholds fixed here.

## What the maths answered
1. `bracketing_firing_order.bracketing_report` counts **groupings as set partitions** (Bell number: 15 at n = 4), not binary bracketings (Catalan: 5 at n = 4). Firing orders: n! (24, 5040). The two counts are different objects: a *grouping* says which operators are fired together; a *bracketing* says in what binary nesting. (Noted, not resolved: which one the author's "bracketing" means.)
2. `emerger.scale_partitions`: the 15 imaginary units partition into parts of size {1, 3, 7} in **10 shapes**; a contiguous group is classed C (1), H (3), O (7), or FRAGMENT (not closed).
3. `emerger.verify`: e₁+e₁₀ is a zero divisor on the ZD equator; e₁+e₂ is not; e₀ is a unit. 14 of 14 checks pass.

## Consequence for a basis-unit word (derived, not assumed)
The product of basis units is ±e_k, with k the XOR of the indices *whatever the bracketing*. So for a word of basis units the bracketing and the order move the **sign only**; zero divisors need sums (e₁+e₁₀), not words. The equation space of basis-unit words is a space of signs over a fixed index.

## Predictions
- **EQ1.** For three distinct imaginary units a, b, c of the sedenion, (ab)c and a(bc) have the same sign **iff** {a, b, c} is closed (c = a⊕b, classed H by the emerger's `domain_of`); otherwise the sign flips. Threshold: 0 exceptions over all 15·14·13 = 2,730 ordered triples (0 and 100 % are the only passing values; a failure stays recorded).
- **EQ2.** For a word of basis units of any length n ≤ 7, the number of distinct values over all Catalan(n−1) bracketings is **1 or 2** (indices fixed, sign only). Threshold: 0 words with 3 or more distinct values among 20,000 random words per n.
- **EQ3 (the grouping/bracketing question).** The count of distinct sign-patterns over all bracketings of an n-letter word is bounded by Catalan(n−1) and is below it for n ≥ 4 (many bracketings give the same sign). Threshold: the mean number of distinct sign patterns, not the number of bracketings, is reported per n; no pass/fail, measurement only.
