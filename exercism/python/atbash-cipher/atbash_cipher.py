import string
import textwrap


def encode(plain_text: str) -> str:
    return " ".join(
        textwrap.wrap(
            plain_text.lower().translate(
                str.maketrans(
                    string.ascii_lowercase,
                    string.ascii_lowercase[-1::-1],
                    string.punctuation + string.whitespace,
                )
            ),
            5,
        )
    )


def decode(ciphered_text: str) -> str:
    return ciphered_text.translate(
        str.maketrans(
            string.ascii_lowercase[-1::-1], string.ascii_lowercase, string.whitespace
        )
    )
