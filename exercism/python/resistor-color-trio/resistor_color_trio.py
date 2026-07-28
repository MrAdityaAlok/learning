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


def label(colors: List[str]) -> str:
    resistance = (BAND_MAP[colors[0]] * 10 + BAND_MAP[colors[1]]) * 10 ** BAND_MAP[
        colors[2]
    ]

    resistance_label = ""

    if resistance < 1e3:
        resistance_label = f"{resistance} ohms"
    elif resistance < 1e6:
        resistance_label = f"{resistance // 1000} kiloohms"
    elif resistance < 1e9:
        resistance_label = f"{resistance // 1000_000} megaohms"
    elif resistance < 1e12:
        resistance_label = f"{resistance // 1000_000_000} gigaohms"

    return resistance_label
