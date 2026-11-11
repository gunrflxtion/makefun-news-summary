"""News-summary-01 entry: copy summary.txt to /output/entry.txt.

The copy is byte-for-byte, so both grader runs produce identical output:
no timestamps, no randomness, no network, standard library only.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(
    os.path.join(HERE, "summary.txt"),
    os.path.join(OUT, "entry.txt"),
)
