#!/usr/bin/env bash
# Builds ../TwinPrimeWheels.pdf (the ONLY PDF kept in the repo; Cody 2026-10-14) from the markdown (pandoc + LuaLaTeX; DejaVu fonts with a Unifont fallback).
# The fallback definition must come BEFORE the font set-up, so the tex is generated, patched, then compiled twice.
set -euo pipefail
cd "$(dirname "$0")"
python3 make_paper.py
pandoc Twin_Prime_Wheels.md -s -o /tmp/twinwheels.tex -V geometry:margin=1in -V fontsize=10pt -V colorlinks=true \
  -V mainfont="DejaVu Serif" -V mainfontoptions="RawFeature={fallback=fbk}" -V monofont="DejaVu Sans Mono" \
  -V monofontoptions="Scale=0.8,RawFeature={fallback=fbk}" -H header.tex \
  -V title-meta="Twin-Prime Wheels" -V author-meta="Cody Michael Allison"
python3 - <<'PY'
p = '/tmp/twinwheels.tex'; s = open(p).read()
fb = '\\directlua{luaotfload.add_fallback("fbk",{"Unifont:mode=node;"})}\n'
i = s.index('\\usepackage{fontspec}') if '\\usepackage{fontspec}' in s else s.index('\\setmainfont')
open(p, 'w').write(s[:i] + fb + s[i:])
PY
for i in 1 2; do lualatex -interaction=nonstopmode -output-directory=/tmp /tmp/twinwheels.tex >/tmp/twinwheels_$i.log 2>&1; done
cp /tmp/twinwheels.pdf ../TwinPrimeWheels.pdf
echo "pages: $(pdfinfo ../TwinPrimeWheels.pdf | awk '/Pages/{print $2}'); missing glyph warnings: $(grep -c 'Missing character' /tmp/twinwheels_2.log || true)"
