from typing import List


def find(search_list: List[int], value: int) -> int:
    if not isinstance(search_list, list):
        raise ValueError("search_list is not a list")

    start = 0
    end = len(search_list) - 1

    while start <= end:
        middle = (start + end) // 2
        item = search_list[middle]

        if item == value:
            return middle

        if value > item:
            start = middle + 1
        else:
            end = middle - 1

    raise ValueError("value not in array")
