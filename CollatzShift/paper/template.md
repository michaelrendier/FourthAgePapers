# A Bit Shift Wearing A Disguise

### The Collatz map as the one-sided binary shift: a code paper, with computed checks

**Cody Michael Allison** (Michael Rendier), independent researcher · the.wandering.god@gmail.com · [ORCID 0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760) · github.com/michaelrendier\
**Written by an AI assistant:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), with the author's [`cs-paper-code-conventions` skill](https://github.com/michaelrendier/ContextPlease/blob/main/claude/skills/cs-paper-code-conventions/SKILL.md) running\
**Date:** @@DATE@@ · **Status:** draft for expert review · **Code:** [FourthAgePapers/CollatzShift](https://github.com/michaelrendier/FourthAgePapers/tree/main/CollatzShift)

---

> ## Read this first: who wrote this, and how
>
> **The assistant.** This paper was written by a transformer language model, Claude Sonnet 5.5 (`claude-sonnet-5-5`), working with the author's `cs-paper-code-conventions` skill active; the skill decides how code is shown in a paper (it is linked above and described in Appendix A). The original engine and README for this topic were committed on 2026-08-21 co-authored by an earlier model (Claude Opus 5); this rewrite, the new code in `engine/`, and the text are from 2026-10-14.
>
> **The author.** The author is a software engineer, not a trained mathematician, and says so. He is asking mathematicians to read this critically. **Every statement here that is not attributed to a cited source should be treated as unverified until an expert has looked at it.**
>
> **The method.** The author deliberately does not tell the assistant what result he is looking for or hoping for. Tasks are given as measurements ("run it through the engine", "chase that anomaly to its source"), so that he is not handed the answers he wants. This is a safeguard, not a guarantee: an assistant can still infer an expectation from context. The real safeguards are exact enumeration, a control before each measurement, and the rule that **failures stay in the code and in the paper** (Section 7).
>
> **What kind of paper this is.** A code paper. It shows the programs, what they compute, how to run them, and what came out. It contains no proofs. Where a result is in the literature it says so and cites it.

---

## Abstract

We describe three small, self-checking Python programs (standard library only, a few seconds each) and report what they compute about the Collatz shortcut map T(n) = n/2 (n even), T(n) = (3n+1)/2 (n odd). The first exhibits T, on residue classes mod 2^k, as the one-sided binary shift under the parity-vector conjugacy of Lagarias, Bernstein and Bernstein–Lagarias, and re-checks ten relations exhaustively or by stated sampling. The second re-computes the numerical tables of Bernstein and Lagarias (1996) for the conjugacy map: the cycle table agrees for every row we computed (n ≤ 16), the order 2^(n−4) and the power-of-two cycle lengths are reproduced, and the counts of odd fixed points agree with @@N_OK23@@ of 99 entries of their Table 2.3 and @@N_OK24@@ of 100 entries of their Table 2.4 for n up to 1000. The disagreements form one block (n = @@MM23@@ in Table 2.3; n = @@MM24@@ in Table 2.4) in which the printed number is our number for n+1; we cannot tell whether the printed table or our reading of it is at fault, and we ask readers to adjudicate. The third reads the map through the author's GenerationalLineage engine, which decomposes operations into three primitives, ADD, SCALE and SIGN; we find that the engine's SIGN (a reflection) occurs in neither branch of T, so the earlier statement "T = ADD ∘ SCALE ∘ SIGN" in this repository conflated a parity selector with that primitive, and we correct it. A control that appeared to show a statistical signature in Collatz parity streams is traced to its source and found to be an artefact of our own matching. We make no claim about the conjecture.

---

## 0. Scope and labels

**Not a Fourth Age paper.** This directory sits in the `FourthAgePapers` repository for historical reasons. The author's Fourth Age template ("One Paper, One Claim") asks for a pre-registered prediction. This paper is a results-and-code paper: it makes **no prediction**, nothing in it is pre-registered, and it is not an instance of that template.

**Labels.** Each result carries a label.

| label | meaning |
|---|---|
| `ESTABLISHED` | stated in the literature (cited); here only re-computed |
| `OURS` | the author's reading or measurement; it may well be known, we did not find it stated |
| `THEORETICAL` | an interpretation inside the author's framework, offered for review |
| `OPEN` | a question we cannot settle |
| suffix `:CALCULATED` | the number or statement is produced by code in this repository and reproduced in this paper (`python3 engine/...`); **CALCULATED is not DERIVED**: an engine ran, deterministically and inspectably, but no symbolic proof chain is claimed |

A label is placed next to the result it describes. A result without code carries no `:CALCULATED`. The original engine prints its own provenance word, `KNOWN` or `OURS`; this paper maps `KNOWN` to `ESTABLISHED` and appends `:CALCULATED`, and the engine's blocks are shown verbatim, so both words appear.

**Provenance of the literature: built-against and Post-Hoc.** The project distinguishes work the author built against from work he found afterwards. **The Collatz conjecture is the one thing here the author engineered against** (built-against, no tag): it was the first test of the GenerationalLineage engine, chosen as a simple ordering of the integers before any of the literature below had been read. **Everything else cited in this paper was noticed after the code already ran and is marked `Post-Hoc:`** in the references. In particular, the author did not know the Bernstein–Lagarias results when the original engine was written; that his engine reproduces their tables is a check on the code, not evidence that he derived them.

## 1. Introduction

The Collatz conjecture asserts that every positive integer reaches 1 under iteration of T. It is well known that T, extended to the 2-adic integers Z₂, is conjugate to the shift (Lagarias 1985; Bernstein 1994; Bernstein–Lagarias 1996), and that the difficulty therefore sits in how the integers lie inside Z₂ and not in the dynamics of the shift itself. This paper does not add to that. It does three narrower things: it shows, with runnable code, ten facts about T that follow from the conjugacy and from elementary counting; it re-computes the published numerical tables of Bernstein–Lagarias and records exactly where our numbers and theirs differ; and it reads T through one particular software framework, the GenerationalLineage engine, whose first real test this map was in August 2026.

**What we do not claim.** Nothing here proves or disproves the conjecture, and nothing here is evidence for or against it.

## 2. Definitions and the literature

Let T be as above. For x in Z₂ let Q(x) = Σ_{i≥0} (T^i(x) mod 2) 2^i be its **parity vector**, and Q_n(x) = Q(x) mod 2^n. Let S be the shift S(x) = ⌊x/2⌋. Then Q(T(x)) = S(Q(x)), so Q conjugates T to S; Φ = Q⁻¹ is the conjugacy map of Bernstein–Lagarias, normalised by Φ(0) = 0. Q_n is a permutation of Z/2^n (a "solenoidal" bijection), and the Collatz conjecture is equivalent to the statement that every positive integer lies in Φ(−⅓Z) (Bernstein–Lagarias, Section 1). **[ESTABLISHED]** (Terras 1976; Lagarias 1985; Bernstein 1994; Bernstein–Lagarias 1996.) We use their definitions throughout; the copies we read are in `references/`.

## 3. The code

Three engines, each standard-library Python, each returning a dictionary and printing a transcript:

| file | what it does | time here |
|---|---|---|
| `engine/e_collatz_shift.py` | the original engine (2026-08-21, unchanged): ten relations about T, each with a provenance label | about 4 s |
| `engine/e_collatz_bl_replication.py` | re-computes the Bernstein–Lagarias tables with two independent algorithms | about 3 s |
| `engine/e_collatz_gl_decomposition.py` | reads T through GenerationalLineage; the control that went wrong | about 7 s |

`python3 paper/make_paper.py` rebuilds this paper from them: every number from code below is taken from a fresh run (the two sentences in Section 5.9 that say "in an earlier run" refer to exploratory scripts kept in ContextPlease, see Appendix A), every listing is extracted verbatim from the engine source and executed in an empty namespace before it is printed, and `--check` reports whether the committed text still matches a fresh build. The files' SHA-256 prefixes are in Section 9.

**Listing 1: the map, the parity vector, and the affine form of T^k on a residue class** (`engine/e_collatz_shift.py`, extracted verbatim; one complete unit)

```python
@@L1@@
```

Cold run of Listing 1:

```
@@T1@@
```

The last line is the whole content of "T is affine on classes": for n ≡ 7 (mod 16), four steps of T are n ↦ (27n + 19)/16 (check: n = 7 gives 13, and 7 → 11 → 17 → 26 → 13), and the exponent d = 3 counts the odd steps, which the class alone determines. (The docstring of `T` in this listing, "SIGN selects, SCALE acts, ADD couples", is the origin of the labelling that Section 5.7 corrects.)

**Listing 2: the odd fixed points of Q_n, by an independent search** (`engine/e_collatz_bl_replication.py`)

```python
@@L2@@
```

```
@@T2@@
```

Bit j of a fixed point is free exactly when a quantity f_j, computable from the lower bits, is 0; otherwise the branch dies. This is a second algorithm for the same counts as the "extend one bit at a time" method in the same file, and the two agree (Section 5.8).

**Listing 3: parity stream of an orbit, and the number of Lyndon factors** (`engine/e_collatz_gl_decomposition.py`; used in Section 5.9)

```python
@@L3@@
```

```
@@T3@@
```

The full transcripts of the three engines are reproduced in Sections 5.1–5.9 below as they are discussed.

## 4. GenerationalLineage

Because Sections 5.7 and 5.9 use it, we describe the engine first, as the author's own software and not as a result.

**What it is.** GenerationalLineage ([repository](https://github.com/michaelrendier/GenerationalLineage), @@GLVER@@, GPL-3.0) tracks the "lineage" of each operation in a calculation, meaning what it can be built from, in order that anything which cannot be built from the list is visible rather than silent. The author calls the project "Generational" because the word carries four meanings at once: descent, a generating set, a code generator (an iterator that holds its state), and a generation (a level or cohort). The engine and its skill are documented in the repository and in [the skill file](https://github.com/michaelrendier/ContextPlease/blob/main/claude/skills/generational-lineage/SKILL.md).

**The domain.** Operations are placed against a fixed domain whose floor is three primitives: **ADD** (identity 0), **SCALE** (identity 1) and **SIGN** (a single bit: a ±1 reflection). Above them are tiers: tier 1 (reflect, dilate), tier 2 (fixed sets: origin, anchor, boundary), tier 3 (counts and ratios of the layer below). An operation must land in exactly one place; one that lands nowhere is flagged as a possible new operator, and one that lands in two is taken to be mis-decomposed.

**The decomposition test.** For any named operator the engine asks, in order: is it a count or a ratio of something else (tier 3)? is it a fixed set (tier 2)? does it change length (so it needs DILATE)? does it need an added constraint to exist (a corollary, not a primitive)? Only what survives all four is a candidate primitive.

**Three kinds of wrong.** The engine keeps apart a CODE fault (the check did not run, so the claim is unjudged), a MATHS fault (both sides were measured and disagree, so the claim is false) and a METHOD error (correct code, correct maths, wrong approach, invisible to both). Section 7 uses these words.

**Factor moves.** Thirty-one toolsets share a contract (`descend` is free; `build_up` is paid or refuses with `AscentNotFree`; `verify` self-checks). This paper uses one of them, `lyndon` (unique non-increasing factorisation of a word into Lyndon words), and the engine's `ADD:SCALE:SIGN` element algebra with its recorded "Long Path" and set-membership test (the rule that decides Recamán's flip).

**Why this map.** The Collatz map was the first real computation the author ran through the engine, in August 2026, chosen as the simplest non-trivial ordering of the integers. The engine has grown since (a public 1.0.0 release, thirty-one self-verifying toolsets), so this paper re-runs the test against the current engine and does not quote the old one. **The engine and this paper share an author and an assistant; the check is not independent**, and we say so rather than imply otherwise.

**The decomposition the original engine reported** (computed, from `e_collatz_shift.py`):

| operation | tier | descends from | status |
|---|---|---|---|
@@LINEAGE_ROWS@@

The last row, "T = ADD ∘ SCALE ∘ SIGN", is the statement Section 5.7 re-examines.

## 5. Results

### 5.1 T^k is affine on residue classes mod 2^k

@@R1@@

### 5.2 The parity vector is a bijection; T is conjugate to the shift

@@R2@@

@@R3@@

### 5.3 Counting: the class tree is Pascal's triangle

@@R4@@

@@R5@@

The author's reading is that the apparent chaos of the d-histogram is the binomial triangle seen in the wrong metric. We believe this to be elementary once stated, and we claim the framing at most.

### 5.4 Cycles and the denominator 2^k − 3^d

@@R6@@

A bounded search (k ≤ 200, d ≤ 200) finds @@PM@@ pairs with |2^k − 3^d| = 1: @@PM_LIST@@. **[ESTABLISHED:CALCULATED]** for that range; that these are all such pairs with d ≥ 1 in general is a theorem of Catalan type (Mihăilescu) which we cite and do not prove. The original text of this repository stated only the pair (2,1) for 2^k − 3^d = +1, which is correct for d ≥ 1 but incomplete if the absolute value is meant; we state it here with the full list.

### 5.5 Leaves, and the two directions

@@R7@@

@@R8@@

@@R9@@

The reading offered is that forward T destroys one bit per step (entropy log 2), the backward tree on N restores log(4/3), and the shortfall log(3/2) is the odd branch's own gain. We believe each ingredient is elementary and we do not know whether the combined accounting appears in the literature. **OURS.**

### 5.6 The drift

@@R10@@

### 5.7 Reading T through GenerationalLineage

**[THEORETICAL:CALCULATED]**

*What the original paper said.* "T = ADD ∘ SCALE ∘ SIGN; no new generator is required", where SIGN was taken to be the parity bit that selects a branch.

*What the current engine shows.* Written as engine elements (x ↦ sign·scale·x + add), the even branch is SCALE(1/2) and the odd branch is ADD(1/2) after SCALE(3/2). The engine's SIGN, a ±1 factor, occurs in **neither** branch. Composing the branch elements along the true parity word reproduces T^k on every residue class mod 2^k for k ≤ 12: @@A_CLASSES@@ classes checked, @@A_BAD@@ mismatches, slope exactly 3^d/2^k. The parity bit is a *selector between two elements of the affine group*, not an application of the engine's SIGN. **The earlier sentence conflated the two and is corrected here.** What survives is the narrower statement: T is a piecewise map whose two pieces are generated by SCALE and ADD, selected by one bit. The engine's firing order, innermost first, is SIGN, SCALE, ADD, which is also the order in which the odd branch acts (select, scale by 3/2, add 1/2); firing ADD first would need the non-integer constant 1/3. This is a statement about how the author's framework names things, offered for review.

*The engine's Long-Path memory.* The engine records an operation's trajectory and the set of values already visited, the same test that decides Recamán's flip. On the orbits tried the first value to repeat is always 2, one step after the orbit reaches 1: @@FIRST_COLL@@. **[THEORETICAL:CALCULATED]** The reading is that the Collatz conjecture is equivalent to the statement that, for every n, the first repeated value in the orbit is in the loop {1, 2}, or no value repeats (divergence). That equivalence is immediate and is not new; what the engine adds is that the test is already implemented.

### 5.8 Replication of the Bernstein–Lagarias tables

**[ESTABLISHED:CALCULATED]** for the agreements; **[OPEN:CALCULATED]** for the one disagreement.

Transcript of `python3 engine/e_collatz_bl_replication.py`:

```
@@EX_BL@@
```

- The cycle table (their Table 2.2, the number of cycles of each length 2^j of Φ̂_n, the map on odd residues) agrees for every row we computed; the order of Q_n @@ORD_OK@@ and equals 2^(n−4); every cycle length is a power of two; the solenoidal property has @@SOL@@ violations. These are theorems or tabulated facts in Bernstein–Lagarias; we only reproduce them.
- The odd fixed-point counts (1-cycles) are computed by two independent algorithms that agree with each other. They agree with @@N_OK23@@ of the 99 entries of Table 2.3 and @@N_OK24@@ of the 100 entries of Table 2.4 (n up to 1000). Odd fixed points at n = 10, 100, 200, 500, 1000: @@FP10@@, @@FP100@@, @@FP200@@, @@FP500@@, @@FP1000@@.
- **The disagreement.** The printed numbers differ from ours at n = @@MM23@@ (Table 2.3) and n = @@MM24@@ (Table 2.4). In @@SHIFT@@, the printed value for n equals our value for n+1: the block looks like a one-cell shift. We checked that our two algorithms agree with each other, that both agree with the printed tables at every other entry (including on both sides of the block), and that the retypeset 2022 version of the paper prints the same numbers as the 1996 preprint, so a layout or OCR error in our transcription is unlikely. We cannot exclude a fault in our code that happens to affect exactly these n, or a slip in the printed table or in the data it was built from. **We do not know which is right**; this is the first of the questions in Section 8.
- **What the chase added.** (i) *Soundness:* each of the @@WA_N@@ odd fixed points our code lists for n = 60..80 was re-checked by plain iteration of T (the parity vector of the residue, computed directly, equals the residue); @@WA_UNSOUND@@ fail. So nothing in our lists is spurious; if we are wrong in the window, we are wrong by omission, and completeness rests on the lifting step (a fixed point mod 2^(n+1) reduces to one mod 2^n) that both of our algorithms use, which is the one assumption not tested independently here. (ii) *Shape:* compared as multisets over n = 66..80, the printed block and ours differ in exactly one value each way: @@WA_OURS@@ occurs only in ours and @@WA_PRINTED@@ only in the printed table, which is what a single deleted cell plus a single duplicated cell in a typeset table would produce. This is consistent with a slip in the printed table; it does not prove one. (iii) *Outside sources:* Rozier (2018) tabulates the counts N_k of odd ergodic sets for k ≤ 16, citing Bernstein–Lagarias Table 2.2; we read those values as consistent with the Table 2.2 columns, but we did not compare them entry by entry, and k ≤ 16 does not reach the window, and we found no published source for the counts at n = 66..78.

### 5.9 Parity streams, controls, and a recorded fault

**[OURS:CALCULATED]**

Transcript of `python3 engine/e_collatz_gl_decomposition.py`:

```
@@EX_GL@@
```

*What looked like a result.* Taking the parity stream of an orbit as a binary word, the number of factors in its Lyndon factorisation was higher for Collatz orbits than for random bit strings of the same length (8 to 10 against 5 to 7, for five orbits), while linear complexity and a grammar-compression ratio were indistinguishable from random.

*Chasing it.* (i) The engine's Lyndon tool and an independent implementation agree. (ii) Forcing the first bit to 1 raises the count for random bits themselves: a stream of 115 random bits has @@FB_FREE@@ factors on average, @@FB_ONE@@ if its first bit is 1 and @@FB_ZERO@@ if it is 0. Every start we had used was odd, so every stream began with 1. (iii) A stream that reaches 1 must end in a nearly forced pattern (the last six bits were 001000 in 284 of 300 starts in an earlier run). (iv) Mean z-scores of the Collatz streams to 1 for odd starts: unmatched control @@Z_UN@@, control matched on the first bit @@Z_FB@@, control matched on the first bit and the last six bits @@Z_BOTH@@; for even starts with matched controls @@Z_EVEN@@. **The excess is an artefact of our control, not a property of the parity stream.** We classify it, in the engine's vocabulary, as a METHOD error (the control was not matched on the conditioning). It is recorded here because it is the kind of error a reader is likely to make, and it is *not* offered as a question.

*The sanity check that did hold.* By the conjugacy, the first k parities of a *random* n are independent fair bits; for 400-bit random n the Lyndon-factor counts match random bits with the same first bit (an earlier run: 7.02 and 5.04 against 7.04 and 5.02 for odd and even n).

## 6. What this does and does not show

It shows that three short programs reproduce the standard structure of the shortcut map and the published Bernstein–Lagarias tables (with one block of disagreement), that the map's two branches are the elements SCALE(1/2) and ADD(1/2)∘SCALE(3/2) of the affine group selected by one bit, and that one tempting statistical signature in Collatz parity streams is an artefact of mismatched controls. It does **not** bear on the conjecture, does not prove any of the cited theorems, and does not establish that the GenerationalLineage reading is useful to anyone but its author.

## 7. Faults and negative results, kept

| # | what | kind | status |
|---|---|---|---|
| 1 | Necklace filter kept rotation-minimal words, not primitive ones: one loop reported as seven (original run). Re-found with the engine's Lyndon tool: @@RM@@. | CODE | fixed in the original engine |
| 2 | An assertion that the fibre of T has size 4 against a correct measurement of 2 (original run) | CODE (wore a MATHS fault's label) | assertion corrected |
| 3 | A predicted backward out-degree 7/6 from a condition that does not exist: "(2n−1)/3 is odd" is vacuous, because 2n−1 and 3 are both odd | MATHS (in the prediction) | corrected; the exact value is 4/3 |
| 4 | "T = ADD ∘ SCALE ∘ SIGN" conflated a parity selector with the engine's SIGN (Section 5.7) | METHOD (labelling) | corrected in this paper; the original README is unchanged |
| 5 | A Lyndon-factor excess in Collatz parity streams: control not matched on first bit and forced tail (Section 5.9) | METHOD | resolved: artefact |
| 6 | A block of 13 entries of Bernstein–Lagarias Table 2.3 (and n = 70 of Table 2.4) disagree with two independent computations (Section 5.8) | OPEN | for the reader |
| 7 | While gathering references, a guessed URL returned an unrelated paper; it was caught by reading the file's own title page and discarded. Four cited works could not be downloaded automatically (see `references/README.md`) | process | recorded |

## 8. Questions for the reader

1. **Table 2.3 / 2.4.** Is the printed block n = @@MM23@@ (and n = @@MM24@@ in Table 2.4) in Bernstein–Lagarias a misprint or a data slip, or is our count wrong there? (Both of our algorithms are in `engine/e_collatz_bl_replication.py`; Section 5.8 gives the numbers.)
2. **The accounting in Section 5.5**: forward 2-to-1 (log 2 nats per step), backward mean out-degree 4/3 (log(4/3)), shortfall exactly log(3/2). Is this exact statement in the literature?
3. **Section 5.7**: is it reasonable to describe T as a selector between two elements of the affine group, generated by a scaling and a translation, and to keep the engine's SIGN out of it? Does this say anything beyond the observation that T is piecewise affine?
4. **Beyond n = 1000.** The second algorithm reaches n = 1000 in about two seconds. Would counts at larger n, or other statistics of Φ̂_n, be of interest, and are there known predictions (for instance the heuristic Bernstein–Lagarias give for the growth of the number of 1-cycles) worth testing against them?

## 9. Reproducibility

```
cd FourthAgePapers/CollatzShift
python3 engine/e_collatz_shift.py            # about 4 s: the ten relations
python3 engine/e_collatz_bl_replication.py   # about 3 s (add --full for n <= 18 cycles and the slower lineage method to n = 200)
python3 engine/e_collatz_gl_decomposition.py # about 7 s; needs GenerationalLineage next to this repository or GL_PATH
python3 paper/make_paper.py --check          # does this paper match a fresh build?
```

Environment of this build: Python 3.12.3, a ThinkPad X1 Carbon (6th gen, Core i7-8550U); building the paper took about @@RUNTIME@@ s. SHA-256 prefixes of the engine files used:

| file | sha256 (first 12) |
|---|---|
@@HASHES@@

The original engine's own transcript (relations and provenance as the original paper labelled them):

```
@@EX_CS@@
```

## References

**The Collatz conjecture itself (the 3x+1 problem) is built-against and carries no tag; every numbered item below is `Post-Hoc:` except item 7.** Copies of the works we could download are in `references/` (and in [ContextPlease](https://github.com/michaelrendier/ContextPlease/tree/main/claude/references/CollatzShift)); the ledger of what was and was not downloaded is [`references/INDEX.md`](https://github.com/michaelrendier/ContextPlease/blob/main/claude/references/INDEX.md).

1. `Post-Hoc:` R. Terras, A stopping time problem on the positive integers, *Acta Arith.* **30** (1976), 241–252. (not downloaded)
2. `Post-Hoc:` C. J. Everett, Iteration of the number theoretic function f(2n) = n, f(2n+1) = 3n+2, *Adv. Math.* **25** (1977), 42–45. (not downloaded)
3. `Post-Hoc:` J. C. Lagarias, The 3x+1 problem and its generalizations, *Amer. Math. Monthly* **92** (1985), 3–23. (not downloaded)
4. `Post-Hoc:` D. J. Bernstein, A non-iterative 2-adic statement of the 3x+1 conjecture, *Proc. Amer. Math. Soc.* **121** (1994), 405–408. (not downloaded; the publisher's site returned a bot-check page)
5. `Post-Hoc:` D. J. Bernstein, J. C. Lagarias, The 3x+1 conjugacy map, *Canad. J. Math.* **48** (1996), 1154–1169. (`references/Bernstein_Lagarias_1996_retypeset.pdf`, preprint copy also included)
6. `Post-Hoc:` J. C. Lagarias, The 3x+1 problem: an annotated bibliography (1963–1999), arXiv:math/0309224v13. (`references/Lagarias_annotated_bibliography_arXiv_math0309224.pdf`; read only for its existence and scope)
7. `Post-Hoc:` O. Rozier, Parity sequences of the 3x+1 map on the 2-adic integers and Euclidean embedding, arXiv:1805.00133v6. (`references/Rozier_2018_parity_sequences_arXiv_1805.00133.pdf`; used only for its table of N_k, k ≤ 16)
8. (built-against; the author's own software, no tag) C. M. Allison, The Generational Lineage Engine, version 1.0.0 (2026), https://github.com/michaelrendier/GenerationalLineage.

(Citation details for items 1–4 are from memory or from publisher listings and should be checked before this draft is circulated further. The paper's own code was executed; the cited papers' proofs were not re-derived.)

---

## Appendix A. What in ContextPlease was used, and what ContextPlease is

**What ContextPlease is.** [ContextPlease](https://github.com/michaelrendier/ContextPlease) is a versioned, human-readable archive of the working context of the author's projects, kept so that a model, or a person, who has never seen the work can come up to speed with historical access. It holds the standing rules and notation, a per-repository current-state file, a dated log of what happened, the *skills* (reusable working methods the assistant is given), every research scratchpad with its scripts and outputs, copies of context primers and wiki pages, and, since 2026-10-14, a ledger of every third-party work downloaded. It is deliberately "manual transmission": nothing in it is loaded automatically; the reader chooses what to read and in what order. A new model should start with [`README.md`](https://github.com/michaelrendier/ContextPlease/blob/main/README.md) (rules, traps, layout), then `claude/.clauderc_context_1` (what is true now) and `claude/.clauderc_context_2` (what happened), then the skills it is pointed at.

**What was used for this paper.**

| in ContextPlease | role in this paper |
|---|---|
| [`README.md`](https://github.com/michaelrendier/ContextPlease/blob/main/README.md) | the standing rules in force: no renormalisation, no fitted parameters; all failures stay in the code and the data |
| [`claude/skills/cs-paper-code-conventions/SKILL.md`](https://github.com/michaelrendier/ContextPlease/blob/main/claude/skills/cs-paper-code-conventions/SKILL.md) | how code appears in a paper: verbatim, numbered, executed-cold listings for short mechanisms; transcripts for sessions; paths for long files; no formula standing in for a loop |
| [`claude/skills/generational-lineage/SKILL.md`](https://github.com/michaelrendier/ContextPlease/blob/main/claude/skills/generational-lineage/SKILL.md) | the decomposition test, the tiers, the three kinds of wrong, the label discipline (Sections 4, 5.7, 7) |
| [`claude/scratchpad/2026-10-14_collatz_gl_rerun/`](https://github.com/michaelrendier/ContextPlease/tree/main/claude/scratchpad/2026-10-14_collatz_gl_rerun) | the exploratory scripts and outputs behind Sections 5.7–5.9 before they were folded into `engine/` |
| [`claude/references/INDEX.md`](https://github.com/michaelrendier/ContextPlease/blob/main/claude/references/INDEX.md) and [`references/CollatzShift/`](https://github.com/michaelrendier/ContextPlease/tree/main/claude/references/CollatzShift) | the literature ledger and the downloaded copies (the Literature Download Protocol) |
| [`claude/.clauderc_citations`](https://github.com/michaelrendier/ContextPlease/blob/main/claude/.clauderc_citations) | the queue of citations by repository |
| [`claude/.clauderc_canonical_maths`](https://github.com/michaelrendier/ContextPlease/blob/main/claude/.clauderc_canonical_maths) (block `@RCCM_CONFIDENCE_TIERS`) | the label tiers, including the `:CALCULATED` suffix |
| [`claude/hooks/clauderc_primer.py`](https://github.com/michaelrendier/ContextPlease/blob/main/claude/hooks/clauderc_primer.py) | the start-of-session map of the files above (documentation copy) |

Not in ContextPlease: the assistant's local memory notes (for example the rule that every download of another person's work is recorded and mirrored beside the paper, and that outbound requests carry a browser-style user agent). Their content is summarised in the ledger and the primer where it matters.

*This appendix is a standing section of every paper the author now writes with an assistant.*
