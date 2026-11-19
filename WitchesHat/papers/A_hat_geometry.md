# The Hat as Geometry: the null cone, the brim, and the inversion

**Witch's Hat family, sibling paper A. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

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

At any event the null cone ds² = 0 has the shape of a witch's hat: tip = the event, surface = null geodesics, brim = the circle where a constant-time surface cuts the cone `ESTABLISHED`. The brim is the **fixed set** of the conformal inversion r ↦ R²/r about the brim sphere. The paper reads the brim as the Hawking pair's shared horizon (`INTERPRETATION`) and σ = ½ (`THEORETICAL`). One claim: *what the inversion does and does not give*.

## 2. Machinery

Engine: `ArdaQuenta/modes/witches_hat.py` (591 lines: null-cone pair, inversion, galaxy emergence, the L_dynamic action cone, animation; run `python3 modes/witches_hat.py out.gif`). Cold check of the lemma and of the halo claim: `papers/code/A_inversion.py` (numpy only).

**Listing 1** — `papers/code/A_inversion.py`, abridged output

```
involution max |inv(inv(r)) - r| = 4.44e-16
fixed set |inv(R) - R| = 0.0
exterior -> interior: True
volume ratio 0.041429  vs (R/r)^6 = 0.041429
inverted uniform density slope -6.02 (isothermal halo needs -2)
source r^-4 -> image slope -2.00
source r^-3 -> image slope -3.00
source r^0  -> image slope -6.00
```

## 3. Results (`:CALCULATED`)

- The inversion is an involution (to 4e-16), fixes r = R exactly, swaps exterior and interior, and has volume Jacobian (R/r)⁶ in three dimensions (finite-difference check, six digits). `ESTABLISHED` geometry, confirmed.
- **Failed, kept:** a uniform exterior density inverts to ρ ∝ r⁻⁶, not r⁻². An isothermal (flat-rotation) halo needs a pre-inversion density ∝ r⁻⁴. "The 1/r² halo emerges from the inversion" is not supported; the pre-inversion density is an input, not a consequence.
- The Lagrangian interpolation r(t) = (1−t)r + tR²/r fixes r = R for every t (arithmetic); it is a chosen interpolation, not an action principle.

## 4. Stub list (to do)

1. Run `witches_hat.py` headless and record its printed state; restore the missing animation (`Ainulindale/animations/`).
2. The operator mapping (null → e₁, cone → e₁₁, horizon → e₂ …) is not in code: write it as a table or drop it.
3. Source density: which physical pre-inversion density would be r⁻⁴, and why (open).
4. Link to Part B (what flows on the cone) and the Circle Atlas (inversion = the `inversion` viewport).

## 5. References

Hawking (1974); Hawking, Perry & Strominger (2016); Penrose (1965). Journal details to be checked against `Ainulindale/wiki/98_provenance_and_citations.md`.

## Update 2026-11-19

The hat's shape and its paths are now computed by `ValaQuenta/modules/witches_hat` (action cone, tip and sheets, §8 of the parent `../README.md`; figures `figures/lagrangians/v1.0` and `v2.0`). Parts of this draft predate that: the focus is a funnel (closest approach ∝ offset^0.504), not a point caustic; the tip of the action cone stands 0.2189 depth-units above the hilltop at E = 0. Failed results above are kept.
