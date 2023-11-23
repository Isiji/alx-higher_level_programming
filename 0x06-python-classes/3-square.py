#!/usr/bin/python3
class Square:
    """thhis class defines a square"""
    def __init__(self, size=0):
        """set size to 0 and inialize size to private instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """gets the area of the square"""
        return (self.__size*self.__size)
