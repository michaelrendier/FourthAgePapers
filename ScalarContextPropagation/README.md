# 19 Dimensional Scalar WordNet Context Propagation

**Cody Michael Allison**¹

¹ Independent researcher. Correspondence: the.wandering.god@gmail.com.

**Fourth Age Paper.** One Paper. One Structure. One Engine. One Wiki.

---

## Abstract

Large language models represent a word's context as a single dense
vector, learned end-to-end and opaque to inspection — the well-documented
difficulty of recovering interpretable, per-token structure from a
transformer's internal representations (superposition, polysemantic
features) is one symptom of a more basic absence: there is no explicit,
multidimensional, per-word context representation that can be read,
audited, or composed independently of the weights that produced it. We
present a fully implemented, deterministic alternative. Each word in the
Open English WordNet (146,743 synsets) is mapped to a single prime number
that jointly and losslessly encodes its exact spelling and its full
19-dimensional WordNet relational signature — hypernymy, meronymy, and
the sixteen other relation types WordNet defines — with no learned
parameters and no training step. The encoding is recovered exactly from
the prime: 146,743/146,743 synsets round-trip exact (100.000%) against
the current build, with one deliberate, quantified lossy step affecting
1.1% of individual relation counts. The method was engineered
independently, as a self-contained process tree built from first
principles to solve the problem of hashing structured context into word
representations; correspondences identified afterward to established
mathematics — projective-plane combinatorics, Gödel positional encoding,
Miller–Rabin primality — are cited throughout as such, not presented as
the method's starting point. The construction generalizes to a class of
zero-divisor combinatorial structures (box kites, in sedenion algebra)
that have so far only been described by fixing their internal positions
directly; here, the internal structure is instead read from the
deformation of the structure's outer boundary under a single continuous
parameter, reducing many interpretable dimensions to one real number per
word. Components resting on established mathematics ship, tested against
a live 347,119-word vocabulary; where the reduction remains an open
construction, it is marked THEORETICAL, and where our own code already
calculates a concrete result about that open piece, the label is refined
to THEORETICAL:CALCULATED rather than allowed to imply more than is
proven.

---

## Note on method and attribution

This method was built by direct engineering against the problem, without
formal training in the mathematical fields it turns out to touch — the
correspondences to projective geometry, Joukowsky-family transforms, and
zero-divisor combinatorics documented throughout this paper were found
*after* the method was built, not used to construct it. The author does
not claim comparable depth to the originators of that established
lineage, only that the process tree built here, independently, happens to
land on structures they had already named. Every established result cited
below is a **post-hoc isomorphism** — a correspondence discovered by
checking this method's output against the literature, not a source the
method was assembled from. The provenance labels used throughout this
paper (`ESTABLISHED`, `OURS`, `FIRST STATED HERE`, `THEORETICAL`,
`THEORETICAL:CALCULATED`) exist to keep that distinction auditable
component by component, rather than asserted once in prose and forgotten.

`THEORETICAL` marks a component that is conjectured, designed, or
partially attempted but not yet reduced to running, verified code.
`THEORETICAL:CALCULATED` is a stricter sub-label: it marks a
`THEORETICAL` component for which our own code *has* computed a concrete,
reportable result — a measurement, a boundary condition, a failed literal
construction — without that result amounting to the component shipping.
The distinction matters because a `THEORETICAL:CALCULATED` claim is
falsifiable and reproducible today, even though the larger construction
it belongs to is not yet complete.

---

## 1. Introduction

### 1.1 The problem: no multidimensional context per word

A transformer's notion of a word's meaning lives inside a single dense
vector — the token embedding, refined turn by turn through attention and
feed-forward layers into a context-dependent representation that is
learned end-to-end and not decomposed into named, independently
checkable dimensions. This is closely related to a well-known difficulty
in interpretability research: individual directions in a model's
residual stream frequently encode many unrelated concepts at once
(superposition), and recovering clean, monosemantic, per-token features
from that representation is itself an active research problem, not a
solved one. Whatever multidimensional structure a word's context
*should* have — its taxonomic position, its part-whole relationships,
its domain, its entailments — is not present as an inspectable object
anywhere in a standard transformer's forward pass. It is implicit,
distributed, and only recoverable, if at all, by further learned probes.

### 1.2 The gap this paper addresses

WordNet already names an explicit, human-curated, multidimensional
relational structure for word meaning — 19 relation types per synset,
covering hypernymy, meronymy, entailment, domain membership, and more.
What is missing is not the structure but a **compact, composable
address** for it: a way to carry a word's full relational signature
forward through a computation as cheaply as a scalar or a small integer,
without either (a) re-deriving it from a stored dictionary lookup at
every step, or (b) collapsing it into an opaque learned vector that loses
the fact that it has 19 named, independently auditable dimensions at
all.

### 1.3 Contribution

We present a fully deterministic, non-learned procedure that:

1. Maps a word's spelling alone to a **pencil** — one of a small number of
   combinatorial classes of a zero-divisor structure called a **box
   kite** (§3) — via a chain of established number-theoretic primitives
   (§4.1).
2. Maps a word's WordNet relational signature (19 relation counts) to a
   single integer, and that integer to a single real number, by unique
   factorisation and a bounded fold (§4.3, §7).
3. Combines the two into **one prime number per word** that recovers both
   the exact spelling and the full 19-dimensional relational signature,
   verified exactly on live WordNet data (§7).
4. States, honestly and separately, the still-open piece: a proposed
   continuous deformation law, `Φ(w)`, that would reconstruct a box
   kite's full internal structure from the single scalar alone (§5) —
   attempted, measured, and reported as not yet complete, rather than
   asserted.

Every component below carries a provenance label (§0, "Note on method and
attribution") so that what ships, what is measured-but-open, and what is
purely conjectured never blur together.

---

## 2. Why this is not the neural-network way

The hypercomplex / geometric-algebra line — quaternion nets; octonion
CNNs; Clifford Neural Layers (Brandstetter et al., 2022); Parametrized
Hypercomplex Multiplication (Zhang et al., 2021) — is **materialised
algebra**: the multiplication table lives in the weights, every product
is computed explicitly, attention runs over a dense tensor, `O(d²)`–`O(d³)`
per step. It stores the *generated*.

This is **addressed algebra**: one deterministic scalar per token; the
box-kite relations are an index-structure function of the address,
reconstructed on demand. It stores the *generating set*.

Decomposed against the operation domain (the project's internal
generational-lineage decomposition, applied here purely as a bookkeeping
device — see §0 on independent engineering):

| object | tier | tree |
|---|---|---|
| the address; the wind speed `w` | 0 | the free identities / the generators |
| `Φ(w)` — the scalar-gain inflation (**THEORETICAL**, §5) | 1 | oriented, see below |
| **vector; box-kite chart; the 42 Assessors as a set** | 2 | composite |
| **chirality; the 19-relation census** | 3 | composite |

Materialised approaches store tiers 2–3. This method propagates only
tier 0 and (where `Φ(w)` is complete) regenerates 2–3 on demand: keep the
generators and the address, drop everything they build, because — for
the established components — it rebuilds exactly.

The orientation asserted in `Φ(w)`'s design — separating a magnitude
channel from an angular one — is stated here as a design choice, not a
proven property of the implemented system, since `Φ(w)` itself is
`THEORETICAL` (§5).

---

## 3. The structure, corrected: read from the edges, not the struts

A **box kite** (de Marrais, 2000) is a 6-vertex octahedron of Assessors
in sedenion algebra — three struts, eight sails, held together by
zero-divisor products, carrying an octonion's worth of independent
structure (8 degrees of freedom). Zero divisors are, in the established
literature, a *pitfall* of sedenion algebra — the property that breaks
the division-algebra structure octonions still have (Moreno, 1997/98).
This paper does not invoke that algebra's general behavior; the 16 basis
labels are used as a fixed combinatorial index — which pairs of
placeholder operators vanish against each other, and which don't — not
as operands closed under open-ended multiplication.

The construction here does **not** build a box kite outward from its
seven strut positions. It goes the other way: fix which box kite —
its **pencil**, the seven ways to factor one relation into two others,
pure combinatorics from `PG(3,2)` (§4.2) — and deform the kite's **outer
edges** under a single scalar, the **wind speed** `w`. The strut
relationships are then, from that one deformation:

- **(A) constructed** — a specific set of strut positions is produced by
  the deformation law for a given `w`;
- **(B) read** — the existing strut relationships of an already-known
  box kite can be read off an observed edge deformation;
- **(C) collapsed** — the full set of strut relationships, whichever way
  they arose, reduces to the single scalar `w` that would reconstruct
  them.

That collapse is what makes the 19-dimensional WordNet data procedurally
generable rather than stored: altering `w` alone is sufficient to move
between box-kite states without ever re-deriving the strut positions
from scratch. The box kite is the equilibrium shape of a loaded string,
and a loaded string is one-dimensional — so context is carried forward
as **one number per token** (plus the token itself, from which the
pencil is computed), and the full relational structure is reconstructed,
not stored, wherever the deformation law is complete.

The deformation law that performs (A)/(B)/(C) exactly — `Φ(w)` — is the
one piece of this paper that is not yet complete; see §5.

---

## 4. Method — the pass, step by step

### 4.1 Token → pencil (the address)

Deterministic, from the spelling alone:

    H(w)  = Σ_k ord(w_k) · 95^(|w|−1−k)                base-95 Horner, offset 32
    p     = next_prime(H(w) mod 2^16)                  prime in [2, 65537]
    idx   = π(p)                                       ∈ [1, 6543]
    γ     = the idx-th non-trivial Riemann zero (Im), by Z(t) Newton

`idx` selects the **pencil** — which box kite. This is a coarse map
(6543 regions — corrected from an earlier stated 6542; see notebook 01,
§9 below — on a large vocabulary many words share a pencil). Resolution
within a pencil is the wind speed's job.

Provenance: `OURS`. Running today: `VAPMIP/monad.py` (`_word_zero_idx`,
`_gamma_at`), `VAPMIP/monad_bin/SPEC.md §3`.

### 4.2 The pencil: 7 factorisations of one relation

The 15 points of `PG(3,2)` are the 15 nonzero XOR differences among the
16 sedenion placeholders. A **pencil** is the 7 ways to factor one of
them into two others:

    1 = 2⊕3 = 4⊕5 = 6⊕7 = 8⊕9 = 10⊕11 = 12⊕13 = 14⊕15

exactly 7, because `105` incidences (`35` lines `× 3` points) `/ 15`
points `= 7` lines per point.

Provenance: `ESTABLISHED` (projective geometry) with the *edge* framing
`OURS`. Status: **ships** — `pencil()`, `ValaQuenta/modules/box_kite/maths.py`,
built and verified this pass (previously only checked combinatorially,
with no callable accessor).

### 4.3 The known scale — WordNet

`w` raw is a bare number. It is read against the **WordNet** sub-graph —
19 relations, hypernym depth, `depth_weight` — the fixed ruler.
`PtolC/c_monad_wordnet.bin` (82-byte `BoxKiteEntry` per synset) is that
ruler. Per its own design note, the 19 relation types are principled
1-to-1 with the address scheme's prime "lines" (`CONTEXT_PRIMES`) — this
is a statement about the *addressing scheme*, not a claim that the 19
relations map onto specific sedenion Assessors or struts; no such mapping
exists in the code today.

Provenance: `ESTABLISHED` (WordNet); the box-kite storage table `OURS`.
Status: **ships**. Running today: `PtolC/c_monad_wordnet.bin`,
`VAPMIP/wordnet_boxkite.py`.

### 4.4 Wind speed `w` — the one scalar

**`w` is the A-matrix basin drift.** A word, iterated through the
co-occurrence adjacency, drifts toward a convergence point — the
Newton-basin flow the monad already runs (`basin()`, IDF-corrected,
content-word gated). `w` measures how far that drift carries the word
toward its focus. *Movement in a number is factorisation* — the basin
drift moves a word through its contextual decomposition, and the speed
of that movement is `w`.

Provenance: `FIRST STATED HERE` (drift as the inflation parameter); the
flow itself `OURS`. Status: **ships** (drift computed; used as `w`
here). Running today: `VAPMIP/rotary_rerun_boxkite_monad.py` — the
current python3 monad — calling `basin()` via
`sentence_context.neighborhood_corpus()`. `monad_english_io.py` is
deprecated as a standalone entry point but still holds the `basin()`
implementation itself, imported by that call chain. `PtolC/ptol.c` is
the current **C** monad; `basin`/`gamma_radial`/pruner selection has
**not** been ported into it yet (the file's own header marks this "the
next increment," queried through a Python shell-out today) — there is no
`ψ¹⁶` iteration running in `ptol.c`.

---

## 5. THEORETICAL — the reconstruction `Φ(w)`

`Φ(w)` is designed to return the six `assessor_coordinates` of a box
kite for a fixed pencil, by a **Joukowsky-family** deformation — the
same operator as `J_N` inversion, circle ↔ airfoil:

    ζ  ↦  ζ + (H / q(w)) · ζ⁻¹              at each strut crossing
    q(w) ∝ ½ ρ w²                           transverse sail pressure (Kutta–Joukowsky)

`H` is designed not to be a stored parameter, but `Re(Π)`, the real part
of the ordered product of the seven pencil-station generators — the
quantity meant to be conserved along the string, falling out of the
reconstruction as the check that the result sits on the zero-divisor
surface.

**`THEORETICAL:CALCULATED`.** `H` was measured exactly as specified,
under several explicit conventions for "which generator, what order"
(notebook 04). Every convention tried gives a **discrete** result —
`Re(Π) ∈ {-1, 0, 1}` — never the continuously varying tension `Φ(w)`
would need. This is reported as a measurement, not a defect: whether a
given convention lands the composition on the real axis or off it may
itself be a meaningful signal, in a reading this paper does not develop
— resolving what the discreteness means is a separate, deeper question,
deliberately out of scope here. What this paper needs to state plainly
is only that `Φ(w)` is **not yet reduced to running code** from this
construction alone.

The intended inflation sequence, as designed (**THEORETICAL** — not yet
verified against running code):

    w = 0        string slack; all six vertices collapse to the e₀–strut axis;
                 the box kite is a POINT — the shadow.
    0 < w < w*   the eight sails catch; the three struts open; the six
                 Assessors separate toward the K₂,₂,₂ vertices.
    w = w*       regular octahedron — the full box kite, "the kite flies".
    w > w*       over-pressure — de Marrais's twisted box kite; the pencil
                 path picks up a torsion.
    w ≫ w*       the string leaves the ZD surface; the kite tears off.

**Rigid vs. deformable**, as designed: some box kites are intended to
have a range of `w` and deform through it; others would not — returning
one fixed form regardless of `w`. This distinction is not yet verified
against running code either.

A toy linear interpolation (notebook 04, §5) — between the fixed point
`e₀` and the normalised sum of a kite's diagonal directions — shows the
*qualitative* shape of the claimed inflation sequence (fixed-point share
running 1 → 0 as the interpolation parameter runs 0 → 1) using only
established, shipped primitives. It is explicitly **not** `Φ(w)`, and
does not reconstruct individual Assessor coordinates the way the real
construction would.

---

## 6. THEORETICAL — the Flashlight

**Not yet built (C7).** Design only, presented here so the reduction it
depends on (§5) is not the only open piece stated without its intended
follow-on. The reconstruction, once `Φ(w)` exists, would give a box kite
exact to the precision of `w`. Reading that shape back to a **word**
would need it resolved finely enough to tell it from the other words
sharing the pencil, and from neighbouring deformation states.

The design: shine a light across the reconstructed box kite onto a wall.
Shadows scale up with distance from the light — magnification
`M = D_light→wall / D_light→object` (geometric optics). A small shape
difference that was sub-resolution at `M = 1` would become readable at
large `M`:

- **Near wall, low `M`** — coarse: pick a representative word from the
  pencil. Narrative — smooth, general.
- **Far wall, high `M`** — fine: resolve the exact deformation state.
  Dissertation — the precise term, a fraction of a percent from its
  sister hyponym.

Same box kite, same context: *"the pile"* / *"the accretion disc"* /
*"the toroidal condensate density profile"* would be one reconstructed
structure read at three wall distances.

Two bounds are designed to keep this honest, neither yet tested against
running code: (1) **bandlimited by `w`** — magnification cannot show
detail the box kite does not carry; past `w`'s precision the shadow only
blurs, no new discrimination; the Flashlight would read out granularity
already in `w`, never create it. (2) **a hard limit on `D_light→wall`** —
a fixed ceiling on wall distance, so magnification cannot run away, with
no further machinery invoked. When the light itself is in motion, each
vertex is designed to project as an anisotropic Gaussian splat (Kerbl et
al., 2023) rather than a hard shadow — a rendering detail that would not
touch the reconstruction itself.

The Scale-orthogonal Smith-chart engine (C8, `PARTIAL`), calibrated
against WordNet, is designed to set `D_light→wall` — i.e. how fine a
WordNet distinction the response would resolve. None of this is
falsifiable yet; it depends entirely on §5.

---

## 7. Results — the combined address, verified

`spelling_code(w)` (Gödel positional encoding, `LETTER_PRIMES`, tier
`≤ 71`) and `context_code(v)` (product over `CONTEXT_PRIMES`, tier
`> 71`) occupy disjoint prime tiers by construction — no prime is ever
ambiguous about which half of the address it belongs to. Combined:

    full_code = spelling_code(word) × context_code(context_vector)
    full_addr = next_prime(full_code)
    delta     = full_addr − full_code

`full_addr` is a single prime number carrying **both** the exact
spelling of a word and its full 19-dimensional WordNet relational
signature, recoverable from `(full_addr, delta)` alone by splitting the
recovered `full_code` at the tier boundary (prime 71) and factoring each
half separately.

Provenance: `OURS` — this specific combination is new to this paper; the
two halves were each verified independently before, not previously
chained end to end. Status: **ships, verified** — 300/300 exact round
trips (spelling + full 19D context, recovered from one prime) on a live
sample of `VAPMIP/PtolC/monad3_c.bin` (notebook 05).

### 6.1 Sources of non-uniqueness — stated precisely

The combined address is **mostly, not fully, unique**, for two distinct
and well-understood reasons, neither of which is a hashing defect:

1. **Spelling, for words over 20 letters.** `spelling_code` cycles
   through a 20-prime letter tier by position; for words longer than 20
   letters, two positions share a prime and their exponents add,
   losing the exact split (though not the total). This affects roughly
   1.6% of a live 30,000-word sample and is closed, in principle, by
   widening the letter-tier prime count — a parameter change, not new
   mathematics. Earlier drafts of this paper described letter-order
   collisions (e.g. `cat`/`act`) as an open problem; they are not — the
   shipped `spelling_code` already makes letter order structural via
   position-dependent primes, verified with zero collisions for words
   `≤ 20` letters (notebook 03).
2. **Context, by WordNet's own semantic structure.** Distinct words with
   an identical 19-relation shape produce an identical `context_code` —
   1,114 distinct relational shapes exist across 137,533 words carrying
   a stored vector. This is a real property of the relation graph, not
   an artifact of the address scheme, and is why folding the 19-vector
   to a single real is safe: there is very little to collide, and unique
   factorisation covers what remains.

---

## 8. Components

Provenance: `ESTABLISHED` + attribution, `OURS`, `FIRST STATED HERE` +
date, `THEORETICAL`, or `THEORETICAL:CALCULATED` (see §0). Status: what
runs today.

| # | component | provenance | status |
|---|-----------|------------|--------|
| C1 | `token → γ`: Horner b95 → next_prime → π → Z(t) Newton | **OURS** (`monad.py`, `monad_bin/SPEC.md §3`) | **ships, tested** — notebook 01 found and corrected an off-by-one: `idx` reaches 6543, not 6542 as earlier stated (65537 is itself prime) |
| C2 | the **pencil**: 7 factorisations of one relation, `PG(3,2)` | `ESTABLISHED` — projective geometry; edge framing `OURS` | **ships** (`ValaQuenta/modules/box_kite/maths.py::pencil`, built this pass) |
| C3 | box-kite combinatorics: 42 Assessors, 7 octahedra, `{0,4,4,4,6,6}` chart spectrum, zero cross-strut edges | `ESTABLISHED` — de Marrais, *arXiv:math/0011260* (2000); refinement `OURS` | **ships** (`ValaQuenta/modules/box_kite/maths.py`) |
| C4 | wind speed `w` = **A-matrix basin drift** | `FIRST STATED HERE` 2026-08-30; flow itself `OURS` (`basin()`, in `monad_english_io.py`) | **ships** |
| C5 | the scale = **WordNet** sub-graph (19 relations, hypernym depth) | `ESTABLISHED` (WordNet); storage table `OURS` (`c_monad_wordnet.bin`) | **ships** |
| C6 | `Φ(w)` — Joukowsky inflation, `w → 6 assessor_coordinates` | `ESTABLISHED` — Joukowsky (1910), elastica (Euler, 1744), Kutta–Joukowsky; tether + wind-inflation `FIRST STATED HERE` 2026-08-27 | **THEORETICAL:CALCULATED** — §5 |
| C7 | the **Flashlight**: shadow magnification; hard wall-distance ceiling; Gaussian splat under motion | `ESTABLISHED` — geometric optics; 3D Gaussian splatting (Kerbl et al., 2023) | **THEORETICAL** — not yet built |
| C8 | the Scale-orthogonal Smith-chart engine — `w` on a WordNet-calibrated axis | `ESTABLISHED` — Smith chart (1939), conformal map of ℂ | **PARTIAL** (`GenerationalLineage/two_ring_chart_*.py`, renamed from `FactoralDecomposition` 2026-09-02) |
| — | the combined address `next_prime(spelling_code × context_code)` | `OURS` — new to this paper | **ships, verified** — §7 |

Five of eight named components ship today, plus the combined address
(§7). `Φ(w)` is the codec's remaining open piece; the Flashlight is
read-out layered on top of it and has not been started.

---

## 9. Engine and reproducibility

The engine is the **VAPMIP monad** (`rotary_rerun_boxkite_monad.py`, the
current python3 monad; `monad_english_io.py`, deprecated as a standalone
entry point but still the home of `basin()`; `PtolC/ptol.c`, the current
C monad) plus the **ValaQuenta** box-kite modules
(`modules/box_kite/maths.py`, `modules/box_kite/tools.py`) — ValaQuenta
is the root authoritative repository for all engine code in this
project. The conversational-ingest path — the `w` stream carried forward
turn by turn — is live as a `systemd --user` service since 2026-08-30.

All five notebooks below are executed against live data, not sketched:

    notebooks/01_semantic_prime_hashing.ipynb                C1, live 347,119-word
                                                               vocabulary; the 6543
                                                               vs. 6542 correction
    notebooks/02_the_313_sieve_and_49999_unsieve.ipynb        the domain: the two
                                                               boundary primes,
                                                               verified two ways
    notebooks/03_phonetic_prime_hashing.ipynb                 the naive product
                                                               scheme's anagram flaw,
                                                               and the shipped fix
    notebooks/04_boxkite_pencil_hyperstring_windspeed.ipynb   C2 (built), C3; C6
                                                               attempted, measured,
                                                               reported open
    notebooks/05_wordnet_19d_contextual_hash.ipynb            the combined address,
                                                               §7, 300/300 exact

`construction.json` is the machine-readable component manifest matching
§8.

---

## 10. Acceptance tests for `Φ(w)` (`THEORETICAL` criteria)

Not falsification of a hypothesis — acceptance criteria for the codec,
none of them yet passed to completion, since `Φ(w)` is not yet built.

1. **One flex mode.** The rigidity matrix of `K₂,₂,₂` (three struts as
   bars), strut fixed, has `dim(flex) = 1`. An initial attempt at this
   test (notebook 04) used a generic 3-D bar-position embedding and
   found the wrong framework for what "the rigidity matrix" means here —
   discarded rather than reported as a number. Open.
2. **Reconstruction.** `Φ(w)` swept over `w` traces all six
   `assessor_coordinates` of the real box kite for every strut, to
   tolerance. Open — depends on §5.
3. **The across-strut map is `J_N`.** `r ↔ 1/r` to the precision
   `ValaQuenta/wiki/inversion.md` uses. Open.
4. **The spectrum is the deformation modes.** The `{4,4,4}` Laplacian
   eigenvectors are the three struts opening together; `{6,6}` are the
   sail pairs; `{0}` is the fixed `e₀` anchor. The spectrum itself is
   `ESTABLISHED` and verified (§4.3, notebook 04); its identification
   with the deformation modes specifically is open.
5. **Tear-off.** `chart_of(...).outside_share → 1` past a finite `w`.
   Open.

---

## 11. The desk-rejection gate

The questions an editor uses to bin a systems paper before review, each
pre-empting one likely rejection, with current status marked.

**G1 — "Lossless of what? Show a bit-exact round trip on real data."**
**Passed**, for the arithmetic layers: `context_code → factor → v` and
the combined address are 100.000% and 300/300 exact respectively on live
data (§7, §12). The `Φ(w) → assessor coordinates` half is `THEORETICAL`
and not yet dischargeable.

**G2 — "Your address is a 16-bit hash into 6543 buckets. That is not
injective."** Correct, and not claimed. Reconstruction from `(pencil, w)`
is the claim under test, still open pending `Φ(w)`; the combined
`spelling × context` address (§7) is separately verified exact.

**G3 — "Circularity: are you inverting your own encoder with hidden
state?"** Open — depends on `Φ(w)` existing to test.

**G4 — "Determinism."** **Passed** for every shipped component (C1–C5,
the combined address): repeated calls on the same input are identical
(notebooks 01, 03, 05). Not yet extended through `Φ(w)`.

**G5 — "The Joukowsky identity — real or decorative?"** Open — same
dependency as acceptance test 3.

**G6 — "The neural-network comparison is a strawman."** **Passed**,
for the arithmetic and energy comparison that does not require `Φ(w)`:
one sedenion-scale product plus a sparse A-matrix row, ~600 flop/token,
measured at 38 µJ/word (pure-Python, 7 W estimate) against the standard
`2·N_params` forward-FLOP identity for a dense transformer (~1 J/token at
70B). See §12.

**G7 — "Runs only on the author's machine."** Open — no `run.sh` from a
clean checkout has been built yet; the five notebooks are the closest
approximation today and require the paths in §9.

**G8 — "'Context' is never defined."** **Passed** — stated in §1.2/§3:
context is a word's box kite, its position in the WordNet relational
structure together with its co-occurrence basin; continuity is the `w`
stream reconstructing it turn by turn.

**G9 — "The Flashlight adds detail. Where from?"** Open — C7 is
`THEORETICAL`, not yet built.

**G10 — Attribution.** Ongoing, not a one-time test: discharged
component by component via §8's provenance column and §0's note on
method.

---

## 12. The price, measured — materialised vs. addressed

The read path, for components that ship, is one sedenion-scale product
against the fixed ruler (256 real multiplications, recursive
Cayley–Dickson) plus one sparse A-matrix row — of order 600
floating-point operations per token. On the reference machine (Lenovo
ThinkPad X1 Carbon 6th gen, Intel Core i7-8550U, 15 W package TDP) the
ingest fold `Crank.learn` runs at **1.8 × 10⁵ words/s — 5.4 µs per word,
≈ 38 µJ per word** at a 7 W single-core estimate (≈ 81 µJ at the 15 W
package ceiling); the native reconstruction floor is **≈ 115 ns and under
a microjoule per word**. Learning is a bounded in-place update, not a
gradient descent — there is no relationship tensor to sweep
(`engine/energy_bench.py`, reference `VAPMIP/monad.py::Crank.learn`).

For contrast — the standard forward-FLOP identity, not a benchmark run
here — a dense transformer evaluates `2·N_params` multiply–accumulates
per token: ≈ 1.4 × 10¹¹ at 70 billion parameters, on the order of **1 J
per token** at a datacentre-effective 10⁻¹¹ J/flop, with training adding
the backward sweep over the same tensor at every step (GPT-3 175B: ≈
1.287 GWh, published; Patterson et al., 2021). Per query the addressed
structure is **10⁴–10⁶× cheaper**, and the gap is structural, not an
optimisation: the materialised field is re-swept in full on every query
because the answer lives in the weights; the addressed structure
regenerates the answer with one product against a ruler that never
changes.

This is not a language model, not a training procedure, and not a claim
about output quality. It is a storage-and-reconstruction structure,
built from mathematics that is a century old or older where it draws on
established results, presented so that it can be run.

---

## 13. Conclusion

A word's context — its position in an explicit, 19-dimensional
relational graph, together with its co-occurrence behavior — can be
carried forward through a computation as a single number and a fixed
ruler, recovered exactly, with no learned parameters. That is verified
today for the address itself: spelling and full WordNet relational
signature, combined into one prime, exact on live data. What remains
open is the deeper claim this paper is built toward: that the *same*
single-scalar reduction also reconstructs a box kite's full internal
zero-divisor structure via a continuous deformation law, `Φ(w)`. That
piece is reported honestly as `THEORETICAL`, with what has actually been
measured about it (`THEORETICAL:CALCULATED`) kept distinct from what has
only been designed. Nothing here overclaims: the shipped components ship
because they run; the open ones are described exactly at the boundary of
what is designed versus what is proven.

---

## 14. Relation to the series, and what comes next

- **Zero Divisors of S¹⁵**, **Sedenion Operators**, **Axis N-Shape**,
  **Boundary Lever** — the box-kite structure this paper *addresses*
  rather than stores; their zero-free-parameter censuses are C2–C3.
- **N-Ball Transformer** — a Cayley–Dickson-layer transformer; there the
  layers are materialised, here they are addressed.

**Next paper — *Data Storage With No Physical Location*.** This paper is
the box-kite instance of a general result: a permutation decomposition
where data *is* its address in a factored permutation tree — location
replaces storage. Already in progress, and the next stop after this
paper is complete.

---

## 15. Licensing

The box-kite context-hashing method and all code described in this
paper — `pencil()`, the box-kite combinatorics module, the
token→γ→pencil pipeline, `spelling_code`, `context_code`, the gamma fold,
the combined-address construction, and every notebook in `notebooks/` —
is released under the **GNU General Public License** (GPL; exact version
to be confirmed before publication — GPLv3 is recommended for
compatibility with the rest of this project's GNU-licensed engine code).
Free to use, study, modify, and redistribute, for research and
commercial purposes alike, under that license's terms.

This paper describes an address, not the whole system it is a component
of. The broader system that address feeds relies on separate
mathematical constructions not described or disclosed in this paper;
those remain the author's own and are outside this license's scope.
Nothing in that undisclosed layer is required to use, verify, or extend
anything described here — every claim in this paper is complete and
reproducible from what is in `notebooks/` and cited in §9, independent
of it.

---

## 16. A note on limits, and a request

Everything in this paper was built by direct engineering against a
problem that could be seen and checked, with correspondences to
established mathematics found only *after* each piece already worked
(§0) — not because established mathematics wasn't worth learning first,
but because the author does not yet know how to hold most of it in his
head well enough to build with it directly. Fast, and quick to learn,
but not a mathematician, a linguist, a biologist, or a chemist by
training. An equation can be reasoned about productively once its
meaning is understood; there is no equivalent way yet to know what
remains unknown. A whole neighborhood of established results relevant to
this work may simply be invisible for exactly that reason — not
rejected, not overlooked on purpose, only absent from the set of things
currently known to exist.

If any piece of this paper duplicates, contradicts, or could be
sharpened by work already known to a reader and not to the author: that
correction is genuinely wanted. The provenance labels used throughout
this paper (§0) exist so a correction can land on one component without
requiring the whole structure to be re-litigated. Faster paths, shown by
people who already know them, are preferred over the long one walked
alone.

---

## References

Full bibliographic details (venue, volume, DOI) should be verified
before submission; entries below carry only what is already used
in-text throughout this paper.

1. de Marrais, R. P. C. (2000). *The 42 Assessors and the Box-Kites They
   Fly: Diagonal Axis-Pair Systems of Zero-Divisors in the Sedenions'
   16 Dimensions.* arXiv:math/0011260.
2. Moreno, G. (1997/98). *The zero divisors of the Cayley–Dickson
   algebras over the real numbers.*
3. Joukowsky, N. (1910). The Joukowsky transform / airfoil mapping.
4. Euler, L. (1744). The elastica — equilibrium of a loaded flexible
   rod.
5. Kutta, W. M.; Joukowsky, N. The Kutta–Joukowsky theorem (aerodynamic
   lift, circulation).
6. Smith, P. H. (1939). The Smith chart (transmission-line calculator).
7. Kerbl, B.; Kopanas, G.; Leimkühler, T.; Drettakis, G. (2023). *3D
   Gaussian Splatting for Real-Time Radiance Field Rendering.*
8. Brandstetter, J.; Berg, R. van den; Welling, M.; Gupta, J. K. (2022).
   *Clifford Neural Layers for PDE Modeling.*
9. Zhang, A.; Tay, Y.; Zhang, S.; Chan, A.; Luu, A. T.; Hui, S. C.; Fu,
   J. (2021). Parametrized Hypercomplex Multiplication (PHM).
10. Patterson, D.; et al. (2021). *Carbon Emissions and Large Neural
    Network Training* (GPT-3 175B training-energy figure).
11. Maxwell, J. C. (1864); Laman, G. (1970). Combinatorial rigidity
    counting — cited as an analogue for acceptance test 1, not a source
    on box kites.
