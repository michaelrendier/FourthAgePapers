# Installing FermatMonster

FermatMonster runs inside its own virtual environment. **Do not use the system Python**: on the author's machine it has numpy 2.x in `~/.local` shadowing the
apt numpy 1.x, so scientific imports crash. Everything below uses the `.venv`.

Linux / macOS:

```bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
# this repository imports ValaQuenta (the code root):
.venv/bin/pip install -e ../ValaQuenta
```

Windows (PowerShell):

```powershell
py -3 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
# this repository imports ValaQuenta (the code root):
.venv\Scripts\pip install -e ..\ValaQuenta
```

Check: `.venv/bin/python -c "import sys; print(sys.prefix)"` prints a path ending in `.venv`.

`requirements.txt` lists what this repository's own code imports, with the version tested in the root environment (`ValaQuenta/.venv`, which holds every
package any engine needs). If an import is reported missing, install it in `ValaQuenta/.venv` first (`ValaQuenta/tools/vq_venv_sync.py`), then here.

<!-- system-software:begin -->
## System software (not Python)

Programs this repository's own files call, found by scanning its source (`ValaQuenta/tools/repo_venv.py`). Install them with the system package manager; they are not pip packages.

| software | command | here | install |
|---|---|---|---|
| a C compiler (gcc, make) for the C code | `gcc` | installed | `sudo apt install build-essential` |
<!-- system-software:end -->
