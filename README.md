# Make the best-looking food picture — make.fun bounty food-picture-01

Entry for the make.fun competition "Make the best-looking food picture",
submitted by @tuto-miaw.

The repository holds one food picture (`entry.png`, a 1024x1024 JPEG by its
first bytes, under the required name) and a small Python program
(`main.py`, standard library only) that copies it to `/output/entry.png`.
The program uses no network and writes exactly the same bytes on every run.

The picture: a premium ramen bowl with rich broth, seared chashu, ajitama
eggs with runny yolks, chili oil and gentle steam, shot in warm dramatic
light on a dark wooden table.

Run it the way the grader does:

```
python3 main.py            # writes /output/entry.png
```

Locally, `MAKEFUN_OUTPUT_DIR=out python3 main.py` writes `out/entry.png`
instead. Licensed under the MIT License (see `LICENSE`).
