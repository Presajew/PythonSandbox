""" 
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import time

# creating a dictionary to save time on processing repetition
memory = {}

def calculate() -> int:
    largest_chain = [0, 0]
    for i in range(1, 1000000):
        chain_size = get_collatz_chain_size(i)
        if chain_size > largest_chain[1]:
            largest_chain[0] = i
            largest_chain[1] = chain_size
    return largest_chain[0]

def get_collatz_chain_size(starting_value) -> int:
    global memory

    value = starting_value
    count = 1

    while True:
        
        if value == 1:
            break
        
        memory_check = check_history(value)
        if memory_check != -1:
            count += memory_check - 1
            break
        
        value = collatz_chain(value)
        count += 1

    memory[starting_value] = count
    return count

def collatz_chain(value) -> int:
    if value % 2 == 0:
        return int(value / 2)
    else:
        return 3 * value + 1

def check_history(value) -> int:
    global memory
    if value in memory.keys():
        return memory[value]
    else:
        return -1


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 14 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")
