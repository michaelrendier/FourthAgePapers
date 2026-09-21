# windspeed_reconstruction — the §9 investigation, in order

Moved here from session scratch work, 2026-09-20, because `draft_section_09.md`
and `draft_section_10.md` cite these results directly — they needed a
permanent home, not `/tmp`. Run in this numbered order; each script is
what it says, including the one that's flawed.

1. **`01_windspeed_recovery.py`** — the exact recovery:
   `(full_addr, delta, spelling) → context_code → gamma_radial`. §9.1.
2. **`02_edge_deformation_toy.py`** — first deformation attempt, the toy
   6-vertex box-kite graph Laplacian. Superseded by 05 (wrong coordinate
   frame — kept for the record, see §9.3).
3. **`03_labeled_spectrum.py`** — eigenvector labeling (`strut`/`sail`) on
   the same toy graph, before the frame correction.
4. **`04_maxwell_counting_ruled_out.py`** — proves the literal "3 struts as
   Cartesian 3D bars" reading of `pencil_hyperstring.md`'s acceptance test 1
   is mathematically impossible (`dim(flex)=9`, exact), not merely unverified.
5. **`05_native_deformation.py`** — the corrected version: real `L_a`
   (16×16), native rotation within a zero divisor's own null-space partner.
   `{4:8:4}` block structure exact and invariant within that plane; breaks
   immediately outside it. §9.3.
6. **`06_real_word_pencil.py`** — real word ("resentment") → `monad3_c.bin`
   → real strut → real pencil → null-space overlap check (partial, honest
   about the SVD-basis caveat).
7. **`07_unflattened_continuous_H.py`** — the aperture correction: bare
   basis-vector generators are provably quantized (256/256 basis products
   are exactly `±1×`another basis vector); continuous generators give
   smooth `Re(Π) = −cos(φ)`, and reveal the conservation law along the
   pencil-ordered rate. §9.3–§9.4.
8. **`08_rate_conservation_all_struts.py`** — the conservation law, all 7
   struts: exact on `{1,3,6}`, drifts on `{2,4,5,7}`. §9.4.
9. **`09_rate_conservation_maxgen_check.py`** — the aperture check on that
   result: same `{1,3,6}` split survives swapping which pair-endpoint is
   generator "first." Confirms it's a fact about the strut, not the
   convention.
10. **`10_pencil_structure_diagnostic.py`** — looked for a combinatorial
    reason `{1,3,6}` conserves (Fano-line membership, generator-set
    overlap). No clean answer found; documents what was ruled out.
11. **`11_order_sensitivity_FLAWED_see_readme.py`** — **a real methodology
    mistake, kept rather than deleted.** Meant to test order-sensitivity of
    the pencil's pairing structure; actually tested bare single-index
    products (dropped the `(a,b)` pair's second element entirely), so its
    "50/50 random split" result answers a different, uninformative
    question. The real order-sensitivity question — does conservation
    depend on the `(a,b)` pairing, not just the index sequence — is still
    open. Left in the appendix exactly because the mistake is instructive
    and because silently deleting a wrong turn breaks the project's own
    "RTFM" discipline.

## What's still open, honestly

Why exactly `{1,3,6}` conserves and `{2,4,5,7}` doesn't is unresolved.
Script 10 rules out the obvious candidate; script 11 is a false start at
the real test, not an answer. See `draft_section_11.md`.
