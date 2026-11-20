"""circles.py (registered in 11): closure, circle number, entry/exit letters, the 8..15 half.  ValaQuenta/.venv/bin/python circles.py"""
import sys, os, csv, collections
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import equation_space as Q
def gens(f): return {"A": 1, "S": 2, "G": 4, "F": f}
def walk(word, f=8):
    g = gens(f); v = (1, 0); out = [v]
    for ch in word:
        if ch in g: v = Q.mul(v, (1, g[ch])); out.append(v)
    return out
def ptwr(v, n):
    r = (1, 0)
    for _ in range(n): r = Q.mul(r, v)
    return r
rows = list(csv.DictReader(open(os.path.join(here, "catalog/archimedes_ufm.csv"))))
loops = sorted({r["loop_word"] for r in rows if 0 < len(r["loop_word"]) <= 400}); pl = sorted({"".join(c for c in w if c in "ASG") for w in loops} - {""})
print("distinct loop words (1..400): %d ; pillar-only projections: %d" % (len(loops), len(pl)))
# C1 closure (pillar letters only)
cl = [w for w in pl if walk(w)[-1] == (1, 0)]; print("C1 closed loop words: %d of %d (%.1f%%)" % (len(cl), len(pl), 100 * len(cl) / len(pl)))
# C2 returns to index 0 at even length; returns to (+1,0) at lengths divisible by 4
ev = tot = 0; r4 = rt = 0
for w in pl:
    ws = walk(w)
    for i, (s, k) in enumerate(ws):
        if i and k == 0:
            tot += 1; ev += (i % 2 == 0)
            if s == 1: rt += 1; r4 += (i % 4 == 0)
print("C2 returns to index 0: %d, even length %d (%.1f%%) ; returns to (+1,e0): %d, length %%4==0: %d (%.1f%%)" % (tot, ev, 100 * ev / max(1, tot), rt, r4, 100 * r4 / max(1, rt)))
# C3 entry/exit letters
fi = collections.Counter(w[0] for w in pl); la = collections.Counter(w[-1] for w in pl)
print("C3 first letters: %s ; last letters: %s" % ({k: "%.1f%%" % (100 * v / len(pl)) for k, v in fi.items()}, {k: "%.1f%%" % (100 * v / len(pl)) for k, v in la.items()}))
# C4 circle number
cn = collections.Counter()
for w in pl:
    v = walk(w)[-1]; cn[1 if v == (1, 0) else 2 if v == (-1, 0) else 4] += 1
print("C4 circle number distribution (order of the loop element): %s ; number 4: %.1f%%" % (dict(cn), 100 * cn[4] / len(pl)))
# per-equation entry / loop / exit table for the fractal rows (kept as CSV)
out = open(os.path.join(here, "catalog/circles_ufm.csv"), "w", newline=""); wr = csv.writer(out)
wr.writerow(["id", "init_end", "loop_end", "circle_number", "bailout_end", "init_first", "loop_first", "bailout_has_sign", "loop_touches_upper_F8"])
bs = bt = 0
for r in rows:
    P = lambda s: "".join(c for c in s if c in "ASG")
    e = walk(P(r["init_word"]))[-1]; l = walk(P(r["loop_word"]))[-1]; b = walk(P(r["bailout_word"]))[-1]
    c = 1 if l == (1, 0) else 2 if l == (-1, 0) else 4
    if r["bailout_word"]: bt += 1; bs += ("G" in r["bailout_word"])
    up = any(k >= 8 for s, k in walk(r["loop_word"][:400], 8))
    wr.writerow([r["id"], e, l, c, b, (P(r["init_word"]) or "-")[0], (P(r["loop_word"]) or "-")[0], int("G" in r["bailout_word"]), int(up)])
out.close(); print("C5 bailout contains SIGN: %d of %d formulas with a bailout (%.1f%%)" % (bs, bt, 100 * bs / max(1, bt)))
# H: the 8..15 half; words (with F) ; full words including F letters, as distinct words
fw = sorted({w for w in loops if "F" in w}); print("words with F: %d" % len(fw))
up8 = [w for w in fw if walk(w, 8)[-1][1] >= 8]; up15 = [w for w in fw if walk(w, 15)[-1][1] >= 8]
print("H1 end in upper half (F=8): %d (%.1f%%)" % (len(up8), 100 * len(up8) / len(fw)))
print("H2 membership identical for F=8 and F=15: %s ; full address same: %d of %d" % (set(up8) == set(up15), sum(walk(w, 8)[-1][1] == walk(w, 15)[-1][1] for w in fw), len(fw)))
ent = sum(any(k >= 8 for s, k in walk(w[:200], 8)[:6]) for w in fw); print("H3 upper half entered within first 5 letters: %d (%.1f%%)" % (ent, 100 * ent / len(fw)))
# time spent in the upper half, mean fraction of the steps
fr = [sum(k >= 8 for s, k in walk(w, 8)) / (len(w) + 1) for w in fw[:3000]]; print("mean fraction of the walk in the upper half: %.3f" % (sum(fr) / len(fr)))
