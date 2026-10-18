"""Runs the paper's listings cold (fresh namespace each) and re-checks the claims the paper makes about them.
Run:  python3 paper/test_listings.py"""
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))
def run(name):
    ns = {}; exec(compile(open(os.path.join(HERE, "listings", name)).read(), name, "exec"), ns); return ns
L1 = run("L1_ordered_address.py"); L2 = run("L2_scrambler.py")
A26 = "abcdefghijklmnopqrstuvwxyz"
assert [L1["text_at"](n, A26) for n in (0, 25, 26, 701, 702)] == ["a", "z", "aa", "zz", "aaa"]
assert all(L1["address"](L1["text_at"](n, A26), A26) == n for n in range(20000))
ALPHA = "abcdefghijklmnopqrstuvwxyz ,."; K = 3; N = 29 ** K
sc, un = L2["make_scrambler"](N)
assert sorted(sc(x) for x in range(N)) == list(range(N)) and all(un(sc(x)) == x for x in range(N))
assert L1["loc_of"](L1["page_at"](12345, ALPHA, K), ALPHA) == 12345
words = [""] + ["".join(p) for n in range(1, 4) for p in __import__("itertools").product(A26, repeat=n)]
assert all(L1["address"]("a" + w, A26) - L1["address"](w, A26) == 26 ** len(w) for w in words)
# the paper's Listing 2 and the ValaQuenta engine's scrambler are the same map (all 24,389 locations)
import sys; sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "..")))
from ValaQuenta.modules.basile import maths as B
engine_sc, engine_un = B.power_of_two_scrambler(N)
assert all(sc(x) == engine_sc(x) and un(sc(x)) == engine_un(sc(x)) for x in range(N))
print("paper/listings: all checks pass (Listing 2 == ValaQuenta basile.power_of_two_scrambler on every location)")
