def rotate(text: str, key: int) -> str:
    """Rotates the given text as per the key"""

    # How does it work?
    # - find upto what index we should rotate the text
    # - create translation and then apply that.
    # - example: key = 2; i.e a -> c (1+2) and so on; thus
    # we move 'ab' to last ...

    key %= 26

    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return text.translate(
        str.maketrans(
            alphabets,
            alphabets[key:26]
            + alphabets[:key]
            + alphabets[key + 26 :]
            + alphabets[26 : 26 + key],
        )
    )


# Previous implementation.
def rotate1(text: str, key: int):
    cipher_text = ""

    for char in text:
        ordinal = ord(char)
        base = 65 if ordinal <= 91 else 97

        position = ordinal - base

        cipher_text += chr((position + key) % 26 + base) if 0 <= position < 26 else char

    return cipher_text
