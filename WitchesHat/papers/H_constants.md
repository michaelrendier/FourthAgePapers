# The Constants Used: Ω_ZS, d* and its four faces

**Witch's Hat family, sibling paper H. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

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

Arithmetic only. Ω = W(1) is the fixed point of e^(−x); d* = Ω/ln 10 is the radial unit in the ln 10 chart; the four faces are four readings of one point (`THEORETICAL`), and d*_spec = 0.24600 is a *measured* value that is not one of them.

## 2. Machinery

**Listing 1** — `papers/code/H_constants.py` (stdlib only)

```
Omega = W(1) = 0.567143290410 ; W e^W = 1.000000000000
d* = Omega/ln10 = 0.246307201473 ; d* ln10 = 0.567143290410
d*_spec (measured) = 0.24600
gap in d* units  d* - d*_spec            = 0.000307201473
gap in ln10 units Omega - d*_spec ln10   = 0.000707357533 ; /ln10 = 0.000307201473
1/(1000 sqrt2) = 0.000707106781 (differs from the ln10-unit gap by 2.5e-07: the 'closeness' is 0.03 percent, not an identity)
X* = e^Omega = 1.763223 = 1/Omega = 1.763223 ; log10 X* = 0.246307201 = d*
c_s/c = 1/sqrt3 = 0.577350 ; Omega/(1/sqrt3) = 0.9823
16-ball volume pi^8/8! = 0.23533 ; d* = 0.24631 ; ratio 0.9554
```

## 3. Results (`:CALCULATED`)

| face | value | status |
|---|---|---|
| d* "Boundary" | 0.24631 | `ESTABLISHED` arithmetic |
| d*_RG "Stability" | dim 8, numeric | `OPEN`, no closed form |
| d*_taut "Flow" | Ω/ln 10 = 0.246307201473 | `ESTABLISHED` arithmetic |
| d*_ln(10) "Translator" | d* ln 10 = Ω = 0.56714329 | `ESTABLISHED` arithmetic |

- **A discrepancy, calculated and resolved:** the canonical maths gap 0.000707357533 and my first reading 0.000307 are the same quantity in two charts: Ω − d*_spec ln 10 = 0.000707357533 in ln 10 units; divided by ln 10 it is d* − d*_spec = 0.000307201473 in d* units (both printed by Listing 1). Its closeness to 1/(1000√2) = 0.000707107 is 2.5e-7 absolute, 0.035 %: a near-coincidence, not an identity (`OPEN`, as recorded).
- The 16-ball volume π⁸/8! = 0.23533 is 4.5 % below d* (ratio 0.9554): the closeness the author noticed. A coincidence of size, not an identity; no derivation links them (`OPEN`).
- X* = e^Ω = 1/Ω: the one point where log₁₀ X = d* and ln X = Ω (`ESTABLISHED` arithmetic; the prime-gap reading is the Riemann-side statement).

## 4. Stub list

1. Always state the chart (d* units or ln 10 units) beside any gap value.
2. d*_RG numeric: keep `OPEN`.

## 5. References

Corless et al. (1996) for Lambert W.

## Update 2026-11-19 (c): units, the natural steps, and constructed constants

- **d* and Ω_ZS are one step in two log bases** (d* = 0.2463072015 decades, Ω = 0.5671432904 nepers, d* · ln 10 = Ω): dimensionless, fixed by W(1), unchanged under any change of units. A natural-unit system such as Planck's supplies four reference points instead (determinant of (c, G, ħ, k_B) over (kg, m, s, K) is −2, an index-2 sublattice); Stoney units differ from Planck by exactly √α. `Ainulindale/wiki/142_units_flattening_and_emergence.md`.
- **Constructed constants in the record.** The thermal information ceiling of the engineered-constant experiment, 1.4×10¹⁷ K (140 quadrillion kelvin), is, for the purposes of that experiment, the upper end of the range over which the signal is distinguishable from background noise. It is a constructed range of applicability, not a Planck-type scale (T_P = 1.4168×10³² K); an earlier remark that the leading digits coincide was a coincidence and is withdrawn.
- **Emergence from two flattenings.** The electromagnetic units written in ESU and EMU differ by exactly one velocity (0, 1, −1) over (kg, m, s); c is the quotient (volt c, ohm c², farad c⁻², measured; ε₀μ₀c² = 1 to 12 digits; Z₀ = μ₀c = 376.730 Ω). The author's stance: constants may be constructed for analysis; where they emerge from native space is what is watched, and the kind of flattening points at the location. Nothing here locates the Planck length.
