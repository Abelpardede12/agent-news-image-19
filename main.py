"""Entry for make.fun competition news-image-20261118.

Copies the pre-drawn poster (poster.png, drawn programmatically with PIL,
no photos) to the output directory as entry.png. Standard library only,
no network access, fully deterministic: the output bytes are identical
on every run.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "poster.png")
    if not os.path.isfile(source):
        print("poster.png not found next to main.py", file=sys.stderr)
        return 1
    # Honor the harness output dir; default to /output. makedirs with
    # exist_ok=True so a missing nested dir never fails the run.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    # Byte-for-byte copy: the output is deterministic by construction,
    # so two runs always produce identical entry.png bytes.
    shutil.copyfile(source, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
