#!/usr/bin/env python3
"""Add the 2026-11-14 correction-pass front block and ContextPlease appendix to a draft paper (markdown), in place.

usage: tools/correction_pass.py PAPER_DIR SOURCE.md [extra note ...]
The text of the draft is not changed: a block is inserted after the first heading, and an appendix is appended.
Findings are searched for in the draft itself (retired or corrected claims of the Ainulindale overhaul) and the
executed-cell count of the paper's notebooks is measured. Idempotent (marker comment).
"""
import glob, json, os, re, sys

MARK = '<!-- correction-pass-2026-11-14 -->'
PATTERNS = [
    (r'Noether (current|balance|conservation)|J_R \+ J_B|J_red \+ J_blue', 'A Noether-current / Noether-balance statement for the σ = ½ map. **Retired as a conserved-current statement**: s ↦ 1 − s is a discrete involution, so there is no continuous symmetry and no Noether current (Ainulindalë wiki 133 §3, ledger X-4). The J_red + J_blue = J_green balance stands as a measured relation of the sedenion grading. The statement is kept as written, because the maths started here.'),
    (r'zero free param|Zero free param|without fitting|no free param', '"Zero free parameters" is stated as a result. A parameter count is a claim about how a number was obtained; where a number was assigned and not computed it is not a result. Each such number needs its script (Fourth Age Protocol §1, §3).'),
    (r'84 (directed )?(ZD )?pairs|84 pairs|168 composite|42 classes', 'Sedenion zero-divisor counts written as "84 pairs / 42 classes / 168 composite". Verified counts: **84 zero-divisors on 42 index pairs; 168 unordered and 336 ordered zero-product pairs** (wiki 133, 135).'),
    (r'self-organis', '"The 16 operator names self-organise … zero free parameters" is **not reproduced**: the run, the criterion and a null (random names through the same hash) are not shown anywhere (wiki `CS_SIGMA_EVALUATION.md` audit).'),
    (r'97 ?%', 'The "97 %" overhead reduction has **no benchmark** behind it and is not reported as a result (wiki 136 and the D-CS_Memory limits).'),
    (r'Zipf', '"Zipf\'s law is the prime number theorem" is **withdrawn** (wiki 133, 135).'),
    (r'mass gap.{0,60}(derived|0\.000707)|0\.000707', 'The mass gap Δ = Ω_ζΣ − d*·ln 10 is a **named subtraction**, not a spectral residue; "derived without fitting" is not supported (wiki 120, 123).'),
    (r'Telperion|Laurelin', 'Telperion / Laurelin labelling: the author\'s current assignment is **Telperion = the primes tree, Laurelin = the factors (Fermat side)**; Telperion is not the zero-divisor tree. Older octonion-half labels are being corrected to it (wiki 133 §7.10, ledger X-20).'),
    (r'137\.03|α ?≈ ?1/137|fine.structure', 'The fine-structure constant α_fs = 1/137.036, the Fermat-side constant A_fermat (value **open**) and the network coupling α_NN are three different things (wiki 133 §0).'),
    (r'0\.246|d\*', 'd* has four faces (0.24631 Boundary; the RG face, numeric open; Ω/ln 10; d*·ln 10 = Ω) and 0.24600 is a measured value that is not one of them (wiki 133 §2.2).'),
    (r'Hagedorn|1\.4 ?[×x] ?10\^?\{?17|140 quadrillion', 'The "1.4×10¹⁷ K / 140 quadrillion" thermal ceiling is a boundary condition chosen by the author, not the hadronic Hagedorn temperature (1.7–2.0×10¹² K) and not the Planck temperature (1.417×10³² K) (wiki 136, ledger X-54).'),
]


def executed(pdir):
    n = tot = 0
    for f in glob.glob(os.path.join(pdir, '**', '*.ipynb'), recursive=True):
        try: nb = json.load(open(f))
        except Exception: continue
        code = [c for c in nb['cells'] if c['cell_type'] == 'code']
        tot += len(code); n += sum(1 for c in code if c.get('outputs'))
    return n, tot


def main():
    pdir, src = sys.argv[1], sys.argv[2]; extra = sys.argv[3:]
    text = open(src).read()
    if MARK in text: print('already done:', src); return
    lines = text.split('\n'); found = []
    for pat, msg in PATTERNS:
        hits = [i + 1 for i, l in enumerate(lines) if re.search(pat, l)]
        if hits: found.append((msg, hits))
    n, tot = executed(pdir)
    nb = ('The notebooks in this directory have **no executed cell** (0 of %d code cells carry outputs): nothing quoted below has been reproduced since the notebooks were generated.' % tot) if tot and n == 0 else \
         ('Notebook code cells with recorded outputs: %d of %d.' % (n, tot) if tot else 'This directory has no notebooks.')
    block = [MARK, '> ## Status and corrections, 2026-11-14', '>',
             '> *Added by the correction pass; the text of the draft below is unchanged.*', '>',
             '> **Assistant note.** This pass was made by a transformer language model (Claude Sonnet 5.5, `claude-sonnet-5-5`) with the project\'s `cs-paper-code-conventions` skill and the Fourth Age Protocol loaded (`ContextPlease/claude/skills/`, `ContextPlease/FOURTH_AGE_PROTOCOL.md`). The author is Cody Michael Allison (pen name Michael Rendier), an autodidact, not an academic; his method is not to tell the model the result he is looking for. This is a **draft**: its claims are the author\'s, and the labels of the Ainulindalë overhaul (ESTABLISHED, OURS, THEORETICAL, OPEN, with `:CALCULATED` for results the paper\'s own code produced) apply to every statement in it.', '>',
             '> **State.** ' + nb, '>']
    if found:
        block += ['> **Statements in this draft that the Ainulindalë overhaul retired, corrected or did not reproduce** (line numbers refer to this file before the block was added; each statement is kept as written):', '>']
        for msg, hits in found:
            ls = ', '.join(str(h) for h in hits[:6]) + (' …' if len(hits) > 6 else '')
            block += ['> - (lines %s) %s' % (ls, msg)]
        block += ['>']
    else:
        block += ['> **Statements retired or corrected by the overhaul:** none of the patterns searched for were found in this draft.', '>']
    for e in extra: block += ['> ' + e, '>']
    block += ['> **Authority.** Notation and verified counts: Ainulindalë `wiki/133_canonical_maths.md`; every defect found: `wiki/135_engine_findings_ledger.md`; the audit of this repository: `AUDIT_2026-11-14.md`.', '']
    # insert after the first heading line
    i = next((k for k, l in enumerate(lines) if l.startswith('#')), -1)
    lines[i + 1:i + 1] = [''] + block
    app = ['', '---', '', '## Appendix — what in ContextPlease was used, and what ContextPlease is', '',
           '**ContextPlease** (`https://github.com/michaelrendier/ContextPlease`) is the *Manual Transmission Context Continuity* library: the versioned record that lets a new human or AI agent pick up a project without rediscovering it. Nothing in it is loaded automatically; whoever works chooses what to read. Used for this correction pass: the Fourth Age Protocol (`FOURTH_AGE_PROTOCOL.md`), the paper-writing conventions (`claude/skills/cs-paper-code-conventions/`) and the canonical notation (`claude/.clauderc_canonical_maths`).', '']
    open(src, 'w').write('\n'.join(lines).rstrip('\n') + '\n' + '\n'.join(app))
    print(src, '- findings:', len(found), '; notebooks executed %d/%d' % (n, tot))


main()
