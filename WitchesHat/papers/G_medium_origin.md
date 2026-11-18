# The Medium's Origin: cavitation, the Bang, the gravastar photon sphere (LAST)

**Witch's Hat family, sibling paper G. State: cursory rough draft, 2026-11-17. Parent: `WitchesHat/README.md` (the parent paper is written after the siblings).**

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

## 1. Status

**This part comes after all observational data has been evaluated (author, 2026-11-17): we do not guess at it, we measure it.** Stub with the one measured object that exists.

## 2. The one calculated object

Circle Atlas viewport `photon_sphere` (`ValaQuenta/modules/circle_atlas`): the photon sphere as a circle, the "last layer before everything breaks".

```
u'' + u = 3u²  from u = 1/3 : circular null orbit r = 3M holds to 9e-16
critical impact parameter b = 3√3 M = 5.196 M
instability: growth per turn cosh 2π = 267.747 (measured 267.75)
gravastar: shell a ≈ 2.002 M, photon sphere at 1.4985 × shell, de Sitter horizon 1/H = 2.003 M (H² = 2M/a³)
```

`:CALCULATED`. The reading that the inside of the de Sitter region of a gravastar is our current universe, and that the last layer leads to the end of the black hole's life and not a singularity, is `INTERPRETATION`; no π route exists for it yet.

## 3. Stub list

`DeSitterCavitation/` (branch stub), `WhiteHoleBang/`, `PiFromAbove/`; nothing is drafted until Parts C, D, E have their results.

## 4. References

Mazur & Mottola (2004); Misner, Thorne & Wheeler (1973).
