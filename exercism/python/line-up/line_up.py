SUFFIX = {1: "st", 2: "nd", 3: "rd"}


def line_up(name: str, number: int) -> str:
    if 11 <= number % 100 <= 13:
        suffix = "th"
    else:
        suffix = SUFFIX.get(number % 10, "th")

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"


def line_up2(name: str, number: int) -> str:
    match number % 10:
        case 1 if number % 100 != 11:
            suffix = "st"
        case 2 if number % 100 != 12:
            suffix = "nd"
        case 3 if number % 100 != 13:
            suffix = "rd"
        case _:
            suffix = "th"

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
