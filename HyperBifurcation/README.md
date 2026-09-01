# Hyper-Bifurcation

## Windows of Order as Renormalization Fixed Points, the 3-D Bifurcation Beyond the Logistic Slice, and Reading Modulus Factors as Order-Bubbles in Un-Sieve Space

**Fourth Age Paper.** One Paper. One Structure. One Engine. One Wiki.
**Author:** Cody Michael Allison <the.wandering.god@gmail.com>
**Registered:** 2026-08-31
**Sibling engine:** `FourthAgePapers/DStarRG/` — the same renormalization,
CD-tower version.

---

## The departure from the template

No claim, no prediction. **Engineering structure.** The *given*: **working
mathematics lives in the windows of order** — the periodic bubbles floating in
the chaotic region of a bifurcation diagram. Chaos is the medium; the bubbles
are shaped by it, almost buoyantly. This paper delivers the engine that
catalogues them, lifts the diagram out of its 2-D slice, and reads a modulus'
factors as the order-bubble it is born into.

Every component carries `ESTABLISHED` (with attribution) or `FIRST STATED HERE`
(with date).

---

## 1. Windows of order ARE renormalization (the given)

The periodic windows in a chaotic bifurcation diagram — the period-3 window at
r ≈ 3.8284 and its entire self-similar family — are **Feigenbaum
renormalization fixed points**. The renormalization operator

```
R[f](x) = α · f(f(x/α)) ,    α ≈ 2.5029 ,   δ ≈ 4.6692
```

has the Feigenbaum function as its fixed point; every window is a rescaled copy
of the whole cascade under iterates of `R`. `d*_RG` (`DStarRG/`) is the
Cayley–Dickson analogue of that fixed point. So: *a window of order is a place
the renormalization has already run to its fixed point.* That is why usable
maths lives there — outside the windows the flow has not converged.

`ESTABLISHED`: Feigenbaum (1978), May (1976), Coullet–Tresser (1978),
Sharkovskii (1964), Mandelbrot (1980).

---

## 2. Buoyancy and wake

The bubbles **rise** — the RG flow carries order-regions toward the fixed
point, which is "up." Buoyancy is displacement, and displacement has a
**return path: a wake.** The disorder the bubble pushes aside flows back down
around it.

| rising bubble | returning wake |
|---|---|
| RG flow to the fixed point | the crisis / Lyapunov sign-flip boundary around the window |
| Noether current (up the tower) | Noether Information current (down) |
| the Oblique-Gear precession (the flower) | its retrograde component — "destructive interference ringing backwards" |

**The wake is often the readable part.** A ship's wake is visible from far
beyond the ship. `FIRST STATED HERE 2026-08-31`: a window's wake carries the
same RG level as the window and can be detected in the parameter/phase space
*adjacent* to it, without landing inside.

---

## 3. The 3-D bifurcation (beyond the slice)

The logistic diagram `x* vs r` is a **2-D slice** — it shows *one ordering* of
the windows. The real object has more layers. Third axes, any of which the
engine can take:

- **second map parameter** `x → r·x(1−x) + s·g(x)` — the windows become 2-D
  regions; sweeping `s` shows how the window ordering rotates and reconnects.
- **CD-tower rung** — the bifurcation diagram computed over ℝ, ℂ, ℍ, 𝕆, 𝕊,
  stacked; how the window structure changes as `d*_RG`'s RG climbs.
- **un-sieve generation** `π(gpf)` — the birth-order axis (§4).
- **`Im(c)`** — the real logistic bifurcation is the `Im(c)=0` slice of the
  Mandelbrot set; the Mandelbrot set is itself a slice of the hypercomplex
  parameter space.

`FIRST STATED HERE`: tracking **how window orderings reconnect across slices**
is the hyper-bifurcation — the object the 2-D picture is a shadow of.

---

## 4. Un-Sieve space, bi- and trifurcation

The un-sieve births composites generation by generation from "just primes"
(`ValaQuenta/wiki/un_sieve.md`). A **bifurcation** is where activating one
prime forks the birth stream — a composite that needed `p` now also needs `q`.
A **trifurcation** is a three-prime fork. The bi/trifurcation tree *is* the
window ordering of the composites: smooth-number bands are the periodic
windows; the ragged generations between them are the chaos.

`FIRST STATED HERE 2026-08-31`: the un-sieve birth tree read as a bifurcation
diagram, generation on the axis, forks at prime activations.

---

## 5. Reading modulus factors as order-bubbles

For `N = p·q`: `N` is born in generation `π(gpf(N)) = π(max(p,q))`, at the
**bifurcation event** where its two primes activate. If the window ordering is
known (the 2-D slice gives one; the 3-D lift gives the reconnections), the RG
self-similarity says the factors sit at **RG-related positions** — you navigate
between order-bubbles with iterates of `R`, not by sweeping the chaotic sea.
And N's birth-window has a **wake** (§2) that may be readable without factoring
N.

**Honest bound (carried from the RSA-ping thread,
`hist_prime/RiemannHypothesisProof/PRIMER_2026-08-31_RSA_PING.md`):** this
*structures and bounds* the search; it does not beat the sub-exponential
exponent for a well-formed balanced modulus. The window ordering is the same
for every `N` in a magnitude class (granularity + jurisdiction), so RG
navigation still needs an **entry point** — close primes, known partial bits,
or a genuinely readable wake. The engine must **report explicitly** whether an
entry point exists or the search is unbounded. No cheating.

---

## 6. The full engine protocol

```
INPUT   a map family f_μ(x); a parameter sweep + resolution; a third axis
        (2nd parameter | CD rung | UNS generation | Im c); optionally N

1  ITERATE      per μ: iterate f_μ from a seed, drop the transient, record the
                attractor (finite period, or "chaotic" by Lyapunov λ > 0)
2  WINDOW       mark μ-intervals with a finite-period attractor → the windows
3  RG CLASSIFY  per window: fit the local rescaling (α, δ); assign RG level and
                parent window (the one it is a rescaled copy of)
4  WAKE         per window: locate the adjacent crisis / λ sign-flip boundary;
                record it with the window's RG level
5  LIFT TO 3-D  add the third axis; repeat 1–4 per slice; track how window
                orderings RECONNECT across slices → the hyper-bifurcation map
6  UNS MAP      in un-sieve space: mark the bi/trifurcation events (prime
                activations that fork the birth stream); the per-generation
                window ordering
7  FACTOR READ  (optional) for N: locate its birth window (generation
                π(gpf(N)), the bifurcation of its primes); report the
                RG-navigation path from the seed to that window, and the
                window's wake; STATE whether an entry point exists

OUTPUT  window catalogue (μ-interval, period, RG level, parent, wake);
        the 3-D reconnection map; [the factor read]

CHECKS
  • Feigenbaum δ ≈ 4.6692 recovered from the period-doubling accumulation
  • α ≈ 2.5029 recovered from the window rescaling
  • self-similarity: a window contains a scaled copy of the whole diagram,
    verified to the sweep resolution
  • SHA-256(catalogue) reproducible across machines
  • FACTOR READ never returns a factor without also returning "entry point:
    <yes/no>" — an unbounded search is reported as unbounded
```

Engine `engine/hyper_bifurcation.py` — **deferred build.** The protocol above
is the spec. Reuses `FactoralDecomposition/engine/lineage.py::un_sieve` for
step 6 and `DStarRG` for the RG classification in step 3.

---

## 7. FourthAgePaper protocol — the gate

| id | reject | test |
|---|---|---|
| G1 | "windows of order is just a picture" | run steps 1–3; produce the window catalogue with fitted α, δ; recover Feigenbaum's constants |
| G2 | "the 3-D lift is arbitrary" | show the same window ordering appears (reconnected) on ≥ 2 independent third axes (2nd parameter and CD rung) |
| G3 | "the UNS map is a relabelling of the sieve" | the bi/trifurcation events are prime *activations* in birth order; show they do not coincide with the extinction (spf) order — this is `un_sieve` §B.1 territory |
| G4 | "the factor read is a factoring claim" | it is not — G-test: the FACTOR READ output must carry `entry point: yes/no`; on a random balanced N it returns `no` and an unbounded interval |
| G5 | "you renormalized / coarse-grained by hand" | the RG classification is Feigenbaum's operator applied, not a subtraction; the window catalogue's RG levels compose (a level-2 window inside a level-1 window) |
| G6 | determinism | SHA-256(catalogue), twice, two machines |
| G7 | attribution | Feigenbaum / May / Coullet–Tresser / Sharkovskii / Mandelbrot own the bifurcation RG; first-stated-here: windows-as-the-locus-of-working-maths, the buoyancy/wake reading, the UNS bi/trifurcation map, the factor-as-order-bubble read |

**No σ-verification** — deliberate. No critical-line claim; the structure
stands on the Feigenbaum RG and a converging iteration.

---

## Conclusion

Lineage verdict: **no new generator.** The logistic map is tier-0
(SCALE ∘ SCALE + ADD); the renormalization is Feigenbaum's, unchanged; the
un-sieve is `ADD ∘ SCALE ∘ SIGN`. What is first-stated-here is the
**identification**: the windows of order are where the renormalization has
converged and therefore where working mathematics is; they rise buoyantly and
trail wakes; the 2-D bifurcation diagram is one slice of a 3-D object whose
subject is how the window orderings reconnect; and a modulus' factors are the
order-bubble it is born into in un-sieve space — navigable by the RG, bounded
only where an entry point exists.

Two engines, one renormalization: `d*_RG` runs it up the algebra tower;
hyper-bifurcation runs it across the parameter plane. The bubbles of order are
the same object in both.

---

## Relation to the series

- **The d* Renormalization Group** (`DStarRG/`) — the sibling engine.
- **The Oblique Gear** (`project_oblique_gear`) — the flowers are the windows;
  the wake is the retrograde precession; σ=½ is the saddle the RG converges on.
- **un_sieve** (`RiemannHypothesisProof/ADDENDUM_recursive_unsieve`,
  `ValaQuenta/wiki/un_sieve.md`) — UNS space, the birth tree, §B.1.
- **Cavitation Cascade** — the σ=½ phase transition is the period-doubling
  accumulation point.
- **Collatz as the 2-adic Shift** — a branch tree that is Pascal's triangle
  exactly; test the bi/trifurcation tree against it.
- **RSA-ping primer** (`hist_prime/RiemannHypothesisProof/`) — the honest
  bound on §5.
