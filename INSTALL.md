# Installing FourthAgePapers

FourthAgePapers is a workbench of workbenches: **each paper has its own `.venv`, `requirements.txt` and `INSTALL.md`** inside its own directory (for example
`FermatMonster/`, `CryptoVulnerability/`), made by `ValaQuenta/tools/repo_venv.py <paper directory> --apply`. The Witch's Hat family (`DM_GalacticCavity`, `CMB_FractalBoundary`, `CMB_PlasmaBoundary`, `Crawford_NavierStokes`, `WhiteHoleBang` and the parent register `WitchesHat/`) lives on the `witches-hat` branch
and has **one** `.venv` (`WitchesHat/.venv`, with its own `requirements.txt` and `INSTALL.md`) covering all of them. Never use the system Python (numpy 2.x in `~/.local` shadows the apt numpy 1.x on the author's machine).

```bash
cd FermatMonster                      # any paper
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -e ../../ValaQuenta      # the code root, if the paper imports it
```

Papers that use only the Python standard library have an empty `requirements.txt`. Non-Python software each paper calls is listed in that paper's `INSTALL.md`.
