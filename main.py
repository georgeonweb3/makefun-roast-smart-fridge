#!/usr/bin/env python3
"""Entry for make.fun "Roast the Smart Fridge: One Line, Best Laugh Wins".

Writes one line to /output/entry.txt: a roast of the smart fridge.
Gate: UTF-8 text, one line, 1 to 140 characters, not only whitespace.
Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "At 3 a.m. the fridge texted that the milk expired, then texted "
    "again: it had already told Alexa, and Alexa had already told my mother."
)


def main() -> None:
    # Gate guard: one line, 1-140 chars, no trailing newline.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 140, "entry breaks the one-line gate"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
