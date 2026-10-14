#!/usr/bin/env python3
"""
e_collatz_gl_decomposition.py: the Collatz map read through the GenerationalLineage engine, and the control that went wrong.

Needs the GenerationalLineage repository (https://github.com/michaelrendier/GenerationalLineage) next to this one, or GL_PATH set to its
directory. Without it this file reports SKIPPED and computes nothing (no silent substitute).

  A. Each branch of the shortcut map written as an ASS element (x -> sign*scale*x + add): even = SCALE(1/2), odd = ADD(1/2) after SCALE(3/2).
     The engine's SIGN (a +-1 reflection) occurs in neither branch; the paper's "SIGN" is the parity SELECTOR. Composing the branch elements
     along the true parity word reproduces T^k on every residue class mod 2^k (k <= 12, 8190 classes), slope 3^d/2^k exactly.   [THEORETICAL:CALCULATED]
  B. The engine's Long-Path memory (set membership, the rule that decides Recaman's flip) on Collatz orbits: the first repeated value.  [THEORETICAL:CALCULATED]
  C. The engine's Lyndon tool against the rotation-minimal filter that produced the first fault of the original paper.                [OURS:CALCULATED]
  D. THE CONTROL THAT WENT WRONG (kept). The Lyndon-factor count of the parity streams looked higher than random; chased to its source:
     (1) every start was odd, so every stream began with 1, and a leading 1 raises the count for random bits too; (2) streams that reach 1 end in
     a nearly forced tail. Matched on both, the excess is gone. Classification: METHOD error (control not matched on the conditioning).  [OURS:CALCULATED]
"""
from __future__ import annotations

import importlib.util
import os
import random
import statistics as st
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e_collatz_shift import T, parity_word  # defined once, in the original engine


def load_gl():
    """Load GenerationalLineage's `engine` package under the alias gl_engine (its own imports are relative). None if absent."""
    root = Path(os.environ.get('GL_PATH', Path(__file__).resolve().parents[3] / 'GenerationalLineage'))
    init = root / 'engine' / '__init__.py'
    if not init.exists():
        return None
    spec = importlib.util.spec_from_file_location('gl_engine', init, submodule_search_locations=[str(init.parent)])
    mod = importlib.util.module_from_spec(spec)
    sys.modules['gl_engine'] = mod
    spec.loader.exec_module(mod)
    return mod


def duval_count(s: str) -> int:
    """Number of factors in the Lyndon factorisation of s (Duval's algorithm)."""
    n, i, c = len(s), 0, 0
    while i < n:
        j, k = i + 1, i
        while j < n and s[k] <= s[j]:
            k = i if s[k] < s[j] else k + 1
            j += 1
        while i <= k:
            i += j - k
            c += 1
    return c


def stream_to_one(n: int) -> list[int]:
    """Parities along the orbit of n, up to (not including) the step taken at 1."""
    out, m = [], n
    while m != 1:
        out.append(m & 1)
        m = T(m)
    return out


def run(verbose: bool = True, starts: int = 100, draws: int = 150) -> dict:
    gl = load_gl()
    if gl is None:
        msg = 'SKIPPED: GenerationalLineage not found (set GL_PATH to its directory). Nothing was computed.'
        if verbose:
            print(msg)
        return {'skipped': msg}
    from gl_engine.add_scale_sign import ASS, ASSWord, CAMSHAFT, compose
    from gl_engine.toolsets import lyndon
    res: dict = {}
    # ---- A
    EVEN, ODD = ASS(add=0.0, scale=0.5, sign=1), ASS(add=0.5, scale=1.5, sign=1)
    res['A_sign_in_either_branch'] = EVEN.sign == -1 or ODD.sign == -1
    res['A_odd_is_ADD_after_SCALE'] = (ASS.ADD(0.5) @ ASS.SCALE(1.5)) == ODD
    bad = n_classes = 0
    for k in range(1, 13):
        for j in range(1 << k):
            w = parity_word(j, k)
            el = ASS.SCALE(1.0)
            for b in w:
                el = (ODD if b else EVEN) @ el
            n_classes += 1
            m = n = j + 3 * (1 << k)
            for _ in range(k):
                m = T(m)
            if el.scale != 3 ** sum(w) / 2 ** k or abs(el(float(n)) - m) > 1e-6 * max(1, m):
                bad += 1
    res['A_classes_checked'], res['A_mismatches'] = n_classes, bad
    res['A_camshaft'] = CAMSHAFT
    # ---- B
    first = {}
    for n in (27, 97, 871, 6171, 77031):
        steps, m = [], n
        while m != 1:
            steps.append(ODD if m & 1 else EVEN)
            m = T(m)
        w = ASSWord(steps=tuple(steps) + (ODD, EVEN), order='collatz', source=compose(*steps))      # at 1: ODD (to 2), then EVEN (back to 1)
        col = w.collisions(float(n), tol=0)
        first[n] = (len(steps), col[0][0], col[0][1], col[0][2])
    res['B_first_collision'] = first          # n -> (steps to reach 1, step of first visit, step of the revisit, repeated value)
    # ---- C
    rng = random.Random(14102026)
    disagreements = 0
    for _ in range(100):
        s = ''.join(rng.choice('01') for _ in range(rng.randint(5, 120)))
        disagreements += duval_count(s) != lyndon.descend(s)['omega']
    res['C_duval_vs_engine_disagreements'] = disagreements
    def n_rotation_minimal(k, d):
        return len({min(w[i:] + w[:i] for i in range(k)) for w in (format(x, f'0{k}b') for x in range(1 << k)) if w.count('1') == d})
    def n_primitive(k, d):
        return sum(1 for w in (format(x, f'0{k}b') for x in range(1 << k)) if w.count('1') == d and lyndon.descend(w)['omega'] == 1)
    res['C_rotation_minimal_vs_primitive'] = {(k, d): (n_rotation_minimal(k, d), n_primitive(k, d)) for k, d in ((4, 2), (6, 3), (8, 4))}
    # ---- D
    def rb(N, first=None, last=None):
        b = [rng.randint(0, 1) for _ in range(N)]
        if first is not None:
            b[0] = first
        if last:
            b[-len(last):] = list(last)
        return b
    om = lambda bits: duval_count(''.join(map(str, bits)))
    free = [om(rb(115)) for _ in range(4000)]
    one = [om(rb(115, first=1)) for _ in range(4000)]
    zero = [om(rb(115, first=0)) for _ in range(4000)]
    res['D_first_bit_effect'] = (st.mean(free), st.mean(one), st.mean(zero))
    rows = {'unmatched': [], 'first bit matched': [], 'first bit and last 6 bits matched': []}
    for n in random.Random(5).sample(range(3, 200001, 2), starts):
        s = stream_to_one(n)
        N, tail, w = len(s), s[-6:], om(s)
        for name, mk in (('unmatched', lambda: rb(N)), ('first bit matched', lambda: rb(N, first=1)), ('first bit and last 6 bits matched', lambda: rb(N, first=1, last=tail))):
            c = [om(mk()) for _ in range(draws)]
            rows[name].append((w - st.mean(c)) / (st.pstdev(c) or 1.0))
    res['D_mean_z_odd_starts'] = {k: st.mean(v) for k, v in rows.items()}
    ev = []
    for n in random.Random(6).sample(range(4, 200001, 2), starts // 2):
        s = stream_to_one(n)
        N, tail, w = len(s), s[-6:], om(s)
        c = [om(rb(N, first=0, last=tail)) for _ in range(draws)]
        ev.append((w - st.mean(c)) / (st.pstdev(c) or 1.0))
    res['D_mean_z_even_starts_matched'] = st.mean(ev)
    res['D_classification'] = 'METHOD error: the control was not matched on the conditioning (odd start, forced approach to 1); the excess vanishes when it is.'
    res['label'] = 'A,B: THEORETICAL:CALCULATED; C,D: OURS:CALCULATED'
    if verbose:
        print('Collatz through GenerationalLineage   [' + res['label'] + ']')
        print(f"  A. branch elements: even = {EVEN}, odd = {ODD}; engine SIGN (+-1) in either branch: {res['A_sign_in_either_branch']}; odd = ADD(1/2) after SCALE(3/2): {res['A_odd_is_ADD_after_SCALE']}")
        print(f"     composing the branch elements along the true parity word: {n_classes} classes (k <= 12), mismatches {bad}; engine firing order (innermost first): {CAMSHAFT}")
        print('  B. Long-Path memory (n: steps to 1, first visit step, revisit step, repeated value):', first)
        print(f"  C. Duval vs engine Lyndon omega on 100 random strings, disagreements: {disagreements}; rotation-minimal vs primitive words (k,d): {res['C_rotation_minimal_vs_primitive']}")
        f, o, z = res['D_first_bit_effect']
        print(f'  D. Lyndon factors of 115 random bits: first bit free {f:.2f}, first bit 1 {o:.2f}, first bit 0 {z:.2f}')
        print(f"     mean z of the Collatz streams to 1 ({starts} odd starts): " + ', '.join(f'{k} {v:+.2f}' for k, v in res['D_mean_z_odd_starts'].items()) + f"; even starts, matched: {res['D_mean_z_even_starts_matched']:+.2f}")
        print('     ' + res['D_classification'])
    return res


if __name__ == '__main__':
    run(True)
