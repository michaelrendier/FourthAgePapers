# Equation Space

**Fourth Age Protocol paper (hypothesis kind): One Paper, One Claim, One Engine, One set of notebooks, One draft paper (wiki last).** Status 2026-11-19: **stub**. The author's definition is recorded, the existing machinery is listed, a few counts are measured; no claim is registered, no prediction is written, nothing is tested. The introduction is not drafted (discuss first).

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5, `claude-sonnet-5-5`) with the project's `cs-paper-code-conventions` skill. The definition is the author's (Cody Michael Allison, pen name Michael Rendier). Labels: `ESTABLISHED`, `THEORETICAL`, `INTERPRETATION`, `CONJECTURE`, `OPEN`; `:CALCULATED` = the paper's own code produced it. Predictions are asked of the maths (Ask Holcus), not written by the assistant. Failed results stay.

## The definition (the author's, 2026-11-19)

Equation space is the permutation space of all the equations that can be made from 0_RB. Axes are not lines but hypercomplex fields (the operator slots are algebra elements). It was "explored a bit somewhere in the documentation". Where it was found:

| Record | What it says |
|---|---|
| `Ainulindale/wiki/19_cayley_dickson_tower.md` §5 (σ = 0) | at σ = 0, p⁰ = 1 for every prime, no prime is distinguished: every division is valid and none is unique; σ above 0 lets the Noether information current select. The HyperWebster in total form lives at σ = 0 |
| `GenerationalLineage/wiki/Equation-Space.md`, `engine/toolsets/equation_space.py` | EXPERIMENTAL toolset: steering through a family of equations by the gradient of a collapse function ρ(s) (Smith's Γ distance to a ray); fold-caustic classification; found the circle (centre i, radius √2) by descent, independently of the sedenion construction |
| `SedenionSpectralRelativity/equation_space_engine.py` | the sedenion-side companion |
| `FLUID_DATA_TODO.md` | "the algorithm lives in equation space, not on the server"; "not a Hamiltonian that lives in equation space, it IS equation space" (the author's own phrasing; not interpreted here) |
| `ValaQuenta/modules/emerger`, `bracketing_firing_order` | the explored finite piece: bracketings and firing orders over the 15 imaginary units; the 10 {1,3,7}-shapes of 15 |
| `~/.claude/skills/spatial-simulation/references/spaces.md` §8 | the skill's record + stub (points, axes, motions; views not yet defined) |

## What is measured now (`ESTABLISHED:CALCULATED`, 2026-11-19; script in the ContextPlease scratchpad of that date)

A "point" in the finite piece is a word (an ordered list of units) in a full bracketing. Counts: bracketings of n factors = Catalan(n − 1) = 1, 2, 5, 14, 42, 132, 429 for n = 2…8; words with a firing order = n! · Catalan(n − 1): 120 at n = 4, 665,280 at n = 7, 2.03×10²⁰ at n = 16. Random words of 4 or 5 units in the octonions and the sedenions give, over all their bracketings, **1.8–1.95 distinct nonzero values on average (1 would be associative)**, and no zero product in 300 random draws of either algebra: equation space is already branching at the octonions, and zero divisors are not found by sampling words at random. The deformation-battery and the 132-bracketing law (§13 of the Scalar paper) are the structured version of this count.

## The first questions (not claims)

1. **What are the points?** Words over the 0_RB operators in a bracketing and an order, or equivalence classes of them (under the associator, under the box-kite symmetry)? The Emerger's partitions are classes; the full space is not defined.
2. **What is the view?** Candidates: the lattice of bracketings per word; word-length strata; the lineage chromosome of a word (GenerationalLineage); the σ-line from σ = 0 (every equation valid) upward (Noether selects).
3. **What does steering mean?** The toolset steers by a collapse function ρ; whether the right ρ for 0_RB equations exists is `OPEN`, and the toolset is marked EXPERIMENTAL by the author.
4. **Relation to the other spaces** of the skill: gauge space (Smith charts), the sedenion space with bracketing, the hat (Higgs field space). The hat's stationary paths and the brim's sheets are a *computed* object; equation space is the space of what could be computed.

## Machinery that exists / still to build

Exists: the toolset and sedenion companion above; `emerger`; `bracketing_firing_order`; GenerationalLineage factoring and firing plans. **Still to build:** a definition of a point and a distance; a view; the σ = 0 → σ > 0 selection as an experiment; the register of predictions asked of Holcus.

## Files

| File | What |
|---|---|
| `README.md` | this stub |
| `TODO.md` | what is next |

## Standing rules that apply
Mainstream tests where a test is mainstream; no framework constants unless the maths asks for them; De Marrais / Scalar / Scaled never mixed; Ĥ_RB is the maths name, 0_RB is VAPMIP/Monad-only; failed results stay; one claim; introduction not drafted before discussion.
