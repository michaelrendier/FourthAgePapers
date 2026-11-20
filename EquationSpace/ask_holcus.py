"""ask_holcus.py: Ask Holcus (the maths) what it says about equation space, the sigma = 0 permutation space of equations over the Cayley-Dickson operators.
Prints exactly what the ValaQuenta engines answer; the predictions in 01_holcus_asks.md are read off these answers.
   ValaQuenta/.venv/bin/python FourthAgePapers/EquationSpace/ask_holcus.py"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/Projects/ThePlace"))
from ValaQuenta.modules.bracketing_firing_order import maths as B
from ValaQuenta.modules.emerger import maths as E
from ValaQuenta.modules.circle_atlas import maths as A
def show(r, d=1):
    for k, v in (r.items() if isinstance(r, dict) else enumerate(r)):
        if isinstance(v, dict): print("  "*d + str(k) + ":"); show(v, d + 1)
        else: print("  "*d + "%s: %s" % (k, str(v)[:240]))
ASK = [("how many ways can n operators be bracketed and fired?", lambda: B.bracketing_report(list("abcd"))),
       ("how many firing orders for n=4, 7?", lambda: {"4": B.firing_order_count(4), "7": B.firing_order_count(7)}),
       ("what shapes does the 15-unit imaginary space partition into? (scale_partitions)", lambda: E.scale_partitions()),
       ("is the emerger self-consistent? (verify)", lambda: E.verify()),
       ("what does the lineage of the emerger say?", lambda: E.lineage_report()[:6])]
if __name__ == "__main__":
    for q, f in ASK:
        print("== asked:", q); show(f())
    print("== circle_atlas viewports:", sorted(A.VIEWPORTS))
