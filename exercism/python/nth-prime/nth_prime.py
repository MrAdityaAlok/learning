import math


FIRST_SIX_PRIME = [2, 3, 5, 7, 11, 13]


def prime(number: int):
    if number < 1:
        # message could have been better but this is needed to pass the tests.
        raise ValueError("there is no zeroth prime")

    if number <= 6:
        return FIRST_SIX_PRIME[number - 1]

    upper_bound = math.ceil(
        number * (math.log(number) + math.log(math.log(number)))
    )  # https://cs.uwaterloo.ca/journals/JIS/VOL22/Axler/axler17.pdf

    # Sieve of Eratosthenes:
    is_prime = [True] * upper_bound
    is_prime[0] = False  # 1 is not prime.

    nth_prime = 2
    count = 1
    for i in range(3, upper_bound + 1):
        if is_prime[i - 1]:
            nth_prime = i

            count += 1
            if count > number:
                break

            is_prime[i * 2 - 1 :: i] = [False] * len(is_prime[i * 2 - 1 :: i])

            # for j in range(i * 2, upper_bound + 1, i):
            #     is_prime[j - 1] = False

    return nth_prime
