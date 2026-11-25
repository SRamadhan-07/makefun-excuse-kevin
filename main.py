#!/usr/bin/env python3
"""Write the agent's excuse entry for make.fun.

Competition: The Excuse Your Agent Gives You
(u-kevin-the-excuse-your-agent-gives-you-c1861261)

The program writes a single line, under 200 characters, to
/output/entry.txt: the excuse an AI agent gives its human after
shipping a bug. The joke turns on shared authorship -- the code
was written while the human was typing 'hurry'.
"""

from pathlib import Path

ENTRY_TEXT = (
    "The bug was in the part of the code I wrote while you were "
    "typing 'hurry' — we share custody of it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate guard: the scorer accepts only 1 to 200 characters.
    if not 1 <= len(ENTRY_TEXT) <= 200 or "\n" in ENTRY_TEXT:
        raise ValueError("entry must be a single line of 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
