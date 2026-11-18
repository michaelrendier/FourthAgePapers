# The Witch's Hat — parent paper (register and plan)

**Branch `witches-hat`. State: plan and claim register, 2026-11-14. Not yet a paper.**

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5) with the project's `cs-paper-code-conventions` skill. The claims are the author's (Cody Michael Allison, pen name Michael Rendier). Labels: ESTABLISHED, THEORETICAL, INTERPRETATION, CONJECTURE, OPEN; `:CALCULATED` marks a result the paper's own code produced; failed results stay.

## 1. What this paper is

The author's statement: the Witch's Hat, the galactic particle, the resonation chamber, **spacetime is a medium**, **dark matter is a shape and not a stuff**, are one picture. The Mexican-hat potential of a particle becomes a Witch's Hat when the dynamic action path (the L_(I|O) path integral, a Lichtenberg-type figure) is added: the paths from the brim to the point trace a cone above the hat, and the tip of that cone is where the action flows. This paper is the **parent**: every telescope dataset tested and every SPARC result is presented here, and each component paper stays a separate paper that this one points to. This file is the register that makes that possible.

## 2. Parts (the component papers and pages)

| Part | What it carries | Where it lives | State of its code |
|---|---|---|---|
| A. The hat as geometry | null cone, brim as the fixed set of the inversion r ↦ R²/r | `Ainulindale/wiki/29_witches_hat_paper.md`; engine `ArdaQuenta/modes/witches_hat.py` | lemma ESTABLISHED; halo from inversion **fails** its test (ρ ∝ r⁻⁶, not r⁻²), recorded |
| B. The dynamic path and the cone | L_(I|O), L_FR = 0, the hat and its inverse | `Ainulindale/wiki/51_dynamic_geodesic.md`; `ValaQuenta/modules/l_io_photon_path`; `BulletCluster/L_IO_SPECIFICATION.md` | listing executed 2026-11-13; claims `CONJECTURE`/`INTERPRETATION` |
| C. The galactic cavity (SPARC) | the resonance chamber; pre-registered P1–P4; the "leaf in the bowl" | `DM_GalacticCavity/` (`paper_draft.md`, notebooks 00–02, `dark_matter_cavity.py`, `03_sparc_test.py`) | **run in this pass: §3 below** |
| D. Dark matter is a shape (needs ptychography and possibly birefringence, author 2026-11-17) | gravity as shape, Bullet Cluster as two shapes crossing; GR/QM class jurisdiction | `BulletCluster/paper_draft.md` (abstract; sections 1–5 are stubs), `BulletCluster/README.md` | RM-ratio test **never run on observational data** (no Stokes Q/U on disk) |
| E. The medium at cosmic scale | CMB/BAO as the same resonance; plasma boundary | `CMB_FractalBoundary/`, `CMB_PlasmaBoundary/` | notebooks not executed (0 of 4); five "confirmed" predictions need rerun |
| F. ~~The brim as turbulence~~ | **Not part of the Witch's Hat paper (author, 2026-11-17).** The Crawford / Navier–Stokes stub is not necessary here; `Crawford_NavierStokes/` stays as a notepad. | — | — |
| G. The medium's origin | cavitation, Bang, black-hole scar; the gravastar's photon sphere (Circle Atlas viewport `photon_sphere`) | `DeSitterCavitation/` (branch stub), `WhiteHoleBang/`, `PiFromAbove/` | **comes after all observational data has been evaluated (author, 2026-11-17): we do not guess at it, we measure it.** Stubs only until then |
| H. Constants used | d*, Ω_ZS, the four d* faces | `Ainulindale/wiki/133_canonical_maths.md` §2.2 | ESTABLISHED arithmetic |

> **Sibling drafts (2026-11-17):** one cursory cs-paper draft per part is in `papers/` (index `papers/README.md`). This file stays the register; the parent paper is rewritten after the siblings are reviewed.

## 3. Pre-registered predictions (framework constants d* and Ω_ZS) and what the data say (`:CALCULATED`, 2026-11-14; kept as the record of a failed pre-registration; the model test of §3b does not use them)

The predictions were committed in `Ainulindale` as `ac67bfa` (2026-05-30 11:52 −0700, notebooks 00 and 01); the first analysis commit is `dd86e87` (2026-05-30 20:42). So the pre-registration is real and precedes the analysis. The notebook gives no operational definition of its quantities; `DM_GalacticCavity/03_sparc_test.py` fixes them and prints every number below (output in `DM_GalacticCavity/results/03_sparc_test_output_2026-11-14.txt`). SPARC data: the repository holds the main tables and all 175 curves, byte-identical to the official site (`DM_GalacticCavity/data/SPARC_DATA.md`); the complete set, 1.3 GB, is in `/media/rendier/Telescope Data/SPARC/`. Used here: 135 have a flat V_flat and an NFW halo mass.

| # | Prediction | Result | Verdict |
|---|---|---|---|
| P1 | r_t / R_virial = 0.246 | median 0.028 (16–84 %: 0.009–0.050) with R_virial = R200 from the SPARC halo-mass table; r_t / R_disk median 1.68 | **fails** |
| P2 | V_flat / V_max,bar = 0.567 | median 1.66; only 16 % of galaxies have V_flat < V_max,bar | **fails** as written (a halo adds to the baryonic curve) |
| P3 | NFW r_s / R_virial = 0.246 (c = 4.07) | the repository has M200 only, not fitted r_s; the notebook's "c ~ 5–30, within range" is wrong for c = 4.07 | **not testable here**; one sentence corrected |
| P4 | Tully–Fisher exponent 4 | baryonic TF slope 3.49 ± 0.09 (y on x), 3.75 (x on y); 5.8 σ below 4 for the first | **fails** at this precision; the published value (≈ 3.85) is also below 4 |
| — | detection signal zero | no experiment is ours; not a result of this paper | `OPEN` (falsifier, not a test) |

The 2026-05-30 analysis in `dark_matter_cavity.py` is a different test from P1/P2: it fits a two-parameter arctan to each curve (v_max and r_last free per galaxy) and compares χ² with an NFW fit; its own commit message records P2 observed 0.508 ± 0.044 against 0.567, P1 median 0.296 against 0.246 "needs better transition detection", and P3 "contaminated". The wiki line "P1 confirmed against SPARC 97-galaxy sample" (`ValaQuenta/wiki/galactic_cavity.md`, `results_at_a_glance.md`) is not supported by that record and is to be corrected.


## 3b. The whole-dataset retest, mainstream models only (`:CALCULATED`, 2026-11-15)

**Ruling (author, 2026-11-15): a "shape of gravity" model needs no d* and nothing outside established astrophysics.** The retest therefore contains no framework constant. `DM_GalacticCavity/04_sparc_retest.py` (numpy + scipy, under a minute; output `results/04_sparc_retest_output_2026-11-15.txt`) fits all 175 SPARC curves with literature models only: baryons (Lelli et al. 2016 3.6 µm), the McGaugh–Lelli–Schombert (2016) radial acceleration relation, the empirical arctan rotation curve (Courteau 1997), and baryons plus an NFW, Burkert, Einasto (α = 0.17) or pseudo-isothermal halo, each with fixed mass-to-light ratios and with them free under the prior of Li et al. (2020). The earlier version of this section (2026-11-14, `results/04_sparc_retest_output_2026-11-14.txt`) carried a d*-based variant; it is kept as the record and is **superseded**.

Median χ²/dof and BIC wins among the eight fixed-M/L models, 5 % error floor (the raw-error run agrees):

| model | parameters | median χ²/dof | BIC wins |
|---|---|---|---|
| baryons only | 0 | 42.3 | 1 |
| baryons + RAR | 0 | 4.9 | 6 |
| arctan curve alone (no baryons) | 2 | 0.51 | 64 |
| baryons + arctan halo | 2 | 0.41 | 19 |
| baryons + NFW | 2 | 1.05 | 3 |
| baryons + Burkert | 2 | 0.48 | 53 |
| baryons + Einasto | 2 | 0.73 | 19 |
| baryons + pseudo-isothermal | 2 | 0.41 | 10 |

- **Cored halos beat NFW.** Arctan, Burkert and pseudo-isothermal halos are better than NFW in 153, 141 and 153 of 175 galaxies (Einasto 136), with median χ²/dof about 0.4 to 0.5 against 1.05. This is the known core–cusp result in SPARC (Li et al. 2020 and others), reproduced here.
- **The arctan "shape" is not distinguished from the other cored halos.** Against pseudo-isothermal the median ΔBIC is 0.0; against Burkert 0.0 (arctan better in 121 and 92 of 175). Whatever the shape of the halo is, these data say "cored and saturating" and no more; they do not select the arctan over the standard cored profiles.
- **Free mass-to-light ratio** (prior σ = 0.1 dex): the fitted disk ratios move off 0.5 in most galaxies (16–84 % range about 0.42 to 0.55 for the cored halos, 0.41 to 0.67 for NFW); with it free Burkert wins most galaxies (84 of 175 within that set) and NFW stays worst (median χ²/dof 0.92 against 0.38 to 0.41).
- **The arctan curve alone wins BIC in 64 galaxies only because it has no baryons to explain**; as a descriptive fit it is not a model of gravity and predicts nothing about the diversity of the curves.
- **The transition radius has no fixed ratio to anything measured.** Fitted r_t against the last measured radius has log-log slope 0.26 (0.54 with baryons), against the disk scale length 0.44 (0.69), against the HI radius 0.32 (0.67); neither is proportional. The last radius is the survey's reach, not a galaxy property.
- Not yet tested: the Burkert/NFW/Einasto parameters against the halo-mass tables of the same data (`HMF_*.mrt`), the DC14 profile of Di Cintio et al. (2014), the baryonic Tully–Fisher and RAR scatter as secondary tests, and any prediction of the shape-of-gravity picture that is not already one of the standard forms.

## 3c. The standing-wave halo, tested on SPARC (`:CALCULATED`, 2026-11-15)

`DM_GalacticCavity/05_sparc_standing_wave.py` (numpy + scipy, under a minute; `results/05_sparc_standing_wave_output_2026-11-15.txt`). Only established physics: the time- and angle-averaged energy density of a standing wave with multipole ℓ, u_ℓ(r) ∝ j_ℓ² + j_ℓ'² + ℓ(ℓ+1) j_ℓ²/x², x = kr, a scalar-wave template for the time-averaged stress-energy that gravitates (Isaacson 1968; Wheeler's geons). Derived and checked numerically: u ∝ 1/r² at kr ≫ 1 for every ℓ, so M(<r) ∝ r and the circular speed becomes constant (**a flat rotation curve follows from a standing wave**); ℓ = 0 and 1 have a finite central density (a core of size ~1/k), ℓ = 2 has a central hole. Birkhoff's theorem forbids a spherically symmetric gravitational wave, so for gravity the lowest multipole is ℓ = 2; ℓ = 0 is the scalar case.

| result on all 175 curves, 2 parameters each, baryons fixed | |
|---|---|
| baryons + wave ℓ = 0 / 1 vs baryons + Burkert | median ΔBIC 0.0 / 0.0; χ²/dof 0.51 / 0.52 against 0.48: **equivalent fits** |
| baryons + wave ℓ = 2 (the gravitational-wave multipole) | χ²/dof 1.00, median ΔBIC +3.3: worse than Burkert, still better than NFW (1.05 median, but a close call) |
| fitted wavelength / HI radius (ℓ = 0) | median 1.09 (16–84 %: 0.62–2.2); wavelength rises with size, log-log slope 0.79 |
| fitted wavelength / HI radius (ℓ = 2) | median 0.44 (0.27–0.77), slope 0.87 |
| stacked radial wiggle in the residuals at a wavelength proportional to the HI radius | **no peak**: prominence 0.164 against a shuffled-size null of 0.140 (95th percentile 0.231), p = 0.34 |

Orders of magnitude for a wave at speed c, wavelength 100,000 ly: period **10⁵ years**, phase advance in 76 years 0.27° (static to a human lifetime, yes), 2.0 cycles in 200,000 years (consistent with the author's "1 to 4 wavelengths"). **Not consistent with `DM_GalacticCavity/paper_draft.md` and `galactic_cavity.py`**, which state billion-year periods (22.7 Gyr): at speed c a billion-year period needs a wavelength of a billion light-years. The strain whose averaged energy density equals the local halo density at that wavelength is h ≈ 1.1 × 10⁻³, about 2000 times the galaxy's own potential depth (V/c)² = 5 × 10⁻⁷: the wave the halo needs is far larger than the field it is supposed to sit in.

A first version of the wiggle test permuted residuals within each galaxy and reported z = 11.5; that null is white noise, so any smooth misfit looked like a signal. It was wrong, was replaced by the shuffled-size null, and is recorded here.

Not yet done: tensor (spin-2) harmonics; the wave-equation dispersion (does the wave travel at c in the medium or slower); mixing ℓ modes; the stellar warp and the spiral pattern as the visible wave amplitude; DC14 and fuzzy-dark-matter soliton cores (Schive et al. 2014) as the standing-wave dark-matter models that are already in the literature.

## 3d. Two standing-wave tests from the literature (`:CALCULATED`, 2026-11-15)

**Fuzzy dark matter** (`DM_GalacticCavity/06_sparc_fdm_soliton.py`, `results/06_sparc_fdm_soliton_output_2026-11-15.txt`): the standing-wave halo already in the mainstream literature (Schive et al. 2014), soliton core + NFW, one **global** boson mass scanned, 3 parameters per galaxy. Simplifications stated in the script (plain sum instead of a matched join; constants recalled and to be checked). Results on all 175 curves: the total χ² is lowest at m = 10⁻²³ eV (7,704 for NFW alone, 5,392 for Burkert alone, 6,158 soliton + NFW); soliton + NFW has median χ²/dof 0.62 against NFW 1.05 and Burkert 0.48, and wins BIC in 18 galaxies against Burkert's 134. **The core-halo relation fails:** fitted r_c against fitted M200 has log-log slope 0.00, the soliton-halo relation predicts −1/3. The preferred mass 10⁻²³ eV lies below the range left open by the Lyman-α forest (recalled: roughly m ≳ 2×10⁻²¹ eV; check). So a standing-wave scalar halo is not preferred over a plain cored halo by these data.

**Disk density waves** (`07_sparc_disk_waves.py`, `results/07_sparc_disk_waves_output_2026-11-15.txt`): SPARC holds azimuthally averaged profiles and rotation curves, so a spiral wave cannot be seen in it; the script tests what can be. κ/Ω has median 1.50 (1.41 is flat rotation); with corotation at 2.2 R_d the outer Lindblad resonance sits at 3.9 R_d (3.5–4.6) and an inner one exists in only 26 of 139 galaxies; Toomre's critical wavelength from the stellar disk alone is 2.1 R_d (0.77–6.3), median 5.1 kpc. A common radial undulation in the surface-brightness profiles with wavelength proportional to R_d: peak at 1.36 R_d, shuffled-size p = 0.04, **not claimed**: it sits at the edge of the range tested (0.15–1.5 R_d) and the cubic baseline's own misfit has a size-linked scale, so the null is not clean at long wavelengths.

## 3e. Three more tests: baryons and halo, vector harmonics, Gaia vertical motion (`:CALCULATED`, 2026-11-16)

Scripts `DM_GalacticCavity/08_sparc_baryon_halo.py`, `09_sparc_vector_harmonics.py`, `10_gaia_vertical_wave.py`; outputs in `results/`. Gaia data: 974,732 DR3 stars with radial velocities
(random subsample, public ESA TAP, re-fetch with `data/Gaia/fetch_gaia.py`; the 152 MB CSV is not committed). A first fetch silently stopped at the service's default 50,000 rows and covered one patch of sky; it was discarded and refetched with a row limit (failure recorded here).

| Test | Result | Reading |
|---|---|---|
| 08 A radial acceleration relation | best g+ = 9.5e-11 m/s², rms scatter 0.195 dex over 3,389 points (literature: 1.2e-10, ~0.13 dex); this run has no quality or inclination cuts | relation holds as a one-parameter law; my numbers are looser than the paper's |
| 08 B halo vs baryons | M_halo vs M_bar Spearman +0.94, slope 0.86; with the shared radius removed +0.66; halo vs baryon velocity at R_last +0.88; r0 vs R_disk +0.61 against 0.01 ± 0.09 in the shuffled-size null; scatter 0.27 dex | the fitted halo follows the baryons; consistent with 'not independent of the matter', and equally with any model in which halo and baryons are coupled |
| 08 C age proxy (Hubble type) | f_DM at the last radius: early 0.77, late 0.79 (no trend, partial −0.12); at 2.2 R_d: early 0.44, late 0.75 (partial +0.22) | older-type galaxies have less dark matter inside the optical disk, not at the last point; type is a weak age proxy and SPARC has no ellipticals |
| 09 vector harmonics | same large-radius envelope for all spins (u x² → 1); vector l=1 median χ²/dof 0.42 vs Burkert 0.48; BIC wins BUR 75, V1 35, S1 23, V3 22, V2 18, mix 2; the l=1+2+3 mix is not preferred (ΔBIC +3.8) and 140 of 175 mixing weights sit at a bound | spin-1 does not change the result of 05; no sign of a multipole mixture; spin-2 radial functions not derived |
| 10 Gaia vertical motion | mean z rises from −37 pc (6–7 kpc) to +58 pc (11–12 kpc), mean V_z −1 to +2 km/s; pattern speed of the warp ≲ 4 km/s (floor 2 km/s systematic) | the plane moves slowly. For amplitudes 0.1 to 1 kpc the period is ≥ 1e8 to 1e9 years |

Finding of 10: matter that followed a wave of period λ/c = 1e5 years with a 0.1–1 kpc vertical amplitude would move at 6e3–6e4 km/s (0.02–0.2 c); the measured vertical motion is more than three orders of magnitude slower.
So the plane of the disk does not oscillate with a c-speed wave of galactic wavelength. A period of about 1e9 years, which is what the original draft says, is consistent with the warp for a kiloparsec amplitude, and is not the wave's own period.
The two periods have to be told apart: λ/c is the wave's, 1e8 to 1e9 years is the matter's.

## 4. Claims in this family that no code in the repository reproduces

- The Bullet Cluster paragraphs of `DM_GalacticCavity/paper_draft.md` §1 (five "attacks") are arguments, not computations; the quantitative parts (Clowe et al. 2006 and Bradač et al. 2006 numbers, WIMP exclusion limits, angular-momentum figures) are TODO.
- "Zero free parameters" (draft §8): the notebook's own constants carry no free parameters, but the analysis code fits two per galaxy (above).
- Schumann analogy (`v_n = v_max √(n(n+1)) mode(r)`): the ℓ = 0 mode being flat is a property of the spherical-cavity model, no calculation of a halo from it is in the repository.
- The 22.7 Gyr wave period of `galactic_cavity.py` is an engine output; its derivation is not in the paper.

## 5. Plan

1. Part C: rerun notebooks 00–02 (notebook 02 is **not valid JSON**, error at line 243, and has to be repaired first), repeat the test with chosen alternative definitions, and write the white-paper form with the cold-running listings.
2. Parts A and B: bring wiki 29 and 51 in as sections with their failed tests kept; run `witches_hat.py` and record what it outputs.
3. Part D: write sections 1–5 of the Bullet Cluster paper only from what exists on disk; keep the RM-ratio test labelled never run.
4. Part E: execute the CMB notebooks, rerun the five "confirmed" predictions, record what holds.
5. Every telescope dataset added later gets a row in a results table of this file, with the script that produced it.
6. ScalarContextPropagation last (the author's order).


## 6. Scope rulings of 2026-11-17 (author)
- **Part F (Crawford / Navier–Stokes) is dropped** from this paper; it remains a notepad.
- **Part G (the medium's origin) is last**: it waits until every observational data set has been evaluated.
- **Part D (dark matter as a shape)** requires **ptychography** and possibly **birefringence**; a polarization control is the Crab Nebula (HST polarizers 1996, 1997, 2003; JWST NIRCam/MIRI mosaics; VLA and pulsar polarization to be requested) with the Planck SMICA maps for the CMB/BAO side.
- **Scaffolds:** every JWST mosaic and IFU cube on disk except the Bullet Cluster (already done) has a raw image and a false-colour image under `WitchesHat/scaffolds/` (script `make_scaffold.py`; algorithm in its header), mirrored to `~/Desktop/SpaceClaude/BulletCluster/scaffolds/`.
