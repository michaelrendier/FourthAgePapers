from _nb import md, code, write

# ---------------------------------------------------------------- v08 layer3
write("v08_layer3_shards/01_mechanism.ipynb", "# v08 · Layer 3: word records filed under their own address\n`PtolemyDesktop/Callimachus/hyperwebster_layer3.py` (git 2026-04-24, commit `3a5d7e6`). One JSON file per word, named by the v02 hex address, in a shard directory by first letter.", [
code('''l3 = load("PtolemyDesktop/Callimachus/hyperwebster_layer3.py", "l3")
import tempfile, pathlib
root = pathlib.Path(tempfile.mkdtemp())
B = l3.HyperWebsterLayer3(words_root=str(root))
n = B.ingest([("sedenion", 1000.0, "the sedenion is the I/O gate"),
              ("noether",  1001.0, "Noether conservation verified"),
              ("sedenion", 2000.0, "sedenion near zero divisor")])
print("records written/updated:", n)
p = B._record_path("sedenion")
print("file:", p.relative_to(root))
print("address_of('sedenion'):", B.address_of("sedenion"))
assert p.name == B.address_of("sedenion") + ".json"'''),
md("## The Rabies Principle at the Python level: `first_encountered` is written once"),
code('''r = B.lookup("sedenion")
print("hit_count:", r.hit_count, "| first_encountered:", r.first_encountered, "| timestamps:", r.timestamps, "| snippets:", len(r.snippets))
assert r.first_encountered == 1000.0 and r.hit_count == 2'''),
md("## Lookup is a computation, not a search\nThe path of a word is derived from the word; there is no index to consult. Two words never share a path (the address is a bijection), so no collision handling exists or is needed, **for words inside the charset**."),
code('''import itertools
words = ["a", "aa", "b", "sedenion", "Sedenion", "sedenion ", "0", "00"]
paths = [B._record_path(w).name for w in words]
print(len(set(paths)), "distinct filenames for", len(words), "words")
assert len(set(paths)) == len(words)'''),
])
write("v08_layer3_shards/02_outside_the_charset.ipynb", "# v08 · Words outside the charset are filed by spelling, not by address", [
code('''l3 = load("PtolemyDesktop/Callimachus/hyperwebster_layer3.py", "l3")
import tempfile, pathlib
root = pathlib.Path(tempfile.mkdtemp())
B = l3.HyperWebsterLayer3(words_root=str(root))
print("address_of('naïve'):", B.address_of("naïve"))       # None: 'ï' is not in the 97-symbol set
print("path:", B._record_path("naïve").name, "| in-charset path:", B._record_path("naive").name[:20] + "...")
# a word with symbols that are neither in the charset nor word characters is squashed to underscores
B.ingest([("a€b", 1.0, "first"), ("a£b", 2.0, "second")])
print(B._record_path("a€b").name, "|", B._record_path("a£b").name)
r = B.lookup("a€b")
print("record for 'a€b': word =", repr(r.word), "| hit_count =", r.hit_count)
assert B._record_path("a€b") == B._record_path("a£b") and r.hit_count == 2'''),
md("Inside the charset the filename is the address, so two words never share a file. Outside it the fallback is `re.sub(r'[^\\w]', '_', word)`: letters such as `ï` survive (Python's `\\w` is Unicode-aware), symbols such as `€` and `£` both become `_`, so `a€b` and `a£b` land in one file and the second overwrites nothing but increments the first's hit count. The exact bijection covers only the 97-symbol charset. v09 (Unicode public charset in `charset.py`) is the later answer."),
])

# ---------------------------------------------------------------- v09 Callimachus v09
V9 = '''import sys
sys.path.insert(0, os.path.join(PROJ, "PtolemyDesktop"))
from Callimachus.v09.core.hyperwebster import HyperWebster as HW9
from Callimachus.v09.core import charset as cs
from Callimachus.v09.core.lsh_datatype import LSH_Datatype
from Callimachus.v09.database.hyperdatabase import HyperDatabase
from Callimachus.v09.gallery import hypergallery as hg9'''
write("v09_callimachus_v09/01_core_database_datatype.ipynb", "# v09 · Callimachus v0.9: Unicode public charset, SHA label as primary key, SQLite store\n`PtolemyDesktop/Callimachus/v09/` (git 2026-05-02).", [
code(V9),
md("## Core: `IndexRecord(label, payload, length, timestamp)`"),
code('''hw = HW9()
rec = hw.index("Hello, World!")
print(rec.label, "|", repr(rec.payload), "|", rec.length)
assert hw.regenerate(rec.payload, rec.length) == "Hello, World!"
print("N =", hw.N, "| first three symbols:", [repr(c) for c in cs.PUBLIC_CHARSET[:3]], "| last:", repr(cs.PUBLIC_CHARSET[-1]))
for size in (140, 1000, 4000):
    r = hw.index(CORPUS[:size]); assert hw.regenerate(r.payload, r.length) == CORPUS[:size]
print("round trips exact at 140/1000/4000 chars")'''),
md("## Database: label is the primary key; `first_encountered` lives on the datatype"),
code('''db = HyperDatabase(":memory:")
lsh = LSH_Datatype.from_acquisition(rec.label, "Hello", "hello", "interj")
db.put(rec, lsh)
print("exists:", db.exists(rec.label), "| count:", db.count(), "| incomplete:", db.count_incomplete())
got = db.get(rec.label); print(got)
try: got.first_encountered = "x"
except AttributeError as e: print("write to first_encountered ->", e)
try: got.set_layer(0, "x")
except PermissionError as e: print("write to layer 0 ->", e)
got.set_layer(7, [0.1, 0.2]); print("layer 7 writable, value:", got.get_layer(7))'''),
md("## Master label of the JSON index"),
code('''idx = hg9.HyperIndex()
spec = hg9.ImageSpec(8, 8, hg9.PixelMode.GRAY8)
g = hg9.HyperGallery(spec); r = g.index_image(list(range(64)), "ramp"); idx.add_image_record(r)
print("master_label:", idx.master_label(), "| records:", idx.record_count())'''),
])
write("v09_callimachus_v09/02_charset_order_and_defects.ipynb", "# v09 · Charset order, and three things v09 does not do", [
code(V9),
md("## The charset order is the only variable, and the code carries three\nSame 97 symbols, three orders: keyboard-row (v01–v07), Unicode codepoint (v09), and `a–z A–Z 0–9…` (v00 and the ValaQuenta module). One string, three integers."),
code('''kb = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "kb").HyperWebster()
vq = load("ValaQuenta/modules/hyperwebster/maths.py", "vq")
uni = HW9()
def addr_vq(s):                                # bijective form, ValaQuenta order, for comparison
    N = 97; a = 0
    for c in s: a = a*N + vq.US_KEYBOARD_CHARS.index(c) + 1
    return a - 1
for w in ("hello", "Ptolemy"):
    print(w, "| keyboard-row:", kb.point_to_text(w), "| Unicode:", uni.address_int(w), "| a-z first:", addr_vq(w))
assert len({kb.point_to_text("hello"), uni.address_int("hello"), addr_vq("hello")}) == 3
# the permutation between two of the orders
sig = [cs.PUBLIC_CHARSET.index(c) for c in kb.characters]
seen, cyc = set(), []
for i in range(97):
    if i in seen: continue
    j, n = i, 0
    while j not in seen: seen.add(j); j = sig[j]; n += 1
    cyc.append(n)
print("keyboard-row -> Unicode permutation, cycle type:", sorted(cyc, reverse=True), "| fixed points:", cyc.count(1), "| order:", math.lcm(*cyc))'''),
md("## `_pixels_to_int` carries a dead stub loop; the image cache still keys on a prefix"),
code('''import inspect
src = inspect.getsource(hg9.HyperGallery._pixels_to_int)
print("dead stub present ('if False'):", "if False" in src)
s = hg9.ImageSpec(8, 8, hg9.PixelMode.GRAY8); G = hg9.HyperGallery(s)
a = [0]*64; b = [0]*64; b[63] = 200
ra, rb = G.index_image(a), G.index_image(b)
print("first-32-values cache: labels equal for different images:", ra.label == rb.label, "| regenerate(b) == b:", G.regenerate_image(rb) == b)'''),
md("## The SQLite 'Rabies' trigger never fires\nIt is declared `BEFORE UPDATE OF first_encountered ON words`; the table has no such column, and SQLite accepts the declaration without complaint."),
code('''import sqlite3
c = sqlite3.connect(":memory:"); c.executescript(__import__("Callimachus.v09.database.hyperdatabase", fromlist=["_SCHEMA"])._SCHEMA)
print("columns:", [r[1] for r in c.execute("PRAGMA table_info(words)")])
c.execute("INSERT INTO words VALUES('a','p',1,'t0',NULL,0)")
c.execute("UPDATE words SET indexed_at='changed' WHERE label='a'")
print("indexed_at after UPDATE:", c.execute("SELECT indexed_at FROM words").fetchone()[0])
assert c.execute("SELECT indexed_at FROM words").fetchone()[0] == "changed"'''),
md("`HyperDatabase.put` avoids touching `indexed_at` on conflict, so in practice the timestamp is kept by the SQL in `put`, not by the trigger."),
])

# ---------------------------------------------------------------- v10 kcf
write("v10_kcf/01_key_derivation.ipynb", "# v10 · KCF-1: HyperWebster address → HKDF key material\n`PtolemyDesktop/Kryptos/kcf.py` (git 2026-05-03).", [
code('''import sys
sys.path.insert(0, os.path.join(PROJ, "PtolemyDesktop"))
kcf = load("PtolemyDesktop/Kryptos/kcf.py", "kcf")
K = kcf.KCF(face_id="callimachus")
k1 = K.derive("hiraeth"); k2 = K.derive("hiraeth"); k3 = K.derive("hiraeth ")
print(k1.hex()[:32], len(k1), "| deterministic:", k1 == k2, "| trailing space changes key:", k1 != k3)'''),
md("## `hw_address` is not the bijection\nIt is a plain base-N numeral with a zero digit (index 0 = first charset symbol), and unknown characters fall back to `ord(ch) % N`. Both make distinct labels share an address."),
code('''cs0 = K.charset[0]
print("first charset symbol:", repr(cs0))
print("hw_address(cs0+'x') == hw_address('x'):", K.hw_address(cs0 + "x") == K.hw_address("x"))
print("hw_address('é') == hw_address('%s'):" % chr(ord("é") % 97 and 0) if False else "", end="")
alias = next(c for c in K.charset if K.charset.index(c) == ord("é") % len(K.charset))
print("hw_address('é') == hw_address(%r):" % alias, K.hw_address("é") == K.hw_address(alias))
assert K.hw_address(cs0 + "x") == K.hw_address("x")'''),
md("## The 'permutation offset' is a hash of the charset string, folded modulo a Mersenne prime\n`_permute` XORs the address with 64 bits of SHA-256(charset), multiplies by 2⁶¹−1 and reduces mod 2⁸⁹−1. The output is below 2⁸⁹ whatever the label length; HKDF then turns it into key bytes."),
code('''big = "x" * 200
a = K.hw_address(big); m = K._permute(a)
print("address bits:", a.bit_length(), "| _permute output bits:", m.bit_length(), "(< 89)")
assert m.bit_length() <= 89
# two labels far apart in address space can still differ; the map is not the N! permutation index charset.py describes
print("charset-order dependence: same label, charset reversed ->",
      kcf.KCF("callimachus", charset=K.charset[::-1]).derive("hiraeth") != k1)'''),
])
write("v10_kcf/02_permutation_index.ipynb", "# v10 · The piece `charset.py` names and the repo does not contain: a permutation index in [0, N!−1]\n`v09/core/charset.py` says PRIVATE mode takes 'a permutation index (integer in [0, N!−1])'. No code in the repo converts between such an integer and a charset order. Below: Myrvold & Ruskey (2001) `rank1`/`unrank1`, written from the paper's pseudocode (read in full), checked against the paper's own n=4 table.", [
code('''def unrank1(n, r, pi=None):
    pi = list(range(n)) if pi is None else pi
    while n > 0:
        pi[n-1], pi[r % n] = pi[r % n], pi[n-1]
        r //= n; n -= 1
    return pi
def rank1(pi):
    pi = list(pi); n = len(pi); inv = [0]*n
    for i, v in enumerate(pi): inv[v] = i
    r, mult = 0, 1
    for m in range(n, 1, -1):
        s = pi[m-1]
        pi[m-1], pi[inv[m-1]] = pi[inv[m-1]], pi[m-1]
        inv[s], inv[m-1] = inv[m-1], inv[s]
        r += s * mult; mult *= m
    return r
# the first eight rows of Fig. 1 of the paper (n = 4), transcribed
fig1 = {0: (1,2,3,0), 1: (3,2,0,1), 2: (1,3,0,2), 3: (1,2,0,3), 4: (2,3,1,0), 5: (2,0,3,1), 6: (3,0,1,2), 7: (2,0,1,3)}
assert all(tuple(unrank1(4, r)) == p for r, p in fig1.items())
assert sorted(rank1(unrank1(4, r)) for r in range(24)) == list(range(24))
print("n=4: unrank1 reproduces Fig. 1 rows 0-7; rank1∘unrank1 is a bijection on 0..23")'''),
md("## At N = 97: the key is an integer of about 505 bits"),
code('''import random
N = 97; F = math.factorial(N)
print("97! has", F.bit_length(), "bits")
rnd = random.Random(2026)
r = rnd.randrange(F)
pi = unrank1(N, r)
assert sorted(pi) == list(range(N)) and rank1(pi) == r
print("rank of a random charset order:", str(r)[:30] + "...", "(%d bits)" % r.bit_length())
# use it as a private charset with the v02 addressing class
hw2 = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw2")
pub = hw2.HyperWebster(); base = pub.characters
priv = hw2.HyperWebster("".join(base[i] for i in pi))
t = "The private order is a substitution"
print("public address :", pub.point_to_text(t))
print("private address:", priv.point_to_text(t))
assert priv.regenerate_text(priv.point_to_text(t)) == t'''),
md("Both directions are O(N) big-integer-free steps until the final integer. This is the missing conversion; `kcf.py` derives key bytes from a *hash* of the charset instead, so a charset order and a permutation index do not correspond in the current code."),
])

# ---------------------------------------------------------------- v11 semantic zero ordinal
write("v11_semantic_ordinal/01_mechanism.ipynb", "# v11 · Semantic address: surface form → Riemann-zero ordinal\n`SemanticWordEngine/hyperwebster.py` (git 2026-05-12). Not the exact bijection: a many-to-one map from a word to one of N zeros.", [
code('''sw = load("SemanticWordEngine/hyperwebster.py", "sw")
monad = load("VAPMIP/monad.py", "monad")
zeros = {k: v for k, v in monad._ZERO_CACHE.items() if k <= 50}          # first 50 exact zeros
lex = sw.Lexicon(zeros, path="/dev/null")
for w in ["listen", "silent", "enlist", "tinsel", "Listen", "hello"]:
    print("%-8s _hash = %-28s address = %s" % (w, sw._hash(w), lex.address_of(w)))'''),
md("`_hash` is `(mean token length, (Σ ord) mod 360 / 360)`. A sum is unchanged by any permutation of the characters, so **every anagram of a word has the same address**: the map is constant on each orbit of the position-permutation group. That is the opposite of the exact address (v02), which separates every string."),
code('''assert lex.address_of("listen") == lex.address_of("silent") == lex.address_of("enlist") == lex.address_of("tinsel")
import re
words = sorted(set(re.findall(r"[a-z]+", CORPUS.lower())))
addrs = Counter(lex.address_of(w)[0] for w in words)
ts = {round(sw._hash(w)[1], 6) for w in words}
print("distinct words:", len(words), "| distinct t values:", len(ts), "(at most 360) | distinct zero ordinals:", len(addrs), "of 50 | largest bucket:", max(addrs.values()))
assert len(ts) <= 360'''),
md("With 50 zeros the address space has 50 cells; the corpus words are spread over them and many share a cell by construction. The file's own `N_ZEROS` is 200. A many-to-one map is the intended behaviour of a *semantic* address (synonyms share a zero); the anagram invariance is a side effect of the choice of `Σ ord`."),
])

# ---------------------------------------------------------------- v12 prime zero index
write("v12_prime_zero_index/01_mechanism.ipynb", "# v12 · Prime zero index: Horner base-95 → next prime → π(p)\n`VAPMIP/monad.py` `_horner_hash`, `_next_prime`, `_word_zero_idx` (git 2026-05-19; `_word_zero_idx` byte-identical since commit `204c75d`, 2026-05-27).", [
code('''mo = load("VAPMIP/monad.py", "mo")
for w in ["a", "listen", "silent", "Listen", "hyperwebster"]:
    h = mo._horner_hash(w); p = mo._next_prime(h)
    print("%-13s horner=%-26d next_prime=%-6d zero_idx=%d" % (w, h, p, mo._word_zero_idx(w)))
print("index range:", min(mo._prime_pi_table[2:]), "to", max(mo._prime_pi_table), "| prime cap:", mo._PRIME_CAP)'''),
md("The Horner integer is order-sensitive (unlike v11's sum), so anagrams get different integers. Two things then make the map many-to-one: `_next_prime` rounds up to the next prime (so neighbouring integers share an index, even for single letters), and it first reduces the integer modulo the prime cap + 1 (a word of three or more characters already exceeds the cap). The result is one of at most 6,543 zero indices."),
md("## Exhaustive collision count: every lowercase word of length ≤ 3"),
code('''from itertools import product
import string
words = ["".join(p) for n in (1, 2, 3) for p in product(string.ascii_lowercase, repeat=n)]
idx = Counter(mo._word_zero_idx(w) for w in words)
print(len(words), "words ->", len(idx), "distinct zero indices; largest bucket:", max(idx.values()))
assert len(idx) < len(words)          # pigeonhole: 18,278 words, at most 6,542 slots
lens = Counter(len(w) for w in words)
by_len = {n: len({mo._word_zero_idx(w) for w in words if len(w) == n}) for n in (1, 2, 3)}
print("distinct indices by word length:", by_len, "| words by length:", dict(lens))'''),
md("This is the lossy semantic hash the paper keeps separate from the exact bijection: it cannot be inverted (many words per index), and it is used as a *lookup key into the zeros*, never as a storage address."),
])
