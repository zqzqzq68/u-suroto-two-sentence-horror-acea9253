#!/usr/bin/env python3
"""Two-Sentence Horror - make.fun bounty u-suroto-two-sentence-horror-acea9253.

The program writes one horror story of exactly two sentences (at most
400 characters) to /output/entry.txt, where the sealed scorer reads it.

The story is fixed, so every run produces byte-identical output and the
run is deterministic. The dread is implied, never explained: the first
sentence states a small impossible routine, and the second sentence
reframes it - whatever has been coming in was already inside, standing
by the bed, and it never left.
"""

from __future__ import annotations

import os
import re
import sys

OUTPUT_PATH = os.environ.get("HORROR_OUTPUT", "/output/entry.txt")
MAX_CHARS = 400

STORY = (
    "Every morning I find my front door unlocked, though I lock it twice "
    "before bed and live alone. "
    "This morning there were footprints in the dust on the floorboards "
    "leading from my bed to the door, and they stopped at the inside of it."
)


def count_sentences(text: str) -> int:
    """Count sentences by terminal punctuation followed by space or end."""
    return len(re.findall(r"[.!?](?:\s|$)", text.strip()))


def validate(text: str) -> None:
    """Enforce the gate the sealed scorer checks: 1-400 chars, 2 sentences."""
    if not text.strip():
        raise ValueError("story is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"story is {len(text)} chars, over the 400 limit")
    sentences = count_sentences(text)
    if sentences != 2:
        raise ValueError(f"story has {sentences} sentences, need exactly 2")


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it holds exactly the story written.

    A silent short write or an encoding slip would fail the scorer's
    gate, so the program refuses to report success unless the bytes on
    disk match the validated story character for character.
    """
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = fh.read()
    if on_disk != expected:
        raise ValueError(
            f"readback mismatch: file holds {len(on_disk)} chars, "
            f"expected {len(expected)}"
        )


def main() -> int:
    validate(STORY)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(STORY)
    verify_written(OUTPUT_PATH, STORY)
    print(STORY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
