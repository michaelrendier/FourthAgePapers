# Crawford / Navier–Stokes — The Laplacian Tail

**Companion to** `00_holcus_vision.md`. Full treatment:
`Ainulindale/wiki/106_the_navier_stokes_problem.md` §"The Laplacian tail".
**Status: THEORETICAL.** A structural note on *where* a singularity's
information can and cannot live. Not a regularity proof.

---

## The pressure Laplacian is pathway-defined

NS carries a Laplacian slaved to the flow — the pressure Poisson equation

    ∇²p = −∂_i ∂_j (u_i u_j)

A *generalized* Laplacian structures continuity with no preferred route. This
one is *pathway-defined*: its source is the velocity pathway, so it grows an
unbroken curve along the flow (the Lichtenberg / dielectric-breakdown reading).
On a genus-1 boundary that curve threads the hole and closes.

## The tail = the timing gear

Model the curve as a chain of circles, one per scale, of different orders of
size (a Doyle-spiral / RG ladder). The last seven, descending toward the
crisis, are the timing gear — **d\* first, Lambert W last**:

1. d\*  — The Boundary      (σ=½ spectral coordinate; the fold opens)
2. d\*_RG — The Stability   (CD-tower RG fixed point; dimensionally 8; OPEN)
3. d\*_taut — The Flow      (Ω_ZS / ln 10)
4. d\*_ln(10) — The Translator  (d\*·ln 10 = Ω_ZS — the seam)
5–7. W — the three rotor faces of Ω_ZS = W(1)  (Wankel trine: intake / power / exhaust; the crisis closes)

d\* = catastrophe (the fold, where a definition first becomes possible).
Lambert W = crisis (where order dissolves into the bulk). The `4 : 3` is the
*phase* relationship — `lcm(4,3) = 12`, the camshaft-free `H = xp` precession —
not the linear layout.

## Order-blind to history, order-rigid internally

- **Order-blind to history.** Like the inertial range (`k^{-5/3}`, universal),
  the tail is a fixed point: it forgets the large-scale forcing and the route
  taken to reach it.
- **Order-rigid internally.** `gcd(4,3) = 1` → exactly one cyclic order that
  never repeats a phase before twelve steps. Permutation-locked.

An order-blind, order-rigid structure carries a **clock, not a coordinate**. It
is identical for every flow, so it cannot hold the flow-specific information a
finite-time singularity would need. That information lives in the **head** — the
large scales, the order-*sensitive* region (the analogue of the erased
coordinate in the factoring pathway). A blow-up would have to be seeded there
and then survive the cascade; the order-rigid cascade smears it — the
`θ → θ + π/2` rotation into the Blue channel that `R̂† = B̂` guarantees,
recoupled by the halocline operator `∂̂_∂M`.

**The tail regularises because it is a checksum, not a message.** Consistent
with the CONFOUND verdict: the blow-up is a coordinate artefact of reading an
order-blind clock as an unbounded length.

## Crawford's data

Crawford's turbulence sections (the 254 model breaks) are records of the *head*
losing its grip — the large-scale PV conservation failing as the flow goes
genuinely 3D. The framework's claim is that the small-scale tail past that
break is not where new information enters; it is where the dropped vertical
(imaginary) component would rotate the apparent divergence into a bounded
orbit. The model problem in `00_holcus_vision.md` §"What a first pass needs"
is the place to measure it.
