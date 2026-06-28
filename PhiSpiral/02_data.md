# PhiSpiral — Data
**Date:** 2026-06-15  
**Source:** Live computation, session 2026-06-15

---

## Constants

    φ  = 1.6180339887498948
    π  = 3.1415926535897932
    d* = 0.2460000000  (Dirichlet beta at σ=½, canonical)

---

## Rotation operators

    e^(πi)       = −1.000000 + 0.000000i
    e^(iφ)       = −0.047220 + 0.998885i
    e^(i(π+φ))   =  0.047220 − 0.998885i
    e^(i(π−φ))   =  0.047220 + 0.998885i

---

## Precession angle

    φ − π/2      = 0.04723766195499
    cos(φ)       = −0.04722009625368
    difference   = 1.756570130e-05

    sin(φ)       = 0.99888450909545
    1 − sin(φ)   = 0.00111549090455

    e^(iφ) ≈ i − (φ−π/2)   [to 1.76e-05]

---

## n* coupling table

    proxy_coupling = d* / (−cos φ) = 5.20964631

    | base | ln(base)  | n*_proxy   |
    |------|-----------|------------|
    | 2    | 0.693147  | 7.515931   |
    | e    | 1.000000  | 5.209646   |
    | π    | 1.144730  | 4.550983   |
    | 10   | 2.302585  | 2.262521   |

    Formula: n*_base = d* / (ln(base) · (−cos φ))

---

## N-ball V(n)

    V(n) = π^(n/2) / Γ(n/2+1)

    V(1)  = 2.00000000
    V(2)  = 3.14159265  [= π exactly]
    V(3)  = 4.18879020
    V(4)  = 4.93480220
    V(5)  = 5.26378901
    V(6)  = 5.16771278
    V(7)  = 4.72476597
    V(8)  = 4.05871213
    V(16) = 0.23533063  [≈ d* = 0.2460]

    N-ball peak: n* = 5.25694646  [ψ(n/2+1) = ln(π)]

---

## Gaps and ratios

    N-ball n*  −  proxy n*_e  =  0.04730015
    φ − π/2                   =  0.04723766
    difference                =  6.25e-05

    proxy n*_e  −  proxy n*_10 =  2.94712480
    F(4) = 3

    n*_e / n*_10 = 2.30258509 = ln(10)  [exact by construction]
    n*_2 / n*_e  = 1.44269504 = log_2(e) [exact]

---

## φ power identities (exact)

    φ¹ = 1.61803399
    φ² = 2.61803399  = φ + 1
    φ³ = 4.23606798  = 2φ + 1
    φ⁴ = 6.85410197  = 3φ + 2
    φ⁵ = 11.09016994 = 5φ + 3

    φ⁴ − φ³ = φ²  [exact: 4 = 3 + 2 in φ-space]
    F(4) = 3, F(5) = 5, F(5)/F(4) = 5/3 → φ

---

## Quaternion rotation: 4 → 3

    e^(φk) · i · e^(−φk) = i·cos(2φ) + j·sin(2φ)
                          = i·(−0.995541) + j·(−0.094335)

    Real (scalar) component: 0  [exactly]
    Result lives in {i,j,k} = ℝ³  [3D, not 4D]
    4D operation → 3D result: 4 = 3

---

## π approximation via φ

    φ² · (6/5) = 3.14164079  vs  π = 3.14159265
    error = 4.81e-05

    golden angle: 2π/φ² = 2.39996323 rad = 137.5078°

---

## V(n) at the 4 proxy n* values

    V(7.5159) = 4.400565   [n*_bits]
    V(5.2096) = 5.277299   [n*_nats]
    V(4.5510) = 5.170555   [n*_geom]
    V(2.2625) = 3.435228   [n*_decades]
