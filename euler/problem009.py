# Problem 9
""" A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """

import time
import math


def calculate() -> int:
    for a in range(1, 1000):
        for b in range(1, 1000):
            if is_special_right_triangle_with_1000_sum(a, b):
                c = int(math.sqrt(math.pow(a, 2) + math.pow(b, 2)))
                print(f"Super Triangle Found\n{a} x {b} x {c}")
                return a * b * c
    return 0


def is_special_right_triangle_with_1000_sum(a, b) -> bool:
    c = 1000 - a - b
    return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 9 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
