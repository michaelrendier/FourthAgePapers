## 4. Why primes at all — how we came to 313

### 4.1 The Two Trees Engine

Two names recur through this section: **Laurelin** and **Telperion**.
They are not this paper's invention — they name a general-purpose
component (`GenerationalLineage`'s Two Trees engine) already used
elsewhere in this project to split a domain of primes into two disjoint
sub-domains and track what crosses between them. Nothing in this section
depends on that engine's wider scope; the two names are used here purely
as fixed labels for the two domains §4.4 derives, so that later sections
(and this paper's own code) have one word each instead of a clause.

Live, runnable: this paper's own
`notebooks/02_the_313_sieve_and_49999_unsieve.ipynb` demonstrates the
engine directly, cell by cell (§4.4–§4.5 below). The engine's own home
notebook, built under this project's Full Engine Protocol (one numbered
notebook per engine, `VAPMIP/notebooks/`), is
`VAPMIP/notebooks/16_e10_generational_lineage.ipynb` — it documents the
Two Trees engine at a depth this paper doesn't need and isn't developed
here; named only as a pointer.

### 4.2 Laurelin — the factors domain

A prime is, by the classical sieve reading, exactly what survives
elimination: strike every multiple of 2, then of 3, then of 5, and so
on — what remains unstruck at the end is prime, defined entirely by the
factors it does *not* have. That is the extinction reading of
factorisation, older than any of the machinery in this paper. Reported
plainly, without claiming it resolves anything open: **Fermat's
framing defines the primes by the extinction of every possible factor;
the Riemann zeta function, by contrast, only describes the primes'
*order of arrival*** — the density and spacing of a set already fixed by
that extinction test, not what makes any one of its members prime.
Nothing here leans on the truth or falsity of any unproven conjecture
about that order; the distinction is between what *defines* the set and
what *describes* its distribution, and both readings are standard.

**Laurelin** is assigned this section's *factors* domain — see §4.5:
the primes above 313 that this paper's own sieve run shows never once
serve as anything but a factor of something larger. They exist in the
dataset only in that role.

### 4.3 Telperion — the Riemann prime-zeta-zero tree

**Telperion** is assigned this section's other domain — the primes at
or below 313 — for a reason specific to this paper, not a restatement of
how the name is used elsewhere in the project: every one of those primes
is exactly a *letter*, and §3 already showed what a letter is for —
`Horner → next_prime → π(p) → γ`, a walk that ends on one specific
non-trivial Riemann zeta zero. Telperion's domain, in this paper, is the
alphabet whose addresses *are* Riemann zeros. That is what "Riemann
prime-zeta-zero tree" means here, concretely, not evocatively.

This is a different object from a same-named "zero divisor tree" used
elsewhere in this project (the sedenion zero-divisor / box-kite
machinery this paper mentions only briefly, in §9–§11). The two share a
name and nothing else — no code path, no data, no domain overlap — and
are not to be conflated; this paper's Telperion is the ≤313 letter
alphabet, full stop.

### 4.4 The boundary itself

The question, asked plainly, before any of the rest of this paper
existed: **what is the last prime number to see any new factors come
down in the sieve?** — equivalently, the highest prime factor ever
required to build any composite in the domain at all. Not offhand maths;
a dataset of two conjugate domains over the composites (the Two Trees
engine — primes, composites), built and checked directly:

```python
# GenerationalLineage/engine/lineage.py::un_sieve, run for N=10^5
import lineage
r = lineage.un_sieve(100_000)
```
Live, runnable: `notebooks/02_the_313_sieve_and_49999_unsieve.ipynb`,
cell 1.

The standard optimised sieve only needs to strike multiples of `p`
starting at `p²` — every smaller multiple of `p` was already struck by a
smaller prime factor. So `p` contributes a **new** strike only while
`p² ≤ N`. Direct code, not looked up:

```python
>>> primes = sieve_primes(100_000)
>>> max(p for p in primes if p * p <= 100_000)
313
```
Live, runnable: `notebooks/02_the_313_sieve_and_49999_unsieve.ipynb`,
cell 3.

313 is the answer: the last prime with anything new to strike at
`N = 10⁵`.

### 4.5 Composite primes — the closed alphabet

What that boundary actually splits the primes into, checked directly
rather than reasoned about in prose (`_spf_gpf_tables(100_000)`, every
composite `≤ 10⁵`, no sampling):

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
Live, runnable: `notebooks/02_the_313_sieve_and_49999_unsieve.ipynb`,
cell 7.

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
