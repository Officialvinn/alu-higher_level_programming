#!/usr/bin/python3
def magic_calculation(a, b, c):
    """
    Function that behaves according to the given bytecode logic:
    - If a < b, return c
    - Else if c > b, return a + b
    - Otherwise, return (a * b) - c
    """
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
