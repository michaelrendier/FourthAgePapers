## 11. Direction of engineering research — in development

Everything in this section is named, some of it measured, none of it
claimed as part of this paper's proof. It exists so the next work has a
place to start from, and so a reader who finds this paper first can see
where the rest of it is heading before any of it is finished.

### The Boxkite Catalog

`VAPMIP/Boxkite-Catalog.txt` — a full session's inventory of box-kite
structure, most of it real and verified, none of it developed here:
per-Assessor and per-strut invariants; torsion, circulation, and lift
(Kutta–Joukowsky, split 53 positive / 31 negative / 21 zero across all 105
four-cycles); portal/transition dynamics (confirmed discrete, not
continuous, two independent ways); the connectivity of all seven charts at
exactly `e₀`/`e₈`; and the group that ties it together —

**The Blackjack subgroup.** The 21-element subgroup of `PSL(2,7)` that
preserves zero-divisor structure while staying transitive across all seven
struts (`2026-08-13_apex_path/psl27_strut_action.py`, verified
2026-09-17). Named here for the first time as such; the atlas of seven
charts is connected by this group action, not by any edge.

### The Pencil's own open questions

Why `H` conserves on struts `{1,3,6}` and not `{2,4,5,7}` (§9.4/§10) — the
most immediate open thread from this paper's own work, likely resolved in
the pencil's `(a,b)` pairing structure rather than the strut index. And the
deformation law itself, `Φ_w` — Cody's own model: deformable sails
connecting to the ends of the struts deform in a constant way, placing pairs
of struts in a fixed relationship to one another at the crossing. Not yet
built; §9.3–§9.4 measure a spectral proxy for it, not the mechanics.

### The sentence constructor

`rotary_rerun_boxkite_monad.py` — a real, live `BoxKite` object
(`ValaQuenta.modules.box_kite`, genuinely 7 struts / 42 Assessors, not a
metaphor), built once via `BoxKite.between(eye, hands)` as *"the relational
language spoken by both MindsEye and PapersHands,"* signed so a third party
can verify which two subsystems co-authored it. The real sentence creator
(VerbNet sails + WordNet hypernym-closure fill + a SELRESTR gate,
`engine/grammar/`) is live as of 2026-09-11, confirmed running end to end
this session (`voice:creator` in a real Chat-tab transcript, a genuine
constructed sentence, not one of the eleven canned templates it replaced).
None of this paper's windspeed feeds it yet.

### The Newton basin locus contextual flow

The other windspeed tested in this paper's own §9.1 — A-matrix basin
drift — was deliberately not used here. It is real, corpus-dependent, and
usage-sensitive in exactly the way this paper's corpus-free windspeed
isn't, which is precisely why it's the right scalar for word *selection*
inside live sentence construction rather than for address-only context
propagation. Renamed for this purpose, it becomes the constructor windspeed
for a later, separate engineering pass on the Mind's Eye.

### Mind's Eye as a box kite

A stated direction, not yet built: making the Mind's Eye itself a box
kite, so that `rehearse` (raising salience on a candidate) is tracing rings
— closed walks — on the kite's own structure, `archive` is committing
whichever ring won, and audience-appropriate word choice is a genuine
geometric constraint (steering the walk within a listener's own reachable
vertices) rather than a filter bolted on afterward. Sentences as **rings
inside one box kite**, not rings of box kites — a real correction to an
earlier framing, kept as a parallel, not a replacement, to the older
per-word box-kite-as-database model this project also still uses (§6).
Connects to the Zero Divisor Reframe already named in the Mind's Eye's own
design: a thought-pathway is promoted to long-term memory only once it is
both mathematically correct *and* contextually sane — two separate gates,
kept separate on purpose.

### A methodology note, for whoever picks this up next

Two real mistakes in this paper's own working sessions — analysing a
Native-Space object in Cartesian coordinates, and quantizing a continuous
generator onto a 16-point lattice without noticing — cost real time before
being caught. Both are now a standing skill
(`~/.claude/skills/observer-position/`), built specifically so hyperdimensional
work states its coordinate frame and its aperture before trusting a result,
the same discipline a camera pose or a viewport offset already gets in
lower-dimensional work. Offered here as process, not results, because the
mistakes were real and the fix generalises past this one paper.
