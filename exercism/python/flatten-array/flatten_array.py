from typing import List


def flatten(iterable: List) -> List:
    if not isinstance(iterable, list):
        if iterable is None:
            return []
        return [iterable]

    flat = []
    for item in iterable:
        flat.extend(flatten(item))

    return flat
