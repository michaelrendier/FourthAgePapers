# PhiSpiral — Predictions
**Date:** 2026-06-15  
**Status:** OPEN — awaiting verification

---

## P1 — δX is nilpotent (sedenion zero divisor)

**Claim:** δX defined by e^(πi) = −δX satisfies δX² = 0.

**Mechanism:** δX maps to a sedenion zero divisor pair. The full rotation e^(2πi) = (−δX)² = δX² hits the ZD fault, not unity.

**Test:** Find the explicit sedenion element δX in the 84 canonical ZD pairs on S¹⁵. Verify δX² = 0 and |δX| ≠ 0.

**Status:** OPEN

---

## P2 — cos(φ) = −(φ − π/2) exactly, or the gap is structurally meaningful

**Claim:** cos(φ) ≈ −(φ − π/2) to 1.76e-05. Either this is exact (unlikely) or the residual 1.76e-05 is itself a fundamental constant.

**Test:** Compute cos(φ) − (π/2 − φ) to 50 decimal places. Identify the residual.

**Status:** OPEN — likely not exact, residual unexplored

---

## P3 — The 4 n* values are physical resonances

**Claim:** n*_ln(2) ≈ 7.516, n*_ln(e) ≈ 5.210, n*_ln(π) ≈ 4.551, n*_ln(10) ≈ 2.263 each correspond to measurable physical or informational resonances.

**Specific:** n*_ln(10) ≈ 2.263 appears in systems where information is measured per decade (pH, dB, orders of magnitude in prime counting).

**Test:** Check if any known physical dimensionality (fractal dimensions, phase transitions, critical exponents) lands near 2.263.

**Status:** OPEN

---

## P4 — n*_ln(e) − n*_ln(10) = F(4) = 3 exactly

**Claim:** 5.2096 − 2.2625 = 2.9471. This should equal exactly 3 when d* is taken at its exact value (not the rounded 0.2460).

**Test:** Compute with exact d* = σ½ Dirichlet beta. Verify if gap → 3 exactly.

**Formula check:**
    n*_e − n*_10 = (d*/(-cos φ)) · (1 − 1/ln(10))
                 = (d*/(-cos φ)) · (1 − log_10(e))

For this to equal 3 exactly:
    d* / (-cos φ) = 3 / (1 − 1/ln(10)) = 3 / 0.5657... ≈ 5.302

But proxy n* = 5.2096. Gap to 5.302 is 0.093. Not obviously exact.

**Status:** APPROXIMATE — likely not exact at d* = 0.2460. Need exact d*.

---

## P5 — The wobble gap = φ − π/2 exactly

**Claim:** N-ball n* − proxy n*_e = φ − π/2 exactly.

**Computed:** 5.2570 − 5.2096 = 0.0474 vs φ − π/2 = 0.0472. Difference: 2e-04.

**Test:** Compute both to 20 decimal places. If not exact, find what the residual is.

**Status:** APPROXIMATE — close but likely not exact

---

## P6 — Three-operator closure is a Noether conservation law

**Claim:** e^(πi) · e^(iφ) · e^(i(π−φ)) = 1 is not merely arithmetic — it is a Noether conservation law in the sedenion field. The three currents (electro, magneto, closure) are J_red, J_blue, and L_(I|O).

**Test:** Map each operator to a Noether current. Verify that the action integral ∫J_red·J_blue ds = L_(I|O) recovers the closure condition.

**Status:** OPEN — deep, requires D-M paper level analysis
