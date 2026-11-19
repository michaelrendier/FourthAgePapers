"""One SVG per Lagrangian, four panels each (isometric, top, front, side), on the Mexican hat (the Witch's Hat), plus one SVG of the Standard-Model context.

The paths come from the ValaQuenta engines; nothing is aimed or designed in this file.  The pictures are normalised to brim radius 1 and depth 1.

    L_SM        the Standard-Model Higgs hat and the stationary paths of the action between two events (modules/witches_hat/action.py)
    L_NN        the VAPMIP hat as coded (tilted by the coupling), the SM hat as a ghost, the as-coded bowl as a ghost, and the paths on it
    L_(I|O)     the SM hat with 16 branches brim -> hilltop coloured by J_red / J_blue, and the flat integrand drawn as a ribbon
    L_dynamic   the original (wiki 51): the hat moves, the particle exchanges energy dE = integral dV/dt dt with it

Run with the ValaQuenta venv:  ~/Projects/ThePlace/ValaQuenta/.venv/bin/python render_lagrangian_svgs.py
Writes ../papers/figures/lagrangians/v1.0/WitchesHat_Lagrangians_v1.0_*.svg and index.html (version 1.0; version 2.0 is render_lagrangians_v2.py).
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace"))
from ValaQuenta.modules.witches_hat import action as AC          # noqa: E402
from ValaQuenta.modules.witches_hat import maths as W            # noqa: E402
from ValaQuenta.modules.lagrangian_sm import maths as S          # noqa: E402

VERSION = "v1.0"
OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "papers", "figures", "lagrangians", VERSION))      # figures live with the paper; v2.0 is render_lagrangians_v2.py
BG, FG, MUTED = "#0b1220", "#e6edf3", "#8b98a9"
GOLD, WHITE = "#f2cc60", "#ffffff"
CHUNKED = False                                                   # v2 sets True: polyline chunks instead of one element per sample
R_EXT = 1.6                                                       # radial extent of the drawn hat (brim radius = 1)


# ------------------------------------------------------------------ geometry
def hat_z(x, y):
    """Normalised Standard-Model hat: brim at r = 1 (z = -1), hilltop at the origin (z = 0): z = r^4 - 2 r^2."""
    r2 = np.asarray(x, float)**2 + np.asarray(y, float)**2
    return r2*r2 - 2*r2


def ring(radius, z_of, n=181, cx=0.0, cy=0.0, lift=0.0):
    t = np.linspace(0, 2*math.pi, n)
    x, y = cx + radius*np.cos(t), cy + radius*np.sin(t)
    return np.stack([x, y, z_of(x - cx, y - cy) + lift], 1)


VIEWS = {"ISOMETRIC": (45.0, 35.264), "TOP  (x, y)": (0.0, 90.0), "FRONT  (x, z)": (0.0, 0.0), "SIDE  (y, z)": (90.0, 0.0)}


def project(P, az, el):
    """Orthographic view: returns screen x, screen y (up positive) and depth (larger = nearer the camera)."""
    a, e = math.radians(az), math.radians(el)
    P = np.asarray(P, float).reshape(-1, 3); x, y, z = P[:, 0], P[:, 1], P[:, 2]
    x1 = x*math.cos(a) - y*math.sin(a); y1 = x*math.sin(a) + y*math.cos(a)
    return x1, z*math.cos(e) + y1*math.sin(e), -y1*math.cos(e) + z*math.sin(e)


def palette(t):
    """Height colour: deep indigo (brim) -> blue -> ice (high).  Gold, white and the warm colours are reserved for the brim, the hilltop and the paths."""
    stops = [(0.0, (24, 38, 104)), (0.35, (36, 96, 160)), (0.65, (70, 150, 190)), (0.85, (140, 200, 220)), (1.0, (205, 232, 240))]
    t = float(np.clip(t, 0, 1))
    for (a, ca), (b, cb) in zip(stops, stops[1:]):
        if t <= b:
            f = (t - a)/(b - a); return "#%02x%02x%02x" % tuple(int(ca[i] + f*(cb[i] - ca[i])) for i in range(3))
    return "#%02x%02x%02x" % stops[-1][1]


# ------------------------------------------------------------------ scene -> primitives -> SVG
class Scene:
    """A hat surface, ghost wireframes, polylines and markers in world coordinates (x, y, z)."""

    def __init__(self, surface, title, subtitle, legend, zlim=(-1.0, 1.5)):
        self.surface, self.title, self.subtitle, self.legend, self.zlim = surface, title, subtitle, legend, zlim
        self.lines, self.points, self.ghosts, self.notes = [], [], [], []
        self.xlim = (-R_EXT, R_EXT); self.ylim = (-R_EXT, R_EXT)

    def line(self, pts, color, width=2.2, dash=None, opacity=1.0, halo=True):
        self.lines.append(dict(p=np.asarray(pts, float), c=color, w=width, d=dash, o=opacity, halo=halo))

    def point(self, p, color, r=5.0, label=None):
        self.points.append(dict(p=np.asarray(p, float), c=color, r=r, label=label))

    def ghost(self, fn, color, opacity=0.35, zmax=None, nr=9, nt=24, rmax=R_EXT):
        self.ghosts.append(dict(fn=fn, c=color, o=opacity, zmax=zmax, nr=nr, nt=nt, rmax=rmax))


def cut(view, x, y):
    """True where the surface is cut away so the hill and the trough can be seen: the wedge or half that faces the camera."""
    if view.startswith("ISO"): return x < 0 and y < 0
    if view.startswith("FRONT"): return y < 0
    if view.startswith("SIDE"): return x < 0
    return False


def surface_quads(sc, view, nr=22, nt=44):
    rs = np.linspace(0, R_EXT, nr + 1); ts = np.linspace(0, 2*math.pi, nt + 1); X = np.outer(rs, np.cos(ts)); Y = np.outer(rs, np.sin(ts)); Z = sc.surface(X, Y)
    z0, z1 = sc.zlim; quads = []
    for i in range(nr):
        for j in range(nt):
            if cut(view, 0.25*(X[i, j] + X[i + 1, j] + X[i + 1, j + 1] + X[i, j + 1]), 0.25*(Y[i, j] + Y[i + 1, j] + Y[i + 1, j + 1] + Y[i, j + 1])): continue
            pts = np.array([[X[i, j], Y[i, j], Z[i, j]], [X[i + 1, j], Y[i + 1, j], Z[i + 1, j]], [X[i + 1, j + 1], Y[i + 1, j + 1], Z[i + 1, j + 1]], [X[i, j + 1], Y[i, j + 1], Z[i, j + 1]]])
            quads.append((pts, palette((pts[:, 2].mean() - z0)/(z1 - z0))))
    return quads


def render_panel(sc, view, ox, oy, pw, ph):
    az, el = VIEWS[view]; out = []; prims = []
    # world box -> scale
    x0, x1 = sc.xlim; y0, y1 = sc.ylim; z0, z1 = sc.zlim
    corners = np.array([[a, b, c] for a in (x0, x1) for b in (y0, y1) for c in (z0, z1)])
    sx, sy, _ = project(corners, az, el); bw, bh = sx.max() - sx.min(), sy.max() - sy.min()
    k = 0.88*min(pw/bw, (ph - 36)/bh); cx, cy = (sx.max() + sx.min())/2, (sy.max() + sy.min())/2
    X = lambda u: ox + pw/2 + (u - cx)*k
    Y = lambda v: oy + 20 + (ph - 36)/2 - (v - cy)*k + 10
    def poly(pts):
        u, v, _ = project(pts, az, el); return " ".join("%.1f,%.1f" % (X(a), Y(b)) for a, b in zip(u, v))
    for pts, col in surface_quads(sc, view):
        d = project(pts, az, el)[2].mean(); prims.append((d, '<polygon points="%s" fill="%s" fill-opacity="0.93" stroke="#0b1220" stroke-opacity="0.35" stroke-width="0.4"/>' % (poly(pts), col)))
    for g in sc.ghosts:                                                    # wireframe ghosts: rings and spokes
        for rr in np.linspace(g["rmax"]/g["nr"], g["rmax"], g["nr"]):
            t = np.linspace(0, 2*math.pi, 120); x, y = rr*np.cos(t), rr*np.sin(t); z = g["fn"](x, y)
            if g["zmax"] is not None: z = np.minimum(z, g["zmax"])
            P = np.stack([x, y, z], 1); u, v, d = project(P, az, el)
            for i in range(0, len(u) - 1, 2):
                if cut(view, P[i, 0], P[i, 1]): continue
                prims.append((d[i] + 0.01, '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity="%.2f" stroke-width="0.9"/>' % (X(u[i]), Y(v[i]), X(u[i + 1]), Y(v[i + 1]), g["c"], g["o"])))
        for a in np.linspace(0, 2*math.pi, g["nt"], endpoint=False):
            r = np.linspace(0, g["rmax"], 40); x, y = r*math.cos(a), r*math.sin(a); z = g["fn"](x, y)
            if g["zmax"] is not None: z = np.minimum(z, g["zmax"])
            P = np.stack([x, y, z], 1); u, v, d = project(P, az, el)
            for i in range(0, len(u) - 1, 2):
                if cut(view, P[i, 0], P[i, 1]): continue
                prims.append((d[i] + 0.01, '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity="%.2f" stroke-width="0.9"/>' % (X(u[i]), Y(v[i]), X(u[i + 1]), Y(v[i + 1]), g["c"], g["o"])))
    # section curves in the front and side views: the profile through the hilltop (the W shape of the hat)
    if view.startswith("FRONT") or view.startswith("SIDE"):
        tt = np.linspace(-R_EXT, R_EXT, 160)
        for fn, col, w_, dash in [(sc.surface, WHITE, 2.0, None)] + [(g["fn"], g["c"], 1.4, "4 3") for g in sc.ghosts if g["zmax"] is None]:
            P = np.stack([tt, 0*tt, fn(tt, 0*tt)], 1) if view.startswith("FRONT") else np.stack([0*tt, tt, fn(0*tt, tt)], 1)
            u, v, d = project(P, az, el)
            for i in range(len(u) - 1):
                prims.append((50.0, '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"%s/>' % (X(u[i]), Y(v[i]), X(u[i + 1]), Y(v[i + 1]), col, w_, (' stroke-dasharray="%s"' % dash) if dash else "")))
    for ln in sc.lines:
        P = ln["p"]; u, v, d = project(P, az, el)
        if CHUNKED:                                                            # v2: each path is a few short coloured polylines, not one element per sample (10x smaller files)
            ch = max(3, len(P)//14)
            for i in range(0, len(P) - 1, ch):
                j = min(i + ch, len(P) - 1)
                if np.isnan(P[i:j + 1]).any() or j <= i: continue
                col = ln["c"][(i + j)//2] if isinstance(ln["c"], list) else ln["c"]; dash = ' stroke-dasharray="%s"' % ln["d"] if ln["d"] else ""
                pts = " ".join("%.1f,%.1f" % (X(u[k]), Y(v[k])) for k in range(i, j + 1)); dd = float(np.mean(d[i:j + 1])) + 0.03
                if ln["halo"]: prims.append((dd, '<polyline points="%s" fill="none" stroke="#0b1220" stroke-opacity="0.8" stroke-width="%.1f" stroke-linecap="round"/>' % (pts, ln["w"] + 2.2)))
                prims.append((dd + 0.001, '<polyline points="%s" fill="none" stroke="%s" stroke-opacity="%.2f" stroke-width="%.1f" stroke-linecap="round"%s/>' % (pts, col, ln["o"], ln["w"], dash)))
            continue
        step = max(1, len(P)//90)
        idx = list(range(0, len(P) - 1, step))
        for i in idx:
            j = min(i + step, len(P) - 1)
            if np.isnan(P[i]).any() or np.isnan(P[j]).any(): continue
            col = ln["c"][i] if isinstance(ln["c"], list) else ln["c"]
            dash = ' stroke-dasharray="%s"' % ln["d"] if ln["d"] else ""
            dd = 0.5*(d[i] + d[j]) + 0.03
            if ln["halo"]:
                prims.append((dd, '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#0b1220" stroke-opacity="0.8" stroke-width="%.1f" stroke-linecap="round"/>' % (X(u[i]), Y(v[i]), X(u[j]), Y(v[j]), ln["w"] + 2.2)))
            prims.append((dd + 0.001, '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity="%.2f" stroke-width="%.1f" stroke-linecap="round"%s/>' % (X(u[i]), Y(v[i]), X(u[j]), Y(v[j]), col, ln["o"], ln["w"], dash)))
    for pt in sc.points:
        u, v, d = project(pt["p"], az, el); prims.append((d[0] + 0.05, '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="#0b1220" stroke-width="1.2"/>' % (X(u[0]), Y(v[0]), pt["r"], pt["c"])))
    for lb in getattr(sc, "labels", []):                                        # optional text labels (v2): world point + text
        u, v, d = project(lb["p"], az, el); prims.append((d[0] + 0.5, '<text x="%.1f" y="%.1f" fill="%s" font-size="12" font-weight="600" paint-order="stroke" stroke="#0b1220" stroke-width="3">%s</text>' % (X(u[0]) + 8, Y(v[0]) - 6, lb.get("c", FG), lb["t"])))
    prims.sort(key=lambda t: t[0]); out += [p for _, p in prims]
    # gnomon
    gx, gy = ox + 34, oy + ph - 18
    for name, vec, col in (("x", (1, 0, 0), "#ff7b72"), ("y", (0, 1, 0), "#7ee787"), ("z", (0, 0, 1), "#79c0ff")):
        u, v, _ = project(np.array([vec]), az, el); L = 24
        if abs(u[0]) + abs(v[0]) < 1e-6: out.append('<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/><text x="%.1f" y="%.1f" fill="%s" font-size="11">%s</text>' % (gx, gy, col, gx + 6, gy - 4, col, name)); continue
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/><text x="%.1f" y="%.1f" fill="%s" font-size="11">%s</text>' % (gx, gy, gx + L*u[0], gy - L*v[0], col, gx + L*u[0]*1.25 + 2, gy - L*v[0]*1.25 + 4, col, name))
    out.append('<text x="%.1f" y="%.1f" fill="%s" font-size="13" font-weight="600" letter-spacing="1.2">%s</text>' % (ox + 14, oy + 18, MUTED, view))
    return "\n".join(out)


def write_svg(sc, name):
    W_, H_ = 1500, 1345; pw, ph = 730, 560; out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" font-family="Helvetica, Arial, sans-serif">' % (W_, H_, W_, H_),
                                                  '<rect width="100%%" height="100%%" fill="%s"/>' % BG,
                                                  '<text x="30" y="40" fill="%s" font-size="25" font-weight="700">%s</text>' % (FG, sc.title),
                                                  '<text x="30" y="66" fill="%s" font-size="14">%s</text>' % (MUTED, sc.subtitle)]
    for i, view in enumerate(VIEWS):
        ox, oy = 20 + (i % 2)*(pw + 10), 84 + (i//2)*(ph + 8)
        out.append('<rect x="%d" y="%d" width="%d" height="%d" rx="8" fill="#0f1a2e" stroke="#1f2c44"/>' % (ox, oy, pw, ph))
        out.append(render_panel(sc, view, ox, oy, pw, ph))
    y = 84 + 2*(ph + 8) + 22
    for i, (col, text) in enumerate(sc.legend):
        out.append('<rect x="%d" y="%d" width="22" height="6" rx="3" fill="%s"/><text x="%d" y="%d" fill="%s" font-size="13">%s</text>' % (30 + (i % 2)*730, y + (i//2)*22 - 7, col, 60 + (i % 2)*730, y + (i//2)*22, FG, text))
    out.append("</svg>")
    path = os.path.join(OUT, name); open(path, "w").write("\n".join(out)); return path


def common(sc):
    """The brim and the hilltop on every panel, and the inflection circle (where the hat changes curvature): the three things that organise the picture."""
    sc.line(ring(1.0, sc.surface, lift=0.02), GOLD, width=3.6)
    sc.line(ring(1/math.sqrt(3), sc.surface, lift=0.02), "#b8c4d6", width=1.1, dash="4 4", opacity=0.8, halo=False)
    sc.point((0, 0, float(sc.surface(0.0, 0.0)) + 0.03), WHITE, 5.5)


# ------------------------------------------------------------------ the four scenes
def scene_sm():
    SM = W.lagrangian_sm(mu2=1.0, lam=1.0)
    sc = Scene(hat_z, "L_SM — the Standard-Model Higgs hat and the path of the action",
               "V(h) = −μ²h²/2 + λh⁴/4 (brim radius 1, depth 1).  Coloured lines: every stationary path (δS = 0) between the same two events, found by solving the Euler–Lagrange equations; nothing is aimed.",
               [(GOLD, "the brim: the vacuum circle (V minimum, the Goldstone directions run around it)"), (WHITE, "the hilltop (symmetric point, V = 0)"),
                ("#b8c4d6", "inflection circle r = 1/√3: curvature changes sign (inside: tachyonic, outside: stable)"), ("#3fb950", "stationary path, Morse index 0 (a minimum of the action), S = 0.7742"),
                ("#f0883e", "stationary path, index 1 (a saddle: a neighbouring path does less work), S = 0.7906"), ("#db61a2", "stationary path, index 2, S = 10.88: swings out to r = 2.66 and back; drawn only inside r = 1.6"),
                ("#5a7fb0", "grey-blue: the whole fan of paths from the brim point at E = 0 (every launch direction)"), (FG, "start (brim) and end event")], zlim=(-1.0, 1.7))
    fam = AC.ray_family(SM, (1.0, 0.0), E=0.0, n_theta=9, t_max=2.0, n_t=201); B = fam["q"][2, 200]; T = fam["t"][200]
    ps = AC.stationary_paths(SM, (1.0, 0.0), B, T, N=200)
    fan = AC.ray_family(SM, (1.0, 0.0), E=0.0, n_theta=28, t_max=3.2, n_t=170)
    for i in range(fan["q"].shape[0]):
        q = fan["q"][i]; m = np.hypot(q[:, 0], q[:, 1]) < R_EXT; q = q[m]
        if len(q) > 2: sc.line(np.stack([q[:, 0], q[:, 1], hat_z(q[:, 0], q[:, 1]) + 0.02], 1), "#5a7fb0", width=1.0, opacity=0.55, halo=False)
    cols = {0: "#3fb950", 1: "#f0883e", 2: "#db61a2"}
    for p in ps:
        q = p["q"]; r = np.hypot(q[:, 0], q[:, 1]); z = hat_z(q[:, 0], q[:, 1]) + 0.05; z[r > R_EXT] = np.nan; P = np.stack([q[:, 0], q[:, 1], z], 1)
        sc.line(P, cols.get(p["index"], FG), width=3.2); print("  path index %d: S = %.4f, max r = %.2f brim radii%s" % (p["index"], p["S"], r.max(), " (drawn only inside r = %.1f)" % R_EXT if r.max() > R_EXT else ""))
    sc.point((1.0, 0.0, hat_z(1.0, 0.0) + 0.05), FG, 5.5); sc.point((B[0], B[1], hat_z(B[0], B[1]) + 0.05), FG, 5.5)
    common(sc); return sc


def scene_nn():
    vap = W.lagrangian_vap(mu_sq=-1.0, lam=0.5, g=0.2, psi=(1.0, 0.0), convention="ssb"); bowl = W.lagrangian_vap(mu_sq=-1.0, lam=0.5, g=0.2, psi=(1.0, 0.0), convention="as_coded")
    R, depth = vap["brim_radius"], vap["depth"]; top = W.hilltop(vap); V2 = vap["V2"]; z_top = float(V2(*top))
    surf = lambda x, y: (V2(np.asarray(x, float)*R, np.asarray(y, float)*R) - z_top)/depth
    bowl_fn = lambda x, y: (bowl["V2"](np.asarray(x, float)*R, np.asarray(y, float)*R) - z_top)/depth
    sc = Scene(surf, "L_NN (VAPMIP) — the hat as coded, tilted by the coupling, against the Standard-Model hat",
               "L_bias is exactly −V_SM, so the hat is the same quartic.  The coupling −(g/φ)ψ·β tilts it (g = 0.2): the hilltop moves.  As coded with μ² = −1 the potential is a bowl (no brim).",
               [(GOLD, "the brim of the untilted hat (r = 1)"), (WHITE, "the hilltop of the TILTED hat (moved off centre by the coupling)"), ("#a5a5ff", "grey wire: the Standard-Model hat"),
                ("#c28cff", "violet wire: L_bias as coded with μ² = −1 (a bowl, clipped at z = 2.4)"), ("#2ec4b6", "paths from the brim toward the hilltop (leapfrog, E = V at the hilltop)")], zlim=(-1.0, 2.4))
    sc.ghost(hat_z, "#a5a5ff", 0.45, nr=8, nt=20); sc.ghost(bowl_fn, "#c28cff", 0.5, zmax=2.4, nr=8, nt=20, rmax=1.45)
    for k in range(14):
        a = 2*math.pi*k/14; p = W.trace_plane(vap, (R*math.cos(a), R*math.sin(a)), top, 0.0, float(V2(*top)))
        x, y = p["x"]/R, p["y"]/R; z = surf(x, y) + 0.04; sc.line(np.stack([x, y, z], 1), "#2ec4b6", width=2.0, opacity=0.9)
    sc.line(ring(1.0, surf, lift=0.03), GOLD, width=3.6); sc.line(ring(1/math.sqrt(3), surf, lift=0.03), "#b8c4d6", width=1.1, dash="4 4", opacity=0.8, halo=False)
    sc.point((top[0]/R, top[1]/R, float(surf(top[0]/R, top[1]/R)) + 0.04), WHITE, 5.5); return sc


def scene_lio():
    E = 1.0; sc = Scene(hat_z, "L_(I|O) = ∫ J_red · J_blue ds — sixteen branches from the brim to the point, and a flat integrand",
                        "On the SM hat (σ = r/2: hilltop σ = 0, brim σ = ½).  Each branch is coloured by the balance of the two currents; the ribbon above the front branch shows J_red, J_blue and their product: the product is the constant e^(−E).",
                        [(GOLD, "the brim (σ = ½: the equal-current point, branches turn white; min(J_red, J_blue) peaks here)"), (WHITE, "the hilltop (σ = 0)"), ("#ff7b72", "ribbon: J_red = e^(−(1−σ)E), the descending current"),
                         ("#58a6ff", "ribbon: J_blue = e^(−σE), the ascending current; branches are blue where it dominates (inside)"), (FG, "J_red · J_blue = e^(−E): flat, the same at every σ (dashed)")], zlim=(-1.0, 3.0))
    for k in range(16):
        a = 2*math.pi*k/16; r = np.linspace(1.0, 0.0, 60); x, y = r*math.cos(a), r*math.sin(a); z = hat_z(x, y) + 0.04
        sig = r/2; jr, jb = np.exp(-(1 - sig)*E), np.exp(-sig*E); f = jr/(jr + jb); fs = (f - f.min())/(0.5 - f.min())       # 0 at the hilltop (J_blue dominates), 1 at the brim (equal)
        cols = ["#%02x%02x%02x" % (int(88 + (255 - 88)*c), int(166 + (255 - 166)*c), 255) for c in fs]
        sc.line(np.stack([x, y, z], 1), cols, width=2.6)
    r = np.linspace(1.0, 0.0, 60); sig = r/2; jr, jb = np.exp(-(1 - sig)*E), np.exp(-sig*E); base = 1.2; sc_h = 1.4
    for J, c, d in ((jr, "#ff7b72", None), (jb, "#58a6ff", None), (jr*jb, FG, "5 4")):
        sc.line(np.stack([r, np.zeros_like(r), base + sc_h*J], 1), c, width=2.6, dash=d, halo=False)
    for rr in (1.0, 0.0):
        sc.line(np.array([[rr, 0, hat_z(rr, 0.0) + 0.04], [rr, 0, base]]), "#5b6b82", width=1.0, dash="2 3", opacity=0.8, halo=False)
    common(sc); return sc


def scene_dyn():
    SM = W.lagrangian_sm(mu2=1.0, lam=1.0); u = (0.25, 0.0); T = 8.0
    r = AC.moving_hat_exchange(SM, (1.0, 0.0), (0.0, 0.7), u, T, n=700); t, q, E = r["t"], r["q"], r["E"]; dE = E - E[0]; amp = max(abs(dE).max(), 1e-9)
    sc = Scene(hat_z, "Original L_dynamic — a hat that moves: the particle borrows and returns energy (slingshot)",
               "L_dynamic = L_standard + ∫ J_red · d(J_blue)/dt dλ (wiki 51, 2026-06-12): a time-dependent background.  The hat drifts at u = 0.25; the energy changes by dE = ∫ ∂V/∂t dt (identity to 1e-11).",
               [(GOLD, "the brim at t = 0; faint gold: the brim at t = T/2 and t = T (the hat has moved)"), (WHITE, "the hilltop at t = 0"), ("#58a6ff", "path coloured by ΔE: blue = energy given up to the field"),
                ("#ff7b72", "red = energy gained from the moving field"), (FG, "z of the path is the potential energy V(q − ut, t) at each time")], zlim=(-1.0, 1.6))
    sc.xlim = (-R_EXT, R_EXT + u[0]*T + 0.2)
    cols = ["#%02x%02x%02x" % (int(88 + (255 - 88)*(0.5 + 0.5*d/amp)), int(166 + (123 - 166)*(0.5 + 0.5*d/amp)), int(255 + (114 - 255)*(0.5 + 0.5*d/amp))) for d in dE]
    z = np.array([hat_z(q[i, 0] - u[0]*t[i], q[i, 1] - u[1]*t[i]) for i in range(len(t))])
    sc.line(np.stack([q[:, 0], q[:, 1], z + 0.05], 1), cols, width=3.0)
    for frac, op in ((0.5, 0.55), (1.0, 0.4)):
        cx = u[0]*T*frac; sc.line(ring(1.0, hat_z, cx=cx, lift=0.02), GOLD, width=2.0, opacity=op, halo=False); sc.point((cx, 0, 0.03), WHITE, 3.5)
    sc.line(np.array([[0, 0, 0.1], [u[0]*T, 0, 0.1]]), "#b8c4d6", width=1.2, dash="3 3", opacity=0.8, halo=False)
    sc.point((q[0, 0], q[0, 1], z[0] + 0.05), FG, 5.5); sc.point((q[-1, 0], q[-1, 1], z[-1] + 0.05), FG, 5.5); common(sc); return sc


def context_svg():
    """The Standard-Model context: what each particle does to the hat, how the hat changes with temperature, and the particle spectrum."""
    import matplotlib; matplotlib.use("svg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans"})
    v = S.fermi_vev(); h = np.linspace(0.05, 2.2, 300)*v; cw = S.coleman_weinberg(h)
    fig, ax = plt.subplots(2, 2, figsize=(15, 11.5), facecolor=BG)
    for a in ax.ravel():
        a.set_facecolor("#0f1a2e"); [s.set_color("#1f2c44") for s in a.spines.values()]; a.tick_params(colors=MUTED); a.xaxis.label.set_color(FG); a.yaxis.label.set_color(FG); a.title.set_color(FG)
    a = ax[0, 0]; xs = h/v
    for k, c in (("top", "#ff7b72"), ("W", "#58a6ff"), ("Z", "#79c0ff"), ("higgs+goldstones", "#d2a8ff"), ("bottom", "#f2cc60")):
        a.plot(xs, cw[k]/1e6, color=c, lw=2.2, label={"top": "top (n = −12)", "W": "W (n = +6)", "Z": "Z (n = +3)", "higgs+goldstones": "Higgs + Goldstones (|m²|)", "bottom": "bottom (n = −12), ×1000"}[k] if k != "bottom" else "bottom (n = −12)")
    a.axhline(0, color=MUTED, lw=0.6); a.axvline(1, color=GOLD, lw=1.4, ls="--"); a.set_xlabel("h / v   (the gold line is the brim)"); a.set_ylabel("one-loop term, 10⁶ GeV⁴"); a.set_title("Each particle adds its own term to the hat (Coleman–Weinberg, μ = v)", fontsize=12)
    a.legend(facecolor="#0f1a2e", edgecolor="#1f2c44", labelcolor=FG, fontsize=9)
    a = ax[0, 1]; hh = np.linspace(0, 1.4*v, 400)
    for T, c in ((100, "#79c0ff"), (140, "#7ee787"), (150, "#f2cc60"), (160, "#ffa657"), (166, "#ff7b72"), (180, "#d2a8ff")):
        r = S.finite_temperature_hat(T, hh); a.plot(hh/v, r["V"]/1e8, color=c, lw=2.2, label="T = %d GeV  (brim at %.2f v)" % (T, r["h_min"]/v))
    r0 = S.finite_temperature_hat(0, hh); a.plot(hh/v, (-0.5*S.higgs_sector()["mu2"]*hh**2 + 0.25*S.higgs_sector()["lam"]*hh**4)/1e8, color=FG, lw=1.6, ls=":", label="T = 0")
    a.axhline(0, color=MUTED, lw=0.6); a.set_xlabel("h / v"); a.set_ylabel("V(h, T) − V(0, T), 10⁸ GeV⁴"); a.set_title("The hat against temperature: no levels, it deepens and widens as it cools", fontsize=11)
    a.legend(facecolor="#0f1a2e", edgecolor="#1f2c44", labelcolor=FG, fontsize=9)
    a = ax[1, 0]; Ts = np.linspace(100, 175, 90); hm = [S.finite_temperature_hat(T)["h_min"]/v for T in Ts]; dp = [S.finite_temperature_hat(T)["depth"]/1e8 for T in Ts]
    a.plot(Ts, hm, color=GOLD, lw=2.6, label="brim radius / v"); a.set_xlabel("temperature T, GeV (valid above ≈ 100 GeV)"); a.set_ylabel("brim radius / v", color=GOLD); a2 = a.twinx(); a2.plot(Ts, dp, color="#58a6ff", lw=2.6, label="depth"); a2.set_ylabel("depth, 10⁸ GeV⁴", color="#58a6ff")
    a2.tick_params(colors=MUTED); a2.spines["right"].set_color("#1f2c44"); a.axvline(S.finite_temperature_hat(100)["T0"], color="#ff7b72", ls="--", lw=1.2); a.set_title("Brim radius and depth against temperature (T₀ = 163 GeV dashed)", fontsize=12)
    a = ax[1, 1]
    parts = [("ν (<1e-9)", 1e-9, "#8b98a9"), ("e", 0.000511, "#f2cc60"), ("μ", 0.10566, "#f2cc60"), ("u", 0.00216, "#7ee787"), ("d", 0.0047, "#7ee787"), ("s", 0.0935, "#7ee787"), ("τ", 1.777, "#f2cc60"), ("c", 1.273, "#7ee787"), ("b", 4.186, "#7ee787"),
             ("W", 80.36, "#58a6ff"), ("Z", 91.19, "#58a6ff"), ("H", 125.2, "#d2a8ff"), ("t", 172.6, "#ff7b72"), ("γ, g", 1e-9, "#8b98a9")]
    parts = sorted(parts, key=lambda t: t[1]); a.barh([p[0] for p in parts], [max(p[1], 1e-4) for p in parts], color=[p[2] for p in parts]); a.set_xscale("log"); a.set_xlabel("mass, GeV (log); in the SM mass = coupling to the hat × v")
    a.set_title("The spectrum: mass = coupling to the one hat × v (grey: ≈ 0)", fontsize=11)
    fig.suptitle("The Standard-Model context of the hat: particles, temperature, spectrum", color=FG, fontsize=17, fontweight="bold", y=0.995); fig.tight_layout(rect=(0, 0, 1, 0.97))
    path = os.path.join(OUT, "WitchesHat_Lagrangians_v1.0_sm_context.svg"); fig.savefig(path, facecolor=BG); plt.close(fig); return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True); made = []
    for name, fn in (("WitchesHat_Lagrangians_v1.0_L_SM.svg", scene_sm), ("WitchesHat_Lagrangians_v1.0_L_NN.svg", scene_nn), ("WitchesHat_Lagrangians_v1.0_L_IO.svg", scene_lio), ("WitchesHat_Lagrangians_v1.0_L_dynamic_original.svg", scene_dyn)):
        made.append(write_svg(fn(), name)); print("wrote", made[-1], "%.0f KB" % (os.path.getsize(made[-1])/1024))
    made.append(context_svg()); print("wrote", made[-1])
    html = ['<!doctype html><meta charset="utf-8"><title>The Lagrangians on the Witch\'s Hat</title><body style="background:#0b1220;color:#e6edf3;font-family:Helvetica,Arial,sans-serif;margin:24px">',
            "<h1>The Lagrangians on the Mexican hat, v1.0 (drawn on the potential surface)</h1><p>Each SVG has four views: isometric, top, front, side. Brim in gold, hilltop in white.</p>"]
    for p in made: html.append('<h2>%s</h2><p><a style="color:#79c0ff" href="%s">%s</a></p><img src="%s" style="max-width:100%%">' % (os.path.basename(p)[:-4], os.path.basename(p), os.path.basename(p), os.path.basename(p)))
    open(os.path.join(OUT, "index.html"), "w").write("\n".join(html)); print("wrote", os.path.join(OUT, "index.html"))
