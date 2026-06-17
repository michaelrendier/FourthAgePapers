#!/usr/bin/env python3
"""
CMB Fractal Flames — boundary D_f from real Planck/WMAP sky maps.

P7 (new): D_f of the 2D CMB temperature boundary = φ = 1.6180...
P8 (new): Boundary is self-similar at all angular scales (ptychographic invariance).
Physical interpretation: fractal plasma flame at last scattering surface, z≈1100.

Part 3 (deferred): compare against H_hat_RB theoretical boundary.
"""

import numpy as np
import healpy as hp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import LinearSegmentedColormap
from scipy import ndimage
from scipy.optimize import curve_fit
import os, json

PHI   = (1 + np.sqrt(5)) / 2   # 1.6180339887...
PHI_1 = PHI - 1                 # 0.6180339887...
OUT   = "/media/rendier/0123-4567/Ainulindale/AddPapers/CMB_FractalBoundary/results"
os.makedirs(OUT, exist_ok=True)

# ── Flame colormap ────────────────────────────────────────────────────────────
_flame_colors = ['#0a0010','#1a0050','#6600aa','#cc0033','#ff4400',
                 '#ff9900','#ffee00','#ffffff']
FLAME_CMAP = LinearSegmentedColormap.from_list('plasma_flame', _flame_colors, N=512)

# ── Box-counting fractal dimension ────────────────────────────────────────────
def box_count_df(boundary_2d, min_box=2, max_box=None):
    """
    boundary_2d: 2D boolean array — True where boundary pixel.
    Returns (scales, counts, D_f, D_f_err).
    """
    N = boundary_2d.shape[0]
    if max_box is None:
        max_box = N // 4
    sizes = np.unique(np.logspace(np.log10(min_box), np.log10(max_box),
                                  num=20, dtype=int))
    sizes = sizes[sizes >= min_box]
    counts = []
    for s in sizes:
        # Coarsen grid: any box containing a boundary pixel counts
        coarse = boundary_2d[:N - N % s, :N - N % s]
        tiles = coarse.reshape(N // s, s, N // s, s)
        n = tiles.any(axis=(1, 3)).sum()
        counts.append(n)
    counts = np.array(counts, dtype=float)
    valid = counts > 0
    if valid.sum() < 3:
        return sizes, counts, np.nan, np.nan
    log_s = np.log(1.0 / sizes[valid])
    log_n = np.log(counts[valid])
    # Linear fit: log N = D_f * log(1/s) + const
    coeffs, cov = np.polyfit(log_s, log_n, 1, cov=True)
    D_f = coeffs[0]
    D_f_err = np.sqrt(cov[0, 0])
    return sizes, counts, D_f, D_f_err

# ── Gnomonic projection of a sky patch ───────────────────────────────────────
def gnomonic_patch(T_map, nside, lon_c, lat_c, fov_deg, npix_img=512):
    """
    Extract a gnomonic (tangent-plane) patch centred at (lon_c, lat_c) degrees.
    fov_deg: full field of view in degrees.
    Returns 2D temperature array (npix_img × npix_img).
    """
    fov_rad = np.radians(fov_deg)
    # Grid of angular offsets
    dx = np.linspace(-fov_rad/2, fov_rad/2, npix_img)
    dy = np.linspace(-fov_rad/2, fov_rad/2, npix_img)
    DX, DY = np.meshgrid(dx, dy)
    # Convert to (theta, phi) on sphere
    lon0, lat0 = np.radians(lon_c), np.radians(lat_c)
    rho = np.sqrt(DX**2 + DY**2)
    c   = np.arctan(rho)
    with np.errstate(invalid='ignore', divide='ignore'):
        lat = np.arcsin(np.cos(c)*np.sin(lat0)
                        + np.where(rho==0, 0, DY*np.sin(c)*np.cos(lat0)/rho))
        lon = lon0 + np.arctan2(DX*np.sin(c),
                                 rho*np.cos(lat0)*np.cos(c)
                                 - DY*np.sin(lat0)*np.sin(c))
    theta = np.pi/2 - lat          # healpy colatitude
    phi   = lon % (2*np.pi)
    pix   = hp.ang2pix(nside, theta.ravel(), phi.ravel())
    img   = T_map[pix].reshape(npix_img, npix_img)
    return img

# ── Boundary extraction ───────────────────────────────────────────────────────
def temperature_boundary(img):
    """
    Find zero-crossing boundary pixels in a 2D temperature patch.
    A pixel is boundary if it or its 4-neighbours crosses ΔT=0.
    Returns boolean mask.
    """
    pos = img > 0
    # Erosion of positive region — XOR gives boundary
    eroded = ndimage.binary_erosion(pos, structure=np.ones((3,3)))
    boundary = pos ^ eroded
    # Also dilated negative side
    dilated = ndimage.binary_dilation(pos, structure=np.ones((3,3)))
    boundary |= (dilated ^ pos)
    return boundary

# ── Galactic mask ─────────────────────────────────────────────────────────────
def galactic_mask(nside, lat_cut_deg=20):
    """Mask galactic plane |b| < lat_cut_deg."""
    npix = hp.nside2npix(nside)
    theta, _ = hp.pix2ang(nside, np.arange(npix))
    lat = np.pi/2 - theta
    mask = np.abs(np.degrees(lat)) > lat_cut_deg
    return mask

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("CMB FRACTAL FLAMES — BOUNDARY ANALYSIS")
print(f"φ = {PHI:.6f}   φ−1 = {PHI_1:.6f}")
print("P7: D_f(2D boundary) = φ = 1.6180...")
print("P8: Self-similar at all angular scales")
print("=" * 60)

# ── Load Planck 70GHz SEVEM (nside=1024) ─────────────────────────────────────
print("\n[1] Loading Planck 70GHz SEVEM nside=1024...")
T_planck_raw = hp.read_map('/tmp/cmb_fractal/planck_sevem_070_1024.fits', field=0)
nside_planck = hp.get_nside(T_planck_raw)

# Subtract monopole, convert K → μK
T_planck = (T_planck_raw - np.median(T_planck_raw)) * 1e6
print(f"  nside={nside_planck}, rms={T_planck.std():.2f} μK")

# Apply galactic mask
mask_planck = galactic_mask(nside_planck, lat_cut_deg=20)
T_planck_masked = T_planck.copy()
T_planck_masked[~mask_planck] = hp.UNSEEN

# ── Synthesize WMAP from real C_l ────────────────────────────────────────────
print("\n[2] Loading WMAP 9yr power spectrum → synfast sky map (nside=512)...")
data_dir = "/media/rendier/0123-4567/Ainulindale/AddPapers/CMB_FractalBoundary/data"
wmap_tt  = np.loadtxt(f"{data_dir}/wmap_tt_9yr.txt")
ell_w, Cl_w = wmap_tt[:, 0], wmap_tt[:, 1]
# C_l in units of l(l+1)C_l/2π → convert to C_l
Cl_w_raw = Cl_w * 2*np.pi / (ell_w * (ell_w + 1))
# Pad to ell=0,1
nside_wmap = 512
lmax_w = int(ell_w.max())
Cl_full = np.zeros(lmax_w + 1)
Cl_full[0] = 0; Cl_full[1] = 0
for i, l in enumerate(ell_w.astype(int)):
    if l <= lmax_w:
        Cl_full[l] = Cl_w_raw[i]
# Interpolate gaps
from scipy.interpolate import interp1d
valid = Cl_full > 0
ells_v = np.where(valid)[0]
if len(ells_v) > 2:
    interp = interp1d(ells_v, Cl_full[valid], kind='linear',
                      fill_value='extrapolate', bounds_error=False)
    Cl_full = np.maximum(interp(np.arange(lmax_w+1)), 0)
    Cl_full[:2] = 0

np.random.seed(42)  # reproducible realisation
T_wmap = hp.synfast(Cl_full, nside=nside_wmap, lmax=lmax_w, new=True)
T_wmap_masked = T_wmap.copy()
mask_wmap = galactic_mask(nside_wmap, lat_cut_deg=20)
T_wmap_masked[~mask_wmap] = hp.UNSEEN
print(f"  nside={nside_wmap}, rms={T_wmap[mask_wmap].std():.2f} μK")

# ── Degrade Planck for direct comparison ─────────────────────────────────────
print("\n[3] Degrading Planck to nside=512 for cross-comparison...")
T_planck_512 = hp.ud_grade(T_planck, nside_out=512)
mask_p512    = galactic_mask(512, lat_cut_deg=20)

# ═══ PTYCHOGRAPHY: D_f at multiple FOV scales ════════════════════════════════
print("\n[4] PTYCHOGRAPHY — box-counting D_f at multiple angular scales")
print(f"{'FOV':>8}  {'Dataset':>8}  {'D_f':>7}  {'err':>6}  {'vs φ':>8}  {'vs φ−1':>8}")
print("-" * 58)

fovs        = [30, 15, 7, 3, 1.5]          # degrees
patch_centres = [
    (0,   45),   # north
    (90,  0),    # equator E
    (180, 0),    # equator W
    (270, -30),  # south
    (45,  60),   # high north
]

results = []
for fov in fovs:
    dfs_planck = []
    dfs_wmap   = []
    for (lon, lat) in patch_centres:
        # skip galactic plane patches
        if abs(lat) < 25:
            lon_use, lat_use = lon, lat + 35
        else:
            lon_use, lat_use = lon, lat

        for (T_map, ns, label) in [
            (T_planck_512, 512, 'Planck'),
            (T_wmap,       512, 'WMAP'),
        ]:
            img = gnomonic_patch(T_map, ns, lon_use, lat_use, fov, npix_img=256)
            bnd = temperature_boundary(img)
            if bnd.sum() < 50:
                continue
            _, _, Df, Df_err = box_count_df(bnd, min_box=2, max_box=bnd.shape[0]//4)
            if np.isfinite(Df):
                if label == 'Planck':
                    dfs_planck.append((Df, Df_err))
                else:
                    dfs_wmap.append((Df, Df_err))

    for (dfs, label) in [(dfs_planck, 'Planck'), (dfs_wmap, 'WMAP')]:
        if not dfs:
            continue
        vals = np.array([d[0] for d in dfs])
        errs = np.array([d[1] for d in dfs])
        Df_mean = vals.mean()
        Df_err  = vals.std() / np.sqrt(len(vals))
        vs_phi   = Df_mean - PHI
        vs_phi1  = Df_mean - PHI_1
        print(f"{fov:>6}°  {label:>8}  {Df_mean:>7.4f}  {Df_err:>6.4f}  "
              f"{vs_phi:>+8.4f}  {vs_phi1:>+8.4f}")
        results.append({'fov': fov, 'dataset': label,
                        'Df': Df_mean, 'Df_err': Df_err,
                        'vs_phi': vs_phi, 'vs_phi1': vs_phi1,
                        'n_patches': len(dfs)})

print("-" * 58)
print(f"Prediction P7: D_f(2D boundary) = φ = {PHI:.4f}")
print(f"Prediction P8: D_f constant across all FOV scales")

# ═══ FULL-SKY FRACTAL FLAMES IMAGE ═══════════════════════════════════════════
print("\n[5] Generating fractal flames images...")

fig, axes = plt.subplots(2, 2, figsize=(20, 12),
                          facecolor='#050010')
fig.suptitle("CMB Fractal Plasma Flame — Last Scattering Surface z≈1100",
             color='white', fontsize=14, fontweight='bold', y=0.98)

# Panel A: Full-sky Planck temperature (Mollweide)
ax = axes[0, 0]
ax.set_facecolor('#050010')
T_vis = T_planck_512.copy()
T_vis[~mask_p512] = 0
# Mollweide via healpy
plt.sca(ax)
hp.mollview(T_vis, fig=fig.number, sub=(2,2,1),
            cmap='RdBu_r', min=-200, max=200,
            title='Planck CMB Temperature (μK)', unit='μK',
            bgcolor='#050010', cbar=True)

# Panel B: Fractal flame boundary — full sky
ax2 = axes[0, 1]
ax2.set_facecolor('#050010')
T_vis2 = T_planck_512.copy()
T_vis2[~mask_p512] = 0
# Generate boundary map
print("  Computing full-sky boundary map (this takes ~30s)...")
nside_b = 256
T_b = hp.ud_grade(T_planck_512, nside_out=nside_b)
mask_b = galactic_mask(nside_b, lat_cut_deg=20)
npix_b = hp.nside2npix(nside_b)
boundary_map = np.zeros(npix_b)
boundary_map[~mask_b] = hp.UNSEEN
for pix in range(npix_b):
    if not mask_b[pix]:
        continue
    neighbors = hp.get_all_neighbours(nside_b, pix)
    neighbors = neighbors[neighbors >= 0]
    if T_b[pix] > 0 and any(T_b[n] < 0 for n in neighbors if mask_b[n]):
        boundary_map[pix] = 2.0    # hot→cold boundary: "flame front"
    elif T_b[pix] < 0 and any(T_b[n] > 0 for n in neighbors if mask_b[n]):
        boundary_map[pix] = 1.0    # cold→hot boundary: "flame base"

plt.sca(ax2)
hp.mollview(boundary_map, fig=fig.number, sub=(2,2,2),
            cmap=FLAME_CMAP, min=0, max=2,
            title='Fractal Plasma Flame Boundary', unit='boundary',
            bgcolor='#050010', cbar=False)

# Panel C: Zoom patch — fractal flames close-up (15° FOV)
ax3 = axes[1, 0]
ax3.set_facecolor('#050010')
img_zoom = gnomonic_patch(T_planck_512, 512, 60, 45, fov_deg=15, npix_img=512)
bnd_zoom = temperature_boundary(img_zoom)
# Flame image: temperature coloured, boundary in white/yellow
T_norm = img_zoom / (3 * np.abs(img_zoom[np.isfinite(img_zoom)]).std() + 1e-10)
T_norm = np.clip(T_norm, -1, 1)
rgba  = plt.cm.RdBu_r((T_norm + 1) / 2)
# Overlay boundary as flame
rgba[bnd_zoom, 0] = 1.0   # R
rgba[bnd_zoom, 1] = 0.6   # G
rgba[bnd_zoom, 2] = 0.0   # B
rgba[bnd_zoom, 3] = 1.0   # A
ax3.imshow(rgba, origin='lower', interpolation='bilinear')
ax3.set_title("15° Patch — Plasma Flame Boundary", color='white', fontsize=11)
ax3.axis('off')

# Panel D: D_f vs FOV scale plot
ax4 = axes[1, 1]
ax4.set_facecolor('#0a0020')
ax4.tick_params(colors='white')
for spine in ax4.spines.values():
    spine.set_color('#333366')
fovs_p = [r['fov'] for r in results if r['dataset']=='Planck']
dfs_p  = [r['Df']  for r in results if r['dataset']=='Planck']
errs_p = [r['Df_err'] for r in results if r['dataset']=='Planck']
fovs_w = [r['fov'] for r in results if r['dataset']=='WMAP']
dfs_w  = [r['Df']  for r in results if r['dataset']=='WMAP']
errs_w = [r['Df_err'] for r in results if r['dataset']=='WMAP']
if fovs_p:
    ax4.errorbar(fovs_p, dfs_p, yerr=errs_p, fmt='o-',
                 color='#ff6600', label='Planck', linewidth=2, markersize=8)
if fovs_w:
    ax4.errorbar(fovs_w, dfs_w, yerr=errs_w, fmt='s--',
                 color='#0099ff', label='WMAP synfast', linewidth=2, markersize=8)
ax4.axhline(PHI,   color='#ffee00', linewidth=2, linestyle='-',
            label=f'φ = {PHI:.4f}  (P7)')
ax4.axhline(PHI_1, color='#aa44ff', linewidth=1.5, linestyle=':',
            label=f'φ−1 = {PHI_1:.4f}  (1D spectral)')
ax4.set_xlabel('Patch FOV (degrees)', color='white', fontsize=11)
ax4.set_ylabel('Fractal Dimension D_f', color='white', fontsize=11)
ax4.set_title('Ptychographic Scale Invariance Test\nP8: D_f constant at all angular scales',
              color='white', fontsize=10)
ax4.legend(facecolor='#0a0020', edgecolor='#333366', labelcolor='white', fontsize=9)
ax4.set_xscale('log')
ax4.grid(True, color='#222244', alpha=0.5)
ax4.set_ylim(0.5, 2.2)

plt.tight_layout(rect=[0, 0, 1, 0.97])
out_path = f"{OUT}/fractal_flames.png"
plt.savefig(out_path, dpi=150, bbox_inches='tight',
            facecolor='#050010', edgecolor='none')
plt.close()
print(f"  Saved: {out_path}")

# ═══ ZOOM CASCADE: same image at 4 scales ═════════════════════════════════════
print("\n[6] Zoom cascade — ptychography: same boundary at 4 scales...")
fig2, axes2 = plt.subplots(1, 4, figsize=(24, 6), facecolor='#050010')
fig2.suptitle("Ptychographic Invariance: Fractal Plasma Flame at 4 Angular Scales",
              color='white', fontsize=13, fontweight='bold')

zoom_fovs   = [30, 10, 3, 1]
zoom_centre = (60, 45)
zoom_dfs    = []

for i, fov in enumerate(zoom_fovs):
    img = gnomonic_patch(T_planck_512, 512, *zoom_centre, fov_deg=fov, npix_img=512)
    bnd = temperature_boundary(img)
    _, _, Df, Df_err = box_count_df(bnd, min_box=2, max_box=bnd.shape[0]//4)
    zoom_dfs.append((fov, Df, Df_err))

    ax = axes2[i]
    ax.set_facecolor('#050010')
    T_norm = img / (3 * np.abs(img).std() + 1e-10)
    T_norm = np.clip(T_norm, -1, 1)
    rgba   = plt.cm.inferno((T_norm + 1) / 2)
    # Colour boundary by gradient magnitude (flame intensity)
    grad = np.sqrt(ndimage.sobel(img, axis=0)**2 + ndimage.sobel(img, axis=1)**2)
    grad_norm = grad / (grad.max() + 1e-10)
    rgba[bnd, 0] = 1.0
    rgba[bnd, 1] = np.clip(grad_norm[bnd] * 1.5, 0, 1)
    rgba[bnd, 2] = 0.1
    rgba[bnd, 3] = 1.0
    ax.imshow(rgba, origin='lower', interpolation='bilinear')
    df_str = f"{Df:.3f}" if np.isfinite(Df) else "?"
    phi_str = f"Δ={Df-PHI:+.3f}" if np.isfinite(Df) else ""
    ax.set_title(f"FOV={fov}°\nD_f={df_str}  {phi_str}",
                 color='white', fontsize=10)
    ax.axis('off')

out_cascade = f"{OUT}/fractal_flames_cascade.png"
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig(out_cascade, dpi=150, bbox_inches='tight',
            facecolor='#050010', edgecolor='none')
plt.close()
print(f"  Saved: {out_cascade}")

# ═══ SAVE NUMERICAL RESULTS ════════════════════════════════════════════════════
print("\n[7] Summary")
print("=" * 58)
print(f"{'FOV':>6}  {'D_f':>7}  {'Δφ':>8}  {'Δ(φ−1)':>8}")
print("-" * 40)
for fov, Df, Df_err in zoom_dfs:
    if np.isfinite(Df):
        print(f"{fov:>5}°  {Df:>7.4f}  {Df-PHI:>+8.4f}  {Df-PHI_1:>+8.4f}")

summary = {
    "experiment": "CMB Fractal Plasma Flame Boundary",
    "dataset": "Planck 70GHz SEVEM nside=1024",
    "prediction_P7": f"D_f(2D boundary) = phi = {PHI:.6f}",
    "prediction_P8": "D_f constant at all angular scales (ptychographic invariance)",
    "new_physical_claim": "CMB boundary = fractal plasma flame (not fur, not foam)",
    "phi":   PHI,
    "phi_1": PHI_1,
    "ptychography": results,
    "zoom_cascade": [{"fov": f, "Df": d, "Df_err": e}
                     for f, d, e in zoom_dfs if np.isfinite(d)],
    "part_3_pending": "Compare boundary to H_hat_RB theoretical prediction — deferred until data confirmed",
}
with open(f"{OUT}/fractal_flames_summary.json", 'w') as fp:
    json.dump(summary, fp, indent=2)
print(f"\nResults: {OUT}/")
print("  fractal_flames.png")
print("  fractal_flames_cascade.png")
print("  fractal_flames_summary.json")
print("\nP7 and P8 measured. Part 3 (H_hat_RB comparison) pending.")
