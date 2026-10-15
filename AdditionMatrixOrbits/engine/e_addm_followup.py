#!/usr/bin/env python3
"""
e_addm_followup.py -- follow-up tests of "The Addition Matrix as Rotors" (Section 6 of the paper).

Self-contained apart from e_addm_orbits.py (same directory). The code of this file is the code of the three Explorer toolsets
`MultiplicationMatrixExplorer/toolsets/{torsor,treeaut,closedform}.py`, assembled here so that the paper can be reproduced from this
directory alone; `python3 e_addm_followup.py --crosscheck` compares the two when the Explorer can be found (next to this repository, or EXPLORER_PATH).

  F1 torsor    does anything in the solution tree prefer the true child? (guide rank tests, exact pruning counts)
  F2 treeaut   automorphisms of the depth-n binary tree: a 2-group of order 2^(2^n - 1); the affine maps on Z/2^n live inside it
  F3 closedform  the closed form for solutions of a*b = N mod p^k, every N, several primes

Labels: ESTABLISHED:CALCULATED (counts, enumeration); F1's rank statistics are measurements with a random-child control.
"""
from __future__ import annotations

import os
import random
import statistics
import sys
from itertools import permutations
from math import gcd, sqrt
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e_addm_orbits import (unit_solutions, prime_power_solutions, solution_count, primes_between)  # noqa: E402

# ── F1 torsor ──
def children(N: int, k: int) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    """Map each unit solution mod 10^k to its lifts mod 10^(k+1)."""
    M = 10 ** k
    out: Dict[Tuple[int, int], List[Tuple[int, int]]] = {(p, q): [] for p, q, _ in unit_solutions(N, k)}
    for p, q, _ in unit_solutions(N, k + 1):
        out[(p % M, q % M)].append((p, q))
    return out


def branching(N: int, k: int) -> Dict[int, int]:
    """{children: parents}: uniformly 10 when the tree is uniformly 10-ary."""
    out: Dict[int, int] = {}
    for kids in children(N, k).values():
        out[len(kids)] = out.get(len(kids), 0) + 1
    return out


def _avg_rank(values: List[float], target: float) -> float:
    """Normalised average rank of `target` among `values` (0 = smallest), ties averaged; 1 value gives 0.5."""
    less = sum(v < target for v in values)
    eq = sum(v == target for v in values)
    n = len(values)
    return ((less + (eq - 1) / 2) / (n - 1)) if n > 1 else 0.5


GUIDES = {
    "overflow": lambda N, k, p, q: abs((p * q - N) // 10 ** k),
    "size": lambda N, k, p, q: N - p * q if p * q <= N else 10 ** 60,   # closest from below
    "low": lambda N, k, p, q: p,
}


def rank_test(n_digits: int, level: int, trials: int = 100, seed: int = 0) -> Dict[str, object]:
    """Rank of the true child among its siblings at tree level `level` (child modulus 10^level), for each guide.

    Products of two distinct n-digit primes; `level` runs 2..n (level 1 has four roots, no parent). Returns the mean normalised rank
    per guide, a z-score against the no-information mean 1/2 (sd sqrt(1/12/trials)), and the same for a uniformly random child.
    """
    rng = random.Random(seed)
    P = primes_between(10 ** (n_digits - 1) + 1, 10 ** n_digits)
    P = [x for x in P if gcd(x, 10) == 1]
    ranks = {g: [] for g in GUIDES}
    ranks["random child"] = []
    for _ in range(trials):
        p, q = rng.sample(P, 2)
        N = p * q
        M = 10 ** level
        parent = (p % (M // 10), q % (M // 10))
        sibs = children(N, level - 1)[parent]
        true = (p % M, q % M)
        for g, f in GUIDES.items():
            vals = [f(N, level, a, b) for a, b in sibs]
            ranks[g].append(_avg_rank(vals, f(N, level, *true)))
        ranks["random child"].append(_avg_rank(list(range(len(sibs))), rng.randrange(len(sibs))))
    sd = sqrt(1 / 12 / trials)
    return {"n_digits": n_digits, "level": level, "trials": trials,
            "mean_rank": {g: statistics.mean(v) for g, v in ranks.items()},
            "z_vs_no_information": {g: (statistics.mean(v) - 0.5) / sd for g, v in ranks.items()}}


def pruning(N: int, n_digits: int) -> List[Tuple[int, int, int]]:
    """Per level k: (k, solutions, solutions with p'q' <= N): how much the exact bound removes."""
    return [(k, len(s), sum(1 for p, q, _ in s if p * q <= N)) for k in range(1, n_digits + 1) for s in [unit_solutions(N, k)]]


def self_check_torsor() -> dict:
    N = 14351
    return {"branching_k1": branching(N, 1), "branching_k2": branching(N, 2),
            "pruning_N14351": pruning(N, 3)}



# ── F2 treeaut ──
def preserves_tree(perm: tuple, n: int) -> bool:
    """A permutation of the 2^n leaves (as positions 0..2^n-1) is a tree automorphism iff it maps every aligned block of size 2^j onto an aligned block."""
    for j in range(1, n):
        size = 1 << j
        for start in range(0, 1 << n, size):
            images = {perm[x] // size for x in range(start, start + size)}
            if len(images) != 1:
                return False
    return True


def automorphism_count_brute(n: int) -> int:
    """Number of permutations of the 2^n leaves preserving the tree (n <= 3: all 40320 permutations for n = 3)."""
    return sum(1 for p in permutations(range(1 << n)) if preserves_tree(p, n))


def automorphism_count_recursive(n: int) -> int:
    """2 * |Aut(T_{n-1})|^2, starting from |Aut(T_0)| = 1: the closed form is 2^(2^n - 1)."""
    return 1 if n == 0 else 2 * automorphism_count_recursive(n - 1) ** 2


def affine_group_order(n: int) -> int:
    """Number of distinct maps x -> a x + b (a odd) on Z/2^n."""
    M = 1 << n
    return len({tuple((a * x + b) % M for x in range(M)) for a in range(1, M, 2) for b in range(M)})


def affine_maps_preserve_tree(n: int) -> bool:
    M = 1 << n
    for a in range(1, M, 2):
        for b in range(M):
            for k in range(1, n):
                m = 1 << k
                if any((a * x + b) % m != (a * (x % m) + b) % m for x in range(M)):
                    return False
    return True


def cycle_lengths(a: int, b: int, m: int) -> List[int]:
    seen, out = bytearray(m), []
    for s in range(m):
        if not seen[s]:
            n, x = 0, s
            while not seen[x]:
                seen[x] = 1
                x = (a * x + b) % m
                n += 1
            out.append(n)
    return sorted(set(out))


def self_check_treeaut() -> Dict[str, object]:
    brute = {n: automorphism_count_brute(n) for n in (1, 2, 3)}
    return {"brute_force": brute, "formula_2^(2^n-1)": {n: 2 ** (2 ** n - 1) for n in (1, 2, 3, 4)},
            "recursion": {n: automorphism_count_recursive(n) for n in (1, 2, 3, 4)},
            "brute_equals_formula": all(brute[n] == 2 ** (2 ** n - 1) for n in brute),
            "affine_group_order_2^(2n-1)": {n: (affine_group_order(n), 2 ** (2 * n - 1)) for n in (2, 3, 4, 5, 6)},
            "affine_maps_preserve_tree": all(affine_maps_preserve_tree(n) for n in (3, 4, 5)),
            "all_affine_cycle_lengths_powers_of_two_Z2^8": all(l & (l - 1) == 0 for a in range(1, 256, 2) for b in range(0, 256, 17) for l in cycle_lengths(a, b, 256)),
            "Z5^m_cycle_lengths_of_x->2x+1": {m: cycle_lengths(2, 1, 5 ** m) for m in (1, 2, 3, 4)}}



# ── F3 closedform ──
def brute(N: int, M: int) -> int:
    """Pairs (a, b) mod M with a*b = N mod M: for each a, gcd(a, M) solutions when gcd(a, M) divides N mod M."""
    return sum(gcd(a, M) for a in range(M) if (N % M) % gcd(a, M) == 0)


def check_prime_power(p: int, k: int) -> int:
    """Number of residues N mod p^k whose closed form differs from enumeration (0 = the formula holds for every N)."""
    M = p ** k
    return sum(prime_power_solutions(N, p, k) != brute(N, M) for N in range(M))


def check_ten(k: int, sample: List[int] = None) -> int:
    M = 10 ** k
    Ns = range(M) if sample is None else sample
    return sum(solution_count(N, k) != brute(N, M) for N in Ns)


def self_check_closedform() -> Dict[str, object]:
    pp = {(p, k): check_prime_power(p, k) for p, ks in ((2, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)), (3, (1, 2, 3, 4, 5, 6)), (5, (1, 2, 3, 4)), (7, (1, 2, 3)), (11, (1, 2))) for k in ks}
    pickN = lambda k: [0, 1, 2 ** k, 5 ** k, 2 ** (k - 1) * 5 ** (k - 1), 2 ** k * 5 ** k // 2, 12345 % 10 ** k, 10 ** k - 1, 4000 % 10 ** k, 6250 % 10 ** k]
    return {"prime_power_mismatches (every N)": {f"{p}^{k}": m for (p, k), m in pp.items()},
            "all_prime_power_ok": all(m == 0 for m in pp.values()),
            "ten_k_1_to_3_every_N": {k: check_ten(k) for k in (1, 2, 3)},
            "ten_k_4_5_selected_N": {k: check_ten(k, pickN(k)) for k in (4, 5)}}




def crosscheck() -> dict:
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.environ.get("EXPLORER_PATH", ""), os.path.join(here, "..", "..", "..", "MultiplicationMatrixExplorer")):
        if cand and os.path.isdir(os.path.join(cand, "toolsets")):
            sys.path.insert(0, cand)
            break
    else:
        return {"found": False}
    from toolsets import treeaut as TA, closedform as CF, torsor as TO
    return {"found": True, "treeaut_equal": TA.self_check() == self_check_treeaut(),
            "closedform_equal": CF.self_check() == self_check_closedform(),
            "torsor_equal": TO.self_check() == self_check_torsor() and
                            TO.rank_test(4, 3, trials=40, seed=7) == rank_test(4, 3, trials=40, seed=7)}


if __name__ == "__main__":
    if "--crosscheck" in sys.argv:
        print(crosscheck())
    else:
        for name, f in (("torsor", self_check_torsor), ("treeaut", self_check_treeaut), ("closedform", self_check_closedform)):
            print(name, f())
