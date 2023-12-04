#!/usr/bin/python3
"""this class inherits from base geometry"""
class Rectangle(BaseGeometry):
    """reps a rectsngle uding base geometry"""
def __init__(self, width, height):
    """uses integer validator"""
    super().integer_validator("width", width)
    self.__width = width
    super().integer_validator("height", height)
    self.__height = height
def area(self):
    """used to get the area"""
    return self.__height*self.__width
def __str__(self):
    """returns a string"""
    string += str(self.__width) + "/" + str(self.__height)
        return string
