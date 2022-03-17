# simple addition of all values
def add(arg, *argv):
    if not(is_int(arg)):
        return f"ERROR - {arg} was not an int"

    for a in argv:
        if not(is_int(a)):
            return f"ERROR - {a} was not an int"

    sum = arg
    for a in argv:
        sum += a
    return sum

# simple type cast check on int
def is_int(val):
    return type(val) == type(1)


if __name__ == '__main__':
    print(add(1,2,3,4,5))
