# Chirp Taxonomy: A Black Hole Merger Chirp is One Species of a General Genus

**Status: TODO — early, not a stub from zero.** Started 2026-09-25, on its
own branch (`chirp-taxonomy`) per Cody's explicit call — this is expected to
grow, unlike the two same-day stubs left on `main`. Built the same session
on real, already-run computation (mpmath, real zeros, real GW formulas), not
designed on paper first.

---

## One Claim

**"Chirp"** — any signal whose instantaneous frequency varies with time — is
not one thing. It is a genus with (at least) two structurally opposite
species, and both reduce to the same single tier-0 generator, `SCALE`, in
this project's `ADD:SCALE:SIGN` decomposition:

- **The gravitational-wave binary-inspiral chirp** (LIGO's own object):
  `f(t) ∝ (t_c − t)^{−3/8}` — a power-law `SCALE` word (`ln(t_c−t)`) whose
  argument runs to **zero**, producing runaway, positive-feedback,
  finite-time divergence at the merger. `df/dt ∝ f^{11/3}`: the rate feeds
  on itself.
- **The Riemann-Siegel theta function's own chirp**, `θ'(t) ≈ ½ln(t/2π)` —
  the *same* `SCALE` word, argument running to **infinity**, producing
  self-damping, ever-slower, non-singular growth (`θ''(t) ≈ 1/2t → 0`).

Same generator, opposite side of the same inversion boundary already
established for `J_N: r↔1/r` in this framework (interior/Contractor vs
exterior/Dilator) — not two unrelated phenomena that happen to share a name.
A LIGO chirp is one specific, real, experimentally-confirmed instance of the
general `SCALE`-chirp category; it is not the category itself.

**A second, matched claim, from the same generator split:** *resonance* is
the other tier-0 generator, `SIGN` (rotation), not `SCALE`. The Riemann zeta
zero spacings carry a genuine resonant substructure (Fourier-dual to the
primes, via the classical explicit formula — `RiemannHypothesisProof/
ADDENDUM_toroidal_theta_structure_2026-09-25.md`), while the smooth chirp
carrying it does not resonate at all (measured: `θ'(t)` power spectrum slope
`−14.3`, far from any resonance signature). A black hole's own merger event
already contains this exact same split, physically, not by analogy: the
**inspiral is the chirp** (`SCALE`), and the **ringdown is the resonance**
(`SIGN`) — a fixed-frequency, exponentially-damped quasinormal-mode ringing,
determined by the final black hole's mass and spin, not a sweep toward
anything.

## One Prediction (Ptolemy/0_RB)

**Checkable against real, already-published LIGO data, not run yet.** If the
`SCALE`/`SIGN` split is real and not a relabeling, then the inspiral-to-
ringdown transition in a real detected merger (e.g. GW150914) should show
the *same* qualitative signature already measured for the zeta torus: a
non-resonant, monotonically-evolving power spectrum during inspiral (no
characteristic peak frequency, consistent with `SCALE`), followed by an
abrupt transition to a sharply peaked, single-frequency, exponentially
decaying spectrum during ringdown (consistent with `SIGN`). This is a
real, falsifiable, and modest prediction — it does not claim a new physical
effect, it claims that a known physical transition (inspiral→ringdown) has
the same `SCALE→SIGN` character as the zeta torus's own major-loop→minor-
loop structure, checkable directly against public LIGO/Virgo strain data
(e.g. GWOSC). Not yet run against real strain data — that is the actual
next step, not a build task.

## One Engine

Home: `ValaQuenta` (per the "One Engine" rule — designed there, copied to
its eventual home by copying). Candidate components:
- Classical GW inspiral/ringdown formulas (standard post-Newtonian
  waveform + quasinormal-mode frequency tables — established physics,
  reference implementation only, not original).
- `RiemannHypothesisProof/ADDENDUM_toroidal_theta_structure_2026-09-25.md`'s
  already-run `θ(t)`/`Z(t)`/power-spectrum code (session scratchpad,
  reusable directly — the major-loop/minor-loop split machinery already
  exists, this paper's engine work is applying it to real GW strain data,
  not re-deriving it).
- A single decomposition function classifying a time series as
  `SCALE`-dominant (chirping, non-resonant, monotonic instantaneous
  frequency) vs `SIGN`-dominant (resonant, peaked, decaying) — not yet
  written.

## Talking to LIGO

The prediction above is stated so it can be put in front of someone who
works with real strain data without requiring them to accept anything about
sedenions, box-kites, or `0_RB` first — it's a claim about spectral
character across a known physical transition, checkable on public data.
That's deliberate: this paper's actual contribution is the *taxonomy*
(chirp genus, two species, one shared generator with resonance), not a new
physics claim GW science doesn't already have in some other vocabulary.

## One Wiki

Not written yet — last, per the rule.
