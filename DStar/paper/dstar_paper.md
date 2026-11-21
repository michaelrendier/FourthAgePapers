# d*: one crossing, four faces, and a symbol table

### A code paper: the census, the two-ceiling derivation, and what the record says about each value

**Cody Michael Allison** (Michael Rendier), independent researcher · the.wandering.god@gmail.com · [ORCID 0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760) · github.com/michaelrendier\
**Written by an AI assistant:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), with the author's [`cs-paper-code-conventions` skill](https://github.com/michaelrendier/ContextPlease/blob/main/claude/skills/cs-paper-code-conventions/SKILL.md) running\
**Date:** 2026-11-21 · **Status:** draft for expert review · **Code:** [FourthAgePapers/DStar](https://github.com/michaelrendier/FourthAgePapers/tree/main/DStar)

---

> ## Read this first
>
> This paper was written by a transformer language model, Claude Sonnet 5.5, working with the author's `cs-paper-code-conventions` skill. The author is a software engineer, not a trained mathematician. Every statement not attributed to a cited source is unverified until an expert checks it. Results computed by code carry `:CALCULATED` after their label. The author does not tell the assistant what result he wants; tasks are given as measurements.
>
> The assistant itself caused the reason this paper exists: it read constant names out of the code (`OMEGA_ZS`, `A_PI`, `D_STAR`) and out of a stale context file, and those names were attached to the wrong values. §1 and §4.2 record that, with counts.

---

## Abstract

d* ≈ 0.2463 is the base-10 position of the fixed point of x ↦ e^(−x), read below a ceiling. The same fixed point, read in nats, is A_π = W(1) = 0.5671. We fix the symbol table the author has stated repeatedly (α, A_π, Ω_ζΣ), census every occurrence of d* and its companion values across the author's repositories and notes (17,240 distinct files, 8,603 matching lines), show that the crossing is independent of which ceiling is used (Hagedorn, Planck, speed of causality), list the five values d* takes in the record and what is known about each, and record two tested negative results: the BAO reading of the residual Δ = A_π − 0.246·ln 10 fails a null test, and the closed form of d*_RG is not found.

## 0. Scope and labels

| label | meaning here |
|---|---|
| `ESTABLISHED` | textbook or cited mathematics (Lambert W, contraction mapping, CODATA constants) |
| `OURS` | the author's assignment and naming; the census and the tests |
| `THEORETICAL` | stated in the repositories, not derived |
| `OPEN` | the record says it is open |
| `:CALCULATED` | a number a program in this directory printed |

Code: `dstar_census.py`, `dstar_symbols.py`, `ceilings_derivation.py`, `bao_test.py` (all in `FourthAgePapers/DStar/`), `ValaQuenta/engine/constants.py`, `ValaQuenta/modules/inductive_onset_residual/`, `RiemannHypothesisProof/rhp/polar_field.py`. Convention A (name the file) for the census and the engine; Convention B (verbatim listing) for the two short mechanisms; Convention D (transcript) for the printed output.

## 1. The symbols  `OURS`

The author's standing ruling (2026-11-21), stored as `@RCCM_SYMBOLS` in `~/.clauderc_canonical_maths`:

| symbol | value | side | what it is |
|---|---|---|---|
| α | 1/137.036 | — | the fine-structure constant (lowercase alpha, unless stated otherwise) |
| A_π (`A_PI`) | 0.5671432904 = W(1) | Fermat: speed of causality, inertia | the author's engineered discovery |
| Ω_ζΣ (Ω_RZ, `OMEGA_ZETA_SIGMA`) | 0.2463072015 = d* | Riemann: Hagedorn information ceiling, entropy | the author's engineered discovery |

Relation (`ESTABLISHED` algebra, `:CALCULATED` below): d*·ln 10 = A_π. "Omega" as the textbook omega constant is a different object from Ω_RZ and A_π.

Before 2026-11-21 `ValaQuenta/engine/constants.py` named 0.56714 `OMEGA_ZS`, 1/137.036 `A_PI` and ran `D_STAR = 0.24600`; the first-day README (2026-04-15) and wiki 17 used the same names. The census (`dstar_symbols.py`, `data/traces_swap.csv`) finds 889 lines that tie a symbol to the other assignment's value (642 for Ω_ζΣ, 247 for A_π), in ContextPlease, Ainulindale, ValaQuenta, VAPMIP and RiemannHypothesisProof. After the rename: `ALPHA_FS`, `A_PI`, `OMEGA_ZETA_SIGMA`; `OMEGA_ZS` stays as a deprecated alias of `A_PI`.

## 2. The values of d* in the record  `OURS` (read from `wiki/17`, `@RCCM_FOUR_DSTAR`, `constants.py`)

| name | value | status |
|---|---|---|
| d* "The Boundary" | 0.2463072015 (σ = ½ coordinate) | `ESTABLISHED` as the digits-per-step of the induction (§3); the σ = ½ reading is `THEORETICAL` |
| d*_RG "The Stability" | none; superseded estimate 0.24682 | `OPEN`: renormalisation-group fixed point in dimension 8, no closed form |
| d*_taut "The Flow" | Ω_ζΣ = A_π/ln 10 = 0.246307201473 | a tautology by construction; code must not hard-code d* as A_π/ln 10 |
| d*_ln(10) "The Translator" | d*·ln 10 = A_π (the wiki writes Ω) | the Jacobian between digits and nats |
| d*_spec | 0.24600 | the first-day measured value (3 digits); `D_STAR` in ~120 code files |

Open claim kept by the engine (`derivation_chain.d_star_tower_ln10`, tagged `[OPEN — high]`): d*_ℝ + d*_ℂ + d*_ℍ + d*_𝕆 = ln 10, one term per Cayley–Dickson stratum. Two weightings were tried in the code (linear in dimension: 3.690; log₂(dim+1): 1.987) and both miss 2.3026. The form of the weight function is not found.

## 3. The code

**Listing 1 — the induction x ↦ e^(−x) and the digits it gains per step (`paper/listing1.py`, verbatim, stand-alone)**

```python
import math
from decimal import Decimal, getcontext
getcontext().prec = 60
x = Decimal("0.5")
for _ in range(400):
    x = (-x).exp()                       # fixed point: x = exp(−x)  ⇒  x = W(1)
A_PI = float(x)
digits_per_step = -math.log10(A_PI)      # = A_PI / ln 10, because ln A_PI = −A_PI
print(f"A_PI              = {A_PI!r}")
print(f"digits per step   = {digits_per_step!r}")
print(f"A_PI / ln 10      = {A_PI / math.log(10)!r}")
print(f"0.246 · ln 10     = {0.246 * math.log(10)!r}   (residual vs A_PI: {A_PI - 0.246 * math.log(10):.12f})")
```

```
A_PI              = 0.5671432904097838
digits per step   = 0.2463072014734226
A_PI / ln 10      = 0.24630720147342253
0.246 · ln 10     = 0.5664359328765353   (residual vs A_PI: 0.000707357533)
```
`:CALCULATED`. The residual Δ = 0.000707357533 is the rounding of 0.24631 to 0.246 times ln 10; with the measured Higgs vacuum expectation value (246.21965 GeV) in place of 0.246 it is 0.000202.

**Listing 2 — one crossing under three ceilings (`paper/listing2.py`, verbatim, stand-alone)**

```python
import math
A_PI = 0.5671432904097838                           # from Listing 1
hbar, c, G, kB = 1.054571817e-34, 299792458.0, 6.67430e-11, 1.380649e-23
ceilings = {
    "Hagedorn (entropy side)":       7.78e16,                                   # K
    "Planck temperature":            math.sqrt(hbar * c**5 / G) / kB,           # K
    "speed of causality (inertia)":  c,                                         # m/s
}
for name, ceil in ceilings.items():
    star = A_PI * ceil                              # T*/T_ceil = exp(−T*/T_ceil)  or  g·exp(g/g0) = g0, g0 = c
    print(f"{name:30s} ceiling {ceil:.6e}  crossing {star:.6e}  digits below ceiling {-math.log10(star / ceil):.13f}")
```

```
Hagedorn (entropy side)        ceiling 7.780000e+16  crossing 4.412375e+16  digits below ceiling 0.2463072014734
Planck temperature             ceiling 1.416784e+32  crossing 8.035196e+31  digits below ceiling 0.2463072014734
speed of causality (inertia)   ceiling 2.997925e+08  crossing 1.700253e+08  digits below ceiling 0.2463072014734
```
`:CALCULATED`. The ceiling fixes the dimensional crossing; the dimensionless x* and the digit position do not depend on it. The Hagedorn value 7.78e16 K is the one used in `RiemannHypothesisProof/docs`; 1.4e17 K is also quoted there, and changes only the first column.

The census (`dstar_census.py`) walks the repositories, ContextPlease, `~/.clauderc*`, the memory directory and the Desktop notes, skips duplicate files by content hash, and records every line carrying a d* name, a face name, a d*-family value or a symbol name. `dstar_symbols.py` classifies each symbol line by the value on that line.

## 4. Results

### 4.1 Census  `:CALCULATED`
17,240 distinct files (7,216 duplicates skipped); 8,603 matching lines: 5,614 name d*/`D_STAR`, 1,190 name a face, 2,466 carry a value, 3,086 carry a symbol. Values: 0.246(0) 1,242 lines; 0.5671 947; 0.2463 302; 0.5664 (superseded d*_ln10) 139; 1/137 243. Largest holders: ContextPlease 2,735, Ainulindale 1,543, ValaQuenta 1,204, VAPMIP 810, FourthAgePapers 429, Ptolemy2 414, RiemannHypothesisProof 324.

### 4.2 The swapped names cost the polar-field experiment its crossing  `:CALCULATED`
`rhp/polar_field.py` is the April-2026 entropy/inertia field S(r, θ), I(r, θ). With the fine-structure value as the entropy coupling the two surfaces never meet: min |S − I| = 0.175 (α = 1/137.036) and 0.147 (α = 0.137), at r = 0.2346 and 0.2563. With the coupling set to A_π they touch (min |S − I| = 1.3·10⁻¹¹). The first touch in this widget is at coupling 0.5496 = 0.9691·A_π, so the widget does not single out A_π; the chase equation (Listing 2) does. The "d* ≈ 0.246" printed on the widget is a fixed string, not a computed value.

### 4.3 BAO reading of Δ: tested, not supported  `:CALCULATED`
`bao_test.py` registered two predictions before running. P1: no engine line computes a BAO observable from the constants (held, by reading `inductive_onset_residual`). P2: no expression of up to three factors from {A_π, Ω_ζΣ, φ, π, e, 2, 3, ln 10, Δ} (5,988 expressions) reproduces z_drag = 1059.94 ± 0.30, z_* = 1089.92 ± 0.25, θ_* = 1.0411·10⁻² ± 3.1·10⁻⁶ or ℓ_A = 301.63 ± 0.15 more often than random targets of the same size do (held: 0 hits on each target; random targets average 0.045–0.131). The BAO and "Yang–Mills mass gap" names for Δ are removed from ValaQuenta; the module is `inductive_onset_residual`. The separate statements "zeros = BAO frequencies" and "Hermite zeros = BAO timing marks" are not covered by this test.

## 5. What this does not show
- d*_RG has no closed form. The tower sum d*_ℝ + d*_ℂ + d*_ℍ + d*_𝕆 = ln 10 is not derived.
- The author reports that one Gemini visual (the zeta cardioid spiral, `Gem_FP.png`) fails without the four-valued d*, and another needs d*_taut. Neither was reproduced here; the visuals are in `~/Desktop/SpaceGemini/`.
- Whether string theory is the operator behind the cardioid is not tested. Nothing in the engines computes it.
- Version B of the inertia chase (the Gemini "α line", fine-structure floor to c) is not recovered; §3 derives the c-side crossing from the stated equation g·e^(g/g0) = g0 instead.
- The census counts lines that tie a symbol to a value; lines with no value on them (1,482) cannot be classified.

## 6. Reproducibility
```
cd FourthAgePapers/DStar
python3 paper/listing1.py ; python3 paper/listing2.py
python3 dstar_census.py && python3 dstar_symbols.py       # about 3 minutes, writes data/
python3 bao_test.py
RiemannHypothesisProof/.venv/bin/python ceilings_derivation.py
```

## Appendix A. What in ContextPlease was used
`~/.clauderc_canonical_maths` (`@RCCM_SYMBOLS`, `@RCCM_FOUR_DSTAR`); `ContextPlease/claude/hist_prime/RiemannHypothesisProof/PRIMER_2026-11-12_CEILING_DESCENT_FROM_CLAUDE_AI.md` (the April 9–10 chase, the widget definitions); the memory files `feedback_symbols_alpha_Apionly_OmegaZS` and `reference_four_dstar_values`; skills `cs-paper-code-conventions`, `lean`. ContextPlease is the author's archive of every context file and primer, committed so each session starts from the maintained copy; the SessionStart hook that injected a 2026-10-13 copy of the canonical maths until 2026-11-21 is the documented cause of the drift in §1.
