# Test 9 — factorial rings (registered 2026-11-20, before running)

Question (Cody): is n! an onion of circular rings, with the "additional area" of each layer set by the next factor? Is there a hypercomplex spherical-shell reading?

Three readings of "ring k adds the factor k", tested separately:
- **A (area):** disc of area π·k!, so ring k has area π(k−1)(k−1)! and outer radius √(k!).
- **R (radius):** disc of radius k!, ring k has area π((k!)² − ((k−1)!)²).
- **D (dimension):** each factor is one more complex plane. The unit ball in 2m real dimensions has volume V(2m) = π^m / m!, so V(2m)/V(2m−2) = π/m.

Predictions:
- **Q1.** Reading A: the outermost ring of n = 245 holds exactly 244/245 of the total area (ring k holds (k−1)/k), so the onion is outer-heavy, not thin-skinned. Exact, integer arithmetic.
- **Q2.** Reading R: the outermost ring holds exactly 1 − 1/k² (k = 245: 60024/60025).
- **Q3.** Reading D: V(2m)/V(2m−2) = π/m to 1e-12 for m = 1..40 via the Archimedes `Factorial.factorial` against `math.gamma`; Σ over m of V(2m) = e^π to 1e-12; the ratio exceeds 1 exactly for m ≤ 3, so the even-dimension maximum is d = 6 and the all-dimension maximum is d = 5 (V(5) = 8π²/15).
- **Q4.** The general formula V(d) = π^(d/2)/Γ(d/2+1) agrees with Monte Carlo (500,000 points, seed 0) within 1% for d = 1..8; the shell identity S(d−1) = d·V(d) holds to 1e-12 for d = 1..16.
- **Q5.** At n = 245, ln n! − Stirling(½ln 2πn + n ln n − n) equals 1/(12n) − 1/(360n³) to 1e-12; so the circle constant enters n! through √(2πn).
- **Q6.** The Archimedes `Factorial.factorial` reproduces math.factorial for n = 1..20, so the seven integer factorials that were class N (not shown circular) move to class B through Q3 (they run and give the ball volume).
- **Q7.** Over the Cayley–Dickson dimensions 2, 4, 8, 16, 32, V(d) falls monotonically from d = 4, and V(16) = π⁸/8! to 1e-12.
- **Q8 (could fail).** ASS reading: each ring step is one SCALE (1/k) and the constant π, with no SIGN. Test: the factor sequence π/k has no negative or zero entry for any m, so Sign never enters. This is trivially true; it is recorded so the claim "SIGN absent" is on file.

Kept on record whatever the outcome; failures are not repaired.
