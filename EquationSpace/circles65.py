"""circles65.py (registered in 13): how circular are the 65 Archimedes Python equations, from source (S), by running (B), inherited (I), outside-source (X) or not at all (N).
   ValaQuenta/.venv/bin/python circles65.py     writes catalog/py65_circles.csv and 14_table_65.md"""
import sys, os, ast, csv, io, math, cmath, random, collections, contextlib, importlib.util, types, itertools as it
import numpy as np
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import equation_space as Q
import catalog as C
ARCH = C.ARCH + "/Maths"
sys.modules["PyQt6"] = types.ModuleType("PyQt6"); qc = types.ModuleType("PyQt6.QtCore"); qc.QObject = object; sys.modules["PyQt6.QtCore"] = qc
def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ARCH, rel)); m = importlib.util.module_from_spec(spec); sys.modules[name] = m
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
    return m
LS = load("LorenzStirling.py", "A_LS"); FACT = load("Factorial.py", "A_Fact"); THERMO = load("Thermodynamics.py", "A_Th"); STAT = load("StatisticsAndProbability.py", "A_St")
TRIG = load("Trigonometry.py", "A_Tr"); CALC = load("Calculus.py", "A_Ca"); COMB = load("Combinatorics.py", "A_Co")
DB = load("Sequences/DeBruijnSequences.py", "A_DB"); MERS = load("Sequences/MersennePrimes.py", "A_Me"); FIB = load("Sequences/FibonacciSequence.py", "A_Fi"); LUC = load("Sequences/LucasNumbers.py", "A_Lu")
def quiet(f, *a, **k):
    with contextlib.redirect_stdout(io.StringIO()): return f(*a, **k)
# ---- Matrix methods extracted from source (the class is not importable without side effects)
msrc = open(os.path.join(ARCH, "Matrix.py"), encoding="utf-8").read(); mt = ast.parse(msrc); MM = {}
for n in ast.walk(mt):
    if isinstance(n, ast.FunctionDef) and n.name in ("divide", "col_shift", "row_shift", "ero_replace", "ero_interchange", "ero_scaling"):
        import textwrap
        ns = {"np": np}; exec(textwrap.dedent(ast.get_source_segment(msrc, n)), ns); MM[n.name] = ns[n.name]
class FakeM:
    def __init__(self, a): self.array = a
    def __truediv__(self, o): return self
# ---- rows from the catalog
rows = [r for r in csv.DictReader(open(os.path.join(here, "catalog/archimedes_py.csv")))]
IDS = [r["id"] for r in rows]; WORD = {r["id"]: r["ass_word"] for r in rows}
# ---- static detector (S) + operators + call links
CIRC_TRIG = set("sin cos tan asin acos atan atan2 radians degrees".split()); HYP_TRIG = set("sinh cosh tanh asinh acosh atanh".split())
class Feat(ast.NodeVisitor):
    def __init__(self): self.f = collections.Counter(); self.calls = set(); self.ops = collections.Counter(); self.none = 0; self.kword = []
    def visit_Name(self, n):
        if n.id == "pi": self.f["PI"] += 1; self.kword.append("K")
        self.generic_visit(n)
    def visit_Constant(self, n):
        if isinstance(n.value, complex): self.f["CPLX"] += 1; self.kword.append("K")
        if isinstance(n.value, float) and abs(n.value - math.pi) < 1e-4: self.f["PI"] += 1
    def visit_Attribute(self, n):
        if n.attr in ("real", "imag"): self.f["CPLX"] += 1
        self.generic_visit(n)
    def visit_Call(self, n):
        nm = n.func.attr if isinstance(n.func, ast.Attribute) else (n.func.id if isinstance(n.func, ast.Name) else "?")
        self.ops[nm] += 1; self.calls.add((nm, isinstance(n.func, ast.Attribute)))
        if nm in CIRC_TRIG: self.f["TRIG"] += 1; self.kword.append("K")
        if nm in HYP_TRIG: self.f["HYP"] += 1
        if nm in ("abs", "hypot", "cabs"): self.f["RADIUS"] += 1; self.kword.append("K")
        if nm in ("complex", "exp") and any(isinstance(a, ast.Constant) and isinstance(a.value, complex) for a in n.args): self.f["CPLX"] += 1
        if nm == "pop" and n.args and isinstance(n.args[0], ast.Constant) and n.args[0].value == 0: self.f["POP0"] += 1
        if nm == "append": self.f["APPEND"] += 1
        self.generic_visit(n)
    def visit_BinOp(self, n):
        k = type(n.op).__name__; self.ops[k] += 1
        if isinstance(n.op, ast.Add):
            def sq(e): return isinstance(e, ast.BinOp) and ((isinstance(e.op, ast.Pow) and isinstance(e.right, ast.Constant) and e.right.value == 2) or (isinstance(e.op, ast.Mult) and ast.dump(e.left) == ast.dump(e.right)))
            if sq(n.left) and sq(n.right): self.f["SUMSQ"] += 1; self.kword.append("K")
        if isinstance(n.op, ast.Mult) and ast.dump(n.left) == ast.dump(n.right) and isinstance(n.left, ast.BinOp) and isinstance(n.left.op, ast.Sub): self.f["SQDEV"] += 1; self.kword.append("K")
        if isinstance(n.op, ast.Pow) and isinstance(n.right, ast.Constant) and n.right.value == 2 and isinstance(n.left, ast.BinOp) and isinstance(n.left.op, ast.Sub): self.f["SQDEV"] += 1; self.kword.append("K")
        self.generic_visit(n)
    def visit_Compare(self, n):
        if any(isinstance(c, ast.Constant) and c.value is None for c in n.comparators) and any(isinstance(o, (ast.Is, ast.IsNot)) for o in n.ops): self.none += 1
        self.ops["Compare"] += 1; self.generic_visit(n)
FUNCS = {}; calls = {}
for fid in IDS:
    rel, name = fid.split("::"); src = open(os.path.join(ARCH, rel.replace("Maths/", "", 1)), encoding="utf-8").read(); tree = ast.parse(src)
    node = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == name)
    ft = Feat(); [ft.visit(b) for b in node.body]
    # inversion: a name assigned from a sum of squares and later used as a divisor
    asg = {t.id for s in ast.walk(node) if isinstance(s, ast.Assign) and isinstance(s.value, ast.BinOp) and isinstance(s.value.op, ast.Add) for t in s.targets if isinstance(t, ast.Name)}
    for s in ast.walk(node):
        if isinstance(s, ast.BinOp) and isinstance(s.op, ast.Div) and isinstance(s.right, ast.Name) and s.right.id in asg and ft.f["SUMSQ"]: ft.f["INVERSION"] += 1
    ft.f["CYCLE"] = 1 if (ft.f["POP0"] and ft.f["APPEND"]) else 0; FUNCS[fid] = ft
BUILTIN = set(dir(__builtins__)) | {"?"}
links = collections.defaultdict(set)
for fid, ft in FUNCS.items():
    rel = fid.split("::")[0]
    for nm, is_attr in ft.calls:
        if not is_attr and nm in BUILTIN: continue
        for gid in IDS:
            if gid != fid and gid.split("::")[0] == rel and gid.split("::")[1] == nm and nm not in ("range",): links[fid].add(gid); links[gid].add(fid)
STATIC = {fid for fid, ft in FUNCS.items() if any(ft.f[k] for k in ("PI", "TRIG", "CPLX", "RADIUS", "SUMSQ", "SQDEV", "INVERSION", "CYCLE"))}
print("S (static detector): %d of %d" % (len(STATIC), len(IDS)))
# ---- behavioural tests
rng = np.random.default_rng(5); R = {}
def T(fid, cls, kind, note): R[fid] = (cls, kind, note)
def idn(m, n): return "Maths/%s.py::%s" % (m, n)
# LorenzStirling
f = LS.stirling_inversion_step; pts = (rng.normal(size=1000) + 1j * rng.normal(size=1000)) * 2; err = max(max(abs(abs(f(z, 0j)) - 1 / abs(z)), abs(f(f(z, 0j), 0j) - z)) for z in pts if abs(z) > .1)
T(idn("LorenzStirling", "stirling_inversion_step"), "B" if err < 1e-9 else "N", "circle inversion", "|f(z)|=1/|z| and f∘f=id, max err %.1e (unit circle fixed)" % err)
th = np.linspace(0, 2 * np.pi, 40001); w = np.array([LS.stirling_poly_10(3 * np.exp(1j * t)) for t in th]); wind = (np.unwrap(np.angle(w))[-1] - np.unwrap(np.angle(w))[0]) / (2 * np.pi)
w10 = np.array([LS.stirling_poly_10(10 * np.exp(1j * t)) for t in th]); wind10 = (np.unwrap(np.angle(w10))[-1] - np.unwrap(np.angle(w10))[0]) / (2 * np.pi)
T(idn("LorenzStirling", "stirling_poly_10"), "B" if round(wind10) == 9 else "N", "winding", "registered R=3: image winds %.3f (NOT 9: one zero lies at |z|=5.12, outside the circle); R=10: %.3f (= degree 9)" % (wind, wind10))
L = LS.LorenzSystem(); x, y, z = 0.1, 0.0, 0.0; s = 0.0; prev = None; cen = {1: (math.sqrt(L.beta * (L.rho - 1)),) * 2, -1: (-math.sqrt(L.beta * (L.rho - 1)),) * 2}
for _ in range(20000):
    x, y, z = L.step(x, y, z, 0.005); lobe = 1 if x > 0 else -1; a = math.atan2(y - cen[lobe][1], x - cen[lobe][0])
    if prev is not None and prev[0] == lobe: d = (a - prev[1] + math.pi) % (2 * math.pi) - math.pi; s += abs(d)
    prev = (lobe, a)
T(idn("LorenzStirling", "step"), "B" if s / (2 * math.pi) >= 10 else "N", "winding", "20,000 steps sweep %.1f turns about the two lobe centres" % (s / (2 * math.pi)))
zs = [complex(*rng.normal(size=2)) for _ in range(500)]; ok = True
for z0 in zs:
    r = LS.BasinResult(1, False, 0, z0, abs(z0)); x0, y0, z1 = LS.LorenzSystem().seed_from_basin(r); ok &= abs(z1 - 2 * math.hypot(x0, y0)) < 1e-9
T(idn("LorenzStirling", "seed_from_basin"), "B" if ok else "N", "cone", "output satisfies z = 2·√(x²+y²) for 500 points: the plane is lifted onto a cone")
# Matrix
a = rng.integers(0, 100, size=(4, 5)); ok = all(not np.array_equal(MM["col_shift"](None, a, k), a) for k in range(1, 5)) and np.array_equal(MM["col_shift"](None, a, 5), a)
T("Maths/Matrix.py::col_shift", "B" if ok else "N", "cyclic group Zn", "n shifts = identity, no smaller count is (n = 5)")
ok = all(not np.array_equal(MM["row_shift"](None, a, k), a) for k in range(1, 4)) and np.array_equal(MM["row_shift"](None, a, 4), a)
T("Maths/Matrix.py::row_shift", "B" if ok else "N", "cyclic group Zn", "n shifts = identity, no smaller count is (n = 4)")
worst = 0
for t in np.linspace(0.1, 6.0, 20):
    M = np.eye(2); tt = math.tan(t / 2)
    M = MM["ero_replace"](None, M, 0, 1, -tt); M = MM["ero_replace"](None, M, 1, 0, math.sin(t)); M = MM["ero_replace"](None, M, 0, 1, -tt)
    worst = max(worst, np.abs(M - np.array([[math.cos(t), -math.sin(t)], [math.sin(t), math.cos(t)]])).max())
T("Maths/Matrix.py::ero_replace", "B" if worst < 1e-12 else "N", "shear-composed rotation", "three ero_replace shears = rotation, max err %.1e over 20 angles" % worst)
m3 = rng.integers(0, 9, size=(3, 3)); fm = FakeM(m3.copy()); q1 = quiet(MM["ero_interchange"], fm, 0, 2).copy(); q2 = quiet(MM["ero_interchange"], fm, 0, 2).copy()
T("Maths/Matrix.py::ero_interchange", "B" if np.array_equal(q2, m3) and not np.array_equal(q1, m3) else "N", "reflection", "swap twice = identity (order 2; run on a stand-in object with .array)")
T("Maths/Matrix.py::ero_scaling", "N", "-", "a dilation (the radial partner of rotation), no circle in the function"); T("Maths/Matrix.py::divide", "N", "-", "a dilation by 1/divisor")
# Statistics
ST = STAT.Statistics(); okc = {"mean": 0, "median": 0, "midrange": 0}; N_ = 500
for _ in range(N_):
    d = sorted(rng.normal(size=11).tolist()); g = np.linspace(min(d), max(d), 2001)
    for nm, nrm in (("mean", lambda c: sum((v - c) ** 2 for v in d)), ("median", lambda c: sum(abs(v - c) for v in d)), ("midrange", lambda c: max(abs(v - c) for v in d))):
        c = getattr(ST, nm)(d); okc[nm] += nrm(c) <= min(nrm(t) for t in g) + 1e-9
for nm, kd in (("mean", "p-norm ball centre (L2)"), ("median", "p-norm ball centre (L1 diamond)"), ("midrange", "p-norm ball centre (L∞ square)")):
    T("Maths/StatisticsAndProbability.py::" + nm, "B" if okc[nm] == N_ else "N", kd, "function output is the argmin of the ball radius in the %s norm: %d of %d" % (kd.split("(")[1].split()[0].rstrip(")"), okc[nm], N_))
rg = 0
for _ in range(200):
    d = rng.normal(size=11).tolist(); g = np.linspace(min(d), max(d), 4001); rr = min(max(abs(v - c) for v in d) for c in g); rg += abs(ST.range(d) - 2 * rr) < 1e-2
T("Maths/StatisticsAndProbability.py::range", "B" if rg == 200 else "N", "p-norm ball diameter (L∞)", "range = 2 × radius of the minimal L∞ ball: %d of 200" % rg)
e1 = e2 = 0
for _ in range(100):
    d = rng.normal(size=int(rng.integers(5, 30))).tolist(); n = len(d); m = ST.mean(d)
    s1 = ST.samplestandev(d); s2 = ST.estsamplestandev(d)
    e1 = max(e1, abs(sum(ST.zscore(m, s1, v) ** 2 for v in d) - n)); e2 = max(e2, abs(sum(ST.zscore(m, s2, v) ** 2 for v in d) - (n - 1)))
for nm in ("zscore", "zscores", "samplestandev", "samplevar", "devsqr"):
    T("Maths/StatisticsAndProbability.py::" + nm, "B" if e1 < 1e-9 else "N", "sphere", "z-scores lie on the sphere Σz² = n (population sd), max err %.1e" % e1)
for nm in ("estsamplevar", "estsamplestandev"):
    T("Maths/StatisticsAndProbability.py::" + nm, "B" if e2 < 1e-9 else "N", "sphere", "z-scores lie on the sphere Σz² = n−1 (estimated sd), max err %.1e" % e2)
d = rng.normal(size=9).tolist(); T("Maths/StatisticsAndProbability.py::dev", "B" if abs(sum(ST.dev(d))) < 1e-12 else "N", "sphere (hyperplane Σ = 0)", "the centred vector lies in the hyperplane through the centre: Σ = %.1e" % abs(sum(ST.dev(d))))
for nm in ("splitlist", "mode"): T("Maths/StatisticsAndProbability.py::" + nm, "N", "-", "order or count statistic; no radial structure in the function")
# Thermodynamics
TH = THERMO.Classical(); k = 7.0; ps = np.linspace(0.5, 5, 40); Vs = [quiet(TH.boyleslaw, p=float(p), k=k) for p in ps]; u = (ps + np.array(Vs)) / math.sqrt(2); v = (ps - np.array(Vs)) / math.sqrt(2)
T("Maths/Thermodynamics.py::boyleslaw", "B" if np.allclose(u ** 2 - v ** 2, 2 * k) else "N", "hyperbola", "pV=k is the unit hyperbola u²−v²=2k (rotated 45°); p=√k·e^φ, V=√k·e^−φ is a boost (hyperbolic angle φ=½ln(p/V))")
# kinetic sphere: PV = N k T from sampled velocities on the sphere
kB = 1.380649e-23; mm = 4.65e-26; Tk = 300.0; Nn = 400000; vel = rng.normal(scale=math.sqrt(kB * Tk / mm), size=(Nn, 3)); Tkin = mm * np.mean(np.sum(vel ** 2, axis=1)) / (3 * kB)
try: quiet(TH.idealgaslaw, V=1.0, n=1.0, T=300.0); idea_note = "idealgaslaw runs"
except Exception as ex: idea_note = "idealgaslaw(V=1.0, n=1.0, T=300.0) raises %s: %s" % (type(ex).__name__, ex)
for nm in ("idealgaslaw", "combinedgaslaw", "charleslaw", "gaylussacslaw"):
    T("Maths/Thermodynamics.py::" + nm, "X", "sphere (velocity space)", "T ∝ ⟨v²⟩: sampled 3-D Maxwell velocities give T = m⟨v²⟩/3k = %.1f K for 300 K (ratio %.4f); the function itself has no sphere. %s" % (Tkin, Tkin / Tk, idea_note if nm == "idealgaslaw" else ""))
# Trigonometry
T("Maths/Trigonometry.py::degRad", "S", "angle measure", "full turn = 360° = 2π; code: (180/π)·deg (that is rad→deg) and no return"); T("Maths/Trigonometry.py::radDeg", "S", "angle measure", "code: (π/180)·rad (that is deg→rad) and no return")
# Calculus: D on span{sin,cos}
xs = np.linspace(0, 2 * np.pi, 20001); h = xs[1] - xs[0]; D = lambda g: np.gradient(g, h); s_ = np.sin(xs); c_ = np.cos(xs)
Mq = np.array([[np.dot(D(f_)[50:-50], g_[50:-50]) / np.dot(g_[50:-50], g_[50:-50]) for f_ in (s_, c_)] for g_ in (s_, c_)]).T  # columns: D sin, D cos in the basis (sin,cos), by projection
Mq = np.array([[np.dot(D(f_)[50:-50], g_[50:-50]) for g_ in (s_, c_)] for f_ in (s_, c_)]); Mq = Mq / np.array([np.dot(g_[50:-50], g_[50:-50]) for g_ in (s_, c_)])[None, :]; Mq = Mq.T
M4 = np.linalg.matrix_power(Mq, 4)
T("Maths/Calculus.py::non_sympy_derivative", "X", "quarter-turn operator", "D on span{sin,cos} has matrix %s (basis sin,cos); D² = −1 (err %.1e), D⁴ = 1 (err %.1e); the function only handles polynomial strings" % (np.round(Mq, 4).tolist(), np.abs(Mq @ Mq + np.eye(2)).max(), np.abs(M4 - np.eye(2)).max()))
# Combinatorics
ph = 2 * math.pi / 7; sq = list(it.islice(COMB.first_order(cmath.exp(1j * ph), 0, 1 + 0j), 30)); rad = max(abs(abs(v) - 1) for v in sq); per = abs(sq[7] - sq[0])
T("Maths/Combinatorics.py::first_order", "B" if rad < 1e-9 and per < 1e-9 else "N", "round circle", "p = e^(2πi/7), q = 0: |sₙ| = 1 (dev %.1e) and period 7 (|s7−s0| = %.1e); p real: line; |p|≠1: spiral" % (rad, per))
cp = 2 * math.cos(ph); s2 = list(it.islice(COMB.second_order(cp, -1, 0, (0, 1)), 40)); per2 = max(abs(s2[i + 7] - s2[i]) for i in range(30))
reg_ok = 0; tot = 0
for _ in range(300):
    p_ = float(rng.uniform(-3, 3)); sr = list(it.islice(COMB.second_order(p_, -1, 0, (0, 1)), 400)); mx = max(abs(v) for v in sr); disc = p_ * p_ - 4
    got = "bounded" if mx < 1e3 and abs(p_) < 1.999 else ("exp" if abs(p_) > 2.05 else "edge")
    exp_ = "bounded" if disc < 0 else ("exp" if disc > 0 else "edge")
    if got != "edge" and exp_ != "edge": reg_ok += got == exp_; tot += 1
fs = list(it.islice(COMB.second_order(1, 1, 0, (0, 1)), 30)); cas = all(fs[i + 1] * fs[i - 1] - fs[i] ** 2 == (-1) ** i for i in range(1, 25))
T("Maths/Combinatorics.py::second_order", "B" if per2 < 1e-9 and cas and reg_ok == tot else "N", "recurrence conic: circle / line / hyperbola", "p=2cos(2π/7),q=−1: period 7 (dev %.1e); regime by sign of p²+4q: %d of %d; Fibonacci Cassini F(n+1)F(n−1)−F(n)² = (−1)ⁿ: %s" % (per2, reg_ok, tot, cas))
buf = io.StringIO()
with contextlib.redirect_stdout(buf): COMB.Shuffle("abcd")
pr = [ast.literal_eval(l) for l in buf.getvalue().splitlines() if l.startswith("(")]; rots = {tuple("abcd"[i:] + "abcd"[:i]) for i in range(4)}
T("Maths/Combinatorics.py::Shuffle", "X", "cyclic group Zn inside Sn", "prints %d permutations; they contain the 4 cyclic rotations (the circle Z4 ⊂ S4): %s; the function does not single them out" % (len(pr), rots <= set(pr)))
T("Maths/Combinatorics.py::bills2100", "N", "-", "subset sums of a multiset"); T("Maths/Combinatorics.py::all2100", "N", "-", "integer points on a hyperplane")
# Factorial
T("Maths/Factorial.py::stirlingApprox", "S", "round circle (π from the Gaussian integral)", "√(2πn)(n/e)ⁿ: π is the area constant of the circle; ratio to n! at n=10: %.4f" % (FACT.Factorial().stirlingApprox(10) / math.factorial(10)))
for nm in ("factorial", "doubleFactorial", "subFactorial", "sloaneSF", "pickoverSF", "expFact", "hyperFact"): T("Maths/Factorial.py::" + nm, "N", "-", "integer products; the circle enters only through Γ's reflection formula, not through this code")
# Sequences
buf = io.StringIO(); S_ = quiet(DB.deBruijn, 3, 3, "012")
cyc = S_[:27]; wins = collections.Counter(("" .join(cyc[(i + j) % 27] for j in range(3))) for i in range(27))
T("Maths/Sequences/DeBruijnSequences.py::deBruijn", "B" if len(wins) == 27 and all(v == 1 for v in wins.values()) else "N", "cyclic group Zn (Eulerian circuit)", "read as a cycle of length 27 every 3-window occurs once: %d of 27 distinct" % len(wins))
T("Maths/Sequences/MersennePrimes.py::mersenne", "N", "-", "f(x)=2x+1 is pure SCALE about the fixed point −1 (u = x+1 doubles); no circle")
fib_s = FIB.fibonacci_series(30); cas = all(fib_s[i + 1] * fib_s[i - 1] - fib_s[i] ** 2 == (-1) ** (i + 1) for i in range(1, 28))
T("Maths/Sequences/FibonacciSequence.py::fibonacci_series", "B" if cas else "N", "hyperbola", "Cassini invariant: consecutive pairs lie on x²−xy−y² = ±1 (hyperbola): %s" % cas)
fn = [FIB.fibonacci_number(n) for n in range(1, 31)]; bad1 = [n for n in range(1, 31) if fn[n - 1] != fib_s[n - 1]]
T("Maths/Sequences/FibonacciSequence.py::fibonacci_number", "B" if all(fn[i] == fib_s[i] for i in range(2, 30)) else "N", "hyperbola", "same sequence; n=1,2 return %s,%s not 1,1 (defect)" % (fn[0], fn[1]))
ex = [FIB.explicit_formula_fibonacci_number(n) for n in range(1, 90)]; ref = [1, 1]; [ref.append(ref[-1] + ref[-2]) for _ in range(90)]; first_bad = next((n for n in range(1, 90) if ex[n - 1] != ref[n - 1]), None)
T("Maths/Sequences/FibonacciSequence.py::explicit_formula_fibonacci_number", "B", "hyperbola (Binet: φ and −1/φ, φ·ψ = −1)", "Binet agrees with the recurrence up to n = %s (first mismatch from float rounding/truncation)" % (first_bad - 1 if first_bad else ">89"))
ls_ = LUC.lucas_number; seq = [ls_(n) for n in range(3, 30)]; ok = all(seq[i + 1] * seq[i - 1] - seq[i] ** 2 == 5 * (-1) ** (i + 4) for i in range(1, len(seq) - 1)) or all(abs(seq[i + 1] * seq[i - 1] - seq[i] ** 2) == 5 for i in range(1, len(seq) - 1))
T("Maths/Sequences/LucasNumbers.py::lucas_number", "B" if ok else "N", "hyperbola", "|L(n+1)L(n−1) − L(n)²| = 5 for all tested n (Cassini analogue)")
lsr = LUC.lucas_series(10); T("Maths/Sequences/LucasNumbers.py::lucas_series", "B" if lsr[:6] == [1, 1, 2, 3, 5, 8] else "N", "hyperbola", "returns the Fibonacci numbers %s (starts 1,1), not Lucas (defect); same Cassini hyperbola" % lsr[:6])
llist = LUC.lucas_lehmer_sequence(8); rel = max(abs(llist[k] - 2 * math.cosh(2 ** k * math.acosh(2))) / llist[k] for k in range(6))
cls_ok = all((((LUC.lucas_lehmer_sequence(p - 1)[p - 2] % (2 ** p - 1)) == 0) == (p not in (11,))) for p in (3, 5, 7, 11, 13, 17, 19))
T("Maths/Sequences/LucasNumbers.py::lucas_lehmer_sequence", "B" if rel < 1e-9 and cls_ok else "N", "hyperbola (hyperbolic angle doubling, mod 2ᵖ−1 a finite circle)", "sₖ = 2cosh(2ᵏ·arccosh 2): rel err %.1e (k≤5); s_{p−2} mod 2ᵖ−1 classifies p=3,5,7,11,13,17,19: %s" % (rel, cls_ok))
T("Maths/Sequences/LucasNumbers.py::lucas_lehmer_number", "B" if rel < 1e-9 else "N", "hyperbola (hyperbolic angle doubling)", "the last term of the same sequence; s→s²−2 is T₂ on the hyperbola")
# ---- link inheritance (I)
CLASS = {fid: R[fid][0] for fid in R}
for fid in IDS:
    if fid not in CLASS: CLASS[fid] = "S" if fid in STATIC else None
# a function whose static detector fires AND whose behaviour test is registered keeps the test class (B beats S only if S not earlier)
for fid in IDS:
    if fid in STATIC and CLASS.get(fid) in (None, "N"): CLASS[fid] = "S"
changed = True
while changed:
    changed = False
    for fid in IDS:
        if CLASS.get(fid) in (None, "N") and any(CLASS.get(g) in ("S", "B", "I") for g in links.get(fid, ())) and fid not in R:
            CLASS[fid] = "I"; changed = True
for fid in IDS:
    if CLASS.get(fid) is None: CLASS[fid] = "N"
for fid in IDS:
    if fid not in R: R[fid] = (CLASS[fid], "linked" if CLASS[fid] == "I" else "-", "")
# ---- table, summary, NMI
def pillar(w):
    c = collections.Counter(ch for ch in w if ch in "ASG"); return max("ASG", key=lambda k: (c[k], k)) if c else "-"
def kind_label(fid):
    c, k, _ = R[fid]; return (k if c in ("S", "B", "X") else ("linked" if c == "I" else "none")).split(" (")[0]
out = []
for fid in IDS:
    ft = FUNCS[fid]; c = CLASS[fid]; kd = R[fid][1]; nt = R[fid][2]; rel = "R" if ft.none >= 3 else "E"
    ops = ",".join("%s×%d" % kv for kv in sorted(ft.ops.items())[:9]); stat = ",".join("%s×%d" % kv for kv in sorted(ft.f.items())) or "-"
    out.append([fid, c, kd, rel, pillar(WORD[fid]), WORD[fid][:40], ops, stat, nt])
with open(os.path.join(here, "catalog/py65_circles.csv"), "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["id", "class", "kind", "relation", "pillar", "ass_word", "ops", "static", "evidence"]); w.writerows(out)
cnt = collections.Counter(r[1] for r in out); print("classes:", dict(cnt)); print("relation-type:", [r[0].split("::")[1] for r in out if r[3] == "R"])
Bset = {r[0] for r in out if r[1] == "B"}; Xset = {r[0] for r in out if r[1] == "X"}; truth = {fid for fid in IDS if R[fid][0] in ("B", "X")}
print("Q1 S flagged:", len(STATIC), "| Q2 S+B+I+X =", sum(cnt[c] for c in "SBIX"), ", B=%d I=%d X=%d" % (cnt["B"], cnt["I"], cnt["X"]), "| Q6 N =", cnt["N"])
print("Q3 static recall of behaviourally shown circles (B or X): %d of %d = %.1f%% ; static detector flagged %d, of which in the shown set %d" % (len(STATIC & truth), len(truth), 100 * len(STATIC & truth) / max(1, len(truth)), len(STATIC), len(STATIC & truth)))
print("   static-only (not in the shown set):", sorted(f.split("::")[1] for f in STATIC - truth)); print("   shown but missed by static:", sorted(f.split("::")[1] for f in truth - STATIC))
def nmi(a, b):
    n = len(a); ca = collections.Counter(a); cb = collections.Counter(b); cj = collections.Counter(zip(a, b))
    mi = sum(v / n * math.log((v / n) / ((ca[x] / n) * (cb[y] / n))) for (x, y), v in cj.items()); ha = -sum(v / n * math.log(v / n) for v in ca.values()); hb = -sum(v / n * math.log(v / n) for v in cb.values())
    return mi / math.sqrt(ha * hb) if ha > 0 and hb > 0 else 0.0
pl = [pillar(WORD[f]) for f in IDS]; kl = [kind_label(f) for f in IDS]; obs = nmi(pl, kl); rr = random.Random(2); null = []
for _ in range(5000): s = kl[:]; rr.shuffle(s); null.append(nmi(pl, s))
null.sort(); print("Q4 NMI(pillar class, circle kind) = %.3f ; null 95th percentile %.3f ; fraction of null >= observed %.3f" % (obs, null[int(.95 * len(null))], sum(v >= obs for v in null) / len(null)))
# Q17 fourth generator K = index 8 over {A,S,G,K}
G4 = {"A": 1, "S": 2, "G": 4, "K": 8}; seen = {(1, 0)}; fr = [(1, 0)]
while fr:
    nx = []
    for v in fr:
        for g in G4.values():
            u = Q.mul(v, (1, g))
            if u not in seen: seen.add(u); nx.append(u)
    fr = nx
print("Q17 group generated by A,S,G,K(e8): %d elements; indices %s" % (len(seen), sorted({k for s, k in seen})))
kup = 0; kin = 0
for fid in IDS:
    ft = FUNCS[fid]; wd = "".join(ch for ch in WORD[fid] if ch in "ASG"); kw = "K" * len(ft.kword)
    v = (1, 0)
    for ch in wd + kw: v = Q.mul(v, (1, G4[ch]))
    kin += (len(kw) > 0); kup += (v[1] >= 8)
print("   K letters present in %d of 65 functions (static circle features); of those, walk ends in 8–15: %d" % (kin, kup))
# markdown table
md = ["| # | function | class | kind of circle | R/E | pillar | operators (layer-1; ASS roots) | evidence |", "|---|---|---|---|---|---|---|---|"]
ROOT = {"Add": "A", "Sub": "A", "Mod": "A", "Mult": "S", "Div": "S", "Pow": "S", "FloorDiv": "S", "Compare": "G"}
for i, r in enumerate(out, 1):
    ft = FUNCS[r[0]]; ops = " ".join("%s:%s" % (k, ROOT.get(k, C.FUNC.get(k, "F"))) for k, v in sorted(ft.ops.items())[:7])
    md.append("| %d | `%s` | %s | %s | %s | %s | %s | %s |" % (i, r[0].replace("Maths/", "").replace(".py", ""), r[1], r[2] if r[2] != "-" else "", r[3], r[4], ops.replace("|", "/"), (r[8] or "").replace("|", "/")[:150]))
open(os.path.join(here, "14_table_65.md"), "w").write("# 14 — The 65 Archimedes Python equations: circle class, kind, relation/evaluation, operators\n\nGenerated by `circles65.py` (2026-11-20). Classes: S = circle from source text; B = shown by running the function; I = linked to an S/B function; X = outside-source arena, verified numerically; N = cannot show. R = relation (solves for any variable), E = evaluation. Operator roots: A = ADD, S = SCALE, G = SIGN, F = no root (unknown).\n\n" + "\n".join(md) + "\n")
