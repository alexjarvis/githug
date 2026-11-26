#!/usr/bin/env python3
"""Print the number of non-empty lines in a text file."""

import sys


def count_non_empty_lines(path):
    count = 0
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if line.strip():
                count += 1
    return count


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: linecount.py FILE\n")
        return 2

    try:
        total = count_non_empty_lines(argv[1])
    except OSError as error:
        sys.stderr.write("linecount.py: %s\n" % error)
        return 1

    print(total)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
