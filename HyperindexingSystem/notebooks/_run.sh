#!/bin/bash
# execute every notebook in place; report failures
cd "$(dirname "$0")"
fail=0
for nb in $(ls v*/*.ipynb w*/*.ipynb 2>/dev/null | sort); do
  if python3 -m nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=900 "$nb" >/dev/null 2>/tmp/nbrun.err; then echo "OK   $nb"; else echo "FAIL $nb"; tail -4 /tmp/nbrun.err; fail=1; fi
done
exit $fail
