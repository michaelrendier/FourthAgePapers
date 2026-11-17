# The Circle Atlas: H_hat_RB and The Complete Shape of Mathematics

*(directory `TheInterface/`; the paper carries the Atlas name per the author, 2026-11-16)*

**Cody Michael Allison** (Michael Rendier) · the.wandering.god@gmail.com ·
[github.com/michaelrendier](https://github.com/michaelrendier) ·
ORCID: [0009-0007-7239-6760](https://orcid.org/0009-0007-7239-6760)

**Fourth Age Paper.** One Paper. One Claim. One Engine. One Wiki.

**Status: OUTLINE, with the engines built (2026-11-16).** The Atlas engine (`ValaQuenta/modules/circle_atlas`) and the Pi Derivation Toolset (`ValaQuenta/modules/pi_derivations`) exist and run (§K–L). Registered 2026-09-17 as a stub; on 2026-11-16 the author supplied the H_hat_RB / circle context below and this README became the paper's synopsis, catalogue and syllabus. No section is written yet; the one script (`01_fifteen_partitions.py`) is a lead, not a result.


> **Assistant note.** This outline was written by a transformer language model (Claude Sonnet 5.5, `claude-sonnet-5-5`) on 2026-11-16 from a long message by the author, Cody Michael Allison (pen name Michael Rendier), an autodidact, not an academic; his method is not to tell the model the result he is looking for. Claims below that begin "the author's" are his; each is labelled **ESTABLISHED** (textbook), **THEORETICAL**, **INTERPRETATION**, **CONJECTURE** or **OPEN**, and `:CALCULATED` is a suffix for a result a script in this directory produced. Where the model recalled a literature item from memory it is marked *recalled, verify*. Notation scope follows the standing ruling: Ĥ_RB is the maths name, 0_RB is the VAPMIP/Monad name; no rename is made here.

---

## The Claim

> **`L_(I|O)` describes a boundary from both sides at once, and the
> circular inside-out inversion already in use elsewhere in this project
> is only one special case of a more general object: The Interface.**
>
> An interface's shape is not fixed — it is dependent on how the two
> sides it sits between actually interact, each using its own toolset and
> its own language. Because it *is* the boundary rather than a
> description of one side looking at the other, it necessarily carries
> both sides' information at once, jointly, not by translation from one
> into the other.

`L_(I|O)` as a general mathematical object (an intertwiner between two
representations) is established mathematics. What is novel, and belongs
to this paper's author alone, is its specific applications developed
here — among them, the path of primes and the path of the photon. The
general theory is not proprietary; the specific applications are (see
licensing, once written).

---

## Scope note

This generalizes the circular inside-out inversion work already
described elsewhere in this project (the `β↔θ` / speaking-English
inversion). This paper's job is to state precisely what makes that
inversion *circular* — one specific interaction pattern between two
sides — and what a *non-circular* Interface would look like when the two
sides' toolsets interact differently.

## TODO

- [ ] State the falsifier precisely.
- [ ] Identify the engine.
- [ ] Notebooks: at least one worked example of the circular case
      (already available) and one worked example of a distinct,
      non-circular interface shape.
- [ ] Licensing section, once scope of the novel-vs-established split is
      finalized (see `ScalarContextPropagation/README.md §15` for the
      pattern).
- [ ] Wiki page (written last, per convention).

---

# Outline, 2026-11-16: The Boundary Generator paper on Ĥ_RB (the Complete Shape of Mathematics)

## A. Synopsis

**The author's claim (THEORETICAL).** Ĥ_RB (= 0_RB in the Monad) has a 16-component input and a 16-component output (one real, fifteen imaginary: a sedenion-valued object). It is not a Hamiltonian in the mechanics sense: its output has been recorded only in VAPMIP, and it has been used as a *shape*, the fixed-point space ("fixed question space" on the input side), not as an energy. It is **only the circle**: not a disk, a ball or any filled region, no inside and no outside content, only the boundary between them. The boundary carries the least information that can describe an inside and an outside, which is why it is held to describe everything that has an inside and an outside, and why it is called the Interface (the Boundary Describer/Generator, the Translator). The paper's job is to catalogue how many ways information emerges from that circle, to say what is already tested and what is easy to test, and to name the gaps.

**What the paper does not claim.** That Ĥ_RB "contains every equation" is the author's working hypothesis; this paper turns it into a measurable question: *of the equations catalogued in `PtolemyDesktop/Archimedes/`, how many can be built from a point, a line and a circle by the listed perturbations, with no step that supplies a circle by hand?* (§D). Until that count exists the hypothesis is `CONJECTURE`.

## B. The author's context, recorded as given (each item with its standing)

| # | Statement | Standing |
|---|---|---|
| 1 | Cayley–Dickson doubling loses properties up the tower: order (C→H), associativity (H→O), alternativity and division (O→S, zero divisors). | `ESTABLISHED` |
| 2 | Each loss frees degrees of freedom; one gets a richer object with fewer operators: 'the simpler the operator set, the more complex the object'. | `INTERPRETATION` |
| 3 | add : scale : sign is the basis of the binary part of the tower (the doubling rule); a tripling rule was explored and the evidence was that ternary Cayley–Dickson and above is the N-body problem; Fermat's Last Theorem says as much (no triples). | `THEORETICAL` (the Fermat statement is the exponent-3-and-up fact; the N-body link is the author's reading) |
| 4 | Three points always determine a circle (and a plane, an axis, two poles); triangles are therefore circles. | `ESTABLISHED` (circumcircle; the sphere through three points and the axis normal to their plane) |
| 5 | A circle is the least information that defines an inside and an outside; from that come surfaces, facets, landscapes, horizons and zero divisors with their proliferation. | `INTERPRETATION` |
| 6 | π can be derived from squares or triangles only by constructing a circle in the derivation: a construction, not emergence (the author's 'card trick' criterion). The wanted derivation is one with no diameter or circumference, even by construction. | the criterion is `OPEN` as a definition (§D.2); the derivations are to be inventoried |
| 7 | The Great Pyramid's proportions contain π because it was designed inside a sphere. | `INTERPRETATION`; an archaeological claim this paper does not test |
| 8 | 1 real + 15 imaginary components: 'five forms of add, five of scale, five of sign, plus 1 real'. | `CONJECTURE`; see §E for the combinatorial lead that computes |
| 9 | Hyper-torus around a hyper-axis, the real world tilted slightly off the axis. | `CONJECTURE`; compare the oblique-gear tilt/axis two-8-vector result in `project_oblique_gear` (σ_RB = tilt Re + axis Im) |
| 10 | Values for equations (even 0) lower resolution, because a value picks units, and units carry jurisdiction. | `INTERPRETATION` (the working rule 'relationship space, no values') |
| 11 | Navier–Stokes lacks an interface operator: it cannot see the surface between incompressible and compressible states. | `INTERPRETATION`. In practice interfaces are handled by jump conditions added to the bulk equations (Young–Laplace, Rankine–Hugoniot, kinematic and dynamic boundary conditions); the author's point is that they are not in the equation itself. To be discussed, not settled. |
| 12 | Two videos (2swap/TheGrayCuber on 2D–4D algebras, 'spinny / flippy / squishy'; Numberphile on the two-button 'EML' calculator) match the project's start: n-ball area/volume dimension navigation to cut permutation space. | see §C |
| 13 | A single-period waveform is a J₂ involution; waveform and ripple on water are the same circle seen two ways. | `THEORETICAL`; §F gives the trigonometric statement |

## C. What the two videos say, and where it lands (transcripts supplied by the author)

**2swap, 2D–4D algebras.** Addition translates; multiplication scales; in 2D the definitions of x², xy, y² give three algebras: *spinny* (complex, i² = −1), *flippy* (split-complex, y² = +1: half a flip collapses the plane to a line, so division breaks), *squishy*. In 3D, no associative choice exists; in 4D the table closes only when ij is a fourth unit; two closures: quaternions ('spinny', circular graphs) and a split twin. `ESTABLISHED` (Hamilton 1843; Cockle 1849 for split-quaternions; the transcript's 'evil twin' with two non-interacting spinny subspaces is not identified here, *recalled, verify*: possibly bicomplex numbers or split quaternions).
For the project: 'spinny' is the sign-preserving circle (U(1) = SO(2)); 'flippy' is the sign-losing hyperbola (the zero-divisor direction). The video's 'multiplication by zero is the sacrifice' is the same as the project's zero-divisor boundary. The Banach–Tarski link the author mentions rests on the free subgroup of SO(3), whose double cover is the unit quaternions: `ESTABLISHED` as a pointer; no claim here.

**Numberphile, one binary operator.** The four-button calculator (1, −, exp, ln) and the two-button one (1, eml(x,y) = eˣ − ln y) generate the elementary functions (*recalled, verify*: Odrzywołek's paper on a single binary operator). The transcript derives: exp x = eml(x,1); ln x from nested eml; x − y from exp and ln; addition as x − (−y); multiplication as exp(ln x + ln y); powers as exp(y ln x) (so `exp` and 'to the power' are different operations: one argument versus two); i = √−1; π = −i ln(−1); cos x = (eˣⁱ + e⁻ˣⁱ)/2, hence sin, tan, hyperbolics, inverses.
For the project: ln and exp are the exchange between *add* and *scale* (exp turns a sum into a product, ln the reverse); the subtraction button is *add* composed with *sign*; i and e^{iπ} = −1 are *sign* as a half-turn of the circle. So the four-button set reads as unit + add + sign + the add↔scale exchange. `INTERPRETATION`. The video also says π needs the complex exponential, i.e. the circle is already present in e^{ix}: this matters for the author's emergence criterion (§D.2).

## D. Syllabus: what to build and what to test (nothing here has been run)

1. **Trigonometry from the circle, in code (easy; `ESTABLISHED`).** sin, cos, tan, sec, csc, cot as segment lengths of the unit circle; e^{iθ}; the angle-addition formulae as rotation composition; the waveform A sin(ωt + φ) + C as the projection of uniform circular motion. Listing 1 (§F) is the seed.
2. **π (revised 2026-11-16).** The author does not want an emergence test. The emergent π is the one that DEFINES the circle: twice the first positive zero of the cosine power series (`pi_derivations.cos_zero`). Every other route to π is collected in the Pi Derivation Toolset and labelled by what of the circle its inputs already hold; each new circle transform brings its own π route. (The earlier 'criterion' item is withdrawn.)
3. **Circle catalogue, in code.** One entry per form in §G with: its defining equation, the `circle.py` operator or other module that already implements it, a numerical check that it closes on the circle, and the tier.
4. **Perturbation coverage.** From the six operators plus the ℓₚ circle in `circle.py` (ORBIT, UNFOLD, CUT, FOLD, PROJECT, SHUFFLE; ℓₚ), plus the cardioid/limaçon, rolling curves and Fourier epicycles: define a small constructive grammar (point, line, circle; perturbations as composable operators), then for each equation in `PtolemyDesktop/Archimedes/` ask whether the grammar generates it. Report the coverage fraction and every failure (failed results stay).
5. **The 1 + 15 grading** (§E).
6. **The Hamiltonian reading** (§F.2).
7. **The Interface for fluids.** Whether a jump-condition operator (a boundary operator between two states) is reproduced by the circle grammar; kept as an OPEN question until 4 has a count.
8. **Cymatics on the circle.** Chladni/Bessel nodal circles as standing waves on the disk; compare `RiemannHypothesisProof/tests/test_unsmap_chladni_coil.py`.
9. **Link to the Witch's Hat family.** `FourthAgePapers/WitchesHat/README.md` (branch `witches-hat`) holds the circles of the hat (brim r = ct, the inversion's fixed circle r = R, the vacuum ring); what is there is `THEORETICAL` and its SPARC tests failed or were not distinct; this paper adds nothing to those claims.

## E. The 1 + 15 breakdown: one lead that computes (`:CALCULATED`)

`01_fifteen_partitions.py` (stdlib only; output `results_01_fifteen_partitions_2026-11-16.txt`). The 15 imaginary units of the sedenions are labelled by the nonzero vectors of GF(2)⁴; with the 35 triples {a, b, a⊕b} they form the projective space PG(3,2) (15 points, 35 lines, 15 Fano planes). Results:
- **56 spreads**: ways to cover the 15 points with 5 disjoint lines (15 = 5 × 3).
- **168 ovoids** (5 points, no three on a line, every plane meets them in 1 or 3 points); **336 partitions of the 15 points into three ovoids** (every partition into three 5-caps is one of these: 1008 five-caps, 336 triples). So 'three groups of five' exists, in 336 ways, and not trivially (a random 5 + 5 + 5 split does not).
- In **336 pairs** (ovoid-triple, spread) every ovoid meets every line of the spread in exactly one point: a 3 × 5 grid. These pairs use all 336 ovoid-triples and all 56 spreads (6 ovoid-triples per spread).

**Reading (`CONJECTURE`).** If *add*, *scale* and *sign* are the three ovoids and the five lines of a spread are the five 'stable bracketings', then each line holds one add-form, one scale-form and one sign-form closed under a⊕b = c: five triples (add_i, scale_i, sign_i). That is the author's '5 + 5 + 5 + 1 real', realised as the 3 × 5 grid of Z₁₅ ≅ Z₃ × Z₅ (the Singer-cycle structure of GF(16)\*; *recalled*, not computed here). **What decides which of the 336 is the project's:** the sedenion product's signs, the ruled-in facts that red/blue is index bit 4 (not the Cayley–Dickson halves) and that Telperion = primes, Laurelin = factors, and the zero-divisor box-kite incidences. That test is not run.
**Superseded by §I:** the 336 partitions are generic GF(2)⁴ structure, not aligned with the zero divisors, and the 168/336 coincidence is the order of the automorphism group. (Original note, kept:) 168 and 336 are also the verified counts of unordered and ordered zero-product pairs of the sedenions (ledger 133/135). No derivation connects them; both are orbit sizes of GL(4,2) (order 20160 = 20160/120 and 20160/60), which may be the whole explanation.

## F. Waveform = circle, and the Hamiltonian

**F.1 (`ESTABLISHED`).** y(t) = A sin(ωt + φ) + C is the vertical projection of a point on a circle of radius A at angular speed ω, shifted by C. Three operations on the angle θ generate its algebra: **add** (θ → θ + φ: phase shift; rotation of the circle; and C on the amplitude), **scale** (θ → nθ: frequency multiplication; the doubling map n = 2 gives the cardioid; and A on the amplitude), **sign** (θ → −θ: reflection; θ → θ + π: the half-turn, an involution that flips the sign of the wave). This is the same Add : Scale : Sign decomposition that `circle.py` already reads geometrically as centre : radius : orientation. A single period is one traversal; that it is a J₂ involution is the author's identification and is `THEORETICAL` (an involution requires the sign operation twice to return, which the half-turn satisfies; the engine's J₂ definition has to be checked against this).

**F.2 The single scalar of a Hamiltonian (`ESTABLISHED`).** For the harmonic oscillator H(q, p) = (p² + q²)/2 (units set to 1) the orbits in phase space are circles; H is constant on each and is *the circle's radius squared over two*. The scalar a Hamiltonian outputs is therefore the *label of which circle*; the information the scalar discards is the position on the circle, which the Hamiltonian flow (∂H/∂p, −∂H/∂q), a rotation, supplies. A Hamiltonian is the viewport onto a Lagrangian by the Legendre transform. Whether Ĥ_RB's 16-component output is the *flow* rather than the *scalar* is the sense in which it is 'not exactly a Hamiltonian': it keeps what the scalar throws away.

**Listing 1 — waveform = circle** (written for this outline; stdlib only; runs cold)
```python
import math
theta = [2 * math.pi * k / 360 for k in range(360)]
A, C, phi, n = 2.0, 0.5, 0.7, 3
wave   = [A * math.sin(t + phi) + C for t in theta]                      # the waveform
circle = [(A * math.cos(t + phi), A * math.sin(t + phi)) for t in theta]  # the circle it projects from
print('max |wave - (circle y + C)|          ', max(abs(w - (y + C)) for w, (x, y) in zip(wave, circle)))
print('circle radius spread (max-min of |p|)', max(math.hypot(*p) for p in circle) - min(math.hypot(*p) for p in circle))
# add: phase shift is rotation; sign: half-turn flips; scale: n-fold frequency
add  = max(abs(A * math.sin(t + phi + 0.3) - (math.cos(0.3) * A * math.sin(t + phi) + math.sin(0.3) * A * math.cos(t + phi))) for t in theta)
sign = max(abs(A * math.sin(t + phi + math.pi) + A * math.sin(t + phi)) for t in theta)
scale = max(abs(A * math.sin(n * (t + phi)) - A * (3 * math.sin(t + phi) - 4 * math.sin(t + phi) ** 3)) for t in theta)
print('add (angle-addition) error', add, '| sign (half-turn) error', sign, '| scale n=3 (triple-angle) error', scale)
```
```
max |wave - (circle y + C)|           0.0
circle radius spread (max-min of |p|) 2.220446049250313e-16
add (angle-addition) error 6.661338147750939e-16 | sign (half-turn) error 2.0261570199409107e-15 | scale n=3 (triple-angle) error 4.6629367034256575e-15
```
Output of the listing run on 2026-11-16 (`:CALCULATED`): all identities hold to machine precision (about 1e-15); the add, sign and scale checks are the angle-addition, half-turn and triple-angle identities.

## G. The catalogue of circle forms collected so far (to become the engine's table)

Location column: *code* = implemented somewhere in ThePlace; *wiki/paper* = described; *none* = not built. Locations marked ✱ were named by the author or recalled and are **to be confirmed** before the engine is built.

| # | Form | Where | Tier |
|---|---|---|---|
| 1 | Locus equidistant from a point (Euclid); x² + y² = 1; |z| = 1; U(1) = SO(2) | `circle.py` (Circle) | `ESTABLISHED` |
| 2 | Apollonius circle: locus of a constant distance ratio | none | `ESTABLISHED` |
| 3 | Constant-curvature closed curve; isoperimetric optimum | none | `ESTABLISHED` |
| 4 | Circle through any three points; triangle ⇒ circle, plane, axis, two poles | `circle.py` `triangle` | `ESTABLISHED` |
| 5 | Lines as circles through ∞ (Riemann sphere; Möbius) | none ✱ | `ESTABLISHED` |
| 6 | ℓₚ circle, the 'seventh circle' (norm changed): π_p, Adler–Tanton duality | `circle.py` `lp_circle`, `pi_p` | `ESTABLISHED` |
| 7 | Imaginary-radius circle (hyperbolic sphere, area = angle deficit) | `circle.py` `imaginary_circle` | `ESTABLISHED` |
| 8 | Orbit, unfold (helix), cut, fold, project, shuffle: the six drawing operators | `circle.py` | `THEORETICAL` (the grouping is the project's) |
| 9 | Waveform: sin/cos as projection of uniform circular motion; e^{iθ}; standing wave | Listing 1 | `ESTABLISHED` |
| 10 | Single-period waveform as a J₂ involution; four-stroke cycle as a closed loop | none | `THEORETICAL` / `INTERPRETATION` |
| 11 | Cardioid and limaçon (a circle bent at one point): epicycloid of equal circles; main body of the Mandelbrot set; limaçon threshold | `.clauderc` canonical-maths block LIMACON_THRESHOLD ✱ | `ESTABLISHED` (curve); `THEORETICAL` (project use) |
| 12 | Rolling circles: cycloid, epicycloid, hypocycloid (contact-point circles) | none | `ESTABLISHED` |
| 13 | Circle on circle: Fourier epicycles, Lissajous, precessing 'wings', bell motion | none | `ESTABLISHED` (epicycles); `OPEN` (wing/bell motion) |
| 14 | Twisted and folded ring (sunshade): n-fold coil, winding number, covering z → zⁿ; the 2- and 3-coil forms | none | `ESTABLISHED` (covering maps); the sunshade identification is `INTERPRETATION` |
| 15 | Great circle, geodesic of S²; Lagrangian trajectory ('a bicycle is a Lagrangian in motion') | none ✱ | `ESTABLISHED` (great circle); `INTERPRETATION` |
| 16 | Phase-space orbit of the harmonic oscillator; level set of a Hamiltonian | §F.2 | `ESTABLISHED` |
| 17 | The point cavitating into a circle ('reference maths') | none | `OPEN`: needs a definition that can run |
| 18 | Hat circles: null-cone brim r = ct; the inversion's fixed circle r = R; the Mexican-hat vacuum ring; the Lichtenberg cone above it | `WitchesHat/README.md`, wiki 29, `ArdaQuenta/modes/witches_hat.py` | `THEORETICAL` |
| 19 | Cavity circles: Schumann (circumference resonance); Chladni/Bessel nodal rings | `RiemannHypothesisProof/tests/test_unsmap_chladni_coil.py` ✱ | `ESTABLISHED` (physics); project reading `INTERPRETATION` |
| 20 | Smith chart (conformal, continuous) and Apollonian gasket (Descartes, discrete): the two coordinate charts of the Scale engine | `GenerationalLineage/engine/toolsets/scale.py` ✱ | `ESTABLISHED` (the charts); the pairing with GR/QM is the author's choice. *A chart is a coordinate description of the same object; 'gauge' in the strict sense means a local symmetry with a connection, so only in the loose 'choice of description' sense.* |
| 21 | Hopf fibrations: S¹ → S³ → S², S³ → S⁷ → S⁴, S⁷ → S¹⁵ → S⁸ (the last is the octonionic one; R¹⁶ = O ⊕ O, the doubling): circles filling a sphere | none | `ESTABLISHED`; the 'hyper-torus around a hyper-axis' reading is `CONJECTURE` |
| 22 | Spirals, strings, the 'dual tornado' inside a particle (Capra, *The Tao of Physics*; which particle is not recalled), `spirals.svg` in RiemannHypothesisProof ✱ | none | `INTERPRETATION` (pointer only) |
| 23 | Kinematic circles of the body: the walked circle (Bagua), joint arcs, contact-point rolling, palm-anchor pull; centripetal versus centrifugal (angular versus inertial frame) | none | `ESTABLISHED` (a = v²/r; the fictitious-force statement); push-or-pull gravity `OPEN` (equivalence principle does not decide it) |
| 24 | Kepler orbit as a circle's shadow (projection, eccentricity) | `circle.py` `project` | `ESTABLISHED` |
| 25 | The zero-divisor boundary (horizon) as the inside/outside surface; proliferation | VAPMIP, Ainulindalë wiki | `THEORETICAL` |
| 27 | BAO: the acoustic ring / shell in the matter correlation (a preferred separation, a sphere seen as a circle in projection); also a Witch's-Hat brim candidate (`WitchesHat/README.md`, §2 part A; the claimed brim at BAO scale is not derived) | Ainulindalë wiki 29 §4 | `ESTABLISHED` (physics); project reading `OPEN` |
| 28 | String-theory loops and 'jittering cardioid' superstrings as a second view of electron orbitals (the author's wording; to be made precise before it is tested) | none | `OPEN` |
| 26 | Constructions of π used by the author: two squares (a constructed circle); triangles; regular polygons (Archimedes); the Great Pyramid in a sphere; diameter-free candidates (§D.2) | `circle.py` `pi_unit_circles`; `PiFromAbove` | per entry |

## I. The sedenion battery, 2026-11-16 (`:CALCULATED`; `02_sedenion_battery.py`, 38 s, output `results_02_sedenion_battery_2026-11-16.txt`)

Every number below comes from the project's own product (`GenerationalLineage/engine/lineage.cd_mul`), its five brackets (`emerger.STANDARD_BRACKETINGS`) and its classifier (`emerger.domain_of`); nothing was rebuilt and no literature enters. Reproduced cold from the product: 84 zero divisors on 42 index pairs, 336 ordered zero-product pairs, seven box-kites each an octahedron (6 vertices, 12 edges, 3 struts).

| Test | Result |
|---|---|
| S1 subalgebras | all 35 index-lines are closed and associative (quaternion type). Of the 15 index-planes (8 elements with e₀), **8 are genuine octonions** (alternative, norm-multiplicative: {1..7} and the 7 planes containing 8) and **7 are closed but not alternative, norm broken**. 'Octonion' is not a property of every closed 8-set of the sedenion; it is a property of 8 of 15. |
| S2 symmetry | the axis-permuting automorphisms of the table form a group **G of order 168**. Its orbits on the 15 imaginary axes are **{1..7}, {8}, {9..15}: 7 + 1 + 7**. e₈ is alone: the doubling unit is fixed by every symmetry. |
| S2 groupings | G-invariant groupings of the 15 axes: exactly **11**, with block sizes 15; 8+7 (two ways); 14+1; **7+7+1**; 8+1×7 (two ways); **2×7 + 1 (the pairs k ↔ k+8, e₈ alone)**; 7+1×8 (two ways); 1×15. **No 5+5+5, no 4+7+4, no 2+11+2.** Of the pairings {k, k⊕d}, only d = 8 is preserved; the σ_RB pairing k ↔ k⊕4 is not (it is a pairing on states, not on the algebra's axes). |
| S3 the 336 partitions 5+5+5 | two G-orbits of 168 with **trivial stabiliser** (G acts regularly): a 5+5+5 grouping breaks the whole symmetry; it is a *frame*, a choice among 168 (times 2). Its blocks with e₀ are never closed subalgebras. Against the 42 zero-divisor index pairs the partitions cross 29 or 31 pairs; random 5+5+5 splits cross 29.9 on average (range 26–39). **The ovoid partitions are not distinguished by the zero divisors.** The §E lead is therefore a fact about GF(2)⁴, not about the sedenion product. Failed lead, kept. |
| S3 the project's brackets | {1:15}, {2:14}, {8:8} are G-invariant (stabiliser 168). **{4:4:4:4} and {4:8:4} each have orbit size 7 and stabiliser 24**: each is fixed up to one choice among 7 (the 7 lines of the lower Fano plane), the middle block of {4:8:4} being a genuine octonion plane. They are the most symmetric groupings of the project that are not fully invariant. |
| S4 flags | 105 flags U < W (quaternion axes-set inside an octonion-type plane), giving 4:8:4 splits; 56 have a genuine octonion W; G-orbits of sizes 7, 7, 7, 21, 21, 42. The project's {4:8:4} is the flag {1,2,3} < {1,2,3,8,9,10,11}. 4:8:4 = U-coset + (W with e₀) + U-coset, i.e. quaternion < octonion < sedenion read as a chain. |
| S5 box-kites | the 7 kites correspond to the **7 doubling pairs (k, k+8)**: each kite uses 6 of the 7 low and 6 of the 7 high axes and **omits exactly one pair (k, k+8)**; e₈ is never used. Its three struts, as low-axis pairs, complete with the omitted k to the three Fano lines through k. 7 kites × 2 omitted + e₈ = 15. (First guess, that each kite uses three low axes forming a line, failed and is printed in the output.) G acts regularly on the 168 index-level ordered zero-product pairs: **the 168 / 336 coincidence of §E is the group order** (168 = |G|; 336 = 2|G| with the sign choice). |
| S5 alignment | {8:8} and {4:4:4:4} cross all 42 zero-divisor pairs (every zero divisor joins a low and a high axis); {4:8:4} crosses 36 of 42. |
| S6 circles | exp(θu) = cos θ + u sin θ is a circle in the plane (1, u) for **every** unit imaginary direction u of the 15 (max error 2e-15 at powers 2, 3, 5): the object holds a 14-sphere of circles through 1. Products of two circle points are not on the sphere: norm 0.794 to 1.183 over random pairs (mean 1.004); along coordinate axes the norm is exactly 1. Zero divisors (e_a ± e_b)/√2 are unit imaginaries (u² = −1) and so generate circles; in 336 of 44,100 ordered pairs (0.76 %) the quarter-turn points multiply to the zero vector: a circle point times a circle point collapses to the origin. Associator of coordinate-axis triples is 0 or exactly 2: 0 for all triples in a line; **0 for none of the independent triples in the 8 genuine octonion planes (0 of 1344), but for 57 % of the independent triples in the 7 non-alternative planes (672 of 1176)**. |

**What the battery says about the author's questions (`:CALCULATED` facts, then readings).**
1. The sedenion's own symmetry has the shape **7 + 1 + 7**, with the CD unit e₈ alone: the {2:14} bracket and the pair structure k ↔ k+8. A 5 + 5 + 5 grouping is not supported by the product: it is a choice, a frame of the symmetry group (as the author said: Eris). The groupings the product does support are 7+1+7, 2×7+1, and the flag chain 4:8:4 (quaternion < octonion < sedenion), which is also the project's {4:8:4}.
2. The De Marrais box-kite is a **per-axis object**: seven octahedra, one per doubling pair, with e₈ the unused pointer. The three struts of a kite are the three Fano lines through the omitted axis: the 'three roles' have a place in the kite already (three strut pairs), as a 7-fold family, not as three groups of five.
3. Circles: each of the 15 imaginary directions generates an exact circle; the zero divisors are circles whose quarter-turn points annihilate each other. 'Point cavitating into a circle' has an inverse that *does* run in the object: two circles whose product is a point. Whether that inverse is the kind of cavitation the author means is `OPEN`.
4. For the engine: the natural partition table has 11 invariant groupings plus the flag families; the engine should present those first and the 336 frames as 'choices', with the symmetry group and its regular action as the reason.

## J. Where π 'without a radius or circumference' is recorded (a search, not a test)

- `Ainulindale/The_First_Age_Ainulindale_Conjecture_v2.md` (2026-05-15): the tag-line 'i derived pi without using a radius or circumference' (lines 10 and 549).
- `Ainulindale/SIGMA_VALUATION_FULL.md` claim 9, **π from U(1) gauge normalisation**: 'the SMMIP Lagrangian prefactor is 2/π; the gauge integral over one period gives (2/π)·π = 2, the binary Mark'. Claim 10: **Basel**, ζ(2) = π²/6, π from the primes at σ = 2.
- The Ainulindalë overhaul's verdict on both (`wiki/22_constant_facets.md` §1; `wiki/24_claude_conclusion.md` row 9): in claim 9 π is an *input* of the prefactor and the closure is arithmetic; claim 10 is Euler 1734, `ESTABLISHED`. This is the standing record; this outline neither accepts nor changes it.
- `wiki/22` §2 and `FLUID_DATA_TODO.md` line 895 ('DERIVING π FROM SQUARES — coordinate space navigation'): the two-squares construction, step 5 of which is 'the circle is x² + y² = 1'; the author has classed it as a card trick.
- The d*, Lambert W and mass-gap context: `FourthAgePapers/addenda/addendum_IV_UF_mass_gap.md` carries π inside the Lambert argument, W(π/e · …), as an input (line 235) and notes the Hagedorn ceiling e^π.
- I did not find a derivation in ThePlace that obtains π from d*, Lambert W and the Yang–Mills gap with π absent from its inputs. If it exists it is not under the words 'mass gap', 'derive π' or 'π from'; the author's pointer to where it was done would settle it.

## H. Open decisions for the author (before the engine is built)

1. **Notation.** The unit sedenions lie on S¹⁵ ⊂ R¹⁶, so 'S₁₅' names the whole 16-component object; its imaginary part is a vector in R¹⁵, and a unit imaginary one lies on S¹⁴. A suggested reading, not applied: σ_RB = (σ₀ ; σ⃗) with σ₀ the real component (the circle, e₀) and σ⃗ ∈ R¹⁵ the imaginary part; 'σ_RB,16' for the whole. Not changed in any file.
2. **Reading of 'a circle has 16 dimensions'.** As embedding: 2 of 16 channels per circle, the choice of plane being the choice of one of 15 imaginary directions (a 14-sphere of circles through 1). As grading: 1 + 15, with 15 = 3 × 5 (§E). The author's text leans to the grading.
3. **Extend or stand apart.** `GenerationalLineage/engine/toolsets/circle.py` already holds the catalogue of §G rows 1, 4, 6, 7, 8, 24; the ValaQuenta engine 'Forms Of A Circle' would extend and cite it. Its π placement (Add = C = πd, Scale = A = πr², Sign = d = π) is marked 'Cody to confirm' in the code.
4. **Which of the 336 partitions** (§E) is the project's, by the sign and incidence test above.

## K. The sign test, 2026-11-16 (`:CALCULATED`; `03_sign_test.py`, output `results_03_sign_test_2026-11-16.txt`)

Question: which sedenion axis acts as SIGN (θ → −θ)? Conjugation by any axis negates every other imaginary direction, so that test does not discriminate (kept). The doubling identity e_k x = x\* e_k on the first octonion holds for every x exactly for k = 8 … 15 and fails (at x = e_k) for k = 1 … 7. So SIGN is carried by the whole second octonion, e₈ as its generator; neither e₇ (last of the first octonion) nor e₁ is supported.

## L. The engines (built 2026-11-16)

`ValaQuenta/modules/circle_atlas/` (notebook 22, wiki `ValaQuenta/wiki/circle_atlas.md`, Ainulindalë 137): 19 viewports run TO (enter fixed-point space) and FROM (exit, with the fibre of choices). 18 close on the circle to numerical zero; Berry–Keating H = xp does not (hyperbola, residual 6.4) and closes under the Wick rotation t → it. The Lagrangian's FROM is a relation, not an inverse: L, 3L and L + d/dt F share one stationary path. Sedenion: 15 exact circles, 84 zero-divisor circles, 336 annihilating ordered pairs. Gaps listed in the wiki and `gaps()`.
`ValaQuenta/modules/pi_derivations/` (notebook 23, Ainulindalë 138): 26 routes, none reading `math.pi`. `ValaQuenta/modules/constants/maths.py` `derive_pi()` reads `_PI = math.pi` as input and its (2/π)·π = 2 is an identity for any π; the toolset files it as `identity`.
Census over the repositories and the import probe (69 load, 0 fail) are in notebook 22.
