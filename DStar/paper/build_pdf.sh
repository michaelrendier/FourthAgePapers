#!/usr/bin/env bash
# Builds ../DStar.pdf
# The fallback definition must come BEFORE the font set-up, so the tex is generated, patched, then compiled twice.
set -euo pipefail
cd "$(dirname "$0")"
true
pandoc dstar_paper.md -s -o /tmp/dstar.tex -V geometry:margin=1in -V fontsize=10pt -V colorlinks=true \
  -V mainfont="DejaVu Serif" -V mainfontoptions="RawFeature={fallback=fbk}" -V monofont="DejaVu Sans Mono" \
  -V monofontoptions="Scale=0.8,RawFeature={fallback=fbk}" -H header.tex \
  -V title-meta="d*: one crossing, four faces, and a symbol table" -V author-meta="Cody Michael Allison"
python3 - <<'PY'
p = '/tmp/dstar.tex'; s = open(p).read()
fb = '\\directlua{luaotfload.add_fallback("fbk",{"Unifont:mode=node;"})}\n'
i = s.index('\\usepackage{fontspec}') if '\\usepackage{fontspec}' in s else s.index('\\setmainfont')
open(p, 'w').write(s[:i] + fb + s[i:])
PY
for i in 1 2; do lualatex -interaction=nonstopmode -output-directory=/tmp /tmp/dstar.tex >/tmp/dstar_$i.log 2>&1; done
cp /tmp/dstar.pdf ../DStar.pdf
echo "pages: $(pdfinfo ../DStar.pdf | awk '/Pages/{print $2}'); missing glyph warnings: $(grep -c 'Missing character' /tmp/dstar_2.log || true)"
