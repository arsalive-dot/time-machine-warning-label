"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label (at most 120 characters) to
/output/entry.txt: a genuine safety notice for a time machine,
straight-faced, with the surprise saved for the last words.
The real hazard — the butterfly effect — is the joke itself,
not named flatly: one butterfly already cost us a whole century.
"""

import os

ENTRY = (
    "WARNING: Do not step on butterflies. "
    "One already cost us the entire 21st century."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
