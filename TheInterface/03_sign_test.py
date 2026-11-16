#!/usr/bin/env python3
"""Sign test: which imaginary axis (if any) of the sedenion acts as SIGN (theta -> -theta, conjugation)?

Written 2026-11-16. Run cold from this directory:  python3 03_sign_test.py
Uses only GenerationalLineage `engine.lineage.cd_mul`. No literature. Nothing is fitted: the product is asked three questions and the answers are printed.
Candidates named by Cody: e_8 (first imaginary of the second octonion, the doubling unit) versus the last imaginary of the first octonion, e_7 (and e_1 as a control).

  A  conjugation-by-axis table: for each axis k, the sign pattern s_k(j) in (e_k e_j) e_k^-1 = s_k(j) e_j, over all 16 basis elements.
     Is any axis's pattern the half-grading character (+1 on e_0..e_7, -1 on e_8..e_15)?
  B  the doubling identity: in the CD construction e_k x = x* e_k for x in the lower octonion {e_0..e_7} (x* = conjugate). Which axes satisfy it for every lower x?
  C  circle reversal: for how many directions u does conjugation by e_k send the circle exp(t u) to exp(-t u) (i.e. (e_k u) e_k^-1 = -u)?
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'GenerationalLineage'))
from engine.lineage import cd_mul
D = 16
def e(k): v = [0.0] * D; v[k] = 1.0; return v
def conj(x): return [x[0]] + [-t for t in x[1:]]
def mul(x, y): return cd_mul(list(x), list(y))
def neg(x): return [-t for t in x]
def eq(x, y): return all(abs(a - b) < 1e-12 for a, b in zip(x, y))
inv = lambda k: neg(e(k))                       # e_k^-1 = -e_k for every imaginary unit (e_k^2 = -1)

print("A  conjugation-by-axis pattern s_k(j) over j=0..15  (+ means (e_k e_j) e_k^-1 = +e_j)")
grading = [1] * 8 + [-1] * 8
hits = []
for k in range(1, 16):
    pat = []
    for j in range(D):
        r = mul(mul(e(k), e(j)), inv(k))
        pat.append(1 if eq(r, e(j)) else -1 if eq(r, neg(e(j))) else 0)
    tag = ''
    if pat == grading: tag = '  <== equals the half-grading character'
    if pat == [-t for t in grading]: tag = '  <== equals minus the half-grading character'
    if tag: hits.append(k)
    print(f"  e{k:<2d} " + ''.join('+' if t == 1 else '-' if t == -1 else '?' for t in pat) + tag)
print("  axes whose pattern is the half-grading character:", hits or "none")

print("\nB  doubling identity e_k x = x* e_k for lower x in e_0..e_7 (count of lower x out of 8)")
for k in range(1, 16):
    n = sum(eq(mul(e(k), e(x)), mul(conj(e(x)), e(k))) for x in range(8))
    print(f"  e{k:<2d} {n}/8" + ('   all' if n == 8 else ''))

print("\nC  circle reversal: directions u != k with (e_k u) e_k^-1 = -u  (out of the 14 other imaginary directions)")
for k in range(1, 16):
    n = sum(eq(mul(mul(e(k), e(u)), inv(k)), neg(e(u))) for u in range(1, 16) if u != k)
    print(f"  e{k:<2d} {n}/14")
