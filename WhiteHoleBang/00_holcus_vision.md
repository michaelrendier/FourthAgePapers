# 00 — Vision: the White-Hole Bang

**Skeleton.** The question, the shape of the claim, and — as loudly as the
claim — what this paper does *not* say.

---

## The question

A black hole has a finite lifetime. The textbook end is a Planck-mass remnant
or nothing at all. This paper asks: **is the end an event instead of a
vanishing** — and if so, what does the event produce?

Cody's answer, which is the claim under test:

> black hole → white hole → gravastar → de Sitter space → **BANG**

driven by **evaporation → unwrapping → uncompressing**, and triggered not at
`m → 0` but at the **deconfinement mass** `M_dec` where the interior
quark–gluon plasma can no longer be held.

## The three moving parts

1. **It never got stiff.** Stiff matter (`p = ρc²`, sound speed `= c`,
   Zel'dovich) is the hardest equation of state there is. A black hole's mean
   interior density is `ρ̄ ∝ M⁻²`; only very small holes approach stiff /
   Planck density. A heavy hole's core can sit at quark–gluon-plasma density
   — deconfined, hot, but **soft compared to stiff** — carrying the MIT-bag
   pressure `B ≈ (145–235 MeV)⁴` as a floor that never got crushed out.

2. **Evaporation weakens the cage.** Hawking loss shrinks the hole and, with
   it, the gravitational binding that confines the plasma. When the binding
   energy density falls to `B`, the bag pressure wins and the core expands —
   **uncompresses**. `M_dec` is that balance point.

3. **Black and white are one object.** The infalling face (`I`) and the
   outrushing face (`O`) are the two readings of the same event through
   `L_(I|O)`. The Bang's light is collimated — it leaves the way the matter
   came in — because the boundary crossing is one-way (`Ainulindale/wiki/90`).

4. **The boundary is exactly flat.** The junction surface — interior to
   exterior, the photon sphere, the `b = a` lemniscate crossing — is the
   locus where the effective curvature invariant is **exactly zero**. The
   tangent cone at the node is two straight lines (the hard cross); `π` is
   its constant (`Ainulindale/wiki/22`); it is the conformal boundary
   `sc = 1.0`. A flat seam does not lens the outgoing beam — which is why the
   Bang stays collimated. Committed as **P5**; falsified if the model's
   zero-curvature locus and the photon sphere do not coincide.

## The timescale reading

"...over a trillion-year lifetime" is **ambiguous** and is resolved here as:
the **trillion years is post-Bang** — the age of the pocket cosmos we are
asked to describe — **not** the pre-Bang evaporation time.

Standard Hawking gives `t_evap ∝ M³`, so a `20 M☉` hole takes `≳ 10⁶⁶ yr` to
reach any `M_dec` of order `10 M☉`. If the engine (step 3) finds a trigger
that fires much earlier, that is a **result**, flagged as such — it is not
assumed here.

## What this paper does NOT claim

- **Not** that our universe is a white-hole Bang. This is *just the black
  hole.* The CMB appears only as the one explosion of this class we can
  measure — a yardstick, not an identification.
- **Not** a resolution of the singularity. There is no field equation for the
  bounce here; the uncompression is a pressure-balance argument (`B` vs
  gravitational binding) and nothing more.
- **Not** a new quantum-gravity model. The lemniscate / saddle machinery is
  used as the *description* of the crossing (order parameter `b/a`,
  separatrix at `b = a` = the photon sphere, hard node at `σ = ½`), not as a
  derivation of GR from something deeper.
- **Not** a statement about information, observers, or meaning.

## Out of scope

- The exterior spacetime and any second observer. One hole, isolated.
- The pre-collapse stellar history that made the hole.
- The bitwise Cayley–Dickson question — parked for the engine's fast path.
- Any claim that depends on a number this skeleton has not yet computed.

## What the next passes do

- **Step 3** — build `engine/`: a proper-time integrator, 6-place fixed
  precision, fast inverse square root, that walks `τ` from a chosen `M₀`
  through evaporation, deconfinement, uncompression and the Bang, and keeps
  the clock so the event can be resolved finely.
- **Step 1** — run it at several `M₀` (stellar / intermediate / supermassive)
  and compare the relic spectra and energy budgets to each other and to the
  CMB; fill `02_data` and `03_results`; write the wiki page last.
