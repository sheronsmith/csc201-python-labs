# Name: Sheron Smith
# Date: October 1, 2026
# Assignment: Lab 12
# Find a student's class standing from their completed credit hours
# Inputs: Number of completed credit hours
# Output: The student's class standing, or an error message for bad input

def print_intro() -> None:
    # Print a short description of what the program does
    print('This program finds your class standing (freshman, sophomore,')
    print('junior, or senior) from the credit hours you have completed.')
    print()

def get_standing(hours: int) -> str:
    # Given the number of completed credit HOURS, return the class standing
    result: str = ''  # Invalid value, will be overwritten
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
    # Read completed credit hours and print the matching class standing
    MAX_HOURS: int = 200  # Constant: a degree takes about 120, so more is not realistic
    print_intro()

    # Input
    try:
        completed_hours: int = int(input('Please enter your completed credit hours: '))
        if completed_hours < 0 or completed_hours > MAX_HOURS:
            raise ValueError  # Negative or very large credit hours are not possible
    except ValueError:
        # Catches letters, blank input, decimals, and numbers out of range
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
