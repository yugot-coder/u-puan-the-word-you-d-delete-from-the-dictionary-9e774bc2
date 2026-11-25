"""Entry for make.fun: The Word You'd Delete From the Dictionary.

Writes the single word to delete from the dictionary to /output/entry.txt.

The word: "irregardless" — the dictionary's most famous non-word, a double
negative (ir- + regardless) that contradicts itself. Deleting it is the
dictionary finally correcting itself. One word, 12 characters, spelled
correctly, nothing else attached.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

WORD = "irregardless"

OUTPUT_PATH = "/output/entry.txt"

# Gate (from the competition rules): /output/entry.txt must be UTF-8 text of
# 1 to 77 characters, not only white space. The entry must be exactly one word.
MIN_CHARS = 1
MAX_CHARS = 77


def validate_entry(text):
    """Check the entry against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    """
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        problems.append(
            "entry is %d characters, must be %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        problems.append("entry is only white space")
    if len(text.split()) != 1:
        problems.append("entry must be exactly one word")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def main():
    problems = validate_entry(WORD)
    if problems:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print("wrote %r (%d chars) to %s" % (WORD, len(WORD), OUTPUT_PATH))


if __name__ == "__main__":
    main()
