NUMBER_TEXT = [
    "No",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
]


def _bottle_s(count: int) -> str:
    return "bottle" if count == 1 else "bottles"


def recite(start: int, take: int = 1) -> list[str]:
    if 10 < start < 1 or 10 < take < 1:
        raise ValueError("Out of the song's scope")

    song = []

    while take:
        initial_line = (
            f"{NUMBER_TEXT[start]} green {_bottle_s(start)} hanging on the wall,"
        )
        song.extend(
            (
                initial_line,
                initial_line,
                "And if one green bottle should accidentally fall,",
                f"There'll be {NUMBER_TEXT[start - 1].lower()} green {_bottle_s(start - 1)} hanging on the wall.",
            )
        )
        if take > 1:
            song.append("")

        take -= 1
        start -= 1

    return song
