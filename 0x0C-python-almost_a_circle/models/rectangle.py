#!/usr/bin/python3
"""this class inherits from the base class"""
from models.base import Base

class Rectangle(Base):
    """has width and height each having its own setters and getters"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """width and height are private instances"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width
    @width.setter
    def width(self, value):
        """checks to see if width is an int and is greater than zero"""
        if type(value) != int:
            raise TypeError("width must me an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """checks to see if the height is an int and is greater than zero"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the x coordinate of the rectangle"""
        return self.__x
    @x.setter
    def x(self, value):
        """checks to see if coordinate is greater than zero"""
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y coordinate of the rectangle"""
        return self.__y
    @x.setter
    def y(self, value):
        """checks to see if y coordinate is an int and is greater than zero"""
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width*self.__height

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """returns the print and str representaion"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
