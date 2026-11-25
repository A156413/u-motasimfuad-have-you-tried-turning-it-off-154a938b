"""Have You Tried Turning It Off?

Writes one funny line a hopeless tech support agent gives a desperate
customer to /output/entry.txt (the gate reads that file) and prints
exactly the same line on stdout.

The joke: the agent opens with the most classic tech-support line ever,
then immediately confesses he already tried it — twelve times — and the
bug has responded by unionizing. The cheerful uselessness is the whole
punchline: the agent did his one trick, it failed, and now the bug has
better working conditions than the customer.
"""

import os

LINE = "Have you tried turning it off and on again? I have. Twelve times. The bug is now unionized and demanding a four-day week."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts 1-199 UTF-8 characters of non-whitespace text;
    # refuse to emit a bad line rather than ship an entry that can
    # never be judged.
    assert 0 < len(LINE.strip()) <= 199, "line exceeds the gate's 199 chars"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # make.fun collects outputs as another user, so the file must be
    # readable by everyone, not just the user the program runs as.
    os.chmod(OUTPUT_PATH, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
