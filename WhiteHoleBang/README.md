# White-Hole Bang

**Fourth Age Paper — SKELETON.** One Paper. One Claim. One Engine. One Wiki.

Adjacent to `DeSitterCavitation/` (the *static* "no-singularity" core). This
paper is the **terminal event**: what the core does when the hole runs out of
lifetime.

Status: skeleton only (2026-09-01). Claim + falsifier + predictions
committed here; the integrator engine and the multi-scale simulations come
next (build order 2 → 3 → 1).

---

## The Claim

> **A black hole does not evaporate to nothing.**
>
> Hawking radiation removes mass until gravity can no longer confine the
> interior **quark–gluon plasma** — which never compressed to stiff matter
> (`p = ρc²`) because the hole was too massive to need that density. At that
> point the interior **uncompresses**: black → white, the input and output
> faces of **one** object — the I/O of a universe (`L_(I|O)`). The previously
> ingested spacetime and matter are released as a **de Sitter Bang** inside
> the photon sphere, radiating collimated along the boundary-crossing
> direction.
>
> The explosion's scale is set by the **deconfinement mass**, not by
> `m → 0`; its relic spectrum is CMB-shaped.

Cody, 2026-09-01:

> *"the end lifetime of a black hole → white hole → gravastar → de Sitter
> space BANG because it still contains its quark-gluon-plasma (still too big
> for stiff matter) and releases the previously ingested spacetime and matter
> into an explosion that we don't have a scale for without looking at the
> CMB. It is one. it's I/O of the universe… black → white. that's my claim.
> evaporation → unwrapping → uncompressing (math corrected)… what would that
> explosion of a higher-mass stellar-mass black hole create over a
> trillion-year lifetime…"*

**Falsifier:** an isolated black-hole interior that reaches stiff-matter
(Zel'dovich) density **before** evaporation removes enough mass to break
confinement — i.e. the plasma settles into a stable stiff / Planck core and
there is nothing left to uncompress. Equivalently: if the deconfinement mass
`M_dec` comes out **below** the Planck remnant scale, evaporation genuinely
ends first and the claim is dead.

---

## The process (math-corrected)

    evaporation   →   unwrapping   →   uncompressing   →   Bang
    ───────────       ───────────      ─────────────       ────────────
    Hawking mass      b/a → 1          QGP bag pressure    de Sitter phase
    loss; R_s, then   the lemniscate   exceeds the         released inside
    the confining     separatrix       gravitational       the photon sphere
    binding, fall     crossing         binding; the core   r = 3GM/c²;
    toward M_dec      at σ = ½         expands             collimated

Each arrow is a segment of the lemniscate / saddle machinery:
`b/a` is the order parameter (Cassini `|z−a||z+a| = b²`), `b = a` is the
separatrix at the saddle value = the photon sphere, and the crossing is the
hard node — the one-way portal (`Ainulindale/wiki/90`, two struts meet in one
point, one-way; `Ainulindale/wiki/108`, `Ainulindale/wiki/110`). "Black" is
the `I` face, "white" the `O` face, of the same event read the two ways
(`L_(I|O)`; `ValaQuenta` `fixed_point`, the inside-out horizon;
`Ainulindale/wiki/31`, BH = cavitation scar, white hole = 1 Planck sec).

### The boundary is exactly flat

The matching surface — interior de Sitter to exterior Schwarzschild, the
photon sphere, the `b = a` lemniscate crossing — is **exactly flat**: the
effective curvature invariant passes through **zero** there, not merely
through a small value. The tangent cone at the lemniscate node is a pair of
**straight lines** (the hard cross, transversal at exactly 90°), `π` is the
constant of that flat boundary (`Ainulindale/wiki/22`), and it is the
conformal boundary `sc = 1.0`. This is a claim about the model's junction,
not about bare Schwarzschild (whose Kretschmann scalar at `r = 3M` is
nonzero) — and it is what lets the Bang leave **collimated**: a flat seam
does not lens the outgoing beam. Committed as **P5**.

---

## Why quark–gluon plasma, not stiff matter

Mean interior density `ρ̄ ~ M / R_s³ ∝ M⁻²` (geometrized): a `10 M☉` hole
averages roughly nuclear density; a `10⁸ M☉` hole, less than water. Collapse
does **not** imply Planck density everywhere. The core can hold at QGP
density (`~10¹⁷–10¹⁹ kg/m³`, `T ~ 10¹² K`) — deconfined but **not stiff** —
with a real pressure floor: the MIT-bag vacuum pressure
`B ≈ (145–235 MeV)⁴`. The more massive the hole, the further its core sits
from stiff matter, and the more uncompression energy is banked. This is the
load-bearing premise, and the falsifier attacks it directly.

---

## The question this paper answers

What does the terminal explosion of a **higher-than-stellar-mass** black hole
(`M₀ ≳ 10 M☉`) produce — energy budget, timescale, spectrum — and what does
the resulting pocket cosmos look like **a trillion years after** the Bang?
Compared point-for-point against the CMB, the only explosion of this class we
can observe.

*(Note the timescale ambiguity, resolved in `00_holcus_vision`: "trillion-year
lifetime" is read as the post-Bang evolution time, not the pre-Bang Page
time — standard Hawking gives `≫ 10⁶⁶ yr` to reach `M_dec`, which the engine
will either confirm or overturn.)*

---

## Notebooks

| | |
|---|---|
| `00_holcus_vision.md` | the claim, what it does **not** claim, out of scope, the QGP-vs-stiff argument, the timescale reading |
| `01_predictions.md`   | P1–P5, structural now, committed as quantitative ranges when the engine is built — before any deciding data is read |
| `02_data.md`          | reference observations — CMB spectrum + dipole, QGP/bag EOS, the Page curve — labelled as reference, **not** tests |
| `03_results.md`       | the scorecard, failures read honestly |

## Engine

`WhiteHoleBang/engine/` — the proper-time integrator (to be built, step 3):
tracks `τ` through evaporation → deconfinement → uncompression → Bang at
**6-place fixed precision** (skips the float-accumulation problem by fiat;
also makes every `√` eligible for fast inverse square root), keeps time so
the event can be "tuned in" at depth. Multi-scale runs (stellar / intermediate
/ supermassive `M₀`) for comparison come after it runs clean (step 1).
Borrows the Cayley–Dickson table from `ValaQuenta/modules/box_kite/`.

## Out of scope

- Whether **our** universe is such an event. This paper is *just the black
  hole* — not the universe around it. The CMB is used only as a calibrated
  yardstick.
- A quantum-gravity mechanism for the bounce. The claim is an
  equation-of-state / pressure-balance argument, not a resolved singularity.
- The bitwise-tower question ("can every Cayley–Dickson level be written as a
  bitwise op for overhead reduction") — the index is `i XOR j` and the sign
  is a bitwise recurrence; noted for the engine's fast path, investigated
  separately, not in this paper.

## Open

- **No bounce mechanism is derived** — the uncompression is argued from
  `B` vs gravitational binding, not from a field equation.
- `M_dec` depends on `B^{1/4}` to the first power under a square root; the
  `145–235 MeV` spread propagates to a factor `~2.6` in `M_dec`.
- The collimation prediction (P4) has no first-principles angular
  distribution yet — only "not isotropic."
- Whether the released spectrum is Planckian out of the box or only after
  the expansion factor is applied (P3).
