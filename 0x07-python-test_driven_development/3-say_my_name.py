#!/usr/bin/python3
"""a function that prints first and last names"""
def say_my_name(first_name, last_name=""):
    """this names must be strings else raise a typr error"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
