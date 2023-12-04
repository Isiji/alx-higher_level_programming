#!/usr/bin/python3
"""checks if a object is an instance of a class that inherited from a specified class"""
def inherits_from(obj, a_class):
    """returns true if the object is an instane"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
