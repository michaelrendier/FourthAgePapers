import sys, nbformat
for p in sys.argv[1:]:
    nb = nbformat.read(p, 4); print("=====", p)
    for c in nb.cells:
        if c.cell_type == "code":
            for o in c.get("outputs", []):
                if o.output_type == "stream": print(o.text.rstrip()[:1800])
                elif o.output_type == "error": print("ERROR", o.ename, o.evalue)
