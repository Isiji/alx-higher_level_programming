#!/usr/bin/python3
"""a class of base geometry"""
def area(self):
    """used to get the area"""
    raise Exception("area() is not implemented")
def integer_validator(self, name, value):
    """valiates the value"""
    if type(value) != int:
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
