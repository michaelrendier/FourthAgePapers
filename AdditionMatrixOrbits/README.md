# The Addition Matrix as Rotors

> **A code paper. Results and code, no prediction.** *The Addition Matrix as Rotors* (source `paper/The_Addition_Matrix_as_Rotors.md`; the PDF is `AdditionMatrixOrbits.pdf` at this level, the only PDF kept) is the paper. It is **not a Fourth Age paper**: it has no pre-registered prediction, so it follows the departure used by `CollatzShift`. It is a **stub for expert review**: the code runs and the numbers are generated, the prose is short.
>
> Written by an AI assistant (Claude Sonnet 5.5, `claude-sonnet-5-5`) with the author's `cs-paper-code-conventions` skill running; the author is a software engineer, not a mathematician. Labels: `ESTABLISHED`, `OURS`, `THEORETICAL`, `OPEN`; suffix `:CALCULATED` = this paper's own code produces the result (not a derivation).

## What it reports

Grade-school multiplication writes one row per digit of the multiplier; adding the rows column by column gives the product. Read as arithmetic modulo 10ᵏ:

1. **Columns are rotors.** The digit in column *c* has exact period 10^(c+1)/gcd(num1, 10^(c+1)) in the multiplier; `x → a·x + b` on ℤ/10ᵐ has the cycle type given by the Chinese-remainder combination of its types on ℤ/2ᵐ and ℤ/5ᵐ; the odometer's first return to the multiples of 10 is the odometer one scale down; on ℤ/2ⁿ every cycle length is a power of two (because the maps lie in the automorphism group of the binary tree, a 2-group of order 2^(2ⁿ−1)).
2. **The law of the factor search.** Digit-by-digit factor reconstruction keeps exactly the pairs (p, q) mod 10^(c+1) with p·q ≡ N. Their number is a closed form, a product over the primes 2 and 5: (v₂+1)(v₅+1)·4·10ᶜ when both valuations are below c+1, i.e. unit-group torsors, ×10 per column. The closed form (and its N ≡ 0 mod pᵏ case, k·φ(pᵏ) + pᵏ) was checked by enumeration for every N over p = 2, 3, 5, 7, 11.
3. **The address of the final answer.** For a unit solution mod 10ⁿ, K = (p′q′ − N)/10ⁿ is an integer and the true factorisation is exactly K = 0. It is unique among zero-overflow solutions and **not isolated**: near-misses with small |K| exist.
4. **Follow-up tests.** No tested guide (overflow, size bound, smallest p′) prefers the true child of a node in the solution tree before the last level; the exact bound p′q′ ≤ N prunes only at the last level.

**It is not a factoring method.** The live-state count is the cost of the search it describes.

## Files

| Path | What |
|---|---|
| `engine/e_addm_orbits.py` | Sections 1–5: matrix, rotors, law, address, partial knowledge (stdlib; `--crosscheck` against ValaQuenta's `addition_matrix`) |
| `engine/e_addm_followup.py` | Section 6: closed form for every prime power tested, tree automorphisms, solution-tree guide tests (`--crosscheck` against the Explorer's toolsets) |
| `paper/make_paper.py` | builds the paper from the engines (`--check`: does the committed paper match a fresh build?) |
| `paper/build_pdf.sh` | builds `AdditionMatrixOrbits.pdf` (pandoc + LuaLaTeX) |
| `references/README.md` | the literature, including the one work that could not be downloaded |

## Where else this lives

ValaQuenta engine `addition_matrix` (v1.0) and its notebooks; Multiplication Matrix Explorer (`toolsets/`, factor-mode law panel, `wiki/`); `TuringStack/wiki/Digit-by-Digit-Factor-Search-Law-2026-10-14.md` (the cryptographic reading, white-hat posture); `Ainulindale/wiki/125_…`.
