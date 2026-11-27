# TODO: HyperindexingSystem

## Next engineering goal (author, 2026-11-27): the text-only Midline address, four digits, at most 52 list indexes

**The idea.** Text is addressed with letters only; digits are **not** semantic and get another method (numbers are not words; the monad harness already splits them out with `mh_split_numbers`, and a mathematical treatment is to come). The text-only code is four digits, each from a tiny set:

| digit | meaning | values |
|---|---|---|
| 1 | case | 0 lower · 1 upper |
| 2 | side of the anchor (m / M) | 0 down · 1 up |
| 3 | tens of the step | 0 or 1 (the step is at most 13) |
| 4 | units of the step | 0–9 (only 0–3 when digit 3 is 1) |

So the whole text-only alphabet is (0,1):(0,1):(0,1):(0–9), **13 steps × 4 (case × side) = 52 list indexes**, and every index is at most two decimal digits (0–51). A text is then a sequence of calls from that list of 52, and the per-character cost is log₂ 52 = 5.7004 bits, against log₂ 96 = 6.5850 for the 96-code table with digits and punctuation.

**Checked against the shipped code, 2026-11-27.** `PtolemyDesktop/Archimedes/Maths/MidlineIndex.py` already contains exactly these 52 letter codes: of its 96 `VALID_CODES`, the 52 below 2000 are 13 for each of (case, side), steps 0–13 (the anchor takes sign 0). The next step is to give them their own two-digit list index and an address over 52 symbols, and to move digits and punctuation out of the text address to their own methods.

**Why (author).** "The whole text only 4 digits have a strictly small and finite permutation": a text can be reduced to four digits per character and called from a list of every permutation of the possible four digits. This is the author's first proposition for the Midline cipher, which did not reach the assistant at the time: follow it **without digits**, text characters only.

**Open (to decide when this is built):** what happens to punctuation and white space (a separate small list, or the 34-symbol group that exists now); the digit method (non-semantic: a numeric address, mathematical treatment); how the bits per character compare once punctuation is paid for. **Not to be built until the author says go.**

## Reference models (author, 2026-11-26)
Basile (`ValaQuenta/modules/basile`, local only) is a reference model, not a necessary inclusion: a post-hoc attempt at reducing the bits needed to represent text. The Sanderson compression video (arithmetic coding) lives with it; see `citations.md`.
