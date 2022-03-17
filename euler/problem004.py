# Problem 4
#   A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#   Find the largest palindrome made from the product of two 3-digit numbers.


def calculate() -> int:
    output = 0
    for x in range(100, 1000):
        for y in range(100, 1000):
            test_val = x * y
            if is_palindrome(test_val) and test_val > output:
                output = test_val
                print(f"{x} x {y} = {test_val}")
    return output


def is_palindrome(val) -> bool:
    original_val = str(val)
    reverse_val = str(val)[::-1]
    return original_val == reverse_val


if __name__ == "__main__":
    print(f"The answer to Problem 4 is {calculate()}")
