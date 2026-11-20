# Test 9 results — factorial rings (2026-11-20)

Registered in `16_registered_factorial_rings.md`; code `factorial_rings.py`; output `results_factorial_rings_2026-11-20.txt`. 7 of 8 passed as registered; Q4 failed on its own tolerance (see below).

| reading | what the rings are | result |
|---|---|---|
| A (area) | disc of area π·k!; ring k area π(k−1)(k−1)! | ring areas sum to π(n!−1) exactly; ring k holds (k−1)/k of everything inside it, so for n = 245 the outer ring holds 244/245 (99.6%). Ring widths grow as √k (w245/w244 = 15.65, √245 = 15.65): the onion is thicker outward, not thin-skinned. |
| R (radius) | disc of radius k! | outer ring holds 1 − 1/k² exactly (60024/60025). |
| D (dimension) | one complex plane per factor | V(2m) = π^m/m!, so each plane adds the factor π/m. Σ V(2m) = e^π (23.1407). The factor exceeds 1 only for m ≤ 3: the all-dimension maximum is d = 5 (V = 5.2638, 8π²/15), the even-dimension maximum d = 6. Past that the factorial wins and the ball shrinks. At the Cayley–Dickson dimensions 2, 4, 8, 16, 32 the unit-ball volume is 3.14, 4.93, 4.06, 0.235, 4.3e-6. |

Also: ln n! − Stirling = 1/(12n) − 1/(360n³) to 1e-13 at n = 245, so π enters n! through √(2πn). The shell identity S(d−1) = d·V(d) holds to 3e-16 for d = 1..16. The Archimedes `Factorial.factorial` reproduces `math.factorial` for 1..20 and drives the ratio test, which moves the integer factorials from class N to class B (they run and give the ball volume).

**Q4 failed as registered:** Monte Carlo at d = 8 was 1.86% off (tolerance 1%). A labelled second run with 5,000,000 points gave 0.30% (expected sd 0.35%). The tolerance was tighter than the sampling noise; the formula is not in doubt.

**ASS reading:** each factor is one SCALE (1/k) and the constant π; SIGN never enters (trivially). The crossover k = π is where SCALE (1/k) stops being outweighed by the circle (π).

Not shown: whether the π/k per plane maps onto the Cayley–Dickson doubling (the planes come in 2, 4, 8, 16 dimensions, not one at a time).
