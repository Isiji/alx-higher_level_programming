#!/usr/bin/python3
"""this function checks if the argument is an instance"""
def is_kind_of_class(obj, a_class):
    """checks if objrct is ann instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
