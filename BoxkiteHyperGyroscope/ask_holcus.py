"""ask_holcus.py: Ask Holcus (the maths) how the sedenion holds the boxkite and the hyper-gyroscope.  Prints exactly what the Circle Atlas
viewports answer; the predictions in 01_holcus_asks.ipynb are read off these answers.  Run:  python3 FourthAgePapers/BoxkiteHyperGyroscope/ask_holcus.py"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace"))
from ValaQuenta.modules.circle_atlas import maths as M
def show(r, d=1):
    for k, v in r.items():
        if isinstance(v, dict): print("  "*d + str(k) + ":"); show(v, d + 1)
        else: print("  "*d + "%s: %s" % (k, str(v)[:240]))
ASK = [("sedenion", "how many circles does the sedenion hold, and which pairs annihilate?"),
       ("kite_spectrum", "what does a boxkite sound like, and can it tell kites apart?"),
       ("hypersphere", "is S^15, the sedenion's unit sphere, a group of rotations?"),
       ("hopf", "what is the circle fibre structure?")]
if __name__ == "__main__":
    for k, q in ASK:
        v = M.VIEWPORTS[k]; print("== %s  [%s]  source: %s\n   asked: %s" % (v["name"], v["tier"], v["source"], q)); show(v["fn"]())
