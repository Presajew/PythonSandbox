"""
Problem 16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

"""

import math
import time


def calculate():
    val = int(math.pow(2, 1000))
    print(f"{val}: {sum_of_digits(val)}")


def sum_of_digits(val) -> int:
    # cast val as a string and split into list
    values = list(str(val))
    # return a sum of casted ints
    return sum([int(i) for i in values])


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 29 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
