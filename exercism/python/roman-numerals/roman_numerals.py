ROMAN = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}


# This approach is practically O(1) as roman numerals are capped at 3999.
def roman(number: int) -> str:
    roman_str = []

    place_value = 1
    while number:
        digit = number % 10

        if digit != 0:
            if digit < 5:
                if digit == 4:
                    roman_str.append(f"{ROMAN[place_value]}{ROMAN[5 * place_value]}")
                else:
                    roman_str.append(ROMAN[place_value] * digit)
            elif digit > 5:
                if digit == 9:
                    roman_str.append(f"{ROMAN[place_value]}{ROMAN[place_value * 10]}")
                else:
                    roman_str.append(
                        f"{ROMAN[5 * place_value]}{ROMAN[place_value] * (digit - 5)}"
                    )
            else:
                roman_str.append(ROMAN[5 * place_value])

        place_value *= 10

        number //= 10

    return "".join(roman_str[::-1])


if __name__ == "__main__":
    import sys

    print(roman(int(sys.argv[1])))
