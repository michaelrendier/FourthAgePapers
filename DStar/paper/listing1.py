# Listing 1 — the induction x → exp(−x) and the digits it gains per step (stand-alone)
import math
from decimal import Decimal, getcontext
getcontext().prec = 60
x = Decimal("0.5")
for _ in range(400):
    x = (-x).exp()                       # fixed point: x = exp(−x)  ⇒  x = W(1)
A_PI = float(x)
step = lambda t: (-t).exp()              # contraction factor at the fixed point: |d/dx exp(−x)| = x = A_PI
digits_per_step = -math.log10(A_PI)      # = A_PI / ln 10, because ln A_PI = −A_PI
print(f"A_PI              = {A_PI!r}")
print(f"digits per step   = {digits_per_step!r}")
print(f"A_PI / ln 10      = {A_PI / math.log(10)!r}")
print(f"0.246 · ln 10     = {0.246 * math.log(10)!r}   (residual vs A_PI: {A_PI - 0.246 * math.log(10):.12f})")
