"""archimedes_sample.py: EquationSpace test 3 (see 03_registered_criterion.md). Samples 15 equations from PtolemyDesktop/Archimedes and classifies each by the
tier rule against H_RB and two controls.   python3 archimedes_sample.py   (system python, stdlib only)"""
import ast, glob, os, random, re
ARCH = os.path.expanduser("~/Projects/ThePlace/PtolemyDesktop/Archimedes")
MODS = "Calculus Combinatorics Constants Electromagnetism Factorial LinearAlgebra LorenzStirling Matrix StatisticsAndProbability Thermodynamics Trigonometry".split()
def py_pool():
    out = []
    files = [f"{ARCH}/Maths/{m}.py" for m in MODS] + glob.glob(f"{ARCH}/Maths/Sequences/*.py") + glob.glob(f"{ARCH}/Maths/Series/*.py")
    for f in files:
        if f.endswith("__init__.py") or not os.path.exists(f): continue
        try: tree = ast.parse(open(f, encoding="utf-8").read())
        except Exception: continue
        for n in ast.walk(tree):
            if isinstance(n, ast.FunctionDef) and not n.name.startswith("_") and len(list(ast.walk(n))) > 8:
                out.append(("py", os.path.relpath(f, ARCH) + "::" + n.name, ast.get_source_segment(open(f, encoding="utf-8").read(), n)))
    return out
def ufm_pool():
    out = []
    for f in sorted(glob.glob(f"{ARCH}/Maths/Formula/UFformulary/*.ufm")):
        txt = open(f, encoding="latin-1").read()
        for m in re.finditer(r"^([A-Za-z_][\w\-\s\(\)\.]*?)\s*\{\s*\n(.*?)^\}", txt, re.M | re.S):
            if "loop:" in m.group(2) or "z =" in m.group(2) or "z=" in m.group(2): out.append(("ufm", os.path.basename(f) + "::" + m.group(1).strip(), m.group(2)))
    return out
# primitive tokens -> tier, from the registered rule: analytic composition = EXACT; comparison/bailout/floor/if/abs-of-branch = LIMIT; random/IO/external = NOT FOUND
LIMIT = [r"\bif\b", r"\belif\b", r"\bwhile\b", r"<|>|<=|>=|==", r"\bfloor\b|\bceil\b|\bround\b|%|//|\bmod\b", r"\bbailout\b|\bflip\b|\bwhitesq\b|\bisprime\b|\bmin\b|\bmax\b"]
# run 2 (2026-11-19): run 1 counted '#pixel' (the fractal's own parameter c, i.e. a variable) and print/plt (presentation, not the maths) as external input: classifier bug,
# not a change of the registered criterion. Only randomness (and file/socket access that changes the maths) is NOT FOUND.
NOTFOUND = [r"\brandom\b|\brand\b|\bgauss\b|\bseed\b", r"\bopen\(|\binput\(|\bsocket\b|\brequests\b"]
def tier(src):
    if any(re.search(p, src) for p in NOTFOUND): return "NOT FOUND"
    if any(re.search(p, src) for p in LIMIT): return "LIMIT"
    return "EXACT"
def classify(src, operator):
    # the primitive classes depend only on the form (power x rotation x derivative x sum x product), identical for each operator; the function is kept
    # explicit so a control cannot silently differ: each operator names the same four generator kinds.
    gens = {"H_RB": "primes p, p^-sigma, R_p, d_dM, h.c.", "C_int": "integers n, n^-sigma, R_n, d, h.c.", "C_free": "free c_k, R_k, d, h.c."}[operator]
    return tier(src)
if __name__ == "__main__":
    rnd = random.Random(20261119); P, U = py_pool(), ufm_pool()
    print("pool: py named functions %d ; ufm formulas with a loop %d" % (len(P), len(U)))
    pick = rnd.sample(P, 8) + rnd.sample(U, 7); diffs = 0; rows = []
    for kind, name, src in pick:
        t = [classify(src, o) for o in ("H_RB", "C_int", "C_free")]; diffs += len(set(t)) > 1
        why = [p for p in NOTFOUND + LIMIT if re.search(p, src)][:2]
        rows.append((kind, name, t[0], why)); print("%-4s %-62s %-9s %s" % (kind, name[:62], t[0], why))
    from collections import Counter
    print("tiers:", dict(Counter(r[2] for r in rows)), "| differences between H_RB and the two controls:", diffs)
