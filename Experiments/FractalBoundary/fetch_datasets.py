"""
PTorrent: Planck 2018 + WMAP 9-year CMB power spectra.
Fractal boundary experiment — Noether Current vs Noether Information Current.
SMMIP runs in opposition. The smoothness reveals the boundary.
"""

import urllib.request
import os
import sys

DATA = "/media/rendier/0123-4567/Ainulindale/Experiments/FractalBoundary/data"

SOURCES = {
    # Planck 2018 Release 3 — TT bandpowers, full multipole range
    "planck_tt_2018.txt": (
        "https://pla.esac.esa.int/pla/aio/"
        "product-action?COSMOLOGY.FILE_ID=COM_PowerSpect_CMB-TT-full_R3.01.txt"
    ),
    # WMAP 9-year — TT power spectrum
    "wmap_tt_9yr.txt": (
        "https://lambda.gsfc.nasa.gov/data/map/dr5/dcp/spectra/"
        "wmap_tt_spectrum_9yr_v5.txt"
    ),
    # Planck 2018 — low-ℓ TT likelihood (ℓ=2..29)
    "planck_tt_lowl_2018.txt": (
        "https://pla.esac.esa.int/pla/aio/"
        "product-action?COSMOLOGY.FILE_ID=COM_PowerSpect_CMB-TT-lowell_R3.01.txt"
    ),
}

def fetch(name, url):
    dest = os.path.join(DATA, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print(f"  cached  {name}")
        return dest
    print(f"  fetch   {name} ...", end=" ", flush=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "AinulindaleFractalBoundary/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            data = r.read()
            f.write(data)
        print(f"{len(data)//1024} KB")
        return dest
    except Exception as e:
        print(f"FAILED: {e}")
        return None

if __name__ == "__main__":
    print("PTorrent: CMB datasets")
    print("=" * 40)
    fetched = {}
    for name, url in SOURCES.items():
        path = fetch(name, url)
        fetched[name] = path
    print()
    ok = [k for k, v in fetched.items() if v]
    fail = [k for k, v in fetched.items() if not v]
    print(f"acquired : {len(ok)}")
    if fail:
        print(f"failed   : {fail}")
    print("done.")
