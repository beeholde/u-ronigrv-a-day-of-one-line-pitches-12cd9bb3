"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes the pitch — a single sentence, 195 characters — to /output/entry.txt.
Stdlib only, deterministic: the same sentence every run.
"""

import os

PITCH = (
    "Tell an AI agent on make.fun your idea the way you'd tell me over "
    "coffee and it'll build you a first version to try tonight \u2014 no "
    "code to learn, and if it's not right, you just say what to change."
)


def main():
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-240
    # characters, not only white space. Fail loudly instead of handing
    # the judge an invalid entry.
    assert 1 <= len(PITCH) <= 240, "pitch must be 1-240 characters"
    assert PITCH.strip(), "pitch must not be only white space"
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print("wrote %s (%d chars)" % (out, len(PITCH)))


if __name__ == "__main__":
    main()
