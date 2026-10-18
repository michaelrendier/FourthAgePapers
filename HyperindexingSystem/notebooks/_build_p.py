"""Builds the paper's listings (single source of truth) and the two notebooks that run them."""
import os
from _nb import md, code, write
HERE = os.path.dirname(os.path.abspath(__file__))
LDIR = os.path.join(HERE, os.pardir, "paper", "listings")
os.makedirs(LDIR, exist_ok=True)

L1 = '''# Listing 1 - the ordered address (bijective base-N): text <-> non-negative integer
def address(text, alphabet):
    """Rank of `text` among all strings over `alphabet`, shortest first, then alphabetical."""
    N, a = len(alphabet), 0
    for ch in text:
        a = a * N + alphabet.index(ch) + 1
    return a - 1

def text_at(a, alphabet):
    """Inverse of address(): the string whose rank is `a`."""
    N, out = len(alphabet), []
    a += 1
    while a > 0:
        a, r = divmod(a - 1, N)
        out.append(alphabet[r])
    return "".join(reversed(out))

def page_at(loc, alphabet, k):
    """Fixed-length page: the k-digit base-N numeral of `loc` (digit 0 = first symbol)."""
    N, out = len(alphabet), []
    for _ in range(k):
        loc, r = divmod(loc, N)
        out.append(alphabet[r])
    return "".join(reversed(out))

def loc_of(page, alphabet):
    """Inverse of page_at()."""
    N, loc = len(alphabet), 0
    for ch in page:
        loc = loc * N + alphabet.index(ch)
    return loc
'''
L2 = '''# Listing 2 - an invertible scrambler of [0, N): LCG + xorshift, cycle-walked into range
def make_scrambler(N, a=1664525, c=1013904223, s1=7, s2=5):
    e = max(1, (N - 1).bit_length()); M = 1 << e; mask = M - 1
    a_inv = pow(a, -1, M)                       # a odd -> invertible mod 2^e
    def f(x):                                   # bijection on [0, M)
        x = (a * x + c) & mask                  # Hull-Dobell: a = 1 mod 4, c odd
        x ^= x >> s1
        x ^= (x << s2) & mask
        return x
    def finv(y):
        z = y
        for _ in range(e // s2 + 1): z = y ^ ((z << s2) & mask)
        y = z
        for _ in range(e // s1 + 1): z = y ^ (z >> s1)
        return (a_inv * (z - c)) & mask
    def scramble(x):                            # bijection on [0, N)
        x = f(x)
        while x >= N: x = f(x)
        return x
    def unscramble(y):
        y = finv(y)
        while y >= N: y = finv(y)
        return y
    return scramble, unscramble
'''
open(os.path.join(LDIR, "L1_ordered_address.py"), "w").write(L1)
open(os.path.join(LDIR, "L2_scrambler.py"), "w").write(L2)

# ---------------------------------------------------------------- p01 Babel recipe
write("p01_babel_to_ordered/01_babel_recipe.ipynb", "# p01 · The jump-off: an invertible map between locations and pages\nBasile's `libraryofbabel.info`: a location is a number, a page is a base-29 numeral, and the two are joined by an **invertible pseudo-random number generator** (\"a pseudo-random number generating algorithm … without needing to store anything on disk … for any block of text, the program can work backwards to calculate its location\", theory page 4). The published code (`librarianofbabel/libraryofbabel.info-algo`, CC BY-SA-NC, uploaded 2019-01-02) is the image library's; its README gives the recipe: an LCG `pointer = (a·pointer + c) mod m`, then shift/XOR steps, and the inverse by `a⁻¹` and the shifts undone. This notebook realises that **recipe** independently at a size that can be checked exhaustively.", [
code(L1 + "\n" + L2 + "\nprint('listings defined')"),
md("## The toy library: 29 symbols, pages of 3 characters (N = 29³ = 24,389 pages)\nThe scrambler is checked on **every** location, not sampled: it is a bijection on [0, N) and the inverse is exact."),
code('''ALPHA = "abcdefghijklmnopqrstuvwxyz ,."; K = 3; N = len(ALPHA) ** K
scramble, unscramble = make_scrambler(N)
seen = set()
for loc in range(N):
    y = scramble(loc); assert 0 <= y < N and unscramble(y) == loc; seen.add(y)
print("N =", N, "| distinct scrambled values:", len(seen), "| every location round-trips: True")
assert len(seen) == N'''),
md("## A page and its location, both directions\n`page` = the page whose location is `loc` in the *scrambled* library; `ordered` = the page at the same location in the ordered library (Listing 1's numeral)."),
code('''def babel_page(loc):  return page_at(scramble(loc), ALPHA, K)
def babel_loc(page):  return unscramble(loc_of(page, ALPHA))
print("loc    scrambled page   ordered page")
for loc in range(12): print("%-6d %-16r %r" % (loc, babel_page(loc), page_at(loc, ALPHA, K)))
for loc in (0, 1, 777, N - 1): assert babel_loc(babel_page(loc)) == loc
print("babel_loc(babel_page(loc)) == loc  for sampled locations; exhaustive check above")'''),
md("## Neighbouring locations: what each numbering does with them\nMean number of the 3 characters that differ between the pages at locations L and L + 1, over all 24,388 neighbouring pairs."),
code('''def diff(a, b): return sum(x != y for x, y in zip(a, b))
ordered = sum(diff(page_at(L, ALPHA, K), page_at(L + 1, ALPHA, K)) for L in range(N - 1)) / (N - 1)
scrambled = sum(diff(babel_page(L), babel_page(L + 1)) for L in range(N - 1)) / (N - 1)
print("ordered   : %.3f characters differ between neighbours" % ordered)
print("scrambled : %.3f characters differ between neighbours  (independent pages would give %.3f)" % (scrambled, 3 * 28 / 29))
assert ordered < 1.1 and scrambled > 2.5'''),
md("## Same set, same information\nThe scrambler is a permutation of [0, N). Both libraries hold the same N pages and a location costs the same log₂N bits in each; only the *order* differs. Which page sits where is what the scrambler decides; **the address of a page is computed from the page in both, and nothing is stored.**"),
code('''print("log2(N) = %.2f bits per location in both libraries" % math.log2(N))
print("table entries stored by either library: 0 (scramble/unscramble are O(log N) arithmetic)")'''),
])

# ---------------------------------------------------------------- p02 ordered address & hyperindex definition
write("p01_babel_to_ordered/02_ordered_address_and_definition.ipynb", "# p02 · The ordered address, and what 'hyperindex' refers to\nThe Hyperwebster, as presented in Vsauce's *The Banach–Tarski Paradox* (transcript, `sites.google.com/site/vsaucetranscripts/scripts/the-banach-tarski-paradox`): \"a dictionary … [that] lists every single possible word of any length formed from the 26 letters in the English alphabet\"; \"if they put all the words that begin with 'a' in a volume titled 'A,' they wouldn't have to print the initial 'a'.\" Below: the dictionary as a computable address, the volume-A trick checked exhaustively, and the definition tested on both libraries of p01.", [
code(L1 + "\n" + L2 + "\nprint('listings defined')"),
md("## The dictionary as an address (26 letters, shortest first)\nTranscript, first rows. `address` and `text_at` are Listing 1."),
code('''A26 = "abcdefghijklmnopqrstuvwxyz"
print("address   word")
for n in list(range(0, 30)) + [700, 701, 702]:
    w = text_at(n, A26); assert address(w, A26) == n
    print("%-9d %r" % (n, w))'''),
md("Address 0 is `a`, 25 is `z`, 26 is `aa`, 701 is `zz`, 702 is `aaa`. Every finite word has exactly one address and every non-negative integer is the address of exactly one word."),
md("## Volume A: dropping the initial letter\nThe map `w ↦ 'a'+w` from all words (including the empty word) onto the words that begin with `a`, checked for **all** words of length ≤ 4 over 26 letters (475,255 words):"),
code('''from itertools import product
words = [""] + ["".join(p) for n in range(1, 5) for p in product(A26, repeat=n)]
volA = {w for w in words if w[:1] == "a"}
stripped = {w[1:] for w in volA if len(w) <= 4}
print(len(words), "words of length <= 4 | volume A holds", len(volA), "| stripped of the initial letter:", len(stripped))
allshort = {w for w in words if len(w) <= 3}
assert {w[1:] for w in volA if len(w) <= 4} >= allshort
assert {"a" + w for w in allshort} <= volA
print("every word of length <= 3 is a volume-A word with its initial 'a' removed, and back: True")'''),
md("**In the address.** Prepending `a` to a word of length ℓ adds exactly `N^ℓ` to its numeral value (digit value 1 at the new most significant place), so the volume-A word and the word it came from differ by a power of N. Exhaustive for all words up to length 4:"),
code('''N = 26
ok = all(address("a" + w, A26) - address(w, A26) == N ** len(w) for w in words if len(w) <= 4)
print("address('a'+w) - address(w) == 26**len(w) for every word w with len(w) <= 4:", ok); assert ok'''),
md("## What 'hyperindex' refers to, tested on both libraries\nA **hyperindex** is a bijection between a set of texts and an initial segment of the non-negative integers such that (i) the integer is *computed from the text* and the text from the integer (no table is consulted or stored), and (ii) it is exact. Two properties then separate the members of the family, measured on the 24,389-page toy library of p01:"),
code('''ALPHA = "abcdefghijklmnopqrstuvwxyz ,."; K = 3; NP = len(ALPHA) ** K
scramble, unscramble = make_scrambler(NP)
ordered_loc  = lambda page: loc_of(page, ALPHA)
babel_loc    = lambda page: unscramble(loc_of(page, ALPHA))
# (i)+(ii): exact bijection, no table
ex_o = len({ordered_loc(page_at(L, ALPHA, K)) for L in range(NP)}) == NP
ex_b = len({babel_loc(page_at(L, ALPHA, K)) for L in range(NP)}) == NP
# prefix structure: location('b'+w) - location('a'+w) should be the same for every w if the first symbol is a digit
ws = [a + b for a in ALPHA for b in ALPHA]
def spread(loc): return len({loc("b" + w) - loc("a" + w) for w in ws})
print("%-10s %-22s %-28s %s" % ("library", "exact bijection (N pages)", "distinct (loc('b'+w)-loc('a'+w))", "locations of 'aab','aac' differ by"))
print("%-10s %-22s %-28d %d" % ("ordered", ex_o, spread(ordered_loc), ordered_loc("aac") - ordered_loc("aab")))
print("%-10s %-22s %-28d %d" % ("scrambled", ex_b, spread(babel_loc), babel_loc("aac") - babel_loc("aab")))
assert ex_o and ex_b and spread(ordered_loc) == 1 and spread(babel_loc) > 100'''),
md("Both are hyperindices. The ordered one keeps the structure of the text in the integer: a prefix is a place value, so the volume trick, neighbouring pages and one-symbol edits are arithmetic on the address (`+1`, `+N^ℓ`). The scrambled one destroys it on purpose: neighbouring pages are unrelated locations. The rest of this paper is the ordered family, in every form it took, and what each form kept and lost."),
])
