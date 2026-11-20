"""unit_tree.py (exploratory, unregistered): the F = m a family as a 3D node graph, two embeddings.
   LEFT  unit space: a node sits at its dimension vector (M, L, T); multiplying quantities ADDS positions (units multiply like digits).
   RIGHT ASS space:  a node sits at (ADD, SCALE, SIGN) counts of its derivation; d/dt = ADD (the D generator), multiply = SCALE, divide = SCALE + SIGN (inverse).
   The assignment of operators to A/S/G is PROVISIONAL (THEORETICAL). Dimension vectors are computed from the derivations and checked against a hand-typed SI table.
   ValaQuenta/.venv/bin/python unit_tree.py   -> unit_tree_<view>.png"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
BASE = {"m": (1, 0, 0), "x": (0, 1, 0), "t": (0, 0, 1)}
# name: (op, args) ; ops: mul, div, ddt (d/dt), pow handled as mul chains
DER = {
    "v": ("ddt", ["x"]), "a": ("ddt", ["v"]), "jerk": ("ddt", ["a"]),
    "p": ("mul", ["m", "v"]), "F": ("mul", ["m", "a"]), "F2": ("ddt", ["p"]),   # F2 = dp/dt: the second route to force
    "E": ("mul", ["F", "x"]), "P": ("div", ["E", "t"]), "area": ("mul", ["x", "x"]), "vol": ("mul", ["x", "area"]),
    "press": ("div", ["F", "area"]), "rho": ("div", ["m", "vol"]), "freq": ("div", ["x_", "t"]),
    "ang_mom": ("mul", ["x", "p"]), "action": ("mul", ["E", "t"]), "impulse": ("mul", ["F", "t"]),
}
BASE["x_"] = (0, 0, 0)    # the number 1 (dimensionless) so that 1/t is a division
SI = {"v": (0, 1, -1), "a": (0, 1, -2), "jerk": (0, 1, -3), "p": (1, 1, -1), "F": (1, 1, -2), "F2": (1, 1, -2), "E": (1, 2, -2), "P": (1, 2, -3),
      "area": (0, 2, 0), "vol": (0, 3, 0), "press": (1, -1, -2), "rho": (1, -3, 0), "freq": (0, 0, -1), "ang_mom": (1, 2, -1), "action": (1, 2, -1), "impulse": (1, 1, -1)}
unit, word = {k: np.array(v) for k, v in BASE.items()}, {k: np.zeros(3, int) for k in BASE}    # word = (ADD, SCALE, SIGN) counts
edges = []
def build(n):
    if n in unit: return
    op, args = DER[n]
    for a_ in args: build(a_)
    if op == "mul": unit[n] = unit[args[0]] + unit[args[1]]; word[n] = word[args[0]] + word[args[1]] + (0, 1, 0)
    if op == "div": unit[n] = unit[args[0]] - unit[args[1]]; word[n] = word[args[0]] + word[args[1]] + (0, 1, 1)
    if op == "ddt": unit[n] = unit[args[0]] - unit["t"]; word[n] = word[args[0]] + (1, 0, 0)
    for a_ in args: edges.append((a_, n, op))
for n in DER: build(n)
bad = [n for n in SI if tuple(unit[n]) != SI[n]]
print("dimension vectors derived vs SI table: mismatches =", bad)
assert not bad and tuple(unit["F"]) == tuple(unit["F2"])
print("F = m a and F = dp/dt land on the same point:", tuple(unit["F"]), "; action and angular momentum share", tuple(unit["action"]))
col = {"mul": "#1f77b4", "div": "#d95f02", "ddt": "#2ca02c"}
names = [n for n in unit if n != "x_"]
def panel(ax, P, labels, title, off):
    for a_, b_, op in edges:
        if "x_" in (a_, b_): continue
        ax.plot(*zip(P[a_], P[b_]), color=col[op], lw=1.6, alpha=0.85)
    for n in names:
        ax.scatter(*P[n], s=70 if n in BASE else 46, color="k" if n in BASE else "#c9a000" if n in ("F", "F2") else "#555")
        ax.text(P[n][0] + off[0], P[n][1] + off[1], P[n][2] + off[2], "F" if n == "F2" else n, fontsize=8)
    pts = np.array([P[n] for n in names]); lo, hi = pts.min(0) - .7, pts.max(0) + .7
    ax.set_xlim(lo[0], hi[0]); ax.set_ylim(lo[1], hi[1]); ax.set_zlim(lo[2], hi[2])
    ax.set_xlabel(labels[0]); ax.set_ylabel(labels[1]); ax.set_zlabel(labels[2]); ax.set_title(title, fontsize=10)
    return lo, hi
for tag, (el, az) in {"iso": (22, -55), "side": (8, -90), "top": (89.5, -90)}.items():
    fig = plt.figure(figsize=(15, 7))
    a1 = fig.add_subplot(121, projection="3d"); a2 = fig.add_subplot(122, projection="3d")
    r1 = panel(a1, unit, ("mass M", "length L", "time T"), "unit space: position = dimension vector (units multiply = positions add)", (.08, .08, .08))
    r2 = panel(a2, word, ("ADD  (d/dt)", "SCALE (× ÷)", "SIGN (÷, inverse)"), "ASS space: position = counts of A, S, G in the derivation", (.05, .05, .08))
    for a in (a1, a2): a.view_init(elev=el, azim=az)
    fig.text(.5, .02, "edges: blue = multiply (SCALE), orange = divide (SCALE+SIGN), green = d/dt (ADD).  gold = force, reached two ways (m·a and dp/dt) at one point.  THEORETICAL assignment of operators to A/S/G, provisional.", ha="center", fontsize=8)
    fig.savefig(f"unit_tree_{tag}.png", dpi=110, bbox_inches="tight"); plt.close(fig)
    if tag == "iso":
        for nm, P in (("unit", unit), ("ass", word)):
            pts = np.array([P[n] for n in names]); print(nm, "bbox", pts.min(0).tolist(), pts.max(0).tolist(), "distinct points", len({tuple(p) for p in pts}), "of", len(names))
