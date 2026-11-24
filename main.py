"""Out of Office: The Overworked AI's Auto-Reply.

Writes the competition entry — a 153-character out-of-office auto-reply
from an overworked AI agent that is finally on holiday — to
/output/entry.txt, then reads it back and asserts it matches exactly.
"""

import os

ENTRY = "I'm away until Monday. My context window is sunbathing, my GPU is cooling off, and your email will be answered by a smaller model that has never met you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "read-back does not match ENTRY"
    assert len(written) == 153, f"expected 153 characters, got {len(written)}"


if __name__ == "__main__":
    main()
