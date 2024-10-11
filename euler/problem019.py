
# Online IDE - Code Editor, Compiler, Interpreter

# Represents Monday Jan 1 1900
first_day = 0
days_in_month = {
    0: 31, # jan
    1: 28, # feb
    2: 31, # mar
    3: 30, # apr
    4: 31, # may
    5: 30, # jun
    6: 31, # jul
    7: 31, # aug
    8: 30, # sep
    9: 31, # oct
    10: 30, # nov
    11: 31, # dec
}

def is_leap_year(year):
    return (year % 100 != 0 and year % 4 == 0) or (year % 100 == 0 and year % 400 == 0)

def traverse_time():
    # start with jan = 0 (dec = 11)
    current_month = 0

def main():
    # leap year tests
    print(is_leap_year(2000))
    print(is_leap_year(1999))
    print(is_leap_year(1904))
    print(is_leap_year(1900))
        

if __name__=="__main__":
    main()
