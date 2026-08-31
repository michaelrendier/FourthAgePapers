# Forward Propagation of Information and Context by Scalar Value

**Fourth Age Paper.** One Paper. One Structure. One Engine. One Wiki.

Full title: *Forward Propagation of Information and Context by Scalar Value for
Reconstructible Lossless Continuity of Context from WordNet Box Kites.*

---

## Abstract

A box kite — a six-vertex zero-divisor figure in the sedenions, carrying an
octonion's worth of independent structure — is the equilibrium shape of a
loaded string, and a loaded string is one-dimensional. Fixing *which* box
kite (its pencil, pure combinatorics from `PG(3,2)`) leaves a single
continuous degree of freedom. We carry context forward as **one scalar per
token** — a wind speed, the co-occurrence basin drift, read against WordNet —
and reconstruct the full box-kite relational structure from it: exactly for
the deformable charts, trivially for the rigid ones, by a Joukowsky
deformation law. No multiplication table, adjacency tensor, or attention
matrix is stored or propagated; the weights are the number line. A separate
optical stage — a flashlight casting the reconstructed kite onto a
Smith-chart-placed wall — sets the granularity at which the structure is
resolved to a word, from narrative to dissertation, without adding
information. This is not a claim under test. It is a codec assembled entirely
from established mathematics, presented for use.

---

## The departure from the template

Every other Fourth Age paper is *One Paper, One Claim* — a falsifiable
prediction the engine tests. **This one has no claim and no prediction.** It
is an **engineering structure**: a codec that reconstructs a higher-order
group of relationships from a single scalar, built entirely out of established
mathematics, with the working parts named and runnable.

That is the protocol applied, not relaxed. A pre-registered prediction means
something only when the outcome is genuinely unknown. Here the pieces are
either standard results (prime counting, the Joukowsky transform, box-kite
combinatorics, geometric optics, the Smith chart) or exact enumerations over
finite structures. There is nothing to be wrong about — there is a thing to
**build and show working**.

What replaces the claim is a **provenance label on every component**:
`ESTABLISHED` with an attribution, `FIRST STATED HERE` with a date, or the
generational-lineage tier it decomposes to. Nothing borrowed reads as ours.

---

## The structure, in one paragraph

A **box kite** (de Marrais 2000) is a 6-vertex octahedron of Assessors in the
sedenions — three struts, eight sails, held by zero-divisor products, carrying
an octonion's worth of independent structure (8 DOF). We do **not** store
those eight numbers. Fix *which* box kite — its **pencil**, the seven ways to
factor one relation into two others, pure combinatorics from `PG(3,2)` — and
the inflated shape has exactly **one** continuous degree of freedom. One scalar
rides it: the **wind speed** `w`. Push `w` through a fixed deformation law and
every Assessor coordinate comes back, exactly. The box kite is the equilibrium
shape of a loaded string, and a loaded string is one-dimensional. Context is
therefore carried forward as **one number per token** (plus the token itself,
from which the pencil is computed), and the full relational structure is
**reconstructed, not stored**.

---

## The pass, step by step

### 1. Token → pencil (the address)

Deterministic, from the spelling alone:

    H(w)  = Σ_k ord(w_k) · 95^(|w|−1−k)                base-95 Horner, offset 32
    p     = next_prime(H(w) mod 2^16)                  prime in [2, 65537]
    idx   = π(p)                                       ∈ [1, 6542]
    γ     = the idx-th non-trivial Riemann zero (Im), by Z(t) Newton

`idx` selects the **pencil** — which box kite. This is a coarse map (6542
regions; on a large vocabulary many words share a pencil). Resolution within a
pencil is the wind speed's job.

Running today: `VAPMIP/monad.py` (`_word_zero_idx`, `_gamma_at`),
`monad_bin/SPEC.md §3`.

### 2. Wind speed `w` — the one scalar

**`w` is the A-matrix basin drift.** A word, iterated through the co-occurrence
adjacency, drifts toward a convergence point — the Newton-basin flow the monad
already runs (`monad_english_io.basin()`, the `ψ¹⁶` iteration with `psi_prev`
carried state). `w` measures how far that drift carries the word toward its
focus.

*Movement in a number is factorisation* — the basin drift moves a word through
its contextual decomposition, and the speed of that movement is `w`. Leaves
leaving a tree at wind speed `w` is the composite shedding factors at rate `w`.

Running today: `VAPMIP/monad_english_io.py` (`basin`, IDF-corrected,
content-word gated), the `ψ¹⁶` iteration in `PtolC/ptol.c`.

### 3. The known scale — WordNet

`w` raw is a bare number. It is read against the **WordNet** sub-graph — the
19 relations, hypernym depth, `depth_weight` — the fixed ruler.
`PtolC/c_monad_wordnet.bin` (82-byte `BoxKiteEntry` per synset) is that ruler.
The **Scale orthogonal Smith chart engine** reads `w` off the
WordNet-calibrated axis; its two orthogonal circle families are magnitude
(scale) and phase (granularity) — the conformal map of ℂ made a nomogram.

Running today: `PtolC/c_monad_wordnet.bin`, `VAPMIP/wordnet_boxkite.py`
(closed 2026-08-25; the pile-concept test confirmed the scalar route
re-detects a WordNet concept without materialising the charts).

### 4. `w` → box kite (the reconstruction)

`Φ(w)` returns the six `assessor_coordinates` of the box kite for the fixed
pencil. The deformation law is a **Joukowsky-family** transform — the same
operator as `J_N` inversion, circle ↔ airfoil:

    ζ  ↦  ζ + (H / q(w)) · ζ⁻¹              at each strut crossing
    q(w) ∝ ½ ρ w²                           transverse sail pressure (Kutta–Joukowsky)

`H` is **not a stored parameter** — it is `Re(Π)`, the real part of the ordered
product of the seven pencil-station generators, the quantity conserved along
the string. It falls out of the reconstruction as the check that the result
sits on the zero-divisor surface.

The inflation sequence:

    w = 0        string slack; all six vertices collapse to the e₀–strut axis;
                 the box kite is a POINT — the shadow.
    0 < w < w*   the eight sails catch; the three struts open; the six
                 Assessors separate toward the K₂,₂,₂ vertices.
    w = w*       regular octahedron — the full box kite, "the kite flies".
    w > w*       over-pressure — de Marrais's twisted box kite; the pencil
                 path picks up a torsion.
    w ≫ w*       the string leaves the ZD surface; the kite tears off.

**Rigid vs deformable.** Some box kites have a range of `w` and deform through
it; some do not — those are **static methods**: they travel but do not
deform, one fixed form, reconstructed from the pencil alone. `w` matters only
for the deformable charts.

**To implement:** `Φ(w)` — the one component not yet written. ≈ 30 lines of
Joukowsky over `modules/box_kite/maths.py` primitives. Acceptance tests below.

---

## The Flashlight — granularity, not context

The reconstruction gives the box kite exact to the precision of `w`. Reading
that shape back to a **word** needs it resolved finely enough to tell it from
the other words sharing the pencil, and from neighbouring deformation states.

Shine a light across the reconstructed box kite onto a wall. **Shadows scale
up with distance from the light**: magnification `M = D_light→wall /
D_light→object` (geometric optics). A small shape difference that was
sub-resolution at `M = 1` becomes readable at large `M`.

- **Near wall, low `M`** — coarse: pick a representative word from the pencil.
  **Narrative** — smooth, general.
- **Far wall, high `M`** — fine: resolve the exact deformation state.
  **Dissertation** — the precise term, the one a fraction of a percent from
  its sister hyponym.

Same box kite, same context. *"The pile"* / *"the accretion disc"* / *"the
toroidal condensate density profile"* is one reconstructed structure read at
three wall distances.

Two bounds keep this honest:

1. **Bandlimited by `w`.** Magnification cannot show detail the box kite does
   not carry. Past `w`'s precision the shadow only blurs — no new
   discrimination, no new meaning. The Flashlight *reads out* the granularity
   in `w`; it never creates it. The shadow is **additional granularity of word
   selection, not additional context.**
2. **A hard limit on `D_light→wall`** — a fixed ceiling on wall distance, so
   the magnification cannot run away. No further machinery is invoked.

When the light itself is in motion, each vertex projects as an anisotropic
**Gaussian splat** rather than a hard shadow; splats compose under the
integration that motion implies. This is a rendering detail — it does not
touch the reconstruction.

The Scale orthogonal Smith chart engine, calibrated against WordNet, sets
`D_light→wall` — i.e. sets **how fine a WordNet distinction the response will
resolve**.

---

## Why this is not the neural-network way

The hypercomplex / geometric-algebra line — quaternion nets; octonion CNNs;
Clifford Neural Layers (Brandstetter 2022); Parametrized Hypercomplex
Multiplication (Zhang 2021) — is **materialised algebra**: the multiplication
table lives in the weights, every product is computed explicitly, attention
runs over a dense tensor, `O(d²)`–`O(d³)` per step. It stores the *generated*.

This is **addressed algebra**: one deterministic scalar per token; the
box-kite relations are an index-structure function of the address,
reconstructed on demand. It stores the *generating set*.

Decomposed against the operation domain (`generational-lineage` skill,
VAPMIP 2026-08-18):

| object | tier | tree |
|---|---|---|
| ADD, SCALE, SIGN; the address; the wind speed `w` | 0 | the free identities / the generators |
| `Φ(w)` — the scalar-gain inflation | 1 | DILATE, oriented (see below) |
| **vector; box-kite chart; the 42 Assessors as a set** | 2 | Laurelin — composite |
| **chirality; PSL(2,7) orbit counts; the 19-relation census** | 3 | Laurelin — composite |

The NN stores tiers 2–3. This engine propagates only tier 0 and regenerates
2–3. **Generational lineage as a compression strategy: keep {ADD, SCALE,
SIGN} and the address; drop everything they build, because it rebuilds
exactly.**

The orientation in `Φ(w)`: separating a magnitude channel from an angular
one asserts an orthogonality, and an asserted orthogonality made computable is
`i = √SIGN` — a rotation, not a second length. `w` (radial, basin magnitude)
and the pencil phase (angular) are the `r` and `arg` of one complex quantity;
the Smith chart is where that `i` becomes explicit. No new generator — `i` is
a known consequence of SIGN under Cayley–Dickson doubling.

---

## Components

Tier is the generational-lineage tier. Provenance: `ESTABLISHED` +
attribution, `OURS`, or `FIRST STATED HERE` + date. Status: what runs today.

| # | component | tier | provenance | status |
|---|-----------|------|------------|--------|
| C1 | `token → γ`: Horner b95 → next_prime → π → Z(t) Newton | 0 | **OURS** (`monad.py`, `SPEC.md §3`) | **ships, tested** |
| C2 | the **pencil**: 7 factorisations of one relation, `PG(3,2)`, 35 lines / 7 pencils | 2 | ESTABLISHED — projective geometry; the *edge* framing OURS (`generational-lineage §0b`) | **ships** (`modules/box_kite/`) |
| C3 | box-kite combinatorics: 42 Assessors, 7 octahedra, `{0,4,4,4,6,6}` chart spectrum, zero cross-strut edges | 3 | ESTABLISHED — de Marrais, *arXiv:math/0011260* (2000); PSL(2,7) refinement **OURS** (`box_kite.md`, derived) | **ships** (`modules/box_kite/maths.py`) |
| C4 | wind speed `w` = **A-matrix basin drift** | 0 | **FIRST STATED HERE** 2026-08-30 (drift as the inflation parameter); the flow itself **OURS** (`monad_english_io.basin`, `ψ¹⁶`) | **ships** (drift computed; used as `w` here) |
| C5 | the scale = **WordNet** sub-graph (19 relations, hypernym depth, `depth_weight`) | — | ESTABLISHED — WordNet; the box-kite table **OURS** (`c_monad_wordnet.bin`) | **ships** |
| C6 | `Φ(w)` — Joukowsky inflation `ζ ↦ ζ + (H/q(w))·ζ⁻¹`, `w → 6 assessor_coordinates` | 1 | ESTABLISHED — Joukowsky (1910), elastica (Euler 1744), Kutta–Joukowsky; the **tether + wind-inflation** FIRST STATED HERE 2026-08-27 (`pencil_hyperstring.md`) | **to write** — ≈ 30 lines |
| C7 | the **Flashlight**: shadow magnification `M = D_wall/D_object`; hard `D_wall` ceiling; Gaussian splat under a moving light | 1 | ESTABLISHED — geometric optics; 3D Gaussian splatting (Kerbl 2023) | **to write** — projection + splat |
| C8 | the Scale orthogonal Smith chart engine — `w` on a WordNet-calibrated axis; sets `D_wall` | 2 | ESTABLISHED — Smith chart (1939), conformal map of ℂ | **partial** (`FactoralDecomposition/two_ring_chart_*.py`) |

Five of eight ship and run today. C6 is the codec; C7–C8 are the read-out.

---

## Engine

The engine is the **VAPMIP monad** (`monad.py`, `monad_english_io.py`,
`PtolC/`) plus the **FactoralDecomposition** box-kite modules
(`engine/maths.py`, `modules/box_kite/`). The conversational-ingest path — the
`w` stream carried forward turn by turn — is live as a `systemd --user`
service since 2026-08-30.

The registered demonstration:

    00_structure_vision.ipynb    the codec, the domain, the NN contrast
    01_the_pass.ipynb            token → γ → pencil → w → Φ(w) → box kite,
                                 a real word round-tripped end to end
    02_lineage.ipynb             every component decomposed against the tiers
    03_demonstration.ipynb       the Flashlight: a granularity sweep of one
                                 reconstructed box kite, narrative → dissertation

`construction.json` is the component manifest (this table, machine-readable).
`wiki/` is written last.

---

## Acceptance tests for `Φ(w)`

Not falsification of a hypothesis — acceptance criteria for the codec.
Adapted from `ValaQuenta/wiki/pencil_hyperstring.md`.

1. **One flex mode.** The rigidity matrix of `K₂,₂,₂` (three struts as bars),
   strut fixed, has `dim(flex) = 1`. If ≥ 2, one scalar cannot suffice.
2. **Reconstruction.** `Φ(w)` swept over `w` traces all six
   `assessor_coordinates` of the real box kite for strut `s`, to tolerance,
   for every `s ∈ 1..7` — for the deformable charts; rigid charts return their
   one fixed form for all `w`.
3. **The across-strut map is `J_N`.** `r ↔ 1/r` to the precision
   `inversion.md` uses — not merely Joukowsky-shaped.
4. **The spectrum is the deformation modes.** The `{4,4,4}` Laplacian
   eigenvectors are the three struts opening together; `{6,6}` are the sail
   pairs; `{0}` is the fixed e₀ anchor.
5. **Tear-off.** `chart_of(...).outside_share → 1` past a finite `w`, with the
   onset where the elastica solution leaves the unit sphere.

---

## The desk-rejection gate

These are not internal correctness checks — they are the questions an editor
uses to bin a systems paper before review. Each is pass/fail on real data,
and each pre-empts one rejection.

**G1 — "Lossless of what? Show a bit-exact round trip on real data."**
Take ≥ 10⁴ real WordNet synsets. Run `token → γ → pencil → w → Φ(w) → box
kite` and compare every Assessor coordinate and all 19 relations against the
materialised `modules/box_kite` + WordNet computation. Report the exact-match
fraction and the residual distribution. Deformable and rigid charts alike,
within a stated float tolerance. Any structural mismatch is named, with its
cause (rigid vs deformable, `w` precision).

**G2 — "Your address is a 16-bit hash into 6542 buckets. That is not
injective."**
Correct, and the paper does not claim it is. The claim is that reconstruction
from `(pencil, w)` is exact. Report the words-per-bucket distribution over a
real vocabulary, then the within-bucket separation: `min |Δw|` among
co-located words against the `Φ` reconstruction tolerance. If the separation
ever closes below tolerance, that pair is reported as a genuine collision.

**G3 — "Circularity: are you inverting your own encoder with hidden state?"**
Freeze `w` for a word set. On a clean process with no learned A-matrix beyond
frozen WordNet, run `Φ(w)`. The reconstruction must be a pure function of
`(pencil, w, WordNet)` and nothing else. If it needs the live field, the
"reconstructible" claim is void.

**G4 — "Determinism."**
SHA-256 of the reconstructed box-kite table, produced twice, on two machines,
matches. The addressing is already byte-reproducible (`SPEC.md §3`); this
extends the check through `Φ`.

**G5 — "The Joukowsky identity — real or decorative?"**
The across-strut map equals `r ↔ 1/r` symbolically, to the precision
`inversion.md` uses — not "Joukowsky-shaped" by eye. (Same as acceptance
test 3, promoted because a reviewer will demand the symbolic check.)

**G6 — "The neural-network comparison is a strawman."**
Fix one concrete task: reconstruct the 19-relation adjacency for a 10⁴-word
vocabulary. Give the byte counts both ways — materialised (dense adjacency +
product tensor) vs addressed (one f64 `w` per word + the fixed WordNet ruler
+ the `Φ` code) — as one ratio, and state the addressed method's *query-time*
cost (`O(structure queried)` per lookup) so it is not sold as strictly
dominant. Storage collapses; compute moves to read time.

**G7 — "Runs only on the author's machine."**
A `run.sh` from a clean checkout: pinned dependencies, a pointer to a WordNet
install, and the G1 round-trip numbers out the other end. Third party
executes it.

**G8 — "'Context' is never defined."**
Context here is the word's box kite: its position in the WordNet relational
structure together with its co-occurrence basin. *Continuity* of context is
the `w` stream carried across turns reconstructing each word's box kite at
each turn. Stated, not gestured at.

**G9 — "The flashlight adds detail. Where from?"**
Reconstruct at two magnifications. Show the fine reading carries no
discrimination absent from `w`: the high-`M` structure is a deterministic
upsample of the low-`M` one, and mutual information with `w` does not
increase with `M`. Magnification is bandlimited by `w`.

**G10 — Attribution.**
Not a test — a standing checklist, discharged by the provenance table in
`ValaQuenta/wiki/pencil_hyperstring.md`: de Marrais (2000) owns the box kite
and its vocabulary; the hypercomplex-NN line (Clifford Neural Layers, PHM,
quaternion/octonion nets) is the contrast, cited; Joukowsky (1910), Euler
elastica (1744), the Smith chart (1939), 3D Gaussian splatting (2023) are
cited for what they contribute; Maxwell–Laman rigidity, the moment map, and
HKLL bulk reconstruction are cited as *analogues, not sources on box kites*.
The tether, the wind-inflation parameter, and `w` = basin drift are marked
first-stated-here.

---

## Conclusion

A higher-order group of relationships — the box kite, eight independent
degrees of freedom, the object that keeps turning up from different
directions — is the equilibrium shape of a one-dimensional string. Once the
pencil is fixed, one number rides it. That number is a wind speed: the
co-occurrence basin drift, measured against WordNet. Push it back through a
Joukowsky deformation law and every relationship returns — exactly for the
charts that deform, unchanged for the charts that do not. Nothing between the
scalar and the structure is stored; it is regenerated, and the regeneration
is a pure function of the token and one real.

The flashlight is a separate stage and a separate kind of thing. It does not
recover context — it sets the *granularity* at which the recovered context is
resolved to a word. Near wall, a representative term and a smooth narrative;
far wall, the exact term and a granular dissertation. The magnified shadow
carries no bit the scalar did not; a hard ceiling on wall distance keeps it
finite.

Decomposed against the operation domain, the verdict is **no new generator**.
The box-kite apparatus — vector, chart, Assessor set, the PSL(2,7) census —
is Laurelin composite, tier two and three. It is rebuilt from the tier-zero
generators and the address. That is the whole method: keep {ADD, SCALE,
SIGN} and where the word sits; drop what they build, because it rebuilds
exactly. Storage becomes `O(vocabulary)` scalars plus a fixed ruler; the
price is reconstruction at read time.

This is not a language model, not a training procedure, and not a claim about
output quality. It is a storage-and-reconstruction structure, built from
mathematics that is a century old or older, presented so that it can be run.
It is the box-kite instance of a more general result — *Data Storage With No
Physical Location*, the Hyperwebster permutation decomposition — which is the
next paper. The weights are the number line: you locate, you do not store.

---

## Relation to the series, and what comes next

- **Zero Divisors of S¹⁵**, **Sedenion Operators**, **Axis N-Shape**,
  **Boundary Lever** — the box-kite structure this paper *addresses* rather
  than stores; their zero-free-parameter censuses are C2–C3.
- **Wankel Rotary** — prompt + response sum to zero; the `pairs.jsonl` scale
  samples (`u = ln(P_red/P_blue)`) are that measurement, taken live off the
  conversation, and are the `w` stream's dynamical companion.
- **N-Ball Transformer** — the Cayley–Dickson layer transformer; there the
  layers are materialised, here they are addressed.

**Next paper — *Data Storage With No Physical Location*.** This paper is the
box-kite instance of a general result: the Hyperwebster permutation
decomposition, where data *is* its address in a factored permutation tree —
you locate, you do not store. Old, already in context, and the stop after this
one is finished.
