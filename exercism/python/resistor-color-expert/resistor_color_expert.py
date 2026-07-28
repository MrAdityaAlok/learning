from typing import List

BAND_MAP = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

TOLERANCE_MAP = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors: List[str]) -> str:
    if len(colors) == 1:  # Only black is allowed for single value.
        return f"{BAND_MAP['black']} ohms"

    resistance = BAND_MAP[colors[0]] * 10 + BAND_MAP[colors[1]]

    if len(colors) == 5:
        resistance = resistance * 10 + BAND_MAP[colors[2]]

    resistance *= 10 ** BAND_MAP[colors[-2]]

    label = ""

    if resistance < 1e3:
        label = f"{resistance} ohms"
    elif resistance < 1e6:
        label = f"{resistance / 1000:g} kiloohms"
    elif resistance < 1e9:
        label = f"{resistance / 1000_000:g} megaohms"
    elif resistance < 1e12:
        label = f"{resistance / 1000_000_000:g} gigaohms"

    return f"{label} ±{TOLERANCE_MAP[colors[-1]]}%"
