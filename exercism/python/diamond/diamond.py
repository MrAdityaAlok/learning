import string
from typing import List

# Just to speed up lookup.
LETTER_MAP = {letter: index for index, letter in enumerate(string.ascii_uppercase)}


def rows(letter: str) -> List[str]:
    if letter == "A":
        return ["A"]

    number_of_rows = LETTER_MAP[letter] * 2 + 1
    middle_index = number_of_rows // 2

    pattern = []

    for i in range(middle_index + 1):
        t = " " * (middle_index - i) + string.ascii_uppercase[i] + " " * i
        pattern.append(t + t[middle_index - 1 :: -1])

    return pattern + pattern[-2::-1]


if __name__ == "__main__":
    import sys

    for r in rows(sys.argv[1]):
        print(r)
