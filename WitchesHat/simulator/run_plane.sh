#!/usr/bin/env bash
cd "$(dirname "$0")"
for m in sm vap; do nice -n 15 blender -b -P render_plane.py -- renders_plane2 $m > renders_plane2_$m.log 2>&1; echo "[render] $m exit $?"; done
