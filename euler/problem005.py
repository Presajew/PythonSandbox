# Problem 5
#   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from math import factorial, prod
from problem003 import get_prime_factors


def calculate() -> int:

    scope = 20

    # get prime factorization of scope!
    factors = get_prime_factors(factorial(scope))

    # make list unique
    unique_factors = list(set(factors))

    # add factors back in for numbers with repeated factors
    for x in range(2, scope):
        append_unique_factors(unique_factors, x)

    # get product of set
    val = prod(unique_factors)

    return val


def append_unique_factors(factors, val) -> None:
    list_factors = get_prime_factors(val)
    set_factors = set(list_factors)
    for x in set_factors:
        while factors.count(x) < list_factors.count(x):
            factors.append(x)


if __name__ == "__main__":
    print(f"The answer to Problem 5 is {calculate()}")
