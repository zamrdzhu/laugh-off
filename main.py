"""The Toaster Has Two Settings — exactly one funny line.

The joke is a small domestic tragedy with a kicker: the toaster
is not broken, it is committed, and the last clause admits it
knows exactly what it is doing.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this
file. The 200-character gate is checked on every run so an
over-long edit can never slip through silently.
"""

import os
import sys

LINE = (
    "My toaster has two settings: raw bread and a small house fire. "
    "There is no in-between, and it knows it."
)


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} chars, must be 1-200",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
