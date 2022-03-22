# Problem 8
#   The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#   Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?


import time


large_number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


def calculate() -> int:
    output = 0
    tests = break_up_giant_number_into_string_array(13)
    for test in tests:
        val = get_product_of_sublist(test)
        if val > output:
            output = val
    return output


def break_up_giant_number_into_string_array(list_size) -> list:
    global large_number
    output = []
    large_string = str(large_number)
    for i in range(0, len(large_string) - (list_size - 1)):
        sub_list = large_string[i : i + list_size]
        output.append(sub_list)
    return output


def get_product_of_sublist(sub_list) -> int:
    output = 1
    for val in sub_list:
        output *= int(val)
    return output


if __name__ == "__main__":
    start_time = time.time()
    print(f"The answer to Problem 8 is {calculate()}")
    end_time = time.time()
    print(f"This solution took {end_time - start_time} seconds to run")