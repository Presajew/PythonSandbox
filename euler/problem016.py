import math


def calculate():
	val = int(math.pow(2,1000))
	print(f"{val}: {sum_of_digits(val)}")


def sum_of_digits(val) -> int:
	# cast val as a string and split into list
	values = list(str(val))
	# return a sum of casted ints
	return sum([int(i) for i in values])


if __name__ == "__main__":
	calculate()
