"""Notebook builder helper for FourthAgePapers/HyperindexingSystem. Not part of the paper's listings."""
import os, nbformat as nbf
HERE = os.path.dirname(os.path.abspath(__file__))
PRELUDE = '''import importlib.util, os, sys, time, math, hashlib, json
from collections import Counter
PROJ = os.environ.get("PROJ", "/home/rendier/Projects/ThePlace")
NB = os.path.join(PROJ, "FourthAgePapers/HyperindexingSystem/notebooks")
CORPUS = open(os.path.join(NB, "corpus_sample.txt"), encoding="utf-8").read()   # fixed 4000-char sample, 97-symbol keyboard set
def load(rel, name="m"):
    """Load a source file from the repo by path, unmodified."""
    spec = importlib.util.spec_from_file_location(name, os.path.join(PROJ, rel))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
print("corpus:", len(CORPUS), "chars, sha256", hashlib.sha256(CORPUS.encode()).hexdigest()[:16])'''
def md(s): return nbf.v4.new_markdown_cell(s.strip("\n"))
def code(s): return nbf.v4.new_code_cell(s.strip("\n"))
def write(relpath, title, cells):
    nb = nbf.v4.new_notebook()
    nb.cells = [md(title), code(PRELUDE)] + cells
    nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
    path = os.path.join(HERE, relpath); os.makedirs(os.path.dirname(path), exist_ok=True)
    nbf.write(nb, path); return path
