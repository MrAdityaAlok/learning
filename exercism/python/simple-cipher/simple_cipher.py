from itertools import cycle
from secrets import choice as secure_choice
from string import ascii_lowercase
from typing import Literal


class Cipher:
    BASE = ord("a")

    def __init__(self, key: str | None = None) -> None:
        self.key = (
            key if key else "".join(secure_choice(ascii_lowercase) for _ in range(100))
        )

    def _rotate(self, text: str, direction: Literal[1, -1]) -> str:
        rotated_text = []
        key_stream = cycle(self.key)

        for char in text:
            rotate_by = (ord(next(key_stream)) - Cipher.BASE) * direction
            char_index = ord(char) - Cipher.BASE

            rotated_text.append(chr((char_index + rotate_by) % 26 + self.BASE))

        return "".join(rotated_text)

    def encode(self, text: str) -> str:
        return self._rotate(text, direction=1)

    def decode(self, text: str) -> str:
        return self._rotate(text, direction=-1)
