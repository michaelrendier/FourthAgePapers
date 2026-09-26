# The Hyperindexing System: Data With No Physical Location

**Status: TODO — stub.** Started 2026-09-25. This is a placeholder for the
paper, not the paper. Per the FourthAgePapers rule, work happens in the
engine and notebooks first; this file grows as that work lands, and the
wiki page is written last.

---

## Provenance note — this paper is not starting from zero

Unlike a paper written to the FourthAgeProtocol from its first line, the
underlying HyperWebster work **predates the protocol itself** — earliest
commit touching HyperWebster is 2026-04-24, six weeks before "The Lagrangian
of Information Propagation" (2026-06-12), which makes it the oldest
substantial maths in the whole project, and the "One Paper. One Claim. One
Prediction (Ptolemy/0_RB). One Engine. One Wiki" rule (with the prediction
pillar added 2026-09-25) postdates all of that by months. So this paper is
being written and predicted *onto* existing history and results, not the
other way around — the usual order (protocol → engine → results → paper) is
inverted here on purpose, not by accident, and that inversion should stay on
the record rather than be smoothed over to look like every other paper in
this series. Concretely, real, already-existing history feeding this paper
includes: 13 distinct implementations surveyed and characterized (2026-09-24,
see `VAPMIP` conversation log), the plain-Horner-vs-full-charset/minimal-
charset baseline benchmark (`VAPMIP/README.md` + `VAPMIP/benchmarks/
hyperwebster_baseline_bench.py`), and the Blackjack-subgroup (`F₂₁`)
alternative-mechanism test that returned a negative-but-real result
(`VAPMIP/benchmarks/blackjack_vs_horner_bench.py`) — all of it dated *before*
this paper's own stub existed. The claim and prediction sections below are
being fitted to that prior record, not generating it.

---

## One Claim

The plain HyperWebster bijection — string ↔ integer address, exact,
reversible, no hashing anywhere in the path — extends to a hierarchical
day → month → year index that gives lossless, constant-per-chunk
conversational memory: reconstruction cost depends only on the size of the
few index layers actually touched, never on how much time or data has
elapsed since.

## One Prediction (Ptolemy/0_RB)

Pending — not yet run. To be generated from 0_RB once the engine below has
enough shape to give it something to predict against.

## One Engine

Home: `ValaQuenta/modules/hyperwebster/` (existing `horner_encode`/
`horner_decode` core is the right reusable piece; the module's
`fano_encode`/`monad_address` Cayley-Dickson layer is `DataStorageNoLocation`'s
territory, not this paper's — kept in place, not touched here). Per the
"One Engine" rule, new work is designed inside ValaQuenta and copied to its
eventual home (Monad-facing code in VAPMIP/PtolemyDesktop), not developed in
place elsewhere first.

Open engineering questions, in order:
1. Chunk size and minimal (per-chunk) charset — baseline numbers already in
   `VAPMIP/README.md` §"HyperWebster Indexing — Baseline Benchmark".
2. Day/month/year aggregation — reuse the shape of
   `PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hypergallery.py`'s
   `VectorAddress`/`master_address` (many child records → one parent
   address), don't reinvent it.
3. Whether/how `PtolemyDesktop/Philadelphos/cyclic_context_buffer.py`'s
   blockchain gets a calendrical (day-keyed) side-index laid on top of its
   `prev_hash` chain, so retrieval stops being O(depth).

## Sibling work — not a duplicate

`../DataStorageNoLocation/` benchmarked the Cayley-Dickson-folded variant
(fixed-size address per CD rung, `data-storage-no-location` branch,
2026-08-30, unpushed) and already measured Horner encode at ~O(n^1.8) on the
reference machine — independently consistent with this paper's own baseline
benchmark. That paper folds the address down; this one keeps it exact and
manages its growth by chunking and hierarchy instead. Both are real,
neither supersedes the other.

## Licensing

Falls under the same terms as `../DataStorageNoLocation/LICENSE.md` /
`COMMERCIAL_TERMS.md` — same hyperindexer addressing paradigm, same
carve-outs (Ptolemy / any Monad `.bin` state is never covered). Not
duplicated here; those files are the source of record.

## One Wiki

Not written yet — last, per the rule.
