# The Galactic Cavity: SPARC and Gaia tests, mainstream models only

**Witch's Hat family, sibling paper C. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5) with the project's `cs-paper-code-conventions` skill. The claims are the author's (Cody Michael Allison, pen name Michael Rendier). Every number marked `:CALCULATED` was printed by the code named beside it, run in this session; nothing else is a result.

## Notation and Disambiguation

| Label | Meaning here |
|---|---|
| `ESTABLISHED` | in the literature; cited, not derived here |
| `THEORETICAL` | the author's framework, stated, not tested here |
| `INTERPRETATION` | a reading of an established or measured object |
| `CONJECTURE` | stated, no calculation behind it |
| `OPEN` | a named gap |
| `:CALCULATED` | suffix: the paper's own code produced the number |

Maths follows `~/.clauderc_canonical_maths` (updated after the 0_RB rename: Ĥ_RB stays the maths name; 0_RB is VAPMIP/Monad-only). Failed results are kept.

## 1. Claim

A galaxy carves a resonant cavity whose boundary is the stellar disk; the dark-matter halo is the shape of the standing wave, not a particle. Ruling (author, 2026-11-15): a shape-of-gravity model needs no d* and nothing outside established astrophysics, so every test below uses literature models.

## 2. Machinery

`DM_GalacticCavity/03…10_*.py` (numpy + scipy, under a minute each); outputs in `DM_GalacticCavity/results/`. SPARC (Lelli, McGaugh & Schombert 2016): 175 curves, byte-identical to the official site, complete set 1.3 GB on the Telescope Data drive. Gaia DR3: 974,732 stars with radial velocities (`data/Gaia/fetch_gaia.py`). The full tables with every verdict are in `WitchesHat/README.md` §3–§3e; this page is the summary.

## 3. Results (`:CALCULATED`, 2026-11-14 to 2026-11-16)

| Test | Result |
|---|---|
| Pre-registered P1–P4 (d*-based) | P1 median r_t/R_vir 0.028 vs 0.246 **fails**; P2 V_flat/V_max,bar 1.66 vs 0.567 **fails**; P3 not testable; P4 TF slope 3.49 ± 0.09 vs 4 **fails** |
| Mainstream retest, 8 models | cored halos beat NFW in 141–153 of 175; arctan not distinguished from Burkert / pseudo-isothermal (ΔBIC 0.0) |
| Standing-wave halo ℓ = 0, 1 | equivalent to Burkert (median ΔBIC 0.0); ℓ = 2 worse (+3.3) |
| Fuzzy dark matter soliton + NFW | core–halo relation **fails** (slope 0.00 vs −1/3) |
| Radial acceleration relation | g† = 9.5e-11 m/s², 0.195 dex scatter (literature 1.2e-10, ~0.13 dex) |
| Gaia vertical motion | warp pattern speed ≲ 4 km/s; a c-speed wave of galactic wavelength is excluded for 0.1–1 kpc amplitudes |

Reading: the data say "cored and saturating" and no more; the standing-wave halo is an equivalent fit, not a preferred one. The 22.7 Gyr period in the older draft is not the wave's own period (λ/c = 10⁵ yr for λ = 10⁵ ly).

## 4. Stub list

1. Done 2026-11-17: `02_sparc_analysis.ipynb` repaired (its metadata block had been written as an escaped string, invalid JSON at line 243) and notebooks 00–02 executed with 0 errors; notebook 00 needed two compatibility fixes (an unused `sph_harm` import removed from scipy; a colour-array line colour replaced by a scatter). Notebook 02 reproduces the verdicts: P1 mean r_t/r_max rejected (p = 0.0013, deviation 0.093), Tully–Fisher log-slope 0.646 against the predicted 1.0, V_flat/V_bar,max mean 1.34 against 0.567.
2. The wiki line "P1 confirmed against SPARC 97-galaxy sample" is unsupported by the record; correct it **only on the author's go**.
3. Spin-2 radial functions; wave dispersion in the medium; DC14 profile; BTF and RAR scatter as secondary tests.
4. Write the white-paper form with cold listings (each of 03–10 as one Listing).

## 5. References

Lelli, McGaugh & Schombert (2016); McGaugh, Lelli & Schombert (2016); Courteau (1997); Li et al. (2020); Schive et al. (2014); Gaia Collaboration (2023).
