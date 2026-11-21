#!/usr/bin/env python3
"""dstar_symbols.py (2026-11-21): reads data/census.csv.gz and counts, per symbol, which VALUE the record ties it to, against the author's standing ruling (@RCCM_SYMBOLS):
   α (lowercase) = fine-structure 1/137.036 ; A_π = Lambert W 0.5671 (Fermat, inertia, speed of causality) ; Ω_ζΣ = Ω_RZ = d* 0.2463 (Riemann, Hagedorn, entropy).
A line is 'tied' to a value when that value (or its words) is on the same line. Writes data/symbol_ties.json and data/traces_swap.csv (every line where the record contradicts the ruling)."""
import csv, gzip, json, re, collections
RULE = {"A_π": "W1", "Ω_ζΣ": "dstar", "α": "alpha"}
def canon(tok):
    t = tok.replace("Α", "A")
    if re.match(r"(A_pi|A_PI|A_π|Alpha_pi|Alpha_Fermat|ALPHA_FERMAT|A_fermat|A_FERMAT)$", t): return "A_π"
    if re.match(r"(Omega_ZS|OMEGA_ZS|Omega_zS|Ω_ζΣ|Ω_ZS|Ω_ζ|Omega_Riemann|OMEGA_RIEMANN|Omega_RZ|OMEGA_RZ|Ω_RZ)$", t): return "Ω_ζΣ"
    return None
W1 = re.compile(r"Lambert|W\(1\)|0?\.5671|fixed point of x|W e\^W|x ?e\^x ?= ?1", re.I); DS = re.compile(r"0?\.246\d*|\bd\*|D_STAR|log10|digit ceiling|digits? ", re.I); AL = re.compile(r"137|fine.structure|α_fs|alpha_fs|Wyler|CODATA", re.I)
def tie(text):
    t = set()
    if W1.search(text): t.add("W1")
    if re.search(r"0?\.246\d*|\bd\*|D_STAR", text, re.I): t.add("dstar")
    if AL.search(text): t.add("alpha")
    return t
stats = collections.defaultdict(lambda: collections.Counter()); swaps = []; per_file = collections.Counter(); per_scope = collections.Counter()
with gzip.open("data/census.csv.gz", "rt") as fh:
    for r in csv.DictReader(fh):
        if "symbol" not in r["families"]: continue
        syms = {canon(t) for t in r["tokens"].split(";")} - {None}
        if not syms: continue
        t = tie(r["text"])
        for s in syms:
            exp = RULE[s]; names = [x for x in r["tokens"].split(";") if canon(x) == s]
            stats[s]["lines"] += 1
            for v in t: stats[s]["tied_" + v] += 1
            if not t: stats[s]["tied_nothing"] += 1
            bad = (t and exp not in t and t & ({"W1", "dstar", "alpha"} - {exp})) or False
            if bad:
                stats[s]["contradicts_ruling"] += 1; swaps.append((r["path"], r["line"], s, names[0], "/".join(sorted(t)), r["text"][:200])); per_file[r["path"]] += 1
                sc = "scratchpad/primers" if re.search(r"scratchpad|hist_prime|hist_wiki|SpaceClaude|Desktop Archive|SpaceGemini|memory/", r["path"]) else "repository code/docs"
                per_scope[sc] += 1
json.dump({k: dict(v) for k, v in stats.items()}, open("data/symbol_ties.json", "w"), indent=1)
with open("data/traces_swap.csv", "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["path", "line", "symbol(by ruling)", "name_used", "value_on_line", "text"]); w.writerows(swaps)
print("symbol  lines  W1  d*  alpha  nothing  contradicts-ruling"); 
for s, c in stats.items(): print(f"{s:6s} {c['lines']:6d} {c['tied_W1']:5d} {c['tied_dstar']:5d} {c['tied_alpha']:5d} {c['tied_nothing']:6d} {c['contradicts_ruling']:6d}")
print("contradicting lines by scope:", dict(per_scope)); print("top files:"); [print(f"  {n:4d} {p}") for p, n in per_file.most_common(25)]
