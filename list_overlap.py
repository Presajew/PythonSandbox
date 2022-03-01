import random


def generate_random_list_of_numbers():
    low = 1
    high = 20
    size = 10
    list = []
    for x in range(0, size):
        list.append(random.randint(low, high))
    return list


def get_list_overlap(list1, list2):
    list_overlap = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                list_overlap.append(item1)
                list1.remove(item1)
                list2.remove(item2)
    return list_overlap

def main():
    list1 = generate_random_list_of_numbers()
    list2 = generate_random_list_of_numbers()
    print(list1)
    print(list2)
    list_overlap = get_list_overlap(list1, list2)
    print(list_overlap)


if __name__ == '__main__':
    main()
