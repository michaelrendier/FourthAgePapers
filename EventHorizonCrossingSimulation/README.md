# The Event Horizon Crossing Simulation

**Cody Michael Allison** (Michael Rendier) · the.wandering.god@gmail.com ·
[github.com/michaelrendier](https://github.com/michaelrendier) ·
ORCID: [0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760)

**Fourth Age Paper.** One Paper. One Claim. One Engine. One Wiki.

**Status: STUB.** Registered 2026-09-24. Not yet written. **Nothing here is
built** — this is the physics/engineering requirements list, deliberately,
per the registering instruction: get the requirements down precisely first;
the actual simulation is a later, GPU-heavy (Google Colab) project.

---

## The Claim

> **`0_RB` gives the fixed anchor and `L_(I|O)` gives the crossing
> operator needed to simulate a horizon-crossing in real 3D space (SCAD
> for exact parametric geometry, Blender for rendering) such that the
> flat-boundary / one-way / de-Sitter-unwrapping structure already
> derived in this project's own conversation record is something you can
> actually fly a camera through, not just describe.**

The physics the simulation has to get right is **established, not
novel** — general relativity, gravastar models, de Sitter static patches.
What's novel to this project is the mapping from `0_RB`/`L_(I|O)`
(the sedenion boundary-generator/crossing-operator pair) onto that
established geometry as the actual scene-construction method. Keep those
two firmly separate in the eventual paper, the same split
`TheInterface/README.md` already draws: the general theory isn't
proprietary, the specific application is.

---

## Scope note — depends on, does not duplicate

- **[[TheInterface]]** — `L_(I|O)` as a general boundary-object carrying
  both sides' information jointly. This paper's crossing operator is a
  *specific instance* of that general object, not a separate mechanism.
  `TheInterface` should land its own falsifier/engine before this paper
  leans on it hard.
- **Gravastar / de Sitter interior** — the destination geometry
  (Mazur–Mottola). If `DeSitterCavitation` (already registered elsewhere
  in this project) reaches a built engine first, reuse its de Sitter
  interior construction rather than re-deriving it here.
- **`0_RB` as the fixed anchor** — `e0`/`e8`, already established and
  code-verified (`box_kite.maths.e0_is_outside`,
  `fixed_point_gluing`) as the one point outside the geometry it
  generates. This paper's camera-anchor point in the simulation should be
  built from that object directly, not a fresh invented "center."

---

## Physics requirements — established GR, cited precisely

This section is the actual academic physics the geometry has to satisfy.
None of it is new; all of it is required before a single polygon gets
built, because a visually plausible black-hole scene that violates any of
these is a pretty picture, not a simulation.

1. **Exterior metric.** Schwarzschild (non-rotating, start here — Kerr
   only if/when rotation is actually needed for the scene). Standard,
   textbook (Misner–Thorne–Wheeler; Wald).

2. **Interior metric — de Sitter static patch**, per the gravastar model
   (Mazur & Mottola, 2001/2004, "Gravitational Vacuum Star"). Constant
   positive curvature, vacuum-energy-dominated. This is the destination
   geometry "behind" the crossing.

3. **The matching condition — Israel junction conditions.** Exterior
   (Schwarzschild) and interior (de Sitter) are two different exact
   solutions; they have to be glued across a thin shell correctly, with
   the induced metric and extrinsic curvature jump satisfying Israel's
   thin-shell formalism (Israel, 1966). This is the actual mathematical
   object that makes "gravastar" a real spacetime rather than two
   unrelated regions taped together. **Do not skip this and eyeball the
   transition** — it's the one piece of established machinery that turns
   the simulation from illustration into an actual solution of Einstein's
   equations.

4. **The r/t causal-character swap**, Schwarzschild interior (standard):
   outside the horizon `r` is spacelike (free) and `t` is timelike
   (forced); inside, they swap. Already derived precisely earlier in this
   project's own conversation record — the simulation needs to render
   this as an actual change in which direction is "forced," not just a
   visual effect.

5. **Local flatness at the crossing — the equivalence principle.**
   The infalling camera's own local frame must render as locally flat,
   undistorted, "no drama" at the horizon — distortion belongs only to
   the external Schwarzschild-coordinate rendering mode. This means the
   simulation needs **two distinct rendering modes sharing one geometry**:
   the external/distant-observer view and the local proper-frame view.
   Conflating them is the single most common way a black-hole
   visualization becomes physically wrong while still looking dramatic.

6. **Real prior art for the actual rendering method: general-relativistic
   ray tracing.** The established technique is geodesic ray-marching
   through the curved metric, camera-ray by camera-ray — not a rasterized
   "sphere with a shader." The reference implementation to build from
   conceptually is James, von Tunzelmann, Franklin & Thorne (2015),
   *"Gravitational lensing by spinning black holes in astrophysics, and
   in the movie Interstellar,"* Classical and Quantum Gravity 32, 065001
   — the actual published methodology behind that film's black hole
   visualization, and the reason this is correctly flagged as a GPU
   project: one geodesic integration per pixel, not a fixed mesh.

---

## The novel piece — 0_RB / L_(I|O) as the construction method

Kept separate from the established physics above on purpose.

- **`0_RB` (`e0`/`e8`) is the camera's fixed anchor**, not a free
  parameter. Its already-verified property — outside every chart it
  generates, invariant under the conjugation involution — is what should
  place and hold the camera's reference frame across the crossing, the
  same "hub" role it plays in `scaled_mind_eye_boxkite_kernel_monad.py`.
- **`L_(I|O)` is the crossing/unwrapping operator** — the mechanism that
  takes the exterior (Schwarzschild) description and the interior
  (de Sitter) description and carries both sides' information jointly
  across the Israel-junction shell, rather than the simulation needing a
  separate "translate exterior into interior" step. This is the paper's
  actual thesis: that `L_(I|O)`, already defined generally in
  `TheInterface`, is sufficient to *be* the junction-crossing operator
  for this specific geometry, not just an analogy for it.
- **Falsifier, once an engine exists:** does the `L_(I|O)`-constructed
  crossing reproduce the Israel junction condition's own matching
  requirement exactly, or does it require an ad hoc correction term? If
  it needs a correction term, `L_(I|O)` isn't actually doing the
  established physics's job and the claim is dead as stated.

---

## Build requirements — for the eventual (Colab, GPU) build, not now

**Explicitly deferred. Nothing below gets built in this pass.**

- **Geometry:** OpenSCAD (or its Python bindings) for exact parametric
  construction of the shell/interior/exterior regions from the matched
  metric — not hand-modeled geometry. The Israel-junction radii and
  curvatures are computed quantities; the SCAD model should be generated
  from them, not eyeballed to match.
- **Rendering/animation:** Blender, driven by the same computed geometry
  — two camera rigs (external-observer mode, local-proper-frame mode per
  requirement 5 above).
- **Compute:** GPU-bound by the ray-tracing requirement above (one
  geodesic integration per pixel per frame) — Google Colab, per the
  registering instruction, not local hardware.
- **Bridge:** the actual geodesic integration (Schwarzschild exterior,
  de Sitter interior, Israel-matched at the shell) needs to run in Python
  (numpy/GPU array backend) and hand off vertex/camera data to
  SCAD/Blender — not be reimplemented inside either.

## TODO

- [ ] State the falsifier precisely (see "novel piece" above — draft only).
- [ ] Identify the engine (Python: metric + geodesic integrator +
      Israel-junction solver; separate from the SCAD/Blender front end).
- [ ] Confirm `TheInterface`'s own engine/falsifier before leaning on
      `L_(I|O)` here.
- [ ] Confirm whether `DeSitterCavitation` has a reusable de Sitter
      interior construction before re-deriving one.
- [ ] Notebooks: at least a 2D (equatorial-slice) proof of concept of the
      Israel-junction-matched geodesic integration, verified against
      known Schwarzschild geodesic results, before attempting 3D/Blender.
- [ ] Licensing section (see `ScalarContextPropagation/README.md §15` for
      the pattern) — established GR is not proprietary; the `0_RB`/
      `L_(I|O)` construction method is.
- [ ] Wiki page (written last, per convention).
