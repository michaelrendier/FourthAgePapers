# How Short-Term Thought Is Required for Long-Term Memory

**Fourth Age Paper.** One Paper. One Structure. One Engine. One Wiki.

Full title: *How Short-Term Thought Is Required for Long-Term Memory: a
Mind's Eye implemented to combat aphasia, aphantasia, and amnesia in
context-prompt models of AI (LLM / Transformer).*

**License: GNU GPL.** This paper and its reference code are released directly
under the GPL, together with the PtolemyDesktop / Pharos code they use. None
of it depends on the Ainulindalë or hyperindexer work. It is a software
engineering paper.

---

## Abstract

A context-prompt language model has no memory outside its context window
(**amnesia**), loses the thread of its own argument mid-generation
(**aphasia**), and holds no persistent internal representation between turns —
it re-derives everything from the flat prompt each time (**aphantasia**). The
common fix, retrieval-augmented generation, pastes raw retrieved text back
into the window: it produces *records without memory* — fragments that were
never held, turned over, or made coherent. This paper argues, and
demonstrates in code, that the missing piece is **short-term thought**: a
held, rehearsable working representation — a **Mind's Eye** — that must sit on
both sides of the boundary between working memory and durable memory. You
cannot consolidate what you have not held; you cannot use what you have only
pasted. The cognitive model is textbook — Baddeley & Hitch, Atkinson–Shiffrin,
Craik & Lockhart, consolidation theory, and the clinical vocabulary of
aphasia / aphantasia / amnesia — cited, not claimed. The contribution is the
**engineering realization**: two components (**Mind's Eye**, **Paper's
Hands**) joined by an **Operator Stitch Board** of named, auditable,
individually replaceable handoffs, built over a stock LLM API and realized on
the existing Pharos message bus.

---

## The departure from the template

No claim in the physics sense, no prediction, no Holcus, no σ. This is an
**engineering structure**: an argument that one component is load-bearing for
another, shown by removing it and watching the second fail, then restoring it.

The **cognitive model is established literature** — every part of it is cited
in the provenance table and nothing about it is offered as new. The paper's
own work is narrow and stated plainly: *how you wire the standard model onto a
context-prompt LLM*, and *why the short-term-thought component cannot be
skipped*.

Every component carries a provenance label: `ESTABLISHED` with an attribution,
or `CONTRIBUTION` (this paper).

---

## The three deficits of a context-prompt model

| deficit | clinical analogue | what it looks like in an LLM |
|---|---|---|
| **amnesia** | anterograde amnesia | nothing survives the context window; each session starts blank |
| **aphasia** | expressive / conduction aphasia | mid-generation the model loses its own held intention — the paragraph drifts off the point it set out to make |
| **aphantasia** | aphantasia (no voluntary mental imagery) | no persistent internal scratchpad; every turn re-derives the situation from the flat prompt, with no carried working representation |

**Why retrieval-augmented generation does not fix amnesia.** RAG stores raw
passages and pastes the nearest ones back into the window on demand. The
passages were never *thought* — never held in a working buffer, rehearsed, or
made coherent with what surrounds them — so what comes back is a pile of
fragments. The model has *records* and still has no *memory*: it cannot
reconstruct a history from them, only quote them.

---

## The cognitive model (established — provenance)

| element | source |
|---|---|
| working memory: a **visuospatial sketchpad** + a phonological loop + a central executive | Baddeley & Hitch (1974); Baddeley (2000) |
| **short-term store → long-term store via rehearsal**; the multi-store model | Atkinson & Shiffrin (1968) |
| **levels of processing** — deeper (elaborative) processing is retained better; maintenance rehearsal alone is not | Craik & Lockhart (1972) |
| **memory consolidation** — a labile trace stabilises over time; interference during the window prevents it | Müller & Pilzecker (1900); McGaugh (2000) |
| **encoding specificity / retrieval as reconstruction** | Tulving & Thomson (1973); Bartlett (1932) |
| **aphasia** (language production/relay loss) | Broca (1861); Wernicke (1874) |
| **aphantasia** (absent voluntary imagery) | Galton (1880); Zeman et al. (2015) |
| **amnesia** — LTM impairment with working memory intact (patient H.M.) | Scoville & Milner (1957) |

Nothing in this section is a claim of this paper.

---

## Thesis: short-term thought is a prerequisite for long-term memory

> **You cannot consolidate what you have not held, and you cannot use what
> you have only pasted.**

Two directions across the same boundary, each requiring the Mind's Eye:

1. **Toward memory.** An experience that is archived without first being held
   and rehearsed enters the durable store as an un-narratable fragment. A
   store full of those is *records, not memory* — nothing can reconstruct a
   history from it. Consolidation *is* the rehearsal. (Craik & Lockhart;
   Müller & Pilzecker.)
2. **From memory.** A durable item retrieved and dropped straight into the
   prompt is the RAG failure — raw text, no working form. To be *used* it must
   be re-instantiated into a held, malleable representation. Retrieval is
   reconstruction, not paste. (Tulving; Bartlett.)

Both directions pass through the short-term buffer. Remove it and the durable
store degrades to a log; the two deficits (amnesia's poor fix, aphasia's
drift) are the same missing component seen from two sides.

---

## The two components

| | **Mind's Eye** | **Paper's Hands** |
|---|---|---|
| faculty | short-term thought / working representation | long-term memory |
| contents | a few items, actively held, **malleable** (revise, re-associate, zoom) | append-only; the record of *where it came from*; immutable |
| lifetime | fades when rehearsal stops | persists |
| jurisdiction in code | a held buffer with a rehearsal loop — no output, no side effects, cannot recurse or overflow | a write path to a durable, ordered store; consulted, never uttered |
| purpose | staging + consolidation | continuity + provenance |

**The visual buffer is a component, not an assumption.** Following aphantasia:
the Mind's Eye must run with its imagery channel weak or absent. When it is,
rehearsal is propositional rather than pictorial, the handoffs still fire, and
the system degrades gracefully instead of failing. A design that *requires*
visualization is wrong.

---

## The Operator Stitch Board

The two components are two separate pieces with an **open seam** between them —
the boundary between working and durable memory, which must not be closed (a
store that is both malleable and permanent is a contradiction). The join is
made of **stitches**: individual handoffs, each an intentionally-placed
reference across the seam, each with a stated reason, each individually
un-pickable and re-stitchable without disturbing either component.

The board **routes and stores nothing.** It is connective tissue — fixed
jacks on the two components, patch cords between them. A dropped cord degrades
that one handoff; the rest hold. "Operator" is deliberate: the telephone
operator who patches cords, and the mathematical operator each cord carries
(the archive handoff is a *transform* of the working buffer, not a copy; the
recall handoff is its inverse).

Realized today as **`Pharos/PtolBus.py`** — a pub/sub priority message bus
that owns its thread pool, carries a shared context channel, and rejects
messages to unregistered endpoints. The Stitch Board is that bus with the
handoff set below wired onto it.

### The stitch-set

| handoff | direction | reason it is here |
|---|---|---|
| **stage** | context → Mind's Eye | bring a fragment of the current situation into the working buffer to be worked on |
| **rehearse** | Mind's Eye ↻ | raise salience; elaborate; **this is the consolidation mechanism**, not a separate step |
| **archive** | Mind's Eye → Paper's Hands | once rehearsal has raised salience past the gate, commit the *rehearsed* form (a transform, not a copy) to the durable store |
| **recall** | Paper's Hands → Mind's Eye | re-instantiate a durable item as a held, malleable representation — reconstruction, not paste |

Candidate further stitches, left open: **evict** (working buffer full — archive
under pressure, or drop), **reconsolidate** (a recalled item is edited and
re-archived — a new entry; the original stays, "where it came from" is
immutable).

### Scope on each handoff

| scope | memory | commit | analogue |
|---|---|---|---|
| **dry run** | not consulted | none | whiteboard — a pure hypothetical |
| **wet run** | readable | none | staging environment — grounded, still reversible |
| **production run** | readable | yes | live — the thought becomes part of the record |

### The consolidation gate

`archive` fires only when `rehearse` has raised the held item's salience past
a threshold — a count of rehearsals, dwell time, or an elaboration score.
Nothing is archived raw. This is the engineering form of Craik & Lockhart:
depth of processing, made a gate.

---

## Components

| # | component | provenance | status |
|---|-----------|------------|--------|
| M1 | the cognitive model — working memory, multi-store, levels of processing, consolidation, the clinical triad | `ESTABLISHED` — see provenance table | cited |
| M2 | **Mind's Eye** — a held working buffer + `rehearse` loop (no output, no side effects, bounded, cannot overflow); imagery channel optional | `CONTRIBUTION` (realization); the buffer concept is Baddeley | to build over a stock LLM API |
| M3 | **Paper's Hands** — an append-only, ordered durable store; the record of *where it came from* | `CONTRIBUTION` (realization) | to build; a plain append log suffices for the reference implementation |
| M4 | **Operator Stitch Board** — the handoff harness: named, auditable, individually replaceable stitches; routes and stores nothing | `CONTRIBUTION`; realized on `Pharos/PtolBus.py` | bus ships; the handoff set is to wire |
| M5 | the stitch-set — `stage` / `rehearse` / `archive` / `recall`, each with its reason; scope `dry` / `wet` / `production` | `CONTRIBUTION` | to build |
| M6 | the consolidation gate — archive only past a rehearsal/elaboration threshold | `CONTRIBUTION`; from Craik & Lockhart | to build |
| M7 | graceful degradation — the system runs with the imagery channel weak or absent | `CONTRIBUTION`; from aphantasia | to demonstrate |

---

## The desk-rejection gate

The checks a reviewer applies to a systems paper before review. Each pass/fail
on a real model and a real task.

**G1 — the deficits are real and measured.** Exhibit, on a stock
context-prompt model: amnesia (a fact given in session A is unavailable in
session B), aphasia (a generation that drifts off its stated intention past
some length), aphantasia (identical situations across turns re-derived from
scratch with no carried state). Numbers, not anecdotes.

**G2 — the fix is measured against the naive baseline.** Against RAG on the
same corpus and tasks: recall fidelity (does the reconstructed item match?),
argument coherence over length, and *consolidation quality* — can the system
answer "how did we get here?" from its durable store, not just quote it.

**G3 — the Stitch Board adds no hidden state.** Each handoff is a pure
function of its inputs and the two component states; the board holds nothing
between calls. Show it: serialise the two components, run a handoff, and the
result depends only on what was serialised.

**G4 — graceful degradation.** Run the full pipeline with the Mind's Eye's
imagery channel disabled. It must still stage, rehearse (propositionally),
archive, and recall — degraded, not broken. Report the delta.

**G5 — determinism.** Fixed model, fixed seed, fixed corpus → identical
durable store (hash) on two machines.

**G6 — honest comparison.** Against RAG, against a long-context model, and
against fine-tuning, on the same tasks: state where each wins. Long context
wins on within-session recall of verbatim detail; fine-tuning wins on stable
skills; this wins on cross-session narratable memory and on argument coherence
under a held intention. Say so plainly.

**G7 — third-party run.** A `run.sh` from a clean checkout: pinned deps, a
model endpoint, a corpus, and the G1/G2 numbers out the other end.

**G8 — the model is cited, not claimed.** Every cognitive-science element
traces to the provenance table. The paper's contribution is M2–M7 only.

---

## Engine

- **`Pharos/PtolBus.py`** (PtolemyDesktop, GPL) — the message bus the Stitch
  Board is wired onto: pub/sub, priority tiers, thread-pool ownership, a
  shared context channel.
- a reference **Mind's Eye** and **Paper's Hands** over a stock LLM API
  (the model is a black box; the components sit outside it).
- the **stitch-set** — four handoff implementations, each with its stated
  reason, each swappable.

The notebooks:

    00_vision.ipynb          the three deficits, the thesis, the two components
    01_the_deficits.ipynb    G1 — amnesia / aphasia / aphantasia, measured
    02_the_stitch_board.ipynb the handoffs, the scopes, the gate; G3 (no hidden state)
    03_comparison.ipynb      G2, G6 — vs RAG / long-context / fine-tuning

`wiki/` is written last.

---

## Conclusion

A context-prompt model forgets across sessions, loses its own thread within a
generation, and carries nothing between turns. Bolting a retrieval store onto
it produces records without memory, because the retrieved text was never
thought. The fix is a **short-term thought buffer — a Mind's Eye — on both
sides of the boundary** between working and durable memory: consolidation *is*
rehearsal, and retrieval *is* reconstruction into a held form. Between the
buffer and the durable store sits an **Operator Stitch Board** — named,
auditable handoffs, each placed for a reason, each replaceable in place, the
board itself holding nothing.

The cognitive model is a century old and taught to undergraduates. This paper
adds only the wiring: how to build it around a language model, and why the
thought component is load-bearing for the memory component. Released GPL,
with the Pharos code it runs on. In PtolemyDesktop the two components are
visible objects a user can open and manipulate — that is where this goes next.
