"""H. The constants: Omega, d* and its faces. Cold: stdlib only."""
import math
omega = 0.5
for _ in range(100): omega = math.exp(-omega)          # fixed point of e^-x, W(1)
print("Omega = W(1) = %.12f ; W e^W = %.12f" % (omega, omega*math.exp(omega)))
ln10 = math.log(10)
dstar = omega/ln10
print("d* = Omega/ln10 = %.12f ; d* ln10 = %.12f" % (dstar, dstar*ln10))
spec = 0.24600
print("d*_spec (measured) = %.5f ; gap = %.12f ; 1/(1000 sqrt2) = %.12f" % (spec, dstar - spec, 1/(1000*math.sqrt(2))))
X = math.exp(omega)
print("X* = e^Omega = %.6f = 1/Omega = %.6f ; log10 X* = %.9f = d*" % (X, 1/omega, math.log10(X)))
print("c_s/c = 1/sqrt3 = %.6f ; Omega/(1/sqrt3) = %.4f" % (1/math.sqrt(3), omega*math.sqrt(3)))
print("16-ball volume pi^8/8! = %.5f ; d* = %.5f ; ratio %.4f" % (math.pi**8/math.factorial(8), dstar, math.pi**8/math.factorial(8)/dstar))
