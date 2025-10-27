#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Creates a copy of the string with the character at position n removed.
    """
    new_str = ""
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str
