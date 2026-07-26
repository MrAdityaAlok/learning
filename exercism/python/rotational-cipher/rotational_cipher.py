def rotate(text: str, key: int):
    cipher_text = ""

    for char in text:
        ordinal = ord(char)
        base = 65 if ordinal <= 91 else 97

        position = ordinal - base

        cipher_text += (
            chr((position + key) % 26 + base) if 0 <= position <= 26 else char
        )

    return cipher_text
