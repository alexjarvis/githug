#!/usr/bin/env python3
"""Print line, word and character counts for a text file, like wc."""
import sys


def main(argv):
    if len(argv) != 2:
        print("usage: wc.py FILE", file=sys.stderr)
        return 2

    path = argv[1]
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
    except OSError as error:
        print(f"wc.py: {error}", file=sys.stderr)
        return 1

    lines = len(text.splitlines())
    words = len(text.split())
    chars = len(text)
    print(f"{lines} {words} {chars} {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
