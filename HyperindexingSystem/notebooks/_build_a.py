from _nb import md, code, write

# ---------------------------------------------------------------- v00 First Age
write("v00_first_age/01_mechanism.ipynb", "# v00 · First Age text hyperindex — mechanism\n`PtolemyDesktop/Archive/ainulindale_first_age/FA_smnnip_hyperindex.py` (in-file date: April 2026; git first commit 2026-04-18). Base-97 mixed-radix address + Fano base-7 path index, length stored separately.", [
md("## Load the file unmodified and run its own record function"),
code('''fa = load("PtolemyDesktop/Archive/ainulindale_first_age/FA_smnnip_hyperindex.py", "fa")
T = fa.TextHyperIndex
seq = "Hello, World!"
text_idx, fano_idx, n = T.index_record(seq)
print("text_index:", text_idx)
print("fano_index:", fano_idx)
print("length    :", n)
assert T.decode_text(text_idx, n) == seq and T.verify(seq)'''),
md("## The charset order is `a–z A–Z 0–9 punctuation space tab newline`\nThis is the order later carried into `ValaQuenta/modules/hyperwebster`."),
code('''print(fa.US_KEYBOARD_CHARS[:26], "...", repr(fa.US_KEYBOARD_CHARS[-3:]))
print("index of 'a':", fa.USKeyboardMap.encode("a"), "| space:", fa.USKeyboardMap.encode(" "), "| newline:", fa.USKeyboardMap.encode("\\n"))'''),
md("## This is not a bijection over strings: length is part of the address\nCharacter `a` has index 0, so every string of `a`s has integer 0. The stored `length` is what tells them apart. (The later versions v02 onward use *bijective* base-N and drop this need.)"),
code('''ids = {k: T.encode_text("a"*k) for k in (1, 2, 3, 10)}
print(ids)
assert set(ids.values()) == {0}
# distinct strings of the same length are still distinct
assert T.encode_text("ab") != T.encode_text("ba")'''),
md("## The Fano index is many-to-one by construction (`char_index % 7`)\nSeven classes only; measured on the corpus sample: how many distinct 4-character windows share a Fano index."),
code('''wins = {CORPUS[i:i+4] for i in range(len(CORPUS)-3)}
by_fano = {}
for w in wins: by_fano.setdefault(T.encode_fano(w), set()).add(w)
print("distinct 4-windows:", len(wins), "| distinct Fano indices:", len(by_fano), "| max windows sharing one Fano index:", max(len(v) for v in by_fano.values()))
assert len(by_fano) < len(wins)'''),
])
write("v00_first_age/02_ledger_and_selftest.ipynb", "# v00 · First Age — blockchain ledger and its own self-test", [
md("## The file's own `run_self_test()`"),
code('''fa = load("PtolemyDesktop/Archive/ainulindale_first_age/FA_smnnip_hyperindex.py", "fa")
ok = fa.run_self_test()
print("self-test returned:", ok)'''),
md("## The SHA-256-chained ledger: append, verify, tamper\nWritten to a temporary directory; the repo is not touched."),
code('''import tempfile, os, json
d = tempfile.mkdtemp()
L = fa.BlockchainLedger(os.path.join(d, "ledger"))
for i in range(3):
    idx, _, n = fa.TextHyperIndex.index_record("entry %d" % i)
    L.append("text", 0, i, idx, n, "R", 0.01 * i)
print("verify:", L.verify())
# tamper with block 1 on disk and verify again
p = os.path.join(d, "ledger.jsonl"); rows = [json.loads(x) for x in open(p)]
rows[1]["step"] = 99
open(p, "w").write("\\n".join(json.dumps(r) for r in rows) + "\\n")
print("after tamper:", L.verify())
assert L.verify()[0] is False'''),
])

# ---------------------------------------------------------------- v01 infinite-data
write("v01_flag_packet/01_mechanism.ipynb", "# v01 · Prototype: bijective base-N + flag-byte packet\n`PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/infinite-data.py` (git first commit 2026-04-18; position in the sequence inferred from the code, see wiki index).", [
md("## The file cannot be imported as-is\nIt reads `PTOL_ROOT` (undefined) at module level. The classes above that line are extracted verbatim and executed; nothing else is changed."),
code('''src = open(os.path.join(PROJ, "PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/infinite-data.py")).read()
cut = src.index("# TODO:SETTINGS")
ns = {}
try:
    exec(compile(src, "infinite-data.py", "exec"), {})
except NameError as e:
    print("whole file:", type(e).__name__, e)
exec(compile(src[:cut], "infinite-data.py[:cut]", "exec"), ns)
HW = ns["HyperWebster"]()
print("classes extracted:", [k for k in ns if k[0].isupper()])'''),
md("## The bijection: address 0 is the first character; addresses are shortlex ranks"),
code('''chars = HW.char_list
print("N =", HW.N)
for s in ["`", "1", "`1", "``"]:
    print(repr(s), "->", HW.point_to_text(s))
# shortlex: every one-character string precedes every two-character string
assert HW.point_to_text(chars[-1]) + 1 == HW.point_to_text(chars[0]*2)
for s in ["Hello, World!", "python3", CORPUS[:500]]:
    assert HW.regenerate_text(HW.point_to_text(s)) == s
print("round trips exact")'''),
md("## The 256-bit packet: 8-bit flag + 248-bit coordinate\nCapacity of the 248-bit coordinate field, computed exactly: the longest length L such that *every* string of length ≤ L has an address below 2²⁴⁸."),
code('''N = HW.N
def strings_up_to(L): return (N**(L+1) - N)//(N-1)
L = 0
while strings_up_to(L+1) <= 2**248: L += 1
print("every string up to length", L, "fits in 248 bits;", "length", L+1, "does not (all of them)")
print("log2(97) =", round(math.log2(N), 4), "bits/char ->", round(248/math.log2(N), 2), "chars by division")
assert HW.point_to_text("~"*L) < 2**248'''),
md("## `decode_packet` calls a method the class does not have"),
code('''U = ns["UniversalCoordinateSystem"](HW)
packet = (0 << 248) | HW.point_to_text("hello")
try:
    U.decode_packet(packet)
except AttributeError as e:
    print("AttributeError:", e)
print("flag 1 ->", U.decode_packet((1 << 248) | 5))
print("flag 2 ->", U.decode_packet(2 << 248))'''),
])

# ---------------------------------------------------------------- v02 hex address
write("v02_hex_address/01_mechanism.ipynb", "# v02 · 64-hex address, `(address_hex, length, timestamp)`\n`PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py` — the shipping baseline. Used by `hyperwebster_layer3.py` (git 2026-04-24), the VAPMIP baseline benchmark (2026-09-25), and every measurement in this paper.", [
code('''hw_mod = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py", "hw")
HW = hw_mod.HyperWebster()
print("N =", HW.N)
addr, n, ts = HW.index_text("Hello, World!")
print(addr, n, ts)
assert HW.regenerate_from_address(addr, n) == "Hello, World!"'''),
md("## Exact round trips on the corpus sample at several chunk sizes\nAddress size is compared with the raw 8-bit size."),
code('''rows = []
for size in (38, 140, 500, 1000, 2000, 4000):
    t = CORPUS[:size]
    t0 = time.perf_counter(); a = HW.point_to_text(t); t1 = time.perf_counter()
    back = HW.regenerate_text(a); t2 = time.perf_counter()
    assert back == t
    rows.append((size, a.bit_length(), round(a.bit_length()/(8*size), 3), round((t1-t0)*1e3, 2), round((t2-t1)*1e3, 2)))
print("chars  addr_bits  addr/raw  enc_ms  dec_ms")
for r in rows: print("%5d  %9d  %8.3f  %6.2f  %6.2f" % r)
print("log2(97)/8 =", round(math.log2(97)/8, 4))'''),
md("## The '256-bit' label is a minimum width, not a bound\nThe hex string is zero-padded to 64 digits; longer strings produce wider hex (the docstring says so)."),
code('''for size in (10, 38, 39, 40, 200):
    a, n, _ = HW.index_text(CORPUS[:size])
    print(size, "chars ->", len(a), "hex digits")
cap = max(k for k in range(1, 100) if 97**k <= 2**256)
print("largest k with 97^k <= 2^256:", cap, "(97^%d > 2^256)" % (cap+1))'''),
md("## Two loops, one address, very different cost\n`point_to_text` computes `N ** i` for every position i (`address += index * N**i`). A forward Horner loop (`address = address * N + index`, the form used in v05's `HyperIndex`, v09 and the ValaQuenta module) returns the identical integer with one small multiplication per character."),
code('''import random
rnd = random.Random(1)
def horner_forward(t, N=HW.N, idx=HW._char_index):
    a = 0
    for c in t: a = a * N + idx[c] + 1
    return a - 1
rows = []
for n in (1000, 2000, 4000, 8000, 16000):
    t = "".join(rnd.choice(HW.characters) for _ in range(n))
    a0 = time.perf_counter(); x = HW.point_to_text(t); a1 = time.perf_counter(); y = horner_forward(t); a2 = time.perf_counter()
    assert x == y
    rows.append((n, a1 - a0, a2 - a1))
print("chars   point_to_text s   forward Horner s   ratio")
for n, p, f in rows: print("%5d   %15.4f   %16.4f   %5.1f" % (n, p, f, p / f))
e = lambda k: math.log(rows[-1][k] / rows[0][k]) / math.log(rows[-1][0] / rows[0][0])
print("fitted exponent: point_to_text %.2f | forward Horner %.2f" % (e(1), e(2)))'''),
md("Between 1,000 and 16,000 characters the time grows as about n^2.5 for `point_to_text` (2.4–2.6 across runs) and n^1.8 for the forward loop, and the ratio between them widens with size. The 4.7–5.3× growth per doubling recorded by the VAPMIP baseline benchmark, which runs this class, is the first exponent."),
md("## Unrelated but on the same file\nThe module smoke-test reads `PTOL_ROOT`, which is undefined; the class itself is unaffected."),
code('''import inspect
print("PTOL_ROOT referenced in __main__ block:", "PTOL_ROOT" in inspect.getsource(hw_mod))
print("defined in module namespace:", hasattr(hw_mod, "PTOL_ROOT"))'''),
])

# ---------------------------------------------------------------- v03 hash label
write("v03_sha_label/01_mechanism.ipynb", "# v03 · SHA-256 label + base-N payload\n`PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster-hash.py`. The 64-character address becomes a hash; regeneration needs the payload.", [
code('''mod = load("PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster-hash.py", "hh")
HW = mod.HyperWebster()
rec = HW.index_text("Hello, World!")
print(rec.label, len(rec.label))
print(repr(rec.payload), rec.length)
assert HW.regenerate_from_record(rec) == "Hello, World!"'''),
md("## Label length is fixed; the payload is the address and grows like it"),
code('''print("chars  label  payload_chars  payload_bits(8/char)  raw_bits  payload/raw")
for size in (140, 1000, 4000):
    r = HW.index_text(CORPUS[:size])
    assert HW.regenerate_from_record(r) == CORPUS[:size]
    pb = 8*len(r.payload)
    print("%5d  %5d  %13d  %20d  %8d  %.3f" % (size, len(r.label), len(r.payload), pb, 8*size, pb/(8*size)))'''),
md("## The label alone cannot regenerate anything\nIt is SHA-256 of the integer address. Regeneration is the payload path; the label is a lookup key. (Payload chars use the keyboard-order charset, one digit per character, so `payload/raw` ≈ 1.0 at 8 bits per stored character; measured above.)"),
code('''r = HW.index_text("abc")
try:
    HW.regenerate(r.label, r.length)
except Exception as e:
    print(type(e).__name__, "-", str(e)[:80])
# with the label's own length supplied, the label decodes without complaint to an unrelated string
g = HW.regenerate(r.label, len(r.label))
print("label decoded as a payload ->", len(g), "chars, equals 'abc':", g == "abc")'''),
])
