#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for c in str:
        if 'a' <= c <= 'z':
            new_str += chr(ord(c) - 32)
        else:
            new_str += c
    print("{}".format(new_str))
