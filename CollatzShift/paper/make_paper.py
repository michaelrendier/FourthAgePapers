#!/usr/bin/env python3
"""
make_paper.py: builds A_Bit_Shift_Wearing_A_Disguise.md from the engines in ../engine.

Every number in the paper that comes from code is taken from a run of that code when this script runs (nothing is typed in by hand), every
listing is extracted verbatim from the engine source and executed cold before it is printed, and the engine files' SHA-256 prefixes are
printed in the paper. `python3 make_paper.py --check` regenerates in memory and reports whether the committed paper still matches
(the date line is ignored): the "perpetual now" check of the cs-paper-code-conventions skill, enforced by machine.
"""
from __future__ import annotations

import ast
import contextlib
import hashlib
import io
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE.parent / 'engine'
sys.path.insert(0, str(ENGINE))
import e_collatz_shift as cs                       # noqa: E402
import e_collatz_bl_replication as bl              # noqa: E402
import e_collatz_gl_decomposition as gl            # noqa: E402

OUT = HERE / 'A_Bit_Shift_Wearing_A_Disguise.md'
CP = 'https://github.com/michaelrendier/ContextPlease'


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def extract(path: Path, names: list[str]) -> str:
    src = path.read_text()
    tree = ast.parse(src)
    parts = []
    for n in names:
        node = next(x for x in tree.body if isinstance(x, (ast.FunctionDef, ast.ClassDef)) and x.name == n)
        parts.append(ast.get_source_segment(src, node))
    return '\n\n\n'.join(parts)


def run_cold(code: str, call: str) -> str:
    """Execute a listing in an empty namespace and return what `call` prints (the transcript shown under it)."""
    ns: dict = {}
    exec(code, ns)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(call, ns)
    return buf.getvalue().rstrip()


def capture(fn, *a, **k) -> str:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(*a, **k)
    return buf.getvalue().rstrip()


def lab(prov: str) -> str:
    """map the original engine's provenance string to this paper's label"""
    return 'OURS:CALCULATED' if prov.startswith('OURS') else 'ESTABLISHED:CALCULATED'


def build() -> str:
    t0 = time.time()
    rel = {r[0]: r for r in cs.run(verbose=False)['relations']}
    lineage = cs.run(verbose=False)['lineage']
    B = bl.run(verbose=False, n_cycles=16, n_fixed=100)
    G = gl.run(verbose=False)
    if 'skipped' in G:
        raise SystemExit('GenerationalLineage not found: ' + G['skipped'])
    csp, blp, glp = ENGINE / 'e_collatz_shift.py', ENGINE / 'e_collatz_bl_replication.py', ENGINE / 'e_collatz_gl_decomposition.py'

    L1 = ('from __future__ import annotations\nfrom fractions import Fraction\nfrom typing import Tuple\n\n\n'
          + extract(csp, ['T', 'parity_vector', 'branch_affine']))
    T1 = run_cold(L1, "print('T(7), T(8) =', T(7), T(8)); print('parity_vector(7, 4) =', parity_vector(7, 4), '(binary', format(parity_vector(7, 4), '04b')[::-1] + ', low bit first)')\n"
                      "d, slope, c = branch_affine(4, 7); print('class 7 mod 16: d =', d, ' slope =', slope, ' c =', c, ' i.e. T^4(n) = (%d n + %s)/16' % (3 ** d, c * 16))")
    L2 = extract(blp, ['odd_fixed_points_dfs'])
    T2 = run_cold(L2, "c = odd_fixed_points_dfs(20); print({n: c[n] for n in (2, 5, 10, 15, 20)})")
    L3 = 'def T(n): return n // 2 if n % 2 == 0 else (3 * n + 1) // 2   # as in Listing 1\n\n\n' + extract(glp, ['duval_count', 'stream_to_one'])
    T3 = run_cold(L3, "s = stream_to_one(27); print(len(s), 'parities to reach 1:', ''.join(map(str, s))); print('Lyndon factors of that stream:', duval_count(''.join(map(str, s))))")

    ex_cs = capture(cs.run, True)
    ex_head = '\n'.join(l for l in ex_cs.splitlines() if 'relations hold' in l or l.startswith('collatz.'))
    ex_bl = capture(bl.run, True, 16, 100)
    ex_gl = capture(gl.run, True)

    blocks = {}
    for blk in re.split(r'\n(?=collatz\.[a-z_0-9]+ +\[tier)', ex_cs):
        m = re.match(r'(collatz\.[a-z_0-9]+) +\[tier', blk)
        if m:
            blocks[m.group(1)] = blk.strip()

    def R(name: str) -> str:
        r = rel[name]
        return f"**[{lab(r[3])}]**\n\n```\n{blocks[name]}\n```"

    odd_fp = B['odd_fixed_points']
    mm23, mm24 = B['table_2_3_mismatches'], B['table_2_4_mismatches']
    sq = {k: v for k, v in G['B_first_collision'].items()}
    dz = G['D_mean_z_odd_starts']
    fe = G['D_first_bit_effect']
    pm = sum(1 for k in range(1, 201) for d in range(0, 201) if abs(2 ** k - 3 ** d) == 1)
    pm_list = [(k, d) for k in range(1, 201) for d in range(0, 201) if abs(2 ** k - 3 ** d) == 1]
    lin_rows = '\n'.join(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |" for r in lineage)
    hashes = '\n'.join(f"| `engine/{p.name}` | `{sha(p)}` |" for p in (csp, blp, glp))
    glver = 'GenerationalLineage 1.0.0 (git 4892eaf, 2026-09-28)'

    md = TEMPLATE
    subs = {
        'DATE': time.strftime('%d %B %Y').lstrip('0'),
        'L1': L1, 'T1': T1, 'L2': L2, 'T2': T2, 'L3': L3, 'T3': T3,
        'EX_CS': ex_head, 'EX_BL': ex_bl, 'EX_GL': ex_gl,
        'R1': R('collatz.affine_on_classes'), 'R2': R('collatz.parity_bijection'), 'R3': R('collatz.shift_conjugacy'),
        'R4': R('collatz.pascal_refinement'), 'R5': R('collatz.gaussian_from_pascal'), 'R6': R('collatz.cycle_denominator'),
        'R7': R('collatz.mod3_orphans'), 'R8': R('collatz.forward_two_to_one'), 'R9': R('collatz.backward_deficit'), 'R10': R('collatz.drift_at_half'),
        'LINEAGE_ROWS': lin_rows, 'HASHES': hashes, 'GLVER': glver,
        'MM23': ', '.join(map(str, mm23)), 'N_MM23': str(len(mm23)), 'MM24': ', '.join(map(str, mm24)),
        'N_OK23': str(99 - len(mm23)), 'N_OK24': str(100 - len(mm24)),
        'SHIFT': 'every one of them' if B['mismatch_is_a_one_cell_shift'] else 'not all of them',
        'FP10': str(odd_fp[10]), 'FP100': str(odd_fp[100]), 'FP200': str(odd_fp[200]), 'FP500': str(odd_fp[500]), 'FP1000': str(odd_fp[1000]),
        'ORD_OK': 'holds for every n from 6 to 16' if B['order_is_2^(n-4)_for_n>=6'] else 'FAILS for some n',
        'SOL': str(B['solenoidal_violations']),
        'A_CLASSES': str(G['A_classes_checked']), 'A_BAD': str(G['A_mismatches']),
        'FIRST_COLL': '; '.join(f"n = {n}: {v[0]} steps to reach 1, first value to repeat is {v[3]:g}, at step {v[2]}" for n, v in sq.items()),
        'RM': '; '.join(f"(k,d) = {k}: {a} rotation-minimal vs {b} primitive" for k, (a, b) in G['C_rotation_minimal_vs_primitive'].items()),
        'FB_FREE': f'{fe[0]:.2f}', 'FB_ONE': f'{fe[1]:.2f}', 'FB_ZERO': f'{fe[2]:.2f}',
        'Z_UN': f"{dz['unmatched']:+.2f}", 'Z_FB': f"{dz['first bit matched']:+.2f}", 'Z_BOTH': f"{dz['first bit and last 6 bits matched']:+.2f}",
        'Z_EVEN': f"{G['D_mean_z_even_starts_matched']:+.2f}",
        'PM': str(pm), 'PM_LIST': ', '.join(f'({k},{d})' for k, d in pm_list),
        'RUNTIME': f'{time.time() - t0:.0f}',
    }
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
        strip = lambda s: re.sub(r'\*\*Date:\*\*[^\n]*\n', '', s)
        print('paper matches a fresh build:', strip(cur) == strip(md))
        return
    OUT.write_text(md)
    print('wrote', OUT, len(md), 'chars')


if __name__ == '__main__':
    main()
