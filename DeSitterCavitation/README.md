# No Singularity

**the Abrikosov-Vortex Core and De Sitter Cavitation over a Black Hole's Life**

**Fourth Age Paper.** One Paper. One Claim. One Engine. One Wiki.
v0.100 — 2026-08-30
Engine: `ValaQuenta/modules/desitter_cavitation/` (`DeSitterCavitationModule`) — **calculation, not simulation**
Notebooks: `00_no_singularity_vision` · `01_predictions` · `02_data` · `03_results`
Wikis: `Ainulindale/wiki/108_desitter_cavitation.md` · `ValaQuenta/wiki/desitter_cavitation.md`

This is an **engineering exploration** carried out with academic methodology.
The engineering portion — the four black-hole-class calculation — lives in the
paper (§5), it is not an appendix.

---

## The Claim

> **There is no singularity.**
>
> The interior of a black hole is a finite, sub-Planckian **de Sitter core** —
> the Abrikosov vortex core made gravitational. The arithmetic / spectral
> condensate goes to zero (a Riemann zero, winding number 1) while density,
> pressure and curvature stay **finite**. Over the hole's life the core
> releases *stiff space* (metric, Λ-signed, `p = −ρc²`) and *stiff matter*
> (radiative, ceiling `p = ρc²`), and at evaporation it unwraps completely —
> the **De Sitter Cavitation**.

Everything rests on one matching identity. A gravastar match (Mazur–Mottola
2001) of the interior de Sitter metric `1 − (r/L)²` to the exterior
Schwarzschild `1 − r_s/r` at the shell forces

```
L_dS = r_s.
```

---

## §1 — Why a vortex core has no singularity

In a type-II superconductor a vortex core is a **simple zero** of the order
parameter, `|Ψ| → 0`, winding number 1. The free-energy density there is
finite — the condensation energy `H_c²/8π`. There is no divergence; the "line
singularity" of ideal-fluid vortex theory is an artifact of ignoring the core's
finite size `ξ`.

Ainulindale wiki/75 already identifies the Riemann zeros as the vortex cores of
the prime condensate. One domain over, the black-hole interior is the same
object: the condensate vanishes on a codimension-set of winding 1, and
everything else stays finite. The "singularity" of `r = 0` in the Schwarzschild
solution is the ideal-fluid line-singularity mistake, made in geometry.

---

## §2 — The Holcus prediction (P1, pre-registered)

> The maximum curvature invariant inside **any** black hole is the de Sitter
> Kretschmann scalar at `L_dS = r_s`:
>
> ```
> K_core(M) = 24 / L_dS⁴ = 24 / r_s⁴ = (3/2) · c⁸ / (G⁴ M⁴)      [m⁻⁴]
> ```
>
> Finite for every `M > 0`. Scales as `M⁻⁴`. **Sub-Planckian for every
> `M > (3/2)^{1/4} m_Pl ≈ 1.107 m_Pl`.** Its observational shadow is a
> gravitational-wave ringdown echo at delay `Δt_echo ≈ (2 r_s/c)·ln(r_s/ℓ_Pl)`,
> of order the interior light-crossing time.

**Falsifier (the sole one):** a core curvature that either **diverges**
(classical GR singularity) *or* **pins to `K_Planck` independent of `M`**
(limiting-curvature / Planck-star). Observationally: **no ringdown echoes**
down to the reflectivity bound a finite core requires.

The prediction is a fork: it distinguishes the gravastar/Abrikosov core
(`K_max ∝ M⁻⁴`, mass-dependent, deeply sub-Planckian for astrophysical `M`)
from **both** classical GR (`K → ∞`) **and** Planck-star / limiting-curvature
models (`K_max = K_Planck` for every `M`).

---

## §3 — What follows from `L_dS = r_s`

| quantity | value | reading |
|---|---|---|
| interior BANG time | `τ = 1/H_dS = r_s/c = 2GM/c³` | one e-fold; the core cannot rest |
| core curvature | `K_core = 24/r_s⁴ = (3/2) c⁸/(G⁴M⁴)` | **P1** — finite, `M⁻⁴`, sub-Planckian |
| Schwarzschild contrast | `K(r) = 48 G²M²/(c⁴r⁶) → ∞` as `r → 0` | the artifact the claim denies |
| core / Hawking temperature | `T_dS = ħH_dS/2πk_B = 2·T_H(M)` | the core inherits the hole's scale, doubled (**P5**) |
| stiff-space channel | `p = −ρc²`, `ρ_core c² = 3c⁸/(32πG³M²) ∝ M⁻²` | metric / Λ-signed |
| stiff-matter ceiling | `p = ρc²`, sound speed `c` (Zel'dovich) | the incompressibility limit |
| unwrapping | horizon recedes below the core as `M` evaporates | decompression → cavitation |

---

## §4 — Where space stops being a supercritical fluid

The σ = ½ surface — the gravastar shell, the critical line, the **Widom line**
of the vacuum condensate. Inside (de Sitter core, `p = −ρc²`) is the
vacuum-dominated phase; far outside is asymptotically flat; between the horizon
and the shell the medium is *supercritical* — continuous, no interface, which
is why classical infall is smooth. In temperature: supercritical between
`T_dS(M) = 2T_H(M)` and `T_Planck`; distinct phases with a sharp shell below
`T_dS`; no fluid description at all above `T_Planck`. The cavitation is the
first-order transition the shell makes sharp.

---

## §5 — The engineering table (four black-hole classes, all closed form)

| class | `M` | `r_s` | `τ = r_s/c` | `T_H` | `t_evap` | `K_core` (m⁻⁴) | `K_core/K_Planck` | QGP core? | echo delay |
|---|---|---|---|---|---|---|---|---|---|
| kugelblitz / primordial | 10¹² kg | 1.49 fm | 4.95×10⁻²⁴ s | 1.23×10¹¹ K | 2.67×10¹² yr | 4.93×10⁶⁰ | 3.4×10⁻⁷⁹ | **yes** | 4.6×10⁻²² s |
| stellar | 10 M☉ | 29.5 km | 9.85×10⁻⁵ s | 6.2×10⁻⁹ K | 2.1×10⁷⁰ yr | 3.15×10⁻¹⁷ | 2.2×10⁻¹⁵⁶ | no¹ | 1.8×10⁻² s |
| intermediate | 10⁴ M☉ | 2.95×10⁴ km | 9.85×10⁻² s | 6.2×10⁻¹² K | 2.1×10⁷⁹ yr | 3.15×10⁻²⁹ | 2.2×10⁻¹⁶⁸ | no | 1.9×10¹ s |
| supermassive | 10⁹ M☉ | 19.7 AU | 9.85×10³ s | 6.2×10⁻¹⁷ K | 2.1×10⁹⁴ yr | 3.15×10⁻⁴⁹ | 2.2×10⁻¹⁸⁸ | no | 2.1×10⁶ s |

¹ QGP (`ρ_core c² ≥ 1 GeV/fm³`) is reached for `M ≲ 3 M☉`. `ρ_core ∝ M⁻²` — the
small holes are the hot ones. **Every class is sub-Planckian in core curvature
by ≥ 78 orders**: there is never even Planck-scale curvature, let alone a
singularity, except for Planck-mass holes.

- The interior BANG time is a **light-crossing time** in the interior frame —
  the core does not persist. The exterior sees it dilated (`~(M/m_Pl)² t_Pl`)
  into a long slow glow; "it lasts a while" is a frame artifact.
- Kugelblitz / primordial mass is the **only** class where the black→white
  bounce time can be less than the age of the universe and where Hawking
  evaporation is dynamically relevant — so the cavitation picture is
  observationally live there and nowhere else.

---

## §6 — Results (from `03_results.ipynb`)

| # | prediction | verdict |
|---|---|---|
| **P1** | `K_core(M) = (3/2) c⁸/(G⁴M⁴)` — finite, `M⁻⁴`, sub-Planckian; ringdown echo ~ `r_s/c` | **STANDS** — consistency check passes across a 27-order mass sweep (`M⁻⁴` to rel err ≤ 1.6×10⁻¹⁶; crossover = `(3/2)^{1/4} m_Pl`); sole falsifier not triggered |
| P2 | energy split `1 − d* : d*` = `0.754 : 0.246` | ASSERTED — no independent measurement of the non-radiative fraction yet |
| P3 | QGP only for `M ≲ 3 M☉` + kugelblitz | CONFIRMED in-model (`ρ_core ∝ M⁻²`) |
| P4 | cosmic budget `Ω_cav ≈ Ω_BH(1 − d*) ≈ 7.5×10⁻⁶` vs `Ω_Λ ≈ 0.685` | **FALSIFIED as a magnitude** (short ~5 orders) — kept in data; the mechanism's only possible trace is **dark flow** (directional, cumulative along the spin axis), not a dark-energy density |
| P5 | `T_dS = 2 T_H` exactly | CONFIRMED (ratio = 2.000…) |

**The claim survives because it rests on P1 alone.** No falsified secondary was
reinterpreted to save it.

---

## §7 — Out of scope (stated, enforced)

- **No derivation** that nature selects this interior. The engine checks
  *if*-gravastar-*then*-`K_core` is the de Sitter value; it does not solve a
  field equation for the interior. P1 is an internal identity verified across a
  mass sweep — evidence of consistency, not a theorem.
- Bounce-time and echo-delay **coefficients** are `O(1)` and model dependent
  (Haggard–Rovelli; Cardoso–Pani). Only the scalings are asserted.
- Nothing about information, unitarity, or the Page curve — that sits at the
  "before measurement breaks" seam.
- The `d*` energy split is asserted, not derived. `cosmic_cavitation_budget`
  is expected to fail as a magnitude.
- The paper uses the **labelled** ZD object **PSL(2,7)** (order 168, Aut Fano);
  Moreno's `ZD(𝕊) ≅ G₂` is the blow-up that forgets the labelling.

---

## §8 — Open

The largest gap: **there is no proof, and no interior field solution.** P1 is
verified as a de Sitter identity across 27 orders of mass; that is consistency,
not a theorem, and the claim is stated for *every* black hole. The
observational falsifier — ringdown echoes at `Δt ~ r_s/c` — is live for
LIGO/Virgo now and decisive for LISA on supermassive mergers.

---

*No free parameters in P1. No renormalization. Failed predictions (P4) stay in data.*
