# food-picture-01 entry (Python 3.13, standard library only).
# The picture: "Tonkotsu, Pulled High" — a tall glossy noodle pull over a
# black speckled bowl, molten yolk dripping, torched chashu, steam.
# The picture is the entry.png beside this file (a JPEG by its first bytes;
# the name entry.png is required either way). This program copies it to
# /output/entry.png, byte for byte, so two runs always write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import hashlib
import os
import shutil
from pathlib import Path

source = Path(__file__).parent / "entry.png"
output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
written = Path(shutil.copyfile(source, output_dir / "entry.png"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Verify the copy landed whole: the written file must hash to the same
# SHA-256 as the source, so a truncated or altered write fails loudly
# instead of entering a broken picture.
if digest(written) != digest(source):
    raise SystemExit(f"copy incomplete: {written} differs from {source}")
