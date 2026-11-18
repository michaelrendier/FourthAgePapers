# Dark Matter as a Shape: polarization, birefringence and ptychography

**Witch's Hat family, sibling paper D. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

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

Gravity registers energy, and what energy leaves behind is a **shape** (the curvature of the region it occupied); a shape has nothing to scatter against, so in the Bullet Cluster the lensing peaks crossed while the gas stopped. Testing "dark matter as a shape" needs **ptychography** and possibly **birefringence** (author, 2026-11-17); the test is an RM-ratio test on real Stokes Q/U. `THEORETICAL`; **the test has never been run on observational data** (no Stokes Q/U is on disk).

## 2. Machinery

- Scope: `BulletCluster/paper_draft.md` (abstract; §1–5 are stubs), `BulletCluster/README.md`.
- **Listing 1** — `papers/code/D_birefringence.py`: the QED vacuum birefringence indices n∥ − 1 = (7/2)(α/45π)(B/B_c)², n⊥ − 1 = 2(α/45π)(B/B_c)², B_c = 4.414e9 T (`ESTABLISHED`, weak field B ≪ B_c), and a two-band Faraday-rotation recovery.

```
B=1e-04 T: n_par-1=9.273e-32 n_perp-1=5.299e-32 ratio=1.750000
B=1e+04 T: n_par-1=9.273e-16 n_perp-1=5.299e-16 ratio=1.750000
B=1e+08 T: n_par-1=9.273e-08 n_perp-1=5.299e-08 ratio=1.750000
RM in 150.0, two-band estimate 16.7 (n-pi ambiguity: 66.7 per step)
```

## 3. Results (`:CALCULATED`)

- The ratio of the two deviations is exactly 7:4 at every field strength (`ESTABLISHED`, confirmed): a birefringence test must look at a *ratio*, which is independent of B.
- **A failed recovery, kept:** two radio bands recover a rotation measure only modulo π/(λ₂² − λ₁²) = 66.7 rad/m²; the toy value 150 came back as 16.7. A real RM-ratio test needs many frequency channels (RM synthesis, Brentjens & de Bruyn 2005), not two bands.
- **Control: the Crab Nebula** (`J_crab_control.md`): its polarization is intrinsic synchrotron, so it is a control for the *instrument chain*, not for scattering. Real polarization exists at three HST epochs and IXPE.

## 4. Stub list (needs from the author)

1. The exact RM-ratio test: observable, expected sign and size, and which Einstein cross first.
2. Real Stokes Q/U for the chosen target (not yet requested; the Crab VLA/GBT request lists are in `BulletCluster/already_evaluated/CrabNebula/`).
3. A mass-model comparison for the Bullet Cluster using *measured* DM layer, not the stub.
4. Ptychography reconstruction code: not in this paper until it runs on a known object (Crab first).

## 5. References

Clowe et al. (2006); Heisenberg & Euler (1936); Brentjens & de Bruyn (2005).
