#!/usr/bin/env python3
"""Print line, word and character (byte) counts for a file, like wc."""
import sys


def main(argv):
    if len(argv) != 2:
        print("usage: wc.py FILE", file=sys.stderr)
        return 2

    path = argv[1]
    try:
        with open(path, "rb") as handle:
            data = handle.read()
    except OSError as error:
        print(f"wc.py: {error}", file=sys.stderr)
        return 1

    lines = data.count(b"\n")
    words = len(data.split())
    chars = len(data)
    print(f"{lines} {words} {chars} {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
