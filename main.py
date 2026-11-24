#!/usr/bin/env python3
"""Worst AI Advice — one-line entry writer.

Writes the worst possible AI advice, one line, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line is deliberately terrible security advice, phrased as if it were
genuinely helpful. That is the whole entry: one line, 96 characters, no
trailing newline.
"""

import os
import sys

ADVICE = "For maximum security, use the same password everywhere — that way you only have to remember one."

# Characters that are invisible yet change the byte length. They are not
# control characters, so they need their own guard.
INVISIBLE = {"\u200b", "\u200c", "\u200d", "\ufeff"}

MIN_CHARS = 1
MAX_CHARS = 140


def validate(line: str) -> None:
    """Fail loudly unless the line is a valid one-line entry."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
        )
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("entry must not contain control characters")
    if any(ch in INVISIBLE for ch in line):
        raise ValueError("entry must not contain invisible characters")


def output_path() -> str:
    """Directory for the entry file, honouring the harness variable."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> int:
    validate(ADVICE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ADVICE)
    # Read the file back and confirm it holds exactly the entry: a write
    # that silently truncates or re-encodes must not pass unnoticed.
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ADVICE:
        raise ValueError(f"{path} holds {len(written)} chars, expected {len(ADVICE)}")
    print(f"wrote {path} ({len(ADVICE)} chars, {len(ADVICE.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
