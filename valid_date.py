# Name: Sheron Smith
# Date: September 22, 2026
# This program checks if a date is real.
# Input: A day, month, and year
# Output: If those numbers make a real date or not

def leapyear(year: int) -> bool:
    # Tells if the YEAR is a leap year (a year that has Feb 29)
    is_leap: bool = (year % 4) == 0
    if is_leap:
        is_leap = ((year % 100) != 0) or ((year % 400) == 0)
    return is_leap


def main(args: list[str]) -> int:
    # Ask for the day, month, and year.
    day: int = int(input('Please enter the day: '))
    month: int = int(input('Please enter the month: '))
    year: int = int(input('Please enter the year: '))

    # Start out saying the date is good.
    valid_date: bool = True

    # Check the year (our calendar started in 1582), the month, and if the day is at least 1.
    if year <= 1582:
        valid_date = False
    elif month < 1 or month > 12:
        valid_date = False
    elif day < 1:
        valid_date = False
    elif month == 2:
        # February has 29 days in a leap year and 28 days the rest of the time.
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
        # All the other months have 31 days.
        if day > 31:
            valid_date = False

    # Show if the date is real or not.
    if valid_date:
        print('This is a valid date.')
    else:
        print('This is not a valid date.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
