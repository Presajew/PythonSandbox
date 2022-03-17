# Problem 3
#   The prime factors of 13195 are 5, 7, 13 and 29.
#   What is the largest prime factor of the number 600851475143 ?


def calculate(val) -> int:
    return max(get_prime_factors(val))


def get_prime_factors(val) -> list:
    factors = []
    # start at 2 since 1 can be ignored for prime factorization
    counter = 2
    while counter <= val:
        if val % counter == 0:
            factors.append(counter)
            val /= counter
        else:
            counter += 1
    print(factors)
    return factors


if __name__ == "__main__":
    print(f"The answer to Problem 3 is {calculate(600851475143)}")
