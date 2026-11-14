# food-picture-01 entry (Python 3.13, standard library only).
# The picture is the entry.png beside this file (a JPEG by its first bytes;
# the name entry.png is required either way). This program copies it to
# /output/entry.png, byte for byte, so two runs always write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

source = Path(__file__).parent / "entry.png"
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(source, output_dir / "entry.png")
