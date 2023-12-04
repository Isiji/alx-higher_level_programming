#!/usr/bin/python3
"""defines a rectangle sublass square"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """represents a square"""
    def __init__(self, size):
        """instantiation of suaare"""
        self.integer_validation("size", size)
        self.__size = size
    def area(self):
        return self.__size*self.__size

