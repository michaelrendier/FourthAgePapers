# The Birth of Chirality and the Nature of a Black Hole

**Status: TODO — stub.** Started 2026-09-25. **Scope, set by Cody the same
day: short paper, no branch — stays on `main`. The content is the
mechanism, demonstrated in code. That's it.** Not a GR treatise, not an
extended prose argument — the claim below is either shown running in code
or the paper isn't done. Per the FourthAgePapers rule, work happens in the
engine first; this file grows only as far as that work justifies.

---

## Provenance note

Unlike `HyperindexingSystem/`, this one is not being fitted onto six-week-old
prior work — it's born directly from tonight's conversation (2026-09-25),
built on material established across this session and already on record
elsewhere, not invented for the paper. Two separate, already-existing
threads converge here for the first time as one claim:

1. `box_kite.md` / the Unified Chainmaille Theory work: **"chirality =
   parity-of-order-count."** Already established, predates tonight.
2. This session's own Schwarzschild `g_tt = −f(r)`, `g_rr = 1/f(r)`
   reciprocal-boundary derivation, and the `ADD:SCALE:SIGN` datatype's
   `SIGN = g ∈ {−1,+1}`, `det ±1` — already established as this
   framework's own name for the parity/chirality bit, also predating
   tonight.

The paper's contribution is showing these are the same fact, not two
facts that happen to rhyme.

## One Claim

A single order-transposition — the numerator/denominator role-swap at a
Schwarzschild horizon (`r` and `t` exchanging which one is timelike) — is,
by definition, an odd-parity operation, and odd parity is what orientation-
reversal (chirality) *is*, not merely correlates with. The horizon swap is
a `SIGN` flip in this framework's own tier-0 vocabulary, not analogous to
one. Separately, and prior to any horizon or any dynamics: the octonion
multiplication underlying `PSL(2,7)`/the box-kite structure already
requires choosing an orientation on the Fano plane's seven lines — a
static chirality decision baked into the algebra before any black hole,
any swap, or any collapse exists. The dynamical birth (at a horizon) and
the static birth (in the algebra's own foundation) are the same fact
appearing twice, not two separate sources of handedness.

A further, more exact statement follows from the same mechanism, and is
part of the claim, not decoration: inside a Schwarzschild horizon `r`
becomes the timelike coordinate, so the singularity `r=0` is not a
location any infalling worldline arrives at — it is a future moment every
such worldline's causal structure already contains. "A black hole isn't
an object, it's a future time" (Cody, 2026-09-25) is the plain-language
statement of this, and it is standard GR, not a metaphor, once the role-
swap is taken to its actual conclusion instead of stopped at "the
coordinates exchange."

## One Prediction (Ptolemy/0_RB)

Pending — not yet run.

## One Engine

Not yet built. Candidate components, all already-existing, none yet wired
together for this specific claim:
- `ValaQuenta/modules/box_kite/maths.py`: `fano_planes()`, `associator`/
  `associator_defect` (the curvature/parity-sensitive quantities),
  `psl27_order()`.
- This session's Schwarzschild `g_tt`/`g_rr` reciprocal derivation
  (conversation-only so far, not yet in a file — needs a home, likely a
  new module or an extension of `box_kite/maths.py` rather than a new
  repo-wide engine).
- `ValaQuenta/modules/add_scale_sign/maths.py`: `ASS.SIGN`, `firing_defect()`
  — the existing formal treatment of the parity bit this claim leans on.

Open engineering question, first thing to actually build: a function that
takes the Fano-plane orientation choice and the opposite one, and verifies
directly (not by argument) that the resulting octonion multiplication
tables are related by conjugation and are not obtainable from one another
without an odd number of line-orientation flips — the concrete, checkable
form of "the algebra's chirality is a choice," rather than asserting it.

## One Wiki

Not written yet — last, per the rule.
