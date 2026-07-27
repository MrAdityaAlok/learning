"""
# Algorithm proof:

1. a + b + c = sum (N)
2. a^2 + b^2 = c^2

a^2 + b^2 = (N - a - b)^2
=> 0 = N^2 - 2Na - 2Nb + 2ab
=> 0 = N^2/2 - Na - Nb + ab

Now, add N^2/2 on both the sides:

=> N^2/2 = N^2 - Na - Nb + ab
=> N^2/2 = N(N-a) - b(N-a)
=> N^2/2 = (N-b)(N-a)

let K = N^2/2, x = N - a, y = N - b

=> x.y = K

therefore, if we find all the factors of K that is integer we can get all the triplets.

## Range for `y`:

1. c > b > a > 0

b > a => N - b < N - a => y < x         --(1)
a > 0 => N - a < N => x < N             --(2)

from inequality (2):
x = N^2/2y => N^2/2y < N => N/2 < y     --(3)

from inequality (1):
y < x => y < N^2/2y => y^2 < N^2/2 => y < N/sqrt(2)     --(4)
"""


def triplets_with_sum(tripletsum: int):
    if tripletsum % 2 != 0 or tripletsum < 12:
        return []

    k = tripletsum * tripletsum // 2

    triplets = []

    for y in range(tripletsum // 2 + 1, int(tripletsum * 0.7071067811865475) + 1):
        if k % y == 0:
            x = k // y
            a, b = tripletsum - x, tripletsum - y
            triplets.append([a, b, tripletsum - a - b])

    return triplets
