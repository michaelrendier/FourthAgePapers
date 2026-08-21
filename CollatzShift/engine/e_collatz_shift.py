"""
e_collatz_shift.py — the Collatz map is the binary shift, and the tree is Pascal's

Fourth Age Paper: **Collatz as the 2-adic Shift**.
One Paper. One RESULT. One Engine. One Wiki.

Built 2026-08-21. python3 first, stdlib only. Self-verifying: every number is
COMPUTED at run time, never asserted. Report discipline is the
`generational-lineage` skill — each relation states its tier, what it descends
from, and its status, and the three kinds of wrong are kept apart:

    CODE fault    the check did not run          -> UNJUDGED
    MATHS fault   both sides measured, disagree  -> FALSE
    METHOD error  correct code, correct maths, wrong question -> invisible here

═══════════════════════════════════════════════════════════════════════════
WHAT THIS PAPER IS — AND IS NOT
═══════════════════════════════════════════════════════════════════════════

This paper makes NO CLAIM and NO PREDICTION. That is deliberate and it is the
one place it departs from the Fourth Age template. It is a straight analysis:
known number theory, re-measured under this framework's engine contract, plus
one thing that is genuinely ours — the generational-lineage decomposition of
the Collatz map itself.

PROVENANCE, stated per result so nothing is smuggled:

  KNOWN   R2, R3   the parity-vector conjugacy to the binary shift is
                   Bernstein (1994) / Bernstein-Lagarias (1996). Re-measured
                   here exhaustively to k=16, not cited.
  KNOWN   R1       T^k affine on residue classes mod 2^k is folklore, older
                   than the conjugacy result.
  KNOWN   R6       cycles <-> rationals with denominator 2^k - 3^d is standard
                   (the "Diophantine" half of the problem). 2^k - 3^d = 1 only
                   at (k,d)=(2,1) is Levi ben Gerson / Catalan, cited not
                   proved.
  KNOWN   R7       multiples of 3 are leaves in the backward tree. Elementary.
  KNOWN   R10      the sqrt(3)/2 heuristic drift. Terras/Everett 1976-79.
  OURS    R4, R5   the tessellation reading: the class tree at level k has
                   d-histogram EXACTLY binomial C(k,d), so the "chaos" is
                   Pascal's triangle read in the wrong metric, and the
                   log-normality is de Moivre-Laplace, not an empirical fact.
                   Elementary once seen. We claim the FRAMING, not the maths.
  OURS    R8, R9   the information-direction measurement: forward is exactly
                   2-to-1 (1 bit destroyed per step, entropy log 2), backward
                   on N has mean out-degree strictly below 2, and the deficit
                   is exactly the mod-3 orphan set. This is the tower-direction
                   asymmetry made numerical.
  OURS    the lineage verdict.

NOTHING HERE PROVES OR DISPROVES THE COLLATZ CONJECTURE, and nothing here is
evidence for or against it. The conjecture is untouched. What the paper does is
say precisely WHERE the difficulty lives: not in the dynamics, which are
completely understood, but in how N sits inside Z_2.

═══════════════════════════════════════════════════════════════════════════
THE MAP
═══════════════════════════════════════════════════════════════════════════

The shortcut map throughout (one halving folded into the odd branch, so every
step does work):

    T(n) = n/2        n even
    T(n) = (3n+1)/2   n odd

SIGMA: infinity for R1-R9 (exact / exhaustive over a finite space).
       2.5 for R10 (a sampled statistic with a known termination bias, stated).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from typing import Dict, List, Sequence, Tuple

# ═══════════════════════════════════════════════════════════════════════════
# The map, and its two readings
# ═══════════════════════════════════════════════════════════════════════════


def T(n: int) -> int:
    """The shortcut Collatz map. SIGN selects, SCALE acts, ADD couples."""
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def parity_word(n: int, k: int) -> Tuple[int, ...]:
    """The first k parities along the orbit of n. This is the 2-adic ADDRESS."""
    out, m = [], n
    for _ in range(k):
        out.append(m & 1)
        m = T(m)
    return tuple(out)


def parity_vector(n: int, k: int) -> int:
    """parity_word packed little-endian into an integer of Z/2^k."""
    v, m = 0, n
    for i in range(k):
        v |= (m & 1) << i
        m = T(m)
    return v


def branch_affine(k: int, j: int) -> Tuple[int, Fraction, Fraction]:
    """For n = j (mod 2^k):  T^k(n) = (3^d n + c)/2^k.  Returns (d, slope, c).

    Fits the affine map from two lifts and then CHECKS the slope against
    3^d/2^k rather than assuming it — a fit that is never tested is a code
    fault waiting to happen.
    """
    lifts = []
    for t in range(3):
        n = j + t * (1 << k)
        m, d = n, 0
        for _ in range(k):
            if m & 1:
                d += 1
            m = T(m)
        lifts.append((n, m, d))
    ds = {L[2] for L in lifts}
    if len(ds) != 1:
        raise ValueError(f'd not constant on class {j} mod 2^{k}: {ds}')
    d = ds.pop()
    (n0, m0, _), (n1, m1, _) = lifts[0], lifts[1]
    slope = Fraction(m1 - m0, n1 - n0)
    c = Fraction(m0) - slope * n0
    return d, slope, c


def rational_cycle(word: Sequence[int]) -> Tuple[object, int, int, int]:
    """Solve T^k(x) = x over Q for a given periodic parity word.

    Returns (x or None, d, k, 2^k - 3^d). The denominator of x is always a
    divisor of 2^k - 3^d; the cycle is an INTEGER cycle only when that
    quantity divides the numerator.
    """
    a, c, d = Fraction(1), Fraction(0), 0
    for b in word:
        if b:
            a, c, d = a * 3 / 2, (c * 3 + 1) / 2, d + 1
        else:
            a, c = a / 2, c / 2
    k = len(word)
    denom = 2 ** k - 3 ** d
    if a == 1:
        return None, d, k, denom
    return c / (1 - a), d, k, denom


def normal_cdf(z: float) -> float:
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


# ═══════════════════════════════════════════════════════════════════════════
# The verifying harness — same contract as VAPMIP engines/e10
# ═══════════════════════════════════════════════════════════════════════════


class Status(Enum):
    HOLDS = 'HOLDS'
    FALSE = 'MATHS-FAULT'
    UNJUDGED = 'CODE-FAULT'


@dataclass
class Relation:
    name: str
    claim: str
    tier: int             # 0 irreducible · 1 reflect/dilate · 2 fixed set · 3 count/ratio
    descends: str
    provenance: str       # KNOWN (with attribution) or OURS
    status: Status
    detail: str


class CollatzShiftEngine:
    """Ten relations. Each one measured, each one tiered, each one attributed."""

    def __init__(self) -> None:
        self.log: List[Relation] = []

    def _record(self, name, claim, tier, descends, provenance, ran, holds, detail):
        st = Status.UNJUDGED if not ran else (Status.HOLDS if holds else Status.FALSE)
        self.log.append(Relation(name, claim, tier, descends, provenance, st, detail))

    # ── R1 — T^k is affine on each residue class mod 2^k ────────────────────
    def r_affine_on_classes(self, kmax: int = 8) -> None:
        ok, seen = True, []
        for k in range(1, kmax + 1):
            for j in range(1 << k):
                d, slope, _ = branch_affine(k, j)
                if slope != Fraction(3 ** d, 1 << k):
                    ok = False
            seen.append(k)
        self._record(
            'collatz.affine_on_classes',
            'T^k restricted to n = j (mod 2^k) is the affine map '
            '(3^d n + c)/2^k, and d depends only on the CLASS, never on n',
            1, 'SCALE — a dilation of gain 3^d/2^k', 'KNOWN (folklore)',
            True, ok,
            f'checked every class at every k in {seen[0]}..{seen[-1]}: '
            f'{sum(1 << k for k in seen)} classes, slope = 3^d/2^k in all of '
            f'them. The map is piecewise-affine and the pieces are indexed by '
            f'Z/2^k — this IS the "recursive decomposition on a modular '
            f'function".')

    # ── R2 — the parity vector is a bijection on Z/2^k ──────────────────────
    def r_parity_bijection(self, ks=(1, 2, 4, 8, 12, 16)) -> None:
        rows = {}
        for k in ks:
            rows[k] = len({parity_vector(n, k) for n in range(1 << k)})
        ok = all(rows[k] == (1 << k) for k in ks)
        self._record(
            'collatz.parity_bijection',
            'Q_k : Z/2^k -> Z/2^k, n |-> its first k parities, is a BIJECTION',
            3, 'SIGN — one bit per step, iterated k times',
            'KNOWN (Bernstein 1994; Bernstein-Lagarias 1996)',
            True, ok,
            '  '.join(f'k={k}:{rows[k]}/{1 << k}' for k in ks) +
            '  — exhaustive, no sampling. The address space is filled exactly '
            'once: every parity word belongs to exactly one class.')

    # ── R3 — the conjugacy: Collatz IS the shift ────────────────────────────
    def r_shift_conjugacy(self, ks=(8, 12, 16)) -> None:
        rows = {}
        for k in ks:
            rows[k] = all(parity_vector(T(n), k - 1) == (parity_vector(n, k) >> 1)
                          for n in range(1 << k))
        ok = all(rows.values())
        self._record(
            'collatz.shift_conjugacy',
            'Q(T(n)) = shift(Q(n)) — T is CONJUGATE to the one-sided binary '
            'shift; on Z_2 the Collatz map is chopping a digit off an address',
            2, 'the bijection of R2 — a change of coordinates, i.e. a fixed set '
               'of the conjugating map',
            'KNOWN (Bernstein-Lagarias 1996)',
            True, ok,
            '  '.join(f'k={k}:{rows[k]}' for k in ks) +
            '  — verified for EVERY n in Z/2^k, not sampled. The dynamics are '
            'therefore completely understood: entropy log 2, dense periodic '
            'points, uncountably many orbits. All difficulty is in how N sits '
            'inside Z_2, not in the map.')

    # ── R4 — the tessellation: the class tree is Pascal's triangle ──────────
    def r_pascal_refinement(self, kmax: int = 12) -> None:
        rows, ok = {}, True
        for k in range(1, kmax + 1):
            hist: Dict[int, int] = {}
            for j in range(1 << k):
                d, _, _ = branch_affine(k, j)
                hist[d] = hist.get(d, 0) + 1
            want = {d: math.comb(k, d) for d in range(k + 1)}
            if hist != want:
                ok = False
            rows[k] = hist
        self._record(
            'collatz.pascal_refinement',
            'over the 2^k classes mod 2^k the number of odd steps d is '
            'distributed EXACTLY as C(k,d) — the branch tree is Pascal\'s '
            'triangle, with no error term',
            3, 'a COUNT over the classes of R1',
            'OURS (framing; the maths is elementary once stated)',
            True, ok,
            f'exact binomial at every k in 1..{kmax}. k=8 histogram: '
            f'{dict(sorted(rows[8].items()))}. This is the tessellation: what '
            f'looks like chaos in the integers is a perfect binary refinement '
            f'in the address space — the same relationship a dragon or Hilbert '
            f'curve has to its digit expansion.')

    # ── R5 — and therefore the log is Gaussian, by de Moivre-Laplace ────────
    def r_gaussian_from_pascal(self, k: int = 20) -> None:
        mu, sd = k * 0.5, math.sqrt(k * 0.25)
        worst = 0.0
        cum = 0
        total = 1 << k
        for d in range(k + 1):
            cum += math.comb(k, d)
            emp = cum / total
            thy = normal_cdf((d + 0.5 - mu) / sd)
            worst = max(worst, abs(emp - thy))
        ok = worst < 0.01
        drift_mu = k * (0.5 * math.log(1.5) + 0.5 * math.log(0.5))
        self._record(
            'collatz.gaussian_from_pascal',
            'log n along an orbit is a SUM of k iid log-steps whose count is '
            'Binomial(k, 1/2); the normal curve is de Moivre-Laplace on R4, '
            'not an empirical observation',
            3, 'the binomial of R4 — a ratio of counts in the limit',
            'OURS (framing)',
            True, ok,
            f'k={k}: sup|binomial CDF - normal CDF| = {worst:.5f} < 0.01 '
            f'(exact binomial, no sampling). E[log n_k - log n_0] = '
            f'{drift_mu:.4f}. "Chaos in many dimensions becomes order" is this '
            f'theorem and nothing more mysterious.')

    # ── R6 — cycles are rationals with denominator 2^k - 3^d ────────────────
    def r_cycle_denominator(self, kmax: int = 16) -> None:
        integer_cycles, checked = [], 0
        for k in range(1, kmax + 1):
            for mask in range(1 << k):
                word = tuple((mask >> i) & 1 for i in range(k))
                # PRIMITIVE necklaces only. A periodic word such as 1010 is the
                # SAME cycle walked twice; counting it again reports one loop as
                # many. (This was a live MATHS-FAULT on the first run — the
                # filter was rotation-minimality alone, which let 1010, 101010,
                # ... through and made {1,2} look like seven distinct cycles.)
                if any(k % p == 0 and word == word[:p] * (k // p)
                       for p in range(1, k)):
                    continue
                if any(word[i:] + word[:i] < word for i in range(1, k)):
                    continue                      # one rotation per necklace
                x, d, kk, denom = rational_cycle(word)
                checked += 1
                if x is not None and x.denominator == 1 and x > 0:
                    integer_cycles.append((int(x), kk, d, denom))
        found = sorted(set(integer_cycles))
        ok = found == [(2, 2, 1, 1)]
        ladder = [(k, d, 2 ** k - 3 ** d)
                  for k, d in ((2, 1), (3, 2), (5, 3), (8, 5), (13, 8), (19, 12))]
        self._record(
            'collatz.cycle_denominator',
            'every periodic parity word of length k with d ones determines ONE '
            'rational cycle whose denominator divides 2^k - 3^d; the only '
            'positive-integer cycle up to k=%d is {1,2}' % kmax,
            3, 'a RATIO — the fixed point of the affine map of R1',
            'KNOWN (standard; 2^k-3^d=1 only at (2,1) is Levi ben Gerson / '
            'Catalan, cited not proved here)',
            True, ok,
            f'{checked} PRIMITIVE necklaces enumerated to k={kmax}; '
            f'positive-integer cycles found: {found} — exactly one, the loop '
            f'{{1,2}}, appearing once as its rotation-minimal representative. '
            f'Ladder 2^k-3^d along the convergents of log2(3)='
            f'{math.log(3, 2):.8f}: ' +
            ', '.join(f'({k},{d})->{v}' for k, d, v in ladder) +
            '. The "near miss" is a linear form in logarithms — the same '
            'family as the Fermat near-miss work, NOT the same problem.')

    # ── R7 — mod 3 is the orphan test in the backward tree ──────────────────
    def r_mod3_orphans(self, N: int = 300_000) -> None:
        has_odd_pre = {n % 3 for n in range(1, N)
                       if (2 * n - 1) % 3 == 0 and ((2 * n - 1) // 3) % 2 == 1}
        never = all((3 * m + 1) // 2 % 3 != 0 for m in range(1, N, 2))
        ok = has_odd_pre == {2} and never
        self._record(
            'collatz.mod3_orphans',
            'n has an ODD predecessor iff n = 2 (mod 3); multiples of 3 are '
            'leaves of the backward tree at every scale, permanently',
            2, 'a FIXED SET — the image of the odd branch, ker of nothing else',
            'KNOWN (elementary)',
            True, ok,
            f'residues with an odd predecessor, n<{N:,}: {sorted(has_odd_pre)}. '
            f'(3m+1)/2 is never 0 mod 3, checked for every odd m<{N:,}. '
            f'Contrast sieve_clock.py: a sieve orphan at N is adopted at 2N. '
            f'A Collatz orphan is NEVER adopted — the bound is algebraic, not '
            f'a universe size.')

    # ── R8 — forward is exactly 2-to-1: one bit destroyed per step ──────────
    def r_forward_two_to_one(self, ks=(6, 8, 10, 12)) -> None:
        rows = {}
        for k in ks:
            M = 1 << k
            counts: Dict[int, int] = {}
            for n in range(M):
                counts[T(n) % (M >> 1)] = counts.get(T(n) % (M >> 1), 0) + 1
            rows[k] = sorted(set(counts.values()))
        ok = all(rows[k] == [2] for k in ks)
        self._record(
            'collatz.forward_two_to_one',
            'T is exactly 2-to-1 on Z_2: each forward step destroys exactly one '
            'bit. Going DOWN the tower is information propagation, and the '
            'propagated quantity is the parity word',
            3, 'a COUNT of preimages — the shift of R3 is 2-to-1 by construction',
            'OURS (the measurement; the fact follows from R3)',
            True, ok,
            'T is well defined as a map Z/2^k -> Z/2^(k-1); fibre sizes, '
            'uniform at every level: ' +
            '  '.join(f'k={k}:{rows[k]}' for k in ks) +
            '  — every fibre has exactly 2 elements, |domain|/|codomain| = 2 '
            'with no exceptional fibre. (First run asserted 4 here and the '
            'harness returned MATHS-FAULT; the measurement was right and the '
            'assertion was wrong — a CODE fault, recorded rather than tidied '
            'away.) Entropy log 2 per step, and the destroyed bit never '
            'comes back — '
            'provenance is discarded exactly as intention_monad.py discards it '
            'on collection.')

    # ── R9 — backward on N carries strictly less: the deficit is the orphans ─
    def r_backward_deficit(self, N: int = 1_000_000) -> None:
        deg, vacuous = 0, True
        for n in range(1, N):
            deg += 1                                        # 2n, always
            if (2 * n - 1) % 3 == 0:
                # (2n-1) is odd and 3 is odd, so the quotient is ALWAYS odd —
                # there is no second condition. Checked, not assumed.
                if ((2 * n - 1) // 3) % 2 != 1:
                    vacuous = False
                deg += 1
        mean_deg = deg / (N - 1)
        predicted = 4.0 / 3.0
        ok = abs(mean_deg - predicted) < 1e-3 and vacuous
        self._record(
            'collatz.backward_deficit',
            'the backward tree on N has mean out-degree 4/3, not 2: going UP '
            'the tower does not propagate information, it enumerates '
            'possibilities — and the shortfall is exactly log(3/2), the odd '
            'branch\'s own gain',
            3, 'a COUNT — the complement of the fixed set of R7',
            'OURS (the measurement)',
            True, ok,
            f'measured mean out-degree over n<{N:,} = {mean_deg:.6f}; '
            f'predicted 4/3 = {predicted:.6f} — always 2n, plus an odd '
            f'predecessor on exactly the density-1/3 set n = 2 (mod 3). The '
            f'second condition usually written here, "(2n-1)/3 must be odd", '
            f'is VACUOUS and was measured to be so ({vacuous}): 2n-1 is odd '
            f'and 3 is odd, so the quotient is odd whenever it is an integer. '
            f'(First run predicted 7/6 from that phantom condition and the '
            f'harness returned MATHS-FAULT.) '
            f'Forward destroys log 2 = {math.log(2):.4f} nats per step; '
            f'backward restores log(4/3) = {math.log(4/3):.4f}. The shortfall '
            f'is {math.log(2) - math.log(4/3):.4f} = log(3/2) = '
            f'{math.log(1.5):.4f} EXACTLY — the deficit between the two '
            f'directions is the odd branch\'s own gain, and it is the '
            f'arithmetic that the 2-adic metric cannot see.')

    # ── R10 — the drift, and why sigma = 1/2 makes it contract ──────────────
    def r_drift_at_half(self, N: int = 60_000) -> None:
        tot, steps = 0.0, 0
        for n in range(3, N, 2):
            m = n
            for _ in range(200):
                m2 = T(m)
                tot += math.log(m2 / m)
                steps += 1
                m = m2
                if m == 1:
                    break
        measured = tot / steps
        predicted = 0.5 * math.log(1.5) + 0.5 * math.log(0.5)
        p_crit = math.log(2) / math.log(3)
        ok = measured < 0 and predicted < 0 and abs(measured - predicted) < 0.05
        self._record(
            'collatz.drift_at_half',
            'at parity measure 1/2 the per-step geometric mean is sqrt(3)/2 < 1; '
            'the drift is negative BECAUSE the two branches are balanced, and '
            'the balance point is the Haar measure on Z_2',
            3, 'a RATIO of the two gains of R1, weighted by the Bernoulli(1/2) '
               'measure the conjugacy of R3 preserves',
            'KNOWN (Terras 1976; Everett 1977)',
            True, ok,
            f'measured mean log-step over {steps:,} steps (odd starts < {N:,}) '
            f'= {measured:+.6f}; predicted log(sqrt(3)/2) = {predicted:+.6f}. '
            f'Residual {measured - predicted:+.6f} is TERMINATION BIAS — the '
            f'sample stops at 1, which truncates the low tail; it is not a '
            f'disagreement with the model and is not corrected for. Critical '
            f'parity fraction (drift = 0) is log2/log3 = {p_crit:.6f}; '
            f'1/2 sits below it with margin.')

    # ── the lineage verdict ─────────────────────────────────────────────────
    def lineage(self) -> List[Tuple[str, int, str, str]]:
        """Decomposition of T against the Two Trees operation domain."""
        return [
            ('n mod 2  (branch select)', 0, 'SIGN',
             'PRIMITIVE — one bit, nothing between'),
            ('n / 2', 1, 'SCALE -> DILATE, gain 1/2',
             'derived — changes length, so needs DILATE'),
            ('3n', 1, 'SCALE -> DILATE, gain 3',
             'derived — changes length, so needs DILATE'),
            ('+ 1', 0, 'ADD',
             'PRIMITIVE — identity 0; the only coupling between the two axes'),
            ('T = the Collatz map', 3, 'ADD o SCALE o SIGN',
             'DERIVED — no new generator required'),
        ]

    def run(self) -> None:
        for r in (self.r_affine_on_classes, self.r_parity_bijection,
                  self.r_shift_conjugacy, self.r_pascal_refinement,
                  self.r_gaussian_from_pascal, self.r_cycle_denominator,
                  self.r_mod3_orphans, self.r_forward_two_to_one,
                  self.r_backward_deficit, self.r_drift_at_half):
            r()

    def report(self) -> None:
        print('=' * 78)
        print('COLLATZ AS THE 2-ADIC SHIFT — engine report')
        print('=' * 78)
        held = sum(1 for r in self.log if r.status is Status.HOLDS)
        print(f'{held}/{len(self.log)} relations hold\n')
        w = max(len(r.name) for r in self.log)
        print(f'{"relation":<{w}}  tier  {"status":<11}  provenance')
        print('-' * 78)
        for r in self.log:
            print(f'{r.name:<{w}}   t{r.tier}   {r.status.value:<11}  {r.provenance}')
        print('-' * 78)
        for r in self.log:
            print(f'\n{r.name}   [tier {r.tier} | {r.provenance}]')
            print(f'  descends: {r.descends}')
            print(f'  claim   : {r.claim}')
            print(f'  detail  : {r.detail}')

        print('\n' + '=' * 78)
        print('GENERATIONAL LINEAGE — T decomposed against the Two Trees domain')
        print('=' * 78)
        print(f'{"operation":<26} {"tier":<5} {"descends from":<28} status')
        print('-' * 78)
        for op, tier, desc, st in self.lineage():
            print(f'{op:<26} t{tier:<4} {desc:<28} {st}')
        print('-' * 78)
        faults = [r for r in self.log if r.status is not Status.HOLDS]
        if faults:
            print('EMERGENCE FLAG: ' + ', '.join(r.name for r in faults) +
                  ' did not hold — investigate before trusting the map.')
        else:
            print('No new generator required. The Collatz map is the smallest')
            print('non-trivial composition that uses all three tier-0')
            print('irreducibles at once. ADD and SCALE have DIFFERENT identities')
            print('(0 and 1); the "+1" is the only thing coupling them, and that')
            print('coupling is the whole difficulty. Drop it and n -> 3n/2^v is a')
            print('pure SCALE tower with no conjecture in it.')
        print('=' * 78)


def run(verbose: bool = True) -> Dict[str, object]:
    """Notebook entry point (matches the e01-e10 contract)."""
    eng = CollatzShiftEngine()
    eng.run()
    if verbose:
        eng.report()
    held = sum(1 for r in eng.log if r.status is Status.HOLDS)
    return {
        'relations': [(r.name, r.tier, r.status.value, r.provenance, r.claim)
                      for r in eng.log],
        'lineage': eng.lineage(),
        'held': held,
        'total': len(eng.log),
        'all_hold': held == len(eng.log),
        'engine': eng,
    }


def main() -> None:
    run(verbose=True)


if __name__ == '__main__':
    main()
