# Problem 6
#   Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def calculate() -> int:
    val = 100
    return squared_sum(val) - sum_of_squares(val)

def sum_of_squares(val) -> int:
    output = 0
    for x in range(1,val + 1):
        output += math.pow(x, 2)
    return int(output)

def squared_sum(val) -> int:
    output = 0
    for x in range(1, val + 1):
        output += x
    return int(math.pow(output, 2))

if __name__ == "__main__":
    print(f"The answer to Problem 6 is {calculate()}")