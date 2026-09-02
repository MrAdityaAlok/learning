def decode(text: str) -> str:
    decoded_str = ""
    i, text_len = 0, len(text)
    while i < len(text):
        if text[i].isnumeric():
            j = i + 1
            while j < text_len:
                if not text[j].isnumeric():
                    break
                j += 1

            if j == text_len:
                raise ValueError("Last char(s) cannot be numeric")

            decoded_str += text[j] * int(text[i:j])
            i = j + 1
        else:
            decoded_str += text[i]
            i += 1

    return decoded_str


def encode(text: str) -> str:
    encoded_str = ""
    i, text_len = 0, len(text)
    while i < text_len:
        j = i + 1
        while j < text_len:
            if text[j] != text[i]:
                break
            j += 1
        count = j - i
        if count > 1:
            encoded_str += f"{count}{text[i]}"
        else:
            encoded_str += text[i]

        i = j

    return encoded_str
