def egg_count(display_value: int) -> int:
    count = 0
    while display_value:
        if display_value % 2 == 1:
            count += 1
        display_value //= 2

    return count
