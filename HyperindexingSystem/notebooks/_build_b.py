from _nb import md, code, write
HW_DIR = "PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/"

# ---------------------------------------------------------------- v04 vector + orbit
write("v04_vector_orbit/01_vector_address.ipynb", "# v04 · VectorAddress (uint32 limbs)\n`infinite-data-vector-shaders.py` — the integer address as a little-endian array of 32-bit words, sized for a GPU buffer.", [
code('''vs = load("__HW__infinite-data-vector-shaders.py", "vs")
VA = vs.VectorAddress
B = vs._Bijection()
for size in (13, 140, 1000, 4000):
    a = B.str_to_int(CORPUS[:size]); va = VA.from_integer(a, size)
    assert va.to_integer() == a and VA.from_label(va.to_label(), size).to_integer() == a
    print("%5d chars  %6d bits  %4d words  %3d uvec4  label %d chars" % (size, a.bit_length(), va.num_words, va.num_uvec4s, len(va.to_label())))
print(VA.from_integer(0xdeadbeefcafe, 1).to_label())'''.replace("__HW__", HW_DIR)),
md("Every 32-bit word is written as 8 hex digits and joined by `_`; the label is 9 characters per word, so it is **larger** than the plain hex address it encodes (8 digits per word plus a separator)."),
code('''va = VA.from_integer(B.str_to_int(CORPUS[:1000]), 1000)
plain_hex = format(va.to_integer(), "x")
print("plain hex digits:", len(plain_hex), "| label chars:", len(va.to_label()))'''),
])
write("v04_vector_orbit/02_orbit_cache.ipynb", "# v04 · OrbitCache: what the code does and what its docstring describes", [
code('''vs = load("__HW__infinite-data-vector-shaders.py", "vs")
HW = vs.HyperWebster()
for t in ["listen", "silent", "enlist", "listen", "tinsel", "listen"]:
    HW.index_text(t)
print(HW.cache_stats())'''.replace("__HW__", HW_DIR)),
md("**What it does:** an exact-string cache plus a bookkeeping list of strings that are anagrams (same sorted letters). `listen`, `silent`, `enlist`, `tinsel` are one orbit under permutation of positions; each gets its own address, each computed by the full bijection. The module docstring describes reaching other orbit members 'by a cheap integer offset'; that offset is not implemented."),
code('''B = vs._Bijection()
addrs = {t: B.str_to_int(t) for t in ["listen", "silent", "enlist", "tinsel"]}
print(addrs)
print("hit rate above counts only exact repeats:", HW.cache_stats()["hit_rate"])'''),
md("## The offset that *does* exist: a transposition\nSwapping the characters at positions i < j changes the address by a closed form: `(d_j − d_i)·(N^(L−1−i) − N^(L−1−j))`, with `d = index + 1`. Checked here on a 500-character string."),
code('''import random
rnd = random.Random(7)
t = "".join(rnd.choice(B.char_list) for _ in range(500)); L = len(t); N = B.N
i, j = 17, 333
u = list(t); u[i], u[j] = u[j], u[i]; u = "".join(u)
d = lambda c: B._char_index[c] + 1
offset = (d(t[j]) - d(t[i])) * (N**(L-1-i) - N**(L-1-j))
assert B.str_to_int(u) == B.str_to_int(t) + offset
print("transposition offset identity holds; |offset| bits:", abs(offset).bit_length(), "| address bits:", B.str_to_int(t).bit_length())'''),
])
write("v04_vector_orbit/03_glsl_source.ipynb", "# v04 · The GLSL shader text (generated, not executed)", [
code('''vs = load("__HW__infinite-data-vector-shaders.py", "vs")
G = vs.GLSLAddressEngine()
src = G.regeneration_shader(64)
print(len(src.splitlines()), "lines;", len(src), "chars")
print(src[:420])'''.replace("__HW__", HW_DIR)),
md("No GL context is available in this environment, so the shader is generated and inspected but **not run**. Whether it applies the bijective `−1` step can be read from the text:"),
code('''lines = [l for l in src.splitlines() if "- 1" in l or "-1" in l or "bijective" in l.lower() or "+ 1" in l]
print("\\n".join(lines[:12]) or "(no such line)")'''),
md("## The generated text still contains doubled braces\nA `{{` in GLSL source is not valid; it is the escape form of a Python `str.format` template that was filled with `str.replace` instead."),
code('''dbl = [l.strip() for l in src.splitlines() if "{{" in l or "}}" in l]
print(len(dbl), "lines with doubled braces, e.g.:", dbl[:2])
assert dbl'''),
])

# ---------------------------------------------------------------- v05 gallery
write("v05_gallery/01_mechanism.ipynb", "# v05 · HyperGallery: images and cubes as addresses; the JSON master index\n`hypergallery.py` (Data-Storage copy).", [
code('''hg = load("__HW__hypergallery.py", "hg")
def roundtrip(spec, vals, tag):
    G = hg.HyperGallery(spec); rec = G.index_image(vals, tag)
    assert G.regenerate_image(rec) == vals
    print("%-22s n_values=%7d  address words=%5d  bits(spec)=%d" % (tag, spec.n_values, len(rec.label.split("_")), spec.address_bits))
    return rec
r1 = roundtrip(hg.ImageSpec(106, 17, hg.PixelMode.BINARY), [(i + j) % 2 for j in range(17) for i in range(106)], "binary 106x17")
r2 = roundtrip(hg.ImageSpec(64, 64, hg.PixelMode.GRAY8), [(i * 255 // 4096) for i in range(4096)], "gray8 64x64")
r3 = roundtrip(hg.ImageSpec(16, 16, hg.PixelMode.SPECTRAL, n_bands=50, bit_depth=16), [(x + y + k * 7) % 65536 for y in range(16) for x in range(16) for k in range(50)], "IFU 16x16x50x16bit")'''.replace("__HW__", HW_DIR)),
md("The address of an image with n values at depth D is a base-D numeral with n digits: `n·log₂D` bits. That is the size of the image itself; nothing is saved. The address exists whether or not the image was ever recorded."),
md("## The JSON master index: many records → one address"),
code('''idx = hg.HyperIndex()
for r in (r1, r2, r3): idx.add_image_record(r)
js = idx.to_json(); m = idx.master_address()
back = idx.regenerate_from_master(m)
assert len(back["image_records"]) == 3
print("index JSON:", len(js), "chars ->", m.num_words, "uint32 words =", m.num_words*32, "bits;", "ratio to raw JSON bits:", round(m.num_words*32/(8*len(js)), 3))'''),
])
write("v05_gallery/02_spectral_search_and_cache.ipynb", "# v05 · Two defects in HyperGallery, each demonstrated by brute force", [
md("## 1. `spectral_address_range` (the JWST search function)\nIt returns one interval `[addr_mid − δ, addr_mid + δ]` meant to bound every image whose bands lie in given ranges. Checked exhaustively on a spec small enough to enumerate: 2×2 pixels, 2 bands, 2-bit depth (4⁸ = 65,536 images)."),
code('''import itertools
hg = load("__HW__hypergallery.py", "hg")
s = hg.ImageSpec(2, 2, hg.PixelMode.SPECTRAL, n_bands=2, bit_depth=2)
G = hg.HyperGallery(s)
cons = {0: (1, 2)}                       # band 0 in [1,2] at every pixel
lo, hi = G.spectral_address_range(cons)
sat, inr = [], []
for v in itertools.product(range(4), repeat=s.n_values):
    a = G._pixels_to_int(list(v))
    ok = all(cons[0][0] <= v[px*2] <= cons[0][1] for px in range(4))
    if ok: sat.append(a)
    if lo <= a <= hi: inr.append(ok)
runs = 1 + sum(1 for x, y in zip(sorted(sat), sorted(sat)[1:]) if y != x + 1)
print("range:", lo, hi, "width", hi - lo + 1)
print("images satisfying the constraint:", len(sat))
print("  of those inside the returned range:", sum(lo <= a <= hi for a in sat))
print("images inside the range:", len(inr), "| of those satisfying:", sum(inr))
print("the satisfying set is", runs, "disjoint runs of consecutive addresses")
assert sum(lo <= a <= hi for a in sat) < len(sat)'''.replace("__HW__", HW_DIR)),
md("**Why:** pixel values are laid out pixel-major, band-minor, and the address is lexicographic in that digit order. Fixing band 0 at every pixel fixes digits scattered through the whole string, including the leading ones, so the satisfying set is a product set spread over many intervals. A correct search returns a union of intervals (or reorders the digits so the constrained band leads)."),
md("## 2. `index_image` caches by the first 16 values"),
code('''s = hg.ImageSpec(8, 8, hg.PixelMode.GRAY8); G = hg.HyperGallery(s)
a = [0]*64; b = [0]*64; b[63] = 200                       # differ only in the last pixel
ra = G.index_image(a, "a"); rb = G.index_image(b, "b")
print("labels equal:", ra.label == rb.label)
print("regenerate(b) == b:", G.regenerate_image(rb) == b, "| regenerate(b) == a:", G.regenerate_image(rb) == a)
assert ra.label == rb.label'''),
])

# ---------------------------------------------------------------- v06 manifold
write("v06_manifold/01_character_manifold.ipynb", "# v06 · Character manifold: per-symbol position sub-addresses\n`hyperwebster_manifold.py`.", [
code('''mf = load("__HW__hyperwebster_manifold.py", "mf")
M = mf.CharacterManifold()
rows = []
for L in (140, 1000, 4000):
    t = CORPUS[:L]; ma = M.decompose(t); assert M.reconstruct(ma) == t
    c = Counter(t)
    Mn = math.factorial(L)
    for k in c.values(): Mn //= math.factorial(k)
    floor = Mn.bit_length() - 1
    rows.append((L, round(L*math.log2(97)), ma.total_sub_bits(), floor, ma.n_active))
print("    L   naive_bits  sum(sub_bits)  log2(multinomial)  active_dims")
for r in rows: print("%5d  %10d  %13d  %17d  %11d" % r)'''.replace("__HW__", HW_DIR)),
md("`sum(sub_bits)` is the sum of `⌈log₂ C(L, cₖ)⌉` over symbols k: each symbol's positions are ranked among *all* L positions, ignoring the positions already taken by the other symbols. The exact number of distinct strings with these symbol counts is the multinomial, and its log₂ (last-but-one column) is smaller. Notebook 03 builds the exact address."),
])
write("v06_manifold/02_vocabulary_factorization.ipynb", "# v06 · Vocabulary factorization: reported reduction vs. what has to be stored", [
code('''mf = load("__HW__hyperwebster_manifold.py", "mf")
V = mf.VocabFactorizer()
print("     L  reported  naive_bits  token_bits  +vocab_bits  +punct_bits  total   real_ratio")
for L in (47, 1000, 4000):
    t = CORPUS[:L]; va = V.encode(t); assert V.decode(va) == t
    r = va.bit_report(t)
    vocab_bits = sum(len(w) + 1 for w in va.vocab) * math.log2(97)               # vocabulary listed as text, 97-symbol charset
    punct_bits = sum(len(s) * math.log2(97) + math.log2(max(va.word_count, 2)) for _, s in va.punct_mask)
    total = r["vocab_token_bits"] + vocab_bits + punct_bits
    print("%6d  %8s  %10d  %10d  %11.0f  %11.0f  %6.0f  %.2f" % (L, r["reduction_factor"], r["naive_char_bits"], r["vocab_token_bits"], vocab_bits, punct_bits, total, r["naive_char_bits"]/total))'''.replace("__HW__", HW_DIR)),
md("The reported factor counts only the token-sequence address. The vocabulary and the punctuation spans are needed to decode and are not in it. With them counted (vocabulary and punctuation costed as text over the 97-symbol charset: an estimate, stated as such) the stored size exceeds the naive size. The round trip is exact in every row."),
])
write("v06_manifold/03_exact_multiset_rank.ipynb", "# v06 · The exact form of what the manifold approximates: (count vector, rank in the anagram class)\nNot in the repo; written here. Each string is an arrangement of a multiset; its address is the pair (counts, rank among the distinct arrangements).", [
code('''N = 97
chars = load("__HW__hyperwebster.py", "hw").HyperWebster._DEFAULT_CHARS
idx = {c: i for i, c in enumerate(chars)}
def rank(text):
    c = Counter(text); syms = sorted(c, key=lambda ch: idx[ch]); m = len(text)
    P = math.factorial(m)
    for k in c.values(): P //= math.factorial(k)
    r = 0
    for ch in text:
        below = sum(c[x] for x in syms if idx[x] < idx[ch])
        r += P * below // m
        P = P * c[ch] // m; c[ch] -= 1; m -= 1
    return r
def unrank(r, counts, L):
    c = dict(counts); syms = sorted(c, key=lambda ch: idx[ch]); m = L
    P = math.factorial(m)
    for k in c.values(): P //= math.factorial(k)
    out = []
    for _ in range(L):
        for x in syms:
            if c[x] == 0: continue
            w = P * c[x] // m
            if r < w: out.append(x); P = w; c[x] -= 1; m -= 1; break
            r -= w
    return "".join(out)
# exhaustive check on a small multiset: every arrangement of 'aabbc' gets a distinct rank 0..29
from itertools import permutations
arr = sorted(set("".join(p) for p in permutations("aabbc")))
ranks = sorted(rank(a) for a in arr)
print(len(arr), "arrangements; ranks are exactly 0..%d:" % (len(arr)-1), ranks == list(range(len(arr))))
assert all(unrank(rank(a), Counter(a), 5) == a for a in arr)'''.replace("__HW__", HW_DIR)),
code('''print("     L   naive  log2(multinomial)  +count-vector  total  total/naive  round-trip")
for L in (140, 1000, 4000):
    t = CORPUS[:L]; c = Counter(t); r = rank(t)
    Mn = math.factorial(L)
    for k in c.values(): Mn //= math.factorial(k)
    mult = Mn.bit_length() - 1
    cnt = math.comb(L + N - 1, N - 1).bit_length() - 1        # index of the count vector among all compositions of L into 97 parts
    print("%6d  %6d  %17d  %13d  %5d  %11.3f  %s" % (L, round(L*math.log2(N)), mult, cnt, mult+cnt, (mult+cnt)/(L*math.log2(N)), unrank(r, c, L) == t))'''),
md("Exact, reversible, and the count vector is paid for. The result is the order-0 entropy of the text: it wins because the corpus is not uniform over 97 symbols, not because the addressing is cleverer."),
])

# ---------------------------------------------------------------- v07 archimedes
write("v07_archimedes/01_geometry.ipynb", "# v07 · Archimedes geometry: the n-ball volume and where it peaks\n`hyperwebster_archimedes.py`, class `ArchimedesGeometry`.", [
code('''ar = load("__HW__hyperwebster_archimedes.py", "ar")
AG = ar.ArchimedesGeometry
# locate the maximum of V(n) = pi^(n/2) / Gamma(n/2 + 1) by golden-section search
f = lambda n: AG.log_vol(n)
a, b = 3.0, 8.0; g = (math.sqrt(5) - 1) / 2
c, d = b - g*(b-a), a + g*(b-a)
for _ in range(80):
    if f(c) > f(d): b = d
    else: a = c
    c, d = b - g*(b-a), a + g*(b-a)
peak = (a + b) / 2
print("numerical peak of the unit n-ball volume: n =", round(peak, 4))
print("code's peak_dimension() returns        :", round(AG.peak_dimension(), 4), "(= 2π − 1)")'''.replace("__HW__", HW_DIR)),
md("The module carries three different statements of the peak: the docstring's 'n~5', the method docstring's '~4.93', and `2π − 1 = 5.283` in the return value. The measured maximum is 5.2569. The return value is off by 0.026, the method docstring by 0.32."),
code('''for n in (5, 5.2569, 97):
    print(n, "log10(ball/cube) =", round(AG.log_fraction_of_cube(n), 3))
print("readable_fraction_estimate(1000):", round(AG.readable_fraction_estimate(1000), 1), "(log10, assumes 4.5 bits/char English entropy)")'''),
])
write("v07_archimedes/02_svd_boundary_calculus.ipynb", "# v07 · SVD dimension reducer, boundary filter, letter↔word 'calculus'", [
code('''ar = load("__HW__hyperwebster_archimedes.py", "ar")
E = ar.HyperWebsterArchimedes()
t = CORPUS[:2000]
E.fit(t); rep = E.analyse(t)
print("SVD:", rep["svd_reduction"]["independent_dims"], "of", rep["svd_reduction"]["total_char_dims"], "dims kept |", rep["svd_reduction"]["compression_ratio"])
print("pipeline estimate:", rep["total_pipeline_savings"])
basis = set(E._svd.basis)
covered = sum(1 for ch in t if ch in basis) / len(t)
print("fraction of the text's characters that lie inside the kept basis:", round(covered, 3))
assert covered < 1.0'''.replace("__HW__", HW_DIR)),
md("The reducer keeps the k most frequent characters. The estimate treats the dropped dimensions as free; the text outside the basis cannot be represented in it, so the reduction is lossy, and it is only ever an estimate (`_estimate_total_savings`); no encoder in the file uses it."),
md("## The boundary filter prunes legal inputs"),
code('''bf = ar.BoundaryFilter()
for label, s in [("all z", "z"*40), ("corpus sample", CORPUS[:2000]), ("every symbol once", ar.HyperWebsterArchimedes()._char_idx and "".join(ar._DEFAULT_CHARS))]:
    inside, why, st = bf.is_inside_boundary(s)
    print("%-18s inside=%-5s entropy=%.2f  %s" % (label, inside, st["entropy_bits_per_char"], why))'''),
md("`zzzz…` and a string using every symbol once are valid strings with valid addresses; the filter would prune them. It is a heuristic about English-like text, not a property of the address space."),
md("## Letter ↔ word shift: exact round trip"),
code('''dc = ar.DiscreteCalcShift()
for size in (200, 1000, 2000):
    tx = CORPUS[:size]; w = dc.integrate(tx)
    assert dc.differentiate(w) == tx
    print(size, "chars | tokens:", len(w.token_ids), "| vocab:", w.vocab_size, "| reported reduction:", w.summary()["reduction_factor"])'''),
])
