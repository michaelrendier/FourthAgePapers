"""
Ask the boundary.

The boundary at ℓ* is not the edge of the data.
It is the answer. Read it directly.
"""

import numpy as np
from scipy.signal import savgol_filter
from scipy.stats import linregress
import os

DATA    = "/media/rendier/0123-4567/Ainulindale/Experiments/FractalBoundary/data"
RESULTS = "/media/rendier/0123-4567/Ainulindale/Experiments/FractalBoundary/results"

def load_spectrum(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                try:
                    rows.append([float(p) for p in parts[:4]])
                except ValueError:
                    continue
    a = np.array(rows)
    ell = a[:, 0]
    Dl  = a[:, 1]
    Cl  = Dl * 2 * np.pi / (ell * (ell + 1))
    return ell, Cl, Dl

def ask(ell, Cl, name, ell_star):
    """Ask the boundary at ell_star what it encodes."""
    idx = np.argmin(np.abs(ell - ell_star))

    # window around boundary: ±5% of ell_star
    w = max(int(0.05 * ell_star), 20)
    lo = max(0, idx - w)
    hi = min(len(ell)-1, idx + w)
    ell_w = ell[lo:hi]
    Cl_w  = Cl[lo:hi]

    # local spectral index at boundary
    log_ell = np.log(ell_w)
    log_Cl  = np.log(np.abs(Cl_w))
    slope, intercept, r, *_ = linregress(log_ell, log_Cl)

    # angular scale
    theta_deg     = 180.0 / ell_star
    theta_arcmin  = theta_deg * 60

    # boundary value
    Cl_star = Cl[idx]
    Dl_star = Cl_star * ell_star * (ell_star + 1) / (2 * np.pi)

    # self-similarity ratio: C(ell_star) / C(ell_star/2)
    idx_half = np.argmin(np.abs(ell - ell_star/2))
    Cl_half  = Cl[idx_half]
    ratio    = Cl_star / Cl_half if Cl_half != 0 else np.nan

    # what ratio would pure fractal Df give?
    Df_implied = -slope / 2 - 0.5
    ratio_fractal = (ell_star / (ell_star/2))**slope  # = 2^slope

    # encode: does C_ℓ* / C_ℓ*/2 match any known constant?
    PHI     = (1 + np.sqrt(5)) / 2
    sigma_h = 0.5
    d_star  = 0.2460    # canonical d*
    pi      = np.pi

    candidates = {
        "2^slope"     : ratio_fractal,
        "1/φ"         : 1/PHI,
        "1/π"         : 1/pi,
        "σ½"          : sigma_h,
        "d*"          : d_star,
        "φ−1"         : PHI - 1,
        "1/e"         : 1/np.e,
        "1/2"         : 0.5,
    }
    best_name, best_val, best_err = min(
        ((k, v, abs(ratio - v)) for k, v in candidates.items()),
        key=lambda x: x[2]
    )

    print(f"\n{'='*56}")
    print(f"BOUNDARY INTERROGATION — {name}")
    print(f"{'='*56}")
    print(f"  ℓ*             = {ell_star}")
    print(f"  θ*             = {theta_arcmin:.4f} arcmin  ({theta_deg:.5f}°)")
    print(f"  C_ℓ*           = {Cl_star:.6e}  μK²")
    print(f"  D_ℓ*           = {Dl_star:.6f}  μK²")
    print(f"  local n(ℓ*)    = {slope:.6f}   (r={r:.5f})")
    print(f"  D_f implied    = {Df_implied:.6f}")
    print(f"  C(ℓ*)/C(ℓ*/2) = {ratio:.6f}")
    print(f"  closest const  = {best_name} = {best_val:.6f}  (err={best_err:.2e})")
    print()

    return {
        "name"         : name,
        "ell_star"     : ell_star,
        "theta_arcmin" : theta_arcmin,
        "Cl_star"      : Cl_star,
        "Dl_star"      : Dl_star,
        "local_n"      : slope,
        "r"            : r,
        "Df_implied"   : Df_implied,
        "self_sim_ratio": ratio,
        "closest"      : best_name,
        "closest_val"  : best_val,
        "closest_err"  : best_err,
    }

def cross_examine(r_planck, r_wmap):
    """What does the gap between the two boundaries encode?"""
    ell_p  = r_planck["ell_star"]
    ell_w  = r_wmap["ell_star"]
    delta  = ell_p - ell_w
    ratio  = ell_p / ell_w

    Cl_p   = r_planck["Cl_star"]
    Cl_w   = r_wmap["Cl_star"]
    Cl_ratio = Cl_w / Cl_p   # WMAP / Planck at their respective ℓ*

    PHI    = (1 + np.sqrt(5)) / 2
    d_star = 0.2460

    print(f"\n{'='*56}")
    print(f"CROSS-EXAMINATION — gap between boundaries")
    print(f"{'='*56}")
    print(f"  Δℓ*            = {delta}  (Planck − WMAP)")
    print(f"  ℓ_P / ℓ_W      = {ratio:.6f}")
    print(f"  vs φ           = {PHI:.6f}  (err={abs(ratio-PHI):.4f})")
    print(f"  vs 2           = 2.000000  (err={abs(ratio-2):.4f})")
    print(f"  C_W(ℓ*)/C_P(ℓ*)= {Cl_ratio:.6f}")
    print(f"  n_P(ℓ*)        = {r_planck['local_n']:.4f}")
    print(f"  n_W(ℓ*)        = {r_wmap['local_n']:.4f}")
    print(f"  Δn             = {r_planck['local_n'] - r_wmap['local_n']:.4f}")
    print()

    return {
        "delta_ell"   : delta,
        "ell_ratio"   : ratio,
        "Cl_ratio"    : Cl_ratio,
        "delta_n"     : r_planck["local_n"] - r_wmap["local_n"],
    }

def emit_svg(path, r_p, r_w, cross):
    lines = [
        '<?xml version="1.0"?>',
        '<svg xmlns="http://www.w3.org/2000/svg">',
        '  <boundary_interrogation>',
        '    <question>what_are_you</question>',
        f'    <noether_current>',
        *[f'      <{k} value="{v}"/>' for k,v in r_p.items()],
        '    </noether_current>',
        f'    <noether_information_current>',
        *[f'      <{k} value="{v}"/>' for k,v in r_w.items()],
        '    </noether_information_current>',
        '    <gap>',
        *[f'      <{k} value="{v}"/>' for k,v in cross.items()],
        '    </gap>',
        '  </boundary_interrogation>',
        '</svg>',
    ]
    with open(path, 'w') as f:
        f.write('\n'.join(lines))

def run():
    ell_p, Cl_p, Dl_p = load_spectrum(os.path.join(DATA, "planck_tt_2018.txt"))
    ell_w, Cl_w, Dl_w = load_spectrum(os.path.join(DATA, "wmap_tt_9yr.txt"))

    r_p = ask(ell_p, Cl_p, "Planck_2018 / Noether_Current",          ell_star=2450)
    r_w = ask(ell_w, Cl_w, "WMAP_9yr / Noether_Information_Current",  ell_star=1179)
    cross = cross_examine(r_p, r_w)

    emit_svg(os.path.join(RESULTS, "boundary_answer.svg"), r_p, r_w, cross)
    print(f"→ {RESULTS}/boundary_answer.svg")

if __name__ == "__main__":
    run()
