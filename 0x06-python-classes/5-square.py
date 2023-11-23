#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """defines the size"""
        self.__size = size

    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance:
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """returns current area"""
        return (self.__self*size.__self)

    def my_print(self):
        """prints the square with # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
        
