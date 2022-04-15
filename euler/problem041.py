""" 
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
import math
import time


def calculate() -> int:
    pandigital_numbers = get_all_permutations_of_pandigital_numbers()
    pandigital_numbers.sort(reverse=True)
    for val in pandigital_numbers:
        if is_prime(val):
            return val
    return -1


def is_prime(val) -> bool:
    for i in range(2, int(math.sqrt(val) + 1)):
        if val % i == 0:
            return False
    return True


def get_all_permutations_of_pandigital_numbers() -> list:
    output = []
    for i in range(1, 10):
        digits = ""
        for j in range(1, i + 1):
            digits += str(j)
        permList = permutations(digits)
        for perm in list(permList):
            output.append(int("".join(map(str, perm))))
    return output


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 41 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
