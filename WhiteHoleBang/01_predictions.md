# 01 — Predictions

**Skeleton.** The predictions committed *before* any deciding number is
computed. Structural now; each gets a quantitative range when `engine/` is
built (step 3), and that range is committed here before `02_data` /
`03_results` are touched. Machine-readable copy: `predictions.json`.

Provenance tag on every row: **KNOWN** (standard physics, cited),
**OURS** (this framework's claim under test), **DERIVED** (falls out of the
engine).

| # | prediction | provenance | falsifier |
|---|---|---|---|
| **P1** | A deconfinement mass `M_dec = c⁴ / (G^{3/2}·√B)` exists **above** `M_Planck`. `B` = MIT bag constant, `B^{1/4} ∈ [145,235] MeV`. Order `10 M☉`. | OURS (bag model KNOWN) | `M_dec < M_Planck`, or the interior reaches stiff-matter density before reaching `M_dec`. **This kills the whole claim.** |
| P2 | Uncompression energy `E_bang ~ M_dec c²` minus binding already radiated; `~10⁴⁸ J` for `M_dec ~ 10 M☉`. | DERIVED | — (magnitude check) |
| P3 | Relic spectrum is **Planckian** after adiabatic expansion `R_final/R_dec`; not a power law, not lines. Shape matches the CMB; absolute `T` set by the expansion factor. | OURS | emergent spectrum is non-thermal |
| P4 | Bang radiation is **anisotropic**, collimated along the infall axis. `dipole/monopole ≳ 0.1` (≫ CMB `~10⁻³`). | OURS | isotropic |
| P5 | The junction surface is **exactly flat**: the effective curvature invariant `= 0` there, and it coincides with the photon sphere `r = 3GM_dec/c²`. Tangent cone at the lemniscate node = two straight lines; `π` its constant; `sc = 1.0`. | OURS | zero-curvature locus ≠ photon sphere in the model |
| P6 | State at `t = 10¹² yr` post-Bang: relic `T`, expansion state, structure scale — vs the CMB-derived history. | DERIVED | committed as a range when the engine runs |

## Not predicted (out)

- The pre-collapse stellar history.
- Anything about the exterior universe or a second observer.
- Whether our CMB *is* such a relic — P3/P6 compare **shape**, they do not
  identify.
