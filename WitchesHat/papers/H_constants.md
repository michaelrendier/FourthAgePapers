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
d*_spec (measured) = 0.24600 ; gap = 0.000307201473 ; 1/(1000 sqrt2) = 0.000707106781
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

- **Gap, corrected:** d*_spec − d* = −0.000307, not the 0.000707 (≈ 1/(1000√2)) recorded in the canonical-maths block; the two differ by a factor 2.3. I could not reproduce the recorded value from the quantities named beside it; recorded as a discrepancy to settle, not resolved.
- The 16-ball volume π⁸/8! = 0.23533 is 4.5 % below d* (ratio 0.9554): the closeness the author noticed. A coincidence of size, not an identity; no derivation links them (`OPEN`).
- X* = e^Ω = 1/Ω: the one point where log₁₀ X = d* and ln X = Ω (`ESTABLISHED` arithmetic; the prime-gap reading is the Riemann-side statement).

## 4. Stub list

1. Settle the gap value (0.000307 vs 0.000707) against `Ainulindale/wiki/133` §2.2.
2. d*_RG numeric: keep `OPEN`.

## 5. References

Corless et al. (1996) for Lambert W.
