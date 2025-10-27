#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase followed by a new line.
    """
    for c in str:
        if 'a' <= c <= 'z':  # check if lowercase
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
