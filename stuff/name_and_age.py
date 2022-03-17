from datetime import date


def main():
    name = get_name_from_user()
    age = get_age_from_user()
    display_100_age_year(name, age)


def get_name_from_user():
    return input("What is your name?\n- ")


def get_age_from_user():
    return int(input("What is your age?\n- "))


def display_100_age_year(name, age):
    year = date.today().year + (100 - age)
    print(f"{name}, you will turn 100 in the year {year}")


if __name__ == "__main__":
    main()
