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

## 2b. The hat potential as the lens (author's test, 2026-11-17)

The author's hypothesis: the size and shape of the Standard-Model Mexican-hat potential is what focuses the Lagrangian cone of dynamic action (L_dynamic, L_(I|O)) converging from the brim to the point at the top; varying the potential varies the focal *resolution* (not the focal point). `THEORETICAL`. Test: `papers/code/B_hat_lens.py` (numpy + scipy), output `papers/code/B_hat_lens_output_2026-11-17.txt`.

Model, stated so it can be argued with: unit-mass rays leave the brim ring inward at angle ψ to the radial, total energy E; potential V(x) = V₀(2xⁿ − nx²)/(n − 2), x = r/r₀, minimum −V₀ at the brim, hilltop V(0) = 0; n = 4 is the quartic hat V₀(x⁴ − 2x²). Resolution = closest approach r_min (units r₀). The existing engine `witches_hat.lichtenberg_paths` does not take a potential as input; this is a new calculation, not a rerun of it.

**Listing 2** — `papers/code/B_hat_lens.py`, output excerpts (`:CALCULATED`)

```
E=0: numerical r_min/r0 vs the small-psi closed form  sqrt(sin ψ) ((n-2)/n)^(1/4)
  psi=0.0001 n= 4  0.008409  0.008409  (rel diff 8.8e-06)
  psi=0.3    n= 4  0.470746  0.457126  (rel diff 3.0e-02)
integrated ray, n=4, psi=0.3, E=0:  (V0=1,r0=1) (10,1) (1,7) (0.2,3) all give 0.47075
bundle median r_min/r0 at E=0 against exponent n:  n=2.2 0.3500  4 0.3916  10 0.4318  20 0.4447
radial ray, n=4: reflection radius r_c/r0 = sqrt(-E/2) as E -> 0-: 0.0708 (E=-0.01), 0.0224 (-0.001), 0.0008 (0)
```

Results:
- At the separatrix energy E = 0 (the ray just reaches the hilltop, "the conical point") the closest approach is r_min/r₀ = √(sin ψ)·((n − 2)/n)^¼ for small ψ, confirmed numerically (8.8e-6 at ψ = 1e-4) and by integrating Cartesian rays. **Depth V₀ and size r₀ drop out entirely** (four (V₀, r₀) pairs, identical to five digits): a hat of any size or depth focuses the same, in units of its own brim.
- **The shape is the only knob.** The bundle's median r_min rises monotonically with the exponent n (0.350 at n = 2.2, 0.392 at n = 4, 0.445 at n = 20): a steeper-walled hat focuses less tightly. This part of the hypothesis (shape sets resolution, not the focal point) holds in this model.
- **Below the hilltop the hump reflects.** For E < 0 radial rays turn back at r_c/r₀ = √(−E/2) (n = 4): the "catastrophic internal reflection" is the hilltop acting as a barrier; the focal point is reached only at E = 0 exactly (a separatrix, infinite time).
- **Not found:** nothing in this family singles out n = 4. The resolution is smooth and monotonic in n, so "the Standard Model value is the one required for a cone" is **not supported by this test**; the quartic form is the lowest-order renormalizable one, which is an argument from the Standard Model, not from the focusing. A different definition of focus (caustic, action, or path-integral amplitude) could single out a value; none is tested here.

Next: the same bundle in the Jacobi metric with the real L_(I|O) weighting, and an amplitude (not ray) version, to see whether any n is selected.

## 2c. The simulator (2026-11-17)

`WitchesHat/simulator/` maps the established maths into one program: the Standard-Model Higgs hat with measured m_h and v (λ = 0.12938, brim radius 246.22 GeV, V″(0) = −μ², V″(v) = m_h² checked), Schrödinger m = 0 ring states (ground state on the brim, r = 0.969 and 0.991 at depths 40 and 400), the Maxwell + hat Nielsen–Olesen vortex (flux 6.283080 against 2π, Bogomolny residual 9.4e-5), and the classical path bundle from the brim at E = 0 with its abbreviated action (radial brim → hilltop W = 0.861929, exact and numerical agree). The author's cone of dynamic action is drawn on top and labelled `THEORETICAL`. Renders (Blender, `renders_v3/`) and the README are in that directory; the method is the `spatial-simulation` skill.

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
