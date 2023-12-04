#!/usr/bin/python3
"""inthis class we use inheritance"""
class MyList(list):
    """mylist inherits from the list class"""
    def print_sorted(self):
        """returns a sorted list"""
        return (sorted(self))
