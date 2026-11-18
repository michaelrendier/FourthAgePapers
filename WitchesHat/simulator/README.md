# The Witch's Hat simulator: the Virtual Action Potential, Brim, Cone and Hat

**Status 2026-11-17: step 1 (numbers) done and run; step 2 (renders) running.** Skill: `spatial-simulation` (`~/.claude/skills/`).

**What it maps.** Everything up to the Mexican-hat potential is established maths; the author's L_dynamic (L_(I|O)) is mapped onto it and labelled as the author's reading.

| Layer | Source | Status |
|---|---|---|
| Hat potential V(h) = −μ²h²/2 + λh⁴/4, m_h = 125.25 GeV, v = 246.22 GeV → λ = 0.12938, μ² = 7843.8 GeV², brim radius v, V″(0) = −μ², V″(v) = m_h² | Standard Model Higgs sector | `ESTABLISHED` |
| m_W, m_Z, photon massless from the vev (tree level) | electroweak theory | `ESTABLISHED` (80.23 and 91.56 GeV tree level against PDG 80.37 and 91.19) |
| Radial m = 0 Schrödinger states on the hat | quantum mechanics | `ESTABLISHED`; the ground state sits on the brim (r = 0.969 at depth 40, 0.991 at depth 400) |
| Maxwell + hat: Nielsen–Olesen vortex, critical coupling | abelian Higgs model | `ESTABLISHED`; solved as a boundary-value problem, flux 6.283080 vs 2π = 6.283185, Bogomolny residual 9.4e-5 |
| Paths of fixed energy from the brim, abbreviated action W = ∫√(2(E−V)) ds | classical mechanics (Maupertuis / Jacobi) | `ESTABLISHED` |
| The bundle brim → hilltop read as the cone of dynamic action | the author's L_dynamic, L_(I|O) | `THEORETICAL` |

**Run:** `python3 hat_sim.py` (output `hat_sim_output_2026-11-17.txt`); `python3 export_paths.py N` writes `hat_paths_nN.json`; `blender -b -P render_hat.py -- OUTDIR N [turn]` renders; `run_renders.sh` does stills for n = 4, 2.5, 10 and a turntable.

**Results (`:CALCULATED`, `hat_sim_output_2026-11-17.txt`).**
- Closest approach at E = 0 against the closed form √(sin ψ)((n−2)/n)^¼: 0.0842 vs 0.0841 (ψ = 0.01), 0.5464 vs 0.5247 (ψ = 0.4; the form is a small-ψ asymptote).
- Abbreviated action along the radial path brim → hilltop, W = ∫₀¹√(4x²−2x⁴)dx = 0.861929 (numerical and exact agree); a non-radial path reaches its closest approach with W = 0.8619, 0.8618, 0.8609, 0.8560, 0.8314 for ψ = 0.01, 0.05, 0.1, 0.2, 0.4: the abbreviated action to the closest approach is almost independent of the launch angle (3.5 % lower at ψ = 0.4). **Correction (2026-11-18):** the first version of this README reported 0.68 to 0.95 here; that was the arc length ∫v dt, not the action ∫p·dq = ∫v² dt; the code and this number are fixed.
- Focus against shape (median r_min/r₀ of the ψ = 0.02–0.4 bundle): 0.350 (n = 2.2), 0.392 (4), 0.445 (20). Shape sets the resolution; nothing singles out n = 4 (paper B).
- Not claimed: that the paths form a cone. The paths are computed; the cone surface drawn in the renders is the author's reading (height = radial action W₀ above the brim plane), not a result.

**Frame check (skill §1, §4).** Each still is read for: the object inside the image, the hilltop marker visible, the brim ring visible, scale cue = the brim ring itself (radius 1). Renders in `renders_v3/` (earlier trial renders `renders/`, `renders_v2/` kept: they were cut too wide, the front wall hid the hilltop).
