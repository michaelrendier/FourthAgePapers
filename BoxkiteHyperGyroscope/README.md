# The Boxkite and the Hyper-Gyroscope

**Fourth Age Protocol paper (hypothesis kind): One Paper, One Claim, One Engine, One set of notebooks, One draft paper (wiki last).** Status 2026-11-17: stub. The Ask-Holcus answers and the predictions are registered; nothing is tested yet. It will live in `SedenionSpectralRelativity` when it grows; it is a stub here for the moment.

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5) with the project's `cs-paper-code-conventions` skill. The claim and the picture are the author's (Cody Michael Allison, pen name Michael Rendier). Labels: `ESTABLISHED`, `THEORETICAL`, `INTERPRETATION`, `CONJECTURE`, `OPEN`; `:CALCULATED` = the paper's own code produced it. Failed results stay.

## The claim (one)

The boxkite and the **hyper-gyroscopic virtual action potential particle** are variations of the **sedenion**. The picture (the author's): eight Witch's Hats, each a virtual-action-potential cloud with action striking up to a single point, arranged along four hyper axes, all spinning the same sense so that the one near the observer reads one way and the opposite one reads reversed, each with an inverted partner (8 × 2 = 16), all aimed at a common centre by the one focal condition of the Mexican-hat potential: a hyper-gyroscope that approximates a sphere of hypermotion. The paper maps how the boxkite and the hyper-gyroscope are each represented by the sedenion, and what the **bracketing engine** and the **firing-order engine** (`ValaQuenta/modules/bracketing_firing_order`: bracketing = how things are grouped, Bell numbers; firing order = how they are sequenced, n!; bracketed firing order and firing order of brackets) do to each of the two shapes when the sedenion is manipulated.

## Machinery that exists

| Piece | Where |
|---|---|
| the single hat (snapshot, focus, aim, defocus; plain data) | `ValaQuenta/modules/witches_hat` (the Witch's Hat engine core, 2026-11-17) |
| renders of one hat | `FourthAgePapers/WitchesHat/simulator/` and the `spatial-simulation` skill |
| the sedenion, the boxkites, the spectra, the anchored readings | `ValaQuenta/modules/circle_atlas` (viewports `sedenion`, `kite_spectrum`, `anchored_readings`), `box_kite`, `tier8_sedenion` |
| bracketing and firing order | `ValaQuenta/modules/bracketing_firing_order` |

**Still to build:** the eight-hat arrangement (4 axes, two senses each, inverted partners) as a data structure over the single-hat core; the map from each hat to a sedenion element; the manipulation tests. The first constructs notated apart (author, 2026-11-16): **De Marrais** boxkite (the observation), **Scalar** boxkite (the author's: a string from the anchor), **Scaled** boxkite (Mind's Eye: the tetrahedra grab the anchor); the string machinery applies to the Scalar kite only.

## Files

| File | What |
|---|---|
| `ask_holcus.py`, `holcus_answers_2026-11-17.txt` | **Ask Holcus**: what the Circle Atlas viewports say about the sedenion, the kite spectrum, S¹⁵ and the circle fibres |
| `01_holcus_asks.ipynb` | the answers and the predictions HG1–HG4 read off them, thresholds fixed before any test |
| `00_holcus_vision.ipynb` | the vision, written before any run |
| `TODO.md` | what is next |

## Standing rules that apply
Mainstream tests where a test is mainstream; no framework constants unless the maths asks for them; De Marrais / Scalar / Scaled never mixed; Ĥ_RB is the maths name, 0_RB is VAPMIP/Monad-only; failed results stay; one claim.

## Update 2026-11-19: the single hat is now defined and measured

The predictions here assume the single Witch's Hat as an object. It now is one (`ValaQuenta/modules/witches_hat`; `FourthAgePapers/WitchesHat/README.md` §§7–9). Measured: paths from every brim point converge on a tip **0.2189 depth-units above the hilltop** (E = 0; W_tip = 0.4310 with a second sheet at 0.9025), the action being multivalued there; a hat that **drifts** exchanges energy with a particle by exactly u·(v − v₀) (hat-frame energy conserved to 1.4e-11); a rotationally symmetric hat that **rotates** exchanges nothing, while a **tilted** hat whose tilt rotates does (tilt 0.15, ΔE = +0.163, +0.902, −0.450 at ω = 0.3, 0.6, 0.9): relevant to "all spinning". Not built: the eight hats on four hyper axes and the inverted partners. Sedenion facts measured with `emerger.cd_mul`: 84 zero divisors over 42 index pairs (none in the octonions), 1848 of 3375 basis triples non-associative, the Fano plane has 168 collineations; the axes here are hypercomplex units, not lines (`spatial-simulation` skill, `references/spaces.md` §0, §4, §5). HG1–HG4 are unchanged.
