#!/usr/bin/env bash
# rebuild_finalpapers.sh (2026-11-20): rebuild every PDF in ~/Desktop/SpaceClaude/FinalPapers/FourthAgePapers/ from the CURRENT draft of its paper.
# 1. archives the current PDFs into FinalPapers/FourthAgePapers/archive/<date>/   2. builds each paper (pandoc + LuaLaTeX via tools/build_pdf.sh; CollatzShift and AdditionMatrixOrbits use their own paper/build_pdf.sh)
# 3. copies the new PDF over the old name only if the build succeeded.   Sources are read from main, from the witches-hat worktree (CMB_FractalBoundary, DM_GalacticCavity, no longer on main), from the minds-eye-papers-hands branch,
# and from VAPMIP (ScalarContextPropagation).  DataStorageNoLocation is NOT rebuilt: its source (branch data-storage-no-location, README.md) has not changed since 2026-08-30.
set -uo pipefail
R="$(cd "$(dirname "$0")/.." && pwd)"; P="$(cd "$R/.." && pwd)"; FP=~/Desktop/SpaceClaude/FinalPapers/FourthAgePapers; D=$(date +%F); A="$FP/archive/$D"; S=$(mktemp -d)
mkdir -p "$A"; for f in "$FP"/*.pdf; do cp -n "$f" "$A/"; done
WH="$P/_worktrees/FourthAgePapers_witches-hat"; git -C "$R" show minds-eye-papers-hands:MindsEyePapersHands/README.md > "$S/MindsEye.md"
declare -A SRC TITLE
SRC[AxisNShape]="$R/AxisNShape/PAPER.md";                       TITLE[AxisNShape]="The Axis N-Shape: Euler's Formula as a Partial-Sum Spiral"
SRC[BoundaryLever]="$R/BoundaryLever/README.md";                TITLE[BoundaryLever]="The Boundary Lever"
SRC[CMB_FractalBoundary]="$WH/CMB_FractalBoundary/paper_draft.md"; TITLE[CMB_FractalBoundary]="Fractal Boundary Ptychography of the Planck and WMAP CMB Datasets"
SRC[DM_GalacticCavity]="$WH/DM_GalacticCavity/paper_draft.md";  TITLE[DM_GalacticCavity]="Dark Matter as Galactic Resonant Cavity Modes"
SRC[HyperindexingSystem]="$R/HyperindexingSystem/paper/00_sections_1_to_4_draft.md"; TITLE[HyperindexingSystem]="The Hyperindexing System: Data With No Physical Location"
SRC[InertiaEntropy]="$R/InertiaEntropy/README.md";              TITLE[InertiaEntropy]="InertiaEntropy: Inertia and Entropy"
SRC[MindsEyePapersHands]="$S/MindsEye.md";                      TITLE[MindsEyePapersHands]="How Short-Term Thought Is Required for Long-Term Memory"
SRC[PhiSpiral]="$R/PhiSpiral/paper_draft.md";                   TITLE[PhiSpiral]="The phi-Spiral: Golden Ratio as the Magneto Operator"
SRC[PiFromAbove]="$R/PiFromAbove/paper_draft.md";               TITLE[PiFromAbove]="The Spiral Defined From Above"
SRC[Telperion]="$R/Telperion/PAPER.md";                         TITLE[Telperion]="The Zero Lattice: Telperion"
SRC[UmbrellaNoether]="$R/UmbrellaNoether/mode2_academic/UMBRELLA_NOETHER_PAPER.md"; TITLE[UmbrellaNoether]="A Unified Framework for Gravity, Fluid Dynamics, and Molecular Physics"
SRC[ScalarContextPropagation]="$P/VAPMIP/FourthAgePaper/ScalarContextPropagation/19_Dimensional_Scalar_WordNet_Context_Propagation_v4.0.md"; TITLE[ScalarContextPropagation]="19 Dimensional Scalar WordNet Context Propagation"
for n in "${!SRC[@]}"; do
  echo "--- $n  (source $(basename "${SRC[$n]}"))"
  ( cd "$(dirname "${SRC[$n]}")" && "$R/tools/build_pdf.sh" "${SRC[$n]}" "$S/$n.pdf" "${TITLE[$n]}" ) 2>&1 | tail -2
  if [ -s "$S/$n.pdf" ]; then cp "$S/$n.pdf" "$FP/$n.pdf"; echo "    installed (was $(pdfinfo "$A/$n.pdf" 2>/dev/null | awk '/Pages/{print $2}') pages)"; else echo "    BUILD FAILED, old PDF kept"; fi
done
for n in CollatzShift AdditionMatrixOrbits; do
  echo "--- $n (own pipeline)"; ( cd "$R/$n/paper" && bash build_pdf.sh ) 2>&1 | tail -2
  [ -s "$R/$n/$n.pdf" ] && cp "$R/$n/$n.pdf" "$FP/$n.pdf" && echo "    installed (was $(pdfinfo "$A/$n.pdf" 2>/dev/null | awk '/Pages/{print $2}') pages)" || echo "    BUILD FAILED, old PDF kept"
done
echo "archive: $A"; ls "$A" | wc -l
