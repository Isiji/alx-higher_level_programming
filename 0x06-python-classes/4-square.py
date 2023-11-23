#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """returns the size of the square"""
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """returns the current area of the square"""
        return (self.__size*self.__size)

