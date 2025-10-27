#!/usr/bin/env python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

# Example usage
if __name__ == "__main__":
    lst = [10, 20, 30, 40]
    print(replace_in_list(lst, 2, 99))  # Output: [10, 20, 99, 40]
    print(replace_in_list(lst, -1, 50)) # Output: [10, 20, 99, 40] (unchanged)
    print(replace_in_list(lst, 10, 50)) # Output: [10, 20, 99, 40] (unchanged)
