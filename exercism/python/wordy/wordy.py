from enum import Enum
from dataclasses import dataclass
from typing import Generator


class ArithmeticTokenType(Enum):
    PLUS = "plus"
    MINUS = "minus"
    MULTIPLY = "multiplied"
    DIVIDE = "divided"
    NUMBER = "real_number"
    EOF = "eof"


@dataclass(frozen=True)
class ArithmeticToken:
    type: ArithmeticTokenType
    value: str | float


class ArithmeticLexer:
    def __init__(self, text: str) -> None:
        self.question_text = text

    @staticmethod
    def _is_number(string: str) -> bool:
        try:
            float(string)
            return True
        except ValueError:
            return False

    def get_token(self) -> Generator[ArithmeticToken]:
        for token in self.question_text.split():
            if ArithmeticLexer._is_number(token):
                yield ArithmeticToken(
                    type=ArithmeticTokenType.NUMBER, value=float(token)
                )
            elif token.lower() == "by":
                continue  # skip 'divided by', 'multiplied by'
            else:
                try:
                    token_type = ArithmeticTokenType(token.lower())
                except ValueError:
                    # raise ValueError("Invalid token:", token)
                    raise ValueError("unknown operation")

                yield ArithmeticToken(type=token_type, value=token_type.value)

        yield ArithmeticToken(
            type=ArithmeticTokenType.EOF, value=ArithmeticTokenType.EOF.value
        )


class ArithmeticParser:
    def __init__(self, text: str) -> None:
        self.tokens = ArithmeticLexer(text).get_token()
        self.advance()  # populate the self.current_token

    def advance(self) -> None:
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            pass

    def consume_token(self, expected_token: ArithmeticTokenType) -> None:
        if self.current_token.type != expected_token:
            raise ValueError("syntax error")
            # raise ValueError("Unexpected token:", self.current_token.value, "expected:", expected_token)
        self.advance()

    def number(self) -> int | float:
        number = self.current_token
        self.consume_token(ArithmeticTokenType.NUMBER)
        return number.value  # pyright: ignore [reportReturnType]

    def evaluate_expr(self) -> float:
        result = self.number()

        while self.current_token.type in (
            ArithmeticTokenType.PLUS,
            ArithmeticTokenType.MINUS,
            ArithmeticTokenType.MULTIPLY,
            ArithmeticTokenType.DIVIDE,
        ):
            match self.current_token.type:
                case ArithmeticTokenType.PLUS:
                    self.consume_token(ArithmeticTokenType.PLUS)
                    result += self.number()
                case ArithmeticTokenType.MINUS:
                    self.consume_token(ArithmeticTokenType.MINUS)
                    result -= self.number()
                case ArithmeticTokenType.MULTIPLY:
                    self.consume_token(ArithmeticTokenType.MULTIPLY)
                    result *= self.number()
                case ArithmeticTokenType.DIVIDE:
                    self.consume_token(ArithmeticTokenType.DIVIDE)
                    try:
                        result /= self.number()
                    except ZeroDivisionError as e:
                        raise ZeroDivisionError("Out of my limit!") from e

        return result

    def parse(self) -> float:
        result = self.evaluate_expr()

        if self.current_token.type != ArithmeticTokenType.EOF:
            # raise Exception("Unxpected end of file reached!")
            raise ValueError("syntax error")

        return result


def answer(question: str) -> float:
    actual_question = question.removesuffix("?").removeprefix("What is").strip()
    if not actual_question:
        raise ValueError("syntax error")
        # raise ValueError("You do not know how to ask a question?")

    return ArithmeticParser(actual_question).parse()
