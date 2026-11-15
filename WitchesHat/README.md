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
| D. Dark matter is a shape | gravity as shape, Bullet Cluster as two shapes crossing; GR/QM class jurisdiction | `BulletCluster/paper_draft.md` (abstract; sections 1–5 are stubs), `BulletCluster/README.md` | RM-ratio test **never run on observational data** (no Stokes Q/U on disk) |
| E. The medium at cosmic scale | CMB/BAO as the same resonance; plasma boundary | `CMB_FractalBoundary/`, `CMB_PlasmaBoundary/` | notebooks not executed (0 of 4); five "confirmed" predictions need rerun |
| F. The brim as turbulence | Ro = 1 ↔ D* = 1, the laminar–turbulent boundary | `Crawford_NavierStokes/` | gathering, not a programme |
| G. The medium's origin | cavitation, Bang, black-hole scar | `DeSitterCavitation/` (branch stub), `WhiteHoleBang/`, `PiFromAbove/` | stubs / drafts |
| H. Constants used | d*, Ω_ZS, the four d* faces | `Ainulindale/wiki/133_canonical_maths.md` §2.2 | ESTABLISHED arithmetic |

## 3. Pre-registered predictions and what the data say (`:CALCULATED`, 2026-11-14)

The predictions were committed in `Ainulindale` as `ac67bfa` (2026-05-30 11:52 −0700, notebooks 00 and 01); the first analysis commit is `dd86e87` (2026-05-30 20:42). So the pre-registration is real and precedes the analysis. The notebook gives no operational definition of its quantities; `DM_GalacticCavity/03_sparc_test.py` fixes them and prints every number below (output in `DM_GalacticCavity/results/03_sparc_test_output_2026-11-14.txt`). SPARC data: the repository holds the main tables and all 175 curves, byte-identical to the official site (`DM_GalacticCavity/data/SPARC_DATA.md`); the complete set, 1.3 GB, is in `/media/rendier/Telescope Data/SPARC/`. Used here: 135 have a flat V_flat and an NFW halo mass.

| # | Prediction | Result | Verdict |
|---|---|---|---|
| P1 | r_t / R_virial = 0.246 | median 0.028 (16–84 %: 0.009–0.050) with R_virial = R200 from the SPARC halo-mass table; r_t / R_disk median 1.68 | **fails** |
| P2 | V_flat / V_max,bar = 0.567 | median 1.66; only 16 % of galaxies have V_flat < V_max,bar | **fails** as written (a halo adds to the baryonic curve) |
| P3 | NFW r_s / R_virial = 0.246 (c = 4.07) | the repository has M200 only, not fitted r_s; the notebook's "c ~ 5–30, within range" is wrong for c = 4.07 | **not testable here**; one sentence corrected |
| P4 | Tully–Fisher exponent 4 | baryonic TF slope 3.49 ± 0.09 (y on x), 3.75 (x on y); 5.8 σ below 4 for the first | **fails** at this precision; the published value (≈ 3.85) is also below 4 |
| — | detection signal zero | no experiment is ours; not a result of this paper | `OPEN` (falsifier, not a test) |

The 2026-05-30 analysis in `dark_matter_cavity.py` is a different test from P1/P2: it fits a two-parameter arctan to each curve (v_max and r_last free per galaxy) and compares χ² with an NFW fit; its own commit message records P2 observed 0.508 ± 0.044 against 0.567, P1 median 0.296 against 0.246 "needs better transition detection", and P3 "contaminated". The wiki line "P1 confirmed against SPARC 97-galaxy sample" (`ValaQuenta/wiki/galactic_cavity.md`, `results_at_a_glance.md`) is not supported by that record and is to be corrected.


## 3b. The whole-dataset retest (`:CALCULATED`, 2026-11-14): is the cavity a better model?

`DM_GalacticCavity/04_sparc_retest.py` (numpy + scipy, 22 s, output in `results/04_sparc_retest_output_2026-11-14.txt`) fits **all 175** SPARC curves with eight models, baryons fixed at Lelli's 3.6 µm mass-to-light ratios, errors with a 5 % floor (the raw-error version is also in the output and agrees). BIC wins out of 175:

| model | free parameters | median χ²/dof | BIC wins |
|---|---|---|---|
| baryons only | 0 | 42.3 | 1 |
| baryons + RAR (McGaugh 2016) | 0 | 4.9 | 8 |
| cavity arctan alone, r_t free | 2 | 0.51 | 64 |
| cavity arctan alone, r_t = d* × r_last | 1 | 3.99 | 21 |
| baryons + cavity halo, r_t free | 2 | 0.41 | 33 |
| baryons + cavity halo, r_t = d* × r_last | 1 | 1.98 | 22 |
| baryons + NFW | 2 | 1.05 | 10 |
| baryons + pseudo-isothermal | 2 | 0.41 | 16 |

What it says, and what it does not:
- The cavity shape with its transition radius free beats NFW (better BIC in 153 of 175 galaxies for baryons + cavity; median χ²/dof 0.41 against 1.05). It **ties** the pseudo-isothermal halo (0.41 against 0.41; 33 against 16 wins is a split between two cored halos that differ by a few per cent in shape). So the data prefer a cored, saturating halo to a cusp; "cavity" is not separated from "cored isothermal sphere" by this test.
- The author's assumption that r_t = d* × r_last, with one parameter less, is **worse** than the free r_t (median BIC +8, +40 for the shape alone) and still the best model in 21–22 galaxies each. The free r_t / r_last has median 0.125 (0.19 with baryons) and 16–84 % range [0.014, 0.31] ([0.06, 0.52]): d* lies inside both, which is not a test, the range is too wide to exclude anything near it.
- r_last is the reach of the survey, not a property of the galaxy. The fitted r_t scales with it with log-log slope 0.26 (0.54 with baryons) and with the disk scale length with slope 0.44 (0.69); neither is a proportionality, so a constant fraction of either is not what the data show.
- The cavity shape alone (no baryons) wins most often because a two-parameter smooth saturating curve fits most smooth curves; it carries no information about the baryons and predicts nothing about the diversity of the curves. The baryon-informed models are the fair comparison.
- Not yet tested: a cavity with r_t set by a physical scale (disk length, HI radius) as one free multiplier; the RAR with a free acceleration scale; the mass-to-light ratio left free; the cavity's own prediction of the baryonic-to-total relation.

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
