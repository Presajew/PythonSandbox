# Problem 7
#   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#   What is the 10 001st prime number?

import time


def calculate() -> int:
    prime_count = 0
    last_prime_value = 0
    index = 2
    while prime_count < 10001:
        if is_prime(index):
            prime_count += 1
            last_prime_value = index
        index += 1
    return last_prime_value


def is_prime(val) -> bool:
    for i in range(2, val):
        if val % i == 0:
            return False
    return True


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 7 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
