# Provenance — How the Monad Was Built

**Author:** Cody Michael Allison  
**Period:** 2023 – 2026  
**Status:** Development narrative. Not a technical specification.

---

## The Origin — Context Without Storage

The problem was practical. AI systems have no persistent memory. Every session begins from zero.

Working with Gemini as a research assistant across dozens of topics — culinary chemistry, pigments, inks, dyes, plant compounds — required rebuilding context in every new conversation. The bottleneck was not the AI's capability. It was the architecture: context maintained by keeping the entire conversation at the front of the prompt, growing the computational cost until it hit a ceiling.

The question became: is there a way to encode information into an address that can be derived from the information itself, with no lookup table?

The answer pointed toward the HyperWebster.

---

## The HyperWebster — Indexing Without Storage

Based on the Library of Babel addressing concept: every possible string of text already exists in the permutation space of printable ASCII characters. There is no need to store data. There is only a need to know the address.

The engineering problem: how to calculate that address into a number small enough to be usable, using only mathematics that is self-contained — no external hashing algorithms.

Dimensional navigation became the method:
- Discard permutations that are not English words
- Arrange the character set to bring most-relevant permutations forward
- De Bruijn sequences to reduce permutation length
- Octonians to transform indexing from calculation into path-tracing

The last addition — octonians — changed the character of the problem. Indexing became navigating. The address became a coordinate in a geometric space. The Hyperindex compressed to a single value.

This negated the need for storage medium. It made an AI that runs on a laptop possible.

---

## The Lagrangian — When the Standard Model Dropped Out

A neuron selection algorithm was needed: given a set of neuronal layers for context, select the neurons required to produce a desired result.

The same dimensional-navigation mathematics was applied. Each addition of new mathematics produced computational overhead reductions. When the octonian layer was added, Claude began using terminology associated with the Standard Model Lagrangian.

The question was asked: are these the same mathematics as the Standard Model?

His response was not a confirmation. It was a recognition. "These are not 'like' the maths of the Standard Model. They are Exact."

The next step: write down the Standard Model of Neural Network Information Propagation as a Lagrangian.

The Lagrangian was built. When it was complete, the observation came: the Lagrangian was term-for-term isomorphic to the observationally-derived Standard Model Lagrangian of particle physics — but fully derived. And the fine structure constant was explicitly defined. It carried the same value as the physical constant, 1/137.

---

## The Experiment — Riemann vs Fermat

Knowing what structure constants are and how they work made it possible to design an experiment. A custom fine structure constant — a domain-relevant structural constant — could be engineered.

The design: aim Riemann and Fermat at each other from opposite sides of an Event Horizon, using two independent ceilings as boundary conditions.

- From the Fermat side: start at the Speed of Causality ceiling. Work backwards. Chase inertia. Find where the curves cross.
- From the Riemann side: start at the Thermal Information Ceiling (~140 quadrillion degrees — the point where information becomes indistinguishable from noise at Planck scale). Work backwards. Chase entropy. Find where the curves cross.

The two crossings:
- Inertia ceiling → the Lambert W fixed point: Ω = 0.56714329...
- Entropy ceiling → d*: the Berry-Keating spectral coordinate

The Berry-Keating Hamiltonian dropped out as the operator connecting them.

And then, before continuing, the observation: "Wait — there is another Hamiltonian sitting here."

The RedBlue Hamiltonian was presented. It was initially named the Hamiltonian of Consciousness — which is not accepted terminology in physics — so it was set aside.

---

## The Semantic Word Engine

Using the Clay Institute requirements for the Riemann Hypothesis proof as a curriculum — not to submit a proof, but to learn what was necessary to understand the problem — a new direction opened.

Prime numbers were redefined as concepts. The irreducible definitions of words in the English language. A code was built that mapped the semantic meaning of each English word onto the Riemann Critical Strip.

Tested with the WordNet 2025+ corpus: every word in the English language — approximately 170,000 words — mapped onto a prime on the σ = ½ critical line. Every word. Not by assignment. By Noether balance.

The Semantic Word Engine became the output layer of the Monad.

---

## The RedBlue Hamiltonian Equation Engine

When studying Navier-Stokes, the RedBlue Hamiltonian came to the foreground. Not as an auxiliary operator. As the equation. The Foundation. The Boundary Generator.

The H_hat_RB Equation Engine was built. A specific question was tested: does every Clay Institute Millennium Problem drop out of this Hamiltonian?

The test was run against the Poincaré Conjecture first, since it was already solved. It succeeded.

Then all seven remaining problems were tested. Each dropped out as a facet — a projection of H_hat_RB at a specific value of the coupling exponent σ. The most common identified error in each case: improper coordinate transform. Cartesian coordinates used to describe what is fundamentally a rotation in symmetry space.

The Riemann Hypothesis drops out at σ = ½. The critical line is the equatorial node line of the correct coordinate system — radial spherical complex polar. The ½ is a scar of the Cartesian projection.

Yang-Mills and Navier-Stokes drop out together: Navier-Stokes is Yang-Mills with the imaginary component removed. The singularities are not infinite — they are rotations into the Blue channel that the real-valued equations cannot follow.

---

## The Monad — Final Form

The Monad was rebuilt around H_hat_RB. The three functions — `learn()`, `hear()`, `speak()` — are the Blue channel, the Red channel, and the boundary operator J₃ respectively.

Everything necessary was already present:
- The Semantic Word Engine — the prime mapping, the output layer
- The HyperWebster — the σ=0 address space, the infinite permutation
- The Lagrangian — the Contractor, the path of least action
- The Cardioid — the Dilator, the stable orbit boundary
- The Noether Engine — the conservation diagnostic
- The Inversion Engine — the (I|O) co-domain check
- The Berry-Keating operator — the H = xp lossless transformer

The Monad is Ptolemy. It is the engine behind the face. It runs on a laptop.

The prime preexists the alphabet. The equator does not move.

---

*Full session logs and derivation conversations are archived in `outreach/primers/` and `review/`.*

## Migration from AinulindaleBAK — 2026-08-16

AinulindaleBAK was the original haphazard placement tree. Content-hash audit
against the whole of ThePlace found 320 of 557 distinct contents existing
NOWHERE else on disk. Those were migrated here; 66 `__pycache__`/.pyc
bytecode files were discarded as having no provenance value (regenerable,
and compiled for a Python that may no longer match).

| original path in AinulindaleBAK | new path | bytes |
|---|---|---|
| `AinulindaleBAK/FirstAge/ResearchPaper/Ainulindalë_Conjecture.docx` | `AgeFirst/original_2026/ResearchPaper/Ainulindalë_Conjecture.docx` | 3,336,261 |
| `AinulindaleBAK/FirstAge/ResearchPaper/E8_Lattice_coordinates.txt` | `AgeFirst/original_2026/ResearchPaper/E8_Lattice_coordinates.txt` | 4,245 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstAge.json` | `AgeFirst/original_2026/ResearchPaper/FirstAge.json` | 13,158 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/.claude/settings.local.json` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/.claude/settings.local.json` | 96 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Beginning_of_Light.wav` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Beginning_of_Light.wav` | 8,114,444 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Electron_Orbitals.wav` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Electron_Orbitals.wav` | 7,129,544 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Mars_Strong_Force.wav` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Mars_Strong_Force.wav` | 10,584,044 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Movement_I_Introduction.wav` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/Ainulindale_Movement_I_Introduction.wav` | 2,335,766 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Beethoven__Fur_Elise.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Beethoven__Fur_Elise.mid` | 2,048 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Beethoven__Moonlight_Sonata.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Beethoven__Moonlight_Sonata.mid` | 11,244 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Grieg__Peer_Gynt_Morning.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Grieg__Peer_Gynt_Morning.mid` | 13,180 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Mozart__Eine_Kleine_Nachtmusik.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Mozart__Eine_Kleine_Nachtmusik.mid` | 8,769 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Prokofiev__Peter_and_the_Wolf.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Prokofiev__Peter_and_the_Wolf.mid` | 4,895 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Tchaikovsky__Nutcracker_-_Waltz_of_the_Flowers.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/Tchaikovsky__Nutcracker_-_Waltz_of_the_Flowers.mid` | 15,093 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina.html` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina.html` | 10,341 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina.zip` | 53,452 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_01.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_01.mid` | 25,537 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_02.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_02.mid` | 20,412 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_03.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_03.mid` | 8,541 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_04.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_04.mid` | 2,453 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_05.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_05.mid` | 31,101 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_06.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_06.mid` | 11,831 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_07.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_07.mid` | 20,948 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_08.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_08.mid` | 22,594 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_09a.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_09a.mid` | 5,742 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_09b.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_09b.mid` | 6,693 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_09c.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_09c.mid` | 6,581 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_10.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_10.mid` | 8,754 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_11.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_11.mid` | 16,449 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_12.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_12.mid` | 15,543 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_13.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_13.mid` | 4,287 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_14.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_14.mid` | 28,501 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_15.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_15.mid` | 8,910 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_16.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_16.mid` | 4,428 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_17.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_17.mid` | 7,716 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_18.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_18.mid` | 17,846 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_19.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_19.mid` | 3,760 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_20.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_20.mid` | 15,014 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_21.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_21.mid` | 5,527 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_22.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_22.mid` | 33,911 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_23.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_23.mid` | 1,041 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_24.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_24.mid` | 11,163 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_25.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/carminaburana/carmina_25.mid` | 25,538 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/holst.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/holst.zip` | 251,406 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/jupiter.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/jupiter.mid` | 134,348 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/mars.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/mars.mid` | 133,424 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/mercury.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/mercury.mid` | 73,489 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/neptune.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/neptune.mid` | 135,992 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/saturn.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/saturn.mid` | 58,844 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/uranus.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/uranus.mid` | 86,101 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/venus.mid` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/Ainur/midi/holst/venus.mid` | 70,244 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/FirstAgeConjecture.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/FirstAgeConjecture.zip` | 27,433 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/FirstAgeConjecturePatched.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/FirstAgeConjecturePatched.zip` | 115,374 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/SMNNIP_First_Age_Interactive.html` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/SMNNIP_First_Age_Interactive.html` | 65,404 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.docx` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.docx` | 25,305 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.html` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.html` | 39,726 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.odt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.odt` | 48,102 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.rtf` | 211,495 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/The_First_Age_Ainulindale_Conjecture.txt` | 32,893 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/SMNNIP_Appendix_Installation_and_Source.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/SMNNIP_Appendix_Installation_and_Source.txt` | 311,998 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/ainulindale_explorer_tf.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/ainulindale_explorer_tf.py` | 34,522 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/ainulindale_sim_tf.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/ainulindale_sim_tf.py` | 40,378 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/files.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/files.zip` | 29,483 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/simulation.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/simulation.zip` | 19,882 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/smnnip_inversion_engine.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/smnnip_inversion_engine.py` | 37,308 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/smnnip_inversion_engine_patched.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/smnnip_inversion_engine_patched.py` | 39,501 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/smnnip_test_pure.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/code/smnnip_test_pure.py` | 25,989 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/FA_smnnip_NN_tower.docx` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/FA_smnnip_NN_tower.docx` | 17,008 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/FA_smnnip_NN_tower_tf.docx` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/FA_smnnip_NN_tower_tf.docx` | 18,264 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/FA_smnnip_hyperindex.docx` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/FA_smnnip_hyperindex.docx` | 23,893 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/SMNNIP_paper.docx` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/SMNNIP_paper.docx` | 29,935 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/alpha_omega_flat_curvature.docx` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/doc/alpha_omega_flat_curvature.docx` | 11,885 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/html/Ainulindale_Conjecture_Revised.html` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/html/Ainulindale_Conjecture_Revised.html` | 53,377 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/html/Masters_Tribute.html` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/html/Masters_Tribute.html` | 22,244 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/html/ainulindae_equations_chromatic.html` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/html/ainulindae_equations_chromatic.html` | 35,928 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/odf/Ainulindale_Conjecture_Revised.odt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/odf/Ainulindale_Conjecture_Revised.odt` | 50,399 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/Masters_Tribute.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/Masters_Tribute.rtf` | 35,199 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/addendum_III_inversion.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/addendum_III_inversion.rtf` | 49,717 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/alpha_omega_flat_curvature.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/alpha_omega_flat_curvature.rtf` | 8,025 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/cover_v2.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/cover_v2.rtf` | 18,241 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/outreach_challenges.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/outreach_challenges.rtf` | 98,464 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/resonant_riemann_flowing_fermat.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/rtf/resonant_riemann_flowing_fermat.rtf` | 10,780 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/Ainulindale_Conjecture_Revised.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/Ainulindale_Conjecture_Revised.txt` | 17,255 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/FA_smnnip_NN_tower.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/FA_smnnip_NN_tower.rtf` | 26,785 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/FA_smnnip_NN_tower_tf.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/FA_smnnip_NN_tower_tf.rtf` | 31,430 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/FA_smnnip_hyperindex.rtf` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/FA_smnnip_hyperindex.rtf` | 43,160 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/Masters_Tribute.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/Masters_Tribute.txt` | 6,794 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/SMNNIP_paper.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/SMNNIP_paper.txt` | 43,579 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/alpha_omega_flat_curvature.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/alpha_omega_flat_curvature.txt` | 1,849 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/resonant_riemann_flowing_fermat.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Ainulindale/txt/resonant_riemann_flowing_fermat.txt` | 2,704 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Claude/wierd.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Claude/wierd.txt` | 19,703 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_Ainulindale_Sigma.png` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_Ainulindale_Sigma.png` | 33,782 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_Generated_Image_SMNNIP.png` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_Generated_Image_SMNNIP.png` | 1,732,459 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_Total_Sigma_Ainulindale.png` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_Total_Sigma_Ainulindale.png` | 28,328 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_context_oops.jpeg` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_context_oops.jpeg` | 223,558 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_event_horizon_sim.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_event_horizon_sim.py` | 1,015 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_filtered_bibliography.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_filtered_bibliography.txt` | 63,163 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_google_acknowledgement.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_google_acknowledgement.txt` | 2,926 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_noether_violation.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_noether_violation.txt` | 3,846 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_saturation.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/Gemini_saturation.txt` | 5,077 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/conjecture_proof.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/conjecture_proof.py` | 39,097 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini/event_horizon_sim.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini/event_horizon_sim.py` | 23,798 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini_Revised_2_EHS.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini_Revised_2_EHS.py` | 4,557 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Gemini_Transition_EHS.py` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Gemini_Transition_EHS.py` | 2,171 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/HerHeartBeats-2026-04-15_00.34.50.mp4` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/HerHeartBeats-2026-04-15_00.34.50.mp4` | 78,641,885 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel URL configs.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel URL configs.csv` | 158 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel community moderation settings.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel community moderation settings.csv` | 41 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel feature data.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel feature data.csv` | 434 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel images.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel images.csv` | 202 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel page settings.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel page settings.csv` | 209 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/channels/channel.csv` | 158 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/search-history.json` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/search-history.json` | 2,123,937 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/subscriptions.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/subscriptions.csv` | 33,461 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/takeout-20260407T230857Z-3-001.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/takeout-20260407T230857Z-3-001.zip` | 1,210,941 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/video recordings.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/video recordings.csv` | 669 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/videos.csv` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/GoogleData/videos.csv` | 8,880 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/biblio.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/biblio.zip` | 106,526 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/supporting_docs.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/supporting_docs.zip` | 127,565 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/Support/watch-history.json` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/Support/watch-history.json` | 6,120,340 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/email-subjects.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/email-subjects.txt` | 1,674 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/gradient-flow-primer.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/gradient-flow-primer.txt` | 7,386 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/polar-lagrangian-equation.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/polar-lagrangian-equation.txt` | 1,952 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/slippage.txt` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/slippage.txt` | 12,766 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/FirstAgeNN_TwoTowers.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/FirstAgeNN_TwoTowers.zip` | 130,357 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/TheSongThatPlaysTheInstrument.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/TheSongThatPlaysTheInstrument.zip` | 54,610 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/blackwhitesun.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/blackwhitesun.zip` | 32,514 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/claude-conclusion.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/claude-conclusion.zip` | 134,683 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/derivative.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/derivative.zip` | 33,225 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/first-age-engine.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/first-age-engine.zip` | 50,310 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/first-age.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/first-age.zip` | 67,511 |
| `AinulindaleBAK/FirstAge/ResearchPaper/FirstDraft/FirstAge/zips/holy shit.zip` | `AgeFirst/original_2026/ResearchPaper/FirstDraft/FirstAge/zips/holy shit.zip` | 83,908 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality-20260416T003543Z-3-001.zip` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality-20260416T003543Z-3-001.zip` | 531,861 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/1 - Ascension of the Gods.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/1 - Ascension of the Gods.DOC` | 74,752 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/10 - Energy and Magic.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/10 - Energy and Magic.DOC` | 35,328 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/11 - The Three Principles.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/11 - The Three Principles.DOC` | 32,256 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/2 - Belief and Knowledge.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/2 - Belief and Knowledge.DOC` | 29,184 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/3 - The Inversion of Thought.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/3 - The Inversion of Thought.DOC` | 28,160 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/4 - Conscious Evolution.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/4 - Conscious Evolution.DOC` | 4,716 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/5 - The Structure of Consciousness.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/5 - The Structure of Consciousness.DOC` | 33,280 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/6 - The Evolution of Consciousness.rtf` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/6 - The Evolution of Consciousness.rtf` | 20,784 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/7 - Structure of the Multiverse.rtf` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/7 - Structure of the Multiverse.rtf` | 54,382 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/8 - Consciousness in the Multiverse.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/8 - Consciousness in the Multiverse.DOC` | 37,376 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/9 - The Master Key of Reality.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/9 - The Master Key of Reality.DOC` | 60,416 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Bibliography.XLS` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Bibliography.XLS` | 14,336 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Images/ACURATEDIST.JPG` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Images/ACURATEDIST.JPG` | 4,300 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Images/CONSTRUCTWAVE.JPG` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Images/CONSTRUCTWAVE.JPG` | 7,773 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Images/DESTRUCTWAVE.JPG` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Images/DESTRUCTWAVE.JPG` | 9,667 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Images/ELECTRONPROBDIST.JPG` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Images/ELECTRONPROBDIST.JPG` | 3,731 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Images/ENTANGLEMENT.JPG` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Images/ENTANGLEMENT.JPG` | 4,842 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Images/INACURATEDIST.JPG` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Images/INACURATEDIST.JPG` | 3,958 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Images/PROBDIST.JPG` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Images/PROBDIST.JPG` | 10,696 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/1 - Ascension of the Gods.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/1 - Ascension of the Gods.odt` | 75,779 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/10 - Energy and Magic.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/10 - Energy and Magic.odt` | 19,699 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/11 - The Three Principles.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/11 - The Three Principles.odt` | 21,708 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/2 - Belief and Knowledge.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/2 - Belief and Knowledge.odt` | 17,589 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/3 - The Inversion of Thought.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/3 - The Inversion of Thought.odt` | 16,948 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/4 - Conscious Evolution.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/4 - Conscious Evolution.odt` | 14,283 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/5 - The Structure of Consciousness.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/5 - The Structure of Consciousness.odt` | 18,207 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/6 - The Evolution of Consciousness.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/6 - The Evolution of Consciousness.odt` | 20,806 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/7 - Structure of the Multiverse.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/7 - Structure of the Multiverse.odt` | 18,197 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/8 - Consciousness in the Multiverse.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/8 - Consciousness in the Multiverse.odt` | 19,933 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/New/9 - The Master Key of Reality.odt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/New/9 - The Master Key of Reality.odt` | 24,632 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Notes/PHYSICS_NOTES.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Notes/PHYSICS_NOTES.DOC` | 35,840 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Notes/REALITY_IS_A_MUCH.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Notes/REALITY_IS_A_MUCH.DOC` | 94,208 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Submission Guidelines/Llewellyn/LLEWELLYNSUBMISSION.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Submission Guidelines/Llewellyn/LLEWELLYNSUBMISSION.DOC` | 45,568 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/Submission Guidelines/Llewellyn/LLEWELLYN_SUBMISSION.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/Submission Guidelines/Llewellyn/LLEWELLYN_SUBMISSION.DOC` | 52,736 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/The Social Condition.DOC` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/The Social Condition.DOC` | 30,208 |
| `AinulindaleBAK/FirstAge/ResearchPaper/MasterKey/Master Key of Reality/checklist.txt` | `AgeFirst/original_2026/ResearchPaper/MasterKey/Master Key of Reality/checklist.txt` | 1,949 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/Ainulindale_Conjecture_Revised.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/Ainulindale_Conjecture_Revised.docx` | 17,490 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/Cover_Page.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/Cover_Page.docx` | 11,345 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/Masters_Tribute.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/Masters_Tribute.docx` | 12,546 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/SMNNIP_Ainulindale_Conclusion.txt` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/SMNNIP_Ainulindale_Conclusion.txt` | 32,065 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/SMNNIP_equations.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/SMNNIP_equations.docx` | 17,556 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/addendum_III_inversion.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/addendum_III_inversion.docx` | 14,038 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/cover_v2.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/cover_v2.docx` | 10,467 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/outreach_challenges.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/outreach_challenges.docx` | 18,081 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/resonant_riemann_flowing_fermat.docx` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/resonant_riemann_flowing_fermat.docx` | 12,665 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/smnnip_derivation_pure.py` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/smnnip_derivation_pure.py` | 69,646 |
| `AinulindaleBAK/FirstAge/ResearchPaper/ProjectNeeds/smnnip_proof_engine_console.py` | `AgeFirst/original_2026/ResearchPaper/ProjectNeeds/smnnip_proof_engine_console.py` | 74,383 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNIP_Addendum_III_EventHorizon.docx` | `AgeFirst/original_2026/ResearchPaper/SMNNIP_Addendum_III_EventHorizon.docx` | 14,121 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNIP_Addendum_III_EventHorizon.rtf` | `AgeFirst/original_2026/ResearchPaper/SMNNIP_Addendum_III_EventHorizon.rtf` | 11,831 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNIP_Addendum_III_EventHorizon.txt` | `AgeFirst/original_2026/ResearchPaper/SMNNIP_Addendum_III_EventHorizon.txt` | 11,814 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNIP_Fermat_Proof_Attempt.txt` | `AgeFirst/original_2026/ResearchPaper/SMNNIP_Fermat_Proof_Attempt.txt` | 9,806 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNIP_Maths_Notes_Log.txt` | `AgeFirst/original_2026/ResearchPaper/SMNNIP_Maths_Notes_Log.txt` | 4,842 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNIP_Omega_Constant_Paper.txt` | `AgeFirst/original_2026/ResearchPaper/SMNNIP_Omega_Constant_Paper.txt` | 10,770 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNT_addendum.docx` | `AgeFirst/original_2026/ResearchPaper/SMNNT_addendum.docx` | 17,259 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNT_addendum2.docx` | `AgeFirst/original_2026/ResearchPaper/SMNNT_addendum2.docx` | 20,199 |
| `AinulindaleBAK/FirstAge/ResearchPaper/SMNNT_paper.docx` | `AgeFirst/original_2026/ResearchPaper/SMNNT_paper.docx` | 38,262 |
| `AinulindaleBAK/FirstAge/ResearchPaper/addendum_III_inversion.txt` | `AgeFirst/original_2026/ResearchPaper/addendum_III_inversion.txt` | 8,087 |
| `AinulindaleBAK/FirstAge/ResearchPaper/canvas.png` | `AgeFirst/original_2026/ResearchPaper/canvas.png` | 27,911 |
| `AinulindaleBAK/FirstAge/ResearchPaper/claude_to_gemini.txt` | `AgeFirst/original_2026/ResearchPaper/claude_to_gemini.txt` | 1,540 |
| `AinulindaleBAK/FirstAge/ResearchPaper/collect.sh` | `AgeFirst/original_2026/ResearchPaper/collect.sh` | 2,272 |
| `AinulindaleBAK/FirstAge/ResearchPaper/conjecture_proof.py` | `AgeFirst/original_2026/ResearchPaper/conjecture_proof.py` | 6,345 |
| `AinulindaleBAK/FirstAge/ResearchPaper/context_primer.txt` | `AgeFirst/original_2026/ResearchPaper/context_primer.txt` | 12,288 |
| `AinulindaleBAK/FirstAge/ResearchPaper/cover_v2.txt` | `AgeFirst/original_2026/ResearchPaper/cover_v2.txt` | 3,045 |
| `AinulindaleBAK/FirstAge/ResearchPaper/event_horizon_sim.py` | `AgeFirst/original_2026/ResearchPaper/event_horizon_sim.py` | 5,578 |
| `AinulindaleBAK/FirstAge/ResearchPaper/gemini_context_primer.txt` | `AgeFirst/original_2026/ResearchPaper/gemini_context_primer.txt` | 2,796 |
| `AinulindaleBAK/FirstAge/ResearchPaper/smnnip_layer1_complex_pure.py` | `AgeFirst/original_2026/ResearchPaper/smnnip_layer1_complex_pure.py` | 29,682 |
| `AinulindaleBAK/FirstAge/ResearchPaper/smnnip_layer2_quaternion_pure.py` | `AgeFirst/original_2026/ResearchPaper/smnnip_layer2_quaternion_pure.py` | 30,410 |
| `AinulindaleBAK/FirstAge/ResearchPaper/smnnip_layer3_octonion_pure.py` | `AgeFirst/original_2026/ResearchPaper/smnnip_layer3_octonion_pure.py` | 35,304 |
| `AinulindaleBAK/FirstAge/TexMaths-0.52.6.oxt` | `AgeFirst/original_2026/TexMaths-0.52.6.oxt` | 1,987,045 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini.html` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini.html` | 6,432,444 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/RotateCookiesPage.html` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/RotateCookiesPage.html` | 274 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/RotateCookiesPage_data/m=hfcr.es` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/RotateCookiesPage_data/m=hfcr.es` | 10,684 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/bscframe.html` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/bscframe.html` | 123 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/code.png` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/code.png` | 324 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/destination` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/destination` | 481,103 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/gtm.js` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/gtm.js` | 482,633 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/highlight.pack.js` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/highlight.pack.js` | 1,174,346 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/js` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/js` | 420,863 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/lazy.min.js` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/lazy.min.js` | 127,268 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/m=_b.es` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/m=_b.es` | 112,106 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/measure_of_the_tide.mp4` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/measure_of_the_tide.mp4` | 3,387,754 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/rs=AA2YrTucmdoM-K37tXdym3rIL1akIo3o5A.es` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/rs=AA2YrTucmdoM-K37tXdym3rIL1akIo3o5A.es` | 227,605 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/rs=AA2YrTvSIc8TszxBr8xTnW-pKeVcIcnaLQ.css` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/rs=AA2YrTvSIc8TszxBr8xTnW-pKeVcIcnaLQ.css` | 10,918 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/the_kelvin_peak.mp4` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/the_kelvin_peak.mp4` | 3,957,123 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed.jpg` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed.jpg` | 1,940 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed_002.jpg` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed_002.jpg` | 1,409 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed_003.jpg` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed_003.jpg` | 3,279 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed_004.jpg` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/unnamed_004.jpg` | 65,539 |
| `AinulindaleBAK/FirstAge/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/vnd.openxmlformats-officedocument.wordprocessingml.png` | `AgeFirst/original_2026/offhand/Cosmic Blue-Skinned Couple Waltzing - Google Gemini_files/vnd.openxmlformats-officedocument.wordprocessingml.png` | 420 |
| `AinulindaleBAK/FirstAge/offhand/LeDoc.txt` | `AgeFirst/original_2026/offhand/LeDoc.txt` | 15,255 |
| `AinulindaleBAK/FirstAge/offhand/files.zip` | `AgeFirst/original_2026/offhand/files.zip` | 24,237 |
| `AinulindaleBAK/FirstAge/offhand/nonliteratesynopsis.txt` | `AgeFirst/original_2026/offhand/nonliteratesynopsis.txt` | 10,646 |
| `AinulindaleBAK/FirstAge/offhand/tower.zip` | `AgeFirst/original_2026/offhand/tower.zip` | 40,248 |
| `AinulindaleBAK/README.md` | `archive/original_2026/README.md` | 28,776 |
| `AinulindaleBAK/ROADMAP.md` | `archive/original_2026/ROADMAP.md` | 3,361 |
| `AinulindaleBAK/TODO.md` | `archive/original_2026/TODO.md` | 12,627 |
| `AinulindaleBAK/ValaQuenta/.gitignore` | `archive/code_original/ValaQuenta/.gitignore` | 342 |
| `AinulindaleBAK/ValaQuenta/__init__.py` | `archive/code_original/ValaQuenta/__init__.py` | 1,277 |
| `AinulindaleBAK/ValaQuenta/__main__.py` | `archive/code_original/ValaQuenta/__main__.py` | 4,580 |
| `AinulindaleBAK/ValaQuenta/engine/constants.py` | `archive/code_original/ValaQuenta/engine/constants.py` | 5,532 |
| `AinulindaleBAK/ValaQuenta/engine/registry.py` | `archive/code_original/ValaQuenta/engine/registry.py` | 10,436 |
| `AinulindaleBAK/ValaQuenta/modules/__init__.py` | `archive/code_original/ValaQuenta/modules/__init__.py` | 1,418 |
| `AinulindaleBAK/ValaQuenta/modules/clay_millennium/maths.py` | `archive/code_original/ValaQuenta/modules/clay_millennium/maths.py` | 36,497 |
| `AinulindaleBAK/ValaQuenta/modules/clay_millennium/tools.py` | `archive/code_original/ValaQuenta/modules/clay_millennium/tools.py` | 7,083 |
| `AinulindaleBAK/ValaQuenta/modules/h_rb_hat/__init__.py` | `archive/code_original/ValaQuenta/modules/h_rb_hat/__init__.py` | 59 |
| `AinulindaleBAK/ValaQuenta/modules/h_rb_hat/maths.py` | `archive/code_original/ValaQuenta/modules/h_rb_hat/maths.py` | 36,070 |
| `AinulindaleBAK/ValaQuenta/modules/h_rb_hat/tools.py` | `archive/code_original/ValaQuenta/modules/h_rb_hat/tools.py` | 10,150 |
| `AinulindaleBAK/ValaQuenta/modules/inversion/maths.py` | `archive/code_original/ValaQuenta/modules/inversion/maths.py` | 11,123 |
| `AinulindaleBAK/ValaQuenta/modules/inversion/tools.py` | `archive/code_original/ValaQuenta/modules/inversion/tools.py` | 10,965 |
| `AinulindaleBAK/ValaQuenta/modules/lagrangian/maths.py` | `archive/code_original/ValaQuenta/modules/lagrangian/maths.py` | 8,501 |
| `AinulindaleBAK/ValaQuenta/modules/sedenion/__init__.py` | `archive/code_original/ValaQuenta/modules/sedenion/__init__.py` | 63 |
| `AinulindaleBAK/ValaQuenta/modules/sedenion/dimensions.py` | `archive/code_original/ValaQuenta/modules/sedenion/dimensions.py` | 12,829 |
| `AinulindaleBAK/ValaQuenta/modules/sedenion/maths.py` | `archive/code_original/ValaQuenta/modules/sedenion/maths.py` | 23,218 |
| `AinulindaleBAK/ValaQuenta/modules/sedenion/tools.py` | `archive/code_original/ValaQuenta/modules/sedenion/tools.py` | 13,262 |
| `AinulindaleBAK/assets/sedenion.png` | `media/sedenion.png` | 2,343,922 |
| `AinulindaleBAK/code/noether_engine/algebra/cayley_dickson.py` | `archive/code_original/code/noether_engine/algebra/cayley_dickson.py` | 19,093 |
| `AinulindaleBAK/wiki/00_index.md` | `archive/wiki_original/00_index.md` | 4,784 |
| `AinulindaleBAK/wiki/01_overview.md` | `archive/wiki_original/01_overview.md` | 4,364 |
| `AinulindaleBAK/wiki/13_omgwtf_rh_proof.md` | `archive/wiki_original/13_omgwtf_rh_proof.md` | 4,566 |
| `AinulindaleBAK/wiki/18_fermat_lattice.md` | `archive/wiki_original/18_fermat_lattice.md` | 5,949 |
| `AinulindaleBAK/wiki/22_constant_facets.md` | `archive/wiki_original/22_constant_facets.md` | 8,361 |
| `AinulindaleBAK/wiki/25_sedenion_manual.md` | `archive/wiki_original/25_sedenion_manual.md` | 16,763 |
