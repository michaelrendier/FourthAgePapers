#!/usr/bin/env python3
"""
make_paper.py: builds Twin_Prime_Wheels.md from ../twin_wheels.py.  Every number that comes from code is taken from a run when this script runs,
every listing is extracted verbatim from twin_wheels.py and executed cold (empty namespace) before it is printed, and the file's SHA-256 prefix is
printed in the paper.  `python3 make_paper.py --check` rebuilds in memory and reports whether the committed paper still matches (date line ignored).
"""
import ast, contextlib, hashlib, io, re, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "twin_wheels.py"
sys.path.insert(0, str(HERE.parent))
import twin_wheels as T                                  # noqa: E402

OUT = HERE / "Twin_Prime_Wheels.md"


def extract(names):
    src = SRC.read_text(); tree = ast.parse(src)
    return "\n\n\n".join(ast.get_source_segment(src, next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == n)) for n in names)


def cold(code, call):
    ns = {}; exec(code, ns); buf = io.StringIO()
    with contextlib.redirect_stdout(buf): exec(call, ns)
    return buf.getvalue().rstrip()


def listing(names, call, header="import numpy as np\n"):
    code = header + "\n\n" + extract(names); return "```python\n" + code + "\n\n" + call + "\n```\n\n```\n" + cold(code, call) + "\n```"


def main():
    t0 = time.time(); R = {N: T.report(N)[0] for N in (10 ** 6, 10 ** 7, 10 ** 8)}; r8 = R[10 ** 8]
    f = lambda x, n=4: f"{x:.{n}f}"
    rows = "\n".join(f"| 10^{len(str(N)) - 1} | {r['twin pairs']:,} | {f(r['observed / HL'])} | {f(r['mean L'], 1)} | {r['largest wheel']:,} | {r['wheels with L = 6 (centres one 6-step apart)']:,} | {f(r['mean interior primes per wheel'], 2)} | {r['max interior primes']} |" for N, r in R.items())
    quad = "\n".join(f"| 10^{len(str(N)) - 1} | {f(r['observed P(m=1)/geometric'], 3)} | {f(r['predicted P(m=1)/geometric = S(0,2,6,8)/(6·S(0,2)²)'], 3)} |" for N, r in R.items())
    brun = "\n".join(f"| 10^{len(str(N)) - 1} | {f(r['Brun partial sum'], 5)} | {f(r['B₂ − partial sum'], 5)} | {f(r['4C₂/ln N'], 5)} |" for N, r in R.items())
    mod30 = "\n".join(f"| 10^{len(str(N)) - 1} | " + " | ".join(f"{x:.3f}" for x in r["observed shares"]) + " |" for N, r in R.items())
    try:
        sys.path.insert(0, str(HERE.parents[1] / "RiemannHypothesisProof")); from rhp import wrap
        st = wrap.straddle_check(10 ** 6); cross = f"`rhp.wrap.straddle_check(10**6)` returns {st}: {st[1]} of {st[0]} pairs (p > 3) straddle the 0 spot of the circumference-6 circle; this program finds {R[10**6]['centres ≡ 0 mod 6 (excluding (3,5))']} centres ≡ 0 (mod 6)."
    except Exception as e:
        cross = f"(`RiemannHypothesisProof` not importable here: {type(e).__name__}; cross-check skipped)"
    L1 = listing(["sieve", "centres", "wheels"], "is_prime = sieve(200); c = centres(is_prime)\nprint('centres :', c.tolist())\nprint('wheels  :', wheels(c).tolist())")
    L2 = listing(["sieve", "centres", "interior_primes"], "is_prime = sieve(300); c = centres(is_prime)\nprint('interior primes per wheel:', interior_primes(is_prime, c).tolist())")
    L3 = listing(["sieve", "singular_series"], "print(round(float(singular_series((0, 2))), 6), round(float(singular_series((0, 2, 6, 8))), 6))")
    sha = hashlib.sha256(SRC.read_bytes()).hexdigest()[:12]
    s = (HERE / "template.md").read_text()
    for k, v in dict(DATE=time.strftime("%Y-%m-%d"), ROWS=rows, QUAD=quad, BRUN=brun, MOD30=mod30, CROSS=cross, L1=L1, L2=L2, L3=L3, SHA=sha, RUNTIME=f"{time.time() - t0:.0f}",
                     P1M=f"{R[10**8]['twin pairs']:,}", LW8=f"{r8['largest wheel']:,}", LWC8=f"{r8['largest wheel at centre']:,}", M1=f(r8["observed P(m=1), geometric P(m=1)"][0], 4),
                     G1=f(r8["observed P(m=1), geometric P(m=1)"][1], 4), DEV=f(r8["max |observed − geometric| over m"], 4), M5=f(r8["share of wheels with m = 5 and m = 7 (L = 30, 42) vs m = 4 and m = 6"][0], 4),
                     M4=f(r8["share of wheels with m = 5 and m = 7 (L = 30, 42) vs m = 4 and m = 6"][2], 4), NOINT=f"{r8['wheels with no interior prime']:,}", SMALL=f"{r8['wheels with L = 6 (centres one 6-step apart)']:,}",
                     MEANL8=f(r8["mean L"], 2), HLLOC8=f(r8["local Hardy–Littlewood spacing at N, (ln N)²/(2C₂)"], 2), HLMEAN8=f(r8["N / HL count (HL mean spacing over [0, N])"], 2)).items():
        s = s.replace(f"@@{k}@@", str(v))
    left = re.findall(r"@@\w+@@", s)
    assert not left, left
    if "--check" in sys.argv:
        old = OUT.read_text() if OUT.exists() else ""; strip = lambda x: re.sub(r"\*\*Date:\*\* \S+", "", x)
        print("paper matches a fresh build" if strip(old) == strip(s) else "paper DIFFERS from a fresh build"); return
    OUT.write_text(s); print("wrote", OUT, f"({time.time() - t0:.0f} s)")


if __name__ == "__main__":
    main()
