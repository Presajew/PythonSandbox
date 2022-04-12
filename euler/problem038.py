""" 
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

import time


def calculate() -> int:

    # variables
    output = 0
    counter = 1
    curr_val = 1
    test_val = 1
    test_arr = []

    while True:
        # BREAK CONDITION
        # cannot be larger than a 4 digit number
        if curr_val > 10000:
            break

        # loop through numbers
        test_arr.append(curr_val * counter)

        # check if pandigital
        test_val = convert_array_into_concatenated_int(test_arr)
        if is_pandigital(test_val):
            output = test_val
            curr_val += 1
            counter = 1
            test_arr = []
            continue

        # check if can be pandigital
        if can_be_pandigital(test_val):
            counter += 1
            continue

        # if code reaches here, cannot be pandigital
        # try next number and reset
        curr_val += 1
        counter = 1
        test_arr = []

    return output


def convert_array_into_concatenated_int(values) -> int:
    output = ""
    for val in values:
        output += str(val)
    return int(output)


def is_pandigital(val) -> bool:
    # first check if val is 9 digits
    if len(str(val)) != 9:
        return False

    # verify that all digits are 1-9
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test = [int(i) for i in str(val)]
    test.sort()
    return expected == test


def can_be_pandigital(val) -> bool:
    # first check if val is less than 9
    if len(str(val)) >= 9:
        return False

    # verify no zeroes
    test = [int(i) for i in str(val)]
    if 0 in test:
        return False

    # verify all digits are unique
    return len(test) == len(set(test))


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 38 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
