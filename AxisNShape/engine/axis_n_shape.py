"""
axis_n_shape.py — The Axis N-Shape: Euler's Formula as a Partial-Sum Spiral

THE CLAIM: the 16 sedenion basis directions, read as 16th roots of unity
via ptol.c's own spoke_angle formula, have partial sums (the "Axis N-shape
spiral") that follow the Dirichlet kernel exactly:

    |S_m| = sin((m+1) * THE_ANGLE / 2) / sin(THE_ANGLE / 2)      THE_ANGLE = pi/8

and the partial sum's PHASE crosses the real axis (Telperion's axis,
Euler's cos(X) term) at exactly m=8 -- the halfway index, m/N = 1/2,
the same location as sigma=1/2 in the Cayley-Dickson tower's proportional
mapping. Zero free parameters: only THE_ANGLE = pi/8, already established
in zero_lattice.py and ptol.c, is used.

WHAT WAS TRIED FIRST AND FAILED (kept in the record, not deleted):
the original hypothesis was that the partial-sum MAGNITUDE would have a
local minimum at m=8, mirroring the N-shape's single crossing point
(wiki/74, ADE type A2 fold). This is false -- the magnitude is near its
MAXIMUM at m=7-8 (the Dirichlet kernel's central lobe), and only returns
to zero trivially at m=15 (the complete sum of all 16 roots, the
elementary roots-of-unity identity Sum_{k=0}^{15} e^{i*2*pi*k/16} = 0).
The real, unexpected, and unforced structure is in the PHASE, not the
magnitude -- see below.

WHY THIS IS TELPERION / LAURELIN / EULER, PRECISELY:
    e^{i*theta} = cos(theta) + i*sin(theta)        Euler, forward (H_hat_RB)
    e^{-i*theta} = cos(theta) - i*sin(theta)       Euler, reverse (-H_hat_BR)

    cos(theta): generically nonzero (zeros only at isolated points off
        the natural lattice) -- the "un-shakeable" projection. Telperion.
    sin(theta): vanishes exactly on the natural lattice theta=0,pi,2pi,...
        -- periodic nodes, the "shakeable" projection. Laurelin.

The partial-sum spiral S_m = Sum_{k=0}^{m} e^{i*spoke_angle(k)} accumulates
both projections simultaneously (Euler refuses the half-coin separation,
wiki/53). Its phase crosses arg=0 (pure real, pure Telperion, zero
Laurelin component) at exactly m=8 -- not by any parameter fit, but
because summing a symmetric arc of unit vectors produces a resultant
whose phase is exactly the angular midpoint of the arc swept so far, a
standard elementary trigonometric identity. At m=8, the arc swept is
exactly the first half of the full circle (k=0..8, spanning the same
angular range as sigma=1 down to sigma=0 in the tower's own eight-level
mapping) -- so the real-axis crossing at m=8 IS the sigma=1/2 crossing,
read off from Euler's formula and THE_ANGLE alone.

Author:  Claude, at Cody's direction -- 2026-07-10
Version: 0.100 -- first pass
"""

import cmath
import math
from typing import Dict, List, Any

THE_ANGLE = math.pi / 8   # 22.5 degrees -- zero_lattice.py / ptol.c's angular quantum
N = 16                     # sedenion dimension


def spoke_angle(k: int, theta: float = 0.0) -> float:
    """Identical to ptol.c's spoke_angle(): the fixed 16-spoke grid."""
    return 2.0 * math.pi * k / N - math.pi / 2.0 + theta


def sedenion_roots() -> List[complex]:
    """The 16 sedenion basis directions as 16th roots of unity."""
    return [cmath.exp(1j * spoke_angle(k)) for k in range(N)]


def partial_sums(roots: List[complex]) -> List[complex]:
    """S_m = sum_{k=0}^{m} roots[k], for m = 0..N-1 -- the Axis N-shape spiral."""
    out = []
    acc = 0j
    for r in roots:
        acc += r
        out.append(acc)
    return out


def dirichlet_kernel(m: int, delta: float = THE_ANGLE) -> float:
    """Closed-form magnitude of the m-th partial sum (m=0..N-1)."""
    if abs(math.sin(delta / 2.0)) < 1e-15:
        return float(m + 1)
    return math.sin((m + 1) * delta / 2.0) / math.sin(delta / 2.0)


def failed_hypothesis_magnitude_minimum_at_half() -> Dict[str, Any]:
    """
    RECORDED, FALSIFIED: the original guess that |S_m| has a local minimum
    at m=8 (mirroring the N-shape's single ADE-A2 crossing). It does not.
    """
    roots = sedenion_roots()
    partial = partial_sums(roots)
    mags = [abs(s) for s in partial]
    min_idx = min(range(1, N), key=lambda i: mags[i])
    return {
        'claim': 'FALSIFIED: |S_m| has a local minimum at m=8',
        'magnitudes': [round(m, 6) for m in mags],
        'actual_minimum_index': min_idx,
        'actual_minimum_value': round(mags[min_idx], 10),
        'value_at_m8': round(mags[8], 6),
        'is_m8_the_minimum': min_idx == 8,
        'note': ('The minimum (m=15, value ~0) is the trivial complete-sum case '
                 '-- the elementary identity that all N-th roots of unity sum to '
                 'zero. m=8 is near the MAXIMUM of the Dirichlet kernel, not a '
                 'minimum. This hypothesis is false and is kept in the record.'),
        'confidence': 'FALSIFIED',
    }


def axis_n_shape_claim() -> Dict[str, Any]:
    """
    The actual, verified claim: partial-sum magnitude follows the Dirichlet
    kernel exactly, and partial-sum phase crosses the real (Telperion) axis
    exactly at m=8 -- the sigma=1/2 point, read from Euler's formula and
    THE_ANGLE alone, zero free parameters.
    """
    roots = sedenion_roots()
    partial = partial_sums(roots)

    magnitude_check = []
    for m, s in enumerate(partial):
        computed = abs(s)
        formula = dirichlet_kernel(m)
        magnitude_check.append({
            'm': m, 'computed': round(computed, 10), 'dirichlet_formula': round(formula, 10),
            'match': abs(computed - formula) < 1e-9,
        })
    all_match = all(row['match'] for row in magnitude_check)

    phase_at_8 = cmath.phase(partial[8])
    real_axis_crossing_exact = abs(phase_at_8) < 1e-9

    # Confirm no OTHER index crosses the real axis (uniqueness of the m=8 crossing)
    other_crossings = [
        m for m, s in enumerate(partial)
        if m != 8 and abs(s) > 1e-9 and abs(cmath.phase(s)) < 1e-9
    ]

    return {
        'claim': 'Partial-sum magnitude = Dirichlet kernel (exact); partial-sum phase '
                 'crosses the real (Telperion) axis exactly at m=8 = N/2, with zero '
                 'free parameters beyond THE_ANGLE = pi/8.',
        'magnitude_check': magnitude_check,
        'all_magnitudes_match_dirichlet_kernel': all_match,
        'phase_at_m8_degrees': round(math.degrees(phase_at_8), 10),
        'real_axis_crossing_exact_at_m8': real_axis_crossing_exact,
        'other_real_axis_crossings': other_crossings,
        'crossing_is_unique_to_m8': len(other_crossings) == 0,
        'm8_over_N': 8 / N,
        'confidence': 'ESTABLISHED' if (all_match and real_axis_crossing_exact and not other_crossings) else 'OPEN',
    }


def run_all() -> Dict[str, Any]:
    failed = failed_hypothesis_magnitude_minimum_at_half()
    verified = axis_n_shape_claim()

    print("=" * 78)
    print("  AXIS N-SHAPE — Euler's formula as a partial-sum spiral over THE_ANGLE")
    print("=" * 78)
    print()
    print("  FIRST HYPOTHESIS (falsified, kept in the record):")
    print(f"    {failed['claim']}")
    print(f"    Actual minimum at m={failed['actual_minimum_index']} "
          f"(value={failed['actual_minimum_value']:.2e}), not m=8 "
          f"(value at m=8: {failed['value_at_m8']})")
    print(f"    m=8 is the minimum: {failed['is_m8_the_minimum']}  -- FALSE, as stated above")
    print()
    print("  VERIFIED CLAIM:")
    print(f"    All 16 partial-sum magnitudes match the Dirichlet kernel exactly: "
          f"{verified['all_magnitudes_match_dirichlet_kernel']}")
    print(f"    Phase at m=8: {verified['phase_at_m8_degrees']:.10f} degrees "
          f"(real-axis crossing exact: {verified['real_axis_crossing_exact_at_m8']})")
    print(f"    This crossing is unique to m=8 (no other index crosses the real axis): "
          f"{verified['crossing_is_unique_to_m8']}")
    print(f"    m/N at the crossing: {verified['m8_over_N']} = sigma=1/2")
    print(f"    Confidence: {verified['confidence']}")
    print("=" * 78)

    return {'failed_hypothesis': failed, 'verified_claim': verified}


if __name__ == "__main__":
    run_all()
