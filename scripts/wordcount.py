#!/usr/bin/env python3
"""Print line, word and character counts for a text file, like wc."""

import sys


def main(argv):
    if len(argv) != 2:
        print("usage: wordcount.py FILE", file=sys.stderr)
        return 2

    filename = argv[1]
    try:
        with open(filename, "r") as handle:
            data = handle.read()
    except OSError as error:
        print("wordcount.py: %s: %s" % (filename, error.strerror), file=sys.stderr)
        return 1
    except UnicodeDecodeError as error:
        print("wordcount.py: %s: %s" % (filename, error), file=sys.stderr)
        return 1

    lines = data.count("\n")
    words = len(data.split())
    characters = len(data)
    print("%d %d %d %s" % (lines, words, characters, filename))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
