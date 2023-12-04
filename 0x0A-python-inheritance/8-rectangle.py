#!/usr/bin/python3
"""this class inherits from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """represents a class using base geometry"""
    def __init__(self, width, height):
        """initialis ea new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

