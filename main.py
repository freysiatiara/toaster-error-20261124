#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, at most 120 characters, to /output/entry.txt:
the error message a kitchen toaster shows its owner when the bagel
in slot 2 turns out to be frozen solid.
"""

import os

LINE = (
    "ERROR E09: Bagel frozen solid. "
    "I refuse to fight a hockey puck. "
    "Thaw it first."
)

# The grader runs the program in a sandbox where /output exists.
# Locally, ENTRY_OUTPUT can point the file elsewhere for a test run.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    line = LINE.strip()
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"line is {len(line)} chars, must be 1..120")
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
