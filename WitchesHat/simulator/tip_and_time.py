"""Companion figure of render_lagrangians_v2.py: the tip numbers and the time pathway.
    (1) the height of the tip above the hilltop against energy (exact radial cone) and the bundle's value;  (2) the sheets of the action at the tip, SM against the tilted L_NN;
    (3) worldlines (r, t): the paths of the lowest sheet as a spacetime diagram, time vertical;  (4) the tip's offset from the hilltop and its height against the coupling g."""
import math
import os

import numpy as np

from ValaQuenta.modules.witches_hat import action as AC
from ValaQuenta.modules.witches_hat import maths as W

BG, PANEL, FG, MUTED, GOLD = "#0b1220", "#0f1a2e", "#e6edf3", "#8b98a9", "#f2cc60"


def make(OUT, VERSION, models):
    import matplotlib
    matplotlib.use("svg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"svg.fonttype": "none", "font.family": "DejaVu Sans"})
    SM = models["SM"]; b = models["SM_b"]; r = models["SM_r"]; rn = models["NN_r"]
    fig, ax = plt.subplots(2, 2, figsize=(15, 11.5), facecolor=BG)
    for a in ax.ravel():
        a.set_facecolor(PANEL); [s.set_color("#1f2c44") for s in a.spines.values()]; a.tick_params(colors=MUTED); a.xaxis.label.set_color(FG); a.yaxis.label.set_color(FG); a.title.set_color(FG)
    # 1 tip height against energy
    a = ax[0, 0]; Es = np.linspace(0, 0.3, 60); gaps = [AC.cone_tip_height(SM, E)["gap"] for E in Es]
    a.plot(Es, gaps, color="#5ce1e6", lw=2.6, label="exact radial cone: tip above the hilltop"); a.scatter([0.0], [r["gap"]], color="#fff4b8", s=90, zorder=5, label="bundle (every source, every direction): %.4f" % r["gap"])
    a.axhline(0, color=MUTED, lw=0.6); a.set_xlabel("energy E (units of μ = λ = 1; hilltop at E = 0, depth 0.25)"); a.set_ylabel("tip height above the hilltop, units of the depth")
    a.set_title("How far the tip stands above the hilltop: 0.219 depth at E = 0, rising with E", fontsize=12); a.legend(facecolor=PANEL, edgecolor="#1f2c44", labelcolor=FG, fontsize=9)
    a.annotate("at E = 0 the tip is smooth (momentum 0);\nfor E > 0 it is a point with slope √(2E)", (0.12, 0.4), color=MUTED, fontsize=9)
    # 2 sheets
    a = ax[0, 1]; Ws = [s["W"] for s in r["sheets"]]; Wn = [s["W"] for s in rn["sheets"]]; Wd = 0.43096; Ww = 0.23572
    for n in range(5): a.axhline(Wd + 2*n*Ww, color="#8b98a9", lw=0.8, ls=":")
    a.scatter([0]*len(Ws), Ws, s=[40 + s["n"]/3 for s in r["sheets"]], color="#5ce1e6", label="L_SM: %d sheets (0.431 and 0.902)" % len(Ws)); a.scatter([1]*len(Wn), Wn, s=[40 + s["n"]/3 for s in rn["sheets"]], color="#ff7b72", label="L_NN g = 0.2: %d sheets" % len(Wn))
    a.set_xticks([0, 1]); a.set_xticklabels(["L_SM", "L_NN, g = 0.2"]); a.set_ylabel("reduced action W at the tip"); a.set_xlim(-0.6, 1.6)
    a.set_title("The action at the tip is multivalued: sheets (dotted: 0.431 + n × 0.4714)", fontsize=12); a.legend(facecolor=PANEL, edgecolor="#1f2c44", labelcolor=FG, fontsize=9)
    # 3 worldlines
    a = ax[1, 0]; low = [p for k, p in enumerate(b["paths"]) if r["sheet_of"][k] == 0]
    for p in low[::6]:
        rr = np.hypot(p["q"][:, 0], p["q"][:, 1]); a.plot(rr, p["t"][:len(rr)], color="#5ce1e6", lw=0.9, alpha=0.7)
    hi = [p for k, p in enumerate(b["paths"]) if r["sheet_of"][k] == 1]
    for p in hi[::6]:
        rr = np.hypot(p["q"][:, 0], p["q"][:, 1]); a.plot(rr, p["t"][:len(rr)], color="#8b3fa8", lw=0.9, alpha=0.6)
    a.axvline(1, color=GOLD, lw=1.6, ls="--"); a.axvline(0, color="white", lw=1.0); a.set_xlabel("distance from the hilltop r / R   (gold: the brim; white: the hilltop)"); a.set_ylabel("time t (units 1/μ)")
    a.set_title("Worldlines (r, t), time vertical: the E = 0 tip is approached, never passed", fontsize=11)
    # 4 tilt
    a = ax[1, 1]; gs = (0.0, 0.05, 0.1, 0.2, 0.4); off, gap, spread = [], [], []
    for g in gs:
        m = W.lagrangian_vap(mu_sq=-1.0, lam=0.5, g=g, psi=(1.0, 0.0), convention="ssb"); bb = AC.brim_bundle(m, n_sources=12, n_dirs=721, T=6.0, n_steps=1200, eps=0.15); rr_ = AC.tip_report(m, bb)
        off.append(rr_["offset"]); gap.append(rr_["gap"]); spread.append(rr_["z_tip_spread"]); print("  g=%.2f tip offset %.4f R gap %+.4f spread %.4f" % (g, rr_["offset"], rr_["gap"], rr_["z_tip_spread"]), flush=True)
    a.plot(gs, off, "o-", color="#ff7b72", lw=2.2, label="tip distance from the tilted hilltop (brim radii)"); a.plot(gs, gap, "s-", color="#fff4b8", lw=2.2, label="tip height above the hilltop (depth)"); a.plot(gs, spread, "^-", color="#8b3fa8", lw=2.2, label="height spread across the sources (a level brim gives 0)")
    a.set_xlabel("coupling g (hilltop shift 0.07 R at g = 0.1, 0.14 R at 0.2, 0.31 R at 0.4)"); a.set_title("L_NN: the tip against the tilt of the hat", fontsize=12); a.legend(facecolor=PANEL, edgecolor="#1f2c44", labelcolor=FG, fontsize=9)
    fig.suptitle("WitchesHat Lagrangians %s: the tip, its sheets, and the time pathway" % VERSION, color=FG, fontsize=17, fontweight="bold", y=0.995); fig.tight_layout(rect=(0, 0, 1, 0.97))
    path = os.path.join(OUT, "WitchesHat_Lagrangians_%s_tip_and_time.svg" % VERSION); fig.savefig(path, facecolor=BG); plt.close(fig); return path
