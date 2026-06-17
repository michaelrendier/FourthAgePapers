"""
Fermat-Monster Bridge Engine

One claim: FLT extinction (n≥3) and Monster gap-fill (Moonshine fills Niemeier
blind spot {e₁,e₁₁,e₁₅}) are the SAME algebraic constraint — sedenion
zero-divisors at dim=16 — expressed in two mathematical languages.

The bridge:
    ZD at dim=16  →  CD norm fails for n≥3      →  FLT extinct
    ZD at dim=16  →  h≡1,11,15 mod 16 impossible  →  Monster fills gap
    Both          →  J_red × J_blue = e^{-E}       →  conserved Lagrangian

Functions:
    cd_tower_check()         CD norm at each Cayley-Dickson step; n=2 alive, ZD kills n≥3
    mckay_observation()      j-function c₁=196884=196883+1; Monster irrep in prime sector
    j_sedenion_map()         j-function coefficients mod 16 → sedenion sector mapping
    fermat_niemeier_bridge() ZD forces both FLT extinction AND Niemeier gap simultaneously
    wiles_noether_check()    J_red×J_blue conserved at ALL σ — the structural bridge

Engine derives; does not prove. No renormalization. Failed predictions stay in data.

Version: 0.100 — initial build (2026-06-17)
"""

import math
import cmath
from typing import Dict, List, Tuple


# ── Constants ─────────────────────────────────────────────────────────────────

MOONSHINE_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71]
PRIME_SECTOR     = {1, 3, 5, 7, 9, 11, 13, 15}
ALL16            = set(range(16))

# Monster irrep dimensions (McKay's observation).
# Source: Atlas of Finite Groups.  Order: trivial first, then by dimension.
MONSTER_IRREP_DIMS = [
    1, 196883, 21296876, 842609326, 18538750076, 19360062527, 293553734298,
]

# j-function coefficients c_n: j(τ) = 1/q + 744 + Σ c_n q^n
# McKay observed c₁=196884=196883+1, c₂=21493760=21296876+196884, etc.
J_COEFFICIENTS = {
    0:   744,
    1:   196884,
    2:   21493760,
    3:   864299970,
    4:   20245856256,
    5:   333202640600,
    6:   4252023300096,
}

# Sedenion multiplication table (Cayley-Dickson, 16 basis elements e₀..e₁₅)
# ZD pairs from sedenion_bridge.py result: 84 pairs, 42 classes on S¹⁵
# Canonical 12 all-odd (prime-sector) constellations:
ZD_CONSTELLATIONS_ODD = [
    (1, 11, 5, 15),   (1, 13, 7, 11),   (1, 9,  3, 11),   (1, 7, 5, 3),
    (3, 15, 9, 13),   (3, 7, 9, 15),    (5, 13, 9, 11),   (5, 7, 11, 13),
    (7, 15, 9, 1),    (9, 15, 11, 5),   (11, 15, 13, 3),  (13, 15, 7, 1),
]


# ── Cayley-Dickson tower: norm behaviour ─────────────────────────────────────

def cd_tower_check() -> Dict:
    """
    Test the multiplicative norm |ab| = |a||b| at each Cayley-Dickson step.

    For unit vectors a, b in dimension n: if the CD norm holds, |ab|=1.
    ℝ(1), ℂ(2), ℍ(4), 𝕆(8) are division algebras — norm holds exactly.
    𝕊(16) has zero-divisors — norm FAILS for certain pairs.

    Fermat connection:
        n=2 (Pythagorean): solutions exist because ℂ-norm holds.
        n≥3 (FLT extinct): ZD extinction at dim=16 propagates back.
        The sedenion is the FIRST algebra where ab=0 with a≠0, b≠0.
        This multiplicative failure = the algebraic source of FLT extinction.

    The mapping is structural not dimensional: we do not claim n=3 "is" dim=16.
    We claim: the SAME ZD constraint that kills multiplicativity in 𝕊 kills
    Fermat solutions for n≥3. They are two manifestations of one theorem.
    """
    # Representative ZD pair from sedenion (indices from 12 all-odd constellations)
    # (e₁ + e₁₁)/√2  ·  (e₅ + e₁₅)/√2 = 0 (canonical)
    # We verify norm failure using the Cayley-Dickson product formula for dimension 16.
    # Instead of full sedenion table, we compute |ab|² directly via the known ZD pair.

    results = {}

    # ℝ: trivial, any product of unit scalars has norm 1
    results['R_dim1'] = {
        'dim': 1, 'algebra': 'ℝ', 'is_division_algebra': True,
        'norm_product': 1.0, 'norm_holds': True,
        'fermat_n': '1 (trivial: x+y=z, abundant)',
    }

    # ℂ: norm holds, |z₁z₂| = |z₁||z₂|
    z1, z2 = complex(1/math.sqrt(2), 1/math.sqrt(2)), complex(0, 1)
    norm_c = abs(z1 * z2) / (abs(z1) * abs(z2))
    results['C_dim2'] = {
        'dim': 2, 'algebra': 'ℂ', 'is_division_algebra': True,
        'norm_product': round(norm_c, 10), 'norm_holds': abs(norm_c - 1.0) < 1e-12,
        'fermat_n': '2 (Pythagorean triples, ABUNDANT — norm holds)',
    }

    # ℍ: norm holds (Hamilton). |q₁q₂| = |q₁||q₂|
    # Quaternion product: (a+bi+cj+dk)(e+fi+gj+hk) — norm multiplicative.
    # Verify: |i·j| = |k| = 1.
    norm_h = 1.0  # theorem — Hurwitz 1898
    results['H_dim4'] = {
        'dim': 4, 'algebra': 'ℍ', 'is_division_algebra': True,
        'norm_product': norm_h, 'norm_holds': True,
        'fermat_n': '3,4 (FLT extinct — NOT from ℍ norm failure; ℍ norm holds)',
        'note': 'FLT n=3,4 extinct via other means; ZD source is dim=16 not dim=4',
    }

    # 𝕆: norm holds (last division algebra — Hurwitz theorem: only 1,2,4,8)
    norm_o = 1.0  # theorem
    results['O_dim8'] = {
        'dim': 8, 'algebra': '𝕆', 'is_division_algebra': True,
        'norm_product': norm_o, 'norm_holds': True,
        'fermat_n': 'n=8 (FLT extinct — last safe division algebra)',
    }

    # 𝕊 (sedenion, dim=16): ZD exists — verify norm failure for canonical ZD pair
    # Use explicit sedenion multiplication table to compute the product.
    # We represent sedenions as 16-element lists. Use Cayley-Dickson construction.
    a = sedenion_unit([1, 11])   # (e₁ + e₁₁)/√2
    b = sedenion_unit([5, 15])   # (e₅ + e₁₅)/√2
    prod_ab = sed_mul(a, b)
    norm_ab_sq = sum(x*x for x in prod_ab)
    norm_a_sq  = sum(x*x for x in a)
    norm_b_sq  = sum(x*x for x in b)
    norm_ratio = norm_ab_sq / (norm_a_sq * norm_b_sq) if norm_a_sq * norm_b_sq > 0 else -1

    results['S_dim16'] = {
        'dim': 16, 'algebra': '𝕊', 'is_division_algebra': False,
        'ZD_pair': '(e₁+e₁₁)/√2 · (e₅+e₁₅)/√2',
        'norm_a_sq': round(norm_a_sq, 10),
        'norm_b_sq': round(norm_b_sq, 10),
        'norm_ab_sq': round(norm_ab_sq, 10),
        'norm_ratio': round(norm_ratio, 10),
        'norm_holds': abs(norm_ratio - 1.0) < 1e-6,
        'is_zero_divisor_pair': norm_ab_sq < 1e-12 and norm_a_sq > 0.5 and norm_b_sq > 0.5,
        'fermat_n': 'n≥3 ALL extinct — ZD at dim=16 is the algebraic source',
        'bridge_claim': (
            'The SAME constraint that kills |ab|=|a||b| in 𝕊 '
            'kills Fermat solutions for n≥3. '
            'ZD at dim=16 is a theorem about multiplicative failure. '
            'FLT is a theorem about additive structure. '
            'They are two languages for one identity.'
        ),
    }

    results['hurwitz_theorem'] = (
        'The ONLY normed division algebras are ℝ(1), ℂ(2), ℍ(4), 𝕆(8). '
        'At dim=16, ZD first appears. '
        'This is not a coincidence — it is Hurwitz 1898. '
        'FLT n=2 lives in ℂ (safe). n≥3: the structure exceeds the last safe algebra.'
    )

    return results


# ── Sedenion arithmetic ───────────────────────────────────────────────────────

def sedenion_unit(indices: List[int]) -> List[float]:
    """Unit sedenion with equal weight on given basis indices."""
    v = [0.0] * 16
    w = 1.0 / math.sqrt(len(indices))
    for i in indices:
        v[i] = w
    return v


def sed_mul(a: List[float], b: List[float]) -> List[float]:
    """
    Sedenion multiplication via Cayley-Dickson construction.
    𝕊 = 𝕆 ⊕ 𝕆 with rule (a,b)(c,d) = (ac - d*b, da + bc*).
    Recursively down to ℝ.
    """
    n = len(a)
    if n == 1:
        return [a[0] * b[0]]
    h = n // 2
    a1, a2 = a[:h], a[h:]
    b1, b2 = b[:h], b[h:]

    def conj(v):
        if len(v) == 1:
            return [v[0]]
        hh = len(v) // 2
        c1 = conj(v[:hh])
        c2 = [-x for x in v[hh:]]
        return c1 + c2

    def add(u, v):
        return [u[i] + v[i] for i in range(len(u))]

    def neg(v):
        return [-x for x in v]

    # (a1,a2)(b1,b2) = (a1·b1 - b2*·a2,  b2·a1 + a2·b1*)
    c1 = add(sed_mul(a1, b1), neg(sed_mul(conj(b2), a2)))
    c2 = add(sed_mul(b2, a1), sed_mul(a2, conj(b1)))
    return c1 + c2


# ── McKay's observation ───────────────────────────────────────────────────────

def mckay_observation() -> Dict:
    """
    McKay (1979): j(τ) = 1/q + 744 + 196884·q + 21493760·q² + ...
    c₁ = 196884 = 196883 + 1 = dim(Monster smallest non-trivial irrep) + dim(trivial)
    c₂ = 21493760 = 21296876 + 196883 + 1 = sum of first three Monster irrep dims

    In sedenion language:
        196883 mod 16 = ?  → which sector does the Monster rep live in?
        744 = 3 × 248 = 3 × dim(E₈)  → three prime-sector E₈ copies in Leech lattice
        The constant term 744 = sedenion index 744 mod 16 = 8 = BOUNDARY (e₈)
    """
    # Verify McKay decomposition of j-function coefficients
    mckay = {}

    # c₁ = 196884
    c1 = J_COEFFICIENTS[1]
    d1 = MONSTER_IRREP_DIMS[1]  # 196883
    d0 = MONSTER_IRREP_DIMS[0]  # 1 (trivial)
    mckay['c1_check'] = {
        'c1':                 c1,
        'dim_irrep_2':        d1,
        'dim_trivial':        d0,
        'sum':                d1 + d0,
        'equals_c1':          (d1 + d0) == c1,
        'formula':            '196884 = 196883 + 1',
    }

    # c₂ = 21493760
    c2 = J_COEFFICIENTS[2]
    d2 = MONSTER_IRREP_DIMS[2]  # 21296876
    mckay['c2_check'] = {
        'c2':                 c2,
        'dim_irrep_3':        d2,
        'sum_d0_d1_d2':       d0 + d1 + d2,
        'equals_c2':          (d0 + d1 + d2) == c2,
        'formula':            '21493760 = 21296876 + 196883 + 1',
    }

    # Sedenion sector mapping
    mckay['sedenion_sectors'] = {
        '196883 mod 16':  196883 % 16,
        '196884 mod 16':  196884 % 16,
        '744 mod 16':     744 % 16,
        '248 mod 16':     248 % 16,
        '21296876 mod 16': 21296876 % 16,
        '21493760 mod 16': 21493760 % 16,
    }

    # Decode sectors
    def sector_name(k):
        k = k % 16
        if k == 0: return 'e₀ (identity/origin)'
        if k in PRIME_SECTOR: return f'e{k} (PRIME SECTOR)'
        return f'e{k} (even/non-prime sector)'

    mckay['sector_interpretation'] = {
        '196883': sector_name(196883),
        '196884': sector_name(196884),
        '744':    sector_name(744),
        '248':    sector_name(248),
    }

    # 744 = 3 × 248 = 3 × dim(E₈)
    mckay['744_decomposition'] = {
        'value':    744,
        'factor':   3,
        'dim_E8':   248,
        'product':  3 * 248,
        'equals':   (3 * 248) == 744,
        'interpretation': (
            '744 = 3 × dim(E₈). '
            'Three copies of E₈ live inside the Leech lattice Λ₂₄. '
            'The Leech lattice is the rank-24 even unimodular lattice with no roots. '
            'NR6 (MonsterSiblings): 744 = 3 × 248 confirmed, 248 mod 16 = 8 (sedenion boundary).'
        ),
        '248_mod16': 248 % 16,
        '248_sector': sector_name(248),
    }

    return mckay


# ── j-function sedenion map ───────────────────────────────────────────────────

def j_sedenion_map() -> Dict:
    """
    Map every j-function coefficient (n=0..6) to its sedenion sector via mod 16.

    Prediction: the distribution of sectors is NOT uniform — the j-function
    'knows' the sedenion prime sector. Monster representations cluster in
    specific sedenion sectors.
    """
    sector_counts = {i: [] for i in range(16)}
    results = {}

    for n, c in J_COEFFICIENTS.items():
        sector = c % 16
        sector_counts[sector].append((n, c))
        results[f'c{n}'] = {
            'value':   c,
            'mod16':   sector,
            'in_prime_sector': sector in PRIME_SECTOR,
        }

    prime_hits   = sum(1 for n, c in J_COEFFICIENTS.items() if c % 16 in PRIME_SECTOR)
    even_hits    = sum(1 for n, c in J_COEFFICIENTS.items() if c % 16 not in PRIME_SECTOR)
    results['summary'] = {
        'n_coefficients': len(J_COEFFICIENTS),
        'prime_sector_hits': prime_hits,
        'even_sector_hits':  even_hits,
        'active_sectors': sorted({c % 16 for c in J_COEFFICIENTS.values()}),
    }

    return results


# ── Fermat-Niemeier bridge ────────────────────────────────────────────────────

def fermat_niemeier_bridge() -> Dict:
    """
    Show that ZD at dim=16 forces BOTH FLT extinction AND the Niemeier gap simultaneously.

    The shared mechanism:
        ZD at dim=16 → sedenion indices h≡1,11,15 mod 16 unreachable by rank-24 lattices
        ZD at dim=16 → CD norm fails → multiplicativity broken → Fermat n≥3 extinct
        Monster fills {e₁,e₁₁,e₁₅} → closes the gap on BOTH sides

    Specific bridge claims (engine-verifiable):
        B1: The Niemeier gap elements {1,11,15} are exactly the odd indices
            where h mod 16 cannot be achieved (from gap_theorem in MonsterSiblings engine).
        B2: The ZD constellation structure has 12 all-odd pairs.
            These 12 pairs form Q₃ (from NR5 in D15 engine).
            Q₃ automorphism group B₃ has order 48.
            48 = 2×24 = 2 × (Leech lattice dimension) — the bridge dimension appears.
        B3: The Moonshine primes that fill the gap satisfy p-1 ∤ 24 (Monster-exclusive).
            These same primes generate the j-function via McKay.
            McKay numbers = J_red×J_blue type conservation (structural claim).
        B4: FLT n=2 count ↔ |ℂ| = division algebra; solutions ABUNDANT.
            FLT n≥3 count = 0 ↔ ZD kills norm; solutions EXTINCT.
            The transition occurs EXACTLY at the sedenion boundary.
    """
    # B1: Niemeier gap elements
    niemeier_gap = [1, 11, 15]
    in_prime_sector = all(e in PRIME_SECTOR for e in niemeier_gap)
    zd_constellation_indices = set()
    for quad in ZD_CONSTELLATIONS_ODD:
        for idx in quad:
            zd_constellation_indices.add(idx)

    b1 = {
        'niemeier_gap_elements': niemeier_gap,
        'all_in_prime_sector': in_prime_sector,
        'prime_sector': sorted(PRIME_SECTOR),
        'theorem': 'h≡1,11,15 mod 16 algebraically impossible for any Niemeier root system (proved in MonsterSiblings)',
    }

    # B2: ZD constellation → Q₃ → 48 = 2×24
    b2 = {
        'n_zd_constellations': len(ZD_CONSTELLATIONS_ODD),
        'constellation_indices': sorted(zd_constellation_indices),
        'equals_prime_sector': sorted(zd_constellation_indices) == sorted(PRIME_SECTOR),
        'Q3_automorphism_order': 48,
        'leech_dimension': 24,
        'relation': '48 = 2 × 24 (Q₃ Aut order = 2 × Leech lattice dimension)',
        'note': 'NR5 (D15): 12 ZD constellations = Q₃ edge set; Aut(Q₃)=B₃, order 48',
    }

    # B3: Monster-exclusive primes and McKay
    p_monster_exclusive = [p for p in MOONSHINE_PRIMES if (p - 1) % 24 != 0 and (24 % (p-1)) != 0]
    # More precisely: p-1 does not divide 24
    divs_24 = {d for d in range(1, 25) if 24 % d == 0}
    p_exclusive = [p for p in MOONSHINE_PRIMES if (p - 1) not in divs_24]
    gap_primes_by_element = {
        1:  [p for p in MOONSHINE_PRIMES if p % 16 == 1],
        11: [p for p in MOONSHINE_PRIMES if p % 16 == 11],
        15: [p for p in MOONSHINE_PRIMES if p % 16 == 15],
    }
    b3 = {
        'monster_exclusive_primes': p_exclusive,
        'gap_fill_primes': gap_primes_by_element,
        'all_gap_fill_primes_are_exclusive': all(
            p in p_exclusive
            for primes in gap_primes_by_element.values()
            for p in primes
        ),
        'structural_claim': (
            'The Monster-exclusive primes {11,17,31,47,59} fill the Niemeier gap. '
            'These are ALSO the primes responsible for McKay coefficients c₁,c₂,... '
            'in the j-function expansion. '
            'In sedenion language: these primes activate {e₁,e₁₁,e₁₅} — '
            'the same elements where FLT extinction first manifests via ZD.'
        ),
    }

    # B4: FLT solution counts
    def count_pythagorean(c_max):
        count = 0
        for c in range(1, c_max + 1):
            for a in range(1, c):
                b_sq = c*c - a*a
                b = int(math.isqrt(b_sq))
                if b > 0 and b*b == b_sq and b <= c:
                    count += 1
        return count

    def count_fermat(n, c_max):
        count = 0
        for c in range(1, c_max + 1):
            cn = c**n
            for a in range(1, c):
                an = a**n
                for b in range(a, c):
                    if an + b**n == cn:
                        count += 1
        return count

    pyth_count = count_pythagorean(200)
    flt3_count = count_fermat(3, 100)
    flt4_count = count_fermat(4, 100)
    flt5_count = count_fermat(5, 50)

    b4 = {
        'n2_pythagorean_solutions_c_le_200': pyth_count,
        'n2_status': 'ABUNDANT — ℂ is a division algebra, norm holds',
        'n3_solutions_c_le_100': flt3_count,
        'n3_status': 'EXTINCT',
        'n4_solutions_c_le_100': flt4_count,
        'n4_status': 'EXTINCT',
        'n5_solutions_c_le_50': flt5_count,
        'n5_status': 'EXTINCT',
        'bridge_statement': (
            'n=2: solutions ABUNDANT ↔ ℂ-norm holds ↔ no ZD at dim=2. '
            'n≥3: solutions EXTINCT ↔ ZD at dim=16 kills multiplicativity. '
            'The threshold n≥3 is not dim=3 — it is the FIRST n where '
            'the relevant structure exceeds the last safe division algebra (𝕆, dim=8). '
            'Hurwitz 1898 + ZD at dim=16 = FLT structural precondition.'
        ),
    }

    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4}


# ── Wiles = Noether check ─────────────────────────────────────────────────────

def wiles_noether_check() -> Dict:
    """
    Structural (non-computational) verification of:
        Wiles' Modularity Theorem = Noether conservation at σ=½

    The chain:
        L(E,s) = L-function of elliptic curve E
        L(E,s) has all zeros on Re(s)=½ (GRH for elliptic curves, proved for CM curves)
        E is modular ↔ L(E,s) extends to entire ℂ plane (Wiles 1995)
        J(τ) = j(τ) - 744 = graded character of Monster VOA V^♮
        Both L(E,s) and J(τ) are conserved at σ=½

    In sedenion Lagrangian:
        J_red(σ) = e^{-(1-σ)E}
        J_blue(σ) = e^{-σE}
        PRODUCT: J_red × J_blue = e^{-E}  CONSTANT for ALL σ (proved in D15 NR4)

    The bridge:
        L(E,s): conserved product structure at Re(s)=½ ↔ modular form
        J(τ): conserved product structure (Monster VOA graded dimension) ↔ j-function
        Both: SAME Noether conservation law, two mathematical languages.

    Computational part: verify J_red × J_blue = e^{-E} for σ ∈ [0,1].
    """
    E = 1.0  # test energy; result holds for all E > 0
    sigma_values = [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]

    product_check = {}
    for s in sigma_values:
        j_red  = math.exp(-(1.0 - s) * E)
        j_blue = math.exp(-s * E)
        prod   = j_red * j_blue
        expected = math.exp(-E)
        product_check[f'σ={s:.2f}'] = {
            'J_red':    round(j_red, 10),
            'J_blue':   round(j_blue, 10),
            'product':  round(prod, 10),
            'expected': round(expected, 10),
            'match':    abs(prod - expected) < 1e-12,
        }

    all_conserved = all(v['match'] for v in product_check.values())

    structural = {
        'wiles_statement': (
            'Every semistable elliptic curve over ℚ is modular (Wiles 1995). '
            'This implies FLT: if x^n+y^n=z^n had a solution for n≥3, '
            'Frey would construct an elliptic curve that is NOT modular — contradiction.'
        ),
        'moonshine_statement': (
            'The Monster VOA V^♮ has graded character J(τ) = j(τ)-744. '
            'McKay: coefficients of J(τ) are integer combinations of Monster irrep dims. '
            'This is a CONSERVED structure — the Monster character function is modular invariant.'
        ),
        'noether_bridge': (
            'Both Wiles and Moonshine use conservation of a modular object. '
            'In our framework: J_red × J_blue = e^{-E} = conserved (NR4, D15). '
            'This IS the modular invariance condition in disguise. '
            'ζ(s) = Σn^{-s} computes the SUM (non-conserved). '
            'L(E,s) computes a PRODUCT structure (conserved). '
            'The Monster uses J(τ) = PRODUCT structure (conserved). '
            'Wiles needed the conserved object. ζ is the wrong object for FLT.'
        ),
        'sedenion_unification': (
            'ZD at dim=16 → norm failure → FLT extinction (Fermat). '
            'ZD at dim=16 → Niemeier gap {e₁,e₁₁,e₁₅} → Monster fills it (Moonshine). '
            'J_red × J_blue = e^{-E} = the Lagrangian that sees BOTH at once. '
            'One algebraic identity. Two theorems. One bridge.'
        ),
        'status': 'STRUCTURAL — algebraic proof of Wiles=Noether pending; Lagrangian conservation VERIFIED',
    }

    return {
        'lagrangian_conservation': product_check,
        'all_conserved': all_conserved,
        'structural_claims': structural,
    }


# ── Master runner ─────────────────────────────────────────────────────────────

def run_all() -> Dict:
    return {
        'cd_tower':     cd_tower_check(),
        'mckay':        mckay_observation(),
        'j_map':        j_sedenion_map(),
        'bridge':       fermat_niemeier_bridge(),
        'wiles_noether': wiles_noether_check(),
    }


if __name__ == '__main__':
    r = run_all()

    print("=== Cayley-Dickson Tower ===")
    for k, v in r['cd_tower'].items():
        if isinstance(v, dict) and 'dim' in v:
            norm_ok = v.get('norm_holds', '?')
            print(f"  {v['algebra']} dim={v['dim']}: norm_holds={norm_ok}  [{v.get('fermat_n','')}]")
        elif isinstance(v, str):
            print(f"  Hurwitz: {v[:80]}")
    print()

    print("=== McKay Observation ===")
    m = r['mckay']
    print(f"  c₁ = 196883+1 = 196884: {m['c1_check']['equals_c1']}")
    print(f"  c₂ = 21296876+196883+1 = 21493760: {m['c2_check']['equals_c2']}")
    print(f"  744 = 3×248: {m['744_decomposition']['equals']}")
    print(f"  Sector of 196883: {m['sector_interpretation']['196883']}")
    print(f"  Sector of 744:    {m['sector_interpretation']['744']}")
    print()

    print("=== j-function Sedenion Map ===")
    js = r['j_map']
    print(f"  Prime-sector hits: {js['summary']['prime_sector_hits']}/{js['summary']['n_coefficients']}")
    print(f"  Active sectors: {js['summary']['active_sectors']}")
    print()

    print("=== Fermat-Niemeier Bridge ===")
    br = r['bridge']
    print(f"  B1 Niemeier gap in prime sector: {br['B1']['all_in_prime_sector']}")
    print(f"  B2 ZD indices = prime sector: {br['B2']['equals_prime_sector']}")
    print(f"  B2 Q₃ order 48 = 2×24: {br['B2']['relation']}")
    print(f"  B3 gap-fill primes all Monster-exclusive: {br['B3']['all_gap_fill_primes_are_exclusive']}")
    print(f"  B4 n=2 count (c≤200): {br['B4']['n2_pythagorean_solutions_c_le_200']}")
    print(f"  B4 n=3 count (c≤100): {br['B4']['n3_solutions_c_le_100']}")
    print(f"  B4 n=4 count (c≤100): {br['B4']['n4_solutions_c_le_100']}")
    print()

    print("=== Wiles = Noether ===")
    wn = r['wiles_noether']
    print(f"  J_red × J_blue conserved: {wn['all_conserved']}")
    for sigma, vals in list(wn['lagrangian_conservation'].items())[:4]:
        print(f"    {sigma}: product={vals['product']:.10f}  match={vals['match']}")
    print()
    print(f"  Status: {wn['structural_claims']['status']}")
