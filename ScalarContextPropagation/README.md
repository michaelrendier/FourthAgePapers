# 19 Dimensional Scalar WordNet Context Propagation

**Cody Michael Allison**¹ (Michael Rendier)

¹ Independent researcher. Correspondence: the.wandering.god@gmail.com ·
GitHub: [github.com/michaelrendier](https://github.com/michaelrendier) ·
ORCID: [0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760).

**Fourth Age Paper.** One Paper. One Structure. One Engine. One Wiki.

---

## Abstract

Large language models represent a word's context as a single dense
vector, learned end-to-end and opaque to inspection — the well-documented
difficulty of recovering interpretable, per-token structure from a
transformer's internal representations (superposition, polysemantic
features) is one symptom of a more basic absence: there is no explicit,
multidimensional, per-word context representation that can be read,
audited, or composed independently of the weights that produced it. With
the help of Claude-Code as a coding, research and calculation tool; I
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

## 1. The problem

A transformer's representation of a word's context is a fixed-length
array of floating-point numbers — a few thousand `float32`s per token,
produced by a chain of matrix multiplications and set entirely by
gradient descent during training. Nothing about that array is
addressable the way an ordinary data structure is. There is no field you
can name and read off independently — no `is_a`, no `part_of`, no
`domain` you could log, assert against in a test, or diff between two
runs. Every one of those thousands of numbers depends on every other
one; changing what the vector "means" means retraining, not editing a
field. It is a value with no schema.

This is not a complaint about accuracy — the vectors work, in the sense
that models trained on them perform well. It is a complaint about
**engineering interface**: nothing about a token embedding is
inspectable, versionable, or composable the way a struct, a database
row, or a hash is. You cannot `grep` it. You cannot write
`assert context.is_a("mammal")` and have it mean anything. You cannot
cheaply diff two words' contexts and get back which of a fixed set of
named relations differ.

WordNet already has exactly the schema that's missing — 19 named
relation types per synset (hypernym, meronym, entailment, domain, and
the rest), curated by hand, stable across builds. What doesn't exist is
a way to carry that schema forward *as an address*: something as small
and portable as a hash or an integer, computed with no training step,
exactly recoverable back into the 19 named fields it came from. That
gap — a compact, deterministic, fully-recoverable address for a word's
WordNet relational record, plus its exact spelling, in one value — is
what the rest of this paper builds, one piece of code at a time.

---

## 2. Notation, disambiguation, and install

### 2.1 Notation

Every component described in this paper carries one of five labels,
applied consistently rather than asserted once in prose and forgotten:

- **`ESTABLISHED`** — mathematics or computer science that predates this
  project, cited to its source.
- **`OURS`** — code or a specific design choice built for this project,
  not published elsewhere.
- **`FIRST STATED HERE`** — a specific claim or construction, dated, not
  found stated this way anywhere else the author has checked.
- **`THEORETICAL`** — designed, or partially attempted, but not yet
  reduced to running, verified code.
- **`THEORETICAL:CALCULATED`** — a `THEORETICAL` component for which
  code has nonetheless computed a concrete, reportable result (a
  measurement, a boundary condition, a failed literal construction)
  without the component itself shipping. The distinction matters because
  a `THEORETICAL:CALCULATED` claim is falsifiable and reproducible
  today, even though the larger construction it belongs to is not.

### 2.2 Disambiguation — the code came first

Every piece of code in this paper was built directly against the
problem in §1, without first consulting the literature it turns out to
correspond to. Correspondences to established mathematics —
projective-plane combinatorics, Gödel positional encoding,
Miller–Rabin primality, sedenion zero-divisor structures — were noticed
*after* the code already worked, by checking its output against the
literature, not used to construct the code in the first place. Where a
mathematical name appears below, it is a label applied after the fact
for a reader who already knows that name; it played no role in how the
code was written, and nothing in this paper requires knowing it to
follow the code. The reverse is stated with the same care: the small
number of pieces marked `FIRST STATED HERE` are exactly that — not
found named this way anywhere else the author has checked, not claimed
as more than that either.

### 2.3 Install

    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    python3 -c "import nltk; nltk.download('wordnet')"

`requirements.txt` is in this directory and is short (`nltk`, `jupyter`)
— it installs the same way on Linux, macOS, and Windows. The five
notebooks under `notebooks/` are the executable form of every result in
this paper; each runs directly once the venv above is active and this
repository's sibling repos (`VAPMIP`, `ValaQuenta`) are checked out
alongside it.

---

## 3. The structure, corrected: read from the edges, not the struts

This section defines two things: the mathematical object (established,
not this paper's), and one engineering move applied to it (not
established — first done here). Kept deliberately separate, because they
have different owners.

### 3.1 The box kite, established

Sedenions are a 16-dimensional number system built by doubling the
complex numbers three times over (ℝ → ℂ → ℍ → 𝕆 → 𝕊 — reals,
complexes, quaternions, octonions, sedenions). Each doubling costs a
property: complex numbers lose ordering, quaternions lose commutativity
(`ab ≠ ba`), octonions lose associativity (`(ab)c ≠ a(bc)`). Sedenions
lose one more: they are the first level with **zero divisors** — nonzero
numbers `x` and `y` whose product `xy` is exactly zero, something that
cannot happen for ordinary reals, complexes, or even octonions. In the
established literature this is treated as a *defect* to characterize,
not a feature to use (Moreno, 1997/98, showed the full set of these zero
divisors forms a continuous shape).

de Marrais (2000) found something sharper underneath that continuous
shape: the zero divisors are not shapeless — they organize into an
**exactly enumerable, finite combinatorial structure**. No sampling, no
statistics, no approximation — a fixed, fully-listable fact about this
one 16-dimensional number system, the same way a graph's edge list or a
finite group's multiplication table is a fixed, fully-listable fact.
Concretely: the 16 basis directions pair up into 42 planes (**Assessors**)
that contain zero-dividing pairs; the 42 Assessors sort into 7 groups of
6 (**box kites**, one per **strut**); each group of 6 forms the edge
graph of an **octahedron** — the same six-vertex, twelve-edge solid as a
d8 die. The exact object this reduces to is `PSL(2,7)`, a specific,
well-known group of 168 symmetries (also written `GL(3,2)`, the
invertible 3×3 grids of 0s and 1s) that is exactly the symmetry group of
the **Fano plane** — the smallest possible projective plane, 7 points
and 7 lines, 3 points per line.[^psl27] None of this — the zero-divisor count,
the 7-octahedra structure, the identification with `PSL(2,7)` — is
proposed here; it is computed directly from the sedenion multiplication
table and checked against de Marrais's published counts (verified in
`ValaQuenta/modules/box_kite/maths.py::verify_counts`).

[^psl27]: The 7 box-kite charts have zero cross-strut edges — mutually
    disconnected under zero-divisor adjacency, an open question in this
    project's own earlier notes on whether any group action glues them
    into one atlas (`ValaQuenta/wiki/box_kite.md`). Checked directly: of
    the 168 elements of `PSL(2,7)`, exactly 21 preserve the zero-divisor
    structure (not just the strut labeling) — and that 21-element subset
    is itself a subgroup, still transitive across all 7 struts. Every
    pair of charts is joined by a structure-preserving group element; the
    atlas is connected by group action, not by any edge
    (`ContextPlease/claude/scratchpad/2026-08-13_apex_path/psl27_strut_action.py`,
    verified 2026-09-17).

A **pencil**, in the classical, established sense used here, is simply
*all the lines through one shared point*. Over the Fano plane's 15
underlying relations, fixing one relation and asking "which pairs of the
other relations combine to reconstruct it" always has exactly 7 answers
— a pencil of 7. This too is checked directly, not asserted
(`ValaQuenta/modules/box_kite/maths.py::pencil`, `verify_pencil_counts`).

### 3.2 The engineering move: what happens if you attach a string?

Everything in §3.1 is established mathematics, decades old. What is not
established, and belongs to this project alone, is a much simpler
question asked of it: a box kite is *named* after a real, physical kite
— so what happens if a piece of that finite combinatorial structure is
treated as if it really were one, and a string is tied to it?

Suppose it can be. A physical kite string needs an anchor — one fixed
point that does not move, so that wind passing the kite has something
to pull *against*, which is what makes a kite fly rather than simply
blow away. Attach that anchor to a single point of the box-kite
structure, and immediately there is a problem a physical kite string
never has: the structure it is anchored to is not one shape but seven
simultaneous octahedra sharing that structure. A single string attached
at one point does not reach the rest of the kite by one path — by
necessity, reaching outward from one anchor into a structure this
interconnected produces several routes at once, not one. Counting those
routes precisely is exactly the classical pencil construction from
§3.1: fixing one point and asking how many ways the rest of the
structure combines to reach back to it. The answer, here as there, is
7. Recognizing that count as a textbook pencil — rather than continuing
to describe it from scratch as "the multiple paths from one point" — is
the only place established terminology was borrowed in this section;
the anchoring, the string, and the question that produced the count are
not from that literature.

With an anchor point identified, wind is a real, physical next question
for a kite: does tension develop in the string, and does the kite's
shape deform under that wind, the way a real airfoil does? Testing this
directly against the finite structure gave a genuinely mixed answer —
tension on some of the 7 pencil paths and not others, real deformation
under some conditions and rigidity under others. That mixed result,
rather than a clean yes or no, is what motivated treating the whole box
kite as **one object** — a relationship
snapshot — anchored at an unmoving point, with a single scalar, **wind
speed**, standing in for however much tension and deformation that wind
produces. The deformation law that would make **the strut relationships
reconstructible from that one scalar** is `Φ(w)`, and is the subject of
§5. Everything about the box kite itself is established; the anchor,
the wind, and the reduction to one scalar are this paper's contribution.

### 3.3 The collapse

Given the anchor and the wind, the strut relationships are, from the one
deformation:

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

### 4.2 The pencil, made callable

The pencil itself is defined in §3.1; concretely, for the anchor relation
`1`:

    1 = 2⊕3 = 4⊕5 = 6⊕7 = 8⊕9 = 10⊕11 = 12⊕13 = 14⊕15

Provenance: `ESTABLISHED` (projective geometry) with the *edge* framing
and the anchor-and-string reading of it (§3.2) `OURS`. Status: **ships** —
`pencil()`, `ValaQuenta/modules/box_kite/maths.py`, built and verified
this pass. Before this, the pencil was checked only combinatorially, with
no callable accessor anywhere in the codebase.

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

### 5.1 Earlier evidence: tension, deformability, and lift, measured

The wind-and-tension question in §3.2 was tested once before this
session, against real address data (`VAPMIP/monad_sedenion_addresses.pkl`,
3,288 addresses), and documented in
`VAPMIP/docs/wiki/Tuning-the-Engine/30_wind_lift_and_the_monads_original_gate.md`
(2026-08-23). Three results from that pass, `THEORETICAL:CALCULATED`,
carried forward here because they measure the same object `Φ(w)` still
needs to reconstruct:

- **The anchor, measured as immovable.** `e₀`'s commutator vanishes
  against all 16 basis directions — total calm at the anchor — while all
  210 ordered pairs among the 15 imaginary directions have a *nonzero*
  commutator: full rotational flow the instant anything steps off that
  one point. A single point of total calm, and full rotational flow
  everywhere else, is not a gradual boundary; it is exact.
- **Deformability, genuinely mixed, as anticipated in §3.2.** A wind
  source built from the box kite's *own* symmetric diagonals gave the
  same deformed spectrum on three different struts — rigid,
  non-discriminating. Switching the wind source to three *real*
  addresses' own energy split gave three genuinely different deformed
  spectra — elastic. The lesson measured directly: a wind source drawn
  from the kite's own structure is rigid; one drawn from real, asymmetric
  content is not.
- **Lift, tested across all 105 four-cycles on all 7 struts, split three
  ways**: 53 positive, 31 negative, 21 zero. Not a continuum — a discrete
  tri-state split, clustering at `±4, ±8, ±16, 0`. This is the same
  *shape* of result the `Re(Π) ∈ {-1, 0, 1}` measurement below finds
  again, independently, a session later.

### 5.2 This session: `H = Re(Π)`, measured discrete

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

### 7.1 Sources of non-uniqueness — stated precisely

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

Nothing about the box kite itself is new (§3.1) — the zero divisors, the
7 octahedra, `PSL(2,7)`, the pencil, are de Marrais's and the wider
literature's. What is new is a much smaller question asked of that
established object: attach a string to it at one unmoving point, and ask
what a wind passing through would do (§3.2). That question, not the
mathematics it was asked of, is this paper's contribution.

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
is released under the **GNU General Public License, version 3 (GPLv3)**.
Free to use, study, modify, and redistribute, for research and
commercial purposes alike, under that license's terms. Full license
text: `LICENSE` in this directory.

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
