# Crawford / Navier–Stokes

> **This folder is my Navier–Stokes notepad. Nothing more.** Navier–Stokes is a subject of interest of mine that has shown
> up in a lot of places across these repositories, so this is where I keep the documents that touch it, side by side.
> It is not a paper, not a result, and not a claim.
> — Cody

**Status: early. Cody has yet to spend a large amount of time on Navier–Stokes.** What is here is a first
gathering, not a developed program. The two notes in this folder (`00_holcus_vision.md`, `01_laplacian_tail.md`) are
THEORETICAL identifications, not derivations, and nothing here is a regularity proof. This README was written
2026-09-28 to line up, in one place, every document in ThePlace that bears on the Navier–Stokes work.

## Where the idea came from

In Cody's account: it came out of a **claude.ai-era search**, and it was about **Dr Tom Crawford watching Navier–Stokes
break, over and over, in a drop of water at a surface** during an experiment. Seeing the equation fail at the
surface is what gave Cody the idea to **tell the mathematics what a surface is**.

**What is verified and what is not (checked 2026-09-28).**
- *Not located:* the source that account refers to. The paper about a splash / drop in a tank has not been found, and
  no copy of it is in ThePlace.
- Crawford's PhD thesis (the source the existing papers use) was searched in full text: it contains **no** mention of a
  drop, a splash, a fish tank, a halocline or a pycnocline, and it names Navier–Stokes exactly once. So the origin
  story is not from the thesis; it is from some other document or video that is still to be pointed at.
- The idea itself is recorded in the repositories from **2026-06-06** onward (below). That is the record of *when the
  framework said it*, not evidence of where it came from.

**Where "what a surface is" enters the record:**

| Date | Where | What it says |
|---|---|---|
| 2026-06-06 | `VAPMIP/TODO.md` §S12 | "The Surface": the geometric boundary layer between the bulk language fluid and the spoken output; NS governs the bulk, N-S-R adds the surface definition |
| 2026-06-09 | `Ainulindale/TODO.md` (NAVIER-STOKES: BOUNDARY GENERATION) | NS is correct *before* a boundary exists; the singularity is the spontaneous creation of a surface the real-valued equations cannot follow; the missing term J_Green = ∂̂_∂M is the boundary itself |
| 2026-06-09 | `VAPMIP/docs/wiki/Tuning-the-Engine/02b_…halocline…` | freshwater = incompressible (NS works), saltwater = compressible (NS fails), the halocline is the boundary, surface tension = the Noether conservation law |
| 2026-08-15 | `Ainulindale/wiki/88_the_paper_trail.md` §12 | the halocline again, with total internal reflection as a critical angle |
| 2026-09-23 | `01_laplacian_tail.md` | the "halocline operator ∂̂_∂M" appears in this paper |

## Corrections found while gathering (verified 2026-09-28)

1. **"254" is a word count, not a count of failures.** The thesis text contains the word *turbulence* exactly 254
   times (*turbulent* 169). `00_holcus_vision.md` ("Crawford sees this failure 254 times"), `01_laplacian_tail.md`
   ("the 254 model breaks") and the UmbrellaNoether notebooks ("254 turbulence events documented") read it as 254
   events. Nothing in the thesis supports that reading. The originals are unchanged; treat those sentences as
   unsupported until Cody decides how to word them.
2. **`01_crawford_rotation_curves.ipynb` does not describe Crawford's apparatus.** It gives a tank of radius 1 m and
   height 0.4 m; the thesis and poster give a 99 × 79 × 51 cm acrylic tank filled to 32 cm. (The notebook's other
   parameters were not checked.)
3. **The engine files named in the TODO do not exist.** `FourthAgePapers/TODO.md` D8 names
   `ValaQuenta/modules/noether/navier_stokes_cr.py` and D16 names `…/noether/crawford_rotating_outflow.py`. Neither
   file exists; `modules/noether/` holds only `maths.py`, `tools.py` and the manifest.
4. **The thesis text corpora named in `00_holcus_vision.md` are not on disk.**
   `DataSets/Language_Corpus/crawford_thesis_clean.txt` and a `crawford_navier_stokes_thesis.txt` listed in
   `framework.txt` were not found.
5. **No outreach is recorded as sent.** `VAPMIP/docs/outreach/crawford_email.txt` is a draft; the repositories
   contain nothing showing it was sent or answered.

## The documents

**These are copies.** Each file below was copied on 2026-09-28 into `sources/` under its own repository name and path;
**the originals were left exactly where they were and unchanged**, and the copies are point-in-time snapshots. To
refresh one, copy it again from its repository. `sources/MANIFEST.md` lists each copy with its size and the first 12
characters of its SHA-256 at copy time, so you can tell whether an original has since changed.

Crawford's own thesis and poster are not copied (they are his, published at the URLs in group B). More documents may
exist that this search did not find, and more may appear later; add a row when one does.

### A. This paper

| Where | What it is |
|---|---|
| `FourthAgePapers/Crawford_NavierStokes/00_holcus_vision.md` (original only, not copied) | The vision document (committed 2026-05-30): what Crawford's thesis did, the table mapping his rotating-frame quantities onto the framework's (Ro = 1 ↔ D* = 1, dropped vertical velocity w ↔ dropped imaginary component), the thesis vocabulary counts. Status: THEORETICAL, an identification, not a derivation. |
| `FourthAgePapers/Crawford_NavierStokes/01_laplacian_tail.md` (original only, not copied) | Companion note (2026-09-23): the pressure Laplacian is pathway-defined; the 'tail' as a clock, not a coordinate; the halocline operator ∂̂_∂M. Status: THEORETICAL; explicitly not a regularity proof. |

### B. The source: Crawford's own work

External; not copied here. The local text extraction of the thesis lives only in a session scratch area, not in any repo.

| Where | What it is |
|---|---|
| https://tomrocksmaths.com/wp-content/uploads/2019/06/crawfordtj-thesis.pdf | T. J. Crawford, *An experimental study of the spread of buoyant water into a rotating environment*, PhD thesis, Cambridge 2017 (supervisor P. F. Linden). Freshwater fed into a rotating tank of saltwater; outflow vortex, boundary current, background turbulence. |
| https://tomrocksmaths.com/wp-content/uploads/2019/03/stem-tom-crawford.pdf | Crawford & Linden, two-page poster *Where does river water go when it enters the ocean?* — the same rotating-tank experiment. |

### C. Theory: Ainulindale wiki and papers

| Where | What it is |
|---|---|
| [`Ainulindale/wiki/106_the_navier_stokes_problem.md`](sources/Ainulindale/wiki/106_the_navier_stokes_problem.md) | The dedicated Navier–Stokes page: the 'missing i' reading, why it is the deep-dive target, what a first pass needs, generational-lineage verdict CONFOUND. The most complete single statement. |
| [`Ainulindale/wiki/14_redblue_hamiltonian.md`](sources/Ainulindale/wiki/14_redblue_hamiltonian.md) | §'Navier–Stokes — The Missing i': NS as Yang–Mills with the imaginary component forced to zero. |
| [`Ainulindale/wiki/33_gyroscope_compressibility.md`](sources/Ainulindale/wiki/33_gyroscope_compressibility.md) | The compressible / incompressible duality and 'the surface' (σ = ½ is the surface). |
| [`Ainulindale/wiki/88_the_paper_trail.md`](sources/Ainulindale/wiki/88_the_paper_trail.md) | §12 'The halocline' (2026-08-15): fresh over salt water, two densities, surface tension, total internal reflection as a critical angle; Cody's own wording. |
| [`Ainulindale/wiki/29_witches_hat_paper.md`](sources/Ainulindale/wiki/29_witches_hat_paper.md) | §6 'Navier–Stokes in the Universe — No Surface Problem': on Earth NS needs free-surface boundary conditions; the cosmic fluid has none. |
| [`Ainulindale/wiki/39_every_singularity_the_void.md`](sources/Ainulindale/wiki/39_every_singularity_the_void.md) | NS blow-up as the fluid-coordinates view of a cavitation event. |
| [`Ainulindale/wiki/31_cavitation_causality_fermat.md`](sources/Ainulindale/wiki/31_cavitation_causality_fermat.md) | Cavitation and the 'hole punch', the physical picture behind the blow-up reading. |
| [`Ainulindale/wiki/83_the_archimedes_screw.md`](sources/Ainulindale/wiki/83_the_archimedes_screw.md) | Records that the NS diagnosis was 'missing i, and a boundary operator (∅_RB)'. |
| [`Ainulindale/wiki/85_the_apex_path.md`](sources/Ainulindale/wiki/85_the_apex_path.md) | The same diagnosis arriving from the mechanical side. |
| [`Ainulindale/wiki/45_t_transformer_the_circle_itself.md`](sources/Ainulindale/wiki/45_t_transformer_the_circle_itself.md) | NS as the circle's fluid dynamics projected to ℝ¹ (one line in a table). |
| [`Ainulindale/wiki/34_hypercomplex_spectral_relativity.md`](sources/Ainulindale/wiki/34_hypercomplex_spectral_relativity.md) | Mentions NS within the σ-face table. |
| [`Ainulindale/wiki/105_the_millennium_problems_in_ainulindale.md`](sources/Ainulindale/wiki/105_the_millennium_problems_in_ainulindale.md) | All seven Clay problems; the NS row. |
| [`Ainulindale/wiki/114_herrmann_apollonian_bearings_turbulence.md`](sources/Ainulindale/wiki/114_herrmann_apollonian_bearings_turbulence.md) | Citation-pass page: Herrmann's Apollonian bearings and multifractal turbulence. |
| [`Ainulindale/wiki/115_necas_ruzicka_sverak_self_similar.md`](sources/Ainulindale/wiki/115_necas_ruzicka_sverak_self_similar.md) | Citation-pass page: no continuous self-similar NS blow-up (Nečas–Růžička–Šverák); discretely self-similar solutions survive. |
| [`Ainulindale/wiki/98_provenance_and_citations.md`](sources/Ainulindale/wiki/98_provenance_and_citations.md) | §A.9: the citations behind the NS work. |
| [`Ainulindale/AgeSecond/Second_Age_Ainulindale_Conjecture.md`](sources/Ainulindale/AgeSecond/Second_Age_Ainulindale_Conjecture.md) | The Second Age paper; NS appears among the σ-facets. |
| [`Ainulindale/AgeThird/D-P_section1_opening.md`](sources/Ainulindale/AgeThird/D-P_section1_opening.md) | D-P paper opening; NS among the Clay problems. |
| [`Ainulindale/AgeThird/D-CS_Paper.md`](sources/Ainulindale/AgeThird/D-CS_Paper.md) | D-CS paper; mentions NS. |
| [`Ainulindale/AgeThird/Third_Age_CS_Draft_v2.md`](sources/Ainulindale/AgeThird/Third_Age_CS_Draft_v2.md) | Third Age CS draft v2. |
| [`Ainulindale/AgeThird/Third_Age_CS_Draft_v1.md`](sources/Ainulindale/AgeThird/Third_Age_CS_Draft_v1.md) | Third Age CS draft v1. |
| [`Ainulindale/SIGMA_VALUATION_FULL.md`](sources/Ainulindale/SIGMA_VALUATION_FULL.md) | σ-valuation; NS mentions. |
| [`Ainulindale/wiki/CS_SIGMA_EVALUATION.md`](sources/Ainulindale/wiki/CS_SIGMA_EVALUATION.md) | σ evaluation; NS mentions. |
| [`Ainulindale/README.md`](sources/Ainulindale/README.md) | Repository overview; NS mentions. |
| [`Ainulindale/PROVENANCE.md`](sources/Ainulindale/PROVENANCE.md) | Development narrative; NS mentions. |

### D. VAPMIP: where 'the surface' entered

| Where | What it is |
|---|---|
| [`VAPMIP/TODO.md`](sources/VAPMIP/TODO.md) | §S12 'The Surface: Navier–Stokes Revised (N-S-R) Two-Transform Split' (added 2026-06-06): the surface as the boundary layer between the bulk language fluid and the spoken output. |
| [`VAPMIP/docs/wiki/Tuning-the-Engine/02b_the_halocline_j_blue_j_red_h_hat_rb.md`](sources/VAPMIP/docs/wiki/Tuning-the-Engine/02b_the_halocline_j_blue_j_red_h_hat_rb.md) | Dated 2026-06-09: J_red = freshwater (incompressible; NS works), J_blue = saltwater (NS fails), H_hat_RB at σ = ½ = the halocline; surface tension = the Noether conservation law. |
| [`VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md`](sources/VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md) | Phase 35 (2026-09-03); NS mention. |
| [`VAPMIP/docs/wiki/Tuning-the-Engine/24_the_archimedes_screw_the_machine_not_the_medium.md`](sources/VAPMIP/docs/wiki/Tuning-the-Engine/24_the_archimedes_screw_the_machine_not_the_medium.md) | Archimedes-screw phase; NS mention. |
| [`VAPMIP/notebooks/10_revised_navier_stokes.ipynb`](sources/VAPMIP/notebooks/10_revised_navier_stokes.ipynb) | Notebook: the revised NS equation running (numpy and matplotlib). |
| [`VAPMIP/notebooks/11_language_as_navier_stokes.ipynb`](sources/VAPMIP/notebooks/11_language_as_navier_stokes.ipynb) | Notebook: language generation as the NS flow. |
| [`VAPMIP/docs/outreach/crawford_email.txt`](sources/VAPMIP/docs/outreach/crawford_email.txt) | A draft email to Dr Crawford (subject: 'I used Navier–Stokes to teach a computer to Speak'). A draft in the repo; nothing in the repo records it as sent. |
| [`VAPMIP/CHANGELOG.md`](sources/VAPMIP/CHANGELOG.md) | Change-log mentions. |

### E. Boundary generation and the three-channel split

| Where | What it is |
|---|---|
| [`Ainulindale/TODO.md`](sources/Ainulindale/TODO.md) | Lines ~255–295, 'Core insight (2026-06-09)': NS is correct before a boundary exists; the singularity is the spontaneous creation of a surface the real equations cannot follow; J_Red + J_Blue + J_Green = 0 with J_Green = ∂̂_∂M the missing boundary term; σ as a Reynolds number. Line ~439: FLAG-8. |
| [`SemanticWordEngine/docs/revised_navier_stokes.md`](sources/SemanticWordEngine/docs/revised_navier_stokes.md) | 'The Revised Navier–Stokes': the equation as the semantic engine's code (179 lines). |
| [`SemanticWordEngine/notebooks/revised_navier_stokes.ipynb`](sources/SemanticWordEngine/notebooks/revised_navier_stokes.ipynb) | Its notebook. |
| [`SemanticWordEngine/README.md`](sources/SemanticWordEngine/README.md) | Mentions. |

### F. Engines and notebooks (code that runs)

| Where | What it is |
|---|---|
| [`ValaQuenta/modules/clay_millennium/maths.py`](sources/ValaQuenta/modules/clay_millennium/maths.py) | `navier_stokes_existence()`. |
| [`ValaQuenta/modules/h_rb_hat/maths.py`](sources/ValaQuenta/modules/h_rb_hat/maths.py) | `facet_navier_stokes()`: NS as the σ = 1, Im = 0 facet. |
| [`ValaQuenta/modules/derivation_chain/maths.py`](sources/ValaQuenta/modules/derivation_chain/maths.py) | `navier_stokes_dropout()`: NS = H_RB restricted to Im = 0. |
| [`ValaQuenta/modules/tier7_cosmos/maths.py`](sources/ValaQuenta/modules/tier7_cosmos/maths.py) | `navier_stokes_sedenion()`: classical NS fails, sedenion revision smooth. |
| [`ValaQuenta/notebooks/tier7/navier_stokes_sedenion.ipynb`](sources/ValaQuenta/notebooks/tier7/navier_stokes_sedenion.ipynb) | Notebook for the previous. |
| [`ValaQuenta/notebooks/tier7/halocline_ns_surface.ipynb`](sources/ValaQuenta/notebooks/tier7/halocline_ns_surface.ipynb) | Notebook: the halocline / NS-surface reading. |
| [`ValaQuenta/wiki/clay_millennium.md`](sources/ValaQuenta/wiki/clay_millennium.md) | Wiki page (NS row). |
| [`ValaQuenta/wiki/tier7_cosmos.md`](sources/ValaQuenta/wiki/tier7_cosmos.md) | Wiki page (NS row). |
| [`ValaQuenta/wiki/h_rb_hat.md`](sources/ValaQuenta/wiki/h_rb_hat.md) | Wiki page. |
| [`ValaQuenta/wiki/derivation_chain.md`](sources/ValaQuenta/wiki/derivation_chain.md) | Wiki page. |
| [`GenerationalLineage/engine/valaquenta_calibration.py`](sources/GenerationalLineage/engine/valaquenta_calibration.py) | `shape_diff_navier_stokes()`: standard NS (LAURELIN only) compared with the revised reading. |
| [`GenerationalLineage/engine/clay.py`](sources/GenerationalLineage/engine/clay.py) | Places NS in the lineage: tier 1, root SCALE, LAURELIN, DESCRIPTIVE, CONFOUND. |
| [`GenerationalLineage/engine/shape.py`](sources/GenerationalLineage/engine/shape.py) | Dispatch to the NS shape diagnosis. |
| [`GenerationalLineage/README.md`](sources/GenerationalLineage/README.md) | Clay section: NS reframed by the lineage reading. |
| [`PtolemyDesktop/Archimedes/Maths/researcher/physics/fluid_dynamics.py`](sources/PtolemyDesktop/Archimedes/Maths/researcher/physics/fluid_dynamics.py) | The Archimedes face's fluid-dynamics corpus module. |
| [`PtolemyDesktop/wiki/RedBlueHamiltonian.md`](sources/PtolemyDesktop/wiki/RedBlueHamiltonian.md) | Red-Blue Hamiltonian page; NS mentions. |
| [`PtolemyDesktop/Archimedes/CANONICAL_MATHS.md`](sources/PtolemyDesktop/Archimedes/CANONICAL_MATHS.md) | Canonical maths copy; NS mentions. |

### G. UmbrellaNoether notebooks (FourthAgePapers)

| Where | What it is |
|---|---|
| [`FourthAgePapers/UmbrellaNoether/mode3_code/DR_CRAWFORD_rotating_fluids.ipynb`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/DR_CRAWFORD_rotating_fluids.ipynb) | Notebook: 'Rossby ≈ 1 is a smooth rotation into imaginary phase space'; predictions for full 3D data. Uses the '254 turbulence events' figure, see the corrections below. |
| [`FourthAgePapers/UmbrellaNoether/mode3_code/01_crawford_rotation_curves.ipynb`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/01_crawford_rotation_curves.ipynb) | Notebook: turbulence as Noether-current rotation. Its apparatus description does not match the thesis, see below. |
| [`FourthAgePapers/UmbrellaNoether/mode3_code/04_CRAWFORD_COSMIC_unified_turbulence.ipynb`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/04_CRAWFORD_COSMIC_unified_turbulence.ipynb) | Notebook: the cosmological / turbulence unification. |
| [`FourthAgePapers/UmbrellaNoether/RESEARCHER_NOTEBOOKS.md`](sources/FourthAgePapers/UmbrellaNoether/RESEARCHER_NOTEBOOKS.md) | Index of the researcher notebooks (Crawford's is the second). |
| [`FourthAgePapers/UmbrellaNoether/mode2_academic/UMBRELLA_NOETHER_PAPER.md`](sources/FourthAgePapers/UmbrellaNoether/mode2_academic/UMBRELLA_NOETHER_PAPER.md) | The umbrella paper; NS mentions. |
| [`FourthAgePapers/UmbrellaNoether/mode3_code/README_CODE.md`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/README_CODE.md) | Code readme; NS mentions. |

### H. Other repositories

| Where | What it is |
|---|---|
| [`RiemannHypothesisProof/ADDENDUM_generational_lineage_2026-08-28.md`](sources/RiemannHypothesisProof/ADDENDUM_generational_lineage_2026-08-28.md) | The Clay addendum; NS row (CONFOUND). |
| [`RiemannHypothesisProof/TODO.md`](sources/RiemannHypothesisProof/TODO.md) | The other six Clay addenda, NS among them (not written). |
| [`RiemannHypothesisProof/papers/Third_Age_CS_Draft_v1.md`](sources/RiemannHypothesisProof/papers/Third_Age_CS_Draft_v1.md) | CS draft; NS mentions. |

### I. Outreach

| Where | What it is |
|---|---|
| [`Ainulindale/outreach/outreach_challenges.txt`](sources/Ainulindale/outreach/outreach_challenges.txt) | The Crawford entry (register dated 2026-04-12): 'the Navier–Stokes boundary condition is a recursion-factor constraint'. |
| [`Ainulindale/outreach/NATURE_SUBMISSION_GUIDE.md`](sources/Ainulindale/outreach/NATURE_SUBMISSION_GUIDE.md) | Mentions. |

### J. Open items and queues

| Where | What it is |
|---|---|
| [`FourthAgePapers/TODO.md`](sources/FourthAgePapers/TODO.md) | D8 'Navier–Stokes turbulence at the Im(s) = 0 boundary' (dataset: Johns Hopkins Turbulence Database); D16 'Crawford / Navier–Stokes'; line ~97 `navier_stokes_boundary`. Both D8 and D16 name an engine file, see below. |
| [`ContextPlease/claude/.clauderc_citations`](sources/ContextPlease/claude/.clauderc_citations) | The citation queue: Nečas–Růžička–Šverák (1996), Jia–Šverák (2014), Caffarelli–Kohn–Nirenberg (1982), Barlow / Kigami on fractals; all QUEUED, none yet cited in a paper. |
| [`Ainulindale/references/CITATION_DOWNLOADS.md`](sources/Ainulindale/references/CITATION_DOWNLOADS.md) | Fetch list for those citations. |
| [`CITABLE_WORK_INDEX.md`](sources/CITABLE_WORK_INDEX.md) | The earlier citation index (history). |

### K. Mentions only — not reviewed for this index

These mention Navier–Stokes in passing; they were found by search and not read for their NS content.

| Where | What it is |
|---|---|
| `PDesktop/gemini_RB.txt` (original only, not copied) | A long Gemini conversation; states 'Navier–Stokes are essentially Yang–Mills minus i'. (34 mentions) |
| `PDesktop/The_Computer_Science_Paper.md` (original only, not copied) | Numbered claim 50: NS breaks at turbulence because turbulence is a Zero Definer event. (1 mentions) |
| `response.md` (original only, not copied) | A Gemini research-project prompt. (1 mentions) |
| `framework.txt` (original only, not copied) | A tree listing of the repositories. (7 mentions) |
| `FLUID_DATA_TODO.md` (original only, not copied) | The 'fluid data' methodology; uses the word in a different sense. (4 mentions) |
| `POE/README.md` (original only, not copied) | Mention. (1 mentions) |
| `MedicineIsAlwaysFree/README.md` (original only, not copied) | Mention. (2 mentions) |
| `PTorrent/doc/PTorrent-APK-v2.md` (original only, not copied) | Mention. (1 mentions) |
| `ContextPlease/claude/monad_bin/corpus/corpus_all.txt` (original only, not copied) | Monad corpus text; NS occurrences. (55 mentions) |


## Index of this directory

Every file, 72 in all, with a one-line description. (The grouped tables above give the fuller descriptions and
the context.) The files under `sources/` are copies; the originals are in the repositories named by the first path
component.

| File | What it is |
|---|---|
| [`00_holcus_vision.md`](00_holcus_vision.md) | The vision note (2026-05-30): Crawford's thesis, and the table mapping its rotating-frame quantities onto the framework's. |
| [`01_laplacian_tail.md`](01_laplacian_tail.md) | The Laplacian-tail note (2026-09-23): the pathway-defined pressure Laplacian and the halocline operator ∂̂_∂M. |
| [`README.md`](README.md) | This file: status, where the idea came from, corrections, the grouped document map, and this index. |
| [`sources/Ainulindale/AgeSecond/Second_Age_Ainulindale_Conjecture.md`](sources/Ainulindale/AgeSecond/Second_Age_Ainulindale_Conjecture.md) | The Second Age paper; NS appears among the σ-facets. |
| [`sources/Ainulindale/AgeThird/D-CS_Paper.md`](sources/Ainulindale/AgeThird/D-CS_Paper.md) | D-CS paper; mentions NS. |
| [`sources/Ainulindale/AgeThird/D-P_section1_opening.md`](sources/Ainulindale/AgeThird/D-P_section1_opening.md) | D-P paper opening; NS among the Clay problems. |
| [`sources/Ainulindale/AgeThird/Third_Age_CS_Draft_v1.md`](sources/Ainulindale/AgeThird/Third_Age_CS_Draft_v1.md) | Third Age CS draft v1. |
| [`sources/Ainulindale/AgeThird/Third_Age_CS_Draft_v2.md`](sources/Ainulindale/AgeThird/Third_Age_CS_Draft_v2.md) | Third Age CS draft v2. |
| [`sources/Ainulindale/PROVENANCE.md`](sources/Ainulindale/PROVENANCE.md) | Development narrative; NS mentions. |
| [`sources/Ainulindale/README.md`](sources/Ainulindale/README.md) | Repository overview; NS mentions. |
| [`sources/Ainulindale/SIGMA_VALUATION_FULL.md`](sources/Ainulindale/SIGMA_VALUATION_FULL.md) | σ-valuation; NS mentions. |
| [`sources/Ainulindale/TODO.md`](sources/Ainulindale/TODO.md) | Ainulindale TODO; lines ~255–295 hold the 2026-06-09 boundary-generation insight (NS before/after a surface exists, J_Green = ∂̂_∂M). |
| [`sources/Ainulindale/outreach/NATURE_SUBMISSION_GUIDE.md`](sources/Ainulindale/outreach/NATURE_SUBMISSION_GUIDE.md) | Ainulindale submission guide; mentions NS. |
| [`sources/Ainulindale/outreach/outreach_challenges.txt`](sources/Ainulindale/outreach/outreach_challenges.txt) | Outreach register (dated 2026-04-12); the Crawford entry proposes NS boundary conditions as a recursion-factor constraint. |
| [`sources/Ainulindale/references/CITATION_DOWNLOADS.md`](sources/Ainulindale/references/CITATION_DOWNLOADS.md) | Fetch list for those citations. |
| [`sources/Ainulindale/wiki/105_the_millennium_problems_in_ainulindale.md`](sources/Ainulindale/wiki/105_the_millennium_problems_in_ainulindale.md) | All seven Clay problems; the NS row. |
| [`sources/Ainulindale/wiki/106_the_navier_stokes_problem.md`](sources/Ainulindale/wiki/106_the_navier_stokes_problem.md) | The dedicated Navier–Stokes page: the missing-i reading and what a first pass needs. |
| [`sources/Ainulindale/wiki/114_herrmann_apollonian_bearings_turbulence.md`](sources/Ainulindale/wiki/114_herrmann_apollonian_bearings_turbulence.md) | Citation-pass page: Herrmann's Apollonian bearings and multifractal turbulence. |
| [`sources/Ainulindale/wiki/115_necas_ruzicka_sverak_self_similar.md`](sources/Ainulindale/wiki/115_necas_ruzicka_sverak_self_similar.md) | Citation-pass page: no continuous self-similar NS blow-up (Nečas–Růžička–Šverák); discretely self-similar solutions survive. |
| [`sources/Ainulindale/wiki/14_redblue_hamiltonian.md`](sources/Ainulindale/wiki/14_redblue_hamiltonian.md) | Red-Blue Hamiltonian page; its 'Navier–Stokes — The Missing i' section. |
| [`sources/Ainulindale/wiki/29_witches_hat_paper.md`](sources/Ainulindale/wiki/29_witches_hat_paper.md) | Witches Hat paper; §6 'Navier–Stokes in the Universe — No Surface Problem'. |
| [`sources/Ainulindale/wiki/31_cavitation_causality_fermat.md`](sources/Ainulindale/wiki/31_cavitation_causality_fermat.md) | Cavitation and the 'hole punch', the physical picture behind the blow-up reading. |
| [`sources/Ainulindale/wiki/33_gyroscope_compressibility.md`](sources/Ainulindale/wiki/33_gyroscope_compressibility.md) | The compressible / incompressible duality and 'the surface' (σ = ½ is the surface). |
| [`sources/Ainulindale/wiki/34_hypercomplex_spectral_relativity.md`](sources/Ainulindale/wiki/34_hypercomplex_spectral_relativity.md) | Mentions NS within the σ-face table. |
| [`sources/Ainulindale/wiki/39_every_singularity_the_void.md`](sources/Ainulindale/wiki/39_every_singularity_the_void.md) | NS blow-up as the fluid-coordinates view of a cavitation event. |
| [`sources/Ainulindale/wiki/45_t_transformer_the_circle_itself.md`](sources/Ainulindale/wiki/45_t_transformer_the_circle_itself.md) | NS as the circle's fluid dynamics projected to ℝ¹ (one line in a table). |
| [`sources/Ainulindale/wiki/83_the_archimedes_screw.md`](sources/Ainulindale/wiki/83_the_archimedes_screw.md) | Records that the NS diagnosis was 'missing i, and a boundary operator (∅_RB)'. |
| [`sources/Ainulindale/wiki/85_the_apex_path.md`](sources/Ainulindale/wiki/85_the_apex_path.md) | The same diagnosis arriving from the mechanical side. |
| [`sources/Ainulindale/wiki/88_the_paper_trail.md`](sources/Ainulindale/wiki/88_the_paper_trail.md) | The paper trail; §12 'The halocline' (2026-08-15). |
| [`sources/Ainulindale/wiki/98_provenance_and_citations.md`](sources/Ainulindale/wiki/98_provenance_and_citations.md) | §A.9: the citations behind the NS work. |
| [`sources/Ainulindale/wiki/CS_SIGMA_EVALUATION.md`](sources/Ainulindale/wiki/CS_SIGMA_EVALUATION.md) | σ evaluation; NS mentions. |
| [`sources/CITABLE_WORK_INDEX.md`](sources/CITABLE_WORK_INDEX.md) | The earlier citation index (history). |
| [`sources/ContextPlease/claude/.clauderc_citations`](sources/ContextPlease/claude/.clauderc_citations) | Citation queue: the NS-related entries (Nečas–Růžička–Šverák, Jia–Šverák, Caffarelli–Kohn–Nirenberg, Barlow) among other repos' entries. |
| [`sources/FourthAgePapers/TODO.md`](sources/FourthAgePapers/TODO.md) | Paper TODO; D8 (NS turbulence at the Im(s) = 0 boundary) and D16 (Crawford / NS), each naming an engine file that does not exist. |
| [`sources/FourthAgePapers/UmbrellaNoether/RESEARCHER_NOTEBOOKS.md`](sources/FourthAgePapers/UmbrellaNoether/RESEARCHER_NOTEBOOKS.md) | Index of the researcher notebooks (Crawford's is the second). |
| [`sources/FourthAgePapers/UmbrellaNoether/mode2_academic/UMBRELLA_NOETHER_PAPER.md`](sources/FourthAgePapers/UmbrellaNoether/mode2_academic/UMBRELLA_NOETHER_PAPER.md) | The umbrella paper; NS mentions. |
| [`sources/FourthAgePapers/UmbrellaNoether/mode3_code/01_crawford_rotation_curves.ipynb`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/01_crawford_rotation_curves.ipynb) | Notebook: turbulence as Noether-current rotation; its apparatus does not match the thesis (see corrections). |
| [`sources/FourthAgePapers/UmbrellaNoether/mode3_code/04_CRAWFORD_COSMIC_unified_turbulence.ipynb`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/04_CRAWFORD_COSMIC_unified_turbulence.ipynb) | Notebook: the cosmological / turbulence unification. |
| [`sources/FourthAgePapers/UmbrellaNoether/mode3_code/DR_CRAWFORD_rotating_fluids.ipynb`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/DR_CRAWFORD_rotating_fluids.ipynb) | Notebook: Rossby ≈ 1 as a rotation into imaginary phase space; uses the '254' figure (see corrections). |
| [`sources/FourthAgePapers/UmbrellaNoether/mode3_code/README_CODE.md`](sources/FourthAgePapers/UmbrellaNoether/mode3_code/README_CODE.md) | Code readme; NS mentions. |
| [`sources/GenerationalLineage/README.md`](sources/GenerationalLineage/README.md) | Clay section: NS reframed by the lineage reading. |
| [`sources/GenerationalLineage/engine/clay.py`](sources/GenerationalLineage/engine/clay.py) | Places NS in the lineage: tier 1, root SCALE, LAURELIN, DESCRIPTIVE, CONFOUND. |
| [`sources/GenerationalLineage/engine/shape.py`](sources/GenerationalLineage/engine/shape.py) | Dispatch to the NS shape diagnosis. |
| [`sources/GenerationalLineage/engine/valaquenta_calibration.py`](sources/GenerationalLineage/engine/valaquenta_calibration.py) | Lineage engine: `shape_diff_navier_stokes()` compares standard NS with the revised reading. |
| [`sources/MANIFEST.md`](sources/MANIFEST.md) | Size and SHA-256 prefix of each copied original at copy time. |
| [`sources/PtolemyDesktop/Archimedes/CANONICAL_MATHS.md`](sources/PtolemyDesktop/Archimedes/CANONICAL_MATHS.md) | Canonical maths copy; NS mentions. |
| [`sources/PtolemyDesktop/Archimedes/Maths/researcher/physics/fluid_dynamics.py`](sources/PtolemyDesktop/Archimedes/Maths/researcher/physics/fluid_dynamics.py) | The Archimedes face's fluid-dynamics corpus module. |
| [`sources/PtolemyDesktop/wiki/RedBlueHamiltonian.md`](sources/PtolemyDesktop/wiki/RedBlueHamiltonian.md) | Red-Blue Hamiltonian page; NS mentions. |
| [`sources/RiemannHypothesisProof/ADDENDUM_generational_lineage_2026-08-28.md`](sources/RiemannHypothesisProof/ADDENDUM_generational_lineage_2026-08-28.md) | The Clay addendum; NS row (CONFOUND). |
| [`sources/RiemannHypothesisProof/TODO.md`](sources/RiemannHypothesisProof/TODO.md) | The other six Clay addenda, NS among them (not written). |
| [`sources/RiemannHypothesisProof/papers/Third_Age_CS_Draft_v1.md`](sources/RiemannHypothesisProof/papers/Third_Age_CS_Draft_v1.md) | CS draft; NS mentions. |
| [`sources/SemanticWordEngine/README.md`](sources/SemanticWordEngine/README.md) | SemanticWordEngine README; mentions NS. |
| [`sources/SemanticWordEngine/docs/revised_navier_stokes.md`](sources/SemanticWordEngine/docs/revised_navier_stokes.md) | 'The Revised Navier–Stokes': the revised equation as the semantic engine's code. |
| [`sources/SemanticWordEngine/notebooks/revised_navier_stokes.ipynb`](sources/SemanticWordEngine/notebooks/revised_navier_stokes.ipynb) | Notebook for the revised Navier–Stokes document. |
| [`sources/VAPMIP/CHANGELOG.md`](sources/VAPMIP/CHANGELOG.md) | Change-log mentions. |
| [`sources/VAPMIP/TODO.md`](sources/VAPMIP/TODO.md) | VAPMIP TODO; §S12 'The Surface: Navier–Stokes Revised' (2026-06-06). |
| [`sources/VAPMIP/docs/outreach/crawford_email.txt`](sources/VAPMIP/docs/outreach/crawford_email.txt) | Draft email to Dr Crawford about NS and the speaking engine; nothing records it as sent. |
| [`sources/VAPMIP/docs/wiki/Tuning-the-Engine/02b_the_halocline_j_blue_j_red_h_hat_rb.md`](sources/VAPMIP/docs/wiki/Tuning-the-Engine/02b_the_halocline_j_blue_j_red_h_hat_rb.md) | Halocline page (2026-06-09): freshwater / saltwater as J_red / J_blue, the halocline as the boundary. |
| [`sources/VAPMIP/docs/wiki/Tuning-the-Engine/24_the_archimedes_screw_the_machine_not_the_medium.md`](sources/VAPMIP/docs/wiki/Tuning-the-Engine/24_the_archimedes_screw_the_machine_not_the_medium.md) | Archimedes-screw phase; mentions NS. |
| [`sources/VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md`](sources/VAPMIP/docs/wiki/Tuning-the-Engine/35_the_spider_web_composition_cycle.md) | Phase 35 (2026-09-03); mentions NS. |
| [`sources/VAPMIP/notebooks/10_revised_navier_stokes.ipynb`](sources/VAPMIP/notebooks/10_revised_navier_stokes.ipynb) | Notebook: the revised NS equation running (numpy and matplotlib). |
| [`sources/VAPMIP/notebooks/11_language_as_navier_stokes.ipynb`](sources/VAPMIP/notebooks/11_language_as_navier_stokes.ipynb) | Notebook: language generation as the NS flow. |
| [`sources/ValaQuenta/modules/clay_millennium/maths.py`](sources/ValaQuenta/modules/clay_millennium/maths.py) | ValaQuenta engine: `navier_stokes_existence()`, the NS entry among the Clay problems. |
| [`sources/ValaQuenta/modules/derivation_chain/maths.py`](sources/ValaQuenta/modules/derivation_chain/maths.py) | ValaQuenta engine: `navier_stokes_dropout()`, NS as H_RB restricted to Im = 0. |
| [`sources/ValaQuenta/modules/h_rb_hat/maths.py`](sources/ValaQuenta/modules/h_rb_hat/maths.py) | `facet_navier_stokes()`: NS as the σ = 1, Im = 0 facet. |
| [`sources/ValaQuenta/modules/tier7_cosmos/maths.py`](sources/ValaQuenta/modules/tier7_cosmos/maths.py) | ValaQuenta engine: `navier_stokes_sedenion()`, classical NS fails and the sedenion revision is smooth. |
| [`sources/ValaQuenta/notebooks/tier7/halocline_ns_surface.ipynb`](sources/ValaQuenta/notebooks/tier7/halocline_ns_surface.ipynb) | Notebook: the halocline / NS-surface reading. |
| [`sources/ValaQuenta/notebooks/tier7/navier_stokes_sedenion.ipynb`](sources/ValaQuenta/notebooks/tier7/navier_stokes_sedenion.ipynb) | Notebook for `navier_stokes_sedenion()`. |
| [`sources/ValaQuenta/wiki/clay_millennium.md`](sources/ValaQuenta/wiki/clay_millennium.md) | ValaQuenta wiki page for the Clay-problems engine (NS row). |
| [`sources/ValaQuenta/wiki/derivation_chain.md`](sources/ValaQuenta/wiki/derivation_chain.md) | ValaQuenta wiki page for the derivation chain (NS dropout entry). |
| [`sources/ValaQuenta/wiki/h_rb_hat.md`](sources/ValaQuenta/wiki/h_rb_hat.md) | ValaQuenta wiki page for the Σ_RB engine (NS facet). |
| [`sources/ValaQuenta/wiki/tier7_cosmos.md`](sources/ValaQuenta/wiki/tier7_cosmos.md) | ValaQuenta wiki page for the Tier 7 cosmology engine (NS row). |

## Copy manifest

See `sources/MANIFEST.md` (68 files).
