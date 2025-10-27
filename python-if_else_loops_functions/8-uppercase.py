#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.
    """
    for c in str:
        # Check if the character is lowercase
        if ord('a') <= ord(c) <= ord('z'):
            # Convert to uppercase by subtracting 32
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
