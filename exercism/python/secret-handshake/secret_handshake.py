from typing import List


ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> List[str]:
    flag = int(binary_str, 2)

    actions = []

    if flag & 1:
        actions.append("wink")
    if flag & 2:
        actions.append("double blink")
    if flag & 4:
        actions.append("close your eyes")
    if flag & 8:
        actions.append("jump")
    if flag & 16:
        actions.reverse()

    return actions


def commands2(binary_str: str) -> List[str]:
    flag = int(binary_str, 2)

    actions = []

    if flag & 1:
        actions.append(ACTIONS[0])
    if flag & 2:
        actions.append(ACTIONS[1])
    if flag & 4:
        actions.append(ACTIONS[2])
    if flag & 8:
        actions.append(ACTIONS[3])
    if flag & 16:
        actions.reverse()

    return actions


def commands3(binary_str: str) -> List[str]:

    i = 0
    action = []
    for flag in binary_str[::-1]:
        if flag == "1":
            if i < 4:
                action.append(ACTIONS[i])
            else:
                action.reverse()
        i += 1
    return action


def commands4(binary_str: str) -> List[str]:
    flag = int(binary_str, 2)

    actions = []
    for i in range(4):
        if flag >> i & 0b1:
            actions.append(ACTIONS[i])

    if flag >> 4 & 0b1:
        actions.reverse()

    return actions
