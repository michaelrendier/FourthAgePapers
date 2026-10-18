# citations.md — HyperindexingSystem

Working notepad. Note (2026-09-30, Cody): the SITE libraryofbabel.info is the progenitor (built against, no tag); BASILE as author, his theory pages, repositories and algorithm are `Post-Hoc:` (found 2026-09-29, after the code).

Rule (Post-Hoc protocol, ScalarContextPropagation §2.2): **no tag** = a source built against on
purpose; **Post-Hoc:** = a correspondence found after the code worked. Citation counts are OpenAlex `cited_by_count`,
fetched 2026-09-29 (they move; re-fetch before submission). "Read" = the full text was opened and checked this session;
"metadata only" = counts/abstract from OpenAlex, text not opened (paywalled or not fetchable) — do not quote from these
until read. PDFs that were free are in `Ainulindale/references/permutation_papers/`.

## Premise (lead of the paper)

| Tag | Work | Notes |
|---|---|---|
| (built against) | J. L. Borges, "The Library of Babel" (1941) | English PDF and Spanish text linked from libraryofbabel.info/About.html |
| (built against) | libraryofbabel.info — the site (About: https://libraryofbabel.info/About.html; forum: https://www.reddit.com/r/BabelForum/); the progenitor of the hyperindexing system | property relied on: text locations are permanent, all permutations accessible at once. Site says the full library is every combination of 1,312,000 characters; the site holds all pages of 3,200 characters |
| Post-Hoc | J. Basile (the site's author, learned of 2026-09-29), *Tar for Mortar: "The Library of Babel" and the Dream of Totality* | open-access via OAPEN link on the About page |
| Post-Hoc | J. L. Borges, "The Total Library" (1939 essay) | linked from the About page; not read |
| Post-Hoc | I. Stewart, *From Here to Infinity* (1996), the Hyperwebster | source of the name via the Vsauce video; book not checked |

## Permutation ranking, generation, sampling

| Tag | Work | Cites | Read? | Connects to |
|---|---|---|---|---|
| Post-Hoc | W. Myrvold, F. Ruskey (2001), *Ranking and unranking permutations in linear time*, IPL 79, 281–284 | 127 | **read** (4 pp, `MyrvoldRuskey_2001.pdf`) | the [0, N!−1] permutation index that `v09/core/charset.py` names as the PRIVATE charset key: rank1/unrank1 do it in O(n) by driving Fisher–Yates with the integer's mixed-radix digits |
| Post-Hoc | R. Durstenfeld (1964), *Algorithm 235: Random permutation*, CACM 7(7) | 462 | metadata only (ACM 403) | the shuffle inside Myrvold–Ruskey's unrank1 |
| Post-Hoc | R. Sedgewick (1977), *Permutation Generation Methods*, ACM Comput. Surv. 9(2) | 262 | metadata only (ACM 403) | survey of generation orders; frames "the address space is an ordering of permutations" |
| Post-Hoc | G. Ehrlich (1973), *Loopless Algorithms for Generating Permutations, Combinations, and Other Combinatorial Configurations*, JACM 20(3) | 184 | metadata only | adjacent-transposition orders; the O(1) transposition offset (T7 in the 2026-09-29 code audit) is the address-space version |
| Post-Hoc | J. R. Bitner, G. Ehrlich, E. M. Reingold (1976), *Efficient generation of the binary reflected Gray code and its applications*, CACM 19(9) | 238 | metadata only | same |
| Post-Hoc | T. M. Cover (1973), *Enumerative source encoding*, IEEE Trans. IT 19(1) | 508 | metadata only (paywalled) | exact rank of a sequence within its composition class = (count vector, rank) address measured in T7 (0.79× naive at L=1000–4000); also `hyperwebster_manifold.py`'s position sub-addresses |
| Post-Hoc | D. Bayer, P. Diaconis (1992), *Trailing the dovetail shuffle to its lair*, Ann. Appl. Probab. 2(2) | 321 | metadata only | permutations reached by composing shuffles; rotation/shuffle group view |
| Post-Hoc | D. Aldous, P. Diaconis (1986), *Shuffling cards and stopping times*, Amer. Math. Monthly 93 | 345 | metadata only | same |

## Rotations of a string, sorted (the tabula recta as a data structure)

| Tag | Work | Cites | Read? | Connects to |
|---|---|---|---|---|
| Post-Hoc | M. Burrows, D. J. Wheeler (1994), *A Block-sorting Lossless Data Compression Algorithm*, DEC SRC Research Report 124 | 2,352 | **read** (8 pp, `Burrows_Wheeler_1994.pdf`) | forms all N rotations (cyclic shifts) of a string, sorts them, keeps the last column — the rotations are the rows of a Vigenère tabula recta; the output is a permutation of the input and is reversible with the index I |
| Post-Hoc | U. Manber, G. Myers (1993), *Suffix arrays: a new method for on-line string searches*, SIAM J. Comput. 22(5) | 1,953 | metadata only | a suffix array is a permutation of positions; sorted-order index over a text |
| Post-Hoc | P. Ferragina, G. Manzini (2000/2002), *Opportunistic data structures with applications*, FOCS | 1,101 | metadata only | FM-index: compressed index built on the BWT |

## Permutation-based indexing and comparing permutations

| Tag | Work | Cites | Read? | Connects to |
|---|---|---|---|---|
| Post-Hoc | E. Chávez, K. Figueroa, G. Navarro (2008), *Effective proximity retrieval by ordering permutations*, IEEE TPAMI 30(9) | 180 | metadata only | an object is indexed by the permutation of reference objects ordered by distance |
| Post-Hoc | G. Amato, P. Savino (2008), *Approximate similarity search in metric spaces using inverted files*, InfoScale | 111 | **read** (`Amato_Savino_2008.pdf`) | same idea with inverted files; objects "represented by permutations of all reference objects" |
| Post-Hoc | R. Fagin, R. Kumar, D. Sivakumar (2003), *Comparing top k lists*, SIAM J. Discrete Math 17(1) | 553 (the SODA record: 761) | metadata only | distances between permutations/partial permutations (Kendall tau, footrule) |

## Vigenère / substitution (cryptanalysis side of the PRIVATE charset)

| Tag | Work | Notes |
|---|---|---|
| (built against) | S. Singh, *The Code Book* (1999) | Vigenère; substitution ciphers broken by frequency analysis; the PRIVATE-charset result (T5: rank-matching alone recovers 44.7% of positions) is chapter 1–2 material |
| Post-Hoc | F. Kasiski (1863); W. Friedman (1922, index of coincidence) | implemented in `Kryptos/analysis.py` (`kasiski`, `index_of_coincidence`, `break_vigenere`); primary sources not opened |

## Not found / not yet fetched
- Lehmer, "Teaching combinatorial tricks to a computer" (1960) and Knuth TAOCP 4A (permutation generation, combinatorial number system): standard references for the combinadic in `hyperwebster_manifold.py`; not fetched.
- Chávez et al. 2008 and Bayer–Diaconis 1992: no open copy found at the URLs tried.

## Added 2026-09-30 (paper §1–§2)

| Tag | Work | Notes |
|---|---|---|
| Post-Hoc | J. Basile, "Grains of Sand", `libraryofbabel.info/theory4.html` | states the mechanism: an invertible pseudo-random number generating algorithm; "for any block of text, the program can work backwards to calculate its location"; early attempts with Halton sequences failed because division made invertibility impossible; the working formula combines modular arithmetic and bit-shifting. Read (page fetched 2026-09-30). |
| Post-Hoc | J. Basile, `github.com/librarianofbabel/libraryofbabel.info-algo` (uploaded 2019-01-02, CC BY-SA-NC, no liability) | the published algorithm is for the **image** library (`babelia`), not the text library; README recipe: LCG `(a·p + c) mod m` + shift/XOR steps, inverted with `a⁻¹` and the shifts undone; Hull–Dobell conditions; the LCG alone was not random-looking enough. Local copy: `Ainulindale/references/babel/` (README, `PRNG`, `imagesearch.cpp`). The paper's Listing 2 is an independent realisation of the recipe, not a copy. |
| (built against) | Vsauce, "The Banach–Tarski Paradox" | transcript `sites.google.com/site/vsaucetranscripts/scripts/the-banach-tarski-paradox`; the Hyperwebster passages quoted in §2 |
| Post-Hoc | I. Stewart, *From Here to Infinity* (1996) | the video attributes the dictionary to Stewart; book not checked |
