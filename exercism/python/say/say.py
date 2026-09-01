NUMBER_MAP = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

ILLIONS = [
    "",
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecillion",
    "duodecillion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septendecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion",
    "googol",
    "centillion",
    "googolplex",
]


def say(number: int) -> str:
    # although python has no limit, we need this to pass the tests.
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return NUMBER_MAP[0]

    illion_idx = 0
    num_str = ""

    while number:
        # process in a batch of 3:
        s = ""

        last_2_digits = number % 100
        if last_2_digits != 0:
            if last_2_digits in NUMBER_MAP:
                s += NUMBER_MAP[last_2_digits]
            else:
                s += f"{NUMBER_MAP[last_2_digits // 10 * 10]}-{NUMBER_MAP[last_2_digits % 10]}"

        first_digit = (number // 100) % 10
        if first_digit != 0:
            s = (
                f"{NUMBER_MAP[first_digit]} hundred {s}".rstrip()
            )  # `s` will be empty when `last_2_digits` is 0

        # then add illion:
        if s:  # skip if empty (000)
            num_str = s + " " + ILLIONS[illion_idx] + " " + num_str

        illion_idx += 1
        number //= 1000

    return num_str.rstrip()  # illion_idx = 0
