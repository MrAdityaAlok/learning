from typing import List


RHYME_SUBJECT = (
    "house",
    "malt",
    "rat",
    "cat",
    "dog",
    "cow with the crumpled horn",
    "maiden all forlorn",
    "man all tattered and torn",
    "priest all shaven and shorn",
    "rooster that crowed in the morn",
    "farmer sowing his corn",
    "horse and the hound and the horn",
)

RHYME_VERB = (
    "Jack built",
    "lay in the house",
    "ate the malt",
    "killed the rat",
    "worried the cat",
    "tossed the dog",
    "milked the cow with the crumpled horn",
    "kissed the maiden all forlorn",
    "married the man all tattered and torn",
    "woke the priest all shaven and shorn",
    "kept the rooster that crowed in the morn",
    "belonged to the farmer sowing his corn",
)


FULL_RHYME = [
    f"This is the {RHYME_SUBJECT[i]} that {' that '.join(RHYME_VERB[i::-1])}."
    for i in range(len(RHYME_SUBJECT))
]


def recite(start_verse: int, end_verse: int) -> List[str]:
    return FULL_RHYME[start_verse - 1 : end_verse]


def recite2(start_verse: int, end_verse: int) -> List[str]:
    """Recite the RHYME from start_verse to end_verse"""

    return [
        f"This is the {RHYME_SUBJECT[i]} that {' that '.join(RHYME_VERB[i::-1])}."
        for i in range(start_verse - 1, end_verse)
    ]


def recite3(start_verse: int, end_verse: int) -> List[str]:

    def _recite(n: int) -> str:
        """Rescurse from nth line upto 0"""

        if n == -1:
            return ""
        return f" that {RHYME_VERB[n]}" + _recite(n - 1)

    return [
        f"This is the {RHYME_SUBJECT[i]}{_recite(i)}."
        for i in range(start_verse - 1, end_verse)
    ]
