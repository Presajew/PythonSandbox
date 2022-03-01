



def isEvenOrOdd(number):
    if (number % 2 == 0):
        return 'EVEN'
    else:
        return 'ODD'


def isNumberFactorOfOtherNumber(number, divisor):
    return (number % divisor == 0)


def main():
    # test 1: is Even or Odd
    eo1 = int(input("Enter Number:\n--> "))
    print(isEvenOrOdd(eo1))

    # test 2: is divisible by 4
    print(isNumberFactorOfOtherNumber(eo1, 4))

    # test 3: are 2 numbers factors
    numb1 = int(input("Enter Number:\n--> "))
    numb2 = int(input("Enter Number:\n--> "))
    print(isNumberFactorOfOtherNumber(numb1, numb2))


if __name__ == '__main__':
    main()
