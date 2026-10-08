# Name: Sheron Smith
# Date: September 22, 2026
# Assignment: Lab 11
# Input: A day, month, and year.
# Output: Whether the three numbers make a valid Gregorian calendar date.

def leapyear(year: int) -> bool:
    # Return whether the given year is a Gregorian leap year.
    is_leap: bool = (year % 4) == 0
    if is_leap:
        is_leap = ((year % 100) != 0) or ((year % 400) == 0)
    return is_leap


def main(args: list[str]) -> int:
    # Read the day, month, and year from the user.
    day: int = int(input('Please enter the day: '))
    month: int = int(input('Please enter the month: '))
    year: int = int(input('Please enter the year: '))

    # Start by assuming the date is valid.
    valid_date: bool = True

    # Check the year, month, and lowest possible day.
    if year <= 1582:
        valid_date = False
    elif month < 1 or month > 12:
        valid_date = False
    elif day < 1:
        valid_date = False
    elif month == 2:
        # February has 29 days in a leap year and 28 days otherwise.
        if leapyear(year):
            if day > 29:
                valid_date = False
        else:
            if day > 28:
                valid_date = False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        # April, June, September, and November have 30 days.
        if day > 30:
            valid_date = False
    else:
        # The remaining months have 31 days.
        if day > 31:
            valid_date = False

    # Print the result of the date check.
    if valid_date:
        print('This is a valid date.')
    else:
        print('This is not a valid date.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
