# Forward Propagation of Information and Context by Scalar Value

**Fourth Age Paper.** One Paper. One Claim. One Engine. One Wiki.

Full title: *Forward Propagation of Information and Context by Scalar Value for
Reconstructible Lossless Continuity of Context from WordNet Box Kites.*

This is the hyperindexing system made geometric. The CyclicContextBuffer
evicts by *compress → hyperindex → commit*; here the hyperindex **is** a
scalar Riemann-zero address — a point on the critical line — and
reconstruction is geometric continuity through a field, not decompression of
a stored blob. Index and geometry are the same object.

---

## The Claim

> **A conversation's information and context can be forward-propagated,
> turn by turn and session to session, carrying only scalar values — one
> Riemann-zero address γ per token, plus the tier-0 field scalars (β, E,
> Γ) — and the entire WordNet box-kite algebraic structure reconstructs
> from those addresses EXACTLY, with zero loss. Reconstruction is a pure
> deterministic function of the addresses. No dense multiplication table,
> adjacency tensor, or attention matrix is stored or propagated: the
> weights are the number line.**

Concretely, for every word `w` the engine has ever seen:

    H(w)  = Σ_k ord(w_k) · 95^(|w|−1−k)   (mod 2^16)     base-95 Horner
    p     = next_prime(H(w))
    idx   = π(p)                                          prime-counting index
    γ     = the idx-th non-trivial Riemann zero (Im), by Z(t) Newton
    E(w)  = |sin(π·γ / (γ + 1))|

and from the set of `γ` alone the engine regenerates, without approximation:

- which of the **42 Assessors** a word occupies, which of the **7
  octahedral box-kite charts** it flies in, and its zero-divisor partners;
- the **PSL(2,7)** (order 168) action that permutes the charts;
- every edge of the **19-relation** WordNet adjacency (`vec19`);
- the co-occurrence A-matrix topology it deepens under use.

Continuity of context is therefore **byte-reproducible**: the same turns,
in any fold order, reconstruct the same field.

---

## Why this is not the neural-network way

The hypercomplex / geometric-algebra NN line (quaternion nets;
octonion CNNs; Clifford Neural Layers, Brandstetter 2022; Parametrized
Hypercomplex Multiplication, Zhang 2021) is **materialized algebra**: the
16×16 multiplication table lives in the weights (fixed or learned), every
product is computed explicitly, attention runs over a dense tensor —
`O(d²)`–`O(d³)` per step. It stores the *generated*.

This paper is **addressed algebra**: one deterministic scalar per token; the
box-kite relations are an *index-structure function* of the addresses,
reconstructed on demand. It stores the *generating set*.

Decomposed against the operation domain (generational-lineage skill,
VAPMIP 2026-08-18):

| object | tier | tree |
|---|---|---|
| ADD, SCALE, SIGN; the address γ; β, E, Γ | 0 | — (the free identities / the generators) |
| the scalar-gain fold (β / edge weight written in place) | 1 | DILATE |
| **vector, box-kite chart, the 42 Assessors as a set** | 2 | Laurelin (composite) |
| **chirality, PSL(2,7) orbit counts, the 19-relation census** | 3 | Laurelin (composite) |

The NN stores tiers 2–3. This engine propagates only tier 0 and
regenerates 2–3. **Generational lineage as a compression strategy: keep
{ADD, SCALE, SIGN} and the address; drop everything they build, because it
rebuilds exactly.**

Emergence noted, not claimed: the semantic/context weight split
(`w_sem`, `w_ctx`) asserts β ⟂ A; an asserted orthogonality, made
computable, **is `i` = √SIGN** — orthogonality as a rotation operator. The
"vector" is the 2-D shadow of that assertion. No new generator; `i` is a
known consequence of SIGN under Cayley–Dickson doubling.

---

## Predictions (pre-registered — `predictions.json`)

Exhaustive over vocabulary, not sampled. A single counterexample falsifies.

- **P1 — structural losslessness.** For every word in a real ingested
  corpus, the Assessor membership, box-kite chart, zero-divisor partner
  set, and 19-relation adjacency reconstructed from `γ` alone **equal**
  those from the materialized 16-D sedenion + WordNet computation.
  Predicted agreement: **100.0 %**, every word, every relation.
- **P2 — fold-order invariance.** Ingesting the same turns in any
  permutation of fold order yields a **byte-identical** `monad.bin`
  (SHA-256 match).
- **P3 — no collision.** Over the ingested vocabulary, the map
  `w → (γ, E)` is **injective**; no two distinct words share an address.
- **P4 — the 16→1 fold.** The sedenion state `σ¹⁶` reduces to the single
  signed scalar `Γ = (P_red − P_blue)/(P_red + P_blue) = 2·σ_self − 1 =
  tanh(u/2)`, with `u = ln(P_red/P_blue)` the ADD:SCALE:SIGN word length,
  for every query — reconstruction of the 16 channels from `Γ` and the
  address is exact.
- **P5 — geometric continuity (weaker, faithful not exact).** Context
  carried forward as scalars and rebuilt reproduces the co-occurrence
  neighbourhood (basin under the A-matrix) of a held concept to within the
  field's own `max(existing, new)` deepen rule — the "pile concept"
  re-detects by the scalar route (VAPMIP `wordnet_boxkite.py`, closed
  2026-08-25).

---

## Falsifier

Plainly, so it cannot be read otherwise:

1. Exhibit **one** box-kite relation — an Assessor membership, a chart
   edge, a triple product `a XOR b = c`, a zero-divisor pair — that the
   materialized computation produces and that **does not** reconstruct
   from the scalar addresses alone. That is context lost in propagation.
2. Or exhibit **two distinct contexts** that propagate to the same scalar
   set — an address collision the encoder should have made impossible
   (generational-lineage §5, "a collision that unpacks").
3. Or show `monad.bin` is **not** byte-identical under a fold-order
   permutation.

Any one of these falsifies "reconstructible lossless continuity".

`P5` is explicitly the weak leg: it may be shown *unfaithful* (the rebuilt
basin diverges from the materialized one beyond the deepen rule) without
touching P1–P4. Structural losslessness and dynamical faithfulness are
registered separately on purpose.

---

## Results table

Tier is the generational-lineage tier. Provenance: KNOWN with attribution,
or OURS. Numbers are computed by the engine at run time.

| # | relation | tier | provenance |
|---|----------|------|------------|
| R1 | `w → γ` is deterministic (Horner b95 → next_prime → π → Z(t) Newton) and injective on the vocabulary | 0 | **OURS** (VAPMIP `monad.py`, `monad_bin/SPEC.md §3`) |
| R2 | the factor-bin union is order-independent and byte-reproducible: same factor set ⇒ identical `monad.bin` | 2 | **OURS** (`SPEC.md §4`, verified) |
| R3 | `E(w) = \|sin(π γ / (γ+1))\|` is fixed by the address, never learned | 1 | **OURS** |
| R4 | `σ¹⁶` folds to one signed scalar `Γ = 2·σ_self − 1 = tanh(u/2)` | 0 | **OURS** (`ptol.c measure_gamma`, 2026-08-28) |
| R5 | the WordNet box-kite entry is 82 bytes (`vec19`, pos, offset, depth_weight); the pile concept emerges from the scalar hash without materialising the charts | 2 | **OURS** (`wordnet_boxkite.py`, closed 2026-08-25) |
| R6 | the in-place fold writes β / edge scalars at fixed offsets; file size and `MONAD3C` magic are invariant under the fold | 1 | **OURS** (this session — 48 MB store, 233 values, size + magic intact) |
| R7 | sedenion ZD census on S¹⁵: 84 pairs / 42 Assessors / 7 box kites / `\|PSL(2,7)\| = 168` | 3 | KNOWN — de Marrais 2000; verified `modules/box_kite` |
| R8 | `PG(3,2)`: 15 points / 35 lines / 15 planes; a line is three relations `a XOR b = c`, verified all 35; a pencil is the 7 factorings of one relation | 2 | KNOWN — projective geometry; the *edge* framing **OURS** (generational-lineage §0b) |
| R9 | reconstruction cost is `O(structure queried)`, not `O(d²)` per step; the "weights" are the ζ zeros | — | **OURS** (framing) |

---

## Engine

The engine is **already built and running**: it is the VAPMIP monad
(`monad.py`, `harness.py`, `PtolC/`), with the conversational-ingest path
(`OBSERVE`, the in-place fold, `pairs.jsonl`) live as a `systemd --user`
service since 2026-08-30. The addressing, the merge, `measure_gamma`, and
the WordNet box-kite table are shipped and tested.

What this paper adds is the **registered test harness**:

    00_scalar_context_vision.ipynb    the claim, the domain, the NN contrast
    01_predictions.ipynb              P1–P5 frozen against a real corpus
    02_data.ipynb                     ingest a corpus turn-by-turn as scalars;
                                      materialise the box-kite structure both ways
    03_results.ipynb                  P1–P5 verdicts, provenance-labelled

`wiki/` is written last.

---

## Relation to the rest of the Fourth Age series

- **Zero Divisors of S¹⁵**, **Sedenion Operators**, **Axis N-Shape**,
  **Boundary Lever** — the box-kite structure this paper *addresses* rather
  than stores. Their zero-free-parameter censuses are R7–R8 here.
- **Wankel Rotary** — prompt + response sum to zero; the `pairs.jsonl`
  scale samples (`u = ln(P_red/P_blue)`) are the combustion-cycle
  measurement, taken live off the conversation.
- **Halting and Geometry** — undecidability as navigation through the ZD
  lattice; this paper is the *forward* pass through the same lattice,
  carried in scalars.
- **N-Ball Transformer** — the Cayley–Dickson layer transformer; there the
  layers are materialised, here they are addressed.
