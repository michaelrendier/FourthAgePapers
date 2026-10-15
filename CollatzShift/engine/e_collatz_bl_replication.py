#!/usr/bin/env python3
"""
e_collatz_bl_replication.py: re-compute the numerical tables of Bernstein & Lagarias (1996)

    D. J. Bernstein, J. C. Lagarias, "The 3x+1 conjugacy map", Canad. J. Math. 48 (1996), 1154-1169.
    (copies in ../references/; the numbers below were transcribed from that paper's Tables 2.2, 2.3, 2.4)

and compare. Stdlib only. Deterministic. Nothing is fitted; every comparison is exact integer equality.

What is computed
  Q_n(x) = sum_{i<n} (T^i(x) mod 2) 2^i   the parity vector, a permutation of Z/2^n (Bernstein-Lagarias eq. (1.5): Q_n = (Phi mod 2^n)^(-1)).
  A. the cycle lengths of Q_n on the ODD residues, n = 2..N, against Table 2.2 (number of cycles of each length 2^j);
  B. the order of Q_n (n >= 6 should be 2^(n-4)) and that every cycle length is a power of two;
  C. the solenoidal property Q_n(x) = Q_(n-1)(x) mod 2^(n-1) for all x;
  D. the number of odd fixed points of Q_n against Tables 2.3 (n <= 100) and 2.4 (n = 100, 110, ..., 200 here; the paper goes to 1000),
     by extending only odd fixed points one bit at a time (exact: a fixed point mod 2^(n+1) reduces to one mod 2^n).

Status of the claims: the tables and theorems are ESTABLISHED (Bernstein-Lagarias 1996). What this file adds is ONLY that the
numbers come out of this code, which is a check on the code (and on our reading of the paper), not a new result.
"""
from __future__ import annotations

import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e_collatz_shift import T  # the shortcut map, defined once in the original engine

# ---- Table 2.2, p. 5: TABLE_2_2[n][j] = number of cycles of length 2^j of Phi-hat_n (the map on odd residues mod 2^n) ----
TABLE_2_2 = {
    2: [2],
    3: [2, 1],
    4: [4, 2],
    5: [6, 3, 1],
    6: [6, 7, 3],
    7: [8, 10, 3, 3],
    8: [14, 17, 8, 0, 3],
    9: [14, 21, 18, 4, 0, 3],
    10: [10, 35, 24, 14, 2, 0, 3],
    11: [12, 40, 37, 18, 12, 2, 0, 3],
    12: [16, 48, 70, 23, 16, 10, 2, 0, 3],
    13: [26, 53, 79, 60, 24, 11, 10, 2, 0, 3],
    14: [22, 63, 111, 98, 50, 14, 11, 10, 2, 0, 3],
    15: [18, 81, 129, 153, 84, 40, 11, 11, 10, 2, 0, 3],
    16: [20, 96, 179, 186, 137, 78, 31, 11, 11, 10, 2, 0, 3],
    17: [18, 91, 242, 236, 207, 131, 61, 29, 11, 11, 10, 2, 0, 3],
    18: [12, 104, 305, 308, 312, 192, 105, 56, 29, 11, 11, 10, 2, 0, 3],
    19: [16, 86, 375, 401, 432, 307, 152, 99, 54, 29, 11, 11, 10, 2, 0, 3],
    20: [26, 95, 424, 573, 564, 445, 281, 133, 91, 54, 29, 11, 11, 10, 2, 0, 3],
}

# ---- Table 2.3, p. 4: number of 1-cycles (odd fixed points) of Phi-hat_n, n = 2..100 ----
TABLE_2_3 = {
    2: 2, 3: 2, 4: 4, 5: 6, 6: 6, 7: 8,
    8: 14, 9: 14, 10: 10, 11: 12, 12: 16, 13: 26,
    14: 22, 15: 18, 16: 20, 17: 18, 18: 12, 19: 16,
    20: 26, 21: 32, 22: 38, 23: 36, 24: 38, 25: 36,
    26: 36, 27: 50, 28: 60, 29: 62, 30: 50, 31: 52,
    32: 54, 33: 56, 34: 54, 35: 54, 36: 54, 37: 68,
    38: 68, 39: 84, 40: 92, 41: 80, 42: 82, 43: 96,
    44: 106, 45: 116, 46: 90, 47: 82, 48: 92, 49: 102,
    50: 108, 51: 116, 52: 122, 53: 124, 54: 124, 55: 114,
    56: 128, 57: 118, 58: 94, 59: 92, 60: 100, 61: 106,
    62: 112, 63: 110, 64: 112, 65: 106, 66: 92, 67: 106,
    68: 116, 69: 122, 70: 132, 71: 152, 72: 144, 73: 120,
    74: 108, 75: 114, 76: 132, 77: 140, 78: 144, 79: 144,
    80: 144, 81: 124, 82: 124, 83: 130, 84: 128, 85: 128,
    86: 136, 87: 124, 88: 118, 89: 104, 90: 98, 91: 110,
    92: 108, 93: 108, 94: 92, 95: 96, 96: 96, 97: 102,
    98: 108, 99: 88, 100: 90,
}

# ---- Table 2.4, p. 5: number of 1-cycles of Phi-hat_n at n = 10, 20, ..., 1000 ----
TABLE_2_4 = {
    10: 10, 20: 26, 30: 50, 40: 92, 50: 108, 60: 100,
    70: 132, 80: 144, 90: 98, 100: 90, 110: 96, 120: 90,
    130: 116, 140: 156, 150: 240, 160: 278, 170: 282, 180: 320,
    190: 378, 200: 404, 210: 380, 220: 458, 230: 452, 240: 544,
    250: 574, 260: 588, 270: 628, 280: 634, 290: 784, 300: 714,
    310: 700, 320: 788, 330: 916, 340: 780, 350: 678, 360: 908,
    370: 818, 380: 784, 390: 870, 400: 892, 410: 844, 420: 840,
    430: 1134, 440: 942, 450: 874, 460: 910, 470: 866, 480: 932,
    490: 1060, 500: 1150, 510: 1278, 520: 1176, 530: 1000, 540: 914,
    550: 998, 560: 1110, 570: 1172, 580: 1172, 590: 1072, 600: 1086,
    610: 1078, 620: 1130, 630: 1212, 640: 1270, 650: 1462, 660: 1476,
    670: 1360, 680: 1358, 690: 1190, 700: 1208, 710: 1330, 720: 1142,
    730: 1170, 740: 1240, 750: 1346, 760: 1538, 770: 1562, 780: 1778,
    790: 1974, 800: 1808, 810: 1944, 820: 2180, 830: 2194, 840: 2226,
    850: 2130, 860: 2294, 870: 2204, 880: 2184, 890: 2114, 900: 2056,
    910: 2030, 920: 2162, 930: 2230, 940: 2128, 950: 2206, 960: 2362,
    970: 2354, 980: 2362, 990: 2242, 1000: 2308,
}


def parity_vector(x: int, n: int) -> int:
    """Q_n(x): the first n parities of the orbit of x under T, packed little-endian."""
    v, m = 0, x
    for i in range(n):
        v |= (m & 1) << i
        m = T(m)
    return v


def odd_cycle_counts(n: int) -> list[int]:
    """counts[j] = number of cycles of length 2^j of Q_n restricted to the odd residues mod 2^n (any other length raises)."""
    seen, counts = set(), {}
    for x in range(1, 1 << n, 2):
        if x in seen:
            continue
        L, m = 0, x
        while m not in seen:
            seen.add(m)
            m = parity_vector(m, n)
            L += 1
        counts[L] = counts.get(L, 0) + 1
    if any(L & (L - 1) for L in counts):
        raise ValueError(f'n={n}: a cycle length that is not a power of two: {sorted(counts)}')
    top = max(L.bit_length() - 1 for L in counts)
    return [counts.get(1 << j, 0) for j in range(top + 1)]


def odd_fixed_point_counts(N: int) -> dict[int, int]:
    """Odd fixed points of Q_n for n = 1..N, extending only odd fixed points one bit at a time."""
    frontier, out = [1], {}
    for n in range(1, N + 1):
        fp = [x for x in frontier if parity_vector(x, n) == x]
        out[n] = len(fp)
        frontier = fp + [x + (1 << n) for x in fp]
    return out


def odd_fixed_points_dfs(N: int) -> dict[int, int]:
    """A second, independent algorithm for the same counts (n up to 1000 in about 2 s).

    For a fixed point x of Q_n the parity of T^j(x) must equal bit j of x. Along the parity word (which is the low bits of x)
    T^j(x) = (3^d x + c) / 2^j, and the parity of T^j(x) equals f_j XOR x_j, where f_j = ((3^d x_low + c) / 2^j) mod 2 depends only on
    the bits of x below j. So bit j is free when f_j = 0 and the branch dies when f_j = 1. Counts the surviving residues at each n."""
    p3 = [1]
    nodes = [(1, 1, 1)]                      # x_0 = 1 (odd): x_low = 1, d = 1 odd step, c = 1
    counts = {1: 1}
    for j in range(1, N):
        nxt = []
        for x_low, d, c in nodes:
            while len(p3) <= d:
                p3.append(p3[-1] * 3)
            if ((p3[d] * x_low + c) >> j) & 1:
                continue
            nxt.append((x_low, d, c))                                      # bit j = 0: even step, c unchanged
            nxt.append((x_low | (1 << j), d + 1, 3 * c + (1 << j)))        # bit j = 1: odd step
        nodes = nxt
        counts[j + 1] = len(nodes)
    return counts


def window_audit(lo: int = 60, hi: int = 80) -> dict:
    """Chase of the disagreement window. (1) SOUNDNESS: every odd fixed point listed at each n in [lo, hi] is checked by plain iteration of T
    (Q_n(x) == x); completeness rests on the lifting lemma (a fixed point mod 2^(n+1) reduces to one mod 2^n), which both algorithms use.
    (2) The printed Table 2.3 block against ours as multisets: a single deletion plus a single duplication would leave exactly one value only
    in ours and one only in theirs."""
    frontier, listed = [1], {}
    for n in range(1, hi + 1):
        fp = [x for x in frontier if parity_vector(x, n) == x]
        listed[n] = fp
        frontier = fp + [x + (1 << n) for x in fp]
    unsound = [(n, x) for n in range(lo, hi + 1) for x in listed[n] if parity_vector(x, n) != x or x % 2 == 0]
    ours = sorted(len(listed[n]) for n in range(66, min(hi, 80) + 1))
    printed = sorted(TABLE_2_3[n] for n in range(66, min(hi, 80) + 1))
    from collections import Counter
    co, cp = Counter(ours), Counter(printed)
    return {'n_residues_checked': sum(len(listed[n]) for n in range(lo, hi + 1)), 'unsound': unsound,
            'only_in_ours': sorted((co - cp).elements()), 'only_in_printed': sorted((cp - co).elements())}


def run(verbose: bool = True, n_cycles: int = 16, n_fixed: int = 100) -> dict:
    """n_cycles: largest n for the cycle table (Table 2.2 goes to 20; 18 takes about a minute). n_fixed: largest n for fixed points (200 compares Table 2.4 too)."""
    res = {'label': 'ESTABLISHED:CALCULATED (Bernstein-Lagarias 1996, re-computed)'}
    # A and B
    rows, mism = [], []
    for n in range(2, n_cycles + 1):
        mine = odd_cycle_counts(n)
        ok = mine == TABLE_2_2[n]
        order = 1
        for j, c in enumerate(mine):
            if c:
                order = order * (1 << j) // gcd(order, 1 << j)
        rows.append((n, mine, ok, order))
        if not ok:
            mism.append(n)
    res['table_2_2_rows_checked'] = len(rows)
    res['table_2_2_mismatches'] = mism
    res['orders'] = {n: order for n, _, _, order in rows}
    res['order_is_2^(n-4)_for_n>=6'] = all(order == 1 << (n - 4) for n, _, _, order in rows if n >= 6)
    # C
    viol = 0
    for n in range(2, min(n_cycles, 14) + 1):
        for x in range(1 << n):
            if parity_vector(x, n) % (1 << (n - 1)) != parity_vector(x % (1 << (n - 1)), n - 1):
                viol += 1
    res['solenoidal_violations'] = viol
    # D: two algorithms for the odd fixed-point counts, then the printed tables
    fp = odd_fixed_point_counts(n_fixed)
    dfs = odd_fixed_points_dfs(1000)
    res['two_algorithms_agree_to_n'] = n_fixed if all(fp[n] == dfs[n] for n in range(1, n_fixed + 1)) else None
    res['table_2_3_checked'] = 99
    res['table_2_3_mismatches'] = [n for n in range(2, 101) if dfs[n] != TABLE_2_3[n]]
    res['table_2_4_checked'] = len(TABLE_2_4)
    res['table_2_4_mismatches'] = [n for n in sorted(TABLE_2_4) if dfs[n] != TABLE_2_4[n]]
    res['mismatch_is_a_one_cell_shift'] = (
        all(TABLE_2_3[n] == dfs[n + 1] for n in res['table_2_3_mismatches'])
        and all(TABLE_2_4[n] == dfs[n + 1] for n in res['table_2_4_mismatches']))
    res['q_lineage_vs_printed_beyond_100'] = (
        [n for n in TABLE_2_4 if 100 < n <= n_fixed and fp[n] != TABLE_2_4[n]] if n_fixed > 100 else 'not run (use --full)')
    res['odd_fixed_points'] = {n: dfs[n] for n in (10, 20, 30, 40, 50, 100, 200, 500, 1000)}
    res['window_audit'] = window_audit(60, 80)
    res['label'] = 'ESTABLISHED:CALCULATED (Bernstein-Lagarias 1996, re-computed), with ONE RECORDED DISCREPANCY WINDOW in the printed tables (see mismatch lists)'
    if verbose:
        print('Bernstein-Lagarias (1996) replication', '(' + res['label'] + ')')
        print(f"  Table 2.2 (cycle lengths on the odd residues): rows n=2..{n_cycles} compared, mismatches: {res['table_2_2_mismatches'] or 'none'}")
        print('  n   cycles by length (1,2,4,...)                      order')
        for n, mine, ok, order in rows:
            print(f"  {n:2d}  {str(mine):52s} {order}{'' if ok else '   <-- DIFFERS from Table 2.2: ' + str(TABLE_2_2[n])}")
        print(f"  order == 2^(n-4) for every n >= 6 checked: {res['order_is_2^(n-4)_for_n>=6']}; every cycle length a power of two: True (checked while counting)")
        print(f"  solenoidal property Q_n(x) = Q_(n-1)(x) mod 2^(n-1): violations {viol}")
        print(f"  odd fixed points: Q-lineage (n<={n_fixed}) and the independent DFS agree: {res['two_algorithms_agree_to_n'] == n_fixed}")
        print(f"  Table 2.3 (n=2..100, 99 values) vs DFS: mismatches at n = {res['table_2_3_mismatches'] or 'none'}")
        print(f"  Table 2.4 (n=10,20,...,1000, {res['table_2_4_checked']} values) vs DFS: mismatches at n = {res['table_2_4_mismatches'] or 'none'}")
        print(f"  every mismatching printed entry equals the computed value at n+1 (a one-cell shift in the printed table): {res['mismatch_is_a_one_cell_shift']}")
        print('  odd fixed points at n =', res['odd_fixed_points'])
        wa = res['window_audit']
        print(f"  window audit n=60..80: {wa['n_residues_checked']} listed odd fixed points re-checked by plain iteration of T, unsound: {wa['unsound'] or 'none'}; printed block n=66..80 vs ours as multisets: only in ours {wa['only_in_ours']}, only in the printed table {wa['only_in_printed']}")
    return res


if __name__ == '__main__':
    full = '--full' in sys.argv
    run(True, n_cycles=18 if full else 16, n_fixed=200 if full else 100)
