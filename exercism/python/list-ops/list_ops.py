from typing import Any, Callable, List


def append(list1: List, list2: List) -> List:
    return list1 + list2


def concat(lists: List) -> List:
    joined = []
    for item in lists:
        joined = append(joined, item)

    return joined


def filter(function: Callable[[Any], bool], list: List) -> List:
    return [item for item in list if function(item)]


def length(list: List) -> int:
    count = 0
    for _ in list:
        count += 1
    return count


def map(function: Callable[[Any], Any], list: List) -> List:
    return [function(item) for item in list]


def foldl(function: Callable[[Any, Any], Any], list: List, initial: Any) -> Any:
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function: Callable[[Any, Any], Any], list: List, initial: Any) -> Any:
    for item in reverse(list):
        initial = function(initial, item)
    return initial


def reverse(list: List) -> List:
    return [list[i] for i in range(length(list) - 1, -1, -1)]
