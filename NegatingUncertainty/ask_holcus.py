"""ask_holcus.py: Ask Holcus (the maths) about position, momentum and uncertainty, in mathematics.
Runs the Circle Atlas viewports that bear on (x, p) and prints exactly what they answer; the predictions in
01_holcus_asks.ipynb are read off these answers, not invented.  Run from the ThePlace directory:
    python3 FourthAgePapers/NegatingUncertainty/ask_holcus.py"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace"))
from ValaQuenta.modules.circle_atlas import maths as M

def show(r, depth=1):
    for k, v in r.items():
        if isinstance(v, dict): print("  "*depth + str(k) + ":"); show(v, depth + 1)
        else: print("  "*depth + "%s: %s" % (k, str(v)[:240]))

ASK = [("hamiltonian", "where do (q, p) live under a Hamiltonian?"),
       ("waveform", "what is the partner of a wave?"),
       ("lagrangian", "what is p, from the action?"),
       ("berry_keating", "what is H = xp?")]
if __name__ == "__main__":
    for k, q in ASK:
        v = M.VIEWPORTS[k]
        print("== %s  [%s]  source: %s\n   asked: %s" % (v["name"], v["tier"], v["source"], q)); show(v["fn"]())
