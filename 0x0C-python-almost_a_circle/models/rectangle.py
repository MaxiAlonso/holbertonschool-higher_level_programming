#!/usr/bin/python3
"""
Rectangle Class
"""


from models.base import Base


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

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
                - {self.__width}/{self.__height}"
