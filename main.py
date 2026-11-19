#!/usr/bin/env python3
"""news-image-20261119 entry program.

Writes the entry image for make.fun's "Sum up 19 November's world news
in one image" competition. The poster beside this file (poster.png) is
the entry; this program copies it, byte for byte, to entry.png in the
output directory, so every run produces exactly the same file.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "poster.png")
    if not os.path.isfile(source):
        # Fail loudly rather than writing nothing: the scorer runs this
        # program twice and compares the bytes, so a silent miss would
        # surface as a confusing mismatch instead of a clear error here.
        print("poster.png not found next to main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Byte-for-byte copy: the output is deterministic by construction,
    # so two runs always produce identical entry.png bytes.
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
