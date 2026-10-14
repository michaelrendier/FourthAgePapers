#!/usr/bin/env bash
# Builds ../CollatzShift.pdf (the ONLY PDF kept in the repo; Cody 2026-10-14) from the markdown (pandoc + LuaLaTeX; DejaVu fonts with a Unifont fallback).
# The fallback definition must come BEFORE the font set-up, so the tex is generated, patched, then compiled twice.
set -euo pipefail
cd "$(dirname "$0")"
python3 make_paper.py
pandoc A_Bit_Shift_Wearing_A_Disguise.md -s -o /tmp/bitshift.tex -V geometry:margin=1in -V fontsize=10pt -V colorlinks=true \
  -V mainfont="DejaVu Serif" -V mainfontoptions="RawFeature={fallback=fbk}" -V monofont="DejaVu Sans Mono" \
  -V monofontoptions="Scale=0.8,RawFeature={fallback=fbk}" -H header.tex \
  -V title-meta="A Bit Shift Wearing A Disguise" -V author-meta="Cody Michael Allison"
python3 - <<'PY'
p = '/tmp/bitshift.tex'; s = open(p).read()
fb = '\\directlua{luaotfload.add_fallback("fbk",{"Unifont:mode=node;"})}\n'
i = s.index('\\usepackage{fontspec}') if '\\usepackage{fontspec}' in s else s.index('\\setmainfont')
open(p, 'w').write(s[:i] + fb + s[i:])
PY
for i in 1 2; do lualatex -interaction=nonstopmode -output-directory=/tmp /tmp/bitshift.tex >/tmp/bitshift_$i.log 2>&1; done
cp /tmp/bitshift.pdf ../CollatzShift.pdf
echo "pages: $(pdfinfo ../CollatzShift.pdf | awk '/Pages/{print $2}'); missing glyph warnings: $(grep -c 'Missing character' /tmp/bitshift_2.log || true)"
