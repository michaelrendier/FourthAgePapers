# The Medium at Cosmic Scale: CMB and BAO

**Witch's Hat family, sibling paper E. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

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

The CMB/BAO structure is the same resonance seen at cosmic scale; the instrument's resolution limit ℓ* is read as a boundary. `THEORETICAL`. The medium's *origin* is not here (Part G, last).

## 2. Machinery

`CMB_FractalBoundary/` (Planck 2018 and WMAP 9-year TT spectra in `data/`; summaries in `results/`), `CMB_PlasmaBoundary/` (Planck 70 GHz SEVEM maps; ptychography and fractal-flame fits). The four notebooks have **no executed cell**. Planck SMICA R3.00 (2.4 GB; I, Q, U and the masks) is planned for the full-sky and polarization side; the manifest is written, **not downloaded**.

## 3. Results as recorded (`:CALCULATED` by the scripts that wrote them; **not reproduced in this pass**)

| Quantity | Planck 2018 | WMAP 9yr |
|---|---|---|
| global spectral index | −2.8596 | −2.0576 |
| DFA exponent α | 1.5414 | 1.2404 |
| fractal boundary ℓ* | 2450 | 1179 |

Fractal-flame ptychography (Planck 70 GHz) gives D_f = 1.973 ± 0.013 (30° fields) against the prediction φ = 1.618: the prediction **fails** at this field size; WMAP 2.011 ± 0.003. BAO: the sound speed c/√3 = 0.5774 c; Ω_ZS = 0.5671 is 1.8 % below it (ratio 0.9823, `:CALCULATED` in `papers/code/H_constants.py`). The two are different numbers; the closeness is noted, not used.

## 4. Stub list

1. Execute the four CMB notebooks; rerun the five "confirmed" predictions (needs the author's go) and record what holds.
2. Download Planck SMICA R3.00 (destination to be chosen; the faulting drive is not used for writes).
3. Euclid DR1-Foundation (released 2026-11-12, about 1900 deg², no polarimeter): footprint check against the Crab and the chosen Einstein crosses.
4. Reconcile the CMB trio (FractalBoundary, PlasmaBoundary, the Witch's Hat Part E): same object, three drafts; state the difference in each README.

## 5. References

Planck Collaboration (2020); Hinshaw et al. (2013); Eisenstein et al. (2005); DESI Collaboration (2024).
