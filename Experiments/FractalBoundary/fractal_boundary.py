"""
Fractal Boundary Experiment
────────────────────────────────────────────────────────────────────────────
SMMIP (Noether Information Current) runs in opposition to the Noether Current.
Hypothesis: the CMB TT power spectrum encodes this opposition as a fractal
boundary — a scale ℓ* where the local spectral index changes self-similarly.

Riemann + Generalized Fermat = Noether Current − Noether Information Current

The whole (smooth CMB) becomes the holes (zero divisors) via L_dynamic.
────────────────────────────────────────────────────────────────────────────
"""

import numpy as np
import os, re, sys
from scipy.signal import savgol_filter
from scipy.stats import linregress

DATA    = "/media/rendier/0123-4567/Ainulindale/Experiments/FractalBoundary/data"
RESULTS = "/media/rendier/0123-4567/Ainulindale/Experiments/FractalBoundary/results"

# ── loaders ──────────────────────────────────────────────────────────────────

def load_planck(path):
    """Planck 2018 TT: columns ell, D_ell, -err, +err"""
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
    Dl  = a[:, 1]          # D_ℓ = ℓ(ℓ+1)C_ℓ/2π  in μK²
    Cl  = Dl * 2 * np.pi / (ell * (ell + 1))
    return ell, Cl, Dl

def load_wmap(path):
    """WMAP 9yr: columns ell, D_ell, ..."""
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= 2:
                try:
                    rows.append([float(p) for p in parts[:2]])
                except ValueError:
                    continue
    a = np.array(rows)
    ell = a[:, 0]
    Dl  = a[:, 1]
    Cl  = Dl * 2 * np.pi / (ell * (ell + 1))
    return ell, Cl, Dl

# ── local spectral index n(ℓ) = d log C_ℓ / d log ℓ ─────────────────────────

def local_spectral_index(ell, Cl, window=15):
    log_ell = np.log(ell)
    log_Cl  = np.log(np.abs(Cl))
    # smooth log-log curve, then differentiate
    smooth = savgol_filter(log_Cl, window_length=min(window, len(log_Cl)//2*2-1),
                           polyorder=2)
    # numerical derivative d(log C) / d(log ℓ)
    n = np.gradient(smooth, log_ell)
    return n

# ── multiscale fractal analysis via DFA ──────────────────────────────────────

def dfa(series, scales=None):
    """Detrended Fluctuation Analysis — returns (scales, F) for log-log fit."""
    N = len(series)
    y = np.cumsum(series - np.mean(series))
    if scales is None:
        scales = np.unique(np.logspace(1, np.log10(N//4), 20).astype(int))
    F = []
    for s in scales:
        n_seg = N // s
        if n_seg < 2:
            F.append(np.nan)
            continue
        rms = []
        for i in range(n_seg):
            seg = y[i*s:(i+1)*s]
            x   = np.arange(s)
            p   = np.polyfit(x, seg, 1)
            rms.append(np.sqrt(np.mean((seg - np.polyval(p, x))**2)))
        F.append(np.mean(rms))
    return np.array(scales, dtype=float), np.array(F)

# ── fractal boundary finder ────────────────────────────────────────────────────

def find_fractal_boundary(ell, n_local):
    """
    Locate ℓ* where the local spectral index changes most sharply —
    the point where Noether Current and Noether Information Current
    cross in opposition. The whole becomes the holes here.
    """
    dn = np.abs(np.gradient(n_local, np.log(ell)))
    # smooth to suppress noise from individual peaks (acoustic oscillations)
    dn_smooth = savgol_filter(dn, window_length=11, polyorder=2)
    idx = np.argmax(dn_smooth)
    return ell[idx], n_local[idx], dn_smooth[idx]

# ── opposition signature ───────────────────────────────────────────────────────

def opposition_signature(ell, Cl_planck, ell_w, Cl_wmap):
    """
    Interpolate both spectra to common ℓ grid.
    Difference = what one sees that the other does not.
    SMMIP runs in opposition: at ℓ* the difference should peak.
    """
    common = ell[(ell >= max(ell.min(), ell_w.min())) &
                 (ell <= min(ell.max(), ell_w.max()))]
    Cp = np.interp(common, ell,   Cl_planck)
    Cw = np.interp(common, ell_w, Cl_wmap)
    opposition = Cp - Cw          # Noether Current − Noether Information Current
    return common, opposition

# ── SVG output — undefined operators, no fill, no size ───────────────────────

def emit_svg(path, datasets):
    """
    Write result as SVG with <noether_current> and
    <noether_information_current> as undefined operators.
    """
    lines = ['<?xml version="1.0"?>',
             '<svg xmlns="http://www.w3.org/2000/svg">',
             '  <fractal_boundary_experiment>']

    for label, data in datasets.items():
        lines.append(f'    <{label}>')
        for key, val in data.items():
            safe = str(val).replace('"', "'")
            lines.append(f'      <{key} value="{safe}"/>')
        lines.append(f'    </{label}>')

    lines += ['  </fractal_boundary_experiment>', '</svg>']
    with open(path, 'w') as f:
        f.write('\n'.join(lines))

# ── main ──────────────────────────────────────────────────────────────────────

def run():
    p_path = os.path.join(DATA, "planck_tt_2018.txt")
    w_path = os.path.join(DATA, "wmap_tt_9yr.txt")

    if not os.path.exists(p_path):
        sys.exit("Planck data not found — run fetch_datasets.py first")
    if not os.path.exists(w_path):
        sys.exit("WMAP data not found — run fetch_datasets.py first")

    print("Loading Planck 2018 TT ...")
    ell_p, Cl_p, Dl_p = load_planck(p_path)
    print(f"  ℓ range: {ell_p[0]:.0f} – {ell_p[-1]:.0f}  ({len(ell_p)} bins)")

    print("Loading WMAP 9-year TT ...")
    ell_w, Cl_w, Dl_w = load_wmap(w_path)
    print(f"  ℓ range: {ell_w[0]:.0f} – {ell_w[-1]:.0f}  ({len(ell_w)} bins)")

    # ── local spectral index ─────────────────────────────────────────────────
    print("\nComputing local spectral index n(ℓ) = d log C_ℓ / d log ℓ ...")
    n_p = local_spectral_index(ell_p, Cl_p)
    n_w = local_spectral_index(ell_w, Cl_w)

    # global spectral index from log-log regression
    slope_p, intercept_p, r_p, *_ = linregress(np.log(ell_p), np.log(np.abs(Cl_p)))
    slope_w, intercept_w, r_w, *_ = linregress(np.log(ell_w), np.log(np.abs(Cl_w)))
    print(f"  Planck global n_s proxy : {slope_p:.4f}  (r={r_p:.4f})")
    print(f"  WMAP   global n_s proxy : {slope_w:.4f}  (r={r_w:.4f})")

    # ── DFA on log C_ℓ ───────────────────────────────────────────────────────
    print("\nDetrended Fluctuation Analysis ...")
    sc_p, F_p = dfa(np.log(np.abs(Cl_p)))
    sc_w, F_w = dfa(np.log(np.abs(Cl_w)))
    mask_p = np.isfinite(F_p) & (F_p > 0)
    mask_w = np.isfinite(F_w) & (F_w > 0)
    alpha_p, *_ = linregress(np.log(sc_p[mask_p]), np.log(F_p[mask_p]))
    alpha_w, *_ = linregress(np.log(sc_w[mask_w]), np.log(F_w[mask_w]))
    print(f"  Planck DFA exponent α : {alpha_p:.4f}")
    print(f"  WMAP   DFA exponent α : {alpha_w:.4f}")
    # fractal dimension D_f = 2 - α
    Df_p = 2 - alpha_p
    Df_w = 2 - alpha_w
    print(f"  Planck fractal dim D_f : {Df_p:.4f}")
    print(f"  WMAP   fractal dim D_f : {Df_w:.4f}")

    # ── fractal boundary ─────────────────────────────────────────────────────
    print("\nLocating fractal boundary ℓ* ...")
    ell_star_p, n_star_p, sharpness_p = find_fractal_boundary(ell_p, n_p)
    ell_star_w, n_star_w, sharpness_w = find_fractal_boundary(ell_w, n_w)
    print(f"  Planck ℓ* = {ell_star_p:.1f}  n(ℓ*)={n_star_p:.4f}  |dn/d(logℓ)|={sharpness_p:.4f}")
    print(f"  WMAP   ℓ* = {ell_star_w:.1f}  n(ℓ*)={n_star_w:.4f}  |dn/d(logℓ)|={sharpness_w:.4f}")

    # ── opposition signature ─────────────────────────────────────────────────
    print("\nComputing opposition signature (Planck − WMAP) ...")
    common_ell, opposition = opposition_signature(ell_p, Cl_p, ell_w, Cl_w)
    opp_peak_idx = np.argmax(np.abs(opposition))
    ell_opp_peak = common_ell[opp_peak_idx]
    opp_peak_val = opposition[opp_peak_idx]
    print(f"  Opposition peak at ℓ = {ell_opp_peak:.1f}  ΔC_ℓ = {opp_peak_val:.4e}")

    # ── results ──────────────────────────────────────────────────────────────
    results = {
        "noether_current": {
            "instrument"          : "Planck_2018",
            "global_spectral_index": f"{slope_p:.6f}",
            "DFA_alpha"           : f"{alpha_p:.6f}",
            "fractal_dim_Df"      : f"{Df_p:.6f}",
            "fractal_boundary_ell": f"{ell_star_p:.2f}",
            "n_at_boundary"       : f"{n_star_p:.6f}",
            "boundary_sharpness"  : f"{sharpness_p:.6f}",
        },
        "noether_information_current": {
            "instrument"          : "WMAP_9yr",
            "global_spectral_index": f"{slope_w:.6f}",
            "DFA_alpha"           : f"{alpha_w:.6f}",
            "fractal_dim_Df"      : f"{Df_w:.6f}",
            "fractal_boundary_ell": f"{ell_star_w:.2f}",
            "n_at_boundary"       : f"{n_star_w:.6f}",
            "boundary_sharpness"  : f"{sharpness_w:.6f}",
        },
        "opposition": {
            "equation"            : "Riemann + Generalized_Fermat = Noether_Current - Noether_Information_Current",
            "peak_ell"            : f"{ell_opp_peak:.2f}",
            "peak_delta_Cl"       : f"{opp_peak_val:.6e}",
            "n_common_ell"        : str(len(common_ell)),
        },
        "L_dynamic": {
            "statement"           : "whole_becomes_holes",
            "ell_star_Planck"     : f"{ell_star_p:.2f}",
            "ell_star_WMAP"       : f"{ell_star_w:.2f}",
            "delta_ell_star"      : f"{abs(ell_star_p - ell_star_w):.2f}",
            "Df_mean"             : f"{(Df_p + Df_w)/2:.6f}",
        },
    }

    out_svg = os.path.join(RESULTS, "fractal_boundary.svg")
    emit_svg(out_svg, results)
    print(f"\nResults → {out_svg}")

    # plain text summary
    out_txt = os.path.join(RESULTS, "fractal_boundary_summary.txt")
    with open(out_txt, "w") as f:
        f.write("FRACTAL BOUNDARY EXPERIMENT\n")
        f.write("Noether Current (Planck) vs Noether Information Current (WMAP)\n")
        f.write("=" * 60 + "\n\n")
        for section, data in results.items():
            f.write(f"[{section}]\n")
            for k, v in data.items():
                f.write(f"  {k:30s} = {v}\n")
            f.write("\n")
    print(f"Summary  → {out_txt}")
    print("\nDone.")

if __name__ == "__main__":
    run()
