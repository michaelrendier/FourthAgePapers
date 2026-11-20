# 12 — Results of 11 (pair census, circle entry/exit, the 8–15 half)

Run 2026-11-20. Scripts `census.py`, `circles.py`; output `results_census_circles_2026-11-20.txt`; per-equation table `catalog/circles_ufm.csv` (one row per fractal formula: init end, loop end, circle number, bailout end, first letters, SIGN in bailout, loop touches 8–15 with F = 8). Predictions in `11_registered_census_circles.md`.

| # | prediction | result | verdict |
|---|---|---|---|
| P1 | AS, AG, SG each present ≥ 70 % | AS 98.1 %, AG 82.6 %, SG 82.5 % (of 3,461) | PASS |
| P2 | SG never order-sensitive | 0 of 2,854 | PASS |
| P3 | AS order-sensitive ≥ 90 %; AG ≥ 85 % | AS 94.8 %; **AG 42.0 %** | AS PASS, **AG FAILED** |
| P4 | all three letters ≥ 60 % | 81.8 % (2,831) | PASS |
| C1 | closed loop words 3–12 % | 288 of 3,415 = 8.4 % | PASS |
| C2 | returns to index 0 at even length 100 %; returns to (+1,e0) ≥ 90 % at multiples of 4 | even 36,317 of 36,317; **only 54.6 % (9,485 of 17,376) at multiples of 4** | first PASS, **second FAILED** |
| C3 | ADD ≤ 20 % first, ≥ 35 % last | first 14.8 %, last 43.4 % | PASS |
| C4 | circle number 4 for ≥ 75 % | 2,823 of 3,415 = 82.7 % (number 2: 304, number 1: 288) | PASS |
| C5 | SIGN in every bailout | 5,922 of 5,922 | PASS |
| H1 | F=8 words ending in 8–15: 35–65 % | 1,303 of 2,317 = 56.2 % | PASS |
| H2 | same membership for F = 8 and 15 | identical; full address identical for 1,014 of 2,317 (43.8 %) | PASS |
| H3 | upper half entered in first 5 letters ≥ 50 % | 76.0 % | PASS |

## Reading
- **Pair census.** 2,831 of 3,461 words (81.8 %) hold all three pair types; the signatures are only 5: all three (2,831), AS alone (563), AG alone (28), SG alone (23), none (16, the single-letter words). AS, the non-conjugate SCALE–ADD pair, is nearly universal (98.1 %), and where it occurs it is order-sensitive 94.8 % of the time. SG, SCALE–SIGN, never matters for order. The AG failure (42 % order-sensitive) means that ADD and SIGN together mostly do NOT make a word order-dependent on their own: I predicted anticommutation would show in most words. I have not chased why (candidate: the reversed AG subword often equals the original because signed translation counts depend on the parity pattern; not verified). The canonical pairs (x,p) and (ln x, θ) are not detectable from words and are not counted: the census measures the generator pairs only.
- **Circles.** Every fractal formula has an entry (init), a loop element and an exit (bailout); the loop element has order 4 for 82.7 % of loop words (a quarter turn per pass, four passes to close), 2 for 8.9 %, 1 for 8.4 % (closes in a pass). Entry letters are mostly SIGN/SCALE (43/42 %), exit letters mostly ADD (43 %): loops enter by flipping or scaling and leave by translating, as z² + c does. C2: a return to index 0 always has even length (parity), but returns to the identity with sign + are at multiples of 4 only 54.6 % of the time; my mod-4 reading of "quarter turns" was wrong for mixed words, because distinct generators anticommute and move the sign.
- **The 8–15 half.** With F = 8 (my choice, not derived) 56.2 % of the words with F end in the upper half and 76 % enter it within five letters; the mean walk spends 53 % of its steps there. This is mostly the parity of F's count (F is dense: 97,461 letters), so membership in 8–15 does not depend on whether F is 8 or 15 (H2, certain by XOR) but the exact address does (56 % differ). The 8–15 half is monitored, but the quantity monitored is the parity of F, not a finding about Ĥ_RB. What would be a finding is a fourth generator that is not just a labelled slot.
- **What the circle table gives.** `catalog/circles_ufm.csv` lists, for each of the 6,268 fractal formulas, where it enters (init end), the circle it goes round (loop end, circle number) and where it leaves (bailout end): the per-equation record the author asked for. Not done: the circle for the 65 python equations (no init/bailout); the walk is only the whole word.
