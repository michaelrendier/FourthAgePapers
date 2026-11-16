#!/usr/bin/env python3
"""How can the 15 imaginary units of the sedenions be grouped as 5 + 5 + 5, or 3 x 5?  Combinatorics only, stdlib only.

Written 2026-11-16. Run cold:  python3 -I 01_fifteen_partitions.py

Setting (ESTABLISHED): in a Cayley-Dickson algebra of dimension 16 the imaginary units e_1..e_15 are labelled by the nonzero vectors of GF(2)^4 (the index
XOR rule: e_a e_b = +-e_(a xor b)).  The 15 labels with the 35 triples {a, b, a xor b} form the projective space PG(3,2): 15 points, 35 lines, 15 planes (each plane is
a Fano plane = an octonion subalgebra).  The question raised by the author: 'five forms of add, five of scale, five of sign' is a partition of 15 points into three
groups of five.  The standard structures of PG(3,2) that do that are computed here; they are THEORETICAL leads, not a derivation of add/scale/sign.
  A  spreads: 5 pairwise disjoint lines (15 = 5 x 3), count and a check that they partition the points
  B  caps of 5: 5 points, no three on a line
  C  ovoids: 5-caps meeting every plane in 1 or 3 points (the elliptic quadrics of PG(3,2))
  D  partitions of the 15 points into three disjoint ovoids, and into three arbitrary 5-caps
  E  for the partitions in D: how each ovoid meets the lines of a fixed spread (one point per line? a 3-by-5 grid / 5-by-3 grid structure)
"""
from itertools import combinations
pts = list(range(1, 16))
lines = [frozenset((a, b, a ^ b)) for a, b in combinations(pts, 2) if a < b < (a ^ b) or True]
lines = sorted({l for l in lines}, key=sorted); assert len(lines) == 35
planes = []
for a, b, c in combinations(pts, 3):                      # a plane = a 3-dim subspace minus 0 = closure of three independent points
    if c != a ^ b:
        s = frozenset({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c})
        if s not in planes: planes.append(s)
assert len(planes) == 15

def is_cap(S): return all((a ^ b) not in S for a, b in combinations(S, 2))
spreads = []
def grow(chosen, used, start):
    if len(chosen) == 5: spreads.append(tuple(chosen)); return
    for i in range(start, 35):
        if not (lines[i] & used): grow(chosen + [lines[i]], used | lines[i], i + 1)
grow([], frozenset(), 0)
print('A  spreads (5 disjoint lines covering the 15 points): %d' % len(spreads))
caps5 = [frozenset(S) for S in combinations(pts, 5) if is_cap(S)]
ovoids = [S for S in caps5 if all(len(S & p) in (1, 3) for p in planes)]
print('B  5-caps: %d;  C  ovoids (every plane meets in 1 or 3 points): %d' % (len(caps5), len(ovoids)))
def partitions(family):
    out = set()
    for A in family:
        for B in family:
            if A & B or min(A) > min(B): continue
            for C in family:
                if (A | B) & C or min(B) > min(C): continue
                out.add(frozenset((A, B, C)))
    return out
pO = partitions(ovoids); pC = partitions(caps5)
print('D  partitions of the 15 points into three ovoids: %d;  into three arbitrary 5-caps: %d' % (len(pO), len(pC)))
sizes = {}
for P in pO:
    key = tuple(sorted(len(O & l) for O in P for l in lines))
    sizes[key] = sizes.get(key, 0) + 1
print('   ovoid-triple partitions by the multiset pattern of (ovoid, line) intersection sizes: %d pattern(s)' % len(sizes))
# E: relation to spreads
cnt = {}
for P in pO:
    for S in spreads:
        meet = sorted(tuple(sorted(len(O & l) for l in S)) for O in P)
        cnt[tuple(meet)] = cnt.get(tuple(meet), 0) + 1
print('E  over all (ovoid partition, spread) pairs, how the three ovoids meet the five lines of the spread (sorted per ovoid):')
for k, v in sorted(cnt.items(), key=lambda t: -t[1])[:6]: print('   %s : %d pairs' % (k, v))
whole = sum(v for k, v in cnt.items() if all(m == (1, 1, 1, 1, 1) for m in k))
print('   pairs in which EVERY ovoid meets EVERY line of the spread in exactly one point (a 3 x 5 grid: 3 ovoids x 5 lines): %d of %d' % (whole, len(pO) * len(spreads)))
w = [(P, S) for P in pO for S in spreads if all(len(O & l) == 1 for O in P for l in S)]
print('   those %d pairs use %d distinct ovoid partitions and %d distinct spreads' % (len(w), len({p for p, s in w}), len({tuple(s) for p, s in w})))
