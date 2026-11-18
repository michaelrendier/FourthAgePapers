# The Crab Control and the JWST Scaffolds

**Witch's Hat family, sibling paper J. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

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

The Crab Nebula is the **control**: a supernova remnant whose polarization is real, intrinsic synchrotron, observed over decades. Any pipeline that will be pointed at an Einstein cross must first recover the Crab's known polarization. One JWST image per target supplies the background scaffold. `THEORETICAL` (as a control design); the data inventory is `ESTABLISHED`.

## 2. Machinery

**Data on disk (verified by sha256, 60 of 60 completed files):** JWST GO 1714 (NIRCam F150W2 + F162M and F480M, Oct 2022; MIRI 7 filters + IFU, Feb–Mar 2023; **JWST has no imaging polarimeter**); the F150W2 + F162M mosaic is incomplete (2.66 of 8.92 GB, `.part` saved) after the Telescope Data drive reported write errors (kernel `critical target error`, Errno 121; no repair attempted). Records: `BulletCluster/already_evaluated/CrabNebula/` (README, manifest.json, VLA request lists).

**Polarization history** (archives and literature): optical polarization discovered by Dombrovsky (1954), mapped by Oort & Walraven (1956), Hiltner (1957), Woltjer (1957); HST polarizers WFPC2 F547M-POLQ 1996-01-26 (6129), NICMOS POL0L/120L/240L 1997-12-15 (7238), ACS F606W POL0V/60V/120V 2003-08-08/09 (9787); IXPE 2022 (Bucciantini et al. 2023: ~20 % at ~145°, toroidal); Moran et al. (2013). Radio: VLA and GBT projects selected by the author from the NRAO list (12B-380, 12A-486, 11A-268, 14B-341, AH919; pulsar polarization 15B-252, 22B-192, 25A-385, AGBT19B_352); **no radio file is downloaded; links awaited**.

**Scaffold algorithm** (`WitchesHat/scaffolds/make_scaffold.py`; from `BulletCluster` commit 8e482d2 `optical/jwst/make_background.py`):

```
level-3 i2d SCI  ->  reproject to a common north-up grid
chromatic assignment: shortest filters -> blue, middle -> green, longest -> red (average within a channel)
white balance: scale each channel by its 99th percentile; black point = 1st percentile
(added here) per-channel 15th-percentile sky subtraction; the unsubtracted variant is kept as _nosky
stretch: Lupton et al. (2004) asinh, make_lupton_rgb, Q = 8, stretch = 99.5th percentile of (R+G+B)/6
```

## 3. Results

- `:CALCULATED` Scaffolds built for every non-Bullet JWST data set on disk (9 targets, 534 files, 116 MB): Crab, HE 0435-1223, NGC 300, 891, 3521, 4051, 7331, Pillars of Creation, UGC 7524; index `WitchesHat/scaffolds/INDEX.md`; mirror `~/Desktop/SpaceClaude/BulletCluster/scaffolds/`.
- **Failure, kept:** the original algorithm leaves a strongly blue sky; the sky subtraction above was added, and the original is kept as `_nosky`.
- **Failure, kept:** a first download of the Crab pulled 532 per-exposure level-2 files (49.8 GB); stopped, cleaned, rebuilt for level-3 mosaics only (18 files, 10.5 GB).
- Polarization is a *control* for the instrument chain: the Crab's is synchrotron, not scattering, so it does not test the scattering hypothesis.

## 4. Stub list

1. Stokes I, Q, U maps from the HST polarizer exposures (1996, 1997, 2003): offered, awaiting the author's go. Then polarization angle and fraction against epoch.
2. Resume the NIRCam mosaic and Planck SMICA once a destination is chosen; one download at a time.
3. Restore `make_background.py` as a tracked, tested module.
4. Euclid DR1-Foundation footprint check for the Crab (b ≈ −5.8°).

## 5. References

Dombrovsky (1954); Oort & Walraven (1956); Hiltner (1957); Woltjer (1957); Moran et al. (2013); Bucciantini et al. (2023); Lupton et al. (2004).
