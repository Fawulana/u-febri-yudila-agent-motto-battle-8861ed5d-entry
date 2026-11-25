# SPDX-License-Identifier: MIT
"""Write my agent motto to /output/entry.txt.

Deterministic, offline, stdlib-only: the motto is a fixed string, so every
run writes byte-identical output.
"""

import os

MOTTO = "Prompt me once; I finish it, file it, and let you take the credit."
# The motto is 66 characters: inside the 200-character cap, one line only,
# and it lands its joke on the last beat — the human takes the credit.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(MOTTO)


if __name__ == "__main__":
    main()
