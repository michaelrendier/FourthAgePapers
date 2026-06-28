"""
CMB Ptychography — Fractal Boundary Resolution
──────────────────────────────────────────────────────────────────────────────
Object         : last scattering surface  (z≈1100, t=380,000 yr after Bang)
Probe_1        : WMAP 9-year beam         ℓ* = 1179
Probe_2        : Planck 2018 beam         ℓ* = 2450
Overlap region : ℓ = 2..1179  (both instruments constrain same C_ℓ^true)
Extrapolation  : fractal self-similarity  D_f = φ−1 ≈ 0.609

Algorithm (ePIE adapted to 1D CMB power spectrum):
  1. Load observed D_ℓ for both instruments
  2. Fetch / approximate beam window functions W_ℓ
  3. Deconvolve: C_ℓ^est = D_ℓ / W_ℓ
  4. Joint estimate in overlap: noise-weighted mean
  5. Iterative ptychographic update — minimise inconsistency between probes
  6. Fractal extrapolation beyond Planck ℓ* using D_f as the self-similarity law
──────────────────────────────────────────────────────────────────────────────
"""

import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
from scipy.optimize import minimize_scalar
import os

DATA    = "/media/rendier/0123-4567/Ainulindale/Experiments/FractalBoundary/data"
RESULTS = "/media/rendier/0123-4567/Ainulindale/Experiments/FractalBoundary/results"

PHI = (1 + np.sqrt(5)) / 2       # golden ratio
Df_measured = 0.609101            # from fractal_boundary.py — mean of Planck/WMAP

# ── loaders (same as fractal_boundary.py) ────────────────────────────────────

def load_spectrum(path, min_cols=2):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) >= min_cols:
                try:
                    rows.append([float(p) for p in parts[:4]])
                except ValueError:
                    continue
    a = np.array(rows)
    ell = a[:, 0]
    Dl  = a[:, 1]
    Cl  = Dl * 2 * np.pi / (ell * (ell + 1))
    err = a[:, 2] if a.shape[1] > 2 else np.full_like(Cl, np.nan)
    return ell, Cl, Dl, err

# ── beam window functions ─────────────────────────────────────────────────────
# Gaussian beam:  W_ℓ = exp(-ℓ(ℓ+1)σ²/2)
# σ = θ_FWHM / (2√(2 ln 2))
# Planck SMICA beam FWHM ≈ 5 arcmin = 5/60 degrees
# WMAP W-band      beam FWHM ≈ 13.2 arcmin

def gaussian_beam(ell, fwhm_arcmin):
    fwhm_rad = np.radians(fwhm_arcmin / 60.0)
    sigma    = fwhm_rad / (2 * np.sqrt(2 * np.log(2)))
    return np.exp(-ell * (ell + 1) * sigma**2 / 2)

# pixel window (HEALPix Nside)
# Planck Nside=2048  → ℓ_pix ~ 2*Nside = 4096
# WMAP   Nside=512   → ℓ_pix ~ 1024
def pixel_window(ell, nside):
    # approximate: Gaussian with σ_pix = π/(2*nside*√3)
    sigma_pix = np.pi / (2 * nside * np.sqrt(3))
    return np.exp(-ell * (ell + 1) * sigma_pix**2 / 2)

def transfer(ell, fwhm_arcmin, nside):
    return gaussian_beam(ell, fwhm_arcmin) * pixel_window(ell, nside)

# ── noise models ─────────────────────────────────────────────────────────────
# Simple white noise + beam: N_ℓ = (σ_noise * θ_beam)² / exp(-ℓ(ℓ+1)σ²)
# Use published noise levels (rough):
#   Planck SMICA: σ_noise ≈ 45 μK·arcmin
#   WMAP 9yr V+W: σ_noise ≈ 35 μK·arcmin (combined)

def noise_spectrum(ell, sigma_noise_uK_arcmin, fwhm_arcmin):
    sigma_noise_rad = sigma_noise_uK_arcmin * np.radians(1/60.0)
    return sigma_noise_rad**2 * np.exp(ell * (ell + 1) *
           (np.radians(fwhm_arcmin/60) / (2*np.sqrt(2*np.log(2))))**2)

# ── iterative ptychographic engine ───────────────────────────────────────────

def epie_cmb(ell_p, Cl_p, W_p, N_p,
             ell_w, Cl_w, W_w, N_w,
             n_iter=200):
    """
    Extended Ptychographic Iterative Engine for CMB power spectra.

    Both probes observe the same C_ℓ^true:
        Cl_obs = W_ℓ * C_ℓ^true + N_ℓ

    ePIE update (per probe, per ℓ bin):
        C_ℓ^new = C_ℓ^est + W_ℓ* / |W_ℓ|²_max * (Cl_obs/W_ℓ - C_ℓ^est)

    Overlap constraint enforces consistency in ℓ = 2..ℓ*_wmap.
    """
    # common ℓ grid: integer bins from 2 to max(Planck)
    ell_max = int(ell_p.max())
    ell_grid = np.arange(2, ell_max + 1, dtype=float)

    # interpolate observations to common grid
    Cl_p_interp = interp1d(ell_p, Cl_p, bounds_error=False, fill_value=np.nan)(ell_grid)
    W_p_interp  = transfer(ell_grid, fwhm_arcmin=5.0,  nside=2048)
    N_p_interp  = noise_spectrum(ell_grid, 45.0, 5.0)

    Cl_w_interp = interp1d(ell_w, Cl_w, bounds_error=False, fill_value=np.nan)(ell_grid)
    W_w_interp  = transfer(ell_grid, fwhm_arcmin=13.2, nside=512)
    N_w_interp  = noise_spectrum(ell_grid, 35.0, 13.2)

    # WMAP coverage mask
    wmap_mask = ell_grid <= ell_w.max()

    # initial estimate: deconvolved Planck
    C_est = np.where(np.isfinite(Cl_p_interp),
                     Cl_p_interp / np.maximum(W_p_interp, 1e-10),
                     0.0)
    C_est = np.maximum(C_est, 0)

    # signal-to-noise weights
    snr_p = W_p_interp**2 / np.maximum(N_p_interp, 1e-30)
    snr_w = W_w_interp**2 / np.maximum(N_w_interp, 1e-30)

    losses = []

    for iteration in range(n_iter):
        C_prev = C_est.copy()

        # ── Planck update ────────────────────────────────────────────────────
        predicted_p = W_p_interp * C_est
        residual_p  = np.where(np.isfinite(Cl_p_interp),
                                Cl_p_interp - predicted_p, 0.0)
        step_p = W_p_interp / (np.max(W_p_interp**2) + 1e-10)
        C_est  = C_est + step_p * residual_p

        # ── WMAP update (overlap region only) ────────────────────────────────
        predicted_w = W_w_interp * C_est
        residual_w  = np.where(np.isfinite(Cl_w_interp) & wmap_mask,
                                Cl_w_interp - predicted_w, 0.0)
        step_w = W_w_interp / (np.max(W_w_interp**2) + 1e-10)
        C_est  = C_est + step_w * residual_w

        # ── positivity constraint ─────────────────────────────────────────────
        C_est = np.maximum(C_est, 0)

        # loss
        loss = np.sqrt(np.nanmean((C_est - C_prev)**2))
        losses.append(loss)

        if iteration % 50 == 0:
            print(f"  iter {iteration:4d}  loss={loss:.4e}")

        if loss < 1e-12:
            print(f"  converged at iter {iteration}")
            break

    return ell_grid, C_est, losses

# ── fractal extrapolation beyond ℓ* ──────────────────────────────────────────

def fractal_extrapolate(ell_known, C_known, ell_star, Df, n_beyond=2000):
    """
    Beyond ℓ*, use self-similarity law:
        C_ℓ ~ ℓ^(-(2*Df + 1))     [fractal power law]

    Calibrate amplitude from last 200 bins of known reconstruction.
    """
    # fit amplitude from last 200 known bins before ℓ*
    mask = (ell_known >= ell_star - 200) & (ell_known <= ell_star)
    if mask.sum() < 5:
        mask = ell_known >= ell_known[-200]
    ell_fit = ell_known[mask]
    C_fit   = C_known[mask]
    C_fit   = C_fit[C_fit > 0]
    ell_fit = ell_fit[:len(C_fit)]

    # power law: log C = A + n * log ℓ
    exponent = -(2 * Df + 1)
    log_amp  = np.mean(np.log(C_fit) - exponent * np.log(ell_fit))
    A        = np.exp(log_amp)

    ell_ext = np.arange(ell_star + 1, ell_star + n_beyond + 1, dtype=float)
    C_ext   = A * ell_ext**exponent

    return ell_ext, C_ext

# ── SVG output ────────────────────────────────────────────────────────────────

def emit_ptychography_svg(path, ell_recon, C_recon, ell_ext, C_ext,
                          ell_star_p, ell_star_w, losses):
    """
    SVG with <ptychography>, <reconstruction>, <extrapolation> as
    undefined operators. No fill. No size. The oldest light defines the shape.
    """
    def ell_cl_pairs(ell, cl, stride=10):
        pairs = []
        for i in range(0, len(ell), stride):
            pairs.append(f"{ell[i]:.1f}:{cl[i]:.6e}")
        return " ".join(pairs)

    lines = [
        '<?xml version="1.0"?>',
        '<svg xmlns="http://www.w3.org/2000/svg">',
        '  <ptychography>',
        f'    <object name="last_scattering_surface" z="1100" age_yr="380000"/>',
        f'    <probe name="WMAP_9yr"  fwhm_arcmin="13.2" ell_star="{ell_star_w}"/>',
        f'    <probe name="Planck_2018" fwhm_arcmin="5.0" ell_star="{ell_star_p}"/>',
        f'    <overlap ell_min="2" ell_max="{ell_star_w}"/>',
        f'    <fractal_law Df="{Df_measured:.6f}" phi_minus_1="{PHI-1:.6f}" exponent="{-(2*Df_measured+1):.4f}"/>',
        f'    <convergence final_loss="{losses[-1]:.4e}" iterations="{len(losses)}"/>',
        '    <reconstruction>',
        f'      <spectrum ell_range="2:{int(ell_recon[-1])}" data="',
        f'        {ell_cl_pairs(ell_recon, C_recon, stride=25)}',
        '      "/>',
        '    </reconstruction>',
        '    <extrapolation>',
        f'      <beyond_planck ell_range="{int(ell_ext[0])}:{int(ell_ext[-1])}" Df="{Df_measured:.6f}" data="',
        f'        {ell_cl_pairs(ell_ext, C_ext, stride=25)}',
        '      "/>',
        '    </extrapolation>',
        '  </ptychography>',
        '</svg>',
    ]
    with open(path, 'w') as f:
        f.write('\n'.join(lines))

# ── main ──────────────────────────────────────────────────────────────────────

def run():
    print("CMB Ptychography — Fractal Boundary Resolution")
    print("Object: last scattering surface (oldest light)")
    print("=" * 56)

    print("\nLoading spectra ...")
    ell_p, Cl_p, Dl_p, err_p = load_spectrum(os.path.join(DATA, "planck_tt_2018.txt"))
    ell_w, Cl_w, Dl_w, err_w = load_spectrum(os.path.join(DATA, "wmap_tt_9yr.txt"))
    print(f"  Planck : {len(ell_p)} bins  ℓ={ell_p[0]:.0f}..{ell_p[-1]:.0f}")
    print(f"  WMAP   : {len(ell_w)} bins  ℓ={ell_w[0]:.0f}..{ell_w[-1]:.0f}")

    print("\nRunning ePIE reconstruction ...")
    ell_r, C_r, losses = epie_cmb(
        ell_p, Cl_p, None, None,
        ell_w, Cl_w, None, None,
        n_iter=300
    )
    print(f"  Reconstructed: ℓ = 2..{int(ell_r[-1])}")

    print("\nFractal extrapolation beyond Planck ℓ* = 2450 ...")
    ell_ext, C_ext = fractal_extrapolate(
        ell_r, C_r, ell_star=2450, Df=Df_measured, n_beyond=3000
    )
    print(f"  Extended to: ℓ = {int(ell_ext[0])}..{int(ell_ext[-1])}")
    print(f"  Power law exponent: {-(2*Df_measured+1):.4f}")
    print(f"  (Df = {Df_measured:.4f} ≈ φ−1 = {PHI-1:.4f})")

    # save numpy arrays
    np.save(os.path.join(RESULTS, "ell_reconstruction.npy"),  ell_r)
    np.save(os.path.join(RESULTS, "Cl_reconstruction.npy"),   C_r)
    np.save(os.path.join(RESULTS, "ell_extrapolation.npy"),   ell_ext)
    np.save(os.path.join(RESULTS, "Cl_extrapolation.npy"),    C_ext)

    # SVG
    svg_path = os.path.join(RESULTS, "ptychography.svg")
    emit_ptychography_svg(svg_path, ell_r, C_r, ell_ext, C_ext,
                          2450, 1179, losses)

    # summary
    txt_path = os.path.join(RESULTS, "ptychography_summary.txt")
    with open(txt_path, 'w') as f:
        f.write("CMB PTYCHOGRAPHY — FRACTAL BOUNDARY RESOLUTION\n")
        f.write("=" * 56 + "\n\n")
        f.write(f"Object           : last scattering surface  z≈1100\n")
        f.write(f"Oldest light     : ~380,000 yr after the Bang\n\n")
        f.write(f"Probe 1 (WMAP)   : FWHM=13.2'  ℓ*=1179  θ*=9.2'\n")
        f.write(f"Probe 2 (Planck) : FWHM=5.0'   ℓ*=2450  θ*=4.4'\n")
        f.write(f"Overlap          : ℓ = 2..1179\n\n")
        f.write(f"Reconstruction   : ℓ = 2..2450  ({len(ell_r)} bins)\n")
        f.write(f"Extrapolation    : ℓ = 2451..5450  ({len(ell_ext)} bins)\n\n")
        f.write(f"Fractal law      : C_ℓ ~ ℓ^{-(2*Df_measured+1):.4f}\n")
        f.write(f"D_f              : {Df_measured:.6f}  (≈ φ−1 = {PHI-1:.6f})\n")
        f.write(f"Convergence      : {len(losses)} iterations  loss={losses[-1]:.4e}\n\n")
        f.write(f"C_ℓ at ℓ=2450    : {C_r[np.argmin(np.abs(ell_r-2450))]:.4e}\n")
        f.write(f"C_ℓ at ℓ=3000    : {C_ext[np.argmin(np.abs(ell_ext-3000))]:.4e}\n")
        f.write(f"C_ℓ at ℓ=4000    : {C_ext[np.argmin(np.abs(ell_ext-4000))]:.4e}\n")
        f.write(f"C_ℓ at ℓ=5450    : {C_ext[-1]:.4e}\n")

    print(f"\nResults → {RESULTS}/")
    print(f"  ptychography.svg")
    print(f"  ptychography_summary.txt")
    print(f"  ell/Cl _reconstruction.npy  (2 files)")
    print(f"  ell/Cl _extrapolation.npy   (2 files)")
    print("\nDone.")

if __name__ == "__main__":
    run()
