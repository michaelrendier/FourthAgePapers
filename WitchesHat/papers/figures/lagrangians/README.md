# Lagrangian figures for the Witch's Hat paper

One folder per version, every version kept. File names carry the version: `WitchesHat_Lagrangians_vX.Y_<name>.svg`.

| version | what | generator |
|---|---|---|
| `v1.0/` | the four Lagrangians with their paths drawn on the potential surface (isometric, top, front, side), plus the Standard-Model context figure | `simulator/render_lagrangian_svgs.py` |
| `v2.0/` | what the maths gives: the bundle of paths from every point of the brim in every direction, selected by what each path does, drawn as the action cone; the tip, its sheets, the time pathway | `simulator/render_lagrangians_v2.py`, `simulator/tip_and_time.py` |

Engines: `ValaQuenta/modules/witches_hat/action.py` (`brim_bundle`, `tip_report`, `cone_tip_height`, `ray_bundle`, `natural_units`), `ValaQuenta/modules/lagrangian_sm`. Rendering rules: the `spatial-simulation` skill, `references/spaces.md` §10. Papers: `../../A_hat_geometry.md`, `../../B_dynamic_path.md`.
