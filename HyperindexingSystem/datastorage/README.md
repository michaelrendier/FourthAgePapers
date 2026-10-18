# Data Storage Without a Physical Location

**Fourth Age Paper.** One Paper. One Structure. One Engine. One Wiki.

---

## Abstract

Every string already has a number — Horner's method is a bijection between
strings and the non-negative integers, and it assigns nothing; it reveals what
was always there. A store built on that fact holds no data. It holds an
**index**: an address and a length. To keep the address space navigable at
low cost, the traversal is a **de Bruijn sequence** — the shortest cyclic
string in which every length-`n` window occurs exactly once, so moving between
neighbouring addresses is a single symbol shift rather than a walk down a
factorial tree. Each ingested item is written to a ledger as `(index,
timestamp)`. The ledger is itself text, so it has its own index; taking the
index of the index, recursively, folds the entire ingested corpus into a
single fixed-width number. The octonion — the last normed division algebra,
where multiplication still preserves length but no longer associates — carries
the recursion's depth: eight limbs, order-dependent, enough structure for the
fold to reach **256 bits** without collapsing to a plain hash. What is stored
is that one number, the de Bruijn generator, and the decode model. Nothing
else. Nothing is compressed, because nothing is stored: once the content is
free at its address, the only quantities left to account for are the **cost**
to reach an address and the **change** between one and the next. This was the
original design for AI context continuity and persistent memory; it is
presented here as the shared ancestor of the two structures that replaced it,
and as the first working definition of **hyperindexing** — the formal
treatment deferred.

---

## The departure from the template

No claim, no prediction, no Holcus, no σ verification. This is an **engineering
structure** — a storage construction assembled from established mathematics —
and, unlike the others in the series, a **retrospective**: it is old, it
predates the box kites, and its job here is to be written down cleanly and to
name what grew out of it.

Every component carries a provenance label: `ESTABLISHED` with an attribution,
or `FIRST STATED HERE` with a date.

---

## This is not compression — it is cost and change

Compression removes redundancy from stored data: the bytes are kept, in fewer
of them. **Nothing here is compressed, because nothing is stored.** Horner's
method is a bijection — every string is *already* a number — so the store does
not shrink data, it *addresses* it. The 256-bit root is not the corpus made
small; it is the corpus's **address** in the space of all corpora, from which
the corpus is reconstructed by a pure function.

Once you accept that the content is free at its address, only two things are
left to account for, and the whole construction is about them:

- **the cost** — what it takes to *reach* an address and *reconstruct* from
  it: navigating the address space, running `Φ`, unfolding the recursion. The
  de Bruijn permutation (§2) exists to drive this down — from factorial tree
  navigation to `O(1)` steps.
- **the change** — the *delta* between addresses: the local operation that
  moves you from one to the next (a de Bruijn shift, a successor, a limb
  increment), and the transport that keeps content operations consistent
  across the move. Each ledger row (§3) is one timestamped change; the Long
  Path is their sequence.

The working term for this, as used in this paper, is **hyperindexing**: an
address you reconstruct *from*, not a pointer you look *up* — storage-free
(the map holds no table that scales with the content), bijective (the address
is the content, up to a known symmetry), structure-carrying (operations on the
content pull back to operations on the address), recursively foldable (the
address of the address, iterated, reaches a fixed-width root). Its subject
matter is the permutations, partitions, and folds of a cyclic index — one
object seen three ways — accounted for by cost and change, not by entropy and
redundancy. A formal treatment of hyperindexing algorithms is a later,
separate work; here the term is defined only as far as the construction uses
it.

---

## The construction

### 1. The empty Hyperwebster — data as (address, length)

A complete address space for all possible strings is infinite, and searching an
infinite space is not useful. The Hyperwebster
(`PtolemyDesktop/wiki/HyperWebster.md`, nine reduction layers) is what remains
after the infinite space is cut down: Banach–Tarski equivalence classes remove
the redundant interior of the permutation space; lexical filtering restricts to
the neighbourhood of human language; Zipf center-loading and a frequency-sorted
charset pull common words toward the origin.

The core operation is **Horner's bijection**. For a string
`s = (c₀ … cₙ)` over a charset of size `N`:

    H(s) = c₀·Nⁿ + c₁·Nⁿ⁻¹ + … + cₙ₋₁·N + cₙ

Every string maps to exactly one non-negative integer and back. Deterministic,
reversible, **no storage**. The address has always existed; the store does not
assign it, it reveals it.

A piece of data is then two numbers: its **address** `H(s)` and its **length**
`|s|`. Together — the **index**. The bytes are not kept. Their location and
extent are.

### 2. The de Bruijn permutation — the geometric alteration

Navigating the address space naively is a walk down a permutation tree:
factorial branching, `O(n!)` to reach a depth-`n` address. Replace the tree
with a **de Bruijn sequence** `B(k, n)` — the shortest cyclic sequence over a
`k`-symbol alphabet in which every length-`n` word appears exactly once as a
substring. Its length is `kⁿ`, it has zero redundancy, and it is generated by
an Eulerian circuit of the de Bruijn graph (equivalently a Hamiltonian circuit
of the `(n−1)`-graph).

On the de Bruijn sequence:

- every address is a **window position** — one integer in `[0, kⁿ)`;
- moving to an adjacent address is a **single symbol shift** — an `O(1)` edge
  in the de Bruijn graph, not a tree descent;
- the whole relevant space is covered by **one string of minimum length**.

This is the "geometric alteration to reduce computational overhead": the
combinatorial cost of addressing drops from factorial tree navigation to
constant-time steps along a `kⁿ` cycle. `Ptolemy2/Archimedes/Maths/Sequences/
DeBruijnSequences.py` generates the sequence by the standard DFS-on-necklaces
construction.

De Bruijn *positional encoding* is the property that makes this "storage with
no physical location" in the strict sense: any `n` consecutive symbols of the
sequence give the **absolute position** with no coordinate stored anywhere —
the position is reconstructed from the local pattern. The store inherits that
property.

### 3. The ledger — (index, timestamp)

Each ingested item is one row:

    { "index": [address, length], "t": <timestamp> }

appended to a JSON file. The ledger is the ordered record of what was taken in
and when. It is append-only; it is the **Long Path**.

### 4. The recursion — index of the index

The ledger is text. Text has a Hyperwebster index. Compute it. Now the ledger —
the thing that indexes every item — is itself a single `(address, length)`.

Append *that* to a higher ledger, and recurse. Each level indexes the level
below. The recursion converges: the index-of-the-index-of-the-index… collapses
toward one number from which every level, and therefore every ingested item, is
reconstructable. The encoding is **holographic** in the operational sense — the
final number depends on the whole corpus, and the whole corpus is recoverable
from it plus the fixed machinery. This is a Merkle fold with a Horner/octonion
address function in place of a cryptographic hash.

### 5. The octonion — the depth that fits in 256 bits

The Horner integer for an average word is ~130 bits. Split it into **eight
equal-width limbs** and read them as the components of an octonion
`(l₀e₀ … l₇e₇)`. The Cayley–Dickson tower `ℝ → ℂ → ℍ → 𝕆` sheds one property
per doubling — order, then commutativity, then associativity. The octonion is
the **last rung that still preserves length** (`|xy| = |x||y|`, no zero
divisors): the deepest algebra in which the fold stays lossless.

Non-associativity is the feature, not the flaw. It means **the path through the
address space matters** — order-of-operations defines the geometry, exactly as
context is not commutative. The recursion of §4 is an ordered octonion product
of the per-level indices; its depth is carried in the eight limbs; and the
whole fold lands, at the tower's genome rung `T₂₅₆` (`2⁸`), on a single
**256-bit** representation.

*(The Hyperwebster wiki states a 512-bit address at Layer 6; that is the
pre-recursion single-item address. The 256-bit figure here is the fixed-width
root of the recursive fold of §4 — a different quantity, an address in the
space of corpora rather than of items, with the octonion carrying the
recursion depth. The two are not in conflict; the engine reports both.)*

### 6. What is stored

- the **256-bit root**;
- the **de Bruijn generator** `(k, n)` and the charset permutation;
- the **decode model** (the file-type / frequency table, learned or static).

No item bytes. No per-item records beyond what the root unfolds to. The
"database" is one number and the rules for reading it.

---

## Where hyperindexing comes from

The term is used here as defined above — an address you reconstruct from,
accounted for by cost and change. It is not a new invention; it names a
pattern that established mathematics has arrived at from several directions,
each contributing one property:

| line of work | contributes | attribution |
|---|---|---|
| **Gödel numbering** | the index *is* the object, decodable — arithmetization | Gödel (1931) |
| **combinatorial / factorial number systems; ranking–unranking** | a bijective index ↔ combinatorial object with *explicit reconstruction* (unrank) | Laisant (1888); Lehmer; Knuth TAOCP |
| **de Bruijn sequences & positional encoding** | minimal complete traversal of a window-space; absolute position from a local pattern, no coordinate stored | Flye Sainte-Marie (1894); de Bruijn, Good (1946) |
| **space-filling / locality-preserving indices** | one scalar ↔ `n`-D position, invertible, proximity-preserving | Hilbert (1891); Morton / Z-order (1966) |
| **arithmetic coding** | the whole message as one number; every digit depends on the whole | Rissanen (1976) |
| **Merkle DAGs / content addressing** | recursive fold of addresses to a single fixed-width root | Merkle (1979); git; IPFS |
| **Cayley–Dickson / Clifford basis indexing** | the `2ⁿ` basis *is* a binary-address set with an operation on the addresses (XOR + sign cocycle) | Cayley (1845); Dickson (1919); Clifford (1878) |

**The box kite** (companion paper) is the *unranking* case: the address
unranks to a de Marrais box kite — a higher-order relational group in the
sedenions — completed by a physical deformation law (`Φ(w)`, the Joukowsky
wind).

**The Hyperwebster** is the *storage* case: the address unranks to the bytes,
and the recursion folds a whole corpus to one number.

`FIRST STATED HERE` in each: the deformable unranking via a physical law (box
kite paper, 2026-08-27); the recursive octonion fold to a fixed-width root,
and the `(index, timestamp)` ledger as the store's record (this paper). The
category itself — its objects, its models, and its relation to gauge symmetry
— is deferred to a formal treatment after the Ainulindalë and VAPMIP papers.

---

## Why "no physical location" is literal

The bytes have no address in a storage medium because they are not in one. The
only physical artifacts are the 256-bit root, the de Bruijn generator, and the
decode model — none of which grows with the corpus. Retrieval is *navigation*:
unfold the root to the ledger, unrank a row's `(address, length)` to the bytes.
Every step is computation over the address, not a fetch from a location.

This is content addressing (Merkle, git, IPFS) taken to its limit: there, the
address is a hash of content still stored somewhere; here, the address is a
*bijection* to the content, and the content is regenerated from it.

---

## Components

Tier is the generational-lineage tier where one applies. Provenance:
`ESTABLISHED` + attribution, or `FIRST STATED HERE` + date.

| # | component | provenance | status |
|---|-----------|------------|--------|
| D1 | Horner bijection — string ↔ non-negative integer, reversible, no storage | ESTABLISHED — Horner's method | **ships** (`HyperWebster.md` L5; `VAPMIP/monad.py` `_horner_hash`) |
| D2 | reduction layers — Banach–Tarski classes, lexical filter, Zipf center-load, frequency-sorted charset | ESTABLISHED — Banach–Tarski (1924), Zipf (1935) | **ships** (`HyperWebster.md` L1–L4) |
| D3 | de Bruijn sequence `B(k,n)` — minimal complete window traversal; `O(1)` neighbour step | ESTABLISHED — Flye Sainte-Marie (1894), de Bruijn (1946) | **ships** (`Ptolemy2/Archimedes/Maths/Sequences/DeBruijnSequences.py`) |
| D4 | de Bruijn positional encoding — absolute position from a local window, no coordinate stored | ESTABLISHED — de Bruijn positioning | **to wire** into the addressing path |
| D5 | the `(index, timestamp)` ledger — append-only JSON, the Long Path | **FIRST STATED HERE** (as the store's record of ingest) | **to build** |
| D6 | octonion splitting — Horner integer → 8 limbs → octonion; non-associative, length-preserving | ESTABLISHED — Cayley–Dickson; the *linguistic* reading OURS (`HyperWebster.md` L6) | **ships** (L6) |
| D7 | recursive index-of-index fold → single fixed-width root | **FIRST STATED HERE** (the octonion Merkle fold to `T₂₅₆` / 256 bits) | **to build** |
| D8 | HYPER_KEY — the charset permutation as a cryptographic key; the whole space rotates | ESTABLISHED — permutation cipher; OURS (`HyperWebster.md` L9, `Kryptos`) | **ships** (L9) |
| D9 | Amplituhedron paradigm — infinite enumeration replaced by one geometric measurement | ESTABLISHED — Arkani-Hamed & Trnka (2013); the paradigm transfer OURS (L7) | framing |

---

## The desk-rejection gate

The checks an editor uses to bin a storage paper before review. Each pass/fail
on real data.

**G1 — bit-exact round trip.** Ingest a real corpus (≥ 10⁴ items). Fold to the
256-bit root. Unfold and reconstruct every item byte-for-byte. Report the
exact-match fraction (must be 1.0) and, if not, the exact failure and its
cause.

**G2 — the recursion terminates.** Show the index-of-index fold reaches a fixed
width in a bounded number of levels for a corpus of size `M`, and give the
level count as a function of `M`. An unbounded recursion is a rejection.

**G3 — the 256 bits are real, not truncation.** Demonstrate that the root
carries the corpus — i.e. two corpora differing in one byte produce different
roots, and the reconstruction distinguishes them — not that the root is a
128-bit quantity zero-padded, nor a hash with the data kept elsewhere.

**G4 — de Bruijn addressing is `O(1)` per step.** Measure the cost of moving
between `T` neighbouring addresses; it is linear in `T`, not `T·n!`. Give the
constant.

**G5 — determinism.** The root of a fixed corpus, computed twice on two
machines, matches (SHA-256 of the root). The de Bruijn generator and charset
permutation are pinned inputs, reported.

**G6 — the comparison is on cost, not size.** A reviewer will reach for `gzip`
and `zstd --ultra`. Those are compressors — they keep the bytes and shrink
them; this keeps nothing. The honest comparison is against **content
addressing** (a Merkle/IPFS CID): both replace the data with an address. State
the two axes side by side — the **cost** to reconstruct one item (this store:
`O(unfold + unrank)`; a CID: a disk or network fetch of stored bytes) and the
**change** a single ledger row carries (this store: a timestamped
`(address, length)` delta; a CID: a new hash over the changed bytes). Do not
report a "compression ratio"; there is no compression here. Where a
compressor genuinely wins — keeping bytes local for fast sequential read —
say so.

**G7 — third-party run.** A `run.sh` from a clean checkout: pinned deps, a
corpus pointer, the G1 round-trip and the G5 root out the other end.

**G8 — "holographic" is used precisely.** Define it operationally: the root is
a function of the whole corpus, and any prefix of the unfold reconstructs a
corresponding prefix of the corpus. No claim of optical holography, no claim
that a fragment of the root alone reconstructs everything.

**G9 — attribution.** The lineage table above is the checklist. Gödel,
Laisant/Lehmer, de Bruijn, Hilbert/Morton, Rissanen, Merkle, Jacobson,
Cayley–Dickson, Gabor/Valiant cited for what each contributes. First-stated-
here: the `(index, timestamp)` ledger as the store's record, and the recursive
octonion fold to a fixed-width root.

---

## Engine

Shipping: the Hyperwebster reduction layers and Horner bijection
(`PtolemyDesktop` HyperWebster, `VAPMIP/monad.py`), the de Bruijn generator
(`Ptolemy2/Archimedes/Maths/Sequences/DeBruijnSequences.py`), octonion
splitting (`HyperWebster.md` L6), the HYPER_KEY (`Kryptos`). The
octonion-hyperindex-then-commit pattern already runs in **Philadelphos** —
`compress → octonion hyperindex → AuditChain (PtolChain) commit` — which is the
Long Path in miniature.

To build: the `(index, timestamp)` ledger (D5) and the recursive
index-of-index fold to the 256-bit root (D7). The rest is assembly.

    00_structure_vision.ipynb    the empty Hyperwebster, the de Bruijn shift,
                                 the recursion, the octonion depth
    01_the_fold.ipynb            ingest a real corpus → 256-bit root →
                                 reconstruct, byte-exact
    02_where_it_comes_from.ipynb the ancestors of the term, each discharged
    03_cost_and_change.ipynb     G6 — reconstruction cost per item and the
                                 delta a ledger row carries, vs a Merkle CID;
                                 no compression ratio

`wiki/` is written last.

---

## Conclusion

Storage does not require a location. Horner's bijection makes every string a
number that already exists; a de Bruijn sequence makes the number **cheap to
reach**; a ledger records **what changed and when**; and the ledger's own
index, taken recursively, folds an entire corpus into one 256-bit root. The
octonion — the deepest algebra that still preserves length — carries the
recursion's depth into that fixed width, and carries it *ordered*, because the
path through an address space is not commutative any more than context is.
What persists on a disk is the root, the generator, and the decode rules.
Everything else is navigation, and navigation is only two quantities: the
**cost** to reach an address and the **change** between one address and the
next. Nothing is compressed, because nothing is stored.

This was the first design for an AI's context continuity and persistent
memory: one number that unfolds to everything taken in. It has since divided
into its two halves, each now its own Fourth Age paper:

- **the codec** — reconstructing a higher-order relational group from a single
  scalar — is the box kite. *`FourthAgePapers/ScalarContextPropagation/` —
  Forward Propagation of Information and Context by Scalar Value* (written).

- **the persistence** — the working loop that holds an intention, and the
  append-only ledgered record that makes it durable and ordered — is
  ***The Mind's Eye and Paper's Hands***, the next paper in this series. The
  Mind's Eye is the flat held loop (`rehearse` — iteration, not recursion, no
  output, cannot overflow); Paper's Hands is the Long Path, blockchain-
  committed (Philadelphos's `compress → octonion hyperindex → PtolChain`
  eviction today).

Between them: this paper's fold makes the memory *reachable at low cost*, the
Long Path makes it *durable and ordered*. The single 256-bit number was the
whole idea. The box kite, and the Mind's Eye with Paper's Hands, are what it
became when it was built.

The formal treatment of hyperindexing — its objects and models, and why the
gauge symmetries of the Standard Model are one of them — comes after the
Ainulindalë and VAPMIP papers, led by Noether: the Noether current runs *up*
the tower carrying information forward, the Noether Information Current runs
*down* it carrying information back. Cost forward, change returned — the two
directions that have to balance.
