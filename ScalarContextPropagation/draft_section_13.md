## 13. Code appendix

The executable form of every result in this paper. Not the `repo_appendix`
generally — this section is the curated path through it: what to run, in
what order, to reproduce §3 through §11 from nothing but this repository
and its two sibling repos (`VAPMIP`, `ValaQuenta`).

### 13.1 The notebooks

| notebook | proves | section |
|---|---|---|
| `notebooks/01_semantic_prime_hashing.ipynb` | the address (Horner→next_prime→π), the `6543`-vs-`6542` anomaly, the `U+200B` collision | §3 |
| `notebooks/02_the_313_sieve_and_49999_unsieve.ipynb` | `313` as the sieve's own extinction boundary, derived twice independently | §4 |
| `notebooks/03_phonetic_prime_hashing.ipynb` | the naive scheme's anagram collision, the Gödel-positional fix | §5 |
| `notebooks/05_wordnet_19d_contextual_hash.ipynb` | `context_code`/`gamma_radial`, exact both directions, the combined address | §7 |
| `notebooks/06.5_monad3c_update_mechanism.ipynb` | the real C update law (`monad_learn_ex`) — C-kernel, every cell actually compiled and run | §6 |
| `repo_appendix/windspeed_reconstruction/` (11 scripts + README, numbered) | the windspeed recovery, the coordinate-frame and aperture corrections, the `{1,3,6}` conservation result | §9 |

`notebook 04` (`boxkite_pencil_hyperstring_windspeed.ipynb`) is cited
throughout §9 as the origin of the discreteness anomaly this paper's own
work later resolved — read alongside `07_unflattened_continuous_H.py`
above for the corrected version of the same question.

### 13.2 The build — WordNet into the box kite, in C

`PtolC/boxkite_bin.h` — the packed record, byte-identical on both sides of
the build:

```c
typedef struct {
    char     word[32];
    uint8_t  pos;
    uint32_t synset_offset;
    int16_t  vector[19];
    float    depth_weight;
} BoxKiteEntry;
```

`PtolC/dump_boxkite_bin.c` — built from the real WordNet C library, not a
reimplementation:

```c
static void synset_context_vector(SynsetPtr syn, int16_t out[N_RELATIONS]) {
    int raw[MAXPTR + 1];
    memset(raw, 0, sizeof(raw));
    for (int i = 0; i < syn->ptrcount; i++) {
        if (syn->pfrm[i] != 0 || syn->pto[i] != 0) continue;
        int t = syn->ptrtyp[i];
        if (t >= 0 && t <= MAXPTR) raw[t]++;
    }
    for (int r = 0; r < N_RELATIONS; r++)
        out[r] = compress_count(raw[REL_PTRTYPE[r]]);
}
```

Cross-checked against the Python side (`wordnet_boxkite.py`) synset by
synset, not assumed to agree — `PtolC/wntest.c`, verified 2026-08-25.

### 13.3 The read — a word's address, in the current monad

`PtolC/ptol.c`, the live touchpoint (`-M`, byte-exact against §13.2's
struct, no shell-out):

```c
const unsigned char *e = g_m3 + g_m3h->off_wn + (size_t)ix[1] * 82u;
uint8_t pos = e[32];
const int16_t *vec = (const int16_t *)(e + 40);
```

### 13.4 The windspeed recovery, exact

`VAPMIP/wordnet_boxkite.py` + `repo_appendix/windspeed_reconstruction/01_windspeed_recovery.py`:

```python
full_code = full_addr - delta
recovered_spelling = spelling_code(word)                  # from text alone
recovered_context  = full_code // recovered_spelling      # exact, disjoint tiers
log_code = sum(v[i] * math.log(CONTEXT_PRIMES[i]) for i in range(19))
gamma_radial = math.tanh(0.5 * math.log(log_code / LOG_ANCHOR))
```

### 13.5 The box kite itself

`ValaQuenta/modules/box_kite/maths.py` — `pencil(s)`, `box_kites()`,
`assessors()`, `chart_of()`; `rotary_rerun_monad.py::BoxKite.between(eye,
hands)` — the live, signed, jointly-authored instance the current monad
actually binds to.

### 13.6 Reproduce

```
python3 -m venv .venv && source .venv/bin/activate
pip3 install -r requirements.txt
python3 -c "import nltk; nltk.download('wordnet')"
# sibling repos VAPMIP and ValaQuenta checked out alongside this one —
# every notebook's first cell hardcodes ~/Projects/ThePlace/<repo>; a
# real portability wrinkle, named in §1, not yet fixed.
jupyter notebook notebooks/
```

`repo_appendix/windspeed_reconstruction/` scripts are plain `python3`,
`ValaQuenta/.venv` required for the WordNet-dependent ones (nltk/sklearn
ABI conflict on bare system Python — use the venv, not a workaround).
