#!/usr/bin/python3
class Square:
    """initialise a class square"""
    def __init__(self, size=0):
        """set size to zero and ensure that size is an integer"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

