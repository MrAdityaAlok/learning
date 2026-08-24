"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import Any, List


SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one: List[Any], list_two: List[Any]) -> int:

    if list_one == list_two:
        return EQUAL

    len_one, len_two = len(list_one), len(list_two)

    if len_one < len_two:
        for i in range(len_two):
            if list_two[i : i + len_one] == list_one:
                return SUBLIST
    else:
        for i in range(len_one):
            if list_one[i : i + len_two] == list_two:
                return SUPERLIST

    return UNEQUAL
