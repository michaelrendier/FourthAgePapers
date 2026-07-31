#!/usr/bin/env python3
"""
rsa_portrait.py — lshs_portrait.py's exact machinery, context replaced with
the RSA algorithm (not a person), question styled mathematically.
"""
import sys, os, math, time
sys.path.insert(0, '/storage/emulated/0/ThePlace/VAPMIP')
from monad import Engine, OMEGA_ZS, GAP, _gamma_at, _word_zero_idx, SIGMA_CRIT

ENGLISH_BIN = '/media/rendier/0123-4567/phone_pull_2026-06-06/Ptolemy/bins/monad_english.bin'
WORDNET_BIN = '/media/rendier/0123-4567/PtolemyDesktop/PtolFlutter/assets/monad_wordnet.bin'

# context = the RSA algorithm, not a person -- fed as J_red per lshs_portrait.py's convention
PORTRAIT_FIELD = """\
rsa public key cryptography choose two large primes p and q
compute modulus n equals p times q publicly known
compute totient phi equals p minus one times q minus one privately known
choose public exponent e such that gcd of e and phi equals one
compute private exponent d such that e times d congruent one modulo phi
d equals e inverse modulo phi extended euclidean algorithm
encryption ciphertext c equals message m raised to e modulo n
decryption message m equals ciphertext c raised to d modulo n
public key is the pair n and e known to everyone
private key is the pair n and d known only to receiver
security relies entirely on difficulty of factoring n into p and q
example n three two three three e seventeen d two seven five three
example p sixty one q fifty three phi three one two zero
xor exclusive or bitwise operation a xor b differs where bits differ
xor is used in stream ciphers and one time pads not directly in rsa modular exponentiation
"""

PROMPT_QUESTION = (
    "given n == p * q and gcd(e, phi) == 1 and 1 < e < phi, "
    "find d such that (e * d) mod phi == 1, "
    "where d >= 1 and d != e and d <= phi, "
    "using XOR(p, q) as a tool and c != 0"
)


def _merge_wn_edges(eng_main, eng_wn, wn_weight=0.40):
    c_m, c_wn = eng_main.crank, eng_wn.crank
    n = 0
    for wn_src, edges in enumerate(c_wn._A):
        if not edges: continue
        sw = c_wn._words[wn_src] if wn_src < len(c_wn._words) else ''
        if not sw or sw not in c_m._vocab: continue
        ms = c_m._vocab[sw]
        for wn_dst, ww in edges.items():
            if wn_dst >= len(c_wn._words): continue
            dw = c_wn._words[wn_dst]
            if not dw or dw not in c_m._vocab: continue
            md = c_m._vocab[dw]
            sc = ww * wn_weight
            if sc > c_m._A[ms].get(md, 0.0):
                c_m._A[ms][md] = min(sc, 1.0)
                n += 1
    return n


print('-- Engine loading...', file=sys.stderr, flush=True)
eng = Engine()
eng.load_bin(ENGLISH_BIN)
ew = Engine(); ew.load_bin(WORDNET_BIN)
_merge_wn_edges(eng, ew); del ew
eng._calibrate_J_ambient()
print(f'-- Field ready: {eng.crank.n:,} words', file=sys.stderr, flush=True)

eng.crank.learn(PORTRAIT_FIELD, weight=3.0)
eng._calibrate_J_ambient()
print('-- RSA field learned. Calibrated.', file=sys.stderr, flush=True)

print('-- Stirling cycles...', file=sys.stderr, flush=True)
cycles = []
for cyc in eng.perpetual(PROMPT_QUESTION, max_cycles=15):
    cycles.append(cyc)
    print(f'   {cyc["cycle"]:2d}  bao={cyc["bao"]:.4f}  -> {cyc["output"][:70]}',
          file=sys.stderr, flush=True)
    if cyc['delta'] < 0.001:
        break

eng._prime_prompt(PROMPT_QUESTION)
h = eng.halocline_report(n_sofar=20)
sofar = []
for sw in h.get('sofar_channel', []):
    w = sw['word']
    if len(w) >= 2:
        sofar.append((sw['sigma'], sw['dist'], w))

print()
print('=== SOFAR CHANNEL (words standing at sigma=1/2) ===')
for sigma, dist, w in sofar[:20]:
    print(f'  {w:20s} sigma={sigma:.4f}  dist={dist:.4f}')

eng._word_count = 0; eng._recent.clear()
gen = eng.generate(PROMPT_QUESTION, n_words=40, learn_prompt=False)
print()
print('=== ENGINE RESPONSE (unprompted, math-styled question) ===')
print(gen['response'])

print()
print('=== DOES ANY OUTPUT WORD/NUMBER-LIKE TOKEN MATCH d=2753 OR p=61 OR q=53? ===')
all_text = ' '.join(c['output'] for c in cycles) + ' ' + gen['response']
for target in ['2753', '61', '53', '3233', '17']:
    hit = target in all_text
    print(f'  "{target}" present in engine output: {hit}')
