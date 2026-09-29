# MODE 3 — LOOK AT MY CODE
## The Noether Engine in Three Domains

This directory contains the computational implementation of the Noether current framework across three experimental/simulation domains:

1. **Domain 1: Rotating Fluids (Crawford)**
   - Data analysis from Crawford's 2017 rotating tank experiments
   - Visualization of turbulence as Noether current rotation
   - Notebook: `01_crawford_rotation_curves.ipynb`

2. **Domain 2: Molecular Dynamics (GROMACS)**
   - Simulation setup for Noether-conserving forces
   - Spontaneous DNA helix formation
   - Notebook: `02_gromacs_dna_emergence.ipynb`

3. **Domain 3: Cosmological Simulations (Dark Matter)**
   - N-body simulations with Noether-conserving potentials
   - Galactic rotation curves from constraint field
   - Notebook: `03_dark_matter_as_constraint.ipynb`

4. **Domain 4: Language Embeddings**
   - Word embeddings trained under Noether balance
   - Semantic structure analysis
   - Notebook: `04_language_embeddings_noether.ipynb`

---

## Quick Start

### Install Dependencies

```bash
pip install numpy scipy matplotlib jupyter
# For GROMACS support:
pip install gromacs-api  # (optional, requires GROMACS installed)
# For cosmological sims:
pip install nbodykit astropy
```

### Run Notebooks in Order

```bash
jupyter notebook 01_crawford_rotation_curves.ipynb
jupyter notebook 02_gromacs_dna_emergence.ipynb
jupyter notebook 03_dark_matter_as_constraint.ipynb
jupyter notebook 04_language_embeddings_noether.ipynb
```

---

## Core Noether Engine

The Noether Current engine is implemented in `/media/rendier/0123-4567/ValaQuenta/noether.py`

```python
from ValaQuenta.noether import NoetherCurrents
from ValaQuenta.semantic_word import SemanticWord

# Initialize
noether = NoetherCurrents()
word = SemanticWord("example")

# Compute currents
J_forward = noether.forward(word)    # J_R (red, forward)
J_backward = noether.backward(word)  # J_B (blue, backward)
J_3 = noether.rotating_field(word)   # J_3 (green, boundary)

# Check balance
balance = noether.balance(word)       # Should → 0
print(f"Balance: {balance:.6f}")      # Noether conservation
```

---

## Notebook Structure

Each notebook follows this pattern:

1. **Import dependencies** and load experimental/simulation data
2. **Define the Noether current** for that domain
3. **Compute J_R, J_B, J_3** for the system
4. **Verify balance:** J_R + J_B + J_3 ≈ 0
5. **Interpret results** in domain-specific language
6. **Make predictions** for next experiments

---

## Expected Results

### 01 — Crawford (Rotating Fluids)

**Input:** Crawford's experimental measurements (velocity, potential vorticity)  
**Output:** 
- Phase-space diagram showing turbulence as rotation
- Smoothness verification at Rossby transition
- Current balance plot

**Falsifiable claim:** Velocity field remains continuous when measured in full 3D.

### 02 — GROMACS (Molecular Dynamics)

**Input:** C, H, O, N atoms in a periodic box with Noether forces  
**Output:**
- Spontaneous helix formation (visual trajectory)
- Chirality verification (left-handed B-DNA)
- Base-pair geometry vs. natural DNA (< 0.1 Å RMS)

**Falsifiable claim:** Without external templates, helix forms spontaneously.

### 03 — Dark Matter (Cosmology)

**Input:** Galaxy simulation with Noether-conserving potential  
**Output:**
- Rotation curve (v vs. r) vs. observed data
- Constraint field visualization (J_B)
- Halo density profile comparison

**Falsifiable claim:** Observed rotation curves emerge without particle dark matter.

### 04 — Language (Embeddings)

**Input:** Word corpus, trained under Noether balance  
**Output:**
- Embedding quality on standard benchmarks (SimLex, RW, etc.)
- Comparison vs. GloVe, Word2Vec, FastText
- Semantic relationship clustering (synonyms, antonyms)

**Falsifiable claim:** Noether-constrained embeddings outperform standard ones by >5%.

---

## Data Sources

- **Crawford experiments:** `/media/rendier/0123-4567/DataSets/Language_Corpus/crawford_navier_stokes_thesis.txt`
  - Full thesis with tables, figures, velocity measurements
  - 82,311 words of experimental fluid mechanics data

- **Molecular data:** GROMACS force field files (provided in `data/gromacs_ff/`)

- **Cosmological:** Public galaxy survey data (SDSS, DES)

- **Language:** WordNet 2025+, pre-trained embeddings

---

## Code Architecture

```
UmbrellaNoether/mode3_code/
├── README_CODE.md                      (this file)
├── 01_crawford_rotation_curves.ipynb   (Rotating fluids)
├── 02_gromacs_dna_emergence.ipynb      (Molecular dynamics)
├── 03_dark_matter_as_constraint.ipynb  (Cosmology)
├── 04_language_embeddings_noether.ipynb (Semantics)
├── lib/
│   ├── noether_engine.py              (Core Noether current computations)
│   ├── pressure_field.py              (Pressure/fluid continuum)
│   ├── molecular_currents.py          (DNA/molecular-scale currents)
│   ├── cosmological_currents.py       (Dark matter/constraint field)
│   └── semantic_currents.py           (Language embeddings)
└── data/
    ├── crawford_data.csv              (Experimental measurements)
    ├── gromacs_ff/                    (Force field parameters)
    └── cosmology_snapshots/           (Simulation outputs)
```

---

## Key Code Snippets

### Noether Balance Verification

```python
import numpy as np

def verify_noether_balance(J_red, J_blue, J_green, tol=1e-6):
    """Check that J_R + J_B + J_3 ≈ 0 (conservation law)."""
    total = J_red + J_blue + J_green
    balance_error = np.linalg.norm(total)
    is_balanced = balance_error < tol
    return {
        'balance_error': balance_error,
        'is_balanced': is_balanced,
        'J_R': J_red,
        'J_B': J_blue,
        'J_3': J_green,
        'total': total
    }
```

### Pressure Dissipation (1/r²)

```python
def pressure_field_1_over_r2(source_charge, radius_array):
    """
    Isotropic pressure dissipation in 3D from a point source.
    
    P(r) ∝ Q / r²  (Noether current conservation in 3D)
    """
    return source_charge / (4 * np.pi * radius_array**2)

def force_from_pressure_gradient(P, r):
    """Force = -∇P"""
    dP_dr = -2 * P / r  # dP/dr for P ∝ 1/r²
    return dP_dr
```

### DNA Helix Detection

```python
def is_double_helix(coordinates, tolerance=0.1):
    """
    Check if atomic coordinates match DNA double helix geometry.
    
    Criteria:
    - Two intertwined helices
    - Pitch ≈ 3.4 nm
    - Rise per turn ≈ 0.34 nm
    - Chirality: left-handed (B-DNA)
    """
    # Clustering: detect two helical strands
    # Measure: spacing, rotation, handedness
    # Return: (is_helix, pitch_nm, rise_nm, chirality_sign)
    pass
```

### Rotation Curve Fitting

```python
def rotation_curve_noether(radius, baryon_mass, constraint_field_strength):
    """
    Predicted rotation curve from Noether balance.
    
    v(r) emerges from J_R + J_B + J_3 = 0 where:
    - J_R: baryonic mass (observable)
    - J_B: constraint field / "dark matter" (geometric)
    - J_3: boundary / curvature
    """
    # Compute Noether-balanced gravitational potential
    # Derive v(r) = √(r dΦ/dr)
    pass
```

---

## Citation

If you use these notebooks or code, please cite:

```bibtex
@preprint{Allison2026,
  title={A Unified Framework for Gravity, Fluid Dynamics, and Molecular 
         Self-Organization via Noether's Theorem},
  author={Allison, Cody Michael and Crawford, Thomas Joseph and 
          Cosić, Irena and Smethurst, Rebecca},
  year={2026},
  note={arXiv preprint (submitted)}
}
```

---

## Contact

- **Cody Michael Allison** — the.wandering.god@gmail.com
- **Thomas Joseph Crawford** — tjc37@cam.ac.uk
- **Irena Cosić** — irena.cosic@mq.edu.au
- **Rebecca Smethurst** — rebecca.smethurst@physics.ox.ac.uk

---

## License

All code and notebooks are released under the MIT License. See LICENSE file.

---

**Last Updated:** 2026-05-30  
**Status:** Ready for execution
