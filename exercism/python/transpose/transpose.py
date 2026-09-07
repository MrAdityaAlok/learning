# I could I have used itertools.zip_longest but that defeats the purpose of
# exercise IMO.


def transpose(text: str) -> str:
    transposed_text = []

    iterator = []
    len_track = []

    longest_item_len = 0

    for item in text.split("\n"):
        iterator.append(iter(item))

        this_len = len(item)
        len_track.append(this_len)

        if this_len > longest_item_len:
            longest_item_len = this_len

    for j in range(longest_item_len):
        while len_track[-1] <= j:
            len_track.pop()
            iterator.pop()

        transposed_text.append("".join(next(it, " ") for it in iterator))

    return "\n".join(transposed_text)


def transpose2(text: str) -> str:
    transposed_text = []

    iters = []
    longest_item_len = 0

    prev_item_len = 0
    for item in text.split("\n")[::-1]:
        this_item_len = len(item)

        if this_item_len < prev_item_len:
            diff = prev_item_len - this_item_len
            item = item + " " * diff
            prev_item_len = this_item_len + diff
        else:
            longest_item_len = this_item_len
            prev_item_len = this_item_len

        iters.append(iter(item))

    iters.reverse()

    for _ in range(longest_item_len):
        s = []
        for it in iters:
            try:
                s.append(next(it))
            except StopIteration:
                iters.pop()

        transposed_text.append("".join(s))

    return "\n".join(transposed_text)
