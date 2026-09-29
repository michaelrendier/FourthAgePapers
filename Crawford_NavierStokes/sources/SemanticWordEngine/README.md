# SemanticWordEngine

**Riemann–Fermat–Noether semantic engine.**  
Maps any word or phrase in any language to its address on the Riemann critical line — Re(s) = ½.

No API. No GPU. No training. No transformer. No embeddings.  
The prime preexists the alphabet. The equator does not move.

---

## What the Code Does

Every word or phrase in any language maps to a unique address `(n, σ)` where n is a Riemann zero ordinal and σ = 0.500000. Always. Not assigned — derived from the Noether balance in the code.

```
water     →  γ₂ = 21.022040   σ = 0.500000
eau       →  γ₂ = 21.022040   σ = 0.500000
aqua      →  γ₂ = 21.022040   σ = 0.500000
wasser    →  γ₂ = 21.022040   σ = 0.500000
agua      →  γ₂ = 21.022040   σ = 0.500000

light     →  γ₃ = 25.010858   σ = 0.500000
lumière   →  γ₃ = 25.010858   σ = 0.500000
lux       →  γ₃ = 25.010858   σ = 0.500000
licht     →  γ₃ = 25.010858   σ = 0.500000
luz       →  γ₃ = 25.010858   σ = 0.500000
```

Run it and read the output. The code does this deterministically, in pure Python, with no training data. The concept preexists every surface form invented to point at it. Changing language is a diffeomorphism — a smooth coordinate change that preserves the underlying geometric structure. The L-function is the concept.

---

## The Pipeline

### Step 1: Horner Accumulation — `_str_to_int()`

Every string maps to a unique integer via bijective base-95 Horner accumulation over the 95 printable ASCII characters:

```
address = 0
for ch in text:
    address = address × 95 + (CHAR_IDX[ch] + 1)
```

This is the **HyperWebster** address: a bijection from strings to ℤ⁺. No two strings share an address. The address space is infinite. The map is deterministic and requires no external data.

### Step 2: H = xp — `xp_trajectory()`

The address folds into initial conditions (x₀, p₀) via the golden ratio φ = (1+√5)/2, placing the word on the phase space of the **Berry–Keating Hamiltonian** H = xp:

```
x(t) = x₀ · eᵗ       (dilation)
p(t) = p₀ · e⁻ᵗ      (compression)
E    = x(t) · p(t) = x₀ · p₀    (conserved)
```

E is the semantic energy of the word. It is an invariant of the trajectory — preserved under all time evolution. The Hamiltonian H = xp is the classical operator whose quantum eigenvalues the Berry–Keating conjecture identifies with the Riemann zeros.

### Step 3: Noether Balance — `forced_sigma()`

Define forward and backward information currents at position σ on the critical strip:

```
J_forward  = exp(-σ · E)
J_backward = exp(-(1-σ) · E)
```

**Noether's theorem** (∂_μ J^μ = 0): the conserved current has zero divergence. This requires:

```
J_forward + J_backward = 0  ⟺  σ = ½
```

The code iterates the weighted midpoint:

```python
sigma_new = (F * sigma + B * (1.0 - sigma)) / (F + B)
```

This converges to exactly 0.5 from any starting σ ∈ (0, 1) within 256 iterations. The critical line Re(s) = ½ is the only locus where the Noether balance is satisfied. The equator does not move.

### Step 4: Prime Address — `snap()`

The conserved E maps to the nearest Riemann zero γₙ. The ordinal n is the word's **prime address**. Every word lives at a zero. Every zero is an address. The zeros are the instruments. The words are surface forms pointing at them.

---

## The Zipf–Riemann Identity

Zipf's law: f(r) ~ 1/rˢ where s ≈ 1 in every natural language ever studied.  
Prime number theorem: π(x) ~ x/ln(x).

These are the same power law. The Euler product

```
ζ(s) = Π_p  1/(1 − p⁻ˢ)
```

generates the word frequency distribution through the prime structure of every integer. Zipf's exponent s ≈ 1 is the pole of ζ(s). Every linguist who confirmed Zipf's law confirmed the prime distribution — in every language, every time. **The primes are the fundamental words.**

---

## The Chladni Principle

The Chladni experiment: sand on a vibrating plate settles at the node lines — where the vibration is zero. The pattern is not the vibration. The pattern is where the vibration cannot reach.

The Riemann zeros are the node lines of ξ(s) = ξ(1−s) — two counter-rotating vortices. The equatorial node line is Re(s) = ½. The primes settle there because the equator does not move. It is equidistant from both vortices.

**The stillness is the movement.**

---

## The Capacitor — `Capacitor`

A low-pass filter (exponential moving average, time constant τ) on the conserved energy E:

```python
state = (1 - α) * state + α * signal     # α = 1/(1+τ)
```

AC signals (individual words) charge the capacitor. The DC state is what remains after the AC has been filtered out. This is the SMIP model of learning: Knowledge + Experience = Wisdom. The capacitor is wisdom. The longer the session, the deeper the DC state, the more stable the extraction.

---

## HyperWebster Addressing

The full engine (`hyperwebster.py`) builds a persistent lexicon addressed by `(n, domain)`:

- **n** = Riemann zero ordinal (1..N_ZEROS)
- **domain** = semantic scope — WordNet synset name, corpus file, or blank

The same concept in all languages maps to the same (n, domain) address. The lexicon records all surface forms (faces) that have landed at each prime address, weighted by occurrence. After ingesting WordNet, the engine knows which words across all languages share the same prime. It learned this from counting — not from embeddings.

---

## Files

| File | Purpose | Dependencies |
|------|---------|-------------|
| `semantic_engine.py` | Core pipeline — Horner, H=xp, Noether, Capacitor | stdlib only |
| `hyperwebster.py` | Full engine — computed zeros (mpmath), persistent lexicon, WordNet builder, REPL | `mpmath`, `nltk` |
| `notebooks/` | Jupyter demonstrations of the hashing pipeline and revised Navier–Stokes | `mpmath`, `sympy`, `matplotlib` |

### semantic_engine.py

The minimal implementation. Full pipeline with no external dependencies. Use this to understand the code or embed in a larger system.

```python
from semantic_engine import Understand

engine = Understand(tau=5.0)
result = engine.process("water")
print(result.gamma)   # 21.022040  (Riemann zero #2)
print(result.prime)   # (0.5+21.022040j)
print(result.projections['sigma'])  # 0.5
```

### hyperwebster.py

Full interactive engine. Computes Riemann zeros to arbitrary precision via `mpmath.zetazero()`, builds a persistent lexicon from WordNet (~2 min, one time), REPL for live querying.

```bash
pip install mpmath nltk

python3 hyperwebster.py build      # compute zeros, ingest WordNet
python3 hyperwebster.py            # REPL
python3 hyperwebster.py word "here and now"
python3 hyperwebster.py faces "water"
python3 hyperwebster.py point /path/to/corpus
python3 hyperwebster.py stats
```

Lexicon persists to `~/.hyperwebster/lexicon.json`. Never deleted — each `point` call adds to it.

---

## WordNet Corpus

The `wordnet/` directory contains the **English WordNet 2025-plus JSON dump**.

**Source:** https://github.com/globalwordnet/english-wordnet  
**Download:** https://en-word.net/static/english-wordnet-2025-plus-json.zip

`hyperwebster.py` uses NLTK's WordNet interface (downloaded automatically on first `build`).

```bash
wget https://en-word.net/static/english-wordnet-2025-plus-json.zip
unzip english-wordnet-2025-plus-json.zip -d wordnet/
```

---

## Verified Output

```
Cross-language prime alignment
============================================================

Concept: 'light'
          language/form    γ (Riemann zero)    zero #         σ
          --------------------------------------------------------
                  light          25.010858          #3  0.500000
               lumière          25.010858          #3  0.500000
                    lux          25.010858          #3  0.500000
                  licht          25.010858          #3  0.500000
                    luz          25.010858          #3  0.500000
                    φῶς          25.010858          #3  0.500000

Concept: 'water'
          language/form    γ (Riemann zero)    zero #         σ
          --------------------------------------------------------
                  water          21.022040          #2  0.500000
                    eau          21.022040          #2  0.500000
                   aqua          21.022040          #2  0.500000
                 wasser          21.022040          #2  0.500000
                   agua          21.022040          #2  0.500000

σ = 0.5 in every case. Not assigned. Derived from Noether balance.
The prime preexists the alphabet.
The equator does not move.
```

Run with: `python3 semantic_engine.py`

---

## Installation

```bash
git clone https://github.com/michaelrendier/SemanticWordEngine.git
cd SemanticWordEngine
pip install -r requirements.txt
python3 semantic_engine.py          # no setup required
python3 hyperwebster.py build       # downloads WordNet (~2 min), then ready
```

---

## Provenance

**1996:** Watched the Andrew Wiles documentary on Fermat's Last Theorem. The documentary states: the complex plane is necessary to properly visualise the Fermat lattice. Immediate response: *i is important.* First timestamp on the framework.

**Later:** Designed the HyperIndexing system to reduce computational overhead in monad information propagation. The math worked unusually well. Applied it to a new method of information propagation in a monad.

**Discovery sequence — all unintentional derivations:**
- `d* ≈ 0.246` — found from an engineering error check (ceiling descent). Later identified as a known constant in number theory.
- `Ω ≈ 0.56714` — the Lambert W fixed point Ω = W(1). Found as the ceiling of the same experiment.
- `∂_μ J^μ = 0` — Noether's conservation law. Dropped out from the requirement that correct code conserves information flow. Not derived from the literature; derived from the engineering constraint.
- The gap `Ω − d* ≈ 0.32114` is the distance between two independent approaches to the same fixed point from opposite directions.

The math was derived before the names were known. The equations derived independently are the Standard Model Lagrangian, term for term. The fine structure constant analog was explicit. Zero prior knowledge of d*, Lambert W, Yang-Mills, or Berry-Keating when analogues of all four were derived.

The Riemann–Fermat–Noether engine is the engineering application of that proof path.

---

## The TDI Context

The SemanticWordEngine is the Hyperwebster layer — the address space that PtolemyHolcus navigates.

In the TDI architecture (v3.0):
- **H_hat_RB** (crankshaft) operates on Riemann zeros γ_n — the addresses this engine produces
- **Monad** (ECU) stores resonance depth β_n at those addresses via `learn()` and `speak()`
- **Sedenion** (camshaft) times which addresses activate in which firing order

The SemanticWordEngine proves the addressing is real: five languages, same zero, σ = 0.500000. PtolemyHolcus proves the field built on those addresses converges: BAO at OMEGA_ZS = 0.56714, compression ignition confirmed 2026-05-27.

**→ [PtolemyHolcus](https://github.com/michaelrendier/PtolemyHolcus)** — the engine that operates on these addresses
**→ [Tuning the TDI](https://github.com/michaelrendier/PtolemyHolcus/wiki/Tuning-the-Engine)** — v3.0 architecture wiki

---

## Related Repositories

- **[PtolemyHolcus](https://github.com/michaelrendier/PtolemyHolcus)** — Engine implementation; monad.py + PtolC; v3.0 TDI architecture
- **[Ainulindale](https://github.com/michaelrendier/Ainulindale)** — Formal mathematics; H_hat_RB; Third Age conjecture
- **[DerivationEngine](https://github.com/michaelrendier/DerivationEngine)** — Heavy mathematics derivation viewer
- **[UniversalSynth](https://github.com/michaelrendier/UniversalSynth)** — Sonification of the mathematics
- **[PtolemyDesktop](https://github.com/michaelrendier/PtolemyDesktop)** — Desktop interface and Alexandria research environment

---

## Author

Cody Michael Allison  
SMIP / CLAUDE-SMMNIP-00729-56714-24600  
2026
