#!/usr/bin/python3
'''
Class Rectangle that defines a rectangle
'''


class Rectangle:
    '''
    Rectangle class
    '''

    def __init__(self, width=0, height=0):
        '''
        Initializes a rectangle
        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''
        To get the width
        '''

        return self.__width

    @width.setter
    def width(self, value):
        '''
        To set the width
        '''

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        To get the height
        '''

        return self.__height

    @height.setter
    def height(self, value):
        '''
        To set the height
        '''

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        '''
        Calculates and return the area of a rectangle
        '''

        return self.__width * self.__height

    def perimeter(self):
        '''
        Calculates and return the perimeter of a rectangle
        '''

        perimeter = 0
        if self.__width > 0 and self.__height > 0:
            perimeter = (self.__width + self.__height) * 2
        return perimeter
