# Twin-Prime Wheels

### Cutting the primes into circles at the twin pairs: an engineering white paper, with computed results

**Cody Michael Allison** (Michael Rendier), independent researcher · the.wandering.god@gmail.com · [ORCID 0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760) · github.com/michaelrendier\
**Written by an AI assistant:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), with the author's [`cs-paper-code-conventions` skill](https://github.com/michaelrendier/ContextPlease/blob/main/claude/skills/cs-paper-code-conventions/SKILL.md) running\
**Date:** @@DATE@@ · **Status:** results paper, no prediction · **Code:** [FourthAgePapers/TwinPrimeWheels](https://github.com/michaelrendier/FourthAgePapers/tree/main/TwinPrimeWheels)

---

> ## Read this first: who wrote this, and how
>
> **The assistant.** This paper was written by a transformer language model, Claude Sonnet 5.5 (`claude-sonnet-5-5`), working with the author's `cs-paper-code-conventions` skill active; the skill decides how code is shown in a paper. The program and all numbers below were produced on 2026-11-16.
>
> **The author.** The author is a software engineer, not a trained mathematician, and says so. **Every statement here not attributed to a cited source should be treated as unverified until an expert has looked at it.** The wheel construction (twin centres as zero points; circles cut at them) is the author's; the assistant wrote the program that counts it and the text that reports the counts.
>
> **The method.** The author does not tell the assistant what result to find. The task was: build the small program, run it, report. **Failures stay in the paper** (Section 6).
>
> **What kind of paper this is.** A results paper: it shows one short program, what it computes, and what came out. **It makes no prediction**, and by the series' own rule a paper with no prediction is not a Fourth Age paper; it is filed in the Fourth Age directory at the author's request and labelled as a results paper. It contains no proofs, and it does not claim the Twin Prime Conjecture.

---

## Abstract

Every twin pair (p, p+2) has exactly one number between its members, its *centre* c = p+1. Two consecutive centres cut a *wheel*: a circle of circumference L = c′ − c whose zero point is c, and whose last position is the number just before the next zero point. We give a short program (about 110 lines) (NumPy only) that sieves the primes, cuts them into wheels and measures them for N up to 10⁸. Computed results: every centre after (3,5) is a multiple of 6, so every wheel is a whole number of turns of the circumference-6 circle (all @@P1M@@ pairs at N = 10⁸); the number of wheels agrees with the Hardy–Littlewood count to within 1% at N = 10⁶ and 0.02% at N = 10⁸; the distance of the partial Brun sum from Brun's constant equals 4C₂/ln N to four digits at N = 10⁸; the centres occupy the allowed residues of the 30- and 210-circles in nearly equal numbers; a random cutting of the 6-steps into wheels fails (wheel size 6 is 2.4 times rarer than random), and the shortfall is predicted by the Hardy–Littlewood singular series of the prime quadruplet (0, 2, 6, 8). The largest wheel grows with N. Nothing here bears on whether the wheels ever stop; that is the Twin Prime Conjecture.

---

## 0. Scope and labels

Labels follow the author's standing scheme: **ESTABLISHED** (textbook or exact), **THEORETICAL**, **INTERPRETATION**, **CONJECTURE**, **OPEN**. A result computed by the program in this directory carries the suffix `:CALCULATED`. Hedging is allowed in this paper; it is labelled, not hidden.

| Statement | Label |
|---|---|
| Every twin pair (p, p+2), p > 3, has its centre ≡ 0 (mod 6) | ESTABLISHED (p ≡ 5 mod 6) |
| Observed counts of wheels, sizes, Brun tail, singular-series ratio, below | ESTABLISHED:CALCULATED |
| Hardy–Littlewood count of twin pairs | CONJECTURE (1923; unproven) |
| There are infinitely many twin primes | OPEN (the Twin Prime Conjecture) |
| Reading each centre as a *zero point* and each wheel as a circle | INTERPRETATION (the author's) |

## 1. What a wheel is

Write the twin pairs (3,5), (5,7), (11,13), (17,19), (29,31)…; their centres are 4, 6, 12, 18, 30, … Consecutive centres c < c′ cut a wheel: the integers c, c+1, …, c′−1 placed at angle 2π(n − c)/L around a circle of circumference L = c′ − c, with the zero point at c. The next wheel starts at c′, so *the end of one wheel is the beginning of the next*. The first wheel, between the centres of (3,5) and (5,7), has L = 2 and is an exception (4 is not a multiple of 6); every other centre is ≡ 0 (mod 6).

**Listing 1: sieve, centres, wheels** (the core of the program; runs cold with NumPy)

@@L1@@

The first wheels have circumferences 2, 6, 6, 12, 12, 18, 12, 30, … : always whole numbers of 6-steps after the first.

## 2. The primes inside a wheel

**Listing 2: the primes strictly inside each wheel**, not counting the two twin members that flank its ends

@@L2@@

A wheel with L = 6 has nothing inside it (e.g. centres 12 and 18: 11, 13 | 17, 19). The positions of the other primes on a wheel are at angles 2πk/L with k ≡ ±1 (mod 6): they sit beside the sub-circle of circumference 6 that every wheel is a whole number of turns of.

## 3. Results

Program: `twin_wheels.py` (SHA-256 prefix `@@SHA@@`). All runs are exact counts from a sieve; nothing is fitted.

### 3.1 The 6-circle, and the count of wheels

@@CROSS@@

| N | twin pairs (= wheels + 1) | observed / Hardy–Littlewood | mean L | largest L | wheels with L = 6 | mean interior primes | max interior primes |
|---|---|---|---|---|---|---|---|
@@ROWS@@

`:CALCULATED`. The Hardy–Littlewood count is 2C₂ Σ 1/ln²x over x < N, with C₂ = 0.6601618158… the twin prime constant. The agreement is the standard one; it is not a proof of anything and it is a heuristic count (CONJECTURE).

### 3.2 Brun's sum

Brun (1919) showed the sum of 1/p over all twin primes is finite; its value B₂ = 1.9021605831… The partial sum up to N falls short of B₂ by almost exactly 4C₂/ln N, which is what the Hardy–Littlewood density predicts for the tail of the sum.

| N | partial sum | B₂ − partial sum | 4C₂/ln N |
|---|---|---|---|
@@BRUN@@

`:CALCULATED`. (B₂ and C₂ are inputs to the comparison, not computed here.)

### 3.3 The primorial circles

The centres after 6 occupy exactly the allowed residues on the 30-circle (3 of 30: 0, 12, 18) and on the 210-circle (15 of 210), and every allowed residue is used about equally often (at 10⁸: between 146,516 and 146,953 centres on each of the three residues mod 30; between 29,080 and 29,522 on each of the fifteen mod 210). The *sizes* of the wheels then show the 30-circle: if consecutive centres drew their residue mod 30 independently from {0, 12, 18}, the shares of wheels with L ≡ 0, 6, 12, 18, 24 (mod 30) would be 0.333, 0.111, 0.222, 0.222, 0.111. Observed:

| N | L ≡ 0 | 6 | 12 | 18 | 24 (mod 30) |
|---|---|---|---|---|---|
@@MOD30@@

`:CALCULATED`. At 10⁸ the share of wheels with L = 30 (m = 5) is @@M5@@ against @@M4@@ for L = 24 (m = 4): the circumference prefers multiples of the next primorial circle. This is close to, but not equal to, the independent-residue prediction; we did not analyse the remaining difference (OPEN).

### 3.3b The sizes and the largest wheel

At N = 10⁸ there are @@P1M@@ twin pairs; the mean wheel is @@MEANL8@@ long (the N / count figure; the Hardy–Littlewood mean over [0, N] is @@HLMEAN8@@) and the largest is @@LW8@@, centred at @@LWC8@@. The largest wheel grows with N (table above). Whether a wheel can be arbitrarily large is the question of whether twin primes can be arbitrarily sparse; the program says only that up to 10⁸ the largest is a small multiple of the mean.

## 4. A random cutting fails, and the quadruplet explains by how much

**Model (kept as a failure).** If the 6-steps were cut independently with the observed mean wheel, the size m = L/6 would be geometric. It is not: the largest difference between the observed and geometric distribution over all m is @@DEV@@ at N = 10⁸, and the size m = 1 (two centres one 6-step apart) is the clearest miss: observed @@M1@@, geometric @@G1@@.

Two consecutive centres c and c + 6 are the prime quadruplet (c−1, c+1, c+5, c+7). The Hardy–Littlewood singular series of the tuple (0, 2, 6, 8) is 4.1512…; of the pair (0, 2), 1.3203… (= 2C₂). If the quadruplet density were independent twin densities the ratio would be 1; it is S(0,2,6,8)/(6·S(0,2)²) = 0.3969.

**Listing 3: the singular series** (the Hardy–Littlewood product, truncated at primes below 10⁶)

@@L3@@

| N | observed P(m=1) / geometric | predicted 0.3969… |
|---|---|---|
@@QUAD@@

`:CALCULATED`. The observed ratio falls toward the prediction as N grows (0.431, 0.415, 0.410 against 0.397). The wheel size m = 1 is rarer than random for the reason the singular series gives; this reproduces a Hardy–Littlewood prediction, it does not prove it. We did not carry the same calculation to m ≥ 2, where the condition that no centre lies between must also be handled.

## 5. The author's reading

**INTERPRETATION (the author's).** Each centre is a zero point: the one number that belongs to both members of the pair (it is the end of one wheel and the beginning of the next); the wheels are circles of varying size cut at zero points; the prime numbers are then not points on a line but positions on circles, and the circumference-6 circle, the 30-circle and the 210-circle are the sub-wheels of every wheel (Section 3.3). In the Circle Atlas (`ValaQuenta/modules/circle_atlas`, viewport `prime_wheels`) the same objects appear as the rotations p^{−it} of the Euler product; the relation between the integer wheels here and those rotations is stated in `RiemannHypothesisProof/rhp/wrap.py` (Spring 1 and Spring 2) and not re-derived here.

What the program supports: the centres lie on the 6-circle; the number of wheels follows the Hardy–Littlewood count; the wheel-size statistics are those of the 30-circle plus a quadruplet correction. What it does not support: any statement that the wheels never end.

## 6. Failures and wrong turns, kept

1. **A mis-comparison.** The first version compared the mean wheel with the *local* Hardy–Littlewood spacing (ln N)²/(2C₂) = @@HLLOC8@@ at N = 10⁸ and found the mean was @@MEANL8@@, a 12% disagreement. That was the wrong comparison: the mean over [0, N] is N / count, and the spacing grows with N. Compared with the right quantity (@@HLMEAN8@@) the disagreement is gone. It is kept because it is easy to make.
2. **The geometric cutting fails** (Section 4).
3. **The first wheel (3,5)→(5,7) is an exception** (L = 2, centre 4); the multiples-of-6 statements exclude it by name. The pair (5,7), centre 6, is also off the 30- and 210-circle allowed residues because 5 divides 30 and 210 and 7 divides 210; the occupancy counts in Section 3.3 start above 6.
4. **No conversation record of an earlier twin-prime derivation was found** in the four exported `conversation-*.txt` files the author pointed to (the only hits for "twin" are "twin to Planck" and an unrelated passage). The claude.ai project record the author refers to was not available here, so nothing in this paper comes from it.

## 7. Questions for the reader

1. Section 4 reproduces a single Hardy–Littlewood singular-series ratio. Is there a known statement of the whole wheel-size distribution (m ≥ 2) from the singular series, and is it what the sizes in `01_twin_wheels.ipynb` §3 show?
2. Is the preference for L ≡ 0 (mod 30) in Section 3.3 fully explained by the allowed residues {0, 12, 18}, or is there a correlation between consecutive centres beyond it?
3. Is "wheel" or "centre" already a name for this construction in the literature on prime gaps and admissible tuples?

## 8. Reproducibility

```
cd FourthAgePapers/TwinPrimeWheels
python3 twin_wheels.py 1e7          # a few seconds; 1e8 takes about 30 s and 0.1 GB
python3 -c "import twin_wheels; print(twin_wheels.selfcheck())"
python3 paper/make_paper.py --check # does this paper match a fresh build?
```

Environment: Python 3.12, a ThinkPad X1 Carbon (6th gen); building this paper took about @@RUNTIME@@ s. The three results files `results_twin_wheels_N1e6.txt`, `…N1e7.txt`, `…N1e8.txt` are the program's full output; `01_twin_wheels.ipynb` runs the same code with the outputs shown.

## References

Everything below is `Post-Hoc:` (cited after the work was done); details are recalled and should be checked before circulation. The author's own program and the Twin Prime Conjecture's statement are built-against and carry no tag.

1. `Post-Hoc:` G. H. Hardy, J. E. Littlewood, Some problems of "Partitio numerorum" III: on the expression of a number as a sum of primes, *Acta Math.* **44** (1923), 1–70. (not downloaded)
2. `Post-Hoc:` V. Brun, La série 1/5 + 1/7 + 1/11 + 1/13 + … où les dénominateurs sont nombres premiers jumeaux est convergente ou finie, *Bull. Sci. Math.* **43** (1919), 100–104, 124–128. (not downloaded)
3. `Post-Hoc:` Y. Zhang, Bounded gaps between primes, *Ann. of Math.* **179** (2014), 1121–1174. (not downloaded)
4. `Post-Hoc:` J. Maynard, Small gaps between primes, *Ann. of Math.* **181** (2015), 383–413. (not downloaded)
5. `Post-Hoc:` D. H. J. Polymath, Variants of the Selberg sieve, and bounded intervals containing many primes, *Res. Math. Sci.* **1** (2014), art. 12. (not downloaded)
6. (built-against) C. M. Allison, `RiemannHypothesisProof/rhp/wrap.py` (2026), github.com/michaelrendier/RiemannHypothesisProof.

---

## Appendix A. What in ContextPlease was used, and what ContextPlease is

**What ContextPlease is.** [ContextPlease](https://github.com/michaelrendier/ContextPlease) is a versioned, human-readable archive of the working context of the author's projects, kept so that a model, or a person, who has never seen the work can come up to speed with historical access: standing rules and notation, a per-repository current-state file, a dated log, the skills, every research scratchpad with its scripts and outputs, copies of context primers and wiki pages, and a ledger of every third-party work downloaded. Nothing in it is loaded automatically; the reader chooses what to read. A new model should start with its [`README.md`](https://github.com/michaelrendier/ContextPlease/blob/main/README.md), then `claude/.clauderc_context_1` and `claude/.clauderc_context_2`.

**Used for this paper:** the `cs-paper-code-conventions` skill (structure of this paper); `claude/scratchpad/2026-11-13_ainulindale_audit/PROMPT_claudeai_twin_prime.md` (the request for the claude.ai twin-prime record, still unanswered); `RiemannHypothesisProof/rhp/wrap.py` (the prior circle/wheel code, cross-checked in Section 3.1); the 2026-11-16 primer `claude/hist_prime/FourthAgePapers/PRIMER_2026-11-16_CIRCLE_ATLAS.md`.
