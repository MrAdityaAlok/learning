def primes(limit: int) -> list[int]:
    if limit < 1:
        raise ValueError("No primes below specified limit:", limit)

    prime = list(range(0, limit + 1))
    prime[1] = 0  # 1 is not a prime

    for i in range(2, limit + 1):  # iterate from 2..limit
        prime[i * 2 :: i] = [0] * len(prime[i * 2 :: i])

    return [x for x in prime if x != 0]
