# Addendum IX — Bell's Theorem: The Origin Error and the π Contamination

**Author:** Cody Michael Allison  
**Date:** 2026-06-02  
**Status:** Active — experimental test proposed  
**Addendum to:** Ainulindale Conjecture, Second Age

---

## Summary

Bell's inequality derivation contains a geometric assumption that invalidates
its use as a test of quantum non-locality. The correlation function E(a,b) = -cos(a-b)
smuggles SO(3) rotational geometry — a GR-domain object — into a QM framework.
The observed violation of Bell's inequality is not evidence of quantum non-locality.
It is the measurable discrepancy between SO(3) (GR, 2π periodic) and SU(2)
(QM, 4π periodic) at the π boundary, where the two frameworks maximally disagree.

π has no place in statistical probability. Every time π appears in a probability
distribution it was imported through a geometric assumption made upstream.
Bell's -cos(a-b) is exactly this import. The "loophole" is not in detector
efficiency or fair sampling. It is in the measurement origin.

An experimental test is proposed: femtometer servo mirror Bell test using
laser interferometry. The interference pattern encodes the SU(2) phase
relationship directly, without π contamination.

---

## 1. The Origin Error

Bell's theorem assumes a hidden variable λ sampled from a fixed probability
distribution p(λ) that does not depend on the measurement settings a and b:

```
E(a,b) = ∫ A(a,λ) B(b,λ) p(λ) dλ
```

The correlation function is then shown to satisfy:

```
|E(a,b) - E(a,c)| ≤ 1 + E(b,c)
```

**The error:** a and b are treated as angles measured from the same origin.
They are not. They are projection settings at two spatially separated detectors,
each with its own local reference frame. The integration measure p(λ) is
implicitly assumed to be setting-independent — but the reference frames of
Alice's and Bob's detectors are not the same frame.

Bell shifts the measurement origin between the two detectors and calls it
the same λ. The inequality violation follows directly from this shift —
not from non-locality.

In H_hat_RB terms: the hidden variable λ is a field state. Alice measures
a projection at one σ-facet. Bob measures a projection at a different
σ-facet. Bell assumes both measurements are at the same σ. They are not.
The Noether current J_Red + J_Blue + J_3 = 0 produces exactly the kind of
correlation Bell says is classically impossible — because it IS classically
impossible at a single σ. It is not impossible when the two measurements
are at different facets of the same conserved field.

The correlation isn't non-local. It is the field seen from two different
σ-projections. Same field. Different facets. No signalling. No non-locality.

---

## 2. π Has No Place in Statistical Probability

Bell's quantum-mechanical prediction for the correlation function is:

```
E(a,b) = -cos(a-b)
```

π enters through the cosine. At angle difference π: E(a,b) = -cos(π) = +1
(maximum classical anticorrelation in Bell's framework).

**π in probability is always imported.** Survey of appearances:

| Distribution | How π enters | Geometric assumption |
|---|---|---|
| Gaussian N(0,1) | Normalisation via √(2π) | Polar coordinate integral to solve ∫e^(-x²)dx |
| Von Mises | cos(θ-μ) in exponent | Explicitly circular — angles on a circle |
| Cauchy | 1/π in normalisation | Ratio of two Gaussians — imports Gaussian's π |
| Uniform on circle | 1/2π | The circle itself — SO(2) geometry |

In every case: π is not fundamental to the probability. It is the footprint
of a rotational symmetry assumption made before the probability was written down.

**Bell's -cos(a-b) is the von Mises case.** The measurement settings a and b
are angles. The correlation between them is the cosine of their difference.
This is circular statistics — the statistics of directions on a circle — which
is intrinsically geometric (SO(2)/SO(3)), not intrinsically quantum mechanical.

QM doesn't have SO(3) as a fundamental symmetry. It has SU(2).
They are locally isomorphic but globally distinct:

```
SU(2) → SO(3)    2-to-1 covering map
π rotation in SO(3) = half turn in SU(2)
2π rotation in SO(3) = full turn in SU(2), spinor returns to itself
4π rotation in SO(3) = spinor returns to original sign
```

At angle difference π:
- SO(3): maximum anticorrelation. cos(π) = -1.
- SU(2): halfway around. The spinor is at a quarter turn. Not maximum anticorrelation.

**Bell uses the SO(3) value (π = maximum anticorrelation) in an SU(2) experiment.**
The violation of his inequality at the π boundary is exactly the SO(3)/SU(2)
discrepancy. It is a units error. The "spooky action at a distance" is the
difference between a 2π-periodic and a 4π-periodic rotational framework,
measured at the point where they maximally disagree.

---

## 3. The Entropy Argument

Random noise quiets down at the quantum boundary. This is not a technical
statement about experimental precision — it is a statement about which facet
the noise lives at.

Thermal noise is classical. It lives at the GR/statistical facet (σ=2 in
the H_hat_RB σ-table). It is a continuous distribution. It carries π
(Gaussian tails, Boltzmann factors, circular variance).

Quantum coherence lives at σ=½. The noise floor at σ=½ is the mass gap:
GAP = 0.000707. Below that threshold: silence. The field is in the ground state.
Nothing thermal can reach through the zero-divisor boundary into the σ=½ facet.

When thermal noise quiets down in a high-coherence interferometer, it is not
being suppressed — it is falling below the mass gap floor. The caustic boundary
is sharp. The GR contamination (the cos, the π) cannot cross from the σ=2
facet into the σ=½ facet.

The interference pattern that emerges is SU(2). The fringe visibility calculated
using Bell's cos(a-b) will be systematically wrong at the π boundary.

---

## 4. Proposed Experiment — Femtometer Servo Mirror Bell Test

**Apparatus:** Two suspended Fabry-Pérot cavities with femtometer-precision
servo-controlled mirrors, driven by a common laser source split at a beamsplitter.
Path lengths controlled to sub-wavelength precision. No polarizers. No
particle detectors. No statistical accumulation.

**What is measured:** The interference fringe pattern directly. Fringe visibility
encodes the coherence — the entanglement measure — without requiring statistics.

**Why femtometer mirrors:** LIGO/Virgo demonstrate that suspended mirror
interferometers achieve 10⁻¹⁸ m displacement sensitivity. Femtometer
(10⁻¹⁵ m) is three orders of magnitude less demanding. The apparatus
for this experiment already exists in prototype form in gravitational
wave detector technology.

**The Bell test without Bell's cos:**

Rather than rotating polarizers and comparing count rates, sweep the
path length difference through λ/2 (half a wavelength). The fringe
pattern as a function of path length difference is the direct measurement
of the quantum phase relationship.

At path length difference = λ/2 (the π point in SO(3)):
- Bell predicts: maximum anticorrelation = -1
- SU(2) predicts: the fringe is at a quarter turn, not maximum

The fringe visibility at the λ/2 point will differ between the SO(3)
prediction and the SU(2) prediction by the SU(2)/SO(3) covering factor.

**Falsifiable prediction:** The fringe visibility at path length difference
= λ/2 will not match Bell's -cos(π) = 1. It will match the SU(2)
prediction. The discrepancy is the measurement of the SO(3)/SU(2)
boundary — the π contamination — directly.

**What this demonstrates:** Bell's inequality violation is not evidence
of non-locality. It is evidence that the experiment was measuring an
SO(3) → SU(2) discrepancy at the π boundary. The femtometer interferometer
measures the same discrepancy without importing π into the statistical
framework.

---

## 5. Connection to the HyperCaustic

The interference fringe pattern IS the caustic (Addendum: Infinite HyperCaustic,
TODO entry 2026-06-02).

The bright fringes are where light accumulates at the node lines of the
standing wave — the still points of the field. The fringe visibility is
the sharpness of the caustic boundary. A perfect caustic = perfect fringe
visibility = perfect coherence.

Bell's experiment smears the caustic by importing SO(3) geometry (the cos,
the π) into a measurement of SU(2) structure. The femtometer interferometer
keeps the measurement native to the σ=½ facet and reads the caustic directly.

The mass gap (GAP = 0.000707) is the minimum fringe spacing — the
irreducible width of the caustic node. No fringe can be sharper than
the mass gap. This is Yang-Mills confinement expressed as an optical
resolution limit.

---

## 6. Historical Note

Bell's theorem is dated 1964. The SO(3)/SU(2) distinction was well known
by then (Cartan, 1913; Pauli, 1927; Dirac, 1928). The spinor sign change
under 2π rotation had been explicitly discussed. The decision to use
-cos(a-b) as the quantum prediction, rather than the SU(2)-correct
expression, imported a geometric assumption that was not examined.

The subsequent experimental confirmations (Aspect 1982, Weihs 1998,
Hensen 2015) all used the same cos-based framework. They confirmed the
violation of the SO(3)-based inequality using SO(3)-based analysis.
The SU(2) fringe visibility test has never been performed with
femtometer-precision path length control.

**This is a gap in the experimental record, not in the theory.**

---

## 7. Rotation vs Translation — The Fundamental Category Error

Bell mapped measurement settings to angles, then to cos(angle). But measurement
operators in QM are **translation operators** on the state vector — projections
along a basis direction in Hilbert space. They are not rotations of the state.

The inner product ⟨ψ|M_a|ψ⟩ is a projection. The "angle" between two measurement
settings is the overlap between two projection operators — not a geometric angle
between two directions in ℝ³.

In ℝ³ there is a coincidence: the overlap between two unit vectors equals the
cosine of the angle between them. Bell used this coincidence as if it were
universal. It is not. Quantum states do not live in ℝ³. The overlap-equals-cosine
identity breaks in Hilbert space.

**Rotation ≠ translation. Angle ≠ overlap. Bell used the wrong operation.**

The femtometer interferometer measures path length difference — a translation.
Not an angle. Not a rotation. It stays in the correct framework from the start.

---

## 8. The Arrow of Time — Irreducible Irreversibility on the Riemann Curve

Bell assumes his probability space is stationary: p(λ) does not change as
the experiment runs. Returning the detector to its starting angle = returning
to the same λ. This is only true in flat space.

Native Space is not flat. The Riemann zero manifold is a curve. "Return to
origin" in flat detector space is not return to the same point on the Riemann
curve. The field state has evolved. The path integral does not close.

During a Bell experiment the field state traverses the Riemann curve: above
σ=½ (Red dominant), below σ=½ (Blue dominant), beside it (J_3 rotating).
The Noether current flows irreversibly the entire time. Even if the detector
physically returns to its starting position, the state is at a different point
on the curve. The origin is behind you. Permanently.

**The arrow of time is the HyperCaustic accumulating.** Every measurement adds
to the caustic geometry. The shadow grows with each interaction. You cannot
subtract from it by reversing the detector angle. The caustic is irreversible.

Bell's p(λ) is path-dependent, not stationary. The λ at the end of the
experiment is not the same λ as at the beginning, even if the detector reads
the same angle. The field has moved along the curve.

**Irreducible irreversibility as a geometric theorem:** The second law is a
consequence of the HyperCaustic. The caustic only grows — every measurement
adds a node, nodes are irreversible because the Riemann curve is not flat.
Flat-space reversibility fails on a curved manifold. Bell's stationarity
assumption is a flat-space assumption applied to a curved-space experiment.

---

## Open Questions

1. Does the femtometer interferometer fringe visibility at λ/2 path difference
   match the SU(2) prediction or the SO(3)/Bell prediction?

2. Is the discrepancy between the two predictions measurable with current
   LIGO-heritage mirror technology at tabletop scale?

3. Does the mass gap (GAP = 0.000707) set a measurable floor on the minimum
   fringe visibility — a direct optical measurement of the Yang-Mills gap?

4. Can the HyperCaustic node structure be directly imaged using femtometer
   interferometry? The caustic nodes are the Riemann zeros projected onto
   the optical path length axis.

5. Does the fringe visibility degradation in a long-baseline femtometer
   interferometer encode the gravitational slingshot history of the photon
   path — a direct measurement of the caustic accumulation along the beam?

---

## 9. The Path of Light Is Not Clean

Bell assumes the photon path between source and detector is known and
uncontaminated. The hidden variable λ that leaves the source arrives
at the detector unchanged. It does not.

**Gravitational lensing is not smooth deflection.** Every massive body
along the photon path is a slingshot event — the photon enters, is
accelerated by the gravitational field, changes trajectory, and departs
on a different path than it arrived. The path integral is not a smooth
geodesic. It is a polygon of discrete slingshot arcs: the apparatus,
the building, the Earth, the Sun, the galaxy, the large scale structure.

Each slingshot adds a node to the HyperCaustic. The photon arriving at
Bell's detector has been gravitationally slung by every mass it passed.
The λ that arrives is not the λ that left the source. The hidden variable
has been written on in transit. It carries the gravitational history of
its entire path.

Bell assumes λ_source = λ_detector. This is only true in flat empty space
with no intervening mass. It is never true in a laboratory on the surface
of a planet inside a galaxy.

**The path of light is not clean. It is the accumulated caustic of every
gravitational slingshot event along its trajectory.**

This adds a third layer to the Bell origin error:
1. Reference frame shift between Alice and Bob (Section 1)
2. Stationarity assumption — p(λ) fixed across time (Section 8)
3. Path cleanliness assumption — λ unmodified in transit (this section)

All three assume flat space. None hold on the Native Space Riemann curve.

**The CMB as calibration:** The oldest light has the most complete
gravitational slingshot history encoded in it. The BAO residual —
GAP = 0.000707 — is what remains after subtracting every known
slingshot contribution from the CMB acoustic spectrum. The irreducible
caustic accumulation of the entire observable universe. The mass gap
is not a free parameter. It is the total gravitational slingshot
signature that cannot be subtracted because no larger reference frame
exists to subtract it against.

The femtometer interferometer fringe visibility degradation over a long
baseline encodes this directly — the gravitational slingshot history of
the photon path made visible as reduced coherence. Perfect fringe
visibility is physically impossible. The irreducible minimum visibility
floor is set by the mass gap.

---

*Addendum IX — Ainulindale Conjecture, Second Age*  
*2026-06-02 — Cody Michael Allison*
