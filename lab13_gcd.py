# Name: Sheron Smith
# Date: October 6, 2026
# Assignment: Lab 13
# This program finds the GCD of two whole numbers. The GCD is the biggest
# number that goes into both of them evenly.
# Inputs: Two whole numbers (they can be negative)
# Output: The GCD of the two numbers

def find_gcd(m: int, n: int) -> int:
    # Takes two numbers M and N and gives back their GCD using Euclid's trick
    while m != 0:
        m, n = n % m, m  # Euclid's step, m gets smaller every time
    # Python's % can make n negative, but a GCD can't be negative, so flip it
    if n < 0:
        n = -n
    return n

def main(args: list[str]) -> int:
    # Asks for two numbers and shows their GCD
    print('This program finds the greatest common divisor (GCD)')
    print('of two whole numbers.')
    print()

    # Input
    try:
        first: int = int(input('Please enter the first whole number: '))
        second: int = int(input('Please enter the second whole number: '))
    except ValueError:
        print('Please enter whole numbers only, like 48 or -12.')
    else:
        # Process
        gcd: int = find_gcd(first, second)

        # Output
        print('The GCD of', first, 'and', second, 'is', gcd)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
