"""A Day of One-Line Pitches — make.fun entry.

Writes one sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when set, for local testing). Deterministic, no network, no randomness,
no external files.
"""

import os

SENTENCE = (
    "You've been talking about that app idea for years \u2014 just describe "
    "it in plain words on make.fun and an AI agent will build the first "
    "working version for you while you watch, no coding needed."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
