# Collatz as the 2-adic Shift

**Fourth Age Paper.** One Paper. One **Result**. One Engine. One Wiki.

---

## The departure from the template

Every other Fourth Age paper is *One Paper, **One Claim***. This one has **no claim
and no prediction**, and there is no `01_predictions.ipynb`.

That is the protocol applied, not relaxed. Pre-registration is a device for
stopping yourself reinterpreting a result after seeing it, and it means something
only when the outcome is genuinely unknown at registration. Everything measured
here is either a theorem already in the literature or an exact enumeration over a
finite space. **There is nothing to be wrong about, so there is nothing to
pre-register.**

What replaces the claim is a **provenance label on every result**, printed by the
engine in the same row as the result: `KNOWN` with an attribution, or `OURS`.
Nothing borrowed is allowed to read as ours.

---

## The Result

> **The Collatz map is the one-sided binary shift on `Z₂`, under an explicit
> measure-preserving change of coordinates — the parity vector. Its pieces are
> affine on residue classes mod `2^k`; its branch tree is Pascal's triangle
> exactly; its cycles are rationals with denominator `2^k − 3^d`.**
>
> **Decomposed against the operation domain: `T = ADD ∘ SCALE ∘ SIGN`. No new
> generator is required.**

The map used throughout is the **shortcut map**, one halving folded into the odd
branch so every step does work:

```
T(n) = n/2         n even
T(n) = (3n+1)/2    n odd
```

### What this means for the conjecture — and what it does not

The dynamics of the shift are completely understood: entropy `log 2`, dense
periodic points, uncountably many orbits. Total chaos, fully solved. The Collatz
conjecture asserts that `N` — dense in `Z₂` and of measure zero — **misses all of
it**. So the difficulty is not in the map. It is in how two incompatible metrics,
the 2-adic and the archimedean, fail to see each other.

**Nothing in this paper proves the conjecture, disproves it, or is evidence
either way.** Stated plainly so it cannot be read otherwise.

---

## Results table

`10/10` relations hold. Every number is computed at run time; nothing is asserted.

| # | relation | tier | provenance |
|---|----------|------|------------|
| R1 | `T^k` is affine on each class mod `2^k`, slope `3^d/2^k`, `d` fixed by the class | 1 | KNOWN — folklore |
| R2 | the parity vector `Q_k : Z/2^k → Z/2^k` is a **bijection** | 3 | KNOWN — Bernstein 1994 |
| R3 | `Q(T(n)) = shift(Q(n))` — **Collatz *is* the shift** | 2 | KNOWN — Bernstein–Lagarias 1996 |
| R4 | the `d`-histogram over the `2^k` classes is **exactly** `C(k,d)` | 3 | **OURS** (framing) |
| R5 | so log-normality is de Moivre–Laplace, not an empirical fact | 3 | **OURS** (framing) |
| R6 | cycles ↔ rationals with denominator `2^k − 3^d`; one integer cycle to `k=16` | 3 | KNOWN — standard |
| R7 | odd predecessor iff `n ≡ 2 (mod 3)`; multiples of 3 are permanent leaves | 2 | KNOWN — elementary |
| R8 | `T` is exactly **2-to-1**: one bit destroyed per step, `log 2` nats | 3 | **OURS** (measurement) |
| R9 | backward mean out-degree on `N` is `4/3`; shortfall is `log(3/2)` **exactly** | 3 | **OURS** (measurement) |
| R10 | drift at parity measure `½` is `log(√3/2) < 0`; critical `p = log2/log3` | 3 | KNOWN — Terras 1976 |

Exhaustive, not sampled: R1–R4 and R6–R8 enumerate a finite space completely.
R9 counts a density over a stated range. **R10 is the one sampled statistic and
carries a stated, uncorrected termination bias** (`+0.0047`) — the sample stops at
`1`, which truncates the low tail. It is not corrected for and not hidden.

---

## The direction result — `OURS`

| direction | what happens | rate |
|-----------|--------------|------|
| **down** (forward `T`) | exactly 2-to-1; one parity bit destroyed per step; provenance discarded | `log 2` nats/step |
| **up** (backward tree on `N`) | mean out-degree `4/3`; enumerates possibilities, propagates nothing | `log(4/3)` nats/step |
| **shortfall** | | `log(3/2)`, **exactly** |

Going *up* the tower does not propagate information — it enumerates. Going *down*
does, and what propagates is the address. The gap between the two directions is
`log(3/2)`, the odd branch's own gain: **the arithmetic the 2-adic metric cannot
see, priced per step.**

---

## The lineage verdict

```
operation                  tier  descends from             status
n mod 2  (branch select)   t0    SIGN                      PRIMITIVE — one bit, nothing between
n / 2                      t1    SCALE → DILATE, gain ½    derived — changes length
3n                         t1    SCALE → DILATE, gain 3    derived — changes length
+ 1                        t0    ADD                       PRIMITIVE — identity 0
T = the Collatz map        t3    ADD ∘ SCALE ∘ SIGN        DERIVED — no new generator
```

**No new generator required** — and that is precisely why it is hard. `T` is the
smallest non-trivial composition using all three tier-0 irreducibles at once. ADD
and SCALE have **different identities** (`0` and `1`); the `+1` is the only thing
coupling the two axes. Drop it and `n → 3n/2^v` is a pure SCALE tower with no
conjecture in it (shown in `02_lineage.ipynb`).

No section-5 emergence signature fires.

---

## The three faults on the first run — all mine, none the mathematics

Kept on the record because they are the most useful part of the paper.

| relation | diagnosis |
|---|---|
| `cycle_denominator` | necklace filter kept rotation-minimal words but not **primitive** ones, so `1010`, `101010`, … came through and one loop was reported as seven cycles |
| `forward_two_to_one` | the **measurement was right** (fibre size 2); my assertion expected 4. A CODE fault wearing a MATHS fault's label |
| `backward_deficit` | I predicted `7/6` from a condition that does not exist |

**The third correction improved the result.** I had written the odd-predecessor
test as *"`n ≡ 2 (mod 3)` **and** `(2n−1)/3` is odd"*. The second half is
**vacuous** — `2n−1` is odd, `3` is odd, so the quotient is odd whenever it is an
integer. The engine now measures that vacuity instead of assuming it. Removing the
phantom condition gives density exactly `1/3`, out-degree exactly `4/3`, and the
shortfall comes out exact at `log(3/2)`.

---

## Notebooks

| | |
|---|---|
| `00_vision.ipynb` | the question, the map, what this paper does **not** claim |
| `01_measurements.ipynb` | the ten relations, plus R1/R4/R6 exhibited by hand |
| `02_lineage.ipynb` | the decomposition, the emergence check, the framework correspondences |
| `03_results.ipynb` | the scorecard, the three faults read honestly, the direction result |

There is **no `01_predictions.ipynb`** and its absence is deliberate — see above.

## Engine

`engine/e_collatz_shift.py` — stdlib only, no dependencies, `run(verbose=True)`
returning a dict, matching the `VAPMIP/engines/e01–e10` contract.

```
python3 engine/e_collatz_shift.py        # ~4s, 10/10
```

## Wiki

`wiki/Collatz-as-the-2-adic-Shift.md`

---

## Where the framework speaks — and where it does not

Structural correspondences, labelled as such. Full text in `02_lineage.ipynb`.

- **`VAPMIP/intention_monad.py`** — set the GC root to `{1}` and the conjecture
  *is* the collector's completeness claim: run it on `N` and it collects nothing.
- **`VAPMIP/sieve_clock.py`** — the mod-3 leaves are the ORPHAN regime, but a
  *permanent* one. A sieve orphan at `N` is adopted at `2N`; a Collatz orphan
  never is. Two kinds of orphan; the instrument models one.
- **`L_(I|O)`** — forward free, backward a branching tree gated by a `mod 3`
  test. **The parity word is the private key.**
- **`0_RB = e₀`** — the attractor is the identity, reachable on `N` only as an
  ordered 2-cycle.

⚠ **The Two Trees do NOT split even/odd.** Telperion = prime, Laurelin =
composite; even/odd is divisibility by 2, not primality (`2` is prime and even,
`9` is composite and odd). The tempting mapping is **wrong** and is recorded as
wrong. The defensible reading is at the *tower* level: the 2-tower against the
3-tower, mingling at `log₂3 = 1.58496`, which is where every candidate cycle must
live.

**"Near miss."** The `2^k − 3^d` ladder is a *linear form in logarithms* — the
same **family** as the Fermat near-miss work (`FermatMonster`,
`VAPMIP/engines/e14_fermat_near_miss.py`), in that both ask how closely towers of
small primes can approach without touching. It is **not the same problem** and it
is **not** the Riemann Hypothesis. Recorded as a family resemblance, nothing more.

---

## Open

- **The whole conjecture.** Untouched.
- **Two kinds of orphan.** Temporary vs permanent is not modelled anywhere.
- **Is `log(3/2)` per step the right price?** Exact for this map. Whether
  `(pn+1)/q` gives `log(p/q)` is not tested here.

No free parameters. No renormalization. Failed predictions — and failed
assertions — stay in the record.

White Hat.
