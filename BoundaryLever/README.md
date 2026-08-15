# The Boundary Lever

**Fourth Age Paper.** One Paper. One Claim. One Engine. One Wiki.

---

## The Claim

> **The Cayley–Dickson doubling boundary is a chiral mirror,**
>
> ```
> e_(i+H) · e_(j+H)  =  e_j · e_i          H = dim/2
> ```
>
> **whose exactly two fixed points — `e_0` and `e_(dim/2)` — are precisely the indices
> belonging to no zero-divisor plane, at every level from `dim = 16` upward.**

**Falsifier:** compute the orphans at any higher level. If they are not `[0, dim/2]`,
the claim is dead.

**Status: STANDS.** Verified by enumeration at `dim = 16, 32, 64`, and at **`dim = 128`
as a pre-registered prediction** (P1) committed before that level was computed.

---

## Result

| # | prediction | verdict |
|---|---|---|
| **P1** | orphans at `dim = 128` are exactly `[0, 64]` | **CONFIRMED** — the sole falsifier |
| P2 | mirror order-reversing at `dim = 128`, `3782` pairs | FALSIFIED *as written* — count mis-derived (`63×62 = 3906`, not `62×61`); measured `3906/3906` reversed, `0` preserved, so the **property** held |
| P3 | `upper × upper` escapes the lower half `0/4096` times | **CONFIRMED** |
| P4 | ZD census at `dim = 64` is `4116` (`588/2940/588`) | **FALSIFIED** — measured `3036` (`588/1860/588`); the `×7` extrapolation is dead |
| P5 | nullity at `dim = 64`: non-crossing `16`, crossing `8, 24` | **FALSIFIED** — replaced by a parity law (below) |

**2/5 confirmed as written.** The claim survives because it was written to rest on P1
alone — no falsified prediction was reinterpreted to save it.

### The productive failure

P5 guessed a *value* where the structure is a *parity*. Found post hoc, holding at
both `dim = 32` and `dim = 64` with no exceptions:

> A zero divisor **confined to one half** has nullity an **even** multiple of 4.
> A zero divisor **spanning the boundary** has nullity an **odd** multiple of 4.

```
dim 32   non-crossing [8]           /4 = [2]              even
         crossing     [4, 12]       /4 = [1, 3]           odd
dim 64   non-crossing [8, 16, 24]   /4 = [2, 4, 6]        even
         crossing     [4, 12, 20, 28] /4 = [1, 3, 5, 7]   odd
```

**P6 — CONFIRMED (2026-08-15, after the paper was written).** The parity law holds at
`dim = 256`, and at `dim = 512` as well — two levels past registration.

```
dim 256   ZD  59,772 = {13884, 32004, 13884}   orphans [0, 128]
dim 512   ZD 249,084 = {59772, 129540, 59772}  orphans [0, 256]
```

Both match the closed form `ZD(d) = d(d + 3/2 − 3·log₂d) − 4` to the unit, and
`lower(2d) = upper(2d) = total(d)` exactly. The main claim's orphans hold at both levels
too.

⚠ **Method changed.** The SVD census is `O(d³)` per candidate — 45 minutes at dim 256,
with a tolerance you have to guess. Every `P_i` is a **signed permutation matrix**, so
`ker(P_i + s·P_j) = ker(I + s·Q)` with `Q = P_i⁻¹P_j` also a signed permutation — and a
signed permutation's spectrum is fixed by its **cycle structure** alone. Nullity becomes a
cycle walk: `O(d)`, exact integers, **no tolerance at all**. dim 128: 27s → 1.8s. dim 256:
~45 min → 3.4s. dim 512 became reachable (29.5s). Script:
`ThePlace/.claude/scratchpad/2026-08-15_zd_asymptote/parity_fast.py`, validated against
the SVD census at 16/32/64/128 before being trusted.

---

## Why it is a lever

The mirror's two fixed points are the identity `e_0` (which generates the boundary and
does not live on it — `[e_0,·,·] = 0`) and `e_(dim/2)`, the generator introduced by that
doubling. They pair with nothing, they sit in no Assessor, and they carry no force —
the subspace 0_RB calls *gravity, present as absence*.

**A fulcrum does no work.** Everything else balances across them in equal number:
`84 / 84` at `dim = 32`, `588 / 588` at `dim = 64`.

And because the mirror is **chiral**, successive boundaries do not stack into parallel
reflections. Two reflections compose to a rotation, and the boundaries sit at `dim/2` —
constant step in `log2`, constant pitch `ln 2`. Rotation plus constant logarithmic
advance is a **spiral**: the Archimedes screw of Phase 24, reached from the algebra
rather than from the primes.

---

## Notebooks

| | |
|---|---|
| `00_boundary_lever_vision.ipynb` | the question, the lever, and what this paper does **not** claim |
| `01_predictions.ipynb` | P1–P5, committed before the deciding data is read; provenance of each stated |
| `02_data.ipynb` | the originating observations — labelled as such, **not** tests |
| `03_results.ipynb` | the scorecard, the failures read honestly, the parity law, P6 |

## Engine

`ValaQuenta/modules/angular_rank/` (the 16D oscilloscope) and
`ValaQuenta/modules/box_kite/` (the Cayley–Dickson table, borrowed not reimplemented).

## Out of scope

Stated in `00_vision` and enforced throughout: **nothing** about observers, nothing
about meaning, nothing about physics. The algebra can rule a symmetry in or out; it
cannot say what the halves *are*.

## Open

The largest gap: **there is no proof.** Every level here is verified by enumeration,
not derived. A sweep holding at four levels is evidence, not a theorem — and the claim
is stated for *every* level.
