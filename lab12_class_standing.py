# Name: Sheron Smith
# Date: October 1, 2026
# Assignment: Lab 12
# This program tells you your class standing (freshman, sophomore, junior,
# or senior) based on how many credit hours you have.
# Inputs: How many credit hours you have done
# Output: Your class standing, or a message if you typed something wrong

def print_intro() -> None:
    # Prints a short message about what the program does
    print('This program finds your class standing (freshman, sophomore,')
    print('junior, or senior) from the credit hours you have completed.')
    print()

def get_standing(hours: int) -> str:
    # Takes the number of credit HOURS and gives back the class standing
    result: str = ''  # Empty for now, it gets filled in below
    if hours < 24:
        result = 'freshman'
    elif hours < 56:
        result = 'sophomore'
    elif hours < 87:
        result = 'junior'
    else:
        result = 'senior'
    return result

def main(args: list[str]) -> int:
    # Asks for credit hours and shows the class standing
    MAX_HOURS: int = 200  # Constant: a degree takes about 120 hours, so more than 200 doesn't make sense
    print_intro()

    # Input
    try:
        completed_hours: int = int(input('Please enter your completed credit hours: '))
        if completed_hours < 0 or completed_hours > MAX_HOURS:
            raise ValueError  # You can't have less than 0 or way too many hours
    except ValueError:
        # This catches letters, blanks, decimals, and numbers that are too big or too small
        print('Credit hours must be a whole number from 0 to ' + str(MAX_HOURS) + '.')
    else:
        # Process
        standing: str = get_standing(completed_hours)

        # Output
        print('Your class standing is:', standing)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
