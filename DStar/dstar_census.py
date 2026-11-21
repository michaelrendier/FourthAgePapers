#!/usr/bin/env python3
"""dstar_census.py (2026-11-21): every occurrence of d* and its companions, everywhere the author's work lives.
Scans (text files < 6 MB): all of ~/Projects/ThePlace (except .git, venvs, caches, data and binary trees), ~/.clauderc*, ~/.claude/projects/*/memory, ~/Desktop/SpaceClaude, ~/Desktop/SpaceGemini and ~/Desktop/Desktop Archive.
Records, per matching line: where, which family, the token, the line's text. Families:
  value    0.246(0), 0.2463x, 0.2468x, 0.56644 (the superseded d*_ln10), 0.5671x (W(1)), 1/137(.036) (the fine-structure constant)
  dstar    the names d*, D*, D_STAR, d_star, dstar
  face     The Boundary / Stability / Flow / Translator, d*_RG, d*_taut, d*_ln10, d*_spec
  symbol   Omega_ZS, OMEGA_ZS, Ω_ζΣ, Omega_Riemann, Omega_RZ, Ω_RZ, A_pi, A_π, Α_π, Alpha_Fermat, A_fermat
Then classifies each symbol line by the value it is tied to on that line (W(1) = 0.567, d* = 0.246, alpha = 137) so the record's assignments can be counted, not remembered.
usage: python3 dstar_census.py   -> data/census.csv.gz, data/summary.json"""
import os, re, csv, gzip, json, sys, collections, subprocess
HOME = os.path.expanduser("~")
ROOTS = [f"{HOME}/Projects/ThePlace", f"{HOME}/Desktop/SpaceClaude", f"{HOME}/Desktop/SpaceGemini", f"{HOME}/Desktop/Desktop Archive"]
EXTRA = [f"{HOME}/.clauderc{s}" for s in ("", "_ValaQuenta", "_canonical_maths", "_citations", "_context", "_context_1", "_context_2", "_context_hub", "_ctx", "_licenses", "_memory", "_official_names", "_scratchpad_contents", "_user_provenance")] + [f"{HOME}/.claude/projects/-home-rendier-Projects-ThePlace/memory/{f}" for f in []]
SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__", "site-packages", "LeanScratch", "DataSets", "datasets", "_worktrees", "bins", "lambeq_env", "phone_pull_2026-06-06", "build", ".cache", "corpora", "corpus", "zips-11-21-26", "_build", "image_gallery", "holcus_paths_gallery", "michaelrendier.github.io"}
EXTS = (".md", ".txt", ".py", ".c", ".h", ".json", ".ipynb", ".html", ".rst", ".tex", ".sh", ".csv", ".yaml", ".yml", ".js", ".bash")
FAMS = [("value", re.compile(r"(?<![\d.])0?\.246[0-9]*|(?<![\d.])0?\.5664[0-9]*|(?<![\d.])0?\.5671[0-9]*|1/137(?:\.0[0-9]*)?|137\.03[0-9]*|(?<![\d.])0?\.2468[0-9]*")),
        ("face", re.compile(r"The (?:Boundary|Stability|Flow|Translator)\b|d\*_?(?:RG|taut|ln\(?10\)?|spec|ℝ)|d_star_(?:spec|taut|rg|ln10)|D_STAR_(?:SPEC|BOUNDARY|TAUT|RG|LN10)")),
        ("dstar", re.compile(r"\bd\*|\bD\*|D_STAR\b|\bd_star\b|\bdstar\b|\bD_star\b")),
        ("symbol", re.compile(r"Omega_ZS|OMEGA_ZS|Omega_zS|Ω_ζΣ|Ω_ZS|Ω_ζ|Omega_Riemann|OMEGA_RIEMANN|Omega_RZ|OMEGA_RZ|Ω_RZ|A_pi\b|A_PI\b|A_π|Α_π|Alpha_Fermat|ALPHA_FERMAT|A_fermat|A_FERMAT|Alpha_pi"))]
SYM_ROLE = [("W(1)/Lambert", re.compile(r"Lambert|W\(1\)|0?\.5671|fixed point of", re.I)), ("d* (0.246)", re.compile(r"0?\.246|d\*|D_STAR|log10|digit", re.I)), ("alpha_fs (1/137)", re.compile(r"137|fine.structure|α_fs|alpha_fs|Wyler", re.I)), ("Hagedorn/entropy/Riemann", re.compile(r"Hagedorn|entropy|Riemann|thermal", re.I)), ("speed of causality/inertia/Fermat", re.compile(r"causality|inertia|Fermat|speed of (light|causality)", re.I))]
def files():
    for root in ROOTS:
        pass
    for root in ROOTS:
        for d, dirs, fs in os.walk(root):
            dirs[:] = [x for x in dirs if x not in SKIP and not (x == 'data' and d.endswith('/DStar'))]
            for f in fs:
                p = os.path.join(d, f)
                if not f.lower().endswith(EXTS) or os.path.islink(p): continue
                try:
                    if os.path.getsize(p) > 6_000_000: continue
                except OSError: continue
                yield p
    for p in EXTRA:
        if os.path.isfile(p): yield p
    mem = f"{HOME}/.claude/projects/-home-rendier-Projects-ThePlace/memory"
    if os.path.isdir(mem):
        for f in os.listdir(mem): yield os.path.join(mem, f)
import hashlib
rows = []; seen = set(); seen_content = {}; nfiles = 0; dup_files = 0
for p in files():
    rp = os.path.realpath(p)
    if rp in seen: continue
    seen.add(rp)
    try: raw = open(p, errors="ignore").read()
    except OSError: continue
    hsh = hashlib.md5(raw.encode("utf-8", "ignore")).hexdigest()
    if hsh in seen_content: dup_files += 1; continue
    seen_content[hsh] = p; nfiles += 1; lines = raw.split("\n")
    for i, ln in enumerate(lines, 1):
        if len(ln) > 4000: ln = ln[:4000]
        hit = {}
        for fam, rx in FAMS:
            m = rx.findall(ln)
            if m: hit[fam] = sorted(set(m))
        if not hit or ("value" in hit and len(hit) == 1 and not re.search(r"d\*|D_STAR|Omega|Ω|Lambert|gap|GAP|Boundary|ln ?10|log", ln)): continue
        role = ""
        if "symbol" in hit:
            role = "|".join(n for n, rx in SYM_ROLE if rx.search(ln))
        rows.append((p.replace(HOME, "~"), i, ";".join(hit), ";".join(sum(hit.values(), []))[:120], role, ln.strip()[:240]))
os.makedirs("data", exist_ok=True)
with gzip.open("data/census.csv.gz", "wt", newline="") as fh:
    w = csv.writer(fh); w.writerow(["path", "line", "families", "tokens", "symbol_role", "text"]); w.writerows(rows)
fam = collections.Counter(); top = collections.Counter(); val = collections.Counter(); sym = collections.defaultdict(collections.Counter); repo = collections.Counter()
for path, ln, fams, toks, role, text in rows:
    for f in fams.split(";"): fam[f] += 1
    top[path] += 1; repo[path.split("/")[3] if path.startswith("~/Projects/ThePlace/") else path.split("/")[1]] += 1
    for t in toks.split(";"):
        if re.match(r"0?\.246", t): val["0.246(0) running" if re.fullmatch(r"0?\.2460*", t) else "0.2463x boundary" if t.startswith(("0.2463", ".2463")) else "0.246x other"] += 1
        elif t.startswith(("0.2468", ".2468")): val["0.2468x superseded RG estimate"] += 1
        elif t.startswith(("0.5664", ".5664")): val["0.5664x superseded d*_ln10"] += 1
        elif re.match(r"0?\.5671", t): val["0.5671x W(1)"] += 1
        elif "137" in t: val["137 (fine structure)"] += 1
    if "symbol" in fams:
        for t in toks.split(";"):
            if re.match(r"(Omega|OMEGA|Ω|A_|Α_|Alpha|ALPHA)", t): sym[t][role or "(no role word on the line)"] += 1
summary = dict(files_scanned=nfiles, duplicate_files_skipped=dup_files, matching_lines=len(rows), by_family=dict(fam), by_value=dict(val.most_common()), by_root=dict(repo.most_common(25)), top_files=top.most_common(30),
               symbol_roles={k: dict(v.most_common(6)) for k, v in sorted(sym.items(), key=lambda kv: -sum(kv[1].values()))[:14]})
json.dump(summary, open("data/summary.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: summary[k] for k in ("files_scanned", "matching_lines", "by_family", "by_value")}, indent=1, ensure_ascii=False))
