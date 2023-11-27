#!/usr/bin/python3
"""shows arectangle"""
class Rectangle:
    """defines a rectangle class"""
    def __init__(self, width=0, height=0):
        """initialise a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """gets the area of the triangle"""
        area = (self.__height*self.__width)
        return area

    def perimeter(self):
        """gets the peermeter"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__height + self.__height + self.__width + self.__width)

