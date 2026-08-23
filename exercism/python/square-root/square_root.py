import math

ACCURACY = 1e-2  # low for this question


def estimate(S: float) -> float:
    # a good estimate (According to a wikipedia article which I found here):
    # https://www.physicsforums.com/threads/seed-values-for-estimating-square-roots.445749/)

    D = math.log10(S) + 1

    is_even = D % 2 == 0
    n = (D - 1) / 2
    if is_even:
        n = (D - 2) / 2

    if is_even:
        return 6 * (10**n)
    return 2 * pow(10, n)


# Using Babylonian method.
# https://en.m.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method
def square_root(S: float) -> int:
    x = estimate(S)
    y = S / x
    while abs(x - y) > ACCURACY:
        x = (x + y) * 0.5
        y = S / x

    return int(x)  # test suite expects integer
