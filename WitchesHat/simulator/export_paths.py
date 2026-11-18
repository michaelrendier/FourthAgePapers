"""Write the path bundle for the renderer: python3 export_paths.py [n] -> hat_paths_n{n}.json (numpy only needed by hat_sim)."""
import json, sys, numpy as np
import hat_sim as H
n = float(sys.argv[1]) if len(sys.argv) > 1 else 4.0
out = {"n": n, "paths": [], "rmin": {}}
for psi in (0.02, 0.06, 0.12, 0.2, 0.3, 0.45):
    x, y, V, W = H.trace_path(psi, 0.0, n, T=300.0, npts=400)
    out["rmin"][str(psi)] = float(np.hypot(x, y).min())
    for sgn in (1, -1):
        for k in range(12):
            a = 2*np.pi*k/12 + (0.13 if sgn < 0 else 0)
            c, s = np.cos(a), np.sin(a)
            xr, yr = c*x - s*sgn*y, s*x + c*sgn*y
            out["paths"].append({"psi": psi, "x": xr.tolist(), "y": yr.tolist(), "V": V.tolist(), "W": W.tolist()})
json.dump(out, open("hat_paths_n%g.json" % n, "w"))
print("n=%g: %d paths, r_min by psi %s" % (n, len(out["paths"]), {k: round(v, 3) for k, v in out["rmin"].items()}))
