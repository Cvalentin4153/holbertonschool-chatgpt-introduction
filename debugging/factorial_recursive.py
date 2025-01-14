#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Check if the user provided an argument
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <non-negative-integer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            raise ValueError("Number must be non-negative.")

        # Calculate and print factorial
        print(factorial(number))

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

