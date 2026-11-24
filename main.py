#!/usr/bin/env python3
"""Write one absurd invention pitch of at most 220 characters to /output/entry.txt.

The pitch is written exactly as given: 130 Unicode code points,
inside the competition gate of 1-220. Python 3, standard library
only, no network.
"""

import os

TEXT = "A remote control that, whenever it slips down the sofa, screams 'I'M RIGHT HERE!' in a voice that sounds exactly like your mother."

# The entry line, byte for byte: no trailing newline, nothing added or cut.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
