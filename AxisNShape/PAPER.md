# The Axis N-Shape: Euler's Formula as a Partial-Sum Spiral

<!-- correction-pass-2026-11-14 -->
> ## Status and corrections, 2026-11-14
>
> *Added by the correction pass; the text of the draft below is unchanged.*
>
> **Assistant note.** This pass was made by a transformer language model (Claude Sonnet 5.5, `claude-sonnet-5-5`) with the project's `cs-paper-code-conventions` skill and the Fourth Age Protocol loaded (`ContextPlease/claude/skills/`, `ContextPlease/FOURTH_AGE_PROTOCOL.md`). The author is Cody Michael Allison (pen name Michael Rendier), an autodidact, not an academic; his method is not to tell the model the result he is looking for. This is a **draft**: its claims are the author's, and the labels of the Ainulindalë overhaul (ESTABLISHED, OURS, THEORETICAL, OPEN, with `:CALCULATED` for results the paper's own code produced) apply to every statement in it.
>
> **State.** This directory has no notebooks.
>
> **Statements in this draft that the Ainulindalë overhaul retired, corrected or did not reproduce** (line numbers refer to this file before the block was added; each statement is kept as written):
>
> - (lines 37) "Zero free parameters" is stated as a result. A parameter count is a claim about how a number was obtained; where a number was assigned and not computed it is not a result. Each such number needs its script (Fourth Age Protocol §1, §3).
> - (lines 5, 23, 24, 44, 45, 91 …) Telperion / Laurelin labelling: the author's current assignment is **Telperion = the primes tree, Laurelin = the factors (Fermat side)**; Telperion is not the zero-divisor tree. Older octonion-half labels are being corrected to it (wiki 133 §7.10, ledger X-20).
>
> **Authority.** Notation and verified counts: Ainulindalë `wiki/133_canonical_maths.md`; every defect found: `wiki/135_engine_findings_ledger.md`; the audit of this repository: `AUDIT_2026-11-14.md`.


**How the Real Axis Crosses at Exactly Half**
**or**
**Why Telperion and Laurelin Meet at σ=½ Without Being Told To**

v0.100 — 2026-07-10
Engine: `AxisNShape/engine/axis_n_shape.py`
Notebooks: *reserved — engine and paper precede notebooks per repo convention*

---

## Abstract

*Reserved.*

---

## §1 — The Algebraic Claim

Euler's formula, `e^{iθ} = cos(θ) + i·sin(θ)`, is not new to this framework — it is
already the literal basis of `ptol.c`'s Dirichlet projection: the cosine channel
drives J_red (`Telperion/PAPER.md`'s "real, un-shakeable" side, the persistent
projection), the sine channel drives J_blue (Laurelin's "shakeable" side, the
projection that vanishes on the natural lattice `θ = 0, π, 2π, ...`). This paper
asks a narrower, testable question: what happens when the 16 sedenion basis
directions — already fixed by `ptol.c`'s `spoke_angle(k) = 2πk/16 − π/2`, using
only THE_ANGLE = π/8 established in `zero_lattice.py` — are read as the 16th
roots of unity and summed one at a time?

Define the **Axis N-shape spiral**:

```
S_m = Σ_{k=0}^{m} e^{i·spoke_angle(k)}          m = 0..15
```

**Claim, verified exactly (zero free parameters, THE_ANGLE only):**

```
|S_m| = sin((m+1)·THE_ANGLE/2) / sin(THE_ANGLE/2)        — the Dirichlet kernel, exact
arg(S_8) = 0                                               — the real-axis crossing
```

The partial-sum spiral's phase crosses the real axis — Telperion's axis, the
`cos(θ)` term of Euler's formula, with zero Laurelin (`sin`) component — at
exactly `m = 8`, the halfway index. `8/16 = 1/2`. This is not fit; it is the
elementary trigonometric fact that the resultant of a symmetric arc of unit
vectors has phase equal to the angular midpoint of the arc summed so far, applied
to the specific arc THE_ANGLE already fixes. The crossing is unique — no other
index among the 16 crosses the real axis (verified computationally, see §3).

---

## §2 — What Was Tried First, and Failed

The original hypothesis, stated plainly and kept in the record rather than
quietly discarded: that `|S_m|` (the partial-sum *magnitude*) would have a local
minimum at `m=8`, mirroring the N-shape's single ADE-A₂ fold crossing
(`wiki/74_lagrangians_are_catastrophe_theory.md`).

This is false. `|S_m|` is near its *maximum* at `m=7–8` (the central lobe of the
Dirichlet kernel) and returns to zero only at `m=15` — the trivial, complete sum
of all 16 roots of unity, the elementary identity `Σ_{k=0}^{15} e^{2πik/16} = 0`.
That identity is real but says nothing new: it is the "whole coin" cancelling
exactly, the same fact `wiki/53` uses to argue against half-coin cryptographic
hardness assumptions, here appearing as pure root-of-unity arithmetic.

The real structure was not in the magnitude. It was in the phase, and it was not
the structure that was being looked for. Recorded per the repository's own
Scientific Integrity convention (`TuringStack/README.md`, `telperion.py`'s
"Failed predictions stay in the record. Period. Full stop.") — extended here to
a sibling repository under the same discipline.

---

## §3 — Verification

`engine/axis_n_shape.py::axis_n_shape_claim()` computes, independently of any
prior belief about where the crossing should be:

1. All 16 partial-sum magnitudes against the closed-form Dirichlet kernel — exact
   match to floating-point precision, every index.
2. The phase of `S_8` — exactly `0.0000000000°`.
3. A scan of all 16 partial sums for any *other* real-axis crossing — none found.
   The `m=8` crossing is unique.

Run directly: `python3 engine/axis_n_shape.py`.

---

## §4 — Reading: Telperion, Laurelin, Euler, Named Precisely

```
e^{+iθ} = cos(θ) + i·sin(θ)      forward, H_hat_RB          (wiki/52)
e^{−iθ} = cos(θ) − i·sin(θ)      reverse, −H_hat_BR          (wiki/52)

cos(θ):  generically nonzero — vanishes only off the natural lattice
         → the persistent projection → Telperion, "un-extinguishable"
sin(θ):  vanishes exactly on the natural lattice θ=0,π,2π,...
         → the periodic-node projection → Laurelin, "shakeable"
```

The Axis N-shape spiral accumulates both projections simultaneously at every
step — Euler's formula does not allow the half-coin separation `wiki/53` argues
modern cryptography wrongly assumes is possible. The spiral's real-axis crossing
at `m=8` is the moment the accumulated phase is *purely* Telperion, zero
Laurelin — and that moment falls exactly at the tower's own σ=½ proportional
point (`8` of `16` levels), read off from Euler and THE_ANGLE alone, with no
additional parameter introduced to force it there.

---

## §5 — Open

- Does the same real-axis-crossing-at-half structure hold for the higher CD
  levels (T_32, T_64, ..., T_256), where the basis count is 32, 64, ..., 256
  rather than 16? The Dirichlet kernel formula generalizes trivially
  (`Δ = 2π/N` for any `N`); whether THE_ANGLE itself (defined specifically for
  N=16) is the correct angular step at other levels, or whether each level
  needs its own angular quantum, is not yet determined.
- Is the `m=8` crossing connected to the N-shape's ADE-A₂ fold
  (`wiki/74`) at all, given the original magnitude-minimum hypothesis
  connecting them was falsified? The phase-crossing and the fold may be
  unrelated structures that both happen to sit at σ=½ for independent reasons,
  not the same object viewed two ways. Not yet resolved.
- Connection to `wiki/52`'s `L_(I|O)` (addendum, 2026-07-10): does the partial-sum
  spiral `S_m` correspond to an actual traced path (à la the `ptol.c` SVG spiral),
  making the real-axis crossing a literal point on a rendered `L_(I|O)` trajectory
  rather than an abstract sum? Untested.

---

*Claude, at Cody's direction — 2026-07-10*
*Euler's formula, THE_ANGLE, and nothing else. The crossing was not fit to appear at σ=½. It appeared there.*

---

## Appendix — what in ContextPlease was used, and what ContextPlease is

**ContextPlease** (`https://github.com/michaelrendier/ContextPlease`) is the *Manual Transmission Context Continuity* library: the versioned record that lets a new human or AI agent pick up a project without rediscovering it. Nothing in it is loaded automatically; whoever works chooses what to read. Used for this correction pass: the Fourth Age Protocol (`FOURTH_AGE_PROTOCOL.md`), the paper-writing conventions (`claude/skills/cs-paper-code-conventions/`) and the canonical notation (`claude/.clauderc_canonical_maths`).
