#!/usr/bin/python3
"""creates a class"""
class Rectangle:
    """defines a rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialise a new rectangle"""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """completes the checks required for the width"""
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

        perimeter = (self.__height + self.__height + self.__width + self.__width)

        return perimeter
    def __str__(self):
        """Return the printable representation of the Rectangle.

        """
        a = ""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return (a.join(rect))
    def __repr__(self):
        """returns a spring representaion of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    def __del__(self):
        """print a message for any deleted instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
        
