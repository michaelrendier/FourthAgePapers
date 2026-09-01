# Recombination Misfires

## Hydrogen Is the Engine: Failed Attempts at Hydrogen Before, During, and After Recombination, and the Quark–Gluon Plasma as the Same Engine Block at Deconfined RPM

**Fourth Age Paper.** One Paper. One Claim. One Engine. One Wiki.
**Status: STUB.** No engine, no notebooks, no data yet — context capture for the
initial draft only.
**Author:** Cody Michael Allison <the.wandering.god@gmail.com>
**Registered:** 2026-08-31

---

## The idea

Cosmological recombination (z ≈ 1100, T ≈ 3000 K, ~380 kyr) is not a moment —
it is a slow, non-equilibrium process. Before an electron and a proton settle
into a hydrogen atom that *survives*, the pair forms and is torn apart many
times: a transient bound state (any n ≥ 1) is photoionised by a CMB photon from
the still-hot blackbody tail before it can cascade down and stabilise. Those are
the **misfires** — and there is no census of them.

The bottleneck that makes recombination slow is itself a feedback loop: a direct
recombination to the ground state emits a photon energetic enough to ionise a
neighbour, so net recombination has to proceed through the 2s→1s two-photon
channel and Lyman-α escape. **Each success triggers a failure elsewhere.** That
is the structure of a chain reaction run *sub-critical* — a decaying cascade
with a multiplication factor k(z) < 1.

**Two failure modes, and they are different (Cody, 2026-08-31):**

- **Misfire** — a capture that never takes: proton + electron → transient bound
  state (any n ≥ 1) → photoionised by a CMB-tail photon before it can cascade
  down and stabilise. Local. Doesn't touch neighbours. Just a wasted attempt.
- **Backfire** — an atom that *had* stabilised, re-ionised by a photon released
  by *another* atom's recombination. Non-local, and it propagates **against the
  flow** — against decreasing z, back up the process, knocking a finished atom
  into the plasma. This is the physical content of the Case-B → two-photon
  bottleneck: every "successful" direct ground-state recombination backfires
  into the medium, and recombination only makes net progress through the
  2s→1s channel *because those two photons are too soft to backfire*.

Misfires set the wasted-work count. **Backfires set k(z)** — they are the
negative reactivity: the reaction emits exactly what suppresses the reaction,
which is why the epoch is sub-critical and self-terminating rather than runaway.

**Hydrogen IS the engine (Cody, 2026-08-31).** Not a simulation *of* an engine —
the forming H atom's binding cycle is a rotary (three-face) heat engine, the
same object as the Wankel semantic engine in `VAPMIP/rotary_monad.py` /
`rotary_rerun_boxkite_monad.py` (RedBlue geometry, σ=½ coupling):

| engine stroke | hydrogen |
|---|---|
| intake | free e⁻ + free p⁺ drawn together (Coulomb) |
| compression | the electron cascades n → 1 down the shells |
| power / ignition | binding energy released as photons |
| exhaust | the photon escapes the medium — *or* is trapped (Lyman-α) |
| **misfire** | capture photoionised mid-cascade — cycle never fires |
| **backfire** | the exhaust photon fires back and re-ionises a finished atom |
| one shaft | the recombination redshift/time coordinate |
| three faces | the three emission channels — Lyman-continuum (direct, backfires), Lyman-α (resonant, trapped), 2s→1s two-photon (the working face) |
| σ = ½ balance | the ionisation fraction x_e = ½ redshift |

Recombination is that engine running **once, across the whole universe**. The
quark–gluon plasma is the **same engine block at deconfined RPM** — compression
so high / timing so advanced that no cycle can complete; QGP hadronisation is
the identical "fuzzy medium cooling through a binding threshold with a
combinatorial explosion of failed clusterings" problem, and parton-shower Monte
Carlo (branching processes, DGLAP) already simulates that cascade. The failed
attempts at hydrogen span the full RPM range: QGP (can't bind) → recombination
(binds, with misfires and backfires) → freeze-out (residual x_e ≈ 2×10⁻⁴).

---

## The claim (provisional — to be pre-registered before any run)

Stable hydrogen forms only when a **two-sided condition** is met at once
(Cody, 2026-08-31): the chain-reactive bath of sub-particles knocking things
about will not let an atom stand until both are satisfied —

- **inside** — the electron has cascaded deep enough (ground state, or below the
  reach of the CMB-tail photons), and the 2s→1s two-photon decay has completed;
- **outside** — the local radiation bath has dropped below the ionisation
  threshold, no neighbour backfire photon is incoming, and the free-electron
  density is low enough that collisional ionisation is rare.

These fail independently: a **misfire** is the *inside* condition unmet (cascade
photoionised before it completes); a **backfire** is the *outside* condition
unmet (a finished atom re-ionised by another atom's emission). The **misfire
ratio** `M(z)` counts inside failures; `k(z) < 1`, set by backfires, is the
outside feedback — the epoch is a **sub-critical branching process** that
mirrors a decaying nuclear chain reaction. The redshift where *both* conditions
hold universe-wide is the true end of recombination, *later* than the z ≈ 1100
last-scattering visibility peak.

Falsifiable against: RECFAST / HyRec / CosmoRec level populations, the Saha vs
non-equilibrium ionisation history, the measured width of the last-scattering
surface.

---

## Open questions carried into the draft

- **Is a QGP a chain reaction?** The thermalised bulk (near-perfect fluid, low
  η/s) is a *phase*, not a cascade. But its *formation and breakup* — parton
  showers, jet fragmentation, hadronisation — are branching processes,
  mathematically the same class (Galton–Watson) as a neutron cascade, with a
  multiplication factor and a criticality. So: the edges of the QGP mirror a
  chain reaction; the middle does not. Recombination is the same — the misfire
  cascade at the binding threshold is the chain-reaction-like part.
- Does `M(z)` diverge as z → recombination from above (fully ionised, every
  capture instantly undone) or stay finite?
- Do the "before" and "after" tails matter — pre-recombination He⁺→He⁰ misfires
  (z ≈ 2500) and post-recombination residual-ionisation misfires (freeze-out
  x_e ≈ 2×10⁻⁴)?
- Is the misfire cascade's branching tree Pascal's triangle (cf. CollatzShift)?

---

## Engine

**The engine is hydrogen** — the binding cycle above. It is not code; it is the
physical object the paper is about. What is *deferred* is the **simulation** of
it: a fine-resolution Monte Carlo of the recombination cascade in the
parton-shower idiom — per (proton, electron) pair, sample intake → compression
(cascade) → power (emission channel) → (exhaust | misfire | backfire) at
electron-shell time steps, over the recombination redshift range, with the
ionising-photon feedback coupled across pairs. Output: `M(z)` (misfire ratio),
`k(z)` (the backfire-set multiplication factor), the failed-attempt redshift
distribution, and the same run at QGP conditions for the deconfined limit.
Nothing to build now.

**TODO — yottasecond resolution.** To catch individual shell-crossing events the
step has to reach the Bohr timescale (~1.5×10⁻¹⁶ s) across a ~10¹² s epoch —
a dynamic range of ~10²⁸. "Yottasecond resolution" (Cody) = yocto-scale
(10⁻²⁴ s) stepping / ~10²⁴ resolution elements; the dynamic range *is* the hard
part and probably the real subject of the paper. Adaptive / multi-rate
integration, or a renormalisation-group-style coarse-graining of the fast loop
— **but note the standing No-Renormalization rule; coarse-graining here must be
exact (a resummation), not a subtraction.**

---

## Relation to the series

- **Cavitation Cascade** — the Big Bang as a phase transition at σ=½; this is a
  later phase transition (ionised → neutral) read the same way.
- **Inertia and Entropy** — the entropy current at a phase boundary; the misfire
  cascade is that current made discrete and countable.
- **CollatzShift** — a branching tree that is Pascal's triangle exactly; test
  whether the misfire tree is too.
- **The Oblique Gear** (`project_oblique_gear`) — destructive interference that
  rings back out of a null; a misfire is that at atomic scale.
