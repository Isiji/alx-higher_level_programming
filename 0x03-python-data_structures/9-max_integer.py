#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        new_list = my_list
        new_list.sort()
        max_value = new_list[-1]
        return max_value
