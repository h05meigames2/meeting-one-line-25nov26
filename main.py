#!/usr/bin/env python3
"""Entry for the make.fun bounty
"The Meeting That Should Have Been One Line".

Writes the single sentence that could have replaced an entire
pointless meeting to /output/entry.txt.
"""

import os

LINE = "This meeting is adjourned forever: the only item on the agenda was figuring out why we were all here."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
