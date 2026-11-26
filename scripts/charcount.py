#!/usr/bin/env python3
import sys


def main(argv):
    if len(argv) != 2:
        print("Usage: charcount.py FILE", file=sys.stderr)
        return 2
    with open(argv[1], "r", encoding="utf-8") as f:
        print(len(f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
