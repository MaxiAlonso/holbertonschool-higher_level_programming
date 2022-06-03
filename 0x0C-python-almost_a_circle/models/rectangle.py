#!/usr/bin/python3
"""
Rectangle Class
"""


from models.base import Base
import json


class Rectangle(Base):
    """
    Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instanitation
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get width
        """

        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Set width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get height
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Set height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get x
        """

        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Set x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get y
        """

        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Set x
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle
        """

        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle
        with the character #
        """
        for jump in range(self.__y):
            print()
        for h in range(self.__height):
            for spaces in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        part1 = f"({self.id}) {self.__x}/{self.__y}"
        part2 = f"{self.__width}/{self.__height}"
        return f"[Rectangle] {part1} - {part2}"

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:
        """

        count = 0

        if args is not None and len(args) != 0:
            for key in self.__dict__:
                if count >= len(args):
                    break
                else:
                    self.__dict__[key] = args[count]
                    count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a
        """

        dic_rec = {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y,
                }

        return dic_rec
