""" 
Problem 13

Work out the first ten digits of the sum of the following one-hundred 
50-digit numbers.

"""

import time
import os


def calculate() -> int:
    values = get_list_of_numbers()
    summed_value = add_list_of_large_numbers(values)
    string_sum = convert_large_number_list_to_string(summed_value)
    return int(string_sum[0:10:])


def get_list_of_numbers() -> list:
    file_dir = os.path.dirname(__file__)
    file_path = os.path.join(file_dir, "problem013.txt")
    file = open(file_path, mode="r")
    output = []
    while True:
        line = file.readline()
        if line == "":
            break
        else:
            output.append(line)
    return output


def add_list_of_large_numbers(values) -> list:
    output = []
    for val in values:
        add_this = convert_large_number_to_list(val)
        output = add_two_large_number_lists(output, add_this)
    return output


def convert_large_number_to_list(value) -> list:
    output = []
    for val in str(value):
        try:
            output.append(int(val))
        except ValueError:
            continue
    return output


def add_two_large_number_lists(list1, list2) -> list:
    index = 0
    output = []
    carry_over = 0
    while True:
        index1 = len(list1) - index - 1
        index2 = len(list2) - index - 1
        if index1 >= 0 and index2 >= 0:
            value = list1[index1] + list2[index2] + carry_over
            added_value = value % 10
            carry_over = int(value / 10)
        elif index1 < 0 and index2 >= 0:
            value = list2[index2] + carry_over
            added_value = value % 10
            carry_over = int(value / 10)
        elif index2 < 0 and index1 >= 0:
            value = list1[index1] + carry_over
            added_value = value % 10
            carry_over = int(value / 10)
        else:
            if carry_over > 0:
                output.insert(0, carry_over)
            break
        output.insert(0, added_value)
        index += 1
    return output


def convert_large_number_list_to_string(values) -> str:
    output = ""
    for val in values:
        output += str(val)
    return output


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 13 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
