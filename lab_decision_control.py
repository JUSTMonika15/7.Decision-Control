"""CSC 161 Lab: Decision Control

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


def is_valid_date(day, month, year):
    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    leap_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    if year > 0:
        y = year
    else:
        return False

    if 12 >= month > 0:
        m = month
    else:
        return False

    if is_leap_year(y) is True:
        date = leap_day[m - 1]
    else:
        date = month_day[m - 1]

    if date < day or day == 0:
        return False
    else:
        return True


def main():
    print("This program accepts a date in the form month/day/year "
          "and outputs whether or not the date is valid")
    input_str = (input("Please enter a date (mm/dd/yyyy): "))
    month, day, year = input_str.split("/")
    month, day, year = int(month), int(day), int(year)
    if is_valid_date(day, month, year) is True:
        print(input_str, "is valid")
    else:
        print(input_str, "is not valid")


if __name__ == "__main__":
    main()
