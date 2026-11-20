"""census.py (registered in 11): pair census over distinct catalog words.  ValaQuenta/.venv/bin/python census.py"""
import sys, os, csv
here = os.path.dirname(os.path.abspath(__file__))
def val(w):
    a, b = 1, 0
    for ch in w:
        if ch == "A": b += 1
        elif ch == "S": a *= 2; b *= 2
        elif ch == "G": a, b = -a, -b
    return (a, b)
rows = []
for fn, col in (("catalog/archimedes_ufm.csv", "loop_word"), ("catalog/archimedes_py.csv", "ass_word")):
    for r in csv.DictReader(open(os.path.join(here, fn))): rows.append(r[col])
words = sorted({"".join(c for c in w if c in "ASG") for w in rows}); words = [w for w in words if 1 <= len(w) <= 400]
N = len(words); print("distinct words (1..400): %d" % N)
res = {}
for pair in ("AS", "AG", "SG"):
    pres = [w for w in words if pair[0] in w and pair[1] in w]
    sub = [("".join(c for c in w if c in pair)) for w in pres]
    sens = sum(val(s) != val(s[::-1]) for s in sub)
    res[pair] = (len(pres), sens); print("pair %s present in %d (%.1f%%); order-sensitive on its subword: %d (%.1f%%)" % (pair, len(pres), 100 * len(pres) / N, sens, 100 * sens / max(1, len(pres))))
al = sum(1 for w in words if all(c in w for c in "ASG")); print("all three letters: %d (%.1f%%)" % (al, 100 * al / N))
none = sum(1 for w in words if len(set(w)) == 1); print("single-letter words (no pair at all): %d" % none)
import collections
c = collections.Counter(tuple(p for p in ("AS", "AG", "SG") if p[0] in w and p[1] in w) for w in words); print("pair-type signatures:", dict(c))
