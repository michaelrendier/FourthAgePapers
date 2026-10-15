#!/usr/bin/env python3
"""
make_paper.py: builds The_Addition_Matrix_as_Rotors.md from ../engine/e_addm_orbits.py.

Every number from code in the paper is taken from a fresh run when this script runs, every listing is extracted verbatim from the engine
source and executed cold before it is printed, and the engine file's SHA-256 prefix is printed in the paper. `--check` regenerates in
memory and reports whether the committed paper still matches (date and build-time lines ignored).
"""
from __future__ import annotations

import ast
import contextlib
import hashlib
import io
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE.parent / 'engine'
sys.path.insert(0, str(ENGINE))
import e_addm_orbits as E                          # noqa: E402
import e_addm_followup as F                        # noqa: E402

OUT = HERE / 'The_Addition_Matrix_as_Rotors.md'


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def extract(path: Path, names: list[str]) -> str:
    src = path.read_text()
    tree = ast.parse(src)
    return '\n\n\n'.join(ast.get_source_segment(src, next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == n)) for n in names)


def run_cold(code: str, call: str) -> str:
    ns: dict = {}
    exec(code, ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(call, ns)
    return buf.getvalue().rstrip()


def build() -> str:
    t0 = time.time()
    eng, fol = ENGINE / 'e_addm_orbits.py', ENGINE / 'e_addm_followup.py'
    R = E.run()
    TA, CF, TO = F.self_check_treeaut(), F.self_check_closedform(), F.self_check_torsor()
    tree_rows = []
    for n, lv, tr in ((3, 2, 200), (3, 3, 200), (4, 2, 200), (4, 3, 200), (4, 4, 100), (5, 3, 100), (5, 4, 100)):
        r = F.rank_test(n, lv, trials=tr, seed=11)
        mr, z = r['mean_rank'], r['z_vs_no_information']
        tree_rows.append(f"| {n} | {lv} | {tr} | {mr['overflow']:.3f} ({z['overflow']:+.1f}) | {mr['low']:.3f} ({z['low']:+.1f}) | {mr['random child']:.3f} ({z['random child']:+.1f}) |")
    L1 = 'from typing import List\n\n\n' + extract(eng, ['live_state_counts'])
    T1 = run_cold(L1, "print('>>> live_state_counts(14351, 3)'); print(live_state_counts(14351, 3))")
    L2 = 'from typing import Optional\n\n\n' + extract(eng, ['valuation', 'phi_prime_power', 'prime_power_solutions', 'solution_count'])
    T2 = run_cold(L2, "print('>>> [solution_count(14351, c + 1) for c in range(3)]'); print([solution_count(14351, c + 1) for c in range(3)])\n"
                      "print('>>> solution_count(420, 2), solution_count(420, 1)'); print(solution_count(420, 2), solution_count(420, 1))")
    L3 = 'from math import gcd\nfrom typing import List, Tuple\n\n\n' + extract(eng, ['unit_solutions'])
    T3 = run_cold(L3, "print('>>> sols = unit_solutions(101 * 103, 3); len(sols)'); sols = unit_solutions(101 * 103, 3); print(len(sols))\n"
                      "print('>>> [s for s in sols if s[2] == 0]'); print([s for s in sols if s[2] == 0])\n"
                      "print('>>> sorted(abs(s[2]) for s in sols if s[2])[:5]'); print(sorted(abs(s[2]) for s in sols if s[2])[:5])")
    law_rows = '\n'.join(f"| {N} | {v2} | {v5} | {live} | {cf} |" for N, n, v2, v5, live, cf in R['law_rows'])
    a = R['address']
    kd = R['known_low_digits']
    subs = {
        'DATE': time.strftime('%d %B %Y').lstrip('0'), 'RUNTIME': f'{time.time() - t0:.0f}',
        'MATRIX_CASES': str(R['matrix_cases']), 'MATRIX_BAD': str(R['matrix_bad']), 'MAX_CARRY': str(R['max_carry']),
        'PERIOD_PAIRS': str(R['period_pairs']), 'PERIOD_BAD': str(R['period_bad']),
        'CRT_MAPS': str(R['crt_maps']), 'CRT_BAD': str(R['crt_bad']),
        'CRT_EX_WHOLE': str(R['crt_example'][0]), 'CRT_EX_2': str(R['crt_example'][1]), 'CRT_EX_5': str(R['crt_example'][2]),
        'NONUNIT_RAISES': str(R['nonunit_raises']), 'ODOMETER': 'True' if all(R['odometer'].values()) else str(R['odometer']),
        'SOLENOID': 'True' if R['solenoid_pow2'] else 'False',
        'CLOSED_CHECKED': str(R['closed_checked']), 'CLOSED_BAD': str(R['closed_bad']),
        'UNIT_ORDERS': str(R['unit_orders']), 'BRANCHING': f"{R['branching'][0]} and {R['branching'][1]}",
        'LAW_ROWS': law_rows,
        'ADDR_PRODUCTS': str(a['products']), 'ADDR_SOLUTIONS': ', '.join(map(str, a['solutions'])), 'ADDR_ZERO': ', '.join(map(str, a['zero'])),
        'ADDR_MIN': str(a['min_smallest_nonzero']), 'ADDR_MAX': str(a['max_smallest_nonzero']), 'ADDR_MEDMED': f"{a['median_median']:.0f}",
        'KNOWN1': str(kd[1]).replace('None', '·'), 'KNOWN2': str(kd[2]).replace('None', '·'), 'KNOWN3': str(kd[3]).replace('None', '·'),
        'L1': L1, 'T1': T1, 'L2': L2, 'T2': T2, 'L3': L3, 'T3': T3,
        'CF_CASES': str(len(CF['prime_power_mismatches (every N)'])), 'CF_BAD': str(sum(1 for v in CF['prime_power_mismatches (every N)'].values() if v)),
        'CF_TEN': 'no mismatches' if all(v == 0 for d in (CF['ten_k_1_to_3_every_N'], CF['ten_k_4_5_selected_N']) for v in d.values()) else 'MISMATCHES',
        'AUT_BRUTE': str(TA['brute_force']), 'AUT_OK': str(TA['brute_equals_formula']), 'AUT_REC': str(TA['recursion'][4]),
        'AFF_TREE': str(TA['affine_maps_preserve_tree']), 'AFF_ORDER': str(TA['affine_group_order_2^(2n-1)']), 'AFF_POW2': str(TA['all_affine_cycle_lengths_powers_of_two_Z2^8']),
        'Z5': str(TA['Z5^m_cycle_lengths_of_x->2x+1']), 'TREE_BRANCH': f"{TO['branching_k1']} and {TO['branching_k2']}",
        'TREE_ROWS': '\n'.join(tree_rows), 'PRUNE': str(tuple(x[2] for x in TO['pruning_N14351'])),
        'HASHES': f"| `engine/{eng.name}` | `{sha(eng)}` |\n| `engine/{fol.name}` | `{sha(fol)}` |",
    }
    md = TEMPLATE
    for k, v in subs.items():
        md = md.replace('@@' + k + '@@', v)
    left = re.findall(r'@@[A-Z0-9_]+@@', md)
    if left:
        raise SystemExit('unfilled placeholders: ' + ', '.join(sorted(set(left))))
    return md


TEMPLATE = (HERE / 'template.md').read_text()


def main() -> None:
    md = build()
    if '--check' in sys.argv:
        cur = OUT.read_text() if OUT.exists() else ''
        strip = lambda s: re.sub(r'building the paper took about \d+ s', '', re.sub(r'\*\*Date:\*\*[^\n]*\n', '', s))
        print('paper matches a fresh build:', strip(cur) == strip(md))
        return
    OUT.write_text(md)
    print('wrote', OUT, len(md), 'chars')


if __name__ == '__main__':
    main()
