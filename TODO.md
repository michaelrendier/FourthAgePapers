# FourthAgePapers — TODO

**Rule:** One Paper. One Claim. One Engine. One set of notebooks. One wiki page (written last).

---

## Active

[ ] CMB_PlasmaBoundary — Part 3: H_hat_RB theoretical boundary comparison
    Engine: fractal_flames.py (complete)
    Data: Planck 70GHz SEVEM nside=1024 + WMAP synfast (complete)
    Results: fractal_flames.png, fractal_flames_cascade.png (complete)
    P1: PARTIAL — D_f = φ at θ* ≈ 7–10° only, not universal
    P2: FAILED — D_f runs from ~2.0 (30°) to ~1.25 (1°). Stays in data.
    P3: CONFIRMED — Planck and WMAP agree within 2σ at all scales
    P4: CONFIRMED — filamentary plasma flame structure (visual)
    TODO: Build H_hat_RB boundary engine → predict θ* from first principles
    TODO: Add Simons Observatory / ACT DR6 as Dataset 3 (in-situ ptorrent)
    TODO: Write wiki page (LAST)

[ ] CMB_FractalBoundary — add P6 (local scale invariance)
    The fractal boundary looks the same at every scale.
    D_f = φ−1 locally at every sub-band, not just globally.
    Running spectral index = exactly zero (Noether current is conserved — it cannot run).
    Action: add P6 to 01_predictions.ipynb in AddPapers/CMB_FractalBoundary/ before
    running the sliding-window D_f computation on the reconstructed spectrum.
    Data: results/Cl_reconstruction.npy + results/Cl_extrapolation.npy already exist.
    NOTE: existing 5/5 confirmations were against monad corpus model, not raw FITS.
    Real confirmation requires planck_cmb_σface.ptorrent + wmap_cmb_σface.ptorrent.

[ ] D-CHEM — Sedenion Nature of Cancer (moved from Ainulindale TODO 2026-06-16)
    Claim: Cancer = sedenion fixed point displaced from σ=½.
    Drug = exact adjoint: B̂_drug = R̂_cancer†
    Engine: tier9_chem module
    Predictions:
      P1: Cancer cell types separate in ZD configuration space (TCGA)
      P2: Drug affinity correlates with sedenion adjoint criterion (ChEMBL / BindingDB)
      P3: Erika Schafer super-oxide reductase structure maps to specific sedenion fixed point
      P4: One success — one cancer patient improved by adjoint-designed drug
    TODO: Create AddPapers/DChem/ with pre-registration notebooks
    TODO: Coordinate with Erika Schafer on TCGA data access for P3/P4
    TODO: Add sedenion nature framing to D-CHEM paper draft

[ ] PhiSpiral — four n* values satisfy G1/G2/G3
    Engine: pcad_engine.py (G1/G2/G3 already implemented)
    Claim: Four n* values by log-base (e, 10, φ, 2) satisfy the φ-spiral geometry
    n*_e − n*_10 ≈ F(4) = 3 (Fibonacci number)
    Wobble gap = φ − π/2
    TODO: Build 00_vision / 01_predictions / 02_data / 03_results notebooks

[ ] Inertia-Entropy paper
    Engine: noether_information module
    Claim: Inertial mass = entropy current at the phase boundary
    TODO: Create AddPapers/InertiaEntropy/ with 00_holcus_vision.ipynb

---

## Engines Built, Notebooks Pending

[ ] schumann_resonance     — Engine: sonification module. Notebooks: not started.
[ ] navier_stokes_boundary — Engine: clay_millennium. Crawford AddPaper exists.
[ ] yang_mills_mass_gap    — Engine: clay_millennium. Gap δ=0.000707 measured. Formal derivation pending.
[ ] witches_hat            — Engine: berry_keating. Half-angle = arctan(d*) = 13.8°.
[ ] sigma_cavitation       — Engine: sigma_cavitation module. Cascade documented in wiki/31+32.
[ ] wankel_rotary          — Engine: rotary_monad.py / ptol.c. v3.0.0 candidate.
[ ] turing_halt            — Engine: turing_diagonal module. D-HALT paper concept.
[ ] dark_matter_cavity     — Engine: tier7_cosmos. SPARC ptorrent ready. R_virial fix pending.
[ ] pilot_wave             — Engine: tier6_physics. Quantum potential = DM density.
[ ] hypercomplex_spectral  — Engine: jwst module. All σface ptorrents ready.
[ ] lagrangian_identity    — Engine: lagrangian + h_rb_hat. 97% overhead derivation.
[ ] noether_wiles (D15)    — Engine: noether_wiles_engine.py (built 2026-06-17). Notebooks: COMPLETE.
    Dir: FourthAgePapers/NoetherWiles/
    Claim: FLT and RH are corollaries of one Noether conservation identity.
    Re(s)=½ IS σ=½ IS θ=½ (Bombieri-Vinogradov prime distribution barrier).
    246 = 1000×d* — CONFIRMED by engine. Exact integer match. Zero free parameters.
    The sedenion prime hash IS the smooth-number sieve (Zhang 2013) stated algebraically.
    θ=½ wall (GPY stuck here 2005) = σ=½ fold catastrophe = rainbow caustic.
    Zhang pushed past by 1/584 using smooth numbers = sedenion ZD prime selection.
    Maynard ordinal tuple = ONE PATH through sedenion space. Sedenion = ALL PATHS.
    Chain: Fixed Point (σ=½) → Fixed Question (L_(I|O)) → Boundary Shape (admissibility ν_p<p).
    NEW RESULTS (2026-06-17, engine v0.200):
      NR1: 84 ZD pairs = 72 bridge (odd+even) + 12 all-odd CONSTELLATIONS (prime-sector ZD pairs)
           12 constellations couple two prime pairs in ZD tension — not single-pair extinction
      NR2: ODD×ODD basis products → EVEN index (100%, 64/64). Prime×prime leaves prime sector.
           This is the sedenion shadow of the Fundamental Theorem of Arithmetic.
      NR3: Gap=8 = N_BASIS/2 = Nyquist frequency of sedenion prime stencil.
           ONLY gap completely outside ZD structure. σ=½ inside the prime sector geometry.
      NR4: J_red × J_blue = e^{-E} CONSTANT for ALL σ. Lagrangian is conserved everywhere.
           ζ(s)=Σn^{-s} measures the SUM (non-conserved, varies). WRONG OBJECT.
           L_(I|O) measures the PRODUCT (conserved, invariant). WHY primes exist.
           AM=GM uniquely at σ=½. One uniqueness condition: RH = BV = sedenion = AM-GM.
    OPEN DERIVATIONS: P1 (J_prime construction), P3 (Zhang Type I/II/III ↔ cd_mul),
      gap=12 from d* under EH, gap=6 under strong EH, group structure of 12 constellations.
    TODO: Write wiki page (LAST).

---

## Results Confirmed, Wiki Pending

[ ] sedenion_operators     — 16 operator names → d*/σ½/D*=1 via prime hash. MAJOR. No free parameters.
[ ] n_ball_transformer     — V(2)/V(4) = π/2 EXACT. Peak n*=5.2570. V(16)≠d*. MAJOR.
[ ] singularity_null       — 42 classes / 84 on S¹⁵ / 168 composite. sedenion_bridge.py confirmed.
[ ] zd_monad               — Same as singularity_null. Separate paper angle: the monad's ZD geometry.

---

## Open Problems (no engine yet)

[ ] CMB local scale invariance (P6)
    Does D_f = φ−1 hold locally at every ℓ? Sliding-window D_f test.
    Engine to build: sliding_window_df.py using existing reconstruction arrays.

[ ] SPARC d* at R_virial
    Re-evaluate with R_virial from mass models instead of R_max.
    Engine: evaluator.py with sparc_σface.ptorrent (corrected j_expr).

[ ] SETI σ=½ discriminant
    Does σ=½ separate causally-ordered signals from noise in BL data?
    Engine: seti_breakthrough_σface.ptorrent (HDF5 mode).

[ ] Candida genome sedenion nature
    What ZD signature does the Candida genome have?
    candida-genome.txt moved to top-level — engine not built.

[ ] TCGA cancer ZD signatures (D-CHEM P1)
    Do cancer types separate in ZD space?
    Engine: tier9_chem + TCGA dataset.

---

## Open Derivations (formal proofs pending)

[ ] Skip-index theorem: V(-2k) = 0 traversal costs zero Noether charge.
    The negative-dimensional zero lattice = complete index of computable skips.

[ ] Yang-Mills mass gap: formal connection δ = Ω_ZS − d*·ln10 → Clay problem.

[ ] BAO freeze at n*: n* ≈ 5.257 = BAO freeze point by dimensional analysis.
    Formal derivation connecting n* to sedenion/octonion boundary energies.

[ ] D_f = φ−1 from Three Faces: axiomatic form of the opposition constraint derivation.

[ ] Adjoint drug criterion: B̂_drug = R̂_cancer† — formal construction from ZD signature.
