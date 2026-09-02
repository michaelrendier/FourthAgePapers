# 02 — Reference Data

**Skeleton — stub.** The reference observations the engine calibrates against.
Labelled as **reference**, not as tests. Filled in step 1.

| set | what | source | role |
|---|---|---|---|
| CMB spectrum | FIRAS blackbody, `T₀ = 2.72548 K`, deviations `< 10⁻⁴` | COBE/FIRAS (Fixsen 2009) | P3 shape yardstick |
| CMB dipole | `3.362 mK`, `dipole/monopole ≈ 1.23×10⁻³` | Planck 2018 | P4 anisotropy yardstick |
| QGP / bag EOS | `B^{1/4} ≈ 145–235 MeV`; deconfinement `T_c ≈ 155–170 MeV`; QGP density `~10¹⁷–10¹⁹ kg/m³` | lattice QCD; MIT bag model (Chodos et al. 1974) | P1 pressure floor |
| Page curve / evaporation | `t_evap ∝ M³`; `t_evap(M☉) ≈ 2×10⁶⁷ yr` | Hawking 1974, Page 1976 | timescale reference (see `00_vision`) |
| Stiff matter | `p = ρc²`, `c_s = c` — the falsifier's ceiling | Zel'dovich 1961 | P1 falsifier |
| Gravastar junction | interior de Sitter, thin shell, exterior Schwarzschild | Mazur & Mottola 2001/2004 | P5 junction model |

No data is read into a scorecard until `01_predictions` carries committed
quantitative ranges.
