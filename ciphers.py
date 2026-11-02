"""Classical substitution exercises. Never use to protect real information."""

import argparse
from collections import Counter
from pathlib import Path
import re
import string

DEMO_KEY = "ihvgwuefxjktaqlnzbmcdopsy r".replace(" ", "")


def validate_key(key):
    if len(key) != 26 or set(key) != set(string.ascii_lowercase):
        raise ValueError("Key must be a permutation of the 26 lowercase ASCII letters")


def swap_pairs(text):
    return "".join(text[i : i + 2][::-1] for i in range(0, len(text), 2))


def transform(text, key=DEMO_KEY, *, decrypt=False, modified=False):
    """Normalize to lowercase, preserve non-ASCII characters, and transform a-z.

    The modified exercise reverses the mapping after floor(length/2) characters
    and swaps adjacent character pairs. Decryption undoes swapping first.
    """
    validate_key(key)
    text = text.lower()
    if decrypt and modified:
        text = swap_pairs(text)
    midpoint = len(text) // 2
    switch = midpoint if midpoint else len(text)
    output = []
    for position, char in enumerate(text):
        active = key[::-1] if modified and position >= switch else key
        if char in string.ascii_lowercase:
            output.append(
                string.ascii_lowercase[active.index(char)]
                if decrypt
                else active[ord(char) - ord("a")]
            )
        else:
            output.append(char)
    result = "".join(output)
    return swap_pairs(result) if modified and not decrypt else result


def analyze_text(text):
    text = text.lower()
    return {
        size: Counter(re.findall(r"(?=([a-z]{" + str(size) + r"}))", text))
        for size in (2, 3)
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["encrypt", "decrypt", "analyze"])
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--modified", action="store_true")
    parser.add_argument("--key", default=DEMO_KEY)
    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8")
    if args.operation == "analyze":
        for size, counts in analyze_text(text).items():
            print(f"{size}-grams: {counts.most_common(10)}")
        return
    if args.output is None:
        parser.error("--output is required")
    if args.output.resolve() == args.input.resolve() or args.output.exists():
        parser.error("Choose a new output file; existing files are never overwritten")
    result = transform(
        text, args.key, decrypt=args.operation == "decrypt", modified=args.modified
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as handle:
        handle.write(result)


if __name__ == "__main__":
    main()
