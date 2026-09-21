## 4. Why primes at all — how we came to 313

The question, asked plainly, before any of the rest of this paper
existed: **what is the last prime number to see any new factors come
down in the sieve?** — equivalently, the highest prime factor ever
required to build any composite in the domain at all. Not offhand maths;
a dataset of two conjugate domains over the composites (The Two Trees
engine — primes, composites), built and checked directly:

```python
# GenerationalLineage/engine/lineage.py::un_sieve, run for N=10^5
import lineage
r = lineage.un_sieve(100_000)
```

The standard optimised sieve only needs to strike multiples of `p`
starting at `p²` — every smaller multiple of `p` was already struck by a
smaller prime factor. So `p` contributes a **new** strike only while
`p² ≤ N`. Direct code, not looked up:

```python
>>> primes = sieve_primes(100_000)
>>> max(p for p in primes if p * p <= 100_000)
313
```

313 is the answer: the last prime with anything new to strike at
`N = 10⁵`. What that boundary actually splits the primes into, checked
directly rather than reasoned about in prose (`_spf_gpf_tables(100_000)`,
every composite `≤ 10⁵`, no sampling):

```python
>>> spf, gpf, primes = _spf_gpf_tables(100_000)
>>> comps = [n for n in range(4, 100_001) if spf[n] != n]
>>> max(spf[n] for n in comps)
313
>>> len({spf[n] for n in comps})            # every one of the 65 gets used
65
>>> never_spf = {p for p in {gpf[n] for n in comps} if p not in {spf[n] for n in comps}}
>>> len(never_spf), min(never_spf), max(never_spf), all(p > 313 for p in never_spf)
(5068, 317, 49999, True)
```

**Composite primes** — Telperion's, ≤313, 65 of them — are the complete,
closed alphabet of every composite's smallest-factor identity: no
composite in the whole domain ever has an `spf` outside this set, and
every one of the 65 gets used. **Factoral primes** — Laurelin's, 317
through 49999, 5,068 of them — are exactly the primes that *never* once
serve as an `spf` for anything: Telperion is permanently blind to them,
zero exceptions, not approximately; they only ever surface as a `gpf`,
which is to say only Laurelin ever accounts for them at all. The split
isn't a rule of thumb, it's exact: `max(spf) == 313`, always, for every
composite ≤ N, because `spf(n) ≤ √n ≤ √N` is arithmetic, not policy.

That single number is what turned an open question — are the primes
*words*, or are they *letters* — into a decision. **The first 65
primes are letters.** With a bounded, principled pool to draw from
(not an arbitrary round number, the sieve's own extinction boundary),
spelling can be hashed into primes in an orderly way, mostly collision-
independent rather than colliding by accident — which is exactly where
§5 picks up.

Reported for completeness, not developed further: the mirror question
(when does a composite's *largest* prime factor finish switching new
composites on) doesn't resolve until 49999 — a genuinely different,
much larger number, left here as one honest line for whichever number
theorist or physicist wants to run with it, not part of this paper's
argument.
