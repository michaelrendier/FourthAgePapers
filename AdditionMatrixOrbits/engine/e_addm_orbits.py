#!/usr/bin/env python3
"""
e_addm_orbits.py -- the addition matrix as arithmetic modulo 10^k: columns as rotors, the closed-form law of
the digit-by-digit factor search, and the K = 0 address of the final answer.

Self-contained (standard library only) so that the paper can be reproduced without any other repository.
The same mathematics is the ValaQuenta engine `addition_matrix` (v1.0) and `MultiplicationMatrixExplorer/toolsets/law.py`;
`python3 e_addm_orbits.py --crosscheck` compares this file with the ValaQuenta engine when it can be found
(next to this repository, or set VQ_PATH to the directory that CONTAINS ValaQuenta).

Labels: every result is ESTABLISHED:CALCULATED (elementary number theory, checked by this code over the stated
range); the K = 0 address is OURS (a restatement, reported with its neighbours). Nothing here is a factoring
method: the live-state count is the cost of the search it describes.
"""
from __future__ import annotations

import statistics
import sys
from math import gcd
from typing import Dict, List, Optional, Tuple


def digits_lsb(n: int, width: int) -> List[int]:
    out = []
    for _ in range(width):
        out.append(n % 10)
        n //= 10
    if n:
        raise ValueError(f"{n} needs more than {width} digits")
    return out


def carry_matrix(num1: int, num2: int, n_digits: int = 10) -> Tuple[List[List[int]], int]:
    """Rows num1*digit_j shifted j places, added one at a time; returns (carries, product)."""
    n_cols = 2 * n_digits + 1
    d2 = digits_lsb(num2, n_digits)
    total, carries = [0] * n_cols, []
    for j in range(n_digits):
        row = [0] * n_cols
        for k, d in enumerate(digits_lsb(num1 * d2[j], n_digits + 1)):
            row[j + k] = d
        carry, out = 0, [0] * n_cols
        for c in range(n_cols):
            s = total[c] + row[c] + carry
            total[c], carry = s % 10, s // 10
            out[c] = carry
        carries.append(out)
    return carries, sum(d * 10 ** c for c, d in enumerate(total))


def column_period(num1: int, c: int) -> int:
    """Period in num2 of the digit in column c of num1*num2: 10^(c+1) / gcd(num1, 10^(c+1))."""
    m = 10 ** (c + 1)
    return m // gcd(num1, m)


def column_period_measured(num1: int, c: int) -> int:
    """Least t > 0 with digit_c(num1*(x+t)) == digit_c(num1*x) for every x (divisors tried in order, full range tested)."""
    m = 10 ** (c + 1)
    f = lambda x: (num1 * x // 10 ** c) % 10
    for t in sorted(d for d in range(1, m + 1) if m % d == 0):
        if all(f(x + t) == f(x) for x in range(m)):
            return t
    return m


def affine_cycle_type(a: int, b: int, m: int) -> Dict[int, int]:
    """Cycle lengths of x -> a x + b on Z/m as {length: count}; raises ValueError when the map is not a permutation."""
    nxt = lambda x: (a * x + b) % m
    if len({nxt(x) for x in range(m)}) != m:
        raise ValueError("not a permutation")
    seen, out = bytearray(m), {}
    for s in range(m):
        if seen[s]:
            continue
        n, x = 0, s
        while not seen[x]:
            seen[x] = 1
            x = nxt(x)
            n += 1
        out[n] = out.get(n, 0) + 1
    return out


def crt_combine(t2: Dict[int, int], t5: Dict[int, int]) -> Dict[int, int]:
    """Cycle lengths l1, l2 on coprime factors give gcd(l1, l2) cycles of length lcm(l1, l2)."""
    out: Dict[int, int] = {}
    for l1, n1 in t2.items():
        for l2, n2 in t5.items():
            g = gcd(l1, l2)
            out[l1 * l2 // g] = out.get(l1 * l2 // g, 0) + n1 * n2 * g
    return out


def crt_rule_holds(a: int, b: int, m: int) -> bool:
    return affine_cycle_type(a, b, 10 ** m) == crt_combine(affine_cycle_type(a, b, 2 ** m), affine_cycle_type(a, b, 5 ** m))


def odometer_first_return(m: int) -> bool:
    """First return of x -> x+1 on Z/10^m to the multiples of 10 is x -> x+10, i.e. the odometer on Z/10^(m-1) after dividing by 10."""
    M = 10 ** m
    return all(((x + 10) % M) // 10 == (x // 10 + 1) % (M // 10) for x in range(0, M, 10))


def valuation(N: int, p: int, cap: Optional[int] = None) -> int:
    if N == 0:
        return cap if cap is not None else 10 ** 9
    v = 0
    while N % p == 0 and (cap is None or v < cap):
        N //= p
        v += 1
    return v


def phi_prime_power(p: int, k: int) -> int:
    return p ** (k - 1) * (p - 1)


def prime_power_solutions(N: int, p: int, k: int) -> int:
    v = valuation(N, p, cap=k)
    return (v + 1) * phi_prime_power(p, k) if v < k else k * phi_prime_power(p, k) + p ** k


def solution_count(N: int, k: int) -> int:
    return prime_power_solutions(N, 2, k) * prime_power_solutions(N, 5, k)


def solution_count_brute(N: int, k: int) -> int:
    M = 10 ** k
    return sum(gcd(a, M) for a in range(M) if (N % M) % gcd(a, M) == 0)


def live_state_counts(N: int, n_digits: int) -> List[int]:
    states, counts = [(0, 0)], []
    for c in range(2 * n_digits):
        mod, target, nxt = 10 ** (c + 1), N % 10 ** (c + 1), []
        if c < n_digits:
            step = 10 ** c
            for p, q in states:
                for dp in range(10):
                    P = p + dp * step
                    for dq in range(10):
                        Q = q + dq * step
                        if (P * Q) % mod == target:
                            nxt.append((P, Q))
        else:
            nxt = [(p, q) for p, q in states if (p * q) % mod == target]
        states = nxt
        counts.append(len(states))
    return counts


def unit_group_order(k: int) -> int:
    return phi_prime_power(2, k) * phi_prime_power(5, k)


def torsor_orbits(N: int, k: int) -> Optional[int]:
    v2, v5 = valuation(N, 2, cap=k), valuation(N, 5, cap=k)
    return None if (v2 >= k or v5 >= k) else (v2 + 1) * (v5 + 1)


def unit_solutions(N: int, n: int) -> List[Tuple[int, int, int]]:
    M = 10 ** n
    if gcd(N, 10) != 1:
        raise ValueError("unit_solutions needs N coprime to 10")
    out = []
    for p in range(1, M):
        if gcd(p, 10) != 1:
            continue
        q = (N * pow(p, -1, M)) % M
        out.append((p, q, (p * q - N) // M))
    return out


def address_profile(N: int, n: int) -> Dict[str, object]:
    sols = unit_solutions(N, n)
    ks = [abs(k) for _, _, k in sols]
    nz = sorted(k for k in ks if k)
    return {"n": n, "solutions": len(sols), "zero_overflow": ks.count(0),
            "smallest_nonzero_K": nz[0] if nz else None, "median_nonzero_K": statistics.median(nz) if nz else None,
            "zero_overflow_pairs": sorted((p, q) for p, q, k in sols if k == 0)}


def lift_branching(N: int, k: int) -> Dict[int, int]:
    """Children per unit solution when lifting from 10^k to 10^(k+1), as {children: count}."""
    kids = {(p, q): 0 for p, q, _ in unit_solutions(N, k)}
    M = 10 ** k
    for p, q, _ in unit_solutions(N, k + 1):
        kids[(p % M, q % M)] += 1
    out: Dict[int, int] = {}
    for v in kids.values():
        out[v] = out.get(v, 0) + 1
    return out


def primes_between(lo: int, hi: int) -> List[int]:
    return [x for x in range(lo, hi) if all(x % d for d in range(2, int(x ** .5) + 1))]


def run() -> dict:
    import random
    res: dict = {}
    rnd = random.Random(0)
    cases = [(0, 0), (1, 10 ** 10 - 1), (10 ** 10 - 1, 10 ** 10 - 1)] + [(rnd.randrange(10 ** 10), rnd.randrange(10 ** 10)) for _ in range(200)]
    res['matrix_cases'] = len(cases)
    res['matrix_bad'] = sum(carry_matrix(a, b)[1] != a * b for a, b in cases)
    res['max_carry'] = max(max(max(r) for r in carry_matrix(a, b)[0]) for a, b in cases[:60])
    nums = (1, 2, 3, 5, 7, 12, 25, 64, 625, 1000)
    res['period_pairs'] = len(nums) * 3
    res['period_bad'] = sum(column_period(a, c) != column_period_measured(a, c) for a in nums for c in range(3))
    n = bad = 0
    for m in (1, 2, 3):
        M = 10 ** m
        for a in range(1, M):
            if gcd(a, 10) != 1:
                continue
            for b in range(0, M, max(1, M // 40)):
                n += 1
                bad += not crt_rule_holds(a, b, m)
    res['crt_maps'], res['crt_bad'] = n, bad
    res['crt_example'] = (affine_cycle_type(3, 1, 1000), affine_cycle_type(3, 1, 8), affine_cycle_type(3, 1, 125))
    res['odometer'] = {m: odometer_first_return(m) for m in (2, 3, 4)}
    res['solenoid_pow2'] = all(l & (l - 1) == 0 for a in (1, 3, 5, 7, 11) for b in (0, 1, 3) for l in affine_cycle_type(a, b, 2 ** 8))
    res['nonunit_raises'] = False
    try:
        affine_cycle_type(4, 1, 100)
    except ValueError:
        res['nonunit_raises'] = True
    res['closed_bad'] = sum(solution_count(N, k) != solution_count_brute(N, k) for k in (1, 2, 3) for N in range(0, 2 * 10 ** k + 50))
    res['closed_checked'] = sum(2 * 10 ** k + 50 for k in (1, 2, 3))
    res['law_rows'] = [(N, n_, valuation(N, 2), valuation(N, 5), live_state_counts(N, n_), [solution_count(N, c + 1) for c in range(n_)])
                       for N, n_ in ((3233, 2), (14351, 3), (1022117, 4), (420, 2), (850, 2), (5100, 2))]
    res['law_agree'] = all(r[4][:r[1]] == r[5] for r in res['law_rows'])
    res['unit_orders'] = [unit_group_order(k) for k in (1, 2, 3, 4)]
    res['branching'] = (lift_branching(14351, 2), lift_branching(3233, 1))
    P3 = primes_between(101, 999)
    prof = [address_profile(p * q, 3) for p, q in (rnd.sample(P3, 2) for _ in range(30))]
    res['address'] = {"products": len(prof), "solutions": sorted({x['solutions'] for x in prof}), "zero": sorted({x['zero_overflow'] for x in prof}),
                      "min_smallest_nonzero": min(x['smallest_nonzero_K'] for x in prof), "max_smallest_nonzero": max(x['smallest_nonzero_K'] for x in prof),
                      "median_median": statistics.median(x['median_nonzero_K'] for x in prof)}
    # partial knowledge: survivors by column when the low k digits of p are known
    N, p = 1009 * 1013, 1009
    res['known_low_digits'] = {k: [sum(1 for pp, _, _ in unit_solutions(N, c + 1) if pp % 10 ** k == p % 10 ** k) if c + 1 >= k else None for c in range(4)] for k in (1, 2, 3)}
    return res


def crosscheck() -> dict:
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.environ.get("VQ_PATH", ""), os.path.join(here, "..", "..", "..")):
        if cand and os.path.isdir(os.path.join(cand, "ValaQuenta")):
            sys.path.insert(0, cand)
            break
    else:
        return {"found": False}
    from ValaQuenta.modules.addition_matrix import maths as VQ
    me = sys.modules[__name__]
    grid = [(N, k) for N in range(0, 400) for k in (1, 2, 3)]
    return {"found": True,
            "closed_form_equal": all(me.solution_count(N, k) == VQ.solution_count_closed(N, k) for N, k in grid),
            "live_states_equal": all(me.live_state_counts(N, n) == VQ.live_state_counts(N, n) for N, n in ((3233, 2), (14351, 3), (420, 2))),
            "address_equal": me.address_profile(10403, 3) == {k: v for k, v in VQ.address_profile(10403, 3).items() if k in me.address_profile(10403, 3)}}


if __name__ == "__main__":
    if "--crosscheck" in sys.argv:
        print(crosscheck())
    else:
        r = run()
        for k, v in r.items():
            print(f"{k}: {v}")
