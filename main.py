"""One Letter for Your Day entry (make.fun program/v1).

Writes exactly one character, the letter D, to entry.txt.

The letter stands for the word behind it: "dead" -- as in "I feel dead
today." Of all the letters, D is the pick because the word it calls up
is vivid (a corpse-flat, battery-empty body), funny in the dark way
people actually joke about a hard day, and true after almost any long
day: drained, done, doomed, dead. The judge reads two letters at a
time and imagines the word behind each; D's word lands at once, and
the letter fits it exactly -- D is dead's own initial.

Deterministic: no input, no network, no randomness, no wall clock.
The output is one byte, inside the 1-to-1 character gate.
"""

import os

LETTER = "D"

# The gate allows exactly one character, no more: a trailing newline
# would make the file two characters and fail it, so the write below
# sends the letter alone, with newline="" on the file object.
assert len(LETTER) == 1 and "A" <= LETTER <= "Z"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
