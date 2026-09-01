# The d* Renormalization Group

## The Cayley–Dickson Tower as a Wilsonian RG, and d*_RG as Its Fixed Point

**Fourth Age Paper.** One Paper. One Structure. One Engine. One Wiki.
**Author:** Cody Michael Allison <the.wandering.god@gmail.com>
**Registered:** 2026-08-31

---

## The departure from the template

Every other Fourth Age Paper is *One Paper, One Claim* — a falsifiable
prediction the engine tests. **This one has no claim and no prediction.** It
is an **engineering structure**, and `d*_RG` is a **given**: "The Stability,"
one of the four canonical faces of `d*` (Ainulindale README §8), the
renormalization-group fixed point of the Cayley–Dickson tower iteration —
already named, already load-bearing, still open in closed form.

What this paper delivers is the **engine protocol**: how `d*_RG` is
structured, how the RG that produces it runs, and where renormalization sits —
which is *inside the machine, not in a move the operator makes*. This is
engineering, not mathematics. Every component carries a provenance label:
`ESTABLISHED` with an attribution, or `FIRST STATED HERE` with a date.

---

## 1. What d*_RG is (structure)

`d*_RG` is **The Stability** — the centre of the `radial complex spherical
ln(10)` chart, the point the flow returns to (0_RB, the Oblique-Gear axis).
It has two readings, and they are one object:

- **as a value:** `≈ 0.24631` — a shadow of `d*`, and self-consistent with the
  Translator face: `d*_RG · ln(10) → Ω_ZS = 0.56714`.
- **as a dimension:** **8** — the persistent octonion. The CD-tower RG flow
  converges dimensionally to the 8-DOF core that keeps gain exactly 1 at every
  scale (`persist ≡ 8` at d = 8, 16, 32, 64; `void = (d−8)/2`; `8/d → 0`).
  The fixed point is **dimensional, not fractional** (`.clauderc_user`
  provenance, 2026-08-20).

**OPEN:** there is no closed form `d*_RG = f(Ω_ZS, …)`. You obtain it by
**iterating the tower to convergence.** That openness is the reason
[[No Renormalization]] is a standing rule — hand-applying a second RG buries
the evidence that would close it.

---

## 2. How it works (the RG)

**The Cayley–Dickson doubling IS the Wilson RG step.** Block → integrate out →
rescale, one CD level per pass:

| Wilson RG | CD tower |
|---|---|
| block transform | `(a,b)·(c,d) = (ac − d̄b, da + bc̄)` — double `d → 2d` |
| relevant vs irrelevant modes | **persistent** (gain exactly 1 — the octonion core, the two indices `e₀`, `e_{d/2}` in no zero-divisor plane, Boundary Lever) vs **void** ((2d−8)/2 modes) |
| integrate out the irrelevant | **project onto the persistent 8**, carrying the complex phase — never `|z|²`, the one step with no adjoint (Standing Directive) |
| rescale to the fixed block size | divide the radial coordinate by the flow unit `d*_taut = Ω_ZS/ln(10)` so the core sits at the same `r` each pass |
| iterate to the fixed point | repeat until `|Δd*| < tol` → `d*_RG` |

**The flow is a saddle at σ = ½.** The Oblique-Gear measurement (T7,
`project_oblique_gear`) gives a positive Lyapunov exponent `λ ≈ 6` off
balance: a generic state flows *into* σ = ½, but exactly on it any
perturbation grows. So the protocol must **approach along the stable
manifold** — balance the tilt (`Σ tilt → 0`) at every pass, or the iteration
diverges instead of converging.

---

## 3. How renormalization is built in

It is not *applied*. **The tower is the RG transformation.** The void is
**projected out** — an exact resummation onto the persistent core, phase
carried — never **subtracted**. There is no counterterm, no discarded
infinity. The nat budget balances at every pass (this is checkable — G5).

That is the [[No Renormalization]] rule stated as an engineering constraint:
the engine renormalizes *by construction*, so the operator never adds a
second, hand-applied one. `d*_RG` is what the built-in RG converges to;
anything you subtract by hand is contamination of that limit.

---

## 4. The full engine protocol

```
INPUT   seed operator x₀ ∈ CD algebra at dimension d₀ (default 𝕆, d₀ = 8),
        in radial-complex-spherical-ln(10) coordinates
        max dimension D (default 256), tolerance ε (default 1e-9)

STATE   (x, d, r_scale, history[])

RG STEP  (one pass)
  a. DOUBLE      x ← CD_double(x);  d ← 2d
  b. CLASSIFY    for each of the 2d basis directions, gain g_k under the
                 doubled product:
                   persistent  = { k : |g_k − 1| < ε_gain }   (expect the 8-core)
                   void        = the remaining (2d − 8)/2 pairs
  c. BALANCE     rotate each ⊕4 pair to drive Σ tilt → 0  (stable-manifold
                 approach; Oblique-Gear T6 construction)
  d. PROJECT     x ← Π_persistent(x)   — project onto the 8-core, CARRY PHASE
                 (no |z|²);  assert Σ nats(x_before) = Σ nats(x_after)  (G5)
  e. RESCALE     r_scale ← r_scale / d*_taut ;  x ← x · r_scale
  f. RECORD      d*_k ← d* evaluated on the rescaled core;  history.append(d*_k)

LOOP    repeat RG STEP until |d*_k − d*_{k-1}| < ε  OR  d > D
        → d*_RG := lim d*_k

FIXED-POINT CHECKS
  • dimensional:  |persistent| = 8 at every pass
  • self-consistency:  |d*_RG · ln(10) − Ω_ZS| < tol_Ω
  • approach exponent:  fit |d*_k − d*_RG| ~ e^{−λ' k};  λ' matches the
    Oblique-Gear λ ≈ 6 (same saddle)
  • semigroup:  two RG steps ≡ one CD double-step composed with one rescale²
  • determinism:  SHA-256 of history[] reproduces across machines

OUTPUT  d*_RG,  history[] (the flow trajectory),  the persistent-core basis
        at each scale,  λ',  the nat-budget ledger
```

---

## 5. Components

| id | name | tier | provenance | status |
|---|---|---|---|---|
| C1 | CD doubler `(a,b)(c,d) = (ac − d̄b, da + bc̄)` | 0 | ESTABLISHED (Cayley 1845, Dickson 1919) | ships (`monad.py::_smul` recursion) |
| C2 | persistent / void classifier (gain-1 core vs shed modes) | 1 | ESTABLISHED Boundary Lever (`e₀`, `e_{d/2}` the two non-ZD indices, dim ≥ 16); **RG relevant/irrelevant reading FIRST STATED HERE 2026-08-31** | partial |
| C3 | phase-carrying projector `Π_persistent` | 1 | Standing Directive (never `\|z\|²`) | to write |
| C4 | rescale by `d*_taut = Ω_ZS/ln(10)` | 0 | `d*_taut` ESTABLISHED (Ainulindale §8); **rescale-role FIRST STATED HERE 2026-08-31** | to write |
| C5 | fixed-point loop | — | ESTABLISHED (Wilson 1971, Kadanoff 1966) | to write |
| C6 | stable-manifold approach (balance `Σ tilt → 0` per pass) | 2 | **FIRST STATED HERE 2026-08-31** (from `project_oblique_gear` T6/T7, λ ≈ 6 saddle) | to write |
| C7 | self-consistency `d*_RG · ln(10) → Ω_ZS` | — | ESTABLISHED (the Translator face) | check |
| C8 | nat-budget ledger (projection is resummation, not subtraction) | — | **FIRST STATED HERE 2026-08-31** ([[No Renormalization]] as engineering constraint) | to write |

---

## 6. Engine

`engine/d_star_rg.py` — **v0, runs.** CD doubler + classifier + phase-carrying
projector + rescaler + fixed-point loop + the checks. Deterministic; 5 seeds;
17 doubling passes to `d = 2²⁰`. Run under `ValaQuenta/.venv/bin/python3`.
Output: `engine/d_star_rg_output.txt`.

---

## 7. Results

| quantity | result |
|---|---|
| **dimensional fixed point** | **CONFIRMED** — persistent core = **8** at every pass, every seed, to `d = 2²⁰`. `dim_ratio = 8/d → 0` exact (7.6×10⁻⁶ at `d = 2²⁰`). `.clauderc` provenance's "persist ≡ 8" — now run, not asserted. |
| **nat budget** (G5) | balanced every pass — `‖core‖² + ‖void‖² = ‖x‖²` asserted, never broke. The projection is a **resummation, not a subtraction**. |
| **determinism** (G4/G6) | `SHA-256(trajectories)` reproducible: `c68fa38d…` |
| **numerical `d*_RG`** | **OPEN — and the engine localises the openness.** A naive iteration, with the old↔new coupling carried as a *summary scalar* of the state, flows to the **trivial fixed point** (`relevant_fraction → 1`, `void_coupling → 0`). The non-trivial value needs the coupling evolved by the **actual CD product** — a data structure, not a number. That is the open part, now pinpointed. |
| `entropy_ratio` limit | 0.6025 ± 0.0540 — the only non-trivial converging observable; within ≈ 1σ of `Ω_ZS = 0.5671`, **not tight**. Logged, not claimed. |
| self-consistency `d*_RG·ln10 → Ω_ZS` (C7) | **not met** — there is no converged `d*_RG` to test. |
| approach exponent `λ′` (C-check) | **n/a** — the trivial fixed point is reached instantly; no approach curve to fit. |

**What the engine settles:** the *dimensional* half of `d*_RG` (= 8, exact,
robust). **What it leaves open:** the *numerical* half (= 0.24631), and it
says precisely why — a scalar coupling is not enough; the RG needs the whole
CD product carried through. Consistent with `d*_RG` being an OPEN derivation
across the framework.

---

## 8. Number-theory framing

The CD doubling is `(ℤ/2)ⁿ` acting by XOR on `2ⁿ` basis indices — the
permutation ladder of §2. The RG's **relevant sector is the persistent
octonion**: `e₀` (the real / Telperion axis) plus the seven imaginary
directions **in no zero-divisor plane**. That is the *"just primes" ground
state* of the un-sieve made algebraic — the irreducible sector, the part a
zero-divisor product can never reach. The **void** `= d − 8` is the composite
sector (everything a ZD product hits), and `void/d → 1` exactly as
`π(x)/x → 0`: composites swamp primes, primes are the fixed 8.

`d*` is "the boundary below which no algebraic definition can occur" — the
prime-desert floor. `d*_RG` as this flow's fixed point says: **the smallest
natural unit is what the doubling cannot decimate — the 8-core.** The number
`0.24631 = Ω_ZS/ln 10` is the self-consistency target (the Lambert-W entropic
ceiling); the gap to the *measured* `d*_spec ≈ 0.24600` is the Yang–Mills
mass-gap analogue `≈ 0.000707`. The engine confirms the 8; it does not close
the 0.24631 — and neither does anything else in the framework yet.

Windows of order in a bifurcation diagram are Feigenbaum RG fixed points
(`HyperBifurcation`); `d*_RG` is the Cayley–Dickson analogue — the largest
bubble of order, the prime sector, floating in the zero-divisor chaos.

---

## 9. CS framing

This is **the renormalization group as a lossless coarse-graining
algorithm**: block-decimate the CD algebra (`d → 2d`), keep the relevant 8,
rescale, repeat — and *nothing is dropped*. The per-pass assertion
`‖core‖² + ‖void‖² = ‖x‖²` is the machine-checkable form of "renormalization
is the machine, not a move": the projection is an **exact resummation**
(a pushforward onto the stored 8-core), not a subtraction of a counterterm.
Lossy compression discards; hand-renormalisation subtracts; this balances the
ledger.

Cost: `O(d)` per pass, `O(log D)` passes → `O(D)` to reach dimension `D` — a
**forward-propagating** algorithm (`feedback_forward_propagating_maths`): the
state is pushed through a fixed map, no search, no gradient sweep; the fixed
point is where the pushforward stops moving.

The engine's honest failure is itself a CS result: **a scalar coupling flows
to the trivial fixed point.** The non-trivial `d*_RG` needs the coupling
carried by the full CD product — a structure, not a number. Same lesson as
the semantic-hash round trip and the tape argument: the content is in the
structure you keep, not the scalar you summarise it with. Determinism
(`SHA-256` of the trajectories, reproducible across machines) makes the flow
a pure function — the RG is a deterministic dynamical system, byte-for-byte
replayable (G4/G6).

---

## 10. The desk-rejection gate

| id | reject | test |
|---|---|---|
| G1 | "RG of *what*? Show a fixed point on real iteration." | run the engine from ≥ 3 seeds; report `history[]` and that `d*_k` converges to one `d*_RG` within `ε` |
| G2 | "The CD tower is not an RG." | exhibit block (C1) + integrate-out (C2–C3) + rescale (C4); verify the **semigroup property** — two passes compose to one double-step + rescale² |
| G3 | "`d*_RG` is just `Ω_ζΣ / ln(10)` renamed." | no: it is the **limit of an iteration** (closed form OPEN), and it is **dimensionally 8**. Report the trajectory `d*_k` *approaching* the value — a renamed constant has no approach curve |
| G4 | "Determinism." | SHA-256 of `history[]`, twice, two machines, matches |
| G5 | "You renormalized by hand." | the projector Π is a **resummation onto the 8-core, not a subtraction**. Report the nat-budget ledger: `Σ nats` in = `Σ nats` out at every pass, no counterterm |
| G6 | "Runs only on the author's machine." | `run.sh` from a clean checkout: pinned deps, `d*_RG` + trajectory + `λ'` out the other end |
| G7 | Attribution | Wilson / Kadanoff own the RG; Cayley / Dickson own the doubling; Boundary Lever owns the two non-ZD indices; the Oblique-Gear paper owns the saddle. The **identification of the CD tower as the RG** and **`d*_RG` as its fixed point** are marked first-stated-here |

**No σ-verification** — deliberate. There is no critical-line / Ainulindale-
constant claim to check; the structure stands on the Wilson RG, the CD tower,
and a converging iteration.

---

## Conclusion

Decomposed against the operation domain, the verdict is **no new generator**.
The CD doubling is tier-0 (ADD ∘ SCALE ∘ SIGN); the block/integrate/rescale
loop is the Wilson RG unchanged; the projection is a resummation. What is
first-stated-here is the **identification**: the Cayley–Dickson tower *is* a
Wilsonian renormalization group, its relevant sector is the persistent
octonion, and its fixed point is `d*_RG` — dimensionally 8, numerically
`0.24631`, closed form open.

Renormalization is the machine, not a move. `d*_RG` is where the machine
settles. You do not renormalize onto it — you iterate, on the stable
manifold, and read the limit.

---

## Relation to the series

- **The Oblique Gear** (`project_oblique_gear`) — the σ=½ saddle and `λ ≈ 6`;
  the stable-manifold approach C6 is that result applied.
- **Boundary Lever** — the two indices `e₀`, `e_{d/2}` in no zero-divisor
  plane are the RG's fixed relevant directions.
- **Scalar Context Propagation** — the sister engineering-structure paper
  (no claim, provenance-labelled, desk-rejection gate).
- **Yang-Mills Mass Gap** — `|d*_spec · ln(10) − Ω_ZS| = 0.000707` is the gap
  between the *measured* fifth d* and this engine's *converged* fourth.
- **Cavitation Cascade** — the Big Bang as a phase transition at σ=½; this
  engine is the RG flow into that transition.
