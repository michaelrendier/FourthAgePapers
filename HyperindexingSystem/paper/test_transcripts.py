"""Re-runs every `>` transcript block in the paper draft in a FRESH namespace (Listings 1 and 2 loaded) and
compares each printed output with the text of the draft. Run:  python3 paper/test_transcripts.py"""
import re, io, os, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
draft = open(os.path.join(HERE, "00_sections_1_to_4_draft.md")).read()
blocks = re.findall(r"```\n(> .*?)```", draft, re.S)
bad = n = 0
for b in blocks:
    ns = {}
    for f in ("L1_ordered_address.py", "L2_scrambler.py"): exec(open(os.path.join(HERE, "listings", f)).read(), ns)
    lines = b.rstrip("\n").split("\n"); i = 0
    while i < len(lines):
        cmd = lines[i][2:]; i += 1; exp = []
        while i < len(lines) and not lines[i].startswith("> "): exp.append(lines[i]); i += 1
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            try: r = eval(cmd, ns)
            except SyntaxError: exec(cmd, ns); r = None
        out = buf.getvalue().rstrip("\n").split("\n") if buf.getvalue() else []
        if r is not None: out.append(repr(r))
        n += 1
        if out != exp: bad += 1; print("MISMATCH:", cmd, "\n expected", exp, "\n got     ", out)
print(n, "transcript commands,", bad, "mismatches")
assert bad == 0
