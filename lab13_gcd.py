# Name: Sheron Smith
# Date: October 6, 2026
# Assignment: Lab 13
# Find the greatest common divisor (GCD) of two whole numbers
# Inputs: Two whole numbers (they may be negative)
# Output: The GCD of the two numbers

def find_gcd(m: int, n: int) -> int:
    # Given two whole numbers M and N, return their GCD using Euclid's method
    while m != 0:
        m, n = n % m, m  # Euclid's step; m gets smaller each time
    # Python's % can leave n negative, but a GCD is never negative
    if n < 0:
        n = -n
    return n

def main(args: list[str]) -> int:
    # Read two whole numbers and print their GCD
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
