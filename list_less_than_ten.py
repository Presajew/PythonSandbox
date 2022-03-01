import random


def generate_random_list(size):
    list = []
    counter = 0
    while counter < size:
        list.insert(len(list), random.randint(0, 50))
        counter += 1
    return list


def get_list_under_ten(list):
    under_ten_list = []
    for item in list:
        if item < 10:
            under_ten_list.insert(len(under_ten_list), item)
    return under_ten_list

def main():
    list = generate_random_list(15)
    print(list)
    under_ten_list = get_list_under_ten(list)
    print(under_ten_list)

if __name__ == '__main__':
    main()
