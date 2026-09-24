# Fast Inverse

**Cody Michael Allison** (Michael Rendier) · the.wandering.god@gmail.com ·
[github.com/michaelrendier](https://github.com/michaelrendier) ·
ORCID: [0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760)

**Fourth Age Paper.** One Paper. One Claim. One Engine. One Wiki.

**Status: STUB.** Registered 2026-09-21. Not yet written.

---

## Origin — a derivation out of a gauge-field experiment

This paper is not a synthesis assembled after the fact. It is the
**derivation that came out of a specific experiment**: a live test of
whether a continuous conformal map (the Smith chart's `Γ(s)=(s−1)/(s+1)`)
carries classical gauge curvature, and whether a discrete circle-packing
(the Apollonian gasket) plays the role of a Mexican-hat potential the way
the Standard Model's symmetry-breaking sector does.

`.claude/scratchpad/2026-09-21_smith_apollonian_uft_probe/` is that
experiment, run first, checked piece by piece:

- `Γ`'s Schwarzian derivative is **exactly zero** — confirmed, not assumed
  — meaning it carries **no** classical gauge curvature (`F_μν`-type) at
  all, ruling out the literal reading tested.
- The gasket's own curvature ladder is a **discrete spectrum**, not a
  continuous potential well — the Mexican-hat reading doesn't fit as
  stated either.

Both specific readings tested **negative**. What the same experiment
turned up instead, checked later the same day and kept in the record
rather than discarded with the failed hypothesis: `Γ`'s real and
imaginary parts are **exactly** a harmonic conjugate pair (Cauchy-Riemann
exact, both parts exactly harmonic, symbolic — not finite-difference),
and `log Γ(s) = log(s−1) − log(s+1)` decomposes it as the superposition
of two elementary 2D Green's-function potentials — a source and a sink.
That **is** classical field structure, just not the gauge-curvature kind
the experiment set out to find. The negative result pointed at the real
one.

**Why the negative result doesn't close the question it looks like it
closes.** "Gauge" is not a metaphor borrowed for this paper — the word's
own origin is Weyl [1], who tried to unify gravity and electromagnetism
by making **SCALE itself** — the length standard, the gauge
(*Eichinvarianz*) — a locally variable freedom rather than a fixed
global constant. The curvature of that attempt's connection was the
first "gauge curvature" ever written down, under that name, and it was
built entirely out of the tier-0 SCALE operator (`L_k`) made **local**
(`k = k(x)`, position-dependent) rather than global. What the Schwarzian
check actually tested was a single, fixed, global Möbius map — correctly
found flat (Schwarzian ≡ 0), and correctly not gauge curvature, because a
*global* transformation was never going to produce any. The sharper,
Weyl-shaped version of the same question — build the connection where
`Γ`'s own scale parameter varies from point to point, and check whether
*that* connection's curvature is nonzero — was never run. That's the
actual open thread this paper inherits, not the closed one.

## The claim

> **The direction that costs — recovering a hidden structure from its
> effect, rather than reading the effect off a known structure — has one
> shape, found independently in three unrelated elementary objects, and
> it collapses to "free" in exactly the same way each time: when the
> object's own representation already encodes the answer, in a
> narrow, nameable regime.**

Three checked instances, not three examples chosen to fit:

1. **Arithmetic.** Digit multiplication decomposes entirely into
   tier-0 SCALE operations (`L_d`, one per digit, always invertible);
   `ADD` (the carry) is the *only* irreversible step in the whole
   construction, and it is exactly where recovering per-row information
   from the summed result becomes as hard as factoring the product.
   (`GenerationalLineage/engine/toolsets/hyper_linear.py`.)
2. **Number theory.** RSA key recovery from the public data alone is
   hard in general (the floor is GNFS/Shor); Wiener's continued-fraction
   attack is the one regime — `d` small — where the object's own
   representation (`e/N`'s continued fraction) already contains the
   answer, `O(log N)`, no search.
   (`GenerationalLineage/engine/ping.py`, `op_wiener`.)
3. **Complex analysis.** `Γ`'s field can be evaluated anywhere for free
   (one division); reconstructing an unknown source/sink configuration
   from field samples is the general inverse problem, hard outside
   special cases (three points pin a Möbius map exactly; fewer, or noisy
   samples, do not).

The **falsifier**: find a fourth elementary structure with a genuine
free/costly split whose "collapse to cheap" case does *not* reduce to
"the representation already linearizes the hard part in a nameable
regime." One clean counterexample closes the paper's claim as stated.

## Scope note — related stubs, not duplicated

- [`../TheInterface/`](../TheInterface/README.md) — `L_(I|O)` as a
  general boundary object. This paper's claim is about the *cost
  asymmetry* either side of an interface, not the interface's own shape;
  cite, don't restate.
- [`../AddScaleSign/`](../AddScaleSign/README.md) — ADD/SCALE/SIGN as
  computation's floor, language-independent, no physics framing by that
  paper's own design. This paper's arithmetic instance (§1 above) is a
  physics/structure-facing use of the same floor; the two should stay
  distinct papers per the "One Paper, One Claim" rule, cross-linked.

## References

1. Weyl, H. (1918). *Gravitation und Elektrizität.* Sitzungsberichte der
   Königlich Preussischen Akademie der Wissenschaften, 465–480. The
   origin of *Eichinvarianz* ("gauge invariance") — an attempt to unify
   gravity and electromagnetism by making the local length standard
   (scale) a free, position-dependent quantity rather than a fixed
   global constant. The unification failed empirically (Einstein's own
   objection: a scale-dependent metric predicts clock rates that depend
   on a particle's past path, unobserved); the *word* and the underlying
   move — promote a global symmetry to a local one, read the connection's
   curvature — survived and became the gauge theories of the Standard
   Model, applied to phase (`U(1)`) rather than scale. Cited here for
   the historical fact this paper's Origin section rests on, not
   re-derived.
2. Wiener, M. J. (1990). *Cryptanalysis of Short RSA Secret Exponents.*
   IEEE Transactions on Information Theory, 36(3), 553–558. §1's
   instance 2 (`op_wiener`) is this attack, ported and cited, not
   reinvented.

## TODO

- [x] Run the actual Weyl-shaped test that the Schwarzian check didn't.
      **Done 2026-09-21** — `ValaQuenta/modules/prime_gauge_field/`
      (`Ainulindale/wiki/122_the_prime_gauge_field.md`). Two connections
      built directly from `Γ`: `A=∇(log|Γ|)` (provably flat for any
      holomorphic scalar, Poincaré lemma — not Γ-specific) and
      `A=(Re Γ, Im Γ)` read as a genuine `ℝ²` 1-form, not a gradient
      (this one carries real curvature, `F(s)=2·Im(Γ'(s))`, exact,
      verified against finite differences to `~1e-11`).

      **Pre-registered prediction, stated before the test was run:** the
      connection's flat locus is the trivial/identity member of the
      SCALE family — the vacuum of the construction, not a generic
      point of it.

      **Result: half right, reported as such rather than upgraded.**
      `F(s)=0` exactly on the real axis (`Γ` real-valued — a defensible
      "trivial phase" reading, matches) **and** on `σ=−1` (`Γ`'s own
      pole line — not predicted, a genuine new feature, kept separate
      from the confirmed half rather than folded in after the fact).
      Checked on 2000 random points, 0 mismatches — the zero locus is
      exactly these two lines and nothing else.
- [ ] State the falsifier's exact test procedure (a candidate structure
      + a checklist for "does its cheap case reduce to representation-
      linearization").
- [ ] Identify the engine — likely a small harness that runs all three
      checked instances (§1–3) and reports the same diagnostic across
      each, rather than three separate scripts. `ValaQuenta/modules/
      prime_gauge_field/` now covers instance 3 (`Γ`) on its own; the
      unifying harness across all three is still open.
- [ ] Notebooks: one per instance (arithmetic, Wiener, `Γ`), each ending
      in the same "representation vs. search" readout. `Γ`'s notebook
      done: `ValaQuenta/notebooks/engines/20_prime_gauge_field.ipynb`.
      Arithmetic and Wiener notebooks still open (their toolset-level
      `verify()` calls exist; a dedicated notebook each does not yet).
- [x] Fold in the gauge-curvature negative result from the origin
      experiment honestly. **Done** — `prime_gauge_field`'s own
      `log_potential_curvature()` reproduces and generalizes the flat
      result explicitly, in the same engine as the positive one, rather
      than letting the positive result quietly replace it.
- [ ] Licensing section (see `ScalarContextPropagation/README.md §15`
      for the pattern).
- [ ] Wiki page (written last, per convention).
