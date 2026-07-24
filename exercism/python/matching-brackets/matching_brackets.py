def is_paired(input_string: str) -> bool:
    stack = []
    brackets = {"}": "{", "]": "[", ")": "("}

    for c in input_string:
        if c in brackets:  # closing bracket
            if (
                not stack or stack.pop() != brackets[c]
            ):  # opening of this is not present
                return False

        elif c in brackets.values():  # opening bracket
            stack.append(c)

    return not stack
