# The Witch's Hat — parent paper (register and plan)

**Branch `witches-hat`. State: claim register and consolidated context, draft v0.2, 2026-11-19. Not yet a paper.** Sections 1–6 are the register of 2026-11-14/17; sections 7–14 (2026-11-19) gather the engines, measurements, figures, wiki pages and skills built since, in one place. Introduction, abstract and prose are to be written with the author (problem and the way around it); nothing here is polished.

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


## 7. The Standard-Model hat as an engine, and the Lagrangians compared (`:CALCULATED`, 2026-11-19)

Engine `ValaQuenta/modules/lagrangian_sm` (21 equations; `Testing/test_lagrangian_sm.py`, 22 tests): the Standard Model built from its gauge group and field content, with PDG inputs from the installed `particle` tables. Narrative and tables: `Ainulindale/wiki/139_three_lagrangians.md`; API: `ValaQuenta/wiki/lagrangian_sm.md`; notebook `ValaQuenta/notebooks/engines/25_lagrangian_sm.ipynb`.

- **Derived, not measured** `ESTABLISHED`: the form of L_SM; the hypercharges (anomaly cancellation fixes them uniquely given the multiplets and Y_H = ½); fractional quark charges follow from N_c = 3 and the lepton charge (Q_u = ½ + 1/(2N_c); proton charge exactly 1 at N_c = 3). **Source of the anomaly cancellation:** the 15 Weyl fermions of a generation are exactly 5̄ ⊕ 10 of SU(5), Y a traceless generator, A(10) + A(5̄) = 0. **Observed:** the group, the multiplets, N_c = 3, three generations. **Measured:** 19 parameters (26 with Dirac neutrinos, 28 with Majorana; counted from the Yukawa structure).
- **The hat in numbers:** v = (√2 G_F)^(−1/2) = 246.22 GeV, λ = m_h²/(2v²) = 0.1291 (m_h = 125.13 GeV from the PDG table), depth λv⁴/4; tree m_W and m_Z within −0.16 % and +0.35 % of PDG, the difference being the electroweak correction Δr = 0.0364 (literature ≈ 0.036). One-loop gauge couplings cross at 1e13, 2e14, 1e17 GeV (spread 3.97 decades: no single unification scale). The one-loop λ → 0 scale swings from none below 1e19 GeV to 1e5 GeV as y_t(M_Z) goes 0.92 → 1.00: not a quotable number.
- **Each particle adds its own term** to the hat (Coleman–Weinberg): the top is about 40 times the W at h = v; bosons enter with n > 0, fermions with n < 0; the sign of one term depends on μ. The Yukawa couplings span six orders of magnitude (e 2.9e-6 … t 0.99) and nothing in the model explains the spread; the charged-lepton masses satisfy the Koide relation (0.666664 against 2/3; error not propagated).
- **L_NN (VAPMIP) against L_SM, measured on the code:** the coded bias term equals −V_SM exactly for μ² > 0 (5.6e-17): the one term-for-term identity; the coded `L_matter` has the form of the scalar–gauge seagull term of |DH|² (ratio 8/n, constant), not a Dirac term; gauge kinetic has degree 2 in A against 4; the coded Yukawa term is linear in ψ against bilinear; `polar_lagrangian` does not apply the 1/φ to `L_bias`; μ² < 0 gives a bowl as coded. "Term-for-term isometric" holds for the hat, the seagull form and the four-sector naming, not for the gauge, Dirac or Yukawa terms.
- **The four Lagrangians and their history:** the original L_dynamic (Ainulindale wiki 51, 2026-06-12) is `L_standard + ∫ J_red · d(J_blue)/dt dλ`, a time-dependent background; L_(I|O) = ∫ J_red · J_blue ds (renamed 2026-06-17) dropped L_standard and the time derivative, and its integrand is the constant e^(−E). `(I|O)` was also the April 2026 Inside-Out inversion inner product. Recommendation recorded: carrier = the SM Higgs hat (the L_NN hat is identical after normalisation); operation = the original L_dynamic read as a time-dependent background.

## 8. The path of action on the hat: stationary paths, the action cone, its tip and sheets (`:CALCULATED`)

Engine `ValaQuenta/modules/witches_hat/action.py` (`Testing/test_witches_hat_action.py`, 13 tests); nothing in it aims a path.

- **Stationary paths** (δS = 0, found by solving the Euler–Lagrange equations, with the Morse index): between one pair of events on the real hat there are three, S = 0.7742 (index 0), 0.7906 (index 1: a saddle, a neighbouring path does less work), 10.88 (index 2; r_min = 0.407, it climbs the hill's flank and out the far wall to r = 2.66; an earlier statement that it crosses the hilltop was wrong and is corrected). The discrete action error falls as 1/N² (ratios 3.99, 4.00, 4.00).
- **The unaimed fan from a brim point at E = 0:** closest approach to the hilltop ∝ (launch offset)^0.504 (closed form 0.5), coefficient 0.858 (0.841): a funnel, not a point caustic (the nearest caustic is 0.51 brim radii from the hilltop). The paths are the gradient lines of an action surface W with |∇W|² = 2(E − V): checked with W built only from 361 rays, median error 0.014 %, median angle 0.003°.
- **The bundle** (`brim_bundle`, `tip_report`): a path from every point of the brim in every direction (34,584), kept if it passes within 0.15 brim radii of the hilltop (698 do), each drawn at z = z_V(start) + W/(V₀τ₀) (brim 0, hilltop 1; τ₀ = R/√(2V₀)). Curved paths rise from the whole ring and converge on one point above the hilltop. **Tip:** 0.0015 R from the hilltop; W_tip = 0.4310 = (2/3)[(1 − r²/2)^(3/2)] from r = 1 to 0; **0.2189 depth-units above the hilltop** (exact radial value 0.2190), rising with E (0.312 at E = 0.01, 0.822 at 0.10). **The action is multivalued at the tip:** sheets at W = 0.4310 and 0.9025 = 0.4310 + 2 × 0.2357 (out to the wall at r = √2 and back), a ladder 0.431 + n × 0.4714.
- **L_NN (g = 0.2):** tip 0.0244 R from the tilted hilltop, 0.42 above it, six or seven sheets, height spread ±0.335 across the sources (the brim is not level); against g: tip offset 0.0078, 0.0007, 0.0026, 0.0505, 0.0686 R and gap 0.2189, 0.2184, 0.2189, 0.2876, 0.3229 for g = 0, 0.05, 0.10, 0.20, 0.40. **L_(I|O) on the same bundle** (E_J = 1, a free parameter): a straight cone in arc length, tip at z = 0.9785. **Moving hat (u = 0.25):** tip in the hat frame 0.0079 R, gap 0.196, W = 0.4228 ± 0.0414; the cone is sheared in the lab frame.
- **The tip distance is an important number (author, 2026-11-19).** It depends on the unit convention (action and energy differ by a time), on E (rising) and on the tilt (rising with g). Which dependence carries physical content is open.
- **Update 2026-11-19 (b): the tip distance has a closed form and ħ emerges.** At E = 0 the tip stands exactly **(4√2 − 5)/3 = 0.218951** depth-units above the hilltop, built from the actions W_direct = (2/3)(1 − 2^(−3/2)), W_wall = (2/3)2^(−3/2), W_total = 2/3 (units μ³/λ); in the hat's action unit S₀ = V₀τ₀ the wall action is 2/3 and the sheet spacing 4/3, for every μ and λ. The exact radial Schrödinger equation has a new bound state at the hilltop energy at ħ = 0.34117, 0.13082, 0.08091, 0.05857 …, following W_total = πħ_n(n + γ) with γ = 0.622 … 0.6235 (measured, not derived); N(ħ) = 1/(6ħ²) (Weyl). `ValaQuenta/modules/witches_hat/semiclassical.py`; `Ainulindale/wiki/141_hbar_from_the_hat.md`. The comparison of L_(I|O) with Feynman's path integral is structural (a sum over paths of e^(iS/ħ) against a line integral along one path) and the sheets are what a semiclassical sum sums over; PhiSpiral's closure is read there as a phase loop.
- **Figures** (versioned, kept with this paper): `papers/figures/lagrangians/v1.0/` (paths drawn on the potential surface) and `v2.0/` (the bundle and the action cone; companion `…_tip_and_time.svg`); generators `simulator/render_lagrangian_svgs.py`, `render_lagrangians_v2.py`, `tip_and_time.py`; index `papers/figures/lagrangians/README.md`. Brim gold, hilltop white, tip pale yellow.

## 9. The hat in time: temperature, a moving hat, the original L_dynamic (`:CALCULATED`)

- **Finite temperature** (`finite_temperature_hat`, high-temperature expansion, valid above about 100 GeV): D = 0.1666, E = 0.0096, T₀ = 163.4 GeV; brim radius 0.99 v at 100 GeV, 0.74 v at 140, 0.38 v at 160, zero above about 164: the hat does not quantise, it opens and deepens as it cools; at high temperature there is only a bowl with every particle massless. The approximation predicts a weak first-order jump where lattice calculations find a crossover; at T = 50 GeV it puts the brim at 1.035 v (an artifact; recorded).
- **A moving hat** (`moving_hat_exchange`, `ray_bundle` with u): a static hat conserves energy to 1e-12; in the hat's frame the energy is conserved to 1.4e-11 and the orbit is an ordinary bound orbit; in the lab frame the change is exactly u·(v − v₀) (0.2028 = 0.2028): momentum handed to the particle along the hat's motion (the gravity-assist form). A rotationally symmetric rotating hat exchanges nothing; a tilted hat whose tilt rotates does (tilt 0.15, T = 40: ΔE = +0.163, +0.902, −0.450 at ω = 0.3, 0.6, 0.9).
- **Shells** exist for a particle moving *in* the hat (radial Schrödinger equation in V = x⁴ − 2x²): 5 bound states below the hilltop at ħ = 0.35, 16 at ħ = 0.20; in the Standard Model itself particles are not bound in the hat, they get mass from the coupling to its vacuum value.

## 10. Length and time, the swap, and the horizon property (`:CALCULATED`, 2026-11-19)

Module `ValaQuenta/modules/witches_hat/length_time.py` (`Testing/test_witches_hat_length_time.py`, 9 tests); full text `Ainulindale/wiki/140_length_and_time.md` with figure.

- **Definition.** A space with a propagation-speed field v has a conversion of length into time: dℓ = v dt. In the hat at energy E, v = √(2(E − V)): the potential is the conversion field. Length measured in time is ρ = ∫ds/v (the tortoise coordinate); every classical path is a null curve of the optical metric −v²dt² + |dq|²; a space is fully described by its geometry and its conversion field together.
- **Tests:** radial paths are straight 45° lines in (ρ, t) (3.6e-12); t = ∂W/∂E on a bent path (4.2e-8), and across the swap dB/dE = −τ (1.1e-8); least action and least time are different paths (time excess 35 % for one pair, 5 % for another; 1.9e-16 for constant v) and v → 1/v exchanges them.
- **The swap** is where v² changes sign: Lorentzian optical metric where E > V, Euclidean beyond (real time becomes imaginary: the Wick rotation); the same conjugacy continues analytically. Penrose's arctan of a time and the Smith chart's tanh of a log-length are one map under ρ → it (tanh(ix/2) = i tan(x/2); the Gudermannian function), to 3e-14.
- **Classification of the zeros of v.** A *simple* zero (v ≈ κ|r − r_h|) is at infinite transit time (ρ ≈ (1/κ) ln distance), a *square-root* zero is at finite transit time. Measured: the E = 0 hilltop is a simple zero (κ = 1.0000; ρ(10⁻⁵) = −11.671; W to it finite, 0.43096): infinite time and finite length, the role of i⁺. The turning circle r = √2 is a square-root zero: transit brim → wall = ln(1 + √2) = 0.881374. The Schwarzschild exterior, with v = f = 1 − 2M/r, has a simple zero at the horizon with κ = 1/(2M) (M = 1: 0.5000, measured): its tortoise coordinate diverges the same way.
- **Not shown:** the Schwarzschild-style swap (both g_tt and g_rr flip, signature stays Lorentzian) is not what the optical metric does there (it goes from (−,+) to (+,+)); the Lorentzian version needs the Eisenhart–Duval lift (not tested). `CONJECTURE`: a static hat (v²(ρ)) and a hat whose conversion field depends on time (v²(t)) are swap partners, which would make the original L_dynamic the swap image of the static hat (null curves are 45° lines whatever v is; untested).

## 11. The horizon as the time distortion (author's reading, 2026-11-19; `INTERPRETATION`)

**The author's statement.** The event horizon *is* the time distortion; it is not an interior space, it is an exterior space. Far into the future, at the end of a black hole's life, technically we are on the inside of the black hole; you cross the horizon and exit the white hole; that is a clear pointer to *this* side of the event horizon being the interior, and we exit it.

**What the measurements say, and no more.** A horizon is, in the conversion-field language of §10, a simple zero of v: the transit time to it is infinite while the length to it is finite, the tortoise coordinate diverges, and the region "beyond" is never entered by the clock of the one approaching. That is what the hat's E = 0 hilltop does (κ = 1, W finite) and what the Schwarzschild exterior does (κ = 1/(2M)). So "the horizon is the time distortion" is exactly the statement that the horizon is where the conversion of length into time degenerates. Nothing in the engine tests whether the side we occupy is an interior; that is a statement about a metric, not about the hat.

**The standard picture it departs from** (`ESTABLISHED` statements, from memory, to verify under the Literature Download Protocol before use): the maximally extended Schwarzschild geometry (Kruskal 1960, Szekeres 1960) has a black-hole region, a white-hole region and a second exterior; for a hole formed by collapse (Oppenheimer–Snyder 1939) the white-hole region is replaced by the collapsing star, and with Hawking evaporation the diagram changes again. The interior of an Oppenheimer–Snyder collapse is a closed FRW universe, so its time reverse is an expanding universe: the established kernel of "an expanding universe as the inside of a black hole". Published proposals of that kind: Pathria 1972, Poplawski (Einstein–Cartan bounce, 2010), Smolin (cosmological natural selection, 1992). The author's reading, that we are on the interior side at the end of the black hole's life and exit through the white hole, is not a recognised solution of GR for a collapse-formed, evaporating hole.

**What would test it** (`OPEN`): which metric, which horizon; whether the "far future of the hole" and the Bang can be the same Penrose boundary (Part G, the medium's origin, comes last in this paper); and whether the hat's two kinds of boundary (a simple zero at infinite time, a square-root zero at a mirror) map onto the two kinds of surface in the maximally extended diagram.

## 12. Spaces and rendering rules (the `spatial-simulation` skill, v1.2.0)

`~/.claude/skills/spatial-simulation/` (mirror `ContextPlease/claude/skills/spatial-simulation/`; wiki `ContextPlease/claude/hist_wiki/skills/spatial-simulation.md`). New in v1.2.0: `references/spaces.md` with De Sitter, Hilbert, the Fano plane, sedenion space with the bracketing and firing-order engines, Mandelbrot–Julia, **gauge space** (the Scale engine's orthogonal Smith charts, Γ_SCALE = tanh(½ ln s) ⟂ Γ_ADD = tanh(½ a), the Apollonian gasket as the same Möbius-group object: the author's "complete shape of scale") and **equation space** (the σ = 0 permutation space of all equations from 0_RB; a stub), and the Higgs field space; the rule that an axis is (algebra, field, view), not a line, with each algebra dimension costing viewer budget. Measured with the repo's own code: 168 collineations of the Fano plane; 84 sedenion zero divisors over 42 index pairs (none in the octonions); Smith-chart circle pencils orthogonal and parabolic. **Rendering rules settled in use:** show what the maths says, never draw to resemble a picture; integrate the whole family and select by outcome; one natural vertical scale; report the tip number; cutaway views; chunked polylines (files under 5 MB); versioned names kept with the paper. The Standard-Model engine does not contain Minkowski space: its Lorentzian action is the spatially uniform mode of the Minkowski action, its Euclidean action the Wick rotation.

## 13. Open items (consolidated)

1. The tip distance: its dependence on E, on the tilt g, on the hat's shape (the quartic family, the exchange-hole hats) and on the unit convention; which dependence is physical.
2. The Lorentzian swap (Eisenhart–Duval lift) and the static ↔ time-dependent swap-partner conjecture (§10); whether Smith z → 1/z and v → 1/v are one inversion.
3. The horizon reading of §11: the metric, the Penrose boundary, and the link to Part G.
4. Paths on a hat whose parameters change with time (the finite-temperature hat); the local action profile along paths; two-loop running.
5. Gauge space and equation space: confirm the definitions in `references/spaces.md` §7–§8 with the author; equation space is a stub.
6. Wiki 04, 52, 64 and 100 still carry the pre-correction L_dynamic framing (not edited).
7. Toolbox pages are missing for `ptycho_weak_lensing`, `pi_derivations` and `circle_atlas`.
8. Failed results kept: P1, P2, P4 of §3 (the framework constants), the fermion-hole hat is not the SM quartic hat (matches only at n ≈ 2.1–2.3), the focus is a funnel and not a caustic (§8), the index-2 path does not cross the hilltop.
9. Parts C–E, G and J keep the state in §2; Part D needs the Crab Stokes maps.

## 14. Where everything lives, and what in ContextPlease was used

| what | where |
|---|---|
| engines | `ValaQuenta/modules/lagrangian_sm`, `modules/witches_hat` (`maths.py`, `action.py`, `length_time.py`), `modules/lagrangian` (L_NN), `modules/l_io_photon_path` |
| tests | `ValaQuenta/Testing/test_lagrangian_sm.py` (22), `test_witches_hat_action.py` (13), `test_witches_hat_length_time.py` (9); `ValaQuenta/tests/test_witches_hat.py` (16) |
| figures | `WitchesHat/papers/figures/lagrangians/v1.0/`, `v2.0/` |
| narrative wiki | `Ainulindale/wiki/139_three_lagrangians.md`, `140_length_and_time.md`; earlier: 29, 51, 52, 63, 64, 82, 133 |
| API wiki | `ValaQuenta/wiki/lagrangian_sm.md`, `witches_hat.md`, `toolbox/41_witches_hat.md`, `42_lagrangian_sm.md` |
| skill | `spatial-simulation` v1.2.0 (`references/spaces.md`) |
| context blocks | `~/.clauderc_ValaQuenta`: `LAGRANGIAN_SM`, `WITCHES_HAT_V2`, `LENGTH_TIME`; `~/.clauderc_canonical_maths`: `SM_LAGRANGIAN`, `L_DYNAMIC_ORIGINAL`, `LENGTH_TIME` (mirrored in `ContextPlease/claude/`) |
| scratchpad | `ContextPlease/claude/scratchpad/2026-11-19_lagrangian_sm/` (every measurement and generator) |
| claude.ai archive | artifact `SMNNIP Project Archive` (the April 2026 L_NN sheet, `SMNNIP_TODO` §3, the proposed UFT) |

**What ContextPlease is.** The project's public archive of the context a session needs to come up to speed: primers, scratchpads, skills, wiki mirrors and the `.clauderc*` context files. Used here: the scratchpad above, the `spatial-simulation` skill and its wiki page, the clauderc blocks in the table, `.clauderc_user_provenance` §1.19 (the three-ring Smith chart) and §1.4 (SMNNIP → VAPMIP), and `scratchpad/2026-09-28_lvap_audit/README.md` (what the L_NN "isometry" was and was not).

## 15. Units, flattening and emergence (Update 2026-11-19 (c))

Part H's constants in one place: d* and Ω are one step of the scale axis in two log bases; natural-unit systems are bases of the unit lattice with different index (Planck: determinant −2) and differ by dimensionless numbers (Stoney/Planck = √α); the electromagnetic systems are two flattenings of the ampere axis whose quotient is c; each unit choice collapses a specific relation (c = 1 the length–time conversion field, measured in §10; ħ = 1 the action unit, measured in §8). Constructed constants (the thermal information ceiling, 1.4×10¹⁷ K, the applicable range of the experiment's signal over background noise) are distinguished from emergent ones. Full text, scripts and what is not shown: `Ainulindale/wiki/142_units_flattening_and_emergence.md`.
