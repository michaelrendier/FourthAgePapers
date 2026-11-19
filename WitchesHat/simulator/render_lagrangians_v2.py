"""WitchesHat Lagrangians, version 2.0: what the maths says, drawn exactly.  Nothing here is drawn to resemble anything.

For each Lagrangian the bundle of paths from EVERY point of the brim in EVERY launch direction is integrated (ValaQuenta/modules/witches_hat/action.py, brim_bundle); a path is kept only
if it passes within 0.15 brim radii of the hilltop (selected by what it does, not by how it was launched); each is drawn at height z = z_V(start) + W/(V0 tau0), the hat's own units
(brim 0, symmetric hilltop 1), so the cone stands on the surface at the brim.  The tip report gives where the paths meet and how high the cone stands above the hilltop.

    L_SM       the Standard-Model Higgs hat; the action is multivalued at the tip: the direct sheet and the sheet that goes out to the wall and back
    L_NN       the VAPMIP hat, tilted by the coupling (g = 0.2): the tip moves, the sheets multiply, the cone no longer stands on a level brim
    L_(I|O)    the functional exp(-E_J) x arc length evaluated on the SAME bundle as L_SM (it picks no paths of its own: its integrand is flat)
    L_dynamic  the SM hat drifting at u = 0.25 (original L_dynamic, wiki 51): the cone is sheared in the lab frame; W is no longer conserved

Run:  ~/Projects/ThePlace/ValaQuenta/.venv/bin/python render_lagrangians_v2.py     Writes ../papers/figures/lagrangians/v2.0/WitchesHat_Lagrangians_v2.0_*.svg and index.html
"""
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import render_lagrangian_svgs as R1                                                    # noqa: E402  (v1 helpers: projection, panels, writer)
from ValaQuenta.modules.witches_hat import action as AC                                # noqa: E402
from ValaQuenta.modules.witches_hat import maths as W                                  # noqa: E402

VERSION = "v2.0"
OUT = os.path.normpath(os.path.join(HERE, "..", "papers", "figures", "lagrangians", VERSION)); R1.OUT = OUT; R1.CHUNKED = True
FG, MUTED, GOLD, WHITE = R1.FG, R1.MUTED, R1.GOLD, R1.WHITE
E_J = 1.0                                                                               # the energy parameter in J_red = exp(-(1-sigma)E), J_blue = exp(-sigma E) (wiki 64)


def lightning(t):
    """violet at the brim (W = 0) -> cyan -> pale yellow at the tip."""
    t = float(np.clip(t, 0, 1)); a = np.array([124, 92, 255]); b = np.array([92, 225, 230]); c = np.array([255, 244, 184])
    col = a + (b - a)*min(t*2, 1) if t < 0.5 else b + (c - b)*(t - 0.5)*2
    return "#%02x%02x%02x" % tuple(int(x) for x in col)


def build_scene(model, bundle, rep, title, subtitle, legend, height=None, ztop_extra=0.15, thin=3, scale=1.0, lab="W"):
    """Scene from a bundle.  ``height(path, units)`` returns the height of every sample of a path; coordinates are in brim radii."""
    U = AC.natural_units(model); R = U["R"]
    surf = lambda x, y: U["zV"](np.stack([np.asarray(x, float)*R, np.asarray(y, float)*R], -1))
    height = height or (lambda p, U: float(U["zV"](p["q"][0])) + p["W"]/(U["depth"]*U["tau"])); sheet = rep["sheet_of"]; zs = []
    sc = Scene_(surf, title, subtitle, legend)
    paths = bundle["paths"]
    for k, p in enumerate(paths):
        if k % thin: continue
        q = p["q"]/R; z = height(p, U); zs.append(z.max()); low = sheet[k] == 0
        if low:
            cols = [lightning((zz - z[0])/max(z.max() - z[0], 1e-9)) for zz in z]
            sc.line(np.stack([q[:, 0], q[:, 1], z], 1), cols, width=1.7, opacity=0.95, halo=False)
        else:
            sc.line(np.stack([q[:, 0], q[:, 1], z], 1), "#8b3fa8", width=1.0, opacity=0.55, halo=False)
    sc.zlim = (0.0, max(zs + [1.4]) + ztop_extra); return sc, U, surf


class Scene_(R1.Scene):
    def __init__(self, *a, **k):
        super().__init__(*a, **k); self.labels = []


def finish(sc, U, surf, rep, R, hilltop, tip_label):
    """brim ring, inflection circle, hilltop, tip marker and the dimension line between them."""
    top = np.asarray(hilltop)/R; ztop = float(surf(top[0], top[1])); tip = np.asarray(rep["tip_xy"])/R; zt = rep["z_tip"]
    sc.line(R1.ring(1.0, lambda x, y: surf(x, y), lift=0.0), GOLD, width=3.6)
    sc.line(R1.ring(1/math.sqrt(3), lambda x, y: surf(x, y), lift=0.0), "#b8c4d6", width=1.1, dash="4 4", opacity=0.8, halo=False)
    sc.point((top[0], top[1], ztop + 0.02), WHITE, 5.5); sc.point((tip[0], tip[1], zt), "#fff4b8", 6.5)
    sc.line(np.array([[top[0], top[1], ztop], [tip[0], tip[1], zt]]), "#fff4b8", width=1.6, dash="3 3", halo=False)
    sc.labels.append({"p": np.array([tip[0], tip[1], zt]), "t": tip_label, "c": "#fff4b8"})
    return sc


def scene_sm(models):
    SM = models["SM"]; b = models["SM_b"]; r = models["SM_r"]; U = r["units"]; R = U["R"]
    sc, U, surf = build_scene(SM, b, r, "L_SM — the paths from every point of the brim, every direction: what reaches the tip",
        "Standard-Model Higgs hat (brim radius 1).  Kept only the paths that pass within 0.15 of the hilltop (selected by outcome, not aimed).  Height = the hat's own units: brim 0, hilltop 1; a path rises by W/(V0 τ0).",
        [(GOLD, "the brim ring: every source point on it"), (WHITE, "the hilltop (z = 1)"), ("#5ce1e6", "paths of the lowest sheet of the action: W = %.4f at the tip (closed form 0.4310)" % r["W_tip"]),
         ("#8b3fa8", "the second sheet: out to the wall at r = √2 and back, W = %.4f = 0.4310 + 2 × 0.2357" % r["sheets"][1]["W"]), ("#fff4b8", "the tip: %.4f above the hilltop (units of the depth); tip is %.4f R from the hilltop; paths: %d of %d launched" % (r["gap"], r["offset"], b["n_selected"], b["n_total"])),
         ("#b8c4d6", "inflection circle r = 1/√3")], thin=4)
    sc.zlim = (0.0, 2.75)
    return finish(sc, U, surf, r, R, b["hilltop"], "tip: +%.3f above the hilltop" % r["gap"])


def scene_nn(models):
    m = models["NN"]; b = models["NN_b"]; r = models["NN_r"]; R = m["brim_radius"]
    sc, U, surf = build_scene(m, b, r, "L_NN (VAPMIP, g = 0.2) — the same bundle on the tilted hat: the tip moves, the sheets multiply",
        "Same procedure on the hat of ValaQuenta's L_NN with the coupling −(g/φ)ψ·β.  The brim is no longer level (z = 0 is its ring average), so the cone does not stand on a level base.",
        [(GOLD, "the brim ring of the untilted hat (tilted by the coupling)"), (WHITE, "the hilltop of the tilted hat, moved to %.3f R" % (np.hypot(*b["hilltop"])/R)), ("#5ce1e6", "lowest sheet: %d paths, W = %.4f ± %.4f across them (a level brim gives ± 0)" % (r["n"], r["W_tip"], r["W_spread"])),
         ("#8b3fa8", "other sheets: %d of them (the SM hat has 2)" % (len(r["sheets"]) - 1)), ("#fff4b8", "the tip: %.4f R from the tilted hilltop, %.3f above it; height spread across the sources ± %.3f" % (r["offset"], r["gap"], r["z_tip_spread"])),
         ("#b8c4d6", "inflection circle")], thin=3)
    sc.zlim = (0.0, 3.2)
    return finish(sc, U, surf, r, R, b["hilltop"], "tip: %+.3f from the hilltop" % r["gap"])


def scene_lio(models):
    SM = models["SM"]; b = models["SM_b"]; r = models["SM_r"]; U0 = r["units"]; R = U0["R"]
    hL = lambda p, U: float(U["zV"](p["q"][0])) + np.exp(-E_J)*p["s"]/(U["depth"]*U["tau"])                  # L_(I|O) = exp(-E_J) x arc length, in the same natural units as W
    low = [p for k, p in enumerate(b["paths"]) if r["sheet_of"][k] == 0]
    zt = float(np.mean([float(AC.natural_units(SM)["zV"](p["q"][0])) + np.exp(-E_J)*p["closest"]["s"]/(U0["depth"]*U0["tau"]) for p in low]))
    sc, U, surf = build_scene(SM, b, r, "L_(I|O) = ∫ J_red·J_blue ds — evaluated on the same bundle: it picks no paths, it values them",
        "The integrand is the constant exp(−E_J) (E_J = 1, a free parameter of the definition), so the value of a path is exp(−E_J) × its arc length.  Drawn: the %d SM paths of L_SM, each at height exp(−E_J)·s in the same units." % len(b["paths"]),
        [(GOLD, "the brim ring"), (WHITE, "the hilltop (z = 1)"), ("#5ce1e6", "lowest sheet at height e^(−E_J) × arc length (arc length to the tip %.4f R)" % r["arc_tip"]),
         ("#fff4b8", "tip of L_(I|O) at z = %.4f (the action W reaches z = %.4f); E_J is free: the height scales with e^(−E_J)" % (zt, r["z_tip"])), ("#8b3fa8", "the wall-and-back sheet")], height=hL, thin=4)
    rep2 = dict(r); rep2["z_tip"] = zt; sc.zlim = (0.0, 2.75)
    return finish(sc, U, surf, rep2, R, b["hilltop"], "L_(I|O) tip z = %.3f" % zt)


def scene_dyn(models):
    SM = models["SM"]; b = models["MV_b"]; r = models["MV_r"]; u = np.array([0.25, 0.0]); U0 = r["units"]; R = U0["R"]
    sc, U, surf = build_scene(SM, b, r, "Original L_dynamic — the hat drifts (u = 0.25): the same bundle in the lab frame, sheared",
        "L_dynamic = L_standard + ∫ J_red·d(J_blue)/dt (wiki 51).  Paths from the hat's brim at t = 0, kept by closest approach to the MOVING hilltop; W is not conserved.",
        [(GOLD, "the brim at t = 0; faint: the brim as the hat drifts"), (WHITE, "the hilltop at t = 0"), ("#5ce1e6", "lowest sheet (%d paths): closest approach to the moving hilltop, in the hat frame: W = %.4f ± %.4f" % (r["n"], r["W_tip"], r["W_spread"])),
         ("#8b3fa8", "other sheets (%d): paths that bounce off the moving wall first" % (len(r["sheets"]) - 1)), ("#fff4b8", "tip in the hat frame: %.4f R from the hilltop; height gap %+.3f; lab-frame tips are spread along x by u·Δt" % (r["offset"], r["gap"]))], thin=3)
    ts = np.array([p["closest"]["t"] for k, p in enumerate(b["paths"]) if r["sheet_of"][k] == 0]); sc.xlim = (-R1.R_EXT, R1.R_EXT + 0.25*float(ts.max()) + 0.3)
    for tt in (0.5, 1.0):
        cx = 0.25*float(ts.max())*tt; sc.line(R1.ring(1.0, lambda x, y: surf(x, y), cx=cx), GOLD, width=1.6, opacity=0.4 if tt < 1 else 0.3, halo=False)
    sc.zlim = (0.0, 3.0)
    for ln in sc.lines:                                                                 # paths of the upper sheets run away with the moving wall: clip to the drawn box
        if not isinstance(ln["c"], list):
            P = ln["p"].copy(); bad = (P[:, 2] > 3.0) | (P[:, 0] > sc.xlim[1]) | (P[:, 0] < sc.xlim[0]) | (np.abs(P[:, 1]) > 2.0); P[bad] = np.nan; ln["p"] = P
    sc.legend.append(("#8b3fa8", "upper sheets are clipped to the drawn box: they run off with the moving wall"))
    return finish(sc, U, surf, r, R, b["hilltop"], "tip (hat frame): %+.3f" % r["gap"])


def main():
    os.makedirs(OUT, exist_ok=True)
    SM = W.lagrangian_sm(mu2=1.0, lam=1.0); NN = W.lagrangian_vap(mu_sq=-1.0, lam=0.5, g=0.2, psi=(1.0, 0.0), convention="ssb"); kw = dict(n_sources=24, n_dirs=1441, T=6.0, n_steps=1500, eps=0.15)
    models = {"SM": SM, "NN": NN}
    for key, mod, extra in (("SM", SM, {}), ("NN", NN, {}), ("MV", SM, {"u": (0.25, 0.0)})):
        b = AC.brim_bundle(mod, **kw, **extra); r = AC.tip_report(mod, b); models[key + "_b"], models[key + "_r"] = b, r
        print("%s: %d of %d paths selected; tip %.4f R from the hilltop; W_tip %.4f; z_tip %.4f; gap %+.4f; sheets %s" % (key, b["n_selected"], b["n_total"], r["offset"], r["W_tip"], r["z_tip"], r["gap"], [(round(s["W"], 3), s["n"]) for s in r["sheets"][:5]]), flush=True)
    made = []
    only = os.environ.get("ONLY")                                                       # e.g. ONLY=L_dynamic_original,tip_and_time re-renders just those
    for name, fn in (("L_SM", scene_sm), ("L_NN", scene_nn), ("L_IO", scene_lio), ("L_dynamic_original", scene_dyn)):
        if only and name not in only.split(","): continue
        made.append(R1.write_svg(fn(models), "WitchesHat_Lagrangians_%s_%s.svg" % (VERSION, name))); print("wrote", os.path.basename(made[-1]), "%.0f KB" % (os.path.getsize(made[-1])/1024), flush=True)
    import tip_and_time
    if not only or "tip_and_time" in only.split(","): made.append(tip_and_time.make(OUT, VERSION, models)); print("wrote", os.path.basename(made[-1]), flush=True)
    html = ['<!doctype html><meta charset="utf-8"><title>WitchesHat Lagrangians %s</title><body style="background:#0b1220;color:#e6edf3;font-family:Helvetica,Arial,sans-serif;margin:24px"><h1>The Lagrangians on the Mexican hat, %s</h1>' % (VERSION, VERSION),
            "<p>What the maths says, drawn exactly: the bundle of paths from every point of the brim in every direction, kept by what each path does. Brim gold, hilltop white, tip pale yellow.</p>"]
    made = sorted(os.path.join(OUT, f) for f in os.listdir(OUT) if f.endswith(".svg"))
    for p in made: html.append('<h2>%s</h2><img src="%s" style="max-width:100%%">' % (os.path.basename(p)[:-4], os.path.basename(p)))
    open(os.path.join(OUT, "index.html"), "w").write("\n".join(html)); print("wrote index.html")


if __name__ == "__main__":
    main()
