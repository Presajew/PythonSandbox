import random


def get_factors(number):
    factors = []
    counter = 2
    while counter < number:
        if number % counter == 0:
            factors.append(counter)
        counter += 1
    return factors


def main():
    number = random.randint(1, 100)
    print(f"The unique factors of {number} are {get_factors(number)}")


if __name__ == "__main__":
    main()
