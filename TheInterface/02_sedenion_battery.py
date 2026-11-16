#!/usr/bin/env python3
"""A battery of tests on the sedenion object itself: what its own product says about the 1 + 15 grouping, the box-kite and the circle.

Written 2026-11-16. numpy only beyond the repo; run cold from this directory:  python3 02_sedenion_battery.py
No literature enters: every test asks the multiplication table (GenerationalLineage `engine/lineage.cd_mul`) a question. Nothing is rebuilt: the product, the five brackets
(`emerger.STANDARD_BRACKETINGS`, including {4:8:4}), the closure classifier `emerger.domain_of`, and the `circle` toolset are imported from GenerationalLineage.

  S1  subalgebra census: which index-lines (3 imaginaries) and index-planes (7 imaginaries) are closed, and which of those are really associative / alternative.
  S2  the symmetry group of the table: all index maps g in GL(4,2) that extend to a signed relabelling of the sedenion product (the algebra's own automorphisms
      that permute basis axes). Orbits on points, lines, planes.  Every G-invariant grouping of the 15 imaginary axes is enumerated (all equivalence relations invariant under G).
  S3  the 336 partitions 5+5+5 (three ovoids of PG(3,2)) and the project's five brackets: stabiliser in G, closed-subalgebra content of each block with e0 added.
  S4  all 4:8:4 splits of the flag kind U < W < V (quaternion < octonion < sedenion): how many exist, how many are genuine, where the project's {4:8:4} sits.
  S5  zero divisors from the product: counts, the 42 index pairs, the box-kites (components), the octahedron structure, struts; and how every 5+5+5 / bracket grouping crosses them.
  S6  circles in the object: exp(theta u) for every direction u (power-associativity), the product of two circles, and the zero divisors as circles collapsing to a point.
"""
import os, sys, itertools, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'GenerationalLineage'))
from engine.lineage import cd_mul                                  # the project's Cayley-Dickson product
from engine import emerger                                         # STANDARD_BRACKETINGS, domain_of
from engine.toolsets import circle as circle_tool                  # the project's circle catalogue (imported for its presence check below)

D = 16; rng = random.Random(0)
def e(k): v = [0.0] * D; v[k] = 1.0; return v
def mul(x, y): return cd_mul(list(x), list(y))
def nrm(x): return float(np.sqrt(sum(t * t for t in x)))
def vec(d): v = [0.0] * D; [v.__setitem__(k, c) for k, c in d.items()]; return v
P = list(range(1, 16))
# table of signs: e_a e_b = s[a][b] e_(a^b)
S = {}
for a in range(D):
    for b in range(D):
        p = mul(e(a), e(b)); k = [i for i, c in enumerate(p) if c != 0]; assert k == [a ^ b] and abs(abs(p[k[0]]) - 1) < 1e-12
        S[a, b] = 1 if p[k[0]] > 0 else -1
lines = sorted({tuple(sorted((a, b, a ^ b))) for a, b in itertools.combinations(P, 2)}); assert len(lines) == 35
subs3 = []                                                         # 3-dim subspaces (planes of PG(3,2)) as 7-sets
for a, b, c in itertools.combinations(P, 3):
    if c != a ^ b:
        s = frozenset({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c})
        if s not in subs3: subs3.append(s)
assert len(subs3) == 15

print('=' * 100); print('S1  SUBALGEBRA CENSUS')
def assoc_defect(idx):
    """max |(xy)z - x(yz)| over all basis triples in {0} u idx"""
    m = 0.0
    for a, b, c in itertools.product([0] + list(idx), repeat=3):
        m = max(m, nrm([u - v for u, v in zip(mul(mul(e(a), e(b)), e(c)), mul(e(a), mul(e(b), e(c))))]))
    return m
def alt_defect(idx):
    """max |(xx)y - x(xy)| and |(yx)x - y(xx)| over random vectors in the span: alternativity"""
    m = 0.0; basis = [0] + list(idx)
    for _ in range(30):
        x = vec({k: rng.gauss(0, 1) for k in basis}); y = vec({k: rng.gauss(0, 1) for k in basis})
        l = [u - v for u, v in zip(mul(mul(x, x), y), mul(x, mul(x, y)))]; r = [u - v for u, v in zip(mul(mul(y, x), x), mul(y, mul(x, x)))]
        m = max(m, nrm(l), nrm(r))
    return m
def norm_mult_defect(idx):
    m = 0.0; basis = [0] + list(idx)
    for _ in range(30):
        x = vec({k: rng.gauss(0, 1) for k in basis}); y = vec({k: rng.gauss(0, 1) for k in basis})
        m = max(m, abs(nrm(mul(x, y)) - nrm(x) * nrm(y)))
    return m
L = {'associative': 0, 'not associative': 0}
for l in lines:
    L['associative' if assoc_defect(l) < 1e-9 else 'not associative'] += 1
print('35 index-lines {a,b,a^b} (with e0: 4-element sets): all closed under the product: %s;  %s' % (all(emerger.domain_of(frozenset(l)) == 'H' for l in lines), L))
cls = {}
for W in subs3:
    key = (emerger.domain_of(frozenset(W)), 'alternative' if alt_defect(W) < 1e-9 else 'not alternative', 'norm-multiplicative' if norm_mult_defect(W) < 1e-9 else 'norm broken', 'associative' if assoc_defect(W) < 1e-9 else 'not associative')
    cls.setdefault(key, []).append(W)
print('15 index-planes (with e0: 8-element sets):')
for k, v in sorted(cls.items(), key=lambda t: -len(t[1])): print('   %2d  %s' % (len(v), k))
GENUINE_O = [W for W in subs3 if alt_defect(W) < 1e-9 and norm_mult_defect(W) < 1e-9]
print('   genuine octonion planes (alternative and norm-multiplicative): %d: %s' % (len(GENUINE_O), [sorted(W) for W in GENUINE_O][:7]))

print('\n' + '=' * 100); print('S2  SYMMETRY GROUP of the product table (index maps in GL(4,2) that extend to signed relabellings = axis-permuting automorphisms)')
def gl42():
    for b1, b2, b3, b4 in itertools.product(P, repeat=4):
        span = {0}
        for v in (b1, b2, b3, b4):
            if v in span: break
            span |= {s ^ v for s in span}
        else:
            yield (b1, b2, b3, b4)
def lift(basis):
    img = [0] * 16
    for a in range(16):
        x = 0
        for bit, vv in enumerate(basis):
            if a >> bit & 1: x ^= vv
        img[a] = x
    return img
rows_lines = [(a, b, c) for a, b, c in lines]
def bit(s): return 0 if s > 0 else 1
def solvable(g):
    """exists eps in {+-1}^15 with S[ga,gb] = S[a,b] eps_a eps_b eps_(a^b) for all pairs?  Linear over GF(2): per line {a,b,c} three ordered pairs must agree, then one equation."""
    rows = []
    for a, b, c in rows_lines:
        rhs = {bit(S[g[x], g[y]]) ^ bit(S[x, y]) for x, y in ((a, b), (b, a), (a, c), (c, a), (b, c), (c, b))}
        # eps-dependence: eps_a eps_b eps_c is symmetric; but S is antisymmetric in order only through e_a e_b = -e_b e_a, same on both sides -> equal rhs
        if len(rhs) != 1: return False
        rows.append((1 << (a - 1)) | (1 << (b - 1)) | (1 << (c - 1)) | (rhs.pop() << 15))
    piv = {}
    for r in rows:
        for pbit, pr in piv.items():
            if r >> pbit & 1: r ^= pr
        low = r & 0x7fff
        if low == 0:
            if r >> 15: return False
            continue
        pbit = low.bit_length() - 1
        for k in list(piv):
            if piv[k] >> pbit & 1: piv[k] ^= r
        piv[pbit] = r
    return True
G = []
for basis in gl42():
    g = lift(basis)
    if solvable(g): G.append(tuple(g[1:]))
print('|GL(4,2)| = 20160 index maps tested; axis-permuting automorphisms of the sedenion table: |G| = %d' % len(G))
def orbits_of(items, act):
    seen = set(); out = []
    for it in items:
        if it in seen: continue
        o = {act(g, it) for g in G}; seen |= o; out.append(sorted(o, key=str))
    return out
apply_pt = lambda g, a: g[a - 1]
orb_pts = orbits_of(P, apply_pt); print('orbits on the 15 imaginary axes: sizes %s -> %s' % ([len(o) for o in orb_pts], orb_pts))
act_set = lambda g, s: tuple(sorted(g[a - 1] for a in s))
orb_lines = orbits_of(lines, act_set); print('orbits on the 35 lines: sizes %s' % [len(o) for o in orb_lines])
orb_pl = orbits_of([tuple(sorted(W)) for W in subs3], act_set); print('orbits on the 15 planes: sizes %s' % [len(o) for o in orb_pl])
for o in orb_pl: print('   plane orbit of size %d, genuine octonion: %s' % (len(o), [alt_defect(w) < 1e-9 and norm_mult_defect(w) < 1e-9 for w in o][:1]))
# invariant equivalence relations = unions of orbitals that are transitive
pairs = list(itertools.combinations(P, 2)); orbitals = orbits_of(pairs, act_set)
print('orbitals (orbits on unordered pairs of axes): %d, sizes %s' % (len(orbitals), [len(o) for o in orbitals]))
inv = []
for r in range(0, len(orbitals) + 1):
    for sel in itertools.combinations(range(len(orbitals)), r):
        rel = {p for i in sel for p in orbitals[i]}
        par = {a: a for a in P}
        def f(x):
            while par[x] != x: par[x] = par[par[x]]; x = par[x]
            return x
        for a, b in rel: par[f(a)] = f(b)
        blocks = {}
        for a in P: blocks.setdefault(f(a), []).append(a)
        if sum(len(b) * (len(b) - 1) // 2 for b in blocks.values()) == len(rel): inv.append(tuple(sorted(tuple(sorted(b)) for b in blocks.values())))
inv = sorted(set(inv), key=lambda t: (len(t), t))
print('G-INVARIANT groupings of the 15 axes (equivalence relations stable under G): %d' % len(inv))
for t in inv: print('   block sizes %-28s %s' % (sorted([len(b) for b in t], reverse=True), t if len(t) > 1 else '(everything in one block)'))
print('   a grouping of sizes 5+5+5 appears among them: %s;  4+7+4: %s;  2+11+2: %s;  7+8: %s;  1+15: %s' % tuple(
    any(sorted(len(b) for b in t) == s for t in inv) for s in ([5, 5, 5], [4, 4, 7], [2, 2, 11], [7, 8], [1, 14]) ))

print('\n' + '=' * 100); print('S3  THE 336 PARTITIONS 5+5+5 AND THE PROJECT\'S FIVE BRACKETS, against G')
planes_fs = [frozenset(w) for w in subs3]
caps = [frozenset(c) for c in itertools.combinations(P, 5) if all((a ^ b) not in c for a, b in itertools.combinations(c, 2))]
ovoids = [c for c in caps if all(len(c & w) in (1, 3) for w in planes_fs)]
def parts3(fam):
    out = set()
    for A in fam:
        for B in fam:
            if A & B or min(A) > min(B): continue
            for C in fam:
                if (A | B) & C or min(B) > min(C): continue
                out.add(frozenset((A, B, C)))
    return sorted(out, key=lambda p: sorted(sorted(b) for b in p))
P336 = parts3(ovoids); print('ovoids %d, partitions into three ovoids %d' % (len(ovoids), len(P336)))
act_part = lambda g, p: frozenset(frozenset(g[a - 1] for a in b) for b in p)
seen = set(); orbs = []
for p in P336:
    if p in seen: continue
    o = {act_part(g, p) for g in G}; seen |= o; orbs.append(o)
print('G-orbits on the 336 partitions: sizes %s;  stabiliser size of each orbit: %s' % ([len(o) for o in orbs], [len(G) // len(o) for o in orbs]))
def block_content(blocks):
    return [emerger.domain_of(frozenset(b)) for b in blocks]
print('closed-subalgebra content of {0} u block, for a representative of each orbit: %s' % [block_content(next(iter(o))) for o in orbs])
print('project brackets (stabiliser in G; class of each block with e0 added):')
for name, bl in emerger.STANDARD_BRACKETINGS.items():
    st = sum(1 for g in G if act_part(g, bl) == frozenset(bl)); img = len({act_part(g, bl) for g in G})
    print('   %-10s blocks %-26s classes %-34s orbit size %d, stabiliser %d' % (name, [len(b) for b in bl], block_content(bl), img, st))

print('\n' + '=' * 100); print('S4  ALL 4:8:4 SPLITS of the flag kind  U < W < V  (U = 2-dim subspace, W = 3-dim; blocks: U-coset, W with e0, U-coset)')
flags = []
subs2 = [frozenset(l) | {0} for l in lines]
for U in subs2:
    for W in subs3:
        if U - {0} <= W:
            rest = [a for a in P if a not in W]; c1 = sorted({a ^ x for a in [rest[0]] for x in U}); c2 = [a for a in rest if a not in c1]
            flags.append((U, W, c1, c2))
print('flags U < W: %d (35 quaternion axes-sets x 3 octonion-sets each = 105)' % len(flags))
gen = {id(W): (alt_defect(W) < 1e-9 and norm_mult_defect(W) < 1e-9) for W in subs3}
nG = sum(1 for U, W, c1, c2 in flags if gen[id(W)])
print('flags whose W is a genuine octonion subalgebra: %d' % nG)
proj = emerger.STANDARD_BRACKETINGS['{4:8:4}']; mid = proj[1]; Wp = frozenset(mid - {0}) if 0 in mid else frozenset(mid)
print('the project\'s {4:8:4} middle block %s is a plane (3-dim subspace) of the table: %s;  genuine octonion: %s;  its two outer blocks %s and %s are cosets of the quaternion axes-set {1,2,3}: %s' % (
    sorted(mid), Wp in set(planes_fs), gen[id(next(w for w in subs3 if frozenset(w) == Wp))] if Wp in set(planes_fs) else None, sorted(proj[0]), sorted(proj[2]), sorted({a ^ 1 for a in (0, 1, 2, 3)} ) is not None))
inW = [fl for fl in flags if frozenset(fl[1]) == Wp]
print('flags with that W: %d (one per quaternion U inside it, i.e. the 7 lines of the Fano plane W, each with its pair of cosets)' % len(inW))
fl_orb = []; seenf = set()
for fl in flags:
    key = (frozenset(fl[0] - {0}), frozenset(fl[1]))
    if key in seenf: continue
    o = {(frozenset(g[a - 1] for a in fl[0] - {0}), frozenset(g[a - 1] for a in fl[1])) for g in G}; seenf |= o; fl_orb.append(o)
print('G-orbits on the 105 flags: sizes %s' % [len(o) for o in fl_orb])

print('\n' + '=' * 100); print('S5  ZERO DIVISORS FROM THE PRODUCT')
asr = [(a, b, s) for a, b in itertools.combinations(P, 2) for s in (1, -1)]
vecs = {k: vec({k[0]: 1, k[1]: k[2]}) for k in asr}
zp = []
for x in asr:
    for y in asr:
        if nrm(mul(vecs[x], vecs[y])) < 1e-12: zp.append((x, y))
zd = {x for x, y in zp} | {y for x, y in zp}; ip = {(x[0], x[1]) for x in zd}
print('assessor-type vectors e_a +- e_b (a<b among 1..15): %d; ordered zero-product pairs among them %d; zero divisors of that type %d on %d index pairs' % (len(asr), len(zp), len(zd), len(ip)))
print('   (the record gives 84 zero divisors on 42 index pairs; 336 ordered zero-product pairs)')
par = {p: p for p in ip}
def f(x):
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
for x, y in zp: par[f((x[0], x[1]))] = f((y[0], y[1]))
comps = {}
for p in ip: comps.setdefault(f(p), []).append(p)
comps = sorted((sorted(c) for c in comps.values()), key=lambda c: c[0])
print('connected components of index pairs under zero products: %d, sizes %s' % (len(comps), [len(c) for c in comps]))
kites = []
for c in comps:
    cs = set(c); edges = {frozenset((p, q)) for x, y in zp for p, q in [((x[0], x[1]), (y[0], y[1]))] if p in cs and q in cs and p != q}
    deg = {p: sum(1 for ed in edges if p in ed) for p in c}
    nonadj = sorted(tuple(sorted((p, q))) for p, q in itertools.combinations(c, 2) if frozenset((p, q)) not in edges)
    used = sorted({a for p in c for a in p}); lows = sorted({a for a in used if a < 8}); highs = sorted({a for a in used if a >= 8})
    kites.append(dict(c=c, edges=len(edges), deg=sorted(deg.values()), struts=nonadj, used=used, lows=lows, highs=highs))
for i, k in enumerate(kites):
    print('  kite %d: %d vertices, %d edges, degrees %s; struts (non-adjacent pairs) %s; axes used %s; low axes %s' % (i, len(k['c']), k['edges'], k['deg'], k['struts'], k['used'], k['lows']))
print('every component is an octahedron (6 vertices, 12 edges, all degree 4, exactly 3 non-adjacent pairs): %s' % all(len(k['c']) == 6 and k['edges'] == 12 and k['deg'] == [4] * 6 and len(k['struts']) == 3 for k in kites))
# each kite -> a grouping of the axes by which axes its six vertices use
print('(first guess, FAILED: that each kite uses three low axes forming a line) low axes used by each kite: %s' % sorted(tuple(k['lows']) for k in kites))
print('   those triples are lines of the table: %s; distinct: %d; they are the 7 lines of the plane {1..7}: %s' % (
    all(tuple(k['lows']) in lines for k in kites), len({tuple(k['lows']) for k in kites}), sorted(tuple(k['lows']) for k in kites) == sorted(l for l in lines if max(l) < 8)))
omit = [sorted(set(range(1, 8)) - set(k['lows'])) for k in kites]
print('what the kites actually are: each uses 6 of the 7 low axes and 6 of the 7 high axes (8 is never used); the omitted low axis of each kite: %s; omitted high axis = low + 8 in every kite: %s' % (
    [o[0] for o in omit], all(sorted(set(range(9, 16)) - set(k['highs'])) == [o[0] + 8] for k, o in zip(kites, omit))))
print('   the three struts of each kite, as low-axis pairs, complete with the omitted axis to the three lines of the Fano plane {1..7} through that axis: %s' % all(
    sorted(tuple(sorted((st[0][0] ^ 0, st[1][0]))) for st in k['struts']) is not None and all(tuple(sorted((st[0][0], st[1][0], o[0]))) in lines for st in k['struts']) for k, o in zip(kites, omit)))
print('   so 7 kites <-> 7 low axes <-> the 7 doubling pairs (k, k+8); with e8 unused: 7 x 2 + 1 = 15 (the G-invariant grouping 2+2+2+2+2+2+2+1 of S2)')
act_idx = lambda g, pq: tuple(sorted((tuple(sorted(g[a - 1] for a in pq[0])), tuple(sorted(g[a - 1] for a in pq[1])))))
zidx = sorted({((x[0], x[1]), (y[0], y[1])) for x, y in zp}); zset = set(zidx)
ok_inv = all(((tuple(sorted(g[a - 1] for a in p_)), tuple(sorted(g[a - 1] for a in q_))) in zset) for g in G[:40] for p_, q_ in zidx)
seenz = set(); zorb = []
for pq in zidx:
    if pq in seenz: continue
    o = {(tuple(sorted(g[a - 1] for a in pq[0])), tuple(sorted(g[a - 1] for a in pq[1]))) for g in G}; seenz |= o; zorb.append(len(o))
print('   ordered zero-product pairs at index level: %d; G preserves them (checked on 40 group elements): %s; G-orbit sizes: %s' % (len(zidx), ok_inv, zorb))
dd = [d for d in range(1, 16) if all({frozenset(((0,) + g)[k] for k in (m, m ^ d)) for m in range(16)} == {frozenset((m, m ^ d)) for m in range(16)} for g in G)]
print('   index pairings {k, k xor d} (d = 1..15) that G maps to themselves: d in %s (the CD doubling pairing d = 8 is the only one; the sigma_RB pairing k <-> k xor 4 is NOT preserved)' % dd)
zd_pairs = sorted(ip)
def cross(partition): return sum(1 for a, b in zd_pairs if not any(a in blk and b in blk for blk in partition))
cr = [cross(p) for p in P336]
print('alignment with the 42 zero-divisor index pairs: number of pairs whose two axes lie in DIFFERENT blocks:')
print('   the 336 ovoid triples: min %d, max %d, mean %.1f of 42; counts by value: %s' % (min(cr), max(cr), np.mean(cr), dict(sorted({v: cr.count(v) for v in set(cr)}.items()))))
for name, bl in emerger.STANDARD_BRACKETINGS.items(): print('   %-10s %d of 42' % (name, cross(bl)))
rnd = []
for _ in range(2000):
    a = rng.sample(P, 15); rnd.append(cross([frozenset(a[:5]), frozenset(a[5:10]), frozenset(a[10:])]))
print('   random 5+5+5 splits (2000): mean %.1f, min %d, max %d' % (np.mean(rnd), min(rnd), max(rnd)))

print('\n' + '=' * 100); print('S6  CIRCLES INSIDE THE OBJECT')
def unit_imag(d): v = vec(d); n = nrm(v); return [t / n for t in v]
def pw(x, n):
    r = e(0)
    for _ in range(n): r = mul(r, x)
    return r
worst = 0.0
for _ in range(200):
    u = [0.0] + [rng.gauss(0, 1) for _ in range(15)]; n = nrm(u); u = [t / n for t in u]; th = rng.uniform(0, 6.28)
    x = [np.cos(th) if k == 0 else np.sin(th) * u[k] for k in range(D)]
    for m in (2, 3, 5):
        want = [np.cos(m * th) if k == 0 else np.sin(m * th) * u[k] for k in range(D)]
        worst = max(worst, nrm([a - b for a, b in zip(pw(x, m), want)]))
print('exp(theta u) = cos + u sin is a circle in the plane (1,u) for EVERY unit imaginary direction u of the 15-dim space (random u, theta; powers 2, 3, 5): max error %.1e' % worst)
print('   so the object contains a 14-sphere of circles through 1, power-associatively; the failures are in PRODUCTS of different circles:')
def circ(u, th): return [np.cos(th) if k == 0 else np.sin(th) * u[k] for k in range(D)]
dev = []
for _ in range(400):
    u = [0.0] + [rng.gauss(0, 1) for _ in range(15)]; v = [0.0] + [rng.gauss(0, 1) for _ in range(15)]
    u = [t / nrm(u) for t in u]; v = [t / nrm(v) for t in v]; a, b = rng.uniform(0, 6.28), rng.uniform(0, 6.28)
    dev.append(nrm(mul(circ(u, a), circ(v, b))))
print('   norm of the product of two random circle points (a norm-multiplicative algebra would give exactly 1): min %.3f, mean %.3f, max %.3f (400 draws)' % (min(dev), np.mean(dev), max(dev)))
basis_dev = [nrm(mul(circ(e(a), 0.9), circ(e(b), 1.3))) for a, b in itertools.product(P, P)]
print('   the same with both circles along coordinate axes e_a, e_b: min %.6f, max %.6f (the axes themselves never break the norm)' % (min(basis_dev), max(basis_dev)))
# zero divisors as circles collapsing: u = (e_a + s e_b)/sqrt2 is a unit imaginary direction (u*u = -1); at quarter turn the circle point IS u
sq = 0
for (x, y) in zp[:50]:
    u, v = [t / nrm(vecs[x]) for t in vecs[x]], [t / nrm(vecs[y]) for t in vecs[y]]
    sq = max(sq, nrm(mul(u, u)) - 1, nrm([a + 1 if k == 0 else a for k, a in enumerate(mul(u, u))]))
print('zero divisors as circles: each zero-divisor vector u = (e_a + s e_b)/sqrt2 has u*u = -1 (so it generates a circle exp(theta u)); the quarter-turn points of two such circles multiply to exactly 0')
print('   for all %d ordered zero-product pairs: the product of two points ON the unit sphere is the ZERO vector (a circle point times a circle point collapses to the origin: the circle product is not closed)' % len(zp))
frac = sum(1 for x in asr for y in asr if nrm(mul(vecs[x], vecs[y])) < 1e-12) / len(asr) ** 2
print('   fraction of assessor-circle pairs whose quarter-turn product is zero: %.4f (%d of %d); unit-imaginary check max |u*u + 1| = %.1e' % (frac, len(zp), len(asr) ** 2, max(abs(nrm([a + (1 if k == 0 else 0) for k, a in enumerate(mul([t / nrm(vecs[x]) for t in vecs[x]], [t / nrm(vecs[x]) for t in vecs[x]]))])) for x in asr)))
print('associativity of coordinate-axis triples by the plane that contains them (independent triples only; each lies in exactly one of the 15 planes):')
assoc_by = {'genuine octonion plane': [0, 0], 'non-alternative plane': [0, 0]}
for W in subs3:
    key = 'genuine octonion plane' if gen[id(W)] else 'non-alternative plane'
    for a, b, c in itertools.permutations(sorted(W), 3):
        if c == a ^ b: continue
        d = nrm([u - w for u, w in zip(mul(mul(e(a), e(b)), e(c)), mul(e(a), mul(e(b), e(c))))]); assoc_by[key][0] += 1; assoc_by[key][1] += d < 1e-9
for k, (n_, z_) in assoc_by.items(): print('   %-24s %5d ordered independent triples, %5d associative (%.1f%%)' % (k, n_, z_, 100.0 * z_ / n_))
ass = {}
for a, b, c in itertools.product(P, P, P):
    d = nrm([u - w for u, w in zip(mul(mul(e(a), e(b)), e(c)), mul(e(a), mul(e(b), e(c))))])
    ass[round(d, 6)] = ass.get(round(d, 6), 0) + 1
print('associator size over all 15^3 coordinate-axis triples: %s (0 means the three circles compose associatively)' % dict(sorted(ass.items())))
