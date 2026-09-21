## 6. `monad3_c.bin` — built to carry the 19D WordNet relationships

Pigeon-holed deliberately: this section is how `monad3_c.bin` came to
carry the WordNet box-kite table, nothing wider. Explicitly **out of
scope here** — bootstrapping and bulk corpus ingest (`ingest.c`,
`build_monad_bin.py merge`), the filesystem-ingestion experiments and the
`.bin` poisoning that followed from pointing a bulk ingest at a real
computer's own file structure, and the vocabulary-update law's formulas
(what the Monad's live "learn" step actually computes). Named here so
the boundary is visible to a reader, not silently narrowed.

### 6.1 The WordNet box-kite table, built in C

`VAPMIP/PtolC/boxkite_bin.h` defines the shared record — one
`BoxKiteEntry` per WordNet synset, 19 compressed relation exponents plus
a depth weight, the same schema `wordnet_boxkite.py` uses on the Python
side (documented as "two different serialisations of one schema, not two
different schemas"):

```c
typedef struct {
    char     word[32];
    uint8_t  pos;                  /* 1=NOUN 2=VERB 3=ADJ 4=ADV */
    uint32_t synset_offset;        /* WordNet's own offset -- the stable id */
    int16_t  vector[19];           /* compress_count()-ed relation exponents */
    float    depth_weight;         /* default 1.0 */
} BoxKiteEntry;
```

`VAPMIP/PtolC/dump_boxkite_bin.c` builds `c_monad_wordnet.bin` from that
struct — reading WordNet's own `index.noun/verb/adj/adv` files directly
(not a library iterator; `getindex()` is fuzzy search, not enumeration),
calling the real C WordNet library (`index_lookup`, `read_synset`) per
word, first sense only, with `compress_count` ported verbatim from the
Python file so the two sides agree by construction, not by convention.

The cross-check that they actually do agree: `wntest.c`, run against the
real C WordNet library, `bank`'s first noun sense — `HYPERPTR=1,
HYPOPTR=2` — exactly matching Python's `{'hypernyms':1,'hyponyms':2}` for
`bank.n.01` (verified 2026-08-25).

### 6.2 Folding into `monad3_c.bin`

`VAPMIP/monad_combine.py` is where the already-built WordNet table joins
the rest — confirming the sequence: the box-kite/WordNet piece existed
first, as its own file, before anything was combined:

```python
def read_boxkite_c(path=DEFAULT_WORDNET):        # c_monad_wordnet.bin
    ...                                            # BXKT header + BoxKiteEntry[n]
    return {word: {'pos', 'offset', 'vec19', 'depth_weight'}}

cm = CombinedMonad(english=<monad.bin state>,
                    wordnet=read_boxkite_c(),
                    phonetic=read_phonetic())
write_c(cm, path)   # -> monad3_c.bin
```

`write_c` takes the **union** of all three sources' vocabularies
(`sorted(set(eng.words) | set(cm.wordnet) | set(cm.phonetic))`) and emits
the single fixed-offset, mmap-able file every notebook so far has loaded
directly — `eng:` (β/E/A-matrix), `wn:` (this section's `BoxKiteEntry`
table), `phon:` (§6.3).

### 6.3 `phon:`, in one line

Checked directly: `monad_phonetic.bin` is built independently, from
`nltk.corpus.cmudict` (real ARPAbet pronunciation + stress), keyed only
by word spelling — no synset, no WordNet relation, anywhere in its
construction. No WordNet wiring to report, so it stays a sibling section
in the packed file and out of scope here. One note worth keeping, since
it's a real, stated limitation: ARPAbet is ASCII by convention; a move
to Unicode IPA is future work, not this file's current form.

### 6.4 Not static

One thing worth saying plainly and no more: `monad3_c.bin` is a
**knowledge store**, not a frozen table — the Monad's live learning step
keeps deepening it, and a word only reaches "verified" status once it's
been seen from both directions, the WordNet entry and real usage. The
mechanism itself — what "learn" actually computes — is out of scope for
this section by design (§ note above); its role here is just this:
**the file this section built keeps growing**, it isn't a one-time
export.

### 6.5 The update mechanism itself, in C

`notebooks/06.5_monad3c_update_mechanism.ipynb` — a genuine C-kernel
notebook (`jupyter-c-kernel`, each cell standalone, compiled and run
with `gcc`, not a Python restatement), covering §6.4's "continuing
growth" claim at the level Cody asked for: the real update law
(`monad_learn_ex`'s β-deepening, `prose_seen` ladder, A-matrix 2D
inverse-distance coupling — `PtolC/monad.c`, real constants from
`PtolC/ptolemy.h`), and only what the daemon *sends* to trigger it
(message class + weight, `external=1.5`/`internal=0.9`) — not the
daemon's own socket/FIFO/spool plumbing. Separate from and complementary
to the Python `Crank.learn` shown for CS-paper readability elsewhere.

Two real findings surfaced just by running the extracted logic, both
flagged rather than fixed:
- **`MONAD_BETA_SAT = 7.552`** (`ptolemy.h`), not the `(0, 1]` range
  `monad_bin/SPEC.md` states for β — a live discrepancy between the spec
  and the actual C constant.
- **The `prose_seen` ladder is order-dependent, asymmetrically**:
  WordNet-then-prose reaches `3` ("verified common"); prose-then-WordNet
  only reaches `2`, silently losing the earlier prose sighting — the
  `NS_FT_WORDNET` branch overwrites unconditionally rather than checking
  prior state.

---

**Production note (Cody, 2026-09-20):** `boxkite_bin.h`/
`dump_boxkite_bin.c`/`wntest.c` are native C, and per Cody: "the Monad
and the Monad Harness [are] strictly C these days" — the Python monads
(`monad.py`, `rotary_rerun_boxkite_monad.py`) are for testing and CS-
paper enumeration, not the live system. Notebook 06 should be a genuine
**C-kernel notebook** (Cling/Clang-style, as done before for other
notebooks in this project) running this section's actual C, not a Python
restatement of it.
