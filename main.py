"""Everyday Wonder, Two Days to Find the Line.

One sentence, at most 200 characters, that makes a small everyday
moment strange and new. The program writes exactly that sentence to
/output/entry.txt. Standard library only.
"""

import os

SENTENCE = (
    "A coin in last winter's coat is a tip from a version of me "
    "who knew I'd be broke in spring."
)


def main() -> None:
    text = SENTENCE.strip()
    assert "\n" not in text, "entry must be a single sentence"
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
