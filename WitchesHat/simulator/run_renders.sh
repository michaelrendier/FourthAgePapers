#!/usr/bin/env bash
# stills for three hat shapes, then a turntable of the SM-shape hat. nice'd so downloads keep priority.
cd "$(dirname "$0")"
for n in 4 2.5 10; do nice -n 15 blender -b -P render_hat.py -- renders_v3 $n > renders_v3_n$n.log 2>&1; echo "[render] still n=$n exit $?"; done
nice -n 15 blender -b -P render_hat.py -- renders_v3 4 turn > renders_v3_turn.log 2>&1; echo "[render] turntable exit $?"
