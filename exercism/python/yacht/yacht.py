# Better would be to use a proper enum but then tests will fail.
# Usings set and sum is nice but it will increase CPU/Memory constraint.
# Not a problem here but I like to optimise.


YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice: list[int], category: int) -> int:
    if category == ONES:
        return 1 * dice.count(1)
    elif category == TWOS:
        return 2 * dice.count(2)
    elif category == THREES:
        return 3 * dice.count(3)
    elif category == FOURS:
        return 4 * dice.count(4)
    elif category == FIVES:
        return 5 * dice.count(5)
    elif category == SIXES:
        return 6 * dice.count(6)
    elif category == FULL_HOUSE:
        count = {}
        for v in dice:
            if v not in count and len(count) == 2:
                return 0
            count[v] = count.get(v, 0) + 1

        x, *_ = count.values()
        if x in (3, 2):
            return sum(a * b for a, b in count.items())
    elif category == FOUR_OF_A_KIND:
        count = {}
        for v in dice:
            if v not in count and len(count) == 2:
                return 0
            count[v] = count.get(v, 0) + 1

        x, *_ = count.values()
        if x in (4, 1, 5):
            return sum(a * 4 for a, b in count.items() if b >= 4)
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        if dice.count(dice[0]) == 5:
            return 50

    return 0
