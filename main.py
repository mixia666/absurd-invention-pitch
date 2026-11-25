#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes my one-sentence pitch for an absurd invention to
/output/entry.txt (or to the path given as argv[1]).
"""

import sys
from pathlib import Path

PITCH = (
    "Introducing the Reverse Microwave: it un-cooks last night's leftovers "
    "back into groceries, re-freezes melted ice cream solid, and turns hot "
    "coffee into a firm intention to brew a cup later."
)


def main() -> None:
    # The gate only accepts a single sentence of 1-200 characters on one
    # line: check the pitch before writing so a bad edit fails loudly
    # here, not at judging.
    assert "\n" not in PITCH and "\r" not in PITCH, "pitch must be one line"
    assert 1 <= len(PITCH) <= 200, f"pitch is {len(PITCH)} characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "pitch must be one sentence"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PITCH, encoding="utf-8")
    # The grader collects the output as a different user: keep it readable.
    out.chmod(0o644)


if __name__ == "__main__":
    main()
