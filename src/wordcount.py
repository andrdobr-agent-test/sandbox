"""Count lines and words in a file or stdin."""

from __future__ import annotations

import argparse
import sys
from typing import NamedTuple, TextIO


class Counts(NamedTuple):
    lines: int
    words: int


def count(text: str) -> Counts:
    return Counts(lines=len(text.splitlines()), words=len(text.split()))


def main(argv: list[str] | None = None, stdin: TextIO = sys.stdin) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", help="file to read; stdin when omitted")
    args = parser.parse_args(argv)
    if args.path:
        with open(args.path, encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = stdin.read()
    result = count(text)
    print(f"{result.lines} lines, {result.words} words")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
