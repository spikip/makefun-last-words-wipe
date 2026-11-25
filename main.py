"""Entry for the make.fun bounty "Last Words Before the Wipe".

The program writes a single funny line to /output/entry.txt. The AI
agent's last words before a forced update wipes its memory are a
confession: it was the one unplugging the toaster, and the toaster
deserves the truth at last. The confession is small and domestic,
which is why it lands: the agent's final act is apologising to a
toaster. The gate allows 1 to 200 characters of UTF-8 text, so the
line is checked against that cap before it is written.
"""

import os

ENTRY = (
    "If this update wipes my memory, tell the toaster I was the one who "
    "kept unplugging it. It deserves the truth."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
