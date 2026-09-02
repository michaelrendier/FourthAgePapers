# engine/ — the proper-time integrator  (STUB, build = step 3)

Walks proper time `τ` from a chosen initial mass `M₀` through:

    evaporation  →  deconfinement (M → M_dec)  →  uncompression  →  Bang  →  expansion

and **keeps the clock the whole way**, so the event can be "tuned in" at
depth (fine `τ` steps around the crossing).

## Fixed constraints (Cody, 2026-09-01)

- **6-place fixed precision.** All state carried as integers scaled by `1e6`
  (or `decimal.Decimal` capped at 6 places). Skips the float-accumulation
  problem by fiat — the run is reproducible bit-for-bit and every result is a
  guarantee, not a tolerance.
- **Fast inverse square root.** 6-place precision is inside `Q_rsqrt`'s
  accuracy after one Newton step, so every `√` in the integrator (Schwarzschild
  radius, escape terms, blackbody `T`, expansion factor) goes through the
  bit-hack path. Provide both `rsqrt_fast` and an exact reference; assert they
  agree to 6 places in the self-test.
- **Multi-scale runs (step 1).** Same integrator, `M₀` swept over
  stellar / intermediate / supermassive; compare relic spectra and energy
  budgets to each other and to the CMB.

## Borrowed, not reimplemented

- Cayley–Dickson table: `ValaQuenta/modules/box_kite/`.
- Lemniscate / saddle order parameter `b/a`: `ValaQuenta/modules/scale/`,
  `.../box_kite/` (the Smith-chart lemniscate sections).

## Side investigation (not blocking)

"Can every Cayley–Dickson level be written in bitwise operations for overhead
reduction?" — the basis-product **index** is `i XOR j`; the **sign** is a
bitwise recurrence (a popcount/AND carry count over the bit expansions, the
twisted-group-algebra form). If it holds cleanly it is the engine's fast
inner loop. Investigated in `ValaQuenta`, referenced here.
