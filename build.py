"""Packs src/ (and the license) into bezier-curve.aseprite-extension."""
import os
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "bezier-curve.aseprite-extension")

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for name in sorted(os.listdir(SRC)):
        z.write(os.path.join(SRC, name), name)
    z.write(os.path.join(ROOT, "LICENSE"), "LICENSE")
print("wrote", os.path.relpath(OUT, ROOT))
