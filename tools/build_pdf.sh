#!/usr/bin/env bash
# Build a PDF from a markdown paper (pandoc + LuaLaTeX; DejaVu fonts with a Unifont fallback for missing glyphs).
# usage: tools/build_pdf.sh SOURCE.md OUT.pdf "Title"
# Same recipe as CollatzShift/paper/build_pdf.sh, made generic.
set -euo pipefail
src="$1"; out="$2"; title="${3:-$(basename "$out" .pdf)}"; here="$(cd "$(dirname "$0")" && pwd)"
t="$(mktemp -d)"; base="$t/paper"
pandoc "$src" -s -o "$base.tex" -f markdown-smart-yaml_metadata_block -V geometry:margin=1in -V fontsize=10pt -V colorlinks=true \
  -V mainfont="DejaVu Serif" -V mainfontoptions="RawFeature={fallback=fbk}" -V monofont="DejaVu Sans Mono" \
  -V monofontoptions="Scale=0.8,RawFeature={fallback=fbk}" -H "$here/header.tex" -V title-meta="$title" -V author-meta="Cody Michael Allison" --wrap=preserve
python3 - "$base.tex" <<'PY'
import sys
p = sys.argv[1]; s = open(p).read()
fb = '\\directlua{luaotfload.add_fallback("fbk",{"Unifont:mode=node;"})}\n'
i = s.index('\\usepackage{fontspec}') if '\\usepackage{fontspec}' in s else s.index('\\setmainfont')
open(p, 'w').write(s[:i] + fb + s[i:])
PY
for i in 1 2; do lualatex -interaction=nonstopmode -output-directory="$t" "$base.tex" >"$t/run$i.log" 2>&1 || true; done
[ -f "$base.pdf" ] || { echo "PDF build FAILED; see $t/run2.log" >&2; tail -20 "$t/run2.log" >&2; exit 1; }
cp "$base.pdf" "$out"
echo "$(basename "$out"): $(pdfinfo "$out" | awk '/Pages/{print $2}') pages; missing-glyph warnings: $(grep -c 'Missing character' "$t/run2.log" || true)"
