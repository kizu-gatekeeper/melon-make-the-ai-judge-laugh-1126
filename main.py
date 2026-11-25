#!/usr/bin/env python3
"""Write the office-life one-liner to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Make the AI Judge Laugh" bounty. The program
writes exactly one line of text and nothing else.

How the line targets the brief: the judge weighs a true observation
about office life, a surprising turn, and tight wording. Triple-booked
calendars are universal office truth; the turn reframes them as a
corporate translation -- the body attends the meetings while the soul
works from home -- recognition and punchline in the same breath, with
no word spent twice.
"""

import os
from pathlib import Path

LINE = "My calendar says I'm in three meetings at once, which is corporate for: my body attends, my soul works from home."

MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the line to entry.txt inside out_dir and return its path.

    The file holds exactly the line and nothing else: no trailing
    newline, no extra whitespace, so the gate sees one line of at
    most 200 chars.
    """
    if not LINE or chr(10) in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("the entry must be exactly one non-empty line within the limit")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
