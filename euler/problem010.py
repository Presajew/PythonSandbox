"""
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

NOTE: Cool solution was to make an array of 1's and flip them to 0 for all factors of each number going up
    Find all non-primes and you are left with only primes... love it
"""

import time
from problem007 import is_prime


def calculate() -> int:
    output = 2
    for i in range(3, 2000000):

        # had to improve the efficiency by skipping all even numbers
        if i % 2 == 0:
            continue

        if is_prime(i):
            output += i

    return output


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 10 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
