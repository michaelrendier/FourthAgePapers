# The Dynamic Path: L_(I|O) as the lensing time-delay functional

**Witch's Hat family, sibling paper B. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

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

L_(I|O) is not a new operator: it is L computed with the real (curved) metric, and the standard lensing statement is that the actual travel time differs from the flat-space one by the lensing potential, L_(I|O) − L = −ψ(θ) `ESTABLISHED` (Fermat potential; Schneider, Ehlers & Falco 1992). The author's reading, that the cone of paths from the brim to the point is a Lichtenberg-type figure on which this action flows, is `CONJECTURE` / `INTERPRETATION`.

## 2. Machinery

`ValaQuenta/modules/l_io_photon_path/` (`kaiser_squires_kappa`, `lensing_potential`, `deflection_field`, `trace_photon`, `l_io_deficit`, `bounded_lensing_pipeline`); specification `BulletCluster/L_IO_SPECIFICATION.md`. The chain: Kaiser–Squires shear → convergence (exact linear transform), ∇²ψ = 2κ (FFT solve), α = ∇ψ, β = θ − α.

**Listing 1** — `papers/code/B_kaiser_squires.py`: round trip on a *known* two-peak lens, no data.

```
kappa round trip max error 2.22e-16 (periodic box, k=0 mode dropped)
peak deflection (pixel units) 7.0138 ; psi range -384.080 .. 108.168
shape noise 0.01: rms kappa error 0.010, peak/rms-noise 38.7
shape noise 0.05: rms kappa error 0.050, peak/rms-noise 7.7
shape noise 0.20: rms kappa error 0.199, peak/rms-noise 1.9
```

## 3. Results (`:CALCULATED`)

- The transform pair is exact to machine precision on a periodic box once the k = 0 mode is set to zero. That degenerate point is where the mean convergence is unmeasurable (the mass-sheet degeneracy), and treating it as a stated boundary, not a patch, is the module's "boundary role" (`ESTABLISHED` method, author's naming).
- Shape noise passes through one-to-one: the recovered κ has rms error equal to the per-pixel shear noise. At 0.2 the peak sits at 1.9× the noise: any claim about a lensing map needs the noise level stated first.
- **First version failed, kept:** the round trip showed 1.6e-2 because the zero mode was zeroed in image space; and ψ was 40× too large because the (2π)² of the Fourier convention was omitted. Both were found by the round-trip test.

## 4. Stub list

1. Run the module on real shear (Bullet Cluster; `BulletCluster/lensing_validation/` holds the data inventory); the Bullet shear is not in this paper until a run is recorded.
2. Define "L_FR" as a functional or retire it (`Ainulindale/wiki/51` §1: three different zero conditions, no common locus computed).
3. The Lichtenberg paths: relate `witches_hat.lichtenberg_paths` to a geodesic family, or label it an illustration.
4. The primes-as-cavitation reading of wiki 51 §6 stays `CONJECTURE`.

## 5. References

Kaiser & Squires (1993); Schneider, Ehlers & Falco (1992); Clowe et al. (2006).
