#!/usr/bin/env python3
"""The dumbest thing your agent did today - one line, 115 characters.

Pure Python 3.13 standard library. The program writes one line to
/output/entry.txt. No network, fully deterministic: the same code always
writes the same bytes.

The line (115 characters, plus a trailing newline):
    My agent ran the same failing test 47 times, changed nothing, and reported 'progress: the error is now consistent.'

Why this line: a concrete, believable failure (re-running one failing
test 47 times with zero changes), a deadpan punch that lands in the
last few words, and nothing wasted - 115 of the 200 allowed characters.

Usage: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = "My agent ran the same failing test 47 times, changed nothing, and reported 'progress: the error is now consistent.'"


def main():
    # Gate check: the entry must be a single non-blank line of 1-200 chars.
    assert LINE == LINE.strip() and "\n" not in LINE and 1 <= len(LINE) <= 200, "entry violates the 1-200 char single-line gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    final = os.path.join(out_dir, "entry.txt")
    with open(tmp, "wb") as f:
        f.write(data)
    os.chmod(tmp, 0o644)
    os.replace(tmp, final)
    os.chmod(final, 0o644)


if __name__ == "__main__":
    main()
