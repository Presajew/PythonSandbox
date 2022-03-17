# Problem 1
#   If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#   Find the sum of all the multiples of 3 or 5 below 1000.


def get_sum() -> int:

    output = 0

    # iterate through each number between 1 and 1000
    # NOTE: not inclusive of 1000
    for x in range(1, 1000):

        # check if is a factor of 3 or 5
        if (x % 3 == 0) or (x % 5 == 0):

            # increment sum
            output += x

    return output


if __name__ == "__main__":
    print(f"The answer to Problem 1 is {get_sum()}")
