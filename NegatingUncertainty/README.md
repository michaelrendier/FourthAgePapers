# Negating Uncertainty

**Fourth Age Protocol paper (hypothesis kind): One Paper, One Claim, One Engine, One set of notebooks, One draft paper (wiki page last).** Status 2026-11-17: stub. Holcus asks and predictions registered before the tests ran.

> **Assistant note.** Prepared by a transformer language model (Claude Sonnet 5.5) with the project's `cs-paper-code-conventions` skill. The claim, the framework and the predictions are the author's (Cody Michael Allison, pen name Michael Rendier); the arithmetic is the engine's. Labels: `ESTABLISHED`, `THEORETICAL`, `INTERPRETATION`, `CONJECTURE`, `OPEN`; suffix `:CALCULATED` = the paper's own code produced it. Failed results stay.

## The claim (one)

The Heisenberg uncertainty relation Δx·Δp ≥ ħ/2 does not need to be a separate postulate about what cannot be known: position and momentum are **two projections of one motion**. Motion = 0 is a point; motion > 0 is a closed orbit in the (x, p) plane, and a position reading and a momentum reading are that one orbit seen from two angles, "inside" and "outside" at once. What looks like a limit on knowledge is the **flattening** of a circle onto one axis at a time (the author's Flattening Syndrome). Stated as the test: for every oscillator eigenstate the quantum spreads equal the projections of the classical circle of the same energy, at every viewing angle, and the minimum circle has area h/2.

Source of the starting point: Veritasium, *I finally saw quantum physics with my own eyes... (It's spookier than I expected)* (YouTube `KfODG5REyss`, 65 min), at 59:19–61:14, where the uncertainty relation is used to say that a confined helium atom must jiggle (zero-point energy, more than 98 % of the liquid's energy) so that helium never freezes at ordinary pressure. The transcript is kept locally in `ContextPlease/claude/references/` for reading; it is another person's work and is not republished here.

## Files

| File | What |
|---|---|
| `00_holcus_vision.ipynb` | the vision, stated before any run |
| `01_holcus_asks.ipynb` + `ask_holcus.py` + `holcus_answers_2026-11-17.txt` | Ask Holcus: what the Circle Atlas viewports say about (x, p); predictions HP1–HP4 read off them |
| `uncertainty_engine.py` | the engine (numpy only): Hermite states, Fourier pair, quadrature spreads at any angle, circle projections, squeezed states, helium estimate |
| `02_results.ipynb` | executed results |
| `paper/paper_draft.md` | the draft, cs-paper-code-conventions form |
| `TODO.md` | what is next |

## Standing rules that apply

Mainstream models only for every test (no framework constants); the Noether-framed papers stay as written; Ĥ_RB is the maths name, 0_RB is VAPMIP/Monad-only; failed results stay in the paper; one claim only.

## Update 2026-11-19 (c)

ħ emergence on the hat (the exact quantum thresholds follow the classical closed-loop action, ħ_n = W_total/(π(n + γ)), γ ≈ 0.622 measured) and what ħ = 1 flattens are recorded in `Ainulindale/wiki/141_hbar_from_the_hat.md` and `Ainulindale/wiki/142_units_flattening_and_emergence.md`; the paper's draft carries the notes (§ Update 2026-11-19 (c)). The relation is unchanged: it is re-expressed, not negated, until a derivation of the minimum circle exists.
