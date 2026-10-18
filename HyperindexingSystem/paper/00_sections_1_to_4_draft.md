# The Hyperindexing System: Data With No Physical Location
### Draft, sections 1–4 (2026-09-30). Listings are extracted verbatim from `paper/listings/`; `python3 paper/test_listings.py` runs them cold and re-checks every claim below. Notebooks: `notebooks/p01_babel_to_ordered/`.

---

## 1  Location by computation

**1.1  The premise.** In Borges's "The Library of Babel" [Borges1941] every possible book exists and none is written: a book is found, not made. The site `libraryofbabel.info` [BasileSite] realises the premise for all pages of 3,200 characters over 29 symbols (26 letters, space, comma, period): about 10^4677 books of 410 pages, each with one permanent location, nothing stored on disk. The site states the mechanism in one sentence: a pseudo-random number generating algorithm that is *invertible*, so that "for any block of text, the program can work backwards to calculate its location" [BasileTheory4].

**1.2  The published recipe.** The code Basile published [BasileAlgo2019] is the one for the site's image library; the text library's own algorithm is an earlier one and is not published (its README: "I've shared the algorithm for babelia … because it is significantly more efficient than the one I wrote for libraryofbabel.info"). The README gives the recipe: a linear congruential generator, `pointer = (a·pointer + c) mod m`, followed by shift/XOR steps, inverted by `a⁻¹` and by undoing the shifts in reverse order; `m` must exceed the number of pages, and `a`, `c` must satisfy the Hull–Dobell conditions so that the LCG is a full-period bijection. The README adds that the LCG alone "did not create sufficiently random-seeming results", which is why the shifts are there.

**1.3  A realisation small enough to check.** Listing 2 is our own construction from that recipe (not Basile's code, which is CC BY-SA-NC and for a different set); it is the same map as `power_of_two_scrambler` in the ValaQuenta engine `basile`, which also runs Basile's published engine on his published constants. It scrambles the integers `[0, N)`: an LCG modulo `2^e ≥ N` with `a ≡ 1 (mod 4)`, `c` odd (Hull–Dobell for a power of two), two xorshift steps, and cycle-walking to stay inside `[0, N)`.

**Listing 1 — the ordered address, `text ↔ integer` (`paper/listings/L1_ordered_address.py`, verbatim; used from §2)**

```python
# Listing 1 - the ordered address (bijective base-N): text <-> non-negative integer
def address(text, alphabet):
    """Rank of `text` among all strings over `alphabet`, shortest first, then alphabetical."""
    N, a = len(alphabet), 0
    for ch in text:
        a = a * N + alphabet.index(ch) + 1
    return a - 1

def text_at(a, alphabet):
    """Inverse of address(): the string whose rank is `a`."""
    N, out = len(alphabet), []
    a += 1
    while a > 0:
        a, r = divmod(a - 1, N)
        out.append(alphabet[r])
    return "".join(reversed(out))

def page_at(loc, alphabet, k):
    """Fixed-length page: the k-digit base-N numeral of `loc` (digit 0 = first symbol)."""
    N, out = len(alphabet), []
    for _ in range(k):
        loc, r = divmod(loc, N)
        out.append(alphabet[r])
    return "".join(reversed(out))

def loc_of(page, alphabet):
    """Inverse of page_at()."""
    N, loc = len(alphabet), 0
    for ch in page:
        loc = loc * N + alphabet.index(ch)
    return loc
```

**Listing 2 — an invertible scrambler of `[0, N)` (`paper/listings/L2_scrambler.py`, verbatim)**

```python
# Listing 2 - an invertible scrambler of [0, N): LCG + xorshift, cycle-walked into range
def make_scrambler(N, a=1664525, c=1013904223, s1=7, s2=5):
    e = max(1, (N - 1).bit_length()); M = 1 << e; mask = M - 1
    a_inv = pow(a, -1, M)                       # a odd -> invertible mod 2^e
    def f(x):                                   # bijection on [0, M)
        x = (a * x + c) & mask                  # Hull-Dobell: a = 1 mod 4, c odd
        x ^= x >> s1
        x ^= (x << s2) & mask
        return x
    def finv(y):
        z = y
        for _ in range(e // s2 + 1): z = y ^ ((z << s2) & mask)
        y = z
        for _ in range(e // s1 + 1): z = y ^ (z >> s1)
        return (a_inv * (z - c)) & mask
    def scramble(x):                            # bijection on [0, N)
        x = f(x)
        while x >= N: x = f(x)
        return x
    def unscramble(y):
        y = finv(y)
        while y >= N: y = finv(y)
        return y
    return scramble, unscramble
```

On the toy library (29 symbols, 3-character pages, N = 29³ = 24,389 pages) the scrambler was checked on **every** location, not sampled:

With Listings 1 and 2 loaded:

```
> ALPHA = "abcdefghijklmnopqrstuvwxyz ,."
> scramble, unscramble = make_scrambler(24389)
> len({scramble(x) for x in range(24389)}), all(unscramble(scramble(x)) == x for x in range(24389))
(24389, True)
> for loc in range(6): print(loc, repr(page_at(scramble(loc), ALPHA, 3)), repr(page_at(loc, ALPHA, 3)))
0 'blr' 'aaa'
1 'lrq' 'aab'
2 'wfl' 'aac'
3 'is,' 'aad'
4 'did' 'aae'
5 ',dz' 'aaf'
```

Between the pages at locations L and L+1, over all 24,388 neighbouring pairs, the scrambled library differs in **2.910** of 3 characters (independent pages would give 2.897); the ordered numeral in the right-hand column differs in 1.036. Both libraries hold the same 24,389 pages, a location costs log₂ 24,389 = 14.57 bits in each, and neither stores a table: the scrambler is O(log N) arithmetic.

---

## 2  The ordered address

**2.1  The dictionary.** The Hyperwebster, as presented in Vsauce's *The Banach–Tarski Paradox* [VsauceBT], is a dictionary that "lists every single possible word of any length formed from the 26 letters in the English alphabet", and its volume trick is that "if they put all the words that begin with 'a' in a volume titled 'A,' they wouldn't have to print the initial 'a'". (The dictionary is attributed in the video to Ian Stewart [Stewart1996] `Post-Hoc:` the book has not been checked.) Read as a computation, the dictionary is Listing 1: the address of a word is its rank among all words, shortest first and alphabetical within a length; the word at an address is recovered by repeated division. There is no zero digit, so `a` and `aa` are different (`address("a") = 0`, `address("aa") = 26`).

```
> A26 = "abcdefghijklmnopqrstuvwxyz"
> [(n, text_at(n, A26)) for n in (0, 1, 25, 26, 27, 701, 702)]
[(0, 'a'), (1, 'b'), (25, 'z'), (26, 'aa'), (27, 'ab'), (701, 'zz'), (702, 'aaa')]
> all(address(text_at(n, A26), A26) == n for n in range(20000))
True
```

**2.2  Volume A.** The map `w ↦ "a" + w` takes the set of all words (including the empty word) onto the words that begin with `a`. Checked over all 475,255 words of length ≤ 4: volume A holds 18,279 of them, and stripped of their initial letter they are 18,279 distinct words, exactly the words of length ≤ 3. In the address the trick is arithmetic, because prepending a letter of digit value 1 adds a place value:

```
> import itertools
> A26 = "abcdefghijklmnopqrstuvwxyz"
> words = [""] + ["".join(p) for n in range(1, 5) for p in itertools.product(A26, repeat=n)]
> len(words), sum(w[:1] == "a" for w in words), len({w[1:] for w in words if w[:1] == "a"})
(475255, 18279, 18279)
> all(address("a" + w, A26) - address(w, A26) == 26 ** len(w) for w in words if len(w) <= 3)
True
```

(The last line ranges over the words of length ≤ 3, so that `"a" + w` stays within the list.)

**2.3  The relation to §1.** Listing 2 is a permutation of the integers that Listing 1 assigns to pages. The library of §1 and the dictionary of §2 hold the same set of texts. What they differ in is the order: in the ordered address `address("aac") − address("aab") = 1` and the location of `"b" + w` minus the location of `"a" + w` is one number for every `w`; in the scrambled library the same differences take 762 distinct values over the 841 two-character suffixes tested and the neighbours `aab`, `aac` are 13,427 places apart.

---

## 3  Definition

A **hyperindex** is a bijection between a set of texts and an initial segment of the non-negative integers such that

1. the integer is computed from the text, and the text from the integer, with no table stored or consulted; and
2. it is exact: no two texts share an integer and every integer below the bound is the location of a text.

Data held under a hyperindex is *located*, not stored: a location and (for variable-length texts) a length suffice to regenerate it. Two families satisfy the definition and were measured in §1 and §2:

| | ordered (Listing 1) | scrambled (Listing 2 ∘ Listing 1) |
|---|---|---|
| exact bijection on the 24,389 pages | yes | yes |
| bits per location | 14.57 | 14.57 |
| table stored | none | none |
| neighbouring pages differ in (of 3 characters) | 1.036 | 2.910 |
| `loc("b"+w) − loc("a"+w)` over 841 suffixes | 1 value | 762 values |

**Where the two meet.** Basile's algorithm lends addressing as a tool to the hyper-index methodology, in which the index is itself text held in JSON files and is indexed in turn, layer above layer (§4). The author's negative-space focus gave the idea to build the Hyperwebster from empty first: the empty word is the root of the dictionary, every word is reached from it by appending symbols, and in Listing 1 it sits at address −1, one place before the first symbol.

```
> A26 = "abcdefghijklmnopqrstuvwxyz"
> address("", A26), text_at(-1, A26), address("a", A26)
(-1, '', 0)
```

The ordered family keeps the structure of the text in the integer: a prefix is a place value, a one-symbol edit is `± N^i`, and the volume trick is a subtraction. The scrambled family removes it deliberately. Neither compresses: a location has the information content of the text it names.

---

## 4  What follows

The remainder of the paper is the ordered family in every form it took in the author's code between April and September 2026: twenty versions, each with its source, the notebooks that run it and the measurements taken (wiki pages 01–20), classified by what an address preserves (page 21), read against the permutation structure of the address (page 22) and against the scale of the Library of Babel (page 23). Failures are results and are kept as runnable code.

### References (this draft)
- [Borges1941] J. L. Borges, "The Library of Babel", 1941.
- [BasileSite] `libraryofbabel.info` (About page; forum `reddit.com/r/BabelForum/`); the site is the progenitor of the system (built against, no tag). Its author, J. Basile, is `Post-Hoc:`.
- [BasileTheory4] `Post-Hoc:` J. Basile, "Grains of Sand", `libraryofbabel.info/theory4.html`.
- [BasileAlgo2019] `Post-Hoc:` J. Basile, `github.com/librarianofbabel/libraryofbabel.info-algo` (uploaded 2019-01-02, CC BY-SA-NC; local copy `Ainulindale/references/babel/`).
- [VsauceBT] Vsauce, "The Banach–Tarski Paradox" (transcript: `sites.google.com/site/vsaucetranscripts/scripts/the-banach-tarski-paradox`).
- [Stewart1996] I. Stewart, *From Here to Infinity*, 1996. `Post-Hoc:` not checked.
