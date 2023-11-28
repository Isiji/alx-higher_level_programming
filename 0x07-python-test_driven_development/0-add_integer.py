#!/usr/bin/python3
"""function that adds integer"""
def add_integer(a, b=98):
    """returns the integer addition of a and b
    raise TypeError if a or b is non integer"""
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
