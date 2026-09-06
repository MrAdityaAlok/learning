from itertools import pairwise


def proverb(*input_data: str, qualifier: None | str) -> list[str]:
    rhyme = [f"For want of a {a} the {b} was lost." for a, b in pairwise(input_data)]

    if input_data:
        rhyme.append(
            "And all for the want of a %s."
            % (f"{qualifier} {input_data[0]}" if qualifier else input_data[0])
        )

    return rhyme
