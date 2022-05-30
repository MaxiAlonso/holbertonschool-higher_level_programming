#!/usr/bin/python3
"""
Empty class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value:
        • you can assume name is always a string
        • if value is not an integer: raise a TypeError exception,
          with the message <name> must be an integer
        • if value is less or equal to 0: raise a ValueError exception
          with the message <name> must be greater than 0
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Return the area of a rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Prints [Rectangle] <width>/<height>
        """

        return (f"[{type(self).__name__}] {self.__width}/{self.__height}")


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with size
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
