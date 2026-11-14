# InertiaEntropy — Inertia and Entropy: The Atomic Decomposition

<!-- correction-pass-2026-11-14 -->
> ## Status and corrections, 2026-11-14
>
> *Added by the correction pass; the text of the draft below is unchanged.*
>
> **Assistant note.** This pass was made by a transformer language model (Claude Sonnet 5.5, `claude-sonnet-5-5`) with the project's `cs-paper-code-conventions` skill and the Fourth Age Protocol loaded (`ContextPlease/claude/skills/`, `ContextPlease/FOURTH_AGE_PROTOCOL.md`). The author is Cody Michael Allison (pen name Michael Rendier), an autodidact, not an academic; his method is not to tell the model the result he is looking for. This is a **draft**: its claims are the author's, and the labels of the Ainulindalë overhaul (ESTABLISHED, OURS, THEORETICAL, OPEN, with `:CALCULATED` for results the paper's own code produced) apply to every statement in it.
>
> **State.** This directory has no notebooks.
>
> **Statements in this draft that the Ainulindalë overhaul retired, corrected or did not reproduce** (line numbers refer to this file before the block was added; each statement is kept as written):
>
> - (lines 21) A Noether-current / Noether-balance statement for the σ = ½ map. **Retired as a conserved-current statement**: s ↦ 1 − s is a discrete involution, so there is no continuous symmetry and no Noether current (Ainulindalë wiki 133 §3, ledger X-4). The J_red + J_blue = J_green balance stands as a measured relation of the sedenion grading. The statement is kept as written, because the maths started here.
> - (lines 37, 52) "Zero free parameters" is stated as a result. A parameter count is a claim about how a number was obtained; where a number was assigned and not computed it is not a result. Each such number needs its script (Fourth Age Protocol §1, §3).
> - (lines 75, 76, 77, 78) d* has four faces (0.24631 Boundary; the RG face, numeric open; Ω/ln 10; d*·ln 10 = Ω) and 0.24600 is a measured value that is not one of them (wiki 133 §2.2).
>
> **Authority.** Notation and verified counts: Ainulindalë `wiki/133_canonical_maths.md`; every defect found: `wiki/135_engine_findings_ledger.md`; the audit of this repository: `AUDIT_2026-11-14.md`.


**Paper Title:** Inertia and Entropy: The Atomic Decomposition  
**Author:** Cody Michael Allison  
**Theory captured:** 2026-06-08  
**Status:** Theory first-captured. Pre-registration pending.

---

## One-Sentence Summary

The nucleus is inertia (R̂_p); the electron orbitals are entropy (B̂_p); R̂†=B̂; chemistry is
the entropy field seeking the stable fixed points defined by the inertial anchors; and the
periodic table is the complete map of those fixed points, ordered by the strength of the anchor.

---

## Core Claim

Chemistry is not about atoms that build molecules. Chemistry is about **stability** — which
configurations are stable fixed points of the Noether current at σ=1.

```
Nucleus           = R̂_p  = Red channel  = Inertia = what IS
Electron orbitals = B̂_p  = Blue channel = Entropy = what CANNOT BE
R̂† = B̂  (exact adjoints — the atom is self-adjoint)
```

Every fact in chemistry follows from this decomposition.

---

## Paper Structure (planned)

```
00_holcus_vision.ipynb      — pre-registration: theory → predictions, commit first
01_predictions.ipynb        — 4 falsifiable predictions, zero free parameters
02_nist_reactivity.ipynb    — P1: entropy distance vs Pauling electronegativity (NIST)
02_nist_bonds.ipynb         — P2: bond energy vs orbital entropy change (NIST CCCBDB)
02_chembl_drugs.ipynb       — P3: drug affinity vs entropy complementarity (ChEMBL)
02_tcga_cancer.ipynb        — P4: cancer entropy signature in Complex I-IV (TCGA)
03_results.ipynb            — synthesis, comparison to existing models, paper draft
```

---

## Falsifiable Predictions

| # | Prediction | Dataset | Metric |
|---|---|---|---|
| P1 | Reactivity ~ entropy distance from noble gas config | NIST Atomic Spectra | Pearson r > 0.90 |
| P2 | Bond energy ∝ orbital entropy change at formation | NIST CCCBDB (1000+ molecules) | r > 0.85, zero free params |
| P3 | Drug affinity ~ orbital entropy complementarity | ChEMBL / BindingDB | Matches or beats docking score |
| P4 | Cancer separates from healthy in electron-chain entropy space | TCGA (33 cancer types) | Clustering accuracy > 80% |

**All predictions derived from H_hat_RB and SMMIP constants. Zero fitted parameters.**

---

## Key Consequences

**Noble gases:** Maximum entropy under Pauli constraint → no gradient → zero reactivity.  
**All bonds:** Entropy phenomena (covalent=shared, ionic=transferred, metallic=delocalized).  
**Reactions:** Entropy gradient descent toward fixed points. Catalyst = lower barrier, same endpoints.  
**ΔG = ΔH − TΔS:** IS the inertia-entropy balance (ΔH=R̂ term, TΔS=B̂ term).  
**Periodic table:** Map of inertial anchors (nuclear charge Z), showing entropy landscapes.  
**Orbital blocks:** CD hierarchy at σ=1: s(U(1)/ℂ), p(SU(2)/ℍ), d(SU(3)/𝕆), f(G₂/full 𝕆).  
**Drug design:** Entropy complementarity — target B̂ field ↔ drug R̂ field (not lock-key shape).  
**Cancer:** Deranged entropy minimum; drug built from the cancer's own algebraic signature.

---

## Connections

- **wiki/46_inertia_entropy_chemistry.md** — full theoretical capture
- **wiki/14_redblue_hamiltonian.md** — R̂†=B̂ adjoint structure
- **wiki/18_fermat_lattice.md** — Pauli Exclusion = Fermat constraint
- **wiki/22_constant_facets.md** — σ=1 chemistry facet; orbital blocks as CD hierarchy
- **D-CHEM** (Erika Schafer collaboration) — this paper IS the theoretical foundation of D-CHEM

---

## Collaboration

**D-CHEM parallel:** Erika Schafer (world-class chemist, super-oxide reductase synthesis).
P3 and P4 may be jointly developed with Erika Schafer.

---

## Pre-Registration Protocol

Per AddPapers protocol:
1. Run `00_holcus_vision.ipynb` with the premise above. **Commit before loading any data.**
2. Derive all predictions in `01_predictions.ipynb`. **Commit.**
3. Load real data in `02_*.ipynb` notebooks. Compare to predictions.
4. Synthesize in `03_results.ipynb`.

The commit hash on `00_holcus_vision.ipynb` and `01_predictions.ipynb` is the
pre-registration record. This is what makes the paper unfakeable.

---

## Appendix — what in ContextPlease was used, and what ContextPlease is

**ContextPlease** (`https://github.com/michaelrendier/ContextPlease`) is the *Manual Transmission Context Continuity* library: the versioned record that lets a new human or AI agent pick up a project without rediscovering it. Nothing in it is loaded automatically; whoever works chooses what to read. Used for this correction pass: the Fourth Age Protocol (`FOURTH_AGE_PROTOCOL.md`), the paper-writing conventions (`claude/skills/cs-paper-code-conventions/`) and the canonical notation (`claude/.clauderc_canonical_maths`).
